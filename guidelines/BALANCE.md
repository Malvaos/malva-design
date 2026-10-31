# Balance: not too harsh, not too soft

Every visual dimension has a *harsh* end (sharp, loud, high energy) and a *soft* end (mushy, low energy, tiring in a different way).
Malva OS aims at the measured middle of each, and the **Balance dial** (Settings > Appearance) lets people slide either way and snaps back to the middle.

| Dimension | Too harsh | Too soft | Malva middle | Measured |
|---|---|---|---|---|
| Body text contrast | 16–21:1 (black on white, halation, glare) | < 7:1 | 10–14:1 | light 14.0, dark 11.7 |
| Muted text | competes with body (> 9:1) | < 4.5:1 | 5.5–8:1 | 6.8 / 6.8 |
| Label on accent | blinding (> 9:1) | < 4.5:1 | 5–8.5:1 | 7.9 / 6.7 |
| Accent colour | neon, chroma > 0.20 | grey | chroma capped at 0.14 (dusty orchid, plum) | Dark `#D47BBC`, Light `#7E376A` |
| Surfaces | pure `#000` / `#FFF` | no layering | `#1D101C` / `#FBF8FB`, tonal steps for elevation | — |
| Corner radius | 4–6 px, clinical | 24 px+, toy-like | 12 px controls, 20 px windows | dial: 16 / 12 / 8 px |
| Type weight | 700 everywhere | 300 | 400 body, ~500 UI labels, 650 titles only | dial: 430–570 |
| Shadow | dark, tight | none | two-layer, plum-tinted, 8–20 % | dial scales it |
| Motion | instant or bouncy (> 1.6 overshoot) | sluggish (> 400 ms) | 120 ms feedback, 240 ms overlays, 1.35 spring | — |
| Wallpaper | detail and contrast everywhere | flat colour | mid-tone, one busy corner, quiet centre | see below |

## Why these choices (psychology and perception)
- **Hue.** Plum and orchid blend red energy with blue calm, which reads as creative and composed. Leaf green is their complement and gives equilibrium, but two saturated complements vibrate, so green is kept dark and low-chroma.
- **Lightness.** Pure black on white causes glare, and bright text on pure black causes halation. Mid-tone surfaces and 10–14:1 text stay comfortably above the accessibility minimum without the strain.
- **Shape.** Rounder corners read as friendly and safe, angular ones as precise and urgent. 12 px sits in between, and the dial moves both ways.
- **Weight.** Hierarchy comes from size and weight steps, not from making everything bold. Only titles go above medium.
- **Visual weight.** The big mallow flower sits bottom-right; a small blurred flower, foliage and bokeh counterweight it top-left and bottom-left. The centre, where windows live, stays quiet.
- **Texture.** A faint soft-light grain adds organic warmth and stops gradient banding; it scales with local lightness so it never adds noise to dark areas.
- **Never colour alone.** Pass / fail, status and focus always pair colour with text, shape or a ring.
- **Defaults win.** The dial has a detent at the middle, so the tuned default is easy to return to.

## Wallpaper measurements (`tools/wallpaper_test.py`)
| Check | Light (Dawn) | Dark (Dusk) |
|---|---|---|
| Mean lightness L\* (target band) | 83.2 (66–90) | 21.0 (8–28) |
| 99th-percentile chroma (≤ 0.14) | 0.083 | 0.103 |
| Visual-weight centroid offset (≤ 0.20) | dx +0.01, dy +0.07 | dx +0.04, dy +0.00 |
| Quiet centre vs busy corner (≤ 0.75) | 0.35 | 0.51 |
| Worst 1 % pixel under glass, body text (≥ 7:1) | 12.0 (soft end 8.8) | 9.9 (soft end 7.5) |
| Worst 1 % pixel under glass, muted text (≥ 4.5:1) | 5.9 (soft end 4.5) | 5.8 (soft end 4.7) |

Wallpaper files are in `assets/wallpapers/` (Dawn = light, Dusk = dark; 2560×1440 and 1170×2532).

## Tuning
All balance values come from `--p` (0 soft … 100 crisp, default 50) in `docs/gui/index.html`. The Rust defaults in `malva-theme` equal the `--p: 50` values, and `tools/verify_tokens.py` checks them.
