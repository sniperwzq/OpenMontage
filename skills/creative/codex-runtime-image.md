# Codex Runtime Image Bridge

Use this skill when a project needs generated still images but no configured
OpenMontage image provider is available, and the active agent runtime can create
images through Codex.

## What This Is

Codex runtime image generation is agent-mediated. It is not a local Python API
and it is not discoverable by `image_selector`.

The bridge has two steps:

1. The agent creates an image through the active Codex runtime image tool.
2. The agent saves the resulting file and imports it with `codex_image_import`.

After import, the image is a normal OpenMontage asset. Edit and compose stages
consume it through `asset_manifest.assets[]` like any other image.

## When To Use

Use this path when all are true:

- The user explicitly accepts Codex runtime images, or no API-key image provider
  is configured and the user wants a zero-key still-image workflow.
- The visual can be represented as a still image animated later by Remotion,
  HyperFrames, or FFmpeg.
- A human or agent can inspect the sample before batch generation.

Do not use it for:

- unattended batch generation,
- API-style provider routing through `image_selector`,
- exact text rendering inside the image,
- scenes requiring real video generation rather than still-image animation.

## Required Communication

Before generating the first sample, say:

- provider: `codex_runtime_external`
- local import tool: `codex_image_import`
- whether this is a sample or a batch
- that OpenMontage cannot call Codex image generation from Python
- that the resulting image will be imported as an external generated asset

Do not batch until the user approves one representative visual sample.

## Asset Workflow

For each approved image:

1. Save the generated image under the project workspace, preferably:
   `projects/<project>/assets/images/<asset_id>.png`
2. Run `codex_image_import` with:
   - `source_path`
   - `project_dir`
   - `asset_id`
   - `scene_id`
   - `prompt`
   - `generation_summary`
3. Add `result.data.asset_entry` to `asset_manifest.assets[]`.
4. Verify the referenced path exists.

Expected asset entry shape:

```json
{
  "id": "scene-001-keyframe",
  "type": "image",
  "path": "assets/images/scene-001-keyframe.png",
  "source_tool": "codex_image_import",
  "scene_id": "scene-001",
  "subtype": "codex_runtime_generated",
  "provider": "codex_runtime",
  "model": "codex-runtime-image-tool",
  "prompt": "Prompt used in the Codex runtime",
  "generation_summary": "Generated through Codex runtime and imported for local composition.",
  "cost_usd": 0.0
}
```

## Quality Gate

- The image file exists on disk.
- The prompt is stored in the asset entry.
- The image matches the approved style direction.
- The asset id is stable and referenced by edit decisions.
- The plan states that Codex runtime image generation is not cost-tracked by
  OpenMontage's local cost estimator.

## Composition Notes

For image-based animation, import 2-3 related stills per scene and let the edit
stage animate them with crossfade, parallax, camera motion, or panel movement.
The imported stills are normal image assets after this stage.
