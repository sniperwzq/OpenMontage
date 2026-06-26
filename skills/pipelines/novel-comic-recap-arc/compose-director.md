# Compose Director - Novel Comic Recap Arc Pipeline

## Purpose

Render the approved arc recap into a 9:16 MP4 with narration, phrase captions, speech bubbles, and comic-panel motion.

## Runtime Routing

Read `edit_decisions.render_runtime` first. It must match the runtime locked in `proposal_packet.production_plan.render_runtime`.

Recommended default for this format is Remotion, but do not silently switch runtimes. If the approved runtime fails, surface the blocker and wait for user approval before changing path.

## Remotion Composition Rules

For Remotion/Explainer-style composition:

- Copy or symlink generated images and audio into `remotion-composer/public/<project>/`.
- Build props at `remotion-composer/public/demo-props/<project>.json`.
- Use 9:16 output settings.
- Use `anime_scene` or equivalent still-led scene components.
- Use speech-bubble overlays for key dialogue.
- Use phrase captions with `"captionHighlightMode": "none"`.

Required props-level flags:

```json
{
  "captionHighlightMode": "none",
  "metadata": {
    "pipeline": "novel-comic-recap-arc",
    "episode_unit": "arc",
    "video_language": "en-US"
  }
}
```

## Text Safety

- Do not rely on AI-generated images for exact text.
- Captions, bubbles, title cards, warning labels, and readable UI text should be rendered by Remotion.
- Check that captions and speech bubbles do not cover faces or key action.

## Validation

Before final delivery:

- run composition validation when available,
- render or inspect sampled frames,
- verify output with ffprobe,
- confirm audio stream exists,
- confirm duration is within approved tolerance,
- confirm no black/blank frames,
- confirm style consistency across scenes.

## Output

Produce:

- `render_report`
- `final_review`
- final MP4 path under `projects/<project>/renders/`

## Quality Gate

- One arc video is complete and watchable.
- Captions are not word-highlighted.
- Frame samples show coherent 9:16 composition.
- Final review notes any remaining risks.
