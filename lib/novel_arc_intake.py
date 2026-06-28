"""解析小说项目里的单个 Arc 输入，供漫画解说 pipeline 使用。

这里刻意只做确定性的本地文件解析：把小说项目根目录和 arc_id 转换成
一组已存在的源文件路径。故事判断、压缩取舍和创意决策仍由 pipeline
director skills 负责。
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class NovelArcIntakeError(ValueError):
    """小说 Arc 源文件包无法解析时抛出。"""


_ARC_ID_RE = re.compile(r"^(?:arc)?[\s_-]*(\d{1,4})$", re.IGNORECASE)
_EC_ARC_RE = re.compile(
    r"^ec_arc(?P<arc_id>\d{4})_Ch(?P<start>\d+)-(?P<end>\d+)\.md$"
)
_CHAPTER_RE = re.compile(r"^chapter_(?P<number>\d+)\.txt$", re.IGNORECASE)
_IMAGE_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".webp"}


@dataclass(frozen=True)
class NovelArcSourceBundle:
    """单个二创 Arc 已解析出的源文件路径集合。"""

    novel_project_path: Path
    arc_id: str
    erchuang_dir: Path
    novels_dir: Path
    adapt_arc_path: Path
    ec_arc_path: Path
    chapter_start: int
    chapter_end: int
    chapter_text_paths: dict[int, Path]
    bible_path: Path | None = None
    book_title_path: Path | None = None
    stage_plan_path: Path | None = None
    visual_style_path: Path | None = None
    character_reference_paths: tuple[Path, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        """返回可写入 artifact metadata 的 JSON 友好结构。"""

        source_paths: dict[str, Any] = {
            "novel_project_path": str(self.novel_project_path),
            "erchuang_dir": str(self.erchuang_dir),
            "novels_dir": str(self.novels_dir),
            "adapt_arc": str(self.adapt_arc_path),
            "ec_arc": str(self.ec_arc_path),
            "chapter_texts": {
                str(number): str(path)
                for number, path in sorted(self.chapter_text_paths.items())
            },
        }
        optional_paths = {
            "bible_setting": self.bible_path,
            "book_title": self.book_title_path,
            "stage_plan": self.stage_plan_path,
            "visual_style": self.visual_style_path,
        }
        for key, path in optional_paths.items():
            if path is not None:
                source_paths[key] = str(path)
        if self.character_reference_paths:
            source_paths["character_references"] = [
                str(path) for path in self.character_reference_paths
            ]

        return {
            "arc_id": self.arc_id,
            "episode_unit": "arc",
            "source_paths": source_paths,
            "source_uris": _source_uris(source_paths),
            "chapter_range": {
                "start": self.chapter_start,
                "end": self.chapter_end,
            },
        }


def normalize_arc_id(arc_id: str | int) -> str:
    """把 ``0101``、``arc0101`` 等用户输入统一为四位 arc id。"""

    raw = str(arc_id).strip()
    match = _ARC_ID_RE.fullmatch(raw)
    if not match:
        raise NovelArcIntakeError(
            f"无效 arc_id：{arc_id!r}；应使用类似 '0101' 的四位数字，"
            "或类似 'arc0101' 的前缀形式。"
        )
    return match.group(1).zfill(4)


def resolve_novel_arc_source_bundle(
    novel_project_path: str | Path,
    arc_id: str | int,
) -> NovelArcSourceBundle:
    """解析 ``novel-comic-recap-arc`` research 阶段需要的本地文件。

    期望的小说项目结构：

    - ``<project>/erchuang/adapt_arcXXXX.md``
    - ``<project>/erchuang/ec_arcXXXX_ChN-M.md``
    - ``<project>/novels/chapter_N.txt``，覆盖 ec 文件名中的章节范围
    """

    normalized_arc_id = normalize_arc_id(arc_id)
    project_path = Path(novel_project_path).expanduser()
    if not project_path.is_dir():
        raise NovelArcIntakeError(f"小说项目路径不存在：{project_path}")
    project_path = project_path.resolve()

    erchuang_dir = project_path / "erchuang"
    novels_dir = project_path / "novels"
    if not erchuang_dir.is_dir():
        raise NovelArcIntakeError(f"缺少 erchuang 目录：{erchuang_dir}")
    if not novels_dir.is_dir():
        raise NovelArcIntakeError(f"缺少 novels 目录：{novels_dir}")

    adapt_arc_path = erchuang_dir / f"adapt_arc{normalized_arc_id}.md"
    if not adapt_arc_path.is_file():
        raise NovelArcIntakeError(f"缺少 adapt arc 文件：{adapt_arc_path}")

    ec_arc_path, chapter_start, chapter_end = _resolve_ec_arc(
        erchuang_dir, normalized_arc_id
    )
    chapter_text_paths = _resolve_chapter_texts(novels_dir, chapter_start, chapter_end)

    stage_number = int(normalized_arc_id[:2])
    return NovelArcSourceBundle(
        novel_project_path=project_path,
        arc_id=normalized_arc_id,
        erchuang_dir=erchuang_dir.resolve(),
        novels_dir=novels_dir.resolve(),
        adapt_arc_path=adapt_arc_path.resolve(),
        ec_arc_path=ec_arc_path.resolve(),
        chapter_start=chapter_start,
        chapter_end=chapter_end,
        chapter_text_paths=chapter_text_paths,
        bible_path=_optional_file(erchuang_dir / "bible_setting.md"),
        book_title_path=_optional_file(erchuang_dir / "book_title.txt"),
        stage_plan_path=_resolve_stage_plan(erchuang_dir, stage_number),
        visual_style_path=_resolve_visual_style(project_path, erchuang_dir),
        character_reference_paths=_resolve_character_reference_paths(
            project_path, erchuang_dir
        ),
    )


def _resolve_ec_arc(erchuang_dir: Path, arc_id: str) -> tuple[Path, int, int]:
    matches: list[tuple[Path, int, int]] = []
    for path in sorted(erchuang_dir.glob(f"ec_arc{arc_id}_Ch*.md")):
        match = _EC_ARC_RE.fullmatch(path.name)
        if not match:
            continue
        start = int(match.group("start"))
        end = int(match.group("end"))
        if start > end:
            raise NovelArcIntakeError(
                f"ec arc 文件名中的章节范围无效：{path.name}"
            )
        matches.append((path, start, end))

    if not matches:
        raise NovelArcIntakeError(
            f"在 {erchuang_dir} 中找不到匹配 ec_arc{arc_id}_ChN-M.md 的 ec arc 文件"
        )
    if len(matches) > 1:
        names = ", ".join(path.name for path, _, _ in matches)
        raise NovelArcIntakeError(
            f"arc {arc_id} 找到多个 ec arc 文件，无法自动选择：{names}"
        )
    path, start, end = matches[0]
    return path, start, end


def _resolve_chapter_texts(
    novels_dir: Path,
    chapter_start: int,
    chapter_end: int,
) -> dict[int, Path]:
    chapter_index = _index_chapter_files(novels_dir)
    missing = [
        number
        for number in range(chapter_start, chapter_end + 1)
        if number not in chapter_index
    ]
    if missing:
        missing_names = ", ".join(f"chapter_{number}.txt" for number in missing)
        raise NovelArcIntakeError(
            f"{novels_dir} 中缺少章节正文文件：{missing_names}"
        )
    return {
        number: chapter_index[number].resolve()
        for number in range(chapter_start, chapter_end + 1)
    }


def _index_chapter_files(novels_dir: Path) -> dict[int, Path]:
    indexed: dict[int, Path] = {}
    for path in sorted(novels_dir.glob("chapter_*.txt")):
        match = _CHAPTER_RE.fullmatch(path.name)
        if not match:
            continue
        number = int(match.group("number"))
        existing = indexed.get(number)
        if (
            existing is None
            or _chapter_file_preference(path) < _chapter_file_preference(existing)
        ):
            indexed[number] = path
    return indexed


def _chapter_file_preference(path: Path) -> tuple[int, str]:
    """优先选择不补零的章节名，其次是更短的补零名，最后按字典序。"""

    match = _CHAPTER_RE.fullmatch(path.name)
    digits = match.group("number") if match else path.stem
    return (len(digits), path.name)


def _resolve_stage_plan(erchuang_dir: Path, stage_number: int) -> Path | None:
    candidate_names = [
        f"stage_{stage_number}_plan.md",
        f"stage_{stage_number:02d}_plan.md",
    ]
    for name in candidate_names:
        path = erchuang_dir / name
        if path.is_file():
            return path.resolve()
    return None


def _resolve_visual_style(project_path: Path, erchuang_dir: Path) -> Path | None:
    for path in (
        erchuang_dir / "visual_style.md",
        project_path / "visual_style.md",
    ):
        if path.is_file():
            return path.resolve()
    return None


def _resolve_character_reference_paths(
    project_path: Path,
    erchuang_dir: Path,
) -> tuple[Path, ...]:
    candidate_dirs = (
        erchuang_dir / "character_refs",
        erchuang_dir / "characters",
        project_path / "character_refs",
        project_path / "characters",
        project_path / "reference_images",
    )
    paths: list[Path] = []
    for directory in candidate_dirs:
        if not directory.is_dir():
            continue
        for path in sorted(directory.iterdir()):
            if path.is_file() and path.suffix.lower() in _IMAGE_SUFFIXES:
                paths.append(path.resolve())
    return tuple(paths)


def _optional_file(path: Path) -> Path | None:
    return path.resolve() if path.is_file() else None


def _source_uris(source_paths: dict[str, Any]) -> dict[str, Any]:
    uris: dict[str, Any] = {}
    for key, value in source_paths.items():
        if isinstance(value, dict):
            uris[key] = {item_key: Path(item).as_uri() for item_key, item in value.items()}
        elif isinstance(value, list):
            uris[key] = [Path(item).as_uri() for item in value]
        else:
            uris[key] = Path(value).as_uri()
    return uris
