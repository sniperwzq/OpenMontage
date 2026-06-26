import {
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

export type SpeechBubbleTone = "light" | "dark" | "gold";

interface SpeechBubbleProps {
  text: string;
  speaker?: string;
  position?: string;
  accentColor?: string;
  tone?: SpeechBubbleTone;
  maxWidth?: number;
  fontSize?: number;
}

function layoutForPosition(position?: string): React.CSSProperties {
  switch (position) {
    case "top-right":
      return { top: 150, right: 72, alignItems: "flex-end" };
    case "mid-left":
      return { top: 610, left: 72, alignItems: "flex-start" };
    case "mid-right":
      return { top: 610, right: 72, alignItems: "flex-end" };
    case "bottom-left":
      return { bottom: 250, left: 72, alignItems: "flex-start" };
    case "bottom-right":
      return { bottom: 250, right: 72, alignItems: "flex-end" };
    case "center":
      return { top: 690, left: 96, right: 96, alignItems: "center" };
    case "top-left":
    default:
      return { top: 150, left: 72, alignItems: "flex-start" };
  }
}

function palette(tone: SpeechBubbleTone, accentColor: string) {
  if (tone === "dark") {
    return {
      background: "rgba(12, 16, 22, 0.9)",
      border: accentColor,
      text: "#F7F0E6",
      speaker: accentColor,
      shadow: "0 24px 60px rgba(0, 0, 0, 0.42)",
    };
  }
  if (tone === "gold") {
    return {
      background: "rgba(213, 177, 103, 0.92)",
      border: "#F4E6BF",
      text: "#14110C",
      speaker: "#2D2416",
      shadow: "0 24px 58px rgba(45, 31, 14, 0.3)",
    };
  }
  return {
    background: "rgba(250, 247, 239, 0.94)",
    border: accentColor,
    text: "#151515",
    speaker: "#5B4A2A",
    shadow: "0 24px 58px rgba(0, 0, 0, 0.34)",
  };
}

export const SpeechBubble: React.FC<SpeechBubbleProps> = ({
  text,
  speaker,
  position = "top-left",
  accentColor = "#D6B46D",
  tone = "light",
  maxWidth = 780,
  fontSize = 46,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const entrance = spring({
    frame,
    fps,
    config: { damping: 18, stiffness: 130, mass: 0.8 },
  });
  const lift = interpolate(entrance, [0, 1], [18, 0]);
  const scale = interpolate(entrance, [0, 1], [0.94, 1]);
  const colors = palette(tone, accentColor);

  return (
    <div
      style={{
        position: "absolute",
        display: "flex",
        flexDirection: "column",
        pointerEvents: "none",
        opacity: entrance,
        transform: `translateY(${lift}px) scale(${scale})`,
        transformOrigin: position.includes("right") ? "top right" : "top left",
        ...layoutForPosition(position),
      }}
    >
      <div
        style={{
          maxWidth,
          background: colors.background,
          color: colors.text,
          border: `4px solid ${colors.border}`,
          borderRadius: 10,
          boxShadow: colors.shadow,
          padding: "24px 30px 26px",
          overflowWrap: "break-word",
        }}
      >
        {speaker && (
          <div
            style={{
              color: colors.speaker,
              fontSize: Math.max(22, Math.round(fontSize * 0.42)),
              fontWeight: 800,
              letterSpacing: 0,
              textTransform: "uppercase",
              marginBottom: 8,
            }}
          >
            {speaker}
          </div>
        )}
        <div
          style={{
            fontSize,
            fontWeight: 800,
            lineHeight: 1.08,
            letterSpacing: 0,
            textShadow:
              tone === "dark" ? "0 2px 2px rgba(0,0,0,0.35)" : "none",
          }}
        >
          {text}
        </div>
      </div>
    </div>
  );
};
