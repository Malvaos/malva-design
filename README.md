# malva-design

The design source of truth for **Malva OS**: brand, tokens, guidelines, reference sheets and the interactive HTML prototypes of
every app. The code is built from this and checked against it.

The look is **black and white with the logo's colour**: neutral grey surfaces, charcoal and silver text, a hairline border, and one
strong colour, the logo's plum, used only on what you can act on.

```
brand/
  logo/            the mallow-flower mark, lockups (light and reverse), app icon, guidelines sheet (SVG + PNG)
  wallpapers/      Malva Dawn and Dusk (the brand artwork), Silver and Graphite (neutral, used by the prototypes);
                   desktop 2560x1440 and mobile 1170x2532
tokens/
  tokens.json      every value: 56 colour roles in light and dark, brand colours, radii, spacing, sizes, type, motion, elevation
  dark.toml        the same, as TOML (accent seed 0xDC73C2)       light.toml   (accent seed 0x8C3274)
guidelines/
  DESIGN_LANGUAGE.md   the specification: colour roles, contrast table, scales    BALANCE.md   why each value sits where it does
  GUI.md               how the widgets behave
reference/
  components/      state sheets of the UI kit's components (buttons, controls, inputs, navigation, feedback, surfaces,
                   window chrome, typography), light and dark
  sheets/          palette, component specimen (light and dark), icon sheet, overview
prototypes/
  html/            working apps; open any file in a browser (Settings, Files, Ltask, Calculator, Image Viewer, Web Browser,
                   Notes, Media, Terminal, LDisk, installers, login screens, widgets)
screenshots/       71 current-look renders and 174 older ones waiting for a script (see screenshots/README.md)
tools/
  sync_tokens.py   rewrites tokens/ from the UI kit's token file
  screenshots/     Playwright scripts that render the prototypes
```

## The system in brief

* **Neutral surfaces.** Light: canvas `#F5F5F7`, cards `#FFFFFF`, text `#1D1D1F`, secondary `#86868B`, border `#E5E5EA`.
  Dark: canvas `#161617`, cards `#1E1E1F`, text `#F5F5F7`, secondary `#8E8E93`, border `#2C2C2E`. Greys are never tinted toward the brand.
* **One accent, the logo's.** Plum `#8C3274` in light, lightened to `#DC73C2` in dark. It marks primary buttons, links, switches that are on,
  selection and the focus ring, and nothing else. Status colours are their own: green, amber, red, blue.
* **Shape.** Radii 6 / 10 / 14 / 22 / 36 px; controls 32, 40 or 48 px tall; a 4-point spacing scale.
* **Motion.** 90 ms press, 160 ms hover, 240 ms open, a small spring only where something arrives.
* **States.** Rest, hover, pressed, focus (a 2 px ring), disabled. Destructive actions are red and never the default; fields validate
  after you leave them; colour is never the only signal.
* **Contrast.** Measured in `guidelines/DESIGN_LANGUAGE.md`: body text 15 to 17 : 1, label on accent 5.8 to 7.4 : 1.

## Tokens

`tokens/` is generated, not edited by hand. The source is the Malva UI kit's `tokens/malva-tokens.json` and `dist/resolved.json`:

```
python3 tools/sync_tokens.py --kit /path/to/malva-ui-kit          # rewrite tokens/
python3 tools/sync_tokens.py --kit /path/to/malva-ui-kit --check  # exit 1 if tokens/ is stale, 2 if the kit is not found
```

Without `--kit` it looks at `$MALVA_KIT`, then `../Malva-ui-toolkit`, then `../malva-ui-kit`. If a prototype and the tokens ever
disagree, the tokens win.

## Using the prototypes

Open any file in `prototypes/html/` in a browser; they load their wallpapers from `../../brand/wallpapers/`, so keep the folder layout.
Control Center, Taskbar, Ltask, the installer, Settings, Calculator, Image Viewer and Web Browser have a light theme (toggle in the app);
the rest are dark only. `Settings.html` loads its detail pages from `settings-pages/` and needs `settings.css` / `settings.js` beside it.

To re-render the screenshots: `pip install playwright && playwright install chromium`, then `python3 tools/screenshots/run_all.py`.

## Known gaps

* **Names.** The prototypes still carry the earlier product names (Lion, LionOS, Leonux, Lingmo) in titles, labels and file names.
  Only colours, wallpapers and tokens were changed, not the wording.
* **Screenshots.** 174 of the 245 states are still the older plum-tinted renders, kept in `screenshots/_old-look/` until a script covers them.
* **Removed settings.** The Balance dial and the high-contrast, reduced-transparency and reduced-motion switches of the earlier system are
  not in the UI kit and are not in the tokens or guidelines. The Settings prototype may still show their pages (for example "Digital Balance");
  they are design sketches, not part of the system.
* **Brand artwork.** The logo files and the Dawn and Dusk wallpapers keep the logo's own colours and are untouched.
* **Licence.** Not chosen yet; add a `LICENSE` file before relying on the repo outside Malva OS.
