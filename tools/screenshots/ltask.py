"""Ltask (task manager) screenshots -> screenshots/ltask/*.jpg. Run: python3 tools/screenshots/ltask.py"""
from common import browser, open_page, snap

APP = "ltask"
PAGE = "Ltask.html"


def theme(pg, t):
    """Use the app's own theme button (it also repaints the canvas graphs); programmatic click works under a modal."""
    cur = pg.evaluate("document.documentElement.getAttribute('data-theme')==='light'?'light':'dark'")
    if cur != t:
        pg.evaluate("document.getElementById('theme-btn').click()")
        pg.wait_for_timeout(500)


def away(pg):
    pg.mouse.move(2, 2)
    pg.wait_for_timeout(150)


def fresh(b, t, old=None):
    if old:
        old.close()
    pg = open_page(b, PAGE, "dark")
    theme(pg, t)
    away(pg)
    return pg


def both(b, name, steps, pair=True):
    """Fresh page per theme, run steps(pg), snap name-dark / name-light (or just `name` when pair is False)."""
    for t in (("dark", "light") if pair else ("dark",)):
        pg = fresh(b, t)
        steps(pg)
        snap(pg, APP, f"{name}-{t}" if pair else name)
        pg.close()


def sel_row(pg, rid):
    pg.click(f'.row[data-id="{rid}"] .sel')
    away(pg)


with browser() as b:
    # 01-09 Processes tab
    both(b, "01-processes", lambda pg: None)

    def collapse(pg):
        pg.click('.row[data-id="browser"] .exp'); away(pg)
    both(b, "02-processes-collapsed-group", collapse)

    def search(pg):
        pg.click("#q"); pg.keyboard.type("term"); away(pg)
    both(b, "03-processes-search", search)

    def sort_mem(pg):
        pg.click('[data-sort="mem"]'); away(pg)
    both(b, "04-processes-sorted-by-memory", sort_mem, pair=False)

    def eff(pg):
        sel_row(pg, "files"); pg.click("#effBtn"); away(pg)
    both(b, "05-processes-efficiency-mode", eff)

    def end_dlg(pg):
        sel_row(pg, "viewer"); pg.click("#endBtn"); pg.wait_for_selector("#tmdlg[open] #endGo"); away(pg)
    both(b, "06-processes-end-task-dialog", end_dlg)

    def run_dlg(pg):
        pg.click("#runBtn"); pg.wait_for_selector("#tmdlg[open] #cmd"); away(pg)
    both(b, "07-processes-run-new-task", run_dlg)

    def run_typing(pg):
        run_dlg(pg); pg.keyboard.type("lion-t")
    both(b, "08-processes-run-new-task-typing", run_typing, pair=False)

    def scrolled(pg):
        pg.evaluate("const e=document.getElementById('procBody');e.scrollTop=e.scrollHeight"); away(pg)
    both(b, "09-processes-background-scrolled", scrolled)

    # 10-19 Performance tab (one page, themes switched with the app button)
    pg = fresh(b, "dark")
    pg.click('.nav-tab[data-target="performance"]'); away(pg)

    def hw(k):
        pg.click(f'.hw-item[data-hw="{k}"]'); away(pg)

    def ctrl(sel):
        pg.click(sel); away(pg)

    def pair(name):
        for t in ("dark", "light"):
            theme(pg, t); away(pg)
            snap(pg, APP, f"{name}-{t}")
        theme(pg, "dark"); away(pg)

    pair("10-performance-cpu")
    ctrl("#btn-cpu-threads")
    pair("11-performance-cpu-threads")
    hw("mem")
    pair("12-performance-memory")
    ctrl("#btn-mem-split")
    snap(pg, APP, "13-performance-memory-split")
    hw("disk")
    pair("14-performance-disks")
    ctrl('[data-disk-idx="1"]')
    snap(pg, APP, "15-performance-disk-2")
    hw("net")
    pair("16-performance-network")
    ctrl("#btn-net-split")
    snap(pg, APP, "17-performance-network-split")
    hw("gpu")
    pair("18-performance-gpu")
    ctrl("#btn-gpu-engines")
    snap(pg, APP, "19-performance-gpu-engines")

    # 20-22 Startup apps and Services
    pg.click('.nav-tab[data-target="startup"]'); away(pg)
    pair("20-startup-apps")
    pg.click("#startup-list tr:nth-child(1) .toggle")
    pg.click("#startup-list tr:nth-child(3) .toggle")   # mouse stays over row 3, as in the original
    snap(pg, APP, "21-startup-apps-toggled")
    pg.click('.nav-tab[data-target="services"]'); away(pg)
    pair("22-services")
