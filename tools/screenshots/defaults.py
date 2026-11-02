"""Captures the first state of every prototype (the ones that need no click-through): screenshots/<app>/<name>.jpg.
    python3 tools/screenshots/defaults.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common

# (screenshot folder, prototype, file name, theme, action) - action: a text to click first, or "BAR" for the 1440 x 100 top strip
SHOTS = [
    ('calculator', 'Calculator.html', '01-basic-dark', 'dark', None),
    ('calculator', 'Calculator.html', '01-basic-light', 'light', None),
    ('control-center', 'Control_center.html', '01-default-dark', 'dark', None),
    ('control-center', 'Control_center.html', '01-default-light', 'light', None),
    ('image-viewer', 'Image_Viewer.html', '01-viewer-dark', 'dark', None),
    ('image-viewer', 'Image_Viewer.html', '01-viewer-light', 'light', None),
    ('ltask', 'Ltask.html', '01-processes-dark', 'dark', None),
    ('ltask', 'Ltask.html', '01-processes-light', 'light', None),
    ('settings', 'Settings.html', '01-wi-fi-dark', 'dark', 'Wi-Fi'),
    ('settings', 'Settings.html', '01-wi-fi-light', 'light', 'Wi-Fi'),
    ('lingmo-installer', 'Lingmoinstaller.html', '01-step-01-language-dark', 'dark', None),
    ('lingmo-installer', 'Lingmoinstaller.html', '01-step-01-language-light', 'light', None),
    ('web-browser', 'Web_Browser.html', '01-start-page-dark', 'dark', None),
    ('web-browser', 'Web_Browser.html', '01-start-page-light', 'light', None),
    ('taskbar', 'Taskbar.html', '01-default-dark', 'dark', None),
    ('taskbar', 'Taskbar.html', '01-default-light', 'light', None),
    ('taskbar', 'Taskbar.html', '01-default-dark-bar', 'dark', 'BAR'),
    ('taskbar', 'Taskbar.html', '01-default-light-bar', 'light', 'BAR'),
    ('files', 'leonux_files.html', '01-home', 'dark', None),
    ('documents', 'leonux_documents.html', '01-recent', 'dark', None),
    ('notes', 'Notes.html', '01-write', 'dark', None),
    ('media-center', 'Media.html', '01-track-1', 'dark', None),
    ('ldisk', 'LDisk.html', '01-device-1', 'dark', 'Samsung SSD 990 PRO'),
    ('terminal', 'terminal.html', '01-default', 'dark', None),
    ('login-screen', 'Ldm.html', '01-default', 'dark', None),
    ('display-manager', 'leonux_display_manager.html', '01-default', 'dark', None),
    ('deb-installer', 'Installer.html', '01-drop-zone', 'dark', None),
    ('settings-fonts', 'leonux_settings_fonts.html', '01-top', 'dark', None),
    ('clock-widget', 'clock widget.html', '01-default', 'dark', None),
]

with common.browser() as b:
    for folder, html, name, theme, action in SHOTS:
        pg = common.open_page(b, html, theme)
        clip = None
        if action == "BAR":
            clip = {"x": 0, "y": 0, "width": 1440, "height": 100}
        elif action:
            pg.get_by_text(action, exact=True).first.click()
        common.snap(pg, folder, name, clip=clip)
        pg.close()
