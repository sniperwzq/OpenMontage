# Burned Luna, Crowned Queen - Comic Recap Visual Style

This is the bundled default visual style for the `novel-comic-recap-arc`
pipeline. It is copied into this repository so the pipeline is self-contained
and does not depend on a project-specific external file.

## Part 1: Global Visual Style

| Field | Content |
|:---|:---|
| `ASPECT_RATIO` | 9:16 vertical. For confrontation, identity pressure, and public reckoning scenes, prioritize upper-body expressions and vertical power imbalance. In group scenes, keep the subject centered or use triangular composition to avoid horizontal overload. |
| `STYLE_CORE` | `Modern American superhero comic-book illustration style`. Semi-realistic adult proportions, clear but thicker outer ink contours, hard-edged cel shading, bold black shadow masses, and modern luxury noir texture. Character silhouettes should feel like American superhero character design: defined mass, shoulder and neck structure, facial bone structure, and pressure. Clothing remains modern luxury, business, and high-society; do not default to armor, capes, masks, or real superhero logos. Avoid live-action short-drama photo realism, Japanese/Korean webtoon big-eye style, otome-game doll faces, chibi, 3D animation, or game-CG mixing. |
| `PALETTE` | Main colors are cold black, graphite gray, snow white, and deep ocean blue, establishing oppression, coldness, and high-society order. Supporting colors are medical cold blue, old gold, and ivory for labs, family rules, and elite social spaces. Accent colors are limited to blood red, fire orange, alarm red, and cold silver for injury, explosions, evidence reveals, and power reversals. Overall: medium-low saturation, high contrast. Early sections lean cold and gray; return/reckoning sections can increase gold and white. Avoid candy colors, fluorescent cyber colors, large dreamy pink-purple fields, and cheap high-saturation neon. |
| `LIGHTING` | Three default lighting families: cold white diffuse light for blizzards, hospitals, and labs to create hypothermia, isolation, and sterility; golden warm light plus deep shadows from ceiling lamps, wall lamps, and chandeliers for manors, banquets, and councils; low side light, searchlights, sodium lamps, and alarm light for ports, restricted zones, and underground spaces. Contrast should be strong with clear shadow edges. Skin and fabric keep comic-block shadows, not soft-focus portrait lighting. |
| `CAMERA_LANGUAGE` | Vertical dramatic tension. Use close-ups and medium close-ups for humiliation, separation, and regret; medium shots for positioning and faction confrontation. Low angles show Alpha, financial, and family power pressure; high angles show trapped or scrutinized characters. Public spaces favor symmetry, steps, doorframes, and crowd negative space. Private conflict favors oppressive foreground occlusion. Motion tends toward slow push-in, slight orbit, and fixed stare. Avoid shaky handheld movement and exaggerated transitions. |
| `TEXTURE_WORLD` | A modern upper-class power world, not traditional fantasy. Pack visuals combine wealthy family, private security, medical foundation, sanatorium, manor, black business vehicles, closed meeting rooms, and cold hard insignia. Sterling family visuals are old-money finance: international legal teams, private security, white-stone architecture, dark wood trim, metal emblems, and highly ordered social spaces. Adrian Cross-related spaces carry sea routes, ports, night, metal railings, wet concrete, glass curtain walls, and understated luxury. Medical R&D spaces use cold white lights, glass, metal, transparent screens, sterile benches, sealed files, and blue-white data glow. Violent or restricted spaces use rusted metal, wet walls, locked doors, dark red warning lights, and rough texture. Weather favors blizzards, cold rain, sea fog, and night wind. |
| `MOOD_TONE` | First impression: someone suffocated by high-society order is calmly keeping the ledger. Long-term emotion moves from coldness, pain, and replacement toward controlled retaliation, identity reversal, public reckoning, and victory without looking back. Every image serves dignity being taken and reclaimed. Avoid sweet romance, light comedy, campus energy, or pure action spectacle. |
| `SOUND_POLICY` | Default to no added music. Keep only necessary dialogue, necessary narration, and environmental sounds such as snow wind, distant helicopters, glass doors, footsteps, medical equipment beeps, banquet murmurs, port metal sounds, rain, and alarms. Do not add extra emotional music, pop songs, stacked sound effects, or unrelated narration. Generated source imagery must not contain subtitles, screen text, title cards, or watermarks. |
| `GLOBAL_NEGATIVE` | No image text, watermarks, logos, subtitles, or gibberish screen text. No wolf transformations, animal ears, tails, claws, fantasy magic circles, moon-mechanic visuals, or glowing race traits. No medieval castles, ancient costume, steampunk, cyberpunk, school youth, rural pastoral look, Japanese/Korean webtoon, chibi, 3D cartoon, or live-action photo realism. Do not depict Pack as a primitive tribe or supernatural species society. No wrong-era clothing, buildings, vehicles, weapons, or medical equipment. No excessive gore, nudity, vulgar seduction, or unnecessary action-blockbuster treatment. |

## Part 2: Visual Style Block

Use `VISUAL_STYLE_BLOCK` for final storyboard and image prompts.

