# Research Director - Novel Comic Recap Arc Pipeline

## Purpose

Convert the user's local arc files into a schema-valid `research_brief` that carries an `arc_brief` in `metadata`. This is not web research. It is source-grounded story analysis.

## Inputs

Required when available:

- `adapt_arc*.md`
- `ec_arc*_Ch*.md`
- `bible_setting.md`
- character reference image(s)
- visual style instructions from the user, especially `visual_style.md`

## Process

### 1. Identify The Arc

Extract:

- `arc_id`
- source file paths
- arc title/topic
- start seed
- landing point
- protected future arcs
- bottom-card protections
- character mapping
- setting mapping

If file names differ, infer from headings and content. Do not assume exactly six nodes.

### 2. Parse Nodes Dynamically

From `adapt_arc`, extract every story node with:

- node id and name
- emotional dimension
- emotional core
- extreme plot expression
- famous scene
- payoff anchor
- source chapter or beat references when available
- must-show priority: `must`, `strong`, or `optional`

### 3. Parse Chapter Beats As Material

From `ec_arc`, extract:

- chapter labels
- beat-by-beat events
- key dialogue
- chapter cut points
- experience targets

Do not let chapter divisions define the video structure. Store them as supporting evidence.

### 4. Build Recap Compression Notes

Write:

- what the viewer must understand by the end
- which nodes can be merged if runtime is tight
- which dialogue lines deserve speech bubbles
- which images are likely hero frames
- what must not be spoiled from later arcs

### 5. Read Visual Style

If the user supplies a `visual_style.md`, read it. If no explicit file is
provided, check the bundled repository default:

`styles/novel-comic-recap-arc.visual-style.md`

Extract and carry forward:

- `STYLE_CORE`: default is `Modern American superhero comic-book illustration style`.
- `VISUAL_STYLE_BLOCK`: use for scene/image prompts.
- `ASSET_STYLE_BLOCK`: use for character sheets and reference assets.
- `PALETTE`, `LIGHTING`, `CAMERA_LANGUAGE`, `TEXTURE_WORLD`, `MOOD_TONE`.
- `GLOBAL_NEGATIVE`: apply to generated images.
- `SOUND_POLICY`: prefer no music or only restrained environmental sound unless the user approves otherwise.

Important: `GLOBAL_NEGATIVE` and no-text/no-logo/no-watermark restrictions apply
to generated images. The recap format may still use controlled Remotion overlay
captions and speech bubbles unless the user explicitly disables them.

### 6. Produce A Schema-Valid `research_brief`

Use local source paths as citations. The generic research schema requires landscape/data/audience fields; adapt them as follows:

- `landscape.existing_content`: list the supplied source modules and what each contributes.
- `data_points`: list concrete story facts, each cited to a local file URI.
- `audience_insights`: describe Western short-form romance/revenge recap expectations.
- `angles_discovered`: create three treatment angles for the same arc.
- `sources`: cite `adapt_arc`, `ec_arc`, `bible_setting`, character refs, and user visual style when present.

Store the detailed source analysis under:

```json
"metadata": {
  "arc_brief": {
    "episode_unit": "arc",
    "arc_id": "...",
    "source_paths": {},
    "protected_future_arcs": [],
    "bottom_card_protections": [],
    "nodes": [],
    "chapter_beats": [],
    "must_show_moments": [],
    "dialogue_candidates": [],
    "hero_frame_candidates": [],
    "compression_notes": [],
    "visual_style": {
      "source_path": "...",
      "style_core": "Modern American superhero comic-book illustration style",
      "visual_style_block": "...",
      "asset_style_block": "...",
      "global_negative": "...",
      "sound_policy": "none_or_minimal_environment_only"
    }
  }
}
```

## Quality Gate

- Every node in `adapt_arc` is represented.
- Protected future material is explicit.
- Key dialogue is quoted only as short snippets.
- The active visual style file is summarized and stored in metadata when present.
- No unsupported story invention enters the brief.
