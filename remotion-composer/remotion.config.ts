import { Config } from "@remotion/cli/config";

// WSL on this machine rejects Chromium's sandbox host shutdown path.
// Single-process mode keeps Remotion rendering local while avoiding that OS-level failure.
// Remotion 4.0.441 treats a literal false as "use default" for this option.
// Passing 0 keeps the value falsy all the way to the Chromium launch check.
Config.setChromiumMultiProcessOnLinux(0 as unknown as boolean);
// Prefer hardware-backed ANGLE rendering. The previous `swangle` value forces
// SwiftShader software rendering and made long vertical comic renders time out.
Config.setChromiumOpenGlRenderer("angle");
Config.setOverwriteOutput(true);
