# malva-design

The design source of truth for **Malva OS**: brand, tokens, guidelines, reference sheets and the interactive HTML prototypes of every app. Code lives elsewhere (`malva-slint` for the UI toolkit); this repo is what the code is built from and checked against.

```
brand/
  logo/            the mallow-flower mark, lockups (light / reverse), app icon, guidelines sheet (SVG + PNG)
  wallpapers/      Malva Dusk and Dawn, desktop (2560x1440) and mobile (1170x2532)
tokens/
  dark.toml        the Rust theme defaults (balance 50)       tokens.json   the same values, plus radii, type, motion, states
  light.toml
guidelines/
  DESIGN_LANGUAGE.md   what Malva is and the rules    BALANCE.md   the Soft..Crisp dial and its formulas    GUI.md   widgets and interaction
reference/
  components/      per-component state sheets (default / hover / pressed / focus / disabled), light and dark
  sheets/          colours and shapes, components overview, desktop icons, palette.svg
prototypes/
  html/            working apps, open any file in a browser (Settings, Files, Ltask task manager, Backup-style flows,
                   Calculator, Image Viewer, Web Browser, Notes, Media, Terminal, LDisk, installers, login screens, widgets...)
screenshots/       245 renders of those prototypes, one folder per app, dark and light (1440 px wide)
```

## The system in brief
- **Accent:** dusty orchid `#D47ABC` on dark, plum `#7E376A` on light. Surfaces tint toward plum, never grey.
- **Balance dial:** 0 Soft ... 100 Crisp. Radii, UI weight, shadows and contrast move together; 50 is the tuned default (controls 12 px, windows 20 px, UI weight 500).
- **Motion:** 120 ms feedback, 240 ms overlays, a small spring only where something arrives; reduce-motion sets all to 0.
- **States:** hover wash 8 %, pressed 14 % with a 0.96 scale, disabled 40 %, 44 px touch targets, 2 px accent focus ring with a 2 px halo.
- **Behaviour:** destructive actions are rose and never the default; fields validate after you leave them; colour is never the only signal.

Full detail: `guidelines/`. Machine-readable values: `tokens/tokens.json`.

## Using the prototypes
Open any file in `prototypes/html/` in a browser. They load their wallpapers from `../../brand/wallpapers/`, so keep the folder layout. Control Center, Taskbar, Ltask, the Lingmo installer, Settings, Calculator, Image Viewer and Web Browser have a light theme (toggle in the app); the rest are dark-only, as designed.
`Settings.html` loads its ten detail pages from `settings-pages/` and needs its `settings.css` / `settings.js` beside it.

## Notes
- The HTML prototypes are design references, not product code. The product UI is built in Slint (`malva-slint`).
- Colour values here follow the balanced tokens. If `tokens/*.toml` and a prototype ever disagree, the TOML wins.
- Licence: not chosen yet - add a `LICENSE` file before making the repo public.
