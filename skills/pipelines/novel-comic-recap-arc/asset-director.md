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

Read and reuse the active `visual_style.md` across the entire arc. If the user
does not supply a path, use the bundled repository default:

`styles/novel-comic-recap-arc.visual-style.md`

Use `VISUAL_STYLE_BLOCK` for scene images and `ASSET_STYLE_BLOCK` for character
reference sheets.

Current default style core:

`Modern American superhero comic-book illustration style`

Scene image prompts should preserve:

- 9:16 vertical composition with strong upper-body expression readability.
- heroic semi-realistic adult proportions, angular facial planes, strong cheekbone/jaw structure.
- thicker outer contour lines, confident interior ink lines, bold black spot shadows.
- hard-edged cel shading, high contrast, dramatic rim light, graphic painted comic colors.
- modern luxury noir palette: cold black, graphite gray, snow white, deep ocean blue, medical cold blue, old gold, ivory, blood red/fire orange/alarm red/cold silver only as accents.
- modern high-society power world: manors, private security, medical foundations, corporate Pack power, old-money interiors, hospitals/labs, ports, rain/snow/fog/night.
- mood: cold pain, public humiliation, controlled retaliation, identity reversal, dignity being taken back.

Asset reference prompts should use the short asset style:

`Modern American superhero comic-book character sheet style, prestige graphic novel cover finish, heroic semi-realistic adult proportions, angular facial planes, strong cheekbone and jaw structure, thicker outer contour lines, confident interior ink lines, bold black spot shadows, high-contrast cel shading, dramatic rim light, sculpted anatomy under tailored luxury clothing, graphic painted comic colors, subtle ink hatching, modern luxury noir palette, clearly non-photorealistic, not a photo, not live-action, not a 3D render, no anime, no manga, no Korean or Japanese webtoon, no otome-game doll face, no soft romance portrait, no delicate fashion-illustration thinness, no glossy game CG, pure white background, no text, no labels, no watermark.`

Apply these global negatives to all generated images:

- no text, subtitles, watermarks, logos, gibberish screen text;
- no wolf transformation, animal ears/tails/claws, magic circles, moon-mechanic visuals, glowing race features;
- no medieval castles, ancient costume, steampunk, cyberpunk, school youth, rural pastoral look;
- no Japanese/Korean webtoon, chibi, 3D cartoon, photorealistic live-action still, glossy game CG;
- do not render Pack as a primitive tribe or supernatural species society;
- no wrong-era clothing, buildings, vehicles, weapons, or medical equipment;
- no excessive gore, nudity, vulgar seduction, or unnecessary action-blockbuster treatment.

Use provided character references and `bible_setting.md` to write consistent character descriptors.

## Speech And Captions

- Generate narration from the approved script.
- Preserve narration script text in the artifact.
- Captions are phrase captions derived from narration/script timing.
- Do not create active word highlighting.
- Default music policy follows `visual_style.md`: no added emotional music unless the user requests it; restrained environment sound is acceptable when available.

## Quality Gate

- Narration duration fits target duration.
- Image prompts cover all planned scenes.
- Exact text is left for Remotion overlays.
- Asset manifest separates generated images, provided references, narration, and optional music.
- Missing assets are explicit blockers, not hidden assumptions.
