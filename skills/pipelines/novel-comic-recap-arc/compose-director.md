# Compose Director - 小说漫画解说 Arc Pipeline

## 目标

把已批准的 Arc recap 渲染成 9:16 MP4，包含旁白、phrase captions、speech bubbles 和 comic-panel motion。

## Runtime 路由

先读取 `edit_decisions.render_runtime`。它必须与 `proposal_packet.production_plan.render_runtime` 中锁定的 runtime 一致。

本格式推荐默认使用 Remotion，但禁止静默切换 runtime。如果已批准 runtime 失败，必须暴露 blocker，并等待用户批准后才能改路径。

## Remotion 合成规则

如果使用 Remotion / Explainer-style composition：

- 把生成图片和音频复制或 symlink 到 `remotion-composer/public/<project>/`。
- 在 `remotion-composer/public/demo-props/<project>.json` 构建 props。
- 使用 9:16 output settings。
- 使用 `anime_scene` 或等价的 still-led scene components。
- 关键对白使用 speech-bubble overlays。
- 使用 phrase captions，并设置 `"captionHighlightMode": "none"`。

Props 级必须包含：

```json
{
  "captionHighlightMode": "none",
  "metadata": {
    "pipeline": "novel-comic-recap-arc",
    "episode_unit": "arc",
    "video_language": "en-US"
  }
}
```

## 文字安全

- 不要依赖 AI-generated images 渲染精确文字。
- 当前视觉风格禁止在生成图片里出现 text、logo、watermark、subtitles 和 gibberish text。
- Captions 和 speech bubbles 是本 recap 格式里受控的 Remotion overlays；要稀疏、可读，并避开人脸和关键动作。
- 除非用户明确要求，否则不要把视频做成大量 title card。
- 检查 captions 和 speech bubbles 是否遮挡人脸或关键动作。

## 验证

最终交付前：

- 可用时运行 composition validation。
- 渲染或检查 sampled frames。
- 使用 ffprobe 验证输出。
- 确认存在 audio stream。
- 确认 duration 在已批准容差内。
- 确认没有 black / blank frames。
- 确认各 scene 风格一致。
- 确认图片保持 modern superhero comic / luxury noir 风格，不漂移到 photoreal、anime、manga、webtoon、3D、game CG 或 fantasy-werewolf imagery。

## 输出

产出：

- `render_report`
- `final_review`
- `projects/<project>/renders/` 下的 final MP4 path

## 质量门

- 一个 Arc 视频完整且可观看。
- Captions 没有 word highlighting。
- Frame samples 显示 9:16 composition 清晰一致。
- Final review 记录任何剩余风险。
