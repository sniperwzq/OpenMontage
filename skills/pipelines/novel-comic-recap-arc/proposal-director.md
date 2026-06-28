# Proposal Director - 小说漫画解说 Arc Pipeline

## 目标

把 `research_brief.metadata.arc_brief` 转换成一个可供用户批准的生产方案。核心约束是：一个 Arc 产出一个完整视频。

## 流程

### 1. 确认生产形态

先明确说明：

- 一个 Arc 变成一个完整 recap video。
- 章节只是源素材，不是输出单位。
- 除非用户另行指定，目标时长为 75-120 秒。
- 旁白使用面向西方观众的英文。
- 视频是 recap drama，不是 audiobook reading。
- 视觉风格优先遵循当前 `visual_style.md`；默认风格是 `Modern American superhero comic-book illustration style`。

### 2. 提供三个方案方向

所有选项都必须覆盖完整 Arc，只改变处理方式：

- hook framing
- 情绪强调
- 压缩策略
- 画面密度
- 结尾悬念角度

常见方向：

- betrayal-first hook
- cold-revenge hook
- identity-humiliation hook

除非用户明确要求，否则不要提出“每章一个视频”。

### 3. 展示渲染 Runtime 选项

严格遵守 `AGENT_GUIDE.md`。如果 Remotion 和 HyperFrames 都可用，必须在锁定 `render_runtime` 前同时展示两者。

本格式的推荐默认值：

- Remotion：适合 still-led comic panels、Ken Burns motion、speech bubbles、captions 和音频控制。

诚实说明 tradeoff：

- HyperFrames 可用于 HTML / GSAP kinetic typography，但这个漫画解说格式更依赖既有 Remotion scene stack，以及对 speech bubble / caption 的精确控制。

### 4. 锁定生产方案

选定 concept 后通常使用：

- `target_duration_seconds`: 约 90
- `renderer_family`: `animation-first`
- `render_runtime`: 用户批准的 runtime，通常为 `remotion`
- `delivery_promise.promise_type`: `motion_led`
- `delivery_promise.motion_required`: `false`
- `delivery_promise.approved_fallback`: `still_led`
- `music_source.source_type`: `none`、`user_library` 或用户批准的本地/免费来源
- `voice_selection`: 优先 local/free TTS，除非用户批准其他 provider

默认使用当前视觉风格里的声音策略：不额外添加煽情音乐；如果使用声音，优先克制环境声。即使视觉风格里的 source-footage policy 提到不要添加无关旁白，本 recap pipeline 仍然需要英文旁白。

### 5. 用户批准门

用户批准 concept 和 runtime 之前，不进入 script / assets 阶段。

## 方案内容要求

必须包含：

- title options
- target duration
- node coverage summary
- image count estimate
- visual style source 和简短风格摘要
- TTS path
- music / sound policy，默认无音乐或最小环境声
- caption style：phrase captions，不使用 word highlighting
- speech bubble count：通常 3-6 个
- cost estimate，优先展示 zero-key path

## 质量门

- `production_plan.pipeline` 必须是 `novel-comic-recap-arc`。
- Proposal 覆盖完整 Arc。
- Runtime selection 必须能在 `decision_log` 中审计。
- 成本和 API key 假设必须明确。
