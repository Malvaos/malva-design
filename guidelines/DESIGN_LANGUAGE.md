# MalvaOS Design Language & Token Specification (`malva-theme`)

## 1. Brand palette (from the Coolors "Malva" palette)
| Name   | Hex       | Role                                   |
|--------|-----------|----------------------------------------|
| Petal  | `#E6DAE8` | lightest lilac neutral                 |
| Lilac  | `#DEC3E0` | selection and hover washes             |
| Orchid | `#B84F9F` | dark-mode accent seed                  |
| Plum   | `#8C3274` | light-mode accent seed                 |
| Leaf   | `#274903` | secondary seed (green)                 |

Constants live in `malva_theme::brand`. The mallow flower (five petals, radiating plum veins, green centre) is the identity mark.

## 2. Perceptual color system (OKLCH)
Accent, hover, pressed, focus ring and secondary colors are synthesized from a seed in OKLCH
(`accent_seed_hex`: Orchid in Dark, Plum in Light). Tonal stop choice per polarity:

| Role          | Dark stop | Light stop |
|---------------|-----------|------------|
| accent        | 400       | 700        |
| accent_hover  | 300       | 800        |
| accent_active | 500       | 900        |
| focus_ring    | 300       | 700        |
| secondary     | Leaf 400  | Leaf 800   |

Neutrals are warm aubergine (not blue-grey): Dark `#180B16` / `#241120`, Light `#F8F3F9` / `#FFFFFF`.
Success, warning and danger are polarity-aware. Foregrounds (`on_accent`, `on_secondary`, `on_danger`) are chosen by `accessible_on`.

## 3. Accessibility contract (enforced by tests)
Every variant (dark, light, dark high-contrast, light high-contrast) must satisfy:
- body text on surfaces ≥ 7:1 (≥ 12:1 in high contrast); muted text ≥ 4.5:1 (≥ 7:1 in high contrast)
- text on accent / accent_hover / accent_active / secondary / danger ≥ 4.5:1
- accent, focus ring, secondary, success, warning, danger against surfaces ≥ 3:1

Run `cargo test -p malva-theme`, or without a Rust toolchain `python3 tools/verify_tokens.py`.

## 4. Spacing (4-pt grid)
`xxs 4`, `xs 8`, `sm 12`, `md 16`, `lg 24`, `xl 32`, `xxl 48` px.

## 5. Continuous-curvature squircle radii
`xs 4`, `sm 8`, `md 12`, `lg 16`, `xl 24`, `pill 9999` px.

## 6. Opacity tokens (`OpacityTokens`)
`disabled 0.40`, `hover_wash 0.10`, `pressed_wash 0.16`.

## 7. Elevation & vibrancy
`level0` (flat) through `level4` (24 px ambient blur, 44 px key blur, 32 px dual-Kawase backdrop blur).

## 8. Visual references
`docs/visuals/` holds the design sheets (colors and shapes, components, icons and desktop) and
contrast-annotated snapshots of the resolved tokens for all four theme variants.
