import {
  AbsoluteFill,
  Audio,
  Img,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

type CaptionWord = {
  word: string;
  startMs: number;
  endMs: number;
};

type Cut = {
  id: string;
  source: string;
  in_seconds: number;
  out_seconds: number;
  animation?: string;
  transform?: {
    animation?: string;
    scale?: number;
  };
};

type Overlay = {
  type: "speech_bubble";
  in_seconds: number;
  out_seconds: number;
  text: string;
  speaker?: string;
  position?: string;
  tone?: "light" | "dark" | "gold";
  maxWidth?: number;
  fontSize?: number;
  accentColor?: string;
};

type AudioConfig = {
  narration?: {
    src: string;
    volume?: number;
  };
};

export type ComicRecapProps = {
  cuts: Cut[];
  overlays?: Overlay[];
  captions?: CaptionWord[];
  captionHighlightMode?: "none" | "active";
  audio?: AudioConfig;
};

const resolveAsset = (src: string): string => {
  if (src.startsWith("http://") || src.startsWith("https://") || src.startsWith("data:")) {
    return src;
  }
  const clean = src.replace(/^file:\/\/\/?/, "");
  if (clean.startsWith("/") || /^[A-Za-z]:[\\/]/.test(clean)) {
    return `file://${clean.replace(/\\/g, "/")}`;
  }
  return staticFile(clean);
};

const motionFor = (animation?: string) => {
  if (animation === "pan-left") {
    return { x0: 32, x1: -32, y0: 0, y1: 0, scale0: 1.1, scale1: 1.1 };
  }
  if (animation === "pan-right") {
    return { x0: -32, x1: 32, y0: 0, y1: 0, scale0: 1.1, scale1: 1.1 };
  }
  if (animation === "parallax") {
    return { x0: 0, x1: 0, y0: 24, y1: -24, scale0: 1.08, scale1: 1.1 };
  }
  if (animation === "zoom-out") {
    return { x0: 0, x1: 0, y0: 0, y1: 0, scale0: 1.14, scale1: 1.02 };
  }
  return { x0: 0, x1: -18, y0: 0, y1: -12, scale0: 1.02, scale1: 1.14 };
};

const ComicPanel: React.FC<{ cut: Cut }> = ({ cut }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const duration = Math.max(1, Math.round((cut.out_seconds - cut.in_seconds) * fps));
  const progress = interpolate(frame, [0, duration], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fadeIn = interpolate(frame, [0, 8], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fadeOut = interpolate(frame, [duration - 10, duration], [1, 0.78], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const motion = motionFor(cut.animation || cut.transform?.animation);
  const x = interpolate(progress, [0, 1], [motion.x0, motion.x1]);
  const y = interpolate(progress, [0, 1], [motion.y0, motion.y1]);
  const scale = interpolate(progress, [0, 1], [motion.scale0, motion.scale1]);

  return (
    <AbsoluteFill style={{ backgroundColor: "#05070A", overflow: "hidden" }}>
      <Img
        src={resolveAsset(cut.source)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          opacity: fadeIn * fadeOut,
          transform: `translate(${x}px, ${y}px) scale(${scale})`,
          willChange: "transform, opacity",
        }}
      />
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(5,7,10,0.28) 0%, rgba(5,7,10,0.02) 42%, rgba(5,7,10,0.54) 100%)",
        }}
      />
    </AbsoluteFill>
  );
};

const bubbleLayout = (position?: string): React.CSSProperties => {
  switch (position) {
    case "top-right":
      return { top: 150, right: 56, alignItems: "flex-end" };
    case "mid-left":
      return { top: 690, left: 56, alignItems: "flex-start" };
    case "mid-right":
      return { top: 690, right: 56, alignItems: "flex-end" };
    case "bottom-left":
      return { bottom: 300, left: 56, alignItems: "flex-start" };
    case "bottom-right":
      return { bottom: 300, right: 56, alignItems: "flex-end" };
    case "top-left":
    default:
      return { top: 150, left: 56, alignItems: "flex-start" };
  }
};

const bubblePalette = (tone: Overlay["tone"], accentColor: string) => {
  if (tone === "dark") {
    return {
      background: "rgba(9, 12, 17, 0.9)",
      border: accentColor,
      text: "#F8FAFC",
      speaker: accentColor,
    };
  }
  if (tone === "gold") {
    return {
      background: "rgba(214, 180, 109, 0.94)",
      border: "#F8E6B9",
      text: "#111827",
      speaker: "#342511",
    };
  }
  return {
    background: "rgba(248, 250, 252, 0.94)",
    border: accentColor,
    text: "#111827",
    speaker: "#5B4A2A",
  };
};

