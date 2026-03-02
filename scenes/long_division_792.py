"""LongDivision792 — animates 4 ) 792 = 198 step by step.

Layout (paper-like aesthetic, standard 16:9 frame):

  Col:         ·    5    6    7
  Row -1.5:         1    9    8    ← quotient (red pen)
  Row -0.8:    ⌐──────────────    ← bracket (vertical bar + vinculum)
  Row  0:   4  |    7    9    2    ← dividend

  Step 1  (7 ÷ 4 = 1 r3):     rows 1.5 / 2.2 / 3.0
  Step 2  (39 ÷ 4 = 9 r3):    rows 4.0 / 4.7 / 5.5
  Step 3  (32 ÷ 4 = 8 r0):    rows 6.5 / 7.2 / 8.0
"""

import sys
from pathlib import Path

import numpy as np
from manim import (
    VGroup,
    Create,
    Indicate,
    Line,
    Write,
    Scene,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from shared.theme import ACCENT, INK, PAPER_BG, RED_PEN
from shared.grid import DigitGrid

# ── Column addresses ──────────────────────────────────────────────────────────
C_D1  = 5   # dividend digit 1  →  "7"
C_D2  = 6   # dividend digit 2  →  "9"
C_D3  = 7   # dividend digit 3  →  "2"

# ── Row addresses ─────────────────────────────────────────────────────────────
R_QUOT  = -1.5   # quotient row (above vinculum)
R_VINC  = -0.8   # vinculum (overline above dividend)
R_DIVID =  0.0   # dividend

_STEP_BASES = [0.0, 2.5, 5.0]

def _step_rows(step_index: int):
    """Return (prod_row, line_row, rem_row) for step 0–2."""
    b = _STEP_BASES[step_index]
    return b + 1.5, b + 2.2, b + 3.0


class LongDivision792(Scene):
    """Full step-by-step long division of 792 ÷ 4 = 198."""

    def construct(self):
        self.camera.background_color = PAPER_BG

        g = DigitGrid(
            cell_w=0.45,
            cell_h=0.45,
            origin=np.array([-2.25, 2.8, 0.0]),
        )

        # ── Initial setup ────────────────────────────────────────────────────
        HOOK_COL = C_D1 - 0.6
        hook_top = g.pos(HOOK_COL, R_VINC)
        hook_bot = g.pos(HOOK_COL, R_DIVID + 0.6)
        vinc_end = g.pos(C_D3 + 0.55, R_VINC)

        divisor = g.char("4", HOOK_COL - 1.0, R_DIVID)
        bracket = VGroup(
            Line(hook_bot, hook_top, color=INK, stroke_width=1.8),
            Line(hook_top, vinc_end, color=INK, stroke_width=1.8),
        )
        d = {
            C_D1: g.char("7", C_D1, R_DIVID),
            C_D2: g.char("9", C_D2, R_DIVID),
            C_D3: g.char("2", C_D3, R_DIVID),
        }

        self.play(
            Write(divisor),
            Create(bracket),
            *[Write(v) for v in d.values()],
            run_time=1.5,
        )
        self.wait(0.8)

        # ══ Step 1: 7 ÷ 4 = 1, remainder 3 ══════════════════════════════════
        prod_r, line_r, rem_r = _step_rows(0)

        q1 = g.char("1", C_D1, R_QUOT, color=RED_PEN)
        self.play(Write(q1))
        self.wait(0.4)
        self.play(Indicate(divisor, color=ACCENT, scale_factor=1.3),
                  Indicate(q1,      color=ACCENT, scale_factor=1.3), run_time=0.5)

        minus1 = g.char("-", C_D1 - 1, prod_r)
        prod1  = g.char("4", C_D1,     prod_r)
        self.play(Write(minus1), Write(prod1))

        line1 = g.hline(C_D1 - 1.4, C_D1 + 0.55, line_r)
        self.play(Create(line1))

        rem1 = g.char("3", C_D1, rem_r)
        self.play(Write(rem1))
        self.wait(0.5)

        # ── Bring down "9" (C_D2) ────────────────────────────────────────────
        self._bring_down(g, d[C_D2], C_D2, rem_r)

        # ══ Step 2: 39 ÷ 4 = 9, remainder 3 ══════════════════════════════════
        prod_r, line_r, rem_r = _step_rows(1)

        q2 = g.char("9", C_D2, R_QUOT, color=RED_PEN)
        self.play(Write(q2))
        self.wait(0.4)
        self.play(Indicate(divisor, color=ACCENT, scale_factor=1.3),
                  Indicate(q2,      color=ACCENT, scale_factor=1.3), run_time=0.5)

        minus2 = g.char("-", C_D1 - 1, prod_r)
        prod2a = g.char("3", C_D1,     prod_r)
        prod2b = g.char("6", C_D2,     prod_r)
        self.play(Write(minus2), Write(prod2a), Write(prod2b))

        line2 = g.hline(C_D1 - 1.4, C_D2 + 0.55, line_r)
        self.play(Create(line2))

        rem2 = g.char("3", C_D2, rem_r)
        self.play(Write(rem2))
        self.wait(0.5)

        # ── Bring down "2" (C_D3) ────────────────────────────────────────────
        self._bring_down(g, d[C_D3], C_D3, rem_r)

        # ══ Step 3: 32 ÷ 4 = 8, remainder 0 ══════════════════════════════════
        prod_r, line_r, rem_r = _step_rows(2)

        q3 = g.char("8", C_D3, R_QUOT, color=RED_PEN)
        self.play(Write(q3))
        self.wait(0.4)
        self.play(Indicate(divisor, color=ACCENT, scale_factor=1.3),
                  Indicate(q3,      color=ACCENT, scale_factor=1.3), run_time=0.5)

        minus3 = g.char("-", C_D2 - 1, prod_r)
        prod3a = g.char("3", C_D2,     prod_r)
        prod3b = g.char("2", C_D3,     prod_r)
        self.play(Write(minus3), Write(prod3a), Write(prod3b))

        line3 = g.hline(C_D2 - 1.4, C_D3 + 0.55, line_r)
        self.play(Create(line3))

        rem3 = g.char("0", C_D3, rem_r)
        self.play(Write(rem3))
        self.wait(0.5)

        # ── Final: pulse the quotient to celebrate ────────────────────────────
        quotient = VGroup(q1, q2, q3)
        self.play(quotient.animate.scale(1.2).set_color(ACCENT), run_time=0.5)
        self.wait(0.3)
        self.play(quotient.animate.scale(1 / 1.2).set_color(RED_PEN), run_time=0.4)
        self.wait(1.5)

    # ── Helper ────────────────────────────────────────────────────────────────

    def _bring_down(self, g, src_mob, target_col, target_row):
        """Flash a dividend digit, then animate a copy dropping to join the remainder."""
        self.play(Indicate(src_mob, color=ACCENT, scale_factor=1.4), run_time=0.4)
        copy = src_mob.copy()
        self.add(copy)
        self.play(
            copy.animate.move_to(g.pos(target_col, target_row)),
            run_time=0.7,
        )
        self.wait(0.3)
        return copy
