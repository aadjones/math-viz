# math-viz

Manim animation pipeline for math educational articles. Paper-like aesthetic—warm cream, not 3b1b black.

## Render

```bash
./render.sh <scene_name>          # MP4
./render.sh <scene_name> --gif    # GIF
```

The script auto-derives the CamelCase class name from the snake_case filename (e.g. `long_division_792` → `LongDivision792`).

Output: `media/videos/<scene_name>/1080p60/<ClassName>.mp4`

## Project structure

```
shared/theme.py   — all colors + font (single place to restyle)
shared/grid.py    — DigitGrid class
scenes/           — one file per animation; import shared modules
```

## DigitGrid

`DigitGrid` maps `(col, row)` addresses to Manim scene coordinates.

**Conventions:**
- `col` increases rightward
- `row` increases downward (row 0 is top)
- `origin` = scene coordinate of the `(0, 0)` anchor

```python
g = DigitGrid(cell_w=0.45, cell_h=0.45, origin=np.array([-2.25, 2.8, 0.0]))
g.pos(col, row)               # → np.ndarray scene coordinate
g.char("7", col, row)         # → Text mobject (INK color by default)
g.char("3", col, row, color=RED_PEN)   # quotient digits use RED_PEN
g.hline(c0, c1, row)          # → Line mobject
g.bg_grid()                   # → VGroup of faint graph-paper lines
```

## Long division layout conventions

These row/col offsets were settled by visual tuning—don't change without re-checking all steps.

- **Quotient:** row `-1.5`, above the vinculum
- **Vinculum:** row `-0.8`
- **Step bases** (one per division step): `[0.0, 4.5, 9.0, 13.5]`
- Per step: product at `base + 1.5`, subtraction line at `base + 2.2`, remainder at `base + 3.0`

## Adding a new scene

1. Create `scenes/<snake_case_name>.py`
2. Class name must be the CamelCase equivalent (the render script derives it automatically)
3. Import theme colors from `shared.theme` and `DigitGrid` from `shared.grid`
4. Test with `./render.sh <snake_case_name>`

## Aesthetic

See `shared/theme.py` for palette and font. To reskin everything, change `MONO_FONT` and the color constants there—all scenes inherit them automatically.
