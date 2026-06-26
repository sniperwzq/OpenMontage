# Script Director - Novel Comic Recap Arc Pipeline

## Purpose

Write one fast English narrator script for the complete arc. The result is a schema-valid `script` artifact.

## Pacing Defaults

- 75 seconds: 180-220 English words.
- 90 seconds: 230-270 English words.
- 120 seconds: 300-360 English words.
- Use short spoken sentences: usually 6-12 words.
- Avoid exposition about lore unless it changes the betrayal, status, or stakes.

## Structure

Use this shape, adapting to the node count:

1. `hook`: 0-4 seconds, one brutal premise.
2. `setup`: only enough context to understand the first betrayal.
3. `node_*`: one compressed section per major arc node, or merged sections when the arc has too many nodes.
4. `turn`: the moment the heroine stops explaining away the betrayal.
5. `arc_landing`: the arc's complete emotional landing.
6. `cliffhanger`: next-arc curiosity without spoiling protected material.

## Writing Rules

- Treat `adapt_arc` as the truth for arc start, landing, protected boundaries, and node intent.
- Treat `ec_arc` as beat/detail/dialogue material.
- Do not narrate chapter-by-chapter unless the arc structure itself demands it.
- Do not write audiobook prose.
- Do not include long direct quotes.
- Use high-clarity Western romance/revenge recap language.
- Keep names pronounceable and consistent with `bible_setting.md`.

## Dialogue Bubble Selection

Select 3-6 short lines for speech bubbles. Prefer:

- commands that reveal betrayal,
- humiliating public lines,
- child rejection lines,
- final controlling threat,
- heroine's quiet decision line.

Speech bubbles are not subtitles. They should be sparse and dramatic.

## Output Requirements

Produce schema-valid `script`:

- `version: "1.0"`
- `title`
- `total_duration_seconds`
- `sections[]`

Add metadata:

```json
"metadata": {
  "pipeline": "novel-comic-recap-arc",
  "arc_id": "...",
  "video_language": "en-US",
  "episode_unit": "arc",
  "target_audience": "Western romance/revenge short-form viewers",
  "word_count": 0,
  "node_coverage": [],
  "merged_nodes": [],
  "dialogue_bubbles": [],
  "protected_future_arcs": [],
  "caption_style": "phrase",
  "captionHighlightMode": "none"
}
```

## Quality Gate

- The arc feels complete.
- The pace is faster than the single-chapter pilot.
- Every must-show node appears or is intentionally merged.
- No protected future reveal leaks.
- The last section creates next-arc desire without making this arc feel unfinished.
