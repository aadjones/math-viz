"""Visual theme for math-viz animations.

Paper-like aesthetic: warm cream background, ink-dark text, teacher's red pen
for answers. Deliberately avoids the 3b1b black-background look.

To change the monospace font:
  - macOS:  "Courier New"    (built-in)
  - Linux:  "Liberation Mono" (apt-get install fonts-liberation)
  - Anywhere: "DejaVu Sans Mono" (apt-get install fonts-dejavu-core)
"""

# ── Palette ───────────────────────────────────────────────────────────────────
PAPER_BG  = "#F5F0E8"   # warm cream — the "page"
INK       = "#1A1A1A"   # near-black — pencil strokes
RED_PEN   = "#8B2020"   # deep red — teacher's pen (quotient digits)
ACCENT    = "#2A5A8B"   # muted blue — highlights / indicators
GRID_LINE = "#C8BCA8"   # faint warm tan — graph-paper grid

# ── Typography ────────────────────────────────────────────────────────────────
MONO_FONT = "Courier New"
FONT_SIZE = 32
