# Edit Director - Novel Comic Recap Arc Pipeline

## Purpose

Turn the scene plan and assets into a fast edit decision list for one complete arc recap. The output is a schema-valid `edit_decisions`.

## Timing Rules

Default arc pacing:

- Hook: 3-5 seconds.
- Main nodes: 7-12 seconds each, depending on node count.
- Highest betrayal/status scenes may get 10-14 seconds.
- Final landing/cliffhanger: 8-12 seconds.

If the cut feels like a single-chapter pilot, tighten it. The viewer should feel the arc moving.

## Caption Rules

Use phrase captions:

- `style`: `phrase`
- `captionHighlightMode`: `none`
- 4-7 words per line for vertical video.
- Bottom-center unless the scene's face/action requires repositioning.

Do not use karaoke or active-word captions by default.

## Speech Bubble Rules

- Use 3-6 speech bubbles total.
- Keep each bubble short.
- Do not display a bubble and a dense caption over the same face/action.
- Bubbles should land on commands, humiliations, or decisions.

## Edit Artifact Requirements

Include:

- scene cuts with start/end times,
- image source per cut,
- camera motion per cut,
- overlay schedule,
- speech bubble schedule,
- subtitle config,
- narration audio layout,
- optional music layout,
- `render_runtime` copied from the approved proposal.

Add metadata:

```json
"metadata": {
  "pipeline": "novel-comic-recap-arc",
  "arc_id": "...",
  "episode_unit": "arc",
  "pacing_mode": "fast_arc_recap",
  "captionHighlightMode": "none",
  "node_coverage": []
}
```

## Quality Gate

- Duration matches approved target within tolerance.
- Every major arc turn appears in the timeline.
- Overlay density is controlled.
- Render runtime matches the proposal; do not silently swap engines.