const SpeechBubble: React.FC<{ overlay: Overlay }> = ({ overlay }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const entrance = spring({
    frame,
    fps,
    config: { damping: 20, stiffness: 140, mass: 0.8 },
  });
  const lift = interpolate(entrance, [0, 1], [18, 0]);
  const accent = overlay.accentColor || "#D6B46D";
  const colors = bubblePalette(overlay.tone || "light", accent);

  return (
    <div
      style={{
        position: "absolute",
        display: "flex",
        flexDirection: "column",
        pointerEvents: "none",
        opacity: entrance,
        transform: `translateY(${lift}px) scale(${interpolate(entrance, [0, 1], [0.96, 1])})`,
        ...bubbleLayout(overlay.position),
      }}
    >
      <div
        style={{
          maxWidth: overlay.maxWidth || 760,
          background: colors.background,
          color: colors.text,
          border: `4px solid ${colors.border}`,
          borderRadius: 8,
          boxShadow: "0 22px 54px rgba(0, 0, 0, 0.38)",
          padding: "22px 28px 24px",
          overflowWrap: "break-word",
        }}
      >
        {overlay.speaker && (
          <div
            style={{
              color: colors.speaker,
              fontSize: 20,
              fontWeight: 900,
              letterSpacing: 0,
              marginBottom: 8,
            }}
          >
            {overlay.speaker}
          </div>
        )}
        <div
          style={{
            fontSize: overlay.fontSize || 42,
            fontWeight: 900,
            lineHeight: 1.08,
            letterSpacing: 0,
          }}
        >
          {overlay.text}
        </div>
      </div>
    </div>
  );
};

const CaptionLayer: React.FC<{ words: CaptionWord[] }> = ({ words }) => {
  const { fps } = useVideoConfig();
  const pages: CaptionWord[][] = [];
  const sorted = [...words].sort((a, b) => a.startMs - b.startMs);
  let current: CaptionWord[] = [];
  for (const word of sorted) {
    const previous = current[current.length - 1];
    const startsNewPhrase =
      !previous || word.startMs - previous.endMs > 700 || current.length >= 7;
    if (startsNewPhrase && current.length > 0) {
      pages.push(current);
      current = [];
    }
    current.push(word);
  }
  if (current.length > 0) {
    pages.push(current);
  }

  return (
    <AbsoluteFill>
      {pages.map((page, index) => {
        if (page.length === 0) return null;
        const startMs = page[0].startMs;
        const nextStartMs = pages[index + 1]?.[0]?.startMs;
        const paddedEndMs = page[page.length - 1].endMs + 450;
        const endMs = nextStartMs ? Math.min(paddedEndMs, nextStartMs - 80) : paddedEndMs;
        const from = Math.round((startMs / 1000) * fps);
        const duration = Math.max(1, Math.round(((endMs - startMs) / 1000) * fps));
        return (
          <Sequence key={`${startMs}-${index}`} from={from} durationInFrames={duration}>
            <CaptionPage words={page} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};

const CaptionPage: React.FC<{ words: CaptionWord[] }> = ({ words }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const entrance = spring({ frame, fps, config: { damping: 24, stiffness: 130 } });
  const y = interpolate(entrance, [0, 1], [16, 0]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-end",
        alignItems: "center",
        paddingBottom: 94,
      }}
    >
      <div
        style={{
          background: "rgba(5, 7, 10, 0.76)",
          color: "#F8FAFC",
          borderRadius: 8,
          padding: "14px 26px",
          maxWidth: "82%",
          textAlign: "center",
          opacity: entrance,
          transform: `translateY(${y}px)`,
          boxShadow: "0 18px 40px rgba(0, 0, 0, 0.34)",
        }}
      >
        <span
          style={{
            fontFamily: "Inter, system-ui, sans-serif",
            fontSize: 42,
            fontWeight: 850,
            lineHeight: 1.28,
            letterSpacing: 0,
            textShadow: "0 2px 4px rgba(0,0,0,0.5)",
          }}
        >
          {words.map((word, index) => (
            <span key={`${word.startMs}-${index}`}>
              {word.word}
              {index < words.length - 1 ? " " : ""}
            </span>
          ))}
        </span>
      </div>
    </AbsoluteFill>
  );
};

export const ComicRecap: React.FC<ComicRecapProps> = ({
  cuts,
  overlays = [],
  captions = [],
  audio = {},
}) => {
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill style={{ backgroundColor: "#05070A" }}>
      {cuts.map((cut) => {
        const from = Math.round(cut.in_seconds * fps);
        const duration = Math.max(1, Math.round((cut.out_seconds - cut.in_seconds) * fps));
        return (
          <Sequence key={cut.id} from={from} durationInFrames={duration}>
            <ComicPanel cut={cut} />
          </Sequence>
        );
      })}

      {overlays.map((overlay, index) => {
        const from = Math.round(overlay.in_seconds * fps);
        const duration = Math.max(1, Math.round((overlay.out_seconds - overlay.in_seconds) * fps));
        return (
          <Sequence key={`${overlay.text}-${index}`} from={from} durationInFrames={duration}>
            <SpeechBubble overlay={overlay} />
          </Sequence>
        );
      })}

      {captions.length > 0 && <CaptionLayer words={captions} />}

      {audio.narration?.src && (
        <Audio src={resolveAsset(audio.narration.src)} volume={audio.narration.volume ?? 1} />
      )}
    </AbsoluteFill>
  );
};
