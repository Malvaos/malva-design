# Malva design language and token specification

The written specification of how Malva looks. The numbers come from `tokens/tokens.json` (and `dark.toml`, `light.toml`), which
`tools/sync_tokens.py` writes from the Malva UI kit's single token file; if this page and the tokens ever disagree, the tokens win.

## 1. Black and white, with the logo's colour

The interface is neutral: grey surfaces, charcoal and silver text, a razor-thin border. One colour is allowed to be strong, and it
is the logo's: Plum `#8C3274` (the mark's gradient runs Plum to Orchid `#B84F9F`), lightened to `#DC73C2` in
dark so it keeps its contrast. It works like the brand blue of a phone maker whose interface is black and white: a signal, not a
wallpaper. It marks **what you can act on** and **what is selected**.

| Accent appears on | Accent does not appear on |
|---|---|
| Primary buttons, links, ghost-button text | Window, card, sidebar and menu backgrounds |
| The on state of a switch, checked boxes, radio dots | Body text, headings, borders, dividers |
| The slider fill and progress fill | Icons at rest (they are `text-2`) |
| Selection (a faint wash over the neutral), the focus ring | Shadows (they are black) |
| The running dot in the dock, today in the calendar | Status (success is green, warning amber, danger red, info blue) |

## 2. Brand palette (the logo)

| Name | Hex | Role |
|---|---|---|
| Petal | `#E6DAE8` | lightest lilac; logo and illustration only |
| Lilac | `#DEC3E0` | logo and illustration only |
| Orchid | `#B84F9F` | the lighter end of the mark's gradient |
| Plum | `#8C3274` | the accent in light mode; the other end of the gradient |
| Leaf | `#274903` | the flower's centre |
| Ink | `#2A1226` | the wordmark |

The mallow flower (five heart-shaped petals around a leaf-green centre, each petal with one small notch) is the identity mark.
Interface roles never use petal, lilac or ink.

## 3. Colour roles

| Role | Light | Dark | Used for |
|---|---|---|---|
| `bg` | `#F5F5F7` | `#161617` | The canvas behind everything |
| `panel` | `#EDEDF0` | `#1A1A1B` | Sidebars and title bars |
| `surface` | `#FFFFFF` | `#1E1E1F` | Windows, cards, content |
| `raised` | `#FFFFFF` | `#29292B` | Menus, popovers, dialogs, toasts (one step above the window) |
| `border` | `#E5E5EA` | `#2C2C2E` | Hairlines round cards and secondary buttons |
| `text` | `#1D1D1F` | `#F5F5F7` | Charcoal, never stark black; silver, never glaring white |
| `text-2` | `#86868B` | `#8E8E93` | Secondary text, hierarchy |
| `muted` | `#A1A1A6` | `#6E6E73` | Placeholders, hints |
| `accent` | `#8C3274` | `#DC73C2` | Primary buttons, links, switches that are on, selection, focus |
| `accent-hover` | `#5D2950` | `#F093D7` | Hover on accent |
| `accent-press` | `#47253F` | `#C75EAE` | Pressed on accent |
| `on-accent` | `#FFFFFF` | `#1D1D1F` | Text and icons on the accent |
| `accent-wash` | `#EBE2EA` | `#422A3D` | A faint accent wash over a neutral: the selected row |
| `focus` | `#8C3274` | `#F093D7` | The 2 px focus ring |
| `danger` | `#D6414F` | `#FF7A85` | Destructive actions and errors |
| `success` | `#3F8A1E` | `#7FD35A` | Success |
| `warning` | `#F2A33A` | `#FFB85C` | Warnings |
| `info` | `#2F6FD6` | `#6BA3FF` | Information (blue, so a notice is never mistaken for the brand) |

All 56 roles, including the hover, pressed, disabled and soft variants, are in `tokens/tokens.json`. Elevation in light mode is
shadow; in dark mode it is a lighter surface plus a stronger shadow (`surface` to `raised`). Never tint a neutral toward the brand:
greys stay grey.

## 4. Accessibility contract

Measured from the tokens when this page was written (WCAG 2.x relative luminance). The UI kit's tests enforce the same limits.

