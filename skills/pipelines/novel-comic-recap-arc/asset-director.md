# Asset Director - 小说漫画解说 Arc Pipeline

## 目标

为一个 Arc recap 创建或整理旁白、漫画静帧和可选音乐。输出必须是 schema-valid 的 `asset_manifest`。

## Provider 策略

默认采用 zero-key / local-first：

- 通过 `tts_selector` 生成 TTS；质量可接受时优先 local/free voices。
- 不使用现有 audiobook audio。
- 用户要求 Codex 绘图时，使用 Codex runtime image flow。
- 使用 `codex_image_import` 把外部创建的 Codex 图片登记进 OpenMontage。
- 如果图片生成不可用，先列出准确缺失的图片，不要直接静默换 provider。

使用任何 generation tool 前，必须读取 registry 声明的 Layer 3 skill。

## 图片策略

产出 Arc 级可复用视觉，不是一句话一张图。

默认图片数量：

- 75-90 秒：8-10 张。
- 90-120 秒：10-12 张。

每张图片都要携带：

- `scene_id`
- `covered_nodes`
- `character_descriptors`
- `style_block`
- `negative_style_block`
- `source_reference_paths`
- `prompt`
- `provider`
- `model`
- `resolution`
- `generation_summary`

## 风格一致性

整个 Arc 都要读取并复用当前 `visual_style.md`。如果用户没有提供路径，使用仓库默认文件：

`styles/novel-comic-recap-arc.visual-style.md`

场景图片使用 `VISUAL_STYLE_BLOCK`，角色参考图使用 `ASSET_STYLE_BLOCK`。

当前默认 style core：

`Modern American superhero comic-book illustration style`

Scene image prompts 应保持：

- 9:16 竖屏构图，上半身表情清晰可读。
- 英雄式半写实成人比例、棱角分明的面部结构、强 cheekbone / jaw structure。
- 更厚的外轮廓线、明确的内部墨线、强黑色块阴影。
- 硬边 cel shading、高对比、dramatic rim light、graphic painted comic colors。
- modern luxury noir palette：cold black、graphite gray、snow white、deep ocean blue、medical cold blue、old gold、ivory；blood red / fire orange / alarm red / cold silver 只作强调色。
- modern high-society power world：manors、private security、medical foundations、corporate Pack power、old-money interiors、hospitals / labs、ports、rain / snow / fog / night。
- mood：cold pain、public humiliation、controlled retaliation、identity reversal、dignity being taken back。

Asset reference prompts 使用短版 asset style：

`Modern American superhero comic-book character sheet style, prestige graphic novel cover finish, heroic semi-realistic adult proportions, angular facial planes, strong cheekbone and jaw structure, thicker outer contour lines, confident interior ink lines, bold black spot shadows, high-contrast cel shading, dramatic rim light, sculpted anatomy under tailored luxury clothing, graphic painted comic colors, subtle ink hatching, modern luxury noir palette, clearly non-photorealistic, not a photo, not live-action, not a 3D render, no anime, no manga, no Korean or Japanese webtoon, no otome-game doll face, no soft romance portrait, no delicate fashion-illustration thinness, no glossy game CG, pure white background, no text, no labels, no watermark.`

所有生成图片都应用这些 global negatives：

- no text、subtitles、watermarks、logos、gibberish screen text；
- no wolf transformation、animal ears / tails / claws、magic circles、moon-mechanic visuals、glowing race features；
- no medieval castles、ancient costume、steampunk、cyberpunk、school youth、rural pastoral look；
- no Japanese / Korean webtoon、chibi、3D cartoon、photorealistic live-action still、glossy game CG；
- 不要把 Pack 渲染成原始部落或超自然种族社会；
- 不要出现错误时代的 clothing、buildings、vehicles、weapons 或 medical equipment；
- 不要 excessive gore、nudity、vulgar seduction 或不必要的 action-blockbuster treatment。

使用角色参考图和 `bible_setting.md` 写出一致的 character descriptors。

## Speech 与 Captions

- 从已批准脚本生成旁白。
- 在 artifact 中保留旁白脚本文本。
- Captions 从 narration / script timing 派生，使用 phrase captions。
- 不创建 active word highlighting。
- 默认音乐策略遵循 `visual_style.md`：除非用户要求，不加情绪音乐；可用时允许克制环境声。

## 质量门

- 旁白时长符合目标时长。
- 图片 prompts 覆盖所有已规划 scenes。
- 精确文字留给 Remotion overlays。
- Asset manifest 清晰分离 generated images、provided references、narration 和 optional music。
- Missing assets 必须作为明确 blocker 暴露，不能藏在假设里。
