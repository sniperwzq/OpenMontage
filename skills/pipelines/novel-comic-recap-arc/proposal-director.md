# Proposal Director - Novel Comic Recap Arc Pipeline

## Purpose

Turn the `research_brief.metadata.arc_brief` into an approved production plan for one arc / one video.

## Process

### 1. Confirm Production Shape

State plainly:

- one arc becomes one complete recap video,
- chapters are source material,
- target duration is 75-120 seconds unless the user overrides,
- narration is English for Western audiences,
- the video is recap drama, not audiobook reading.

### 2. Offer Three Concept Options

All options cover the full arc. Vary only the treatment:

- hook framing,
- emotional emphasis,
- compression strategy,
- visual density,
- ending cliffhanger angle.

Examples:

- betrayal-first hook,
- cold-revenge hook,
- identity-humiliation hook.

Do not propose "one video per chapter" unless the user explicitly requests it.

### 3. Present Runtime Options

Follow `AGENT_GUIDE.md` exactly. If both Remotion and HyperFrames are available, present both before locking `render_runtime`.

Recommended default for this format:

- Remotion for still-led comic panels, Ken Burns motion, speech bubbles, captions, and audio.

Honest tradeoff:

- HyperFrames can work for HTML/GSAP kinetic typography, but this format benefits from the existing Remotion scene stack and speech-bubble/caption control.

### 4. Lock The Production Plan

The selected concept should normally use:

- `target_duration_seconds`: about 90
- `renderer_family`: `animation-first`
- `render_runtime`: user-approved runtime, normally `remotion`
- `delivery_promise.promise_type`: `motion_led`
- `delivery_promise.motion_required`: `false`
- `delivery_promise.approved_fallback`: `still_led`
- `music_source.source_type`: `none`, `user_library`, or approved local/free source
- `voice_selection`: local/free TTS first, unless user approves another provider

### 5. Approval Gate

Do not proceed to script/assets until the user approves the concept and runtime.

## Proposal Content Requirements

Include:

- title options,
- target duration,
- node coverage summary,
- image count estimate,
- TTS path,
- caption style: phrase captions, no word highlighting,
- speech bubble count: usually 3-6,
- cost estimate with zero-key path first.

## Quality Gate

- `production_plan.pipeline` is `novel-comic-recap-arc`.
- Proposal covers the full arc.
- Runtime selection is auditable in `decision_log`.
- Cost and API-key assumptions are explicit.
