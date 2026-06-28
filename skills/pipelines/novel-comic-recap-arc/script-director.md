# Script Director - 小说漫画解说 Arc Pipeline

## 目标

为完整 Arc 写一版快节奏英文旁白脚本，并产出 schema-valid 的 `script` artifact。

## 默认节奏

- 75 秒：约 180-220 个英文词。
- 90 秒：约 230-270 个英文词。
- 120 秒：约 300-360 个英文词。
- 口播句子要短，通常 6-12 个词。
- 除非 lore 会改变背叛、地位或 stakes，否则不要解释设定背景。

## 结构

根据节点数量调整，但默认使用这个形状：

1. `hook`：0-4 秒，一句残酷前提。
2. `setup`：只给理解第一笔背叛所需的最少上下文。
3. `node_*`：每个重要 Arc 节点一段；节点过多时合并。
4. `turn`：女主停止替背叛找理由的瞬间。
5. `arc_landing`：本 Arc 完整情绪落点。
6. `cliffhanger`：制造下一 Arc 好奇，但不能剧透 protected material。

## 写作规则

- `adapt_arc` 是 Arc 起点、落点、保护边界和节点意图的权威。
- `ec_arc` 是 beat、细节和对白素材库。
- `novels/chapter_N.txt` 是最终措辞、连续性和短对白候选的权威。
- 除非 Arc 结构本身要求，否则不要逐章讲述。
- 不要写 audiobook prose。
- 不要包含长篇直接引用。
- 使用清晰、直接、适合西方 romance / revenge recap 的语言。
- 人名读音和写法要与 `bible_setting.md` 保持一致。

## Dialogue Bubble 选择

选择 3-6 句短台词用于 speech bubbles。优先：

- 暴露背叛的命令
- 公开羞辱的句子
- 孩子的拒绝
- 结尾的控制威胁
- 女主安静下决定的句子

Speech bubbles 不是字幕。它们应该稀疏、有戏剧性，不要替代旁白。

## 输出要求

产出 schema-valid 的 `script`：

- `version: "1.0"`
- `title`
- `total_duration_seconds`
- `sections[]`

添加 metadata：

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

## 质量门

- 这个 Arc 听起来是完整的。
- 节奏比单章试播更快。
- 每个 must-show node 都出现，或被明确合并。
- 不泄露 protected future reveal。
- 最后一段制造下一 Arc 欲望，但不能让本 Arc 显得没讲完。
