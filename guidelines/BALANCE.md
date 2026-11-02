# Balance: not too harsh, not too soft

Every visual dimension has a *harsh* end (sharp, loud, high energy) and a *soft* end (mushy, low energy, tiring in a different way).
Malva OS aims at the measured middle of each. There is one tuned setting; the earlier adjustable dial is not part of the system now.

| Dimension | Too harsh | Too soft | Malva middle | Measured |
|---|---|---|---|---|
| Body text contrast | pure black on white, 21 : 1 (glare, halation) | under 4.5 : 1 | charcoal on off-white, silver on graphite | light 16.8 : 1, dark 15.3 : 1 |
| Secondary text | competes with body | unreadable | a quiet grey, for supporting text only | light 3.6 : 1, dark 5.1 : 1 |
| Label on accent | blinding | under 4.5 : 1 | white on plum, charcoal on orchid | light 7.4 : 1, dark 5.8 : 1 |
| Accent colour | neon | grey | the logo's plum, and only on what can be acted on | light `#8C3274`, dark `#DC73C2` |
| Surfaces | pure `#000` / `#FFF` | no layering | off-white canvas with white cards; graphite with one lighter step per elevation | `#F5F5F7` / `#FFFFFF`, `#161617` / `#1E1E1F` |
| Corner radius | 6 px or less, clinical | 36 px and up on controls, toy-like | 10 px controls, 14 px menus, 22 px cards and dialogs | `radius` in the tokens |
| Type weight | 700 everywhere | 300 | 400 body, 600 labels and headings, 700 titles only | `type.scale` |
| Shadow | dark and tight | none | neutral black, 0.08 to 0.18 in light and 0.4 to 0.6 in dark | `elevation` |
| Motion | instant, or bouncy (over 1.6 overshoot) | sluggish (over 400 ms) | 90 ms press, 160 ms hover, 240 ms open, a 1.35 spring where something arrives | `motion` |
| Wallpaper | detail and contrast everywhere | flat colour | a quiet centre where windows live, one soft bloom low in the frame | see below |

## Why these choices

* **Lightness.** Pure black on white causes glare, and bright text on pure black causes halation. Charcoal text on an off-white canvas, and silver text on graphite, stay well above the accessibility minimum without the strain.
* **Hue.** The plum and orchid of the logo blend red energy with blue calm. Because the surfaces are neutral, that one colour carries meaning instead of decorating.
* **Shape.** Rounder corners read as friendly and safe, angular ones as precise and urgent. 10 px for controls sits in between.
* **Weight.** Hierarchy comes from size and weight steps, not from making everything bold. Only titles go to 700.
* **Visual weight.** On a wallpaper, the weight sits low in the frame; the centre, where windows live, stays quiet.
* **Texture.** The Silver and Graphite wallpapers carry a faint grain that stops gradient banding.
* **Never colour alone.** Pass and fail, status and focus always pair colour with text, shape or a ring.

## Wallpapers

| File prefix | Look | Mean lightness L\* |
|---|---|---|
| `malva-silver` | neutral light, soft plum bloom | 92.0 |
| `malva-graphite` | neutral dark, soft plum bloom | 10.6 |
| `malva-dawn` | the brand mallow-flower wallpaper, light | 82.8 |
| `malva-dusk` | the brand mallow-flower wallpaper, dark | 21.8 |

All four exist at 2560 x 1440 and 1170 x 2532 in `brand/wallpapers/`. Silver and Graphite are generated from the UI kit's wallpaper
definition (the prototypes use them as the desktop); Dawn and Dusk are the original brand artwork and are kept as it was.
