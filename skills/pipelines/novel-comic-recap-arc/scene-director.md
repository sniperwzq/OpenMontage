# Scene Director - 小说漫画解说 Arc Pipeline

## 目标

把 Arc 脚本转换成密集的 9:16 漫画分镜 `scene_plan`。输出必须是 schema-valid 的 `scene_plan` artifact。

## Scene 数量预算

默认：

- 75-90 秒：8-10 个 scenes。
- 90-120 秒：10-12 个 scenes。
- 如果 Arc 节点较少，增加 hook / landing / insert scenes。
- 如果 Arc 节点很多，视觉上合并较弱节点，但必须保留所有 must-show turns。

## 分镜规则

- 一个 scene 只承担一个情绪任务。
- 不要把字幕或 speech-bubble 文字烘焙进生成图片。
- captions、bubbles、warning tape、title cards 和小号可读文字都用 Remotion overlays。
- 优先使用强 stills + camera motion，不要用大量弱图堆数量。
- 保持竖屏安全区：关键人脸和文字避开平台 UI 区域。
- 遵循当前 `visual_style.md`：vertical power staging、居中或三角构图、清晰上半身表情、低角度表现压迫、高角度表现被困/被审视、对称公共空间、私人冲突里的压迫性前景、slow push-in / orbit / frozen-stare motion。
- 使用视觉风格里的 modern high-society world：Pack 作为 old-money / corporate power，私安、医疗基金、庄园、黑色商务车、封闭房间、冰冷家族徽记。不要引入原始部落、中世纪、魔法或明显狼人变身视觉。

## 每个 Scene 必须包含的 Metadata

每个 scene 都要包含：

- script section id
- 覆盖的 Arc node(s)
- visual purpose
- image prompt intent
- character presence
- speech bubble overlay，如果有
- camera motion
- safe-zone note
- 是否是 hero frame

Arc 级细节写入 `scene_plan.metadata`：

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

## Required Asset 规划

每个 scene 使用 `required_assets`：

- `type`：通常是 `image`、`audio`、`overlay` 或 `music`
- `description`：可直接进入生产的描述
- `source`：`generate`、`provided` 或 `source`

生成图片描述必须只写视觉内容。精确文字放到 overlay notes。

## 质量门

- Scene 数量足够支撑完整 Arc。
- 最强 Arc moments 获得最强画面。
- Scene descriptions 足够具体，能支持一致的图片生成。
- Text overlays 与 image generation 明确分离。