| Pair | Light | Dark | Minimum | Result |
|---|---|---|---|---|
| Text on canvas | 15.5 : 1 | 16.6 : 1 | 4.5 : 1 | pass |
| Text on surface | 16.8 : 1 | 15.3 : 1 | 4.5 : 1 | pass |
| Secondary text on surface | 3.6 : 1 | 5.1 : 1 | 3 : 1 | pass (the specified grey; supporting text only) |
| Muted text on surface | 2.6 : 1 | 3.3 : 1 | 2.5 : 1 | pass (placeholders and hints only) |
| Label on accent | 7.4 : 1 | 5.8 : 1 | 4.5 : 1 | pass |
| Accent on surface (controls, focus) | 7.4 : 1 | 5.8 : 1 | 3 : 1 | pass (non-text contrast) |
| Danger text on surface | 5.5 : 1 | 6.6 : 1 | 4.5 : 1 | pass |
| Success text on surface | 6.3 : 1 | 9.0 : 1 | 4.5 : 1 | pass |
| Warning text on surface | 6.3 : 1 | 9.7 : 1 | 4.5 : 1 | pass |
| Info text on surface | 7.0 : 1 | 6.6 : 1 | 4.5 : 1 | pass |

`text-2` (`#86868B` on white) and `muted` are the greys that were specified for the system look, and they sit below the usual
4.5 : 1 for small text, so they are held to 3 : 1 and 2.5 : 1 and are only for supporting text. Anything a person must read to act
(labels, button text, errors, values) is `text` or a status text colour.

## 5. Spacing (4-point scale)

`xxs 4`, `xs 8`, `s 12`, `m 16`, `l 24`, `xl 32`, `xxl 48` px.

## 6. Radii

`xs 6` (chips, checkboxes), `s 10` (buttons, fields), `m 14` (menus), `l 22` (cards, dialogs), `xl 36`
(the app-icon squircle), `pill 999`.

## 7. Sizes

Controls are 32 / 40 / 48 px tall (small, medium, large) and never shorter than 32; fields are
42. Switch 52 x 30, checkbox 26, radio 28, slider thumb 22, focus ring 2 px at
2 px offset, menu 230 wide with 34 px rows, dialog 400, toast 380, title bar 44. The full list is `size` in the tokens.

## 8. Type

Inter for the interface, JetBrains Mono for code.

| Role | Size / line | Weight |
|---|---|---|
| title | 28 / 34 | 700 |
| heading | 20 / 26 | 600 |
| body | 14 / 20 | 400 |
| body-strong | 14 / 20 | 600 |
| label | 13 / 18 | 600 |
| caption | 12 / 16 | 400 |
| mono | 13 / 18 | 400 |

## 9. Motion

Motion explains; it never decorates. Press is instant, hover is quick, things that arrive take a little longer than things that leave.

| Duration | ms |
|---|---|
| `press` | 90 |
| `hover` | 160 |
| `fade` | 200 |
| `open` | 240 |
| `close` | 160 |
| `slow` | 380 |

| Easing | cubic-bezier |
|---|---|
| `out` | (0.0, 0.0, 0.2, 1.0) |
| `standard` | (0.2, 0.0, 0.0, 1.0) |
| `soft` | (0.4, 0.0, 0.2, 1.0) |
| `spring` | (0.34, 1.35, 0.64, 1.0) |
| `exit` | (0.4, 0.0, 1.0, 1.0) |

A spring (stiffness 420, damping 32, mass 1) is for things that follow a pointer, such as the dock's magnification.

## 10. Elevation

| Level | y | blur | shadow alpha, light | shadow alpha, dark |
|---|---|---|---|---|
| 1 | 1 | 3 | 0.08 | 0.4 |
| 2 | 6 | 18 | 0.12 | 0.5 |
| 3 | 16 | 40 | 0.18 | 0.6 |

Shadows are black. On glass (the dock, the menu bar) the compositor supplies the backdrop blur; a UI toolkit that cannot blur draws a
translucent plate instead.

## 11. What changed from the previous version

* Surfaces, text and borders are neutral (they used to tint toward plum). The accent is the logo's plum and orchid, only on what can be acted on.
* The TOML files carry the colours as explicit roles. They no longer hold only an accent seed for tonal synthesis.
* Keys follow the UI kit: spacing `s`, `m`, `l` (was `sm`, `md`, `lg`), radii `xs`, `s`, `m`, `l`, `xl`, `pill` with new values, and new `sizes`, `motion` and `elevation` tables.
* The Balance dial and the high-contrast, reduced-transparency and reduced-motion flags are not part of the UI kit and are not in the tokens. The accessibility contract above is measured on the one default.
