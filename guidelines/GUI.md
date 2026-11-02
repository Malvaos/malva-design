# Malva OS GUI rules

How the widgets behave. How they look is in `DESIGN_LANGUAGE.md`; the working reference is the Malva UI kit
(github.com/Malvaos/Malva-ui-toolkit), and the interactive prototypes of every app are in `prototypes/html`.

## Shell

A top bar with quick settings, a dock with magnification, a context menu, toasts and modal dialogs. Open any file in
`prototypes/html` in a browser; `Taskbar.html`, `Control_center.html` and `clock widget.html` show the shell parts.

## Interaction rules

* **States.** Every interactive control has five: rest, hover, pressed, focus, disabled. Hover and pressed shift the fill one step (`accent-hover`, `accent-press`; the secondary and ghost equivalents); pressed also scales to 0.98 in 90 ms.
* **Focus.** A 2 px ring in `focus`, 2 px outside the control, so it reads on any background. It shows for keyboard focus only.
* **Disabled.** Fill drops to `accent-disabled` or the text to `disabled-text`; a disabled control is never hidden.
* **Motion.** 160 ms for hover, 240 ms for open, 160 ms for close; the spring `cubic-bezier(0.34, 1.35, 0.64, 1)` only where something arrives.
* **Glass.** A translucent plate of the surface colour (the `glass` token, 72 to 76 % opaque) with a 1 px sheen along its top edge and a hairline outside. The compositor supplies the blur behind it.
* **Forms.** Validation appears after the person leaves a field, never while typing. Destructive actions use `danger-fill` and are never the default button. Colour always comes with text or an icon.
* **Size.** Controls are never shorter than 32 px; on touch layouts use the large size (48 px).
* **Keyboard.** Ctrl K or `/` opens search, arrow keys move in tabs and menus, Esc closes any overlay.
