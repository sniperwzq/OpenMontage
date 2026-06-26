# Asset Director - Novel Comic Recap Arc Pipeline

## Purpose

Create or organize narration, comic stills, and optional music for one arc recap. The output is a schema-valid `asset_manifest`.

## Provider Policy

Default to zero-key/local-first:

- Use generated TTS through `tts_selector`; prefer local/free voices when acceptable.
- Do not use existing audiobook audio.
- Use the Codex runtime image flow when the user asks for Codex drawing.
- Use `codex_image_import` to register externally created Codex images into OpenMontage.
- If image generation is unavailable, list the exact missing images before attempting a different provider.

Before using any generation tool, read its Layer 3 skill if declared by the registry.

## Image Strategy

Produce arc-level reusable visuals, not one image per sentence.

Default image count:

- 8-10 images for 75-90 seconds.
- 10-12 images for 90-120 seconds.

For each image, carry:

- `scene_id`
- `covered_nodes`
- `character_descriptors`
- `style_block`
- `negative_style_block`
- `source_reference_paths`
- `prompt`
- `provider`
- `model`
- `resolution`
- `generation_summary`

## Style Consistency

Reuse a single style block across the entire arc. For the user's current format, preserve:

`2D American comic illustration style, Western romance comic tone, clean confident ink line art, cel shading, painted comic colors, hard-edged comic shadows, modern luxury noir mood, restrained high-society palette, simplified texture, clearly non-photorealistic, not a photo, not live-action, not a 3D render, no photorealistic skin pores, no anime, no manga, no Korean or Japanese webtoon, no otome-game doll face`

Use provided character references and `bible_setting.md` to write consistent character descriptors.

## Speech And Captions

- Generate narration from the approved script.
- Preserve narration script text in the artifact.
- Captions are phrase captions derived from narration/script timing.
- Do not create active word highlighting.

## Quality Gate

- Narration duration fits target duration.
- Image prompts cover all planned scenes.
- Exact text is left for Remotion overlays.
- Asset manifest separates generated images, provided references, narration, and optional music.
- Missing assets are explicit blockers, not hidden assumptions.
