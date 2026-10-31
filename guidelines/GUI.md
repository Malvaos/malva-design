# Malva OS GUI kit (`docs/gui/index.html`)
Open the file in any modern browser. It is a living reference for how the Rust widgets should look and behave.

## Balance dial and wallpaper
Settings > Appearance has a Soft / Balanced / Crisp dial (snaps to the middle) and a wallpaper picker (Mallow, Gradient, Plain). See `docs/BALANCE.md` for the reasoning and measurements.

## Shell
Top bar with Spotlight and quick settings, a draggable glass Settings window (close / minimise / zoom), a dock with magnification, a context menu, toasts and modal dialogs.

## Interaction rules
- **State layers:** hover 8 %, pressed 14 % overlay of the label colour on every button; pressed also scales to 0.96.
- **Focus:** 2 px accent ring with a 2 px surface halo so it reads on any background; shown for keyboard focus only.
- **Motion:** 120 ms for state feedback, 240 ms for open / close, spring easing `cubic-bezier(.34,1.35,.64,1)`. Reduce motion sets both to 0.
- **Glass:** 20 px blur, 1.3 saturation, about 80 % opaque so text stays legible over any wallpaper, 1 px inner highlight. High contrast turns glass opaque and borders solid.
- **Forms:** validation appears after the user leaves a field, never while typing. Touch targets are at least 44 px.
- **Keyboard:** Ctrl K or `/` Spotlight, arrow keys in tabs / menus / Spotlight, Esc closes any overlay.

## Tests
`python3 tools/gui_test.py` runs 38 browser checks (contrast for 4 variants at 3 balance settings, middle-band check, dial, wallpaper picker, keyboard, overlays, dock, drag, phone layout). `python3 tools/wallpaper_test.py` runs 18 pixel checks on the wallpaper. The Tokens tab runs the same WCAG pairs live.
Screenshots from a passing run are in `docs/visuals/gui/`.
