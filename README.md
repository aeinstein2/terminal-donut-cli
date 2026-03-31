# terminal-donut-cli

A tiny donut project with two renderers:

- **Python CLI**: rotating ASCII donut in terminal
- **Web app**: browser simulator using `<pre>` + JS

## Requirements

- Python 3.10+ (for CLI)
- Any modern browser (for web app)

## Python CLI

```bash
python donut.py
```

Options:

```bash
python donut.py --fps 30 --width 100 --height 30 --frames 600
```

- `--fps`: animation speed
- `--width`: frame width
- `--height`: frame height
- `--frames`: optional number of frames before exit (omit for infinite)

Install as a command (optional):

```bash
pip install .
donut
```

## Web app

Open `index.html` in your browser.

It includes controls for:

- FPS
- Width / Height
- Pause / Resume
- Reset rotation
