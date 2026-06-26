from pathlib import Path

from lib.pipeline_loader import load_pipeline


def test_novel_comic_recap_arc_pipeline_loads_and_has_skills():
    manifest = load_pipeline("novel-comic-recap-arc")

    assert manifest["name"] == "novel-comic-recap-arc"
    assert [stage["name"] for stage in manifest["stages"]] == [
        "research",
        "proposal",
        "script",
        "scene_plan",
        "assets",
        "edit",
        "compose",
        "publish",
    ]

    root = Path(__file__).resolve().parents[2]
    for skill in manifest["required_skills"]:
        if not skill.startswith("pipelines/novel-comic-recap-arc/"):
            continue
        path = root / "skills" / f"{skill}.md"
        assert path.exists(), f"Missing pipeline skill: {path}"


def test_novel_comic_recap_arc_defaults_one_arc_one_video():
    manifest = load_pipeline("novel-comic-recap-arc")
    metadata = manifest["metadata"]

    assert metadata["recap_unit"] == "one_arc_one_video"
    assert metadata["default_aspect_ratio"] == "9:16"
    assert metadata["default_language"] == "en-US"
    assert metadata["caption_highlight_mode"] == "none"
