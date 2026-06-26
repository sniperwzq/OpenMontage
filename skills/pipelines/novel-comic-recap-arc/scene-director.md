# Scene Director - Novel Comic Recap Arc Pipeline

## Purpose

Convert the arc script into a dense 9:16 comic-panel scene plan. The output is a schema-valid `scene_plan`.

## Scene Budget

Default:

- 75-90 seconds: 8-10 scenes.
- 90-120 seconds: 10-12 scenes.
- If the arc has fewer nodes, add hook/landing/insert scenes.
- If the arc has many nodes, merge weaker nodes visually while preserving all must-show turns.

## Scene Planning Rules

- One scene should carry one emotional job.
- Do not bake subtitles or speech-bubble text into generated images.
- Use Remotion overlays for captions, bubbles, warning tape, title cards, and small readable text.
- Favor strong stills with camera motion over many weak images.
- Keep vertical-safe composition: important faces and text away from platform UI zones.
- Follow the active `visual_style.md`: vertical power staging, centered or triangular group composition, clear upper-body expressions, low angles for power pressure, high angles for trapped/scrutinized characters, symmetrical public spaces, oppressive foreground framing for private conflict, slow push-in/orbit/frozen-stare motion.
- Use the visual style's modern high-society world: Pack as old-money/corporate power, private security, medical foundations, manors, black business cars, closed rooms, cold family insignia. Do not introduce tribal, medieval, magical, or overt werewolf transformation visuals.

## Required Scene Metadata

For every scene, include:

- script section id,
- covered arc node(s),
- visual purpose,
- image prompt intent,
- character presence,
- speech bubble overlay if any,
- camera motion,
- safe-zone note,
- whether it is a hero frame.

Store arc-specific details in `scene_plan.metadata`:

```json
"metadata": {
  "pipeline": "novel-comic-recap-arc",
  "arc_id": "...",
  "episode_unit": "arc",
  "aspect_ratio": "9:16",
  "scene_budget": 10,
  "node_to_scene_map": {},
  "speech_bubble_plan": [],
  "visual_style_source": "...",
  "style_core": "Modern American superhero comic-book illustration style",
  "caption_style": "phrase",
  "captionHighlightMode": "none"
}
```

## Required Asset Planning

Use `required_assets` on each scene:

- `type`: usually `image`, `audio`, `overlay`, or `music`
- `description`: production-ready description
- `source`: `generate`, `provided`, or `source`

Generated image descriptions must be visual-only. Put exact words in overlay notes.

## Quality Gate

- Scene count is dense enough for a full arc.
- The strongest arc moments get the strongest frames.
- Scene descriptions are specific enough for consistent image generation.
- Text overlays are separated from image generation.
