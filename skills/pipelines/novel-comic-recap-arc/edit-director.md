# Edit Director - 小说漫画解说 Arc Pipeline

## 目标

把 scene plan 和 assets 转换成一个快节奏、覆盖完整 Arc 的 edit decision list。输出必须是 schema-valid 的 `edit_decisions`。

## 时间规则

默认 Arc 节奏：

- Hook：3-5 秒。
- Main nodes：每个 7-12 秒，取决于节点数量。
- 最高烈度的 betrayal / status scenes 可给 10-14 秒。
- Final landing / cliffhanger：8-12 秒。

如果成片感觉像单章试播，说明节奏太松，需要压紧。观众应该感到整个 Arc 在快速推进。

## Caption 规则

使用 phrase captions：

- `style`: `phrase`
- `captionHighlightMode`: `none`
- 竖屏每行 4-7 个英文词。
- 默认 bottom-center；如果遮挡人脸或动作，则移动位置。

默认不要使用 karaoke 或 active-word captions。

## Speech Bubble 规则

- 总量 3-6 个 speech bubbles。
- 每个 bubble 必须短。
- 不要让 bubble 和密集 caption 同时压在同一张脸或同一个关键动作上。
- Bubbles 应落在命令、羞辱或决定性转折上。

## Edit Artifact 要求

必须包含：

- scene cuts with start/end times
- image source per cut
- camera motion per cut
- overlay schedule
- speech bubble schedule
- subtitle config
- narration audio layout
- optional music layout
- 从已批准 proposal 复制来的 `render_runtime`

添加 metadata：

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

## 质量门

- Duration 与已批准 target 在容差内匹配。
- 每个主要 Arc turn 都出现在 timeline 中。
- Overlay density 受控。
- Render runtime 与 proposal 一致；禁止静默切换引擎。
