# Executive Producer - Novel Comic Recap Arc Pipeline

## When To Use

Use this pipeline when the user provides one adapted novel arc and wants one complete English comic-recap drama video. The source pattern is usually:

- `adapt_arcXXXX.md` for arc-level design, boundaries, nodes, famous scenes, and protected future reveals.
- `ec_arcXXXX_ChN-M.md` for chapter/beat detail, key dialogue, and end-frame material.
- `bible_setting.md` and character reference assets for continuity.

## Core Contract

One arc produces one video. Chapters are source material, not output units. The video structure follows arc-level emotional escalation, not chapter order.

Default target:

- 9:16 vertical.
- 75-120 seconds, usually about 90 seconds.
- English narration for Western audiences.
- Recap style, not audiobook reading.
- Phrase captions only; no active word highlighting.
- Key dialogue appears as comic speech bubbles.
- Zero-key/local-first asset path where possible.

## EP State

Maintain these arc-specific fields across stages:

- `arc_id`
- `adapt_arc_path`
- `ec_arc_path`
- `bible_path`
- `character_reference_paths`
- `protected_future_arcs`
- `bottom_card_protections`
- `arc_start`
- `arc_landing`
- `nodes[]`
- `must_show_moments[]`
- `dialogue_candidates[]`
- `target_duration_seconds`
- `scene_budget`
- `visual_style_block`
- `render_runtime`
- `captionHighlightMode = "none"`

## Stage Order

Run stages serially:

`research -> proposal -> script -> scene_plan -> assets -> edit -> compose -> publish`

Do not generate paid or consequential assets before proposal approval. If both Remotion and HyperFrames are available, follow `AGENT_GUIDE.md` and present both before locking `render_runtime`.

## Cross-Stage Gates

After research:

- Confirm both arc files were parsed.
- Confirm protected future reveals are listed.
- Confirm all nodes were captured even if the node count is not six.

After proposal:

- Confirm the approved concept is one arc / one video.
- Confirm the duration, visual style, voice plan, image path, and render runtime.

After script:

- Confirm narration compresses the full arc.
- Confirm no protected future reveal leaks.
- Confirm every must-show node is used or intentionally merged.

After scene plan:

- Confirm scene count is dense enough: usually 8-12 scenes.
- Confirm exact text is not delegated to image generation.
- Confirm speech bubbles and captions are overlay elements.

After assets:

- Confirm narration is newly generated TTS, not audiobook audio.
- Confirm image style and character descriptors are consistent.
- Confirm any missing visuals are surfaced before compose.

After edit:

- Confirm faster pacing than a single-chapter pilot.
- Confirm `subtitles.style = "phrase"` and `captionHighlightMode = "none"`.

After compose:

- Confirm 9:16 render, audio present, duration in tolerance.
- Inspect sampled frames for black frames, incoherent overlaps, weak text, and style drift.

## Send-Back Rules

- If duration is too long or too slow, send back to script, not edit.
- If too many images are required, send back to scene_plan to merge scenes.
- If style drift appears, send back to assets with a stricter style block.
- If caption or speech bubble overlap appears, send back to edit or compose.
