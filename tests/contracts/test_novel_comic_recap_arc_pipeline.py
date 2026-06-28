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
    style_path = Path(metadata["default_visual_style_path"])
    assert not style_path.is_absolute()
    assert style_path.as_posix() == "styles/novel-comic-recap-arc.visual-style.md"
    assert (Path(__file__).resolve().parents[2] / style_path).exists()
    assert (
        metadata["default_image_style_core"]
        == "Modern American superhero comic-book illustration style"
    )
    assert metadata["default_music_policy"] == "none_or_minimal_environment_only"


def test_novel_comic_recap_arc_declares_project_path_intake():
    manifest = load_pipeline("novel-comic-recap-arc")
    source_intake = manifest["metadata"]["source_intake"]

    assert source_intake["mode"] == "novel_project_path_plus_arc_id"
    assert source_intake["required_input_fields"] == ["novel_project_path", "arc_id"]
    assert source_intake["erchuang_dir_name"] == "erchuang"
    assert source_intake["novels_dir_name"] == "novels"
    assert source_intake["resolver"] == (
        "lib.novel_arc_intake.resolve_novel_arc_source_bundle"
    )