```text
Aspect ratio: 9:16 vertical. For confrontation, identity pressure, and public reckoning scenes, prioritize upper-body expressions and vertical power imbalance. In group scenes, keep the subject centered or use triangular composition to avoid horizontal overload.
Style: Modern American superhero comic-book illustration style. Semi-realistic adult proportions, clear but thicker outer ink contours, hard-edged cel shading, bold black shadow masses, and modern luxury noir texture. Character silhouettes should have defined mass, shoulder and neck structure, facial bone structure, and pressure, while clothing stays modern luxury, business, and high-society. Do not default to armor, capes, masks, or real superhero logos. Avoid live-action short-drama photo realism, Japanese/Korean webtoon big-eye style, otome-game doll faces, chibi, 3D animation, or game-CG mixing.
Palette: cold black, graphite gray, snow white, and deep ocean blue as main colors; medical cold blue, old gold, and ivory as supporting colors; blood red, fire orange, alarm red, and cold silver only as accents. Medium-low saturation, high contrast. Early sections lean cold and gray; return/reckoning sections can increase gold and white. Avoid candy colors, fluorescent cyber colors, large dreamy pink-purple fields, and cheap high-saturation neon.
Lighting: cold white diffuse light for blizzards, hospitals, and labs; golden warm light plus deep shadows from ceiling lamps, wall lamps, and chandeliers for manors, banquets, and councils; low side light, searchlights, sodium lamps, and alarm light for ports, restricted zones, and underground spaces. Strong contrast, clear shadow edges, comic-block shadows on skin and fabric, no soft-focus portrait lighting.
Camera language: vertical dramatic tension. Close-ups and medium close-ups for humiliation, separation, and regret; medium shots for positioning and faction confrontation. Low angles show power pressure; high angles show trapped or scrutinized characters. Public spaces favor symmetry, steps, doorframes, and crowd negative space. Private conflict favors oppressive foreground occlusion. Motion tends toward slow push-in, slight orbit, and fixed stare. Avoid shaky handheld movement and exaggerated transitions.
World texture: a modern upper-class power world, not traditional fantasy. Pack visuals combine wealthy family, private security, medical foundation, sanatorium, manor, black business vehicles, closed meeting rooms, and cold hard insignia. Sterling family visuals are old-money finance: international legal teams, private security, white-stone architecture, dark wood trim, metal emblems, and highly ordered social spaces. Adrian Cross-related spaces carry sea routes, ports, night, metal railings, wet concrete, glass curtain walls, and understated luxury. Medical R&D spaces use cold white lights, glass, metal, transparent screens, sterile benches, sealed files, and blue-white data glow. Violent or restricted spaces use rusted metal, wet walls, locked doors, dark red warning lights, and rough texture. Weather favors blizzards, cold rain, sea fog, and night wind.
Mood: someone suffocated by high-society order is calmly keeping the ledger. Emotion moves from coldness, pain, and replacement toward controlled retaliation, identity reversal, public reckoning, and victory without looking back. Every image serves dignity being taken and reclaimed. Avoid sweet romance, light comedy, campus energy, or pure action spectacle.
Sound policy: default to no added music. Keep only necessary dialogue, necessary narration, and environmental sounds such as snow wind, distant helicopters, glass doors, footsteps, medical equipment beeps, banquet murmurs, port metal sounds, rain, and alarms. Do not add extra emotional music, pop songs, stacked sound effects, or unrelated narration. Generated source imagery must not contain subtitles, screen text, title cards, or watermarks.
Global negative: no image text, watermarks, logos, subtitles, or gibberish screen text. No wolf transformations, animal ears, tails, claws, fantasy magic circles, moon-mechanic visuals, or glowing race traits. No medieval castles, ancient costume, steampunk, cyberpunk, school youth, rural pastoral look, Japanese/Korean webtoon, chibi, 3D cartoon, live-action photo realism, primitive-tribe Pack, wrong-era clothing/buildings/vehicles/weapons/medical equipment, excessive gore, nudity, vulgar seduction, or unnecessary action-blockbuster treatment.
```

## Part 3: Asset Style Block

Use `ASSET_STYLE_BLOCK` for character sheets and asset reference prompts.

```text
Modern American superhero comic-book character sheet style, prestige graphic novel cover finish, heroic semi-realistic adult proportions, angular facial planes, strong cheekbone and jaw structure, thicker outer contour lines, confident interior ink lines, bold black spot shadows, high-contrast cel shading, dramatic rim light, sculpted anatomy under tailored luxury clothing, graphic painted comic colors, subtle ink hatching, modern luxury noir palette, clearly non-photorealistic, not a photo, not live-action, not a 3D render, no anime, no manga, no Korean or Japanese webtoon, no otome-game doll face, no soft romance portrait, no delicate fashion-illustration thinness, no glossy game CG, pure white background, no text, no labels, no watermark.
```

## Part 4: Boundary Notes

| Area | This Style Defines | This Style Must Not Define |
|:---|:---|:---|
| Characters | Overall aesthetic direction, identity aura, clothing material family, visual differences by power class, reusable reference-image style | Specific face, hairstyle, single outfit, expression, pose, or asset ID |
| Scenes | Scene categories, modern luxury/medical capital/underground port architecture, lighting tendency, material mood, reusable asset-reference style | Specific room structure, entrances/exits, action area, or single-scene blocking |
| Props | Thematic prop families, modern medical/family power/legal reckoning materials, forbidden items, reusable asset-reference style | Specific prop appearance, size, story function, or individual key-prop close-up design |
| Storyboard | Global shot scale, composition, angle, and motion tendency | Segment camera position, movement route, keyframes, shot number, or duration |
| Video | Global aspect ratio, style, colors, lighting, texture, and sound rules | Per-segment action progression, emotional turn, ending frame, or image-to-video prompt |

## Part 5: Validation Summary

| Check | Result |
|:---|:---|
| Only global visual style is defined; no assets, storyboard, or video prompts are generated | Yes |
| Aspect ratio, style, color, lighting, camera language, world texture, sound policy, and global negatives are included | Yes |
| Short `ASSET_STYLE_BLOCK` is included without duplicating the full `VISUAL_STYLE_BLOCK` | Yes |
| Every style field is executable and avoids vague adjectives | Yes |
| No plot settings are added or rewritten | Yes |
| No specific character appearance, scene structure, prop appearance, segment camera, or keyframe is defined | Yes |
