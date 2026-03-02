"""DigitGrid — positions characters on a column/row grid.

Grid convention:
  - col increases rightward  (like reading left-to-right)
  - row increases downward   (like reading top-to-bottom on a page)
  - origin = scene coordinate of the (col=0, row=0) anchor point

Usage in a scene::

    g = DigitGrid(cell_w=0.45, cell_h=0.45, origin=np.array([-2.25, 2.8, 0.0]))
    digit = g.char("7", col=5, row=0)
    line  = g.hline(col_start=4.4, col_end=5.6, row=2.2)
    bg    = g.bg_grid()
"""

import numpy as np
from manim import Line, Text, VGroup

from shared.theme import GRID_LINE, INK, MONO_FONT, FONT_SIZE


class DigitGrid:
    """Converts (col, row) grid addresses into Manim scene coordinates."""

    def __init__(
        self,
        cell_w: float = 0.45,
        cell_h: float = 0.45,
        origin: np.ndarray = None,
        font_size: int = FONT_SIZE,
    ):
        self.cell_w = cell_w
        self.cell_h = cell_h
        self.origin = origin if origin is not None else np.zeros(3)
        self.font_size = font_size

    # ── Coordinate conversion ─────────────────────────────────────────────────

    def pos(self, col: float, row: float) -> np.ndarray:
        """Return the 3-D scene coordinate for grid position (col, row)."""
        return np.array([
            self.origin[0] + col * self.cell_w,
            self.origin[1] - row * self.cell_h,
            0.0,
        ])

    # ── Mobject factories ─────────────────────────────────────────────────────

    def char(
        self,
        c: str,
        col: float,
        row: float,
        color=None,
        font_size: int = None,
    ) -> Text:
        """A single-character Text mobject centered at (col, row)."""
        ink = color or INK
        mob = Text(c, font=MONO_FONT, font_size=font_size or self.font_size, color=ink)
        # Set stroke_color to match fill so Write's tracing phase uses ink, not white.
        mob.set_stroke(color=ink)
        mob.move_to(self.pos(col, row))
        return mob

    def hline(
        self,
        col_start: float,
        col_end: float,
        row: float,
        color=None,
        stroke_width: float = 1.8,
    ) -> Line:
        """Horizontal line from col_start to col_end at the given row."""
        return Line(
            self.pos(col_start, row),
            self.pos(col_end, row),
            color=color or INK,
            stroke_width=stroke_width,
        )

    # ── Background ────────────────────────────────────────────────────────────

    def bg_grid(
        self,
        step: float = 0.45,
        x_range: tuple = (-7.5, 7.5),
        y_range: tuple = (-4.2, 4.2),
        opacity: float = 0.25,
    ) -> VGroup:
        """Full-screen faint graph-paper background (independent of digit grid)."""
        lines = VGroup()
        x = x_range[0]
        while x <= x_range[1] + 1e-6:
            l = Line([x, y_range[0], 0], [x, y_range[1], 0],
                     stroke_color=GRID_LINE, stroke_width=0.5)
            l.set_stroke(opacity=opacity)
            lines.add(l)
            x = round(x + step, 6)
        y = y_range[0]
        while y <= y_range[1] + 1e-6:
            l = Line([x_range[0], y, 0], [x_range[1], y, 0],
                     stroke_color=GRID_LINE, stroke_width=0.5)
            l.set_stroke(opacity=opacity)
            lines.add(l)
            y = round(y + step, 6)
        return lines
