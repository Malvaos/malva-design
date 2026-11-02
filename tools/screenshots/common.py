"""Shared helpers for the screenshot scripts in this folder (one script per prototype).

Each script drives one HTML prototype in prototypes/html with Playwright (Chromium) and writes the JPEGs in
screenshots/<app>/ with the names the README lists. Run one with `python3 tools/screenshots/<app>.py`, all of them with
`python3 tools/screenshots/run_all.py`. Needs: python3, playwright (pip install playwright; playwright install chromium).

The prototypes are design references that run from file:// URLs, so nothing is served. Every page is 1440 x 900 unless a
script says otherwise (the taskbar strips are 1440 x 100)."""
import os, sys
from contextlib import contextmanager
from urllib.parse import quote
from playwright.sync_api import sync_playwright

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
HTML = os.path.join(ROOT, "prototypes", "html")
SHOTS = os.path.join(ROOT, "screenshots")
W, H = 1440, 900


@contextmanager
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch()
        try:
            yield b
        finally:
            b.close()


def open_page(b, html, theme="dark", size=(W, H), settle=700):
    """Open prototypes/html/<html> and switch it to `theme` ('dark' or 'light') through data-theme, the attribute the
    prototypes use. Returns the page. Scripts that need the app's own toggle click it instead."""
    pg = b.new_page(viewport={"width": size[0], "height": size[1]})
    pg.goto("file://" + quote(os.path.join(HTML, html)), wait_until="load")
    pg.wait_for_timeout(settle)
    set_theme(pg, theme)
    return pg


def set_theme(pg, theme):
    pg.evaluate(f"document.documentElement.setAttribute('data-theme','{theme}')")
    pg.wait_for_timeout(450)


def snap(pg, app, name, wait=350, clip=None):
    """Save screenshots/<app>/<name>.jpg (quality 82) after letting animations settle."""
    pg.wait_for_timeout(wait)
    d = os.path.join(SHOTS, app)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, name + ".jpg")
    pg.screenshot(path=path, type="jpeg", quality=82, **({"clip": clip} if clip else {}))
    print("  wrote", os.path.relpath(path, ROOT))
    return path
