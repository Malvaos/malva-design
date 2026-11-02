"""screenshots/calculator/: Calculator.html (basic and scientific, dark and light, history drawer)."""
from common import browser, open_page, set_theme, snap

APP = "calculator"


def press(pg, *keys):
    for k in keys:
        pg.click(f'#pad button[data-k="{k}"]')


def park(pg):
    pg.mouse.move(8, 8)  # keep the pointer off the keys so no hover state ends up in the image


with browser() as b:
    pg = open_page(b, "Calculator.html", "dark")
    park(pg)
    snap(pg, APP, "01-basic-dark")
    set_theme(pg, "light")
    snap(pg, APP, "01-basic-light")
    set_theme(pg, "dark")

    press(pg, "1", "2", "×", "3", ".", "5")
    park(pg)
    snap(pg, APP, "02-typing")

    press(pg, "=")
    park(pg)
    snap(pg, APP, "03-result-dark")
    set_theme(pg, "light")
    snap(pg, APP, "03-result-light")
    set_theme(pg, "dark")

    press(pg, "AC", "9", "+", "4", "=")
    pg.click("#hb")
    park(pg)
    snap(pg, APP, "04-history")
    pg.click("#hb")
    press(pg, "AC")

    pg.click('.m button[data-m="s"]')
    park(pg)
    snap(pg, APP, "05-scientific-dark")
    set_theme(pg, "light")
    snap(pg, APP, "05-scientific-light")
    set_theme(pg, "dark")

    press(pg, "√(", "8", "1", ")", "+", "π")
    park(pg)
    snap(pg, APP, "06-scientific-expression")
    pg.close()
