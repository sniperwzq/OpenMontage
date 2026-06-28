from pathlib import Path

import pytest

from lib.novel_arc_intake import (
    NovelArcIntakeError,
    normalize_arc_id,
    resolve_novel_arc_source_bundle,
)


def test_normalize_arc_id_accepts_shortcuts():
    assert normalize_arc_id("0101") == "0101"
    assert normalize_arc_id("arc0101") == "0101"
    assert normalize_arc_id("Arc 101") == "0101"
    assert normalize_arc_id(101) == "0101"


def test_resolves_project_path_arc_bundle_and_ignores_backups(tmp_path):
    project = _make_project(tmp_path)
    _write(project / "erchuang" / "adapt_arc0101.md", "# Arc 0101")
    _write(project / "erchuang" / "adapt_arc0101_backup.md", "# old")
    _write(project / "erchuang" / "ec_arc0101_Ch1-3.md", "# Arc 0101 EC")
    _write(project / "erchuang" / "bible_setting.md", "# Bible")
    _write(project / "erchuang" / "book_title.txt", "Title")
    _write(project / "erchuang" / "stage_1_plan.md", "# Stage 1")
    for chapter in range(1, 4):
        _write(project / "novels" / f"chapter_{chapter}.txt", f"Chapter {chapter}")

    bundle = resolve_novel_arc_source_bundle(project, "arc0101")
    data = bundle.to_dict()

    assert bundle.arc_id == "0101"
    assert bundle.adapt_arc_path.name == "adapt_arc0101.md"
    assert bundle.ec_arc_path.name == "ec_arc0101_Ch1-3.md"
    assert bundle.chapter_start == 1
    assert bundle.chapter_end == 3
    assert list(bundle.chapter_text_paths) == [1, 2, 3]
    assert bundle.stage_plan_path == (
        project / "erchuang" / "stage_1_plan.md"
    ).resolve()
    assert data["source_paths"]["chapter_texts"]["1"].endswith("chapter_1.txt")
    assert data["source_uris"]["adapt_arc"].startswith("file://")


def test_resolves_padded_stage_plan_for_late_arc(tmp_path):
    project = _make_project(tmp_path)
    _write(project / "erchuang" / "adapt_arc0404.md", "# Arc 0404")
    _write(project / "erchuang" / "ec_arc0404_Ch58-61.md", "# Arc 0404 EC")
    _write(project / "erchuang" / "stage_04_plan.md", "# Stage 4")
    for chapter in range(58, 62):
        _write(project / "novels" / f"chapter_{chapter}.txt", f"Chapter {chapter}")

    bundle = resolve_novel_arc_source_bundle(project, "0404")

    assert bundle.chapter_start == 58
    assert bundle.chapter_end == 61
    assert bundle.stage_plan_path == (
        project / "erchuang" / "stage_04_plan.md"
    ).resolve()


def test_missing_chapter_text_blocks_with_specific_error(tmp_path):
    project = _make_project(tmp_path)
    _write(project / "erchuang" / "adapt_arc0101.md", "# Arc 0101")
    _write(project / "erchuang" / "ec_arc0101_Ch1-3.md", "# Arc 0101 EC")
    _write(project / "novels" / "chapter_1.txt", "Chapter 1")
    _write(project / "novels" / "chapter_3.txt", "Chapter 3")

    with pytest.raises(NovelArcIntakeError, match="chapter_2.txt"):
        resolve_novel_arc_source_bundle(project, "0101")


def test_duplicate_ec_arc_files_block(tmp_path):
    project = _make_project(tmp_path)
    _write(project / "erchuang" / "adapt_arc0101.md", "# Arc 0101")
    _write(project / "erchuang" / "ec_arc0101_Ch1-3.md", "# Arc 0101 EC")
    _write(project / "erchuang" / "ec_arc0101_Ch1-4.md", "# Arc 0101 EC alt")
    for chapter in range(1, 5):
        _write(project / "novels" / f"chapter_{chapter}.txt", f"Chapter {chapter}")

    with pytest.raises(NovelArcIntakeError, match="多个 ec arc 文件"):
        resolve_novel_arc_source_bundle(project, "0101")


def _make_project(tmp_path: Path) -> Path:
    project = tmp_path / "novel_project"
    (project / "erchuang").mkdir(parents=True)
    (project / "novels").mkdir()
    return project


def _write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
