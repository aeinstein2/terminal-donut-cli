# terminal-donut-cli

A tiny Python CLI that renders the classic rotating ASCII donut in your terminal.

## Requirements

- Python 3.10+

## Run

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

## Install as a command (optional)

```bash
pip install .
donut
```
