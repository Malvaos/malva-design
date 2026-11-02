# Screenshots

Renders of the interactive prototypes in `prototypes/html`, 1440 x 900 JPEG, named `NN-state[-theme].jpg`, one folder per app.

* **`<app>/`** holds captures of the current look (neutral surfaces, the logo-colour accent). They are made by the scripts in
  `tools/screenshots/`, which open each prototype in Chromium (Playwright), set the theme, drive the app to a state and save it.
  `python3 tools/screenshots/run_all.py` regenerates all of them; `defaults.py` takes the first state of every app, and
  `calculator.py` and `ltask.py` take every state of those two apps.
* **`_old-look/<app>/`** holds the captures of the states that have no script yet, from before the look changed (plum-tinted
  surfaces). They show the right states in the old colours, so the list of states is not lost. A file is deleted from here when a
  script produces the same name in `<app>/`.

| App | Current look | Old look (no script yet) |
|---|---|---|
| `calculator` | 9 | 0 |
| `clock-widget` | 1 | 0 |
| `control-center` | 2 | 8 |
| `deb-installer` | 1 | 5 |
| `display-manager` | 1 | 8 |
| `documents` | 1 | 9 |
| `files` | 1 | 11 |
| `image-viewer` | 2 | 9 |
| `ldisk` | 1 | 10 |
| `lingmo-installer` | 2 | 22 |
| `login-screen` | 1 | 3 |
| `ltask` | 37 | 0 |
| `media-center` | 1 | 7 |
| `notes` | 1 | 8 |
| `settings` | 2 | 41 |
| `settings-fonts` | 1 | 6 |
| `taskbar` | 4 | 8 |
| `terminal` | 1 | 12 |
| `web-browser` | 2 | 7 |
| **Total** | **71** | **174** |

To add a state, write a few lines next to `defaults.py` that open the prototype with `common.open_page`, click to the state and call
`common.snap(page, "<app>", "<name>")`, add the file to `run_all.py`, run it, and delete the same name from `_old-look/`.
