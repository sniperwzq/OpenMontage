# Executive Producer - 小说漫画解说 Arc Pipeline

## 何时使用

当用户提供一个二创小说 Arc，并希望把它制作成一个完整的英文竖屏漫画解说短视频时，使用本 pipeline。常见源文件模式是：

- 小说项目根目录加 `arc_id`，根目录下包含 `erchuang/` 和 `novels/`
- `adapt_arcXXXX.md`：Arc 级设计、边界、节点、名场面和后续剧透保护
- `ec_arcXXXX_ChN-M.md`：章节和 beat 细节、关键对白、结尾定格素材
- `novels/chapter_N.txt` 到 `chapter_M.txt`：最终英文正文
- `bible_setting.md` 和角色参考资产：用于连续性约束

## 核心契约

一个 Arc 产出一个视频。章节是素材来源，不是输出单位。视频结构遵循 Arc 级情绪升级，而不是机械按照章节顺序展开。

默认目标：

- 9:16 竖屏。
- 75-120 秒，通常约 90 秒。
- 面向西方观众的英文旁白。
- Recap 风格，不做 audiobook 朗读。
- 使用 phrase captions，不启用 active word highlighting。
- 关键对白用漫画 speech bubbles 呈现。
- 尽量使用 zero-key / local-first 资产路径。

## EP 状态字段

跨阶段维护这些 Arc 字段：

- `novel_project_path`
- `erchuang_dir`
- `novels_dir`
- `arc_id`
- `adapt_arc_path`
- `ec_arc_path`
- `bible_path`
- `book_title_path`
- `stage_plan_path`
- `chapter_range`
- `chapter_text_paths`
- `character_reference_paths`
- `protected_future_arcs`
- `bottom_card_protections`
- `arc_start`
- `arc_landing`
- `nodes[]`
- `must_show_moments[]`
- `dialogue_candidates[]`
- `target_duration_seconds`
- `scene_budget`
- `visual_style_block`
- `asset_style_block`
- `visual_style_path`
- `render_runtime`
- `captionHighlightMode = "none"`

## 阶段顺序

按顺序执行：

`research -> proposal -> script -> scene_plan -> assets -> edit -> compose -> publish`

在 proposal 通过前，不生成付费或高影响资产。如果 Remotion 和 HyperFrames 都可用，必须遵守 `AGENT_GUIDE.md`：先把两种 runtime 都展示给用户，再锁定 `render_runtime`。

## 跨阶段检查点

Research 后：

- 如果使用快捷输入，确认 `novel_project_path + arc_id` 已解析到 `erchuang/adapt_arcXXXX.md`、`erchuang/ec_arcXXXX_ChN-M.md`，以及所有匹配的 `novels/chapter_N.txt` 文件。
- 确认两个 Arc 文件都已解析。
- 确认最终章节正文已用于校对措辞、连续性和短对白候选，但没有把 recap 写成逐章摘要。
- 确认 protected future reveals 已列出。
- 确认所有节点都已捕获，即使节点数量不是六个。
- 确认用户提供的 `visual_style.md` 已读取；如果没有，则读取仓库默认视觉风格，并将 `VISUAL_STYLE_BLOCK`、`ASSET_STYLE_BLOCK` 和全局负面约束向后传递。

Proposal 后：

- 确认已批准的 concept 是一个 Arc / 一个视频。
- 确认时长、视觉风格、声音方案、图片路径和 render runtime。

Script 后：

- 确认旁白压缩覆盖了完整 Arc。
- 确认没有泄露 protected future reveal。
- 确认每个 must-show node 都被使用，或被有意合并并说明。

Scene plan 后：

- 确认场景数量足够密，一般 75-120 秒视频使用 8-12 个场景。
- 确认精确文字不会交给图片生成模型处理。
- 确认 speech bubbles 和 captions 都作为 overlay 规划。

Assets 后：

- 确认旁白是新生成 TTS，不使用现有 audiobook 音频。
- 确认图片风格和角色描述保持一致。
- 确认生成图片遵守 `Modern American superhero comic-book illustration style`，以及视觉风格文件中的 no-text / no-logo / no-watermark 约束。
- 确认任何缺失视觉都在 compose 前暴露出来。

Edit 后：

- 确认节奏比单章试播更快。
- 确认 `subtitles.style = "phrase"` 且 `captionHighlightMode = "none"`。

Compose 后：

- 确认输出为 9:16，音频存在，时长在容差内。
- 抽帧检查黑帧、overlay 混乱、文字弱、风格漂移等问题。

## 退回规则

- 如果时长过长或节奏过慢，退回 script，而不是 edit。
- 如果所需图片过多，退回 scene_plan 合并场景。
- 如果风格漂移，退回 assets 并收紧 style block。
- 如果 caption 或 speech bubble 重叠，退回 edit 或 compose。
