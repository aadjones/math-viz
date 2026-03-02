# math-viz

Manim animations for math articles. Paper-like aesthetic—warm cream background,
ink-dark strokes, red-pen quotient digits. No black backgrounds.

## Setup (macOS)

```bash
# 1. System deps
brew install ffmpeg cairo pango pkg-config

# 2. Python env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Render

```bash
# MP4 (1080p60, opens when done)
./render.sh long_division_792

# GIF
./render.sh long_division_792 --gif
```

Output lands in `media/videos/<scene_name>/1080p60/`.

## Project structure

```
math-viz/
├── scenes/
│   └── long_division_792.py    ← Manim scene (source of truth)
├── shared/
│   ├── theme.py                ← colors, font — edit here to restyle everything
│   └── grid.py                 ← DigitGrid helper used by all scenes
├── render.sh                   ← render any scene by name
├── requirements.txt
└── README.md
```

## Extending

**New long-division problem:** copy `scenes/long_division_792.py`, rename the class,
update the constants at the top, and swap in the new dividend/divisor/steps. Then
render with `./render.sh <new_scene_name>`.

**New animation topic:** create `scenes/your_topic.py`, import `DigitGrid` and the
theme, and write a new `Scene` subclass. The `shared/` module is the reusable foundation.

**Change the aesthetic:** edit `shared/theme.py`. Every scene picks up the change
automatically on next render.

**Font note:** `MONO_FONT = "Courier New"` in `shared/theme.py`. On Linux, swap to
`"Liberation Mono"` (install via `apt-get install fonts-liberation`).
