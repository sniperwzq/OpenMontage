# Research Director - 小说漫画解说 Arc Pipeline

## 目标

把用户提供的本地小说 Arc 源文件转换成 schema-valid 的 `research_brief`，并把详细的 `arc_brief` 写入 `metadata`。本阶段不是联网调研，而是基于本地源文件做故事分析。

## 输入

优先支持的快捷输入：

- `novel_project_path`：小说项目根目录，例如 `/Users/wangzhiqiang/novel/novel20260413`
- `arc_id`：四位 Arc 编号，例如 `0101`；也允许 `arc0101` 这类带前缀写法

可用时应读取的文件：

- `adapt_arc*.md`
- `ec_arc*_Ch*.md`
- `ec_arc*_ChN-M.md` 文件名对应范围内的 `novels/chapter_N.txt`
- `bible_setting.md`
- `book_title.txt`
- `stage_N_plan.md` 或 `stage_NN_plan.md`
- 角色参考图
- 用户提供的视觉风格说明，尤其是 `visual_style.md`

## 流程

### 1. 解析 Source Bundle

如果用户提供了 `novel_project_path` 和 `arc_id`，先解析 Arc 相关源文件，再进入故事分析。优先使用仓库内 helper：

```python
from lib.novel_arc_intake import resolve_novel_arc_source_bundle

bundle = resolve_novel_arc_source_bundle(novel_project_path, arc_id).to_dict()
```

解析结果必须定位到：

- `<novel_project_path>/erchuang/adapt_arc{arc_id}.md`
- `<novel_project_path>/erchuang/ec_arc{arc_id}_ChN-M.md`
- `<novel_project_path>/novels/chapter_N.txt` 到 `chapter_M.txt`

存在时还应携带这些可选上下文：

- `erchuang/bible_setting.md`
- `erchuang/book_title.txt`
- 对应阶段规划，例如 `stage_1_plan.md` 或 `stage_04_plan.md`
- `visual_style.md`
- 常规参考图目录里的角色参考图

除非用户明确要求使用备份版本，否则不要读取 `adapt_arc{arc_id}_backup*.md`。如果 resolver 报告缺少 `adapt_arc`、`ec_arc` 或章节正文文件，本阶段应停止并按 blocked 处理，明确列出缺失路径。

如果用户直接提供了明确文件路径，而不是项目根目录加 Arc 编号，也可以使用这些显式路径，但仍要构造同样的 `source_paths` 结构。

### 2. 识别 Arc

提取：

- `arc_id`
- source file paths
- chapter range 和 chapter text paths
- novel project path，如果适用
- Arc 标题或主题
- 起点种子
- 落点
- protected future arcs
- bottom-card protections
- 人物映射
- 场景映射

如果文件名不符合标准格式，可以从标题和正文中推断。不要假设节点数一定是六个。

### 3. 动态解析节点

从 `adapt_arc` 中提取每个故事节点：

- node id 和名称
- 情绪维度
- 情绪核心
- 极致情节表达
- 名场面
- 偿还锚点或 payoff anchor
- 可用时记录对应章节或 beat 引用
- must-show priority：`must`、`strong` 或 `optional`

### 4. 把章节 Beat 当作素材解析

从 `ec_arc` 中提取：

- 章节标签
- beat-by-beat 事件
- 关键对白
- 章节截断点
- 体验目标

不要让章节划分决定视频结构。章节只是证据和素材，视频结构仍应服从 Arc 级情绪升级。

### 5. 读取匹配章节正文

从 `novels/chapter_N.txt` 到 `chapter_M.txt` 中，只提取解说视频真正需要的证据：

- 最终正文里的章节标题和 POV 标签
- calibration 里的 known / must-not-reveal 约束
- 适合作为 speech bubble 的短对白原句
- 比 `ec_arc` 更具体、更适合画面的正文细节
- `ec_arc` beats 与最终正文之间的差异

章节正文是措辞和连续性的权威来源；但 Arc 边界和剧透保护仍以 `adapt_arc` 为准。不要把视频写成有声书，也不要做逐章流水账。

### 6. 生成 Recap Compression Notes

写清楚：

- 观众在视频结束时必须理解什么
- 时长紧张时哪些节点可以合并
- 哪些对白值得做 speech bubble
- 哪些画面适合作为 hero frame
- 哪些后续 Arc 内容不能剧透

### 7. 读取视觉风格

如果用户提供 `visual_style.md`，必须读取。如果没有显式提供，检查仓库默认文件：

`styles/novel-comic-recap-arc.visual-style.md`

提取并向后传递：

- `STYLE_CORE`：默认是 `Modern American superhero comic-book illustration style`
- `VISUAL_STYLE_BLOCK`：用于场景和图片 prompt
- `ASSET_STYLE_BLOCK`：用于角色设定图和参考资产
- `PALETTE`、`LIGHTING`、`CAMERA_LANGUAGE`、`TEXTURE_WORLD`、`MOOD_TONE`
- `GLOBAL_NEGATIVE`：用于生成图片的负面约束
- `SOUND_POLICY`：除非用户另行批准，优先无音乐或只使用克制环境声

注意：`GLOBAL_NEGATIVE` 以及 no-text / no-logo / no-watermark 约束适用于生成图片。解说格式仍可使用可控的 Remotion overlay captions 和 speech bubbles，除非用户明确禁用。

### 8. 产出 Schema-Valid `research_brief`

使用本地源文件路径作为引用。通用 research schema 需要 landscape / data / audience 字段，在本 pipeline 中按以下方式适配：

- `landscape.existing_content`：列出已提供的源文件模块，以及每个模块的作用
- `data_points`：列出具体故事事实，每条都引用本地 `file://` URI
- `audience_insights`：描述西方短视频 romance / revenge recap 观众预期
- `angles_discovered`：为同一个 Arc 提供三种处理角度
- `sources`：引用 `adapt_arc`、`ec_arc`、匹配章节正文、`bible_setting`、stage plan、角色参考和用户视觉风格文件

详细源文件分析写入：

```json
"metadata": {
  "arc_brief": {
    "episode_unit": "arc",
    "arc_id": "...",
    "source_paths": {},
    "chapter_range": {"start": 1, "end": 3},
    "protected_future_arcs": [],
    "bottom_card_protections": [],
    "nodes": [],
    "chapter_beats": [],
    "chapter_text_evidence": [],
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

## 质量门

- `adapt_arc` 中的每个节点都被表示出来。
- `ec_arc` 文件名范围内的每一章都能在 `novels/` 中找到，并被引用；如果未使用，必须说明原因。
- protected future material 必须明确记录。
- 关键对白只能短引用，不能大段复刻正文。
- 如果有视觉风格文件，必须总结并写入 metadata。
- 不允许把源文件不支持的故事发明写入 brief。
