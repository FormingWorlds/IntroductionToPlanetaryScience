"""Generate Fig. (`fig:stahler-quakes`).

Panels A and C of Fig. 1 of Stähler et al. (2021) with the axes the crop
lacks. Panel (a) gains the time axis it shares with the spectrograms of the
source figure and labels for the S and ScS arrivals; panel (b) shows the
stacked ScS energy normalised from the minimum to the peak of the fitted
curve, with the absolute core radius on a top axis.

Source pixel positions (crop at 1900 x 680 px):
- time axis: 150 px per 100 s, ScS (t = 0) at x = 875 px, so the frame
  spans -450 to 200 s, as in Fig. 1B of the source.
- S arrival of S0173a: x = 360 px, i.e. -343 s, consistent with ScS
  arriving about 350 s after S in the source text.
- core radius axis: 99.5 px per 50 km, offset 0 (1830 km) at x = 1579 px.
- fitted energy curve: minimum at y = 548 px, peak at y = 225 px.

Caption / figure id : `fig:stahler-quakes`
Markdown source     : book/10_mercury_mars/mercury_mars.md
Citation keys       : Stahler2021
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from scripts.figures._shared.style import save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
SRC = REPO_ROOT / "scripts/figures/L10_mercury_mars/data/stahler2021_fig1_panels_ac.avif"
OUT_AVIF = REPO_ROOT / "book/10_mercury_mars/figures/stahler2021_marsquakes.avif"

PAD_TOP, PAD_BOTTOM = 110, 40
FONT = ["Helvetica", "Arial", "DejaVu Sans"]
TICK_PT, LABEL_PT = 22, 23
INK = "#1a1a1a"

# Source-crop geometry in pixels (see module docstring)
LEFT_X0, LEFT_X1, LEFT_Y1 = 200, 1174, 479
T_ZERO_X, PX_PER_S = 875.0, 1.5
S_X = 360
RIGHT_X0, RIGHT_X1, RIGHT_Y0, RIGHT_Y1 = 1310, 1808, 11, 585
R_ZERO_X, PX_PER_KM, R_CORE = 1579.0, 99.5 / 50.0, 1830
E_MIN_Y, E_MAX_Y = 548.0, 225.0
OLD_GRID_ROWS = (36, 136, 236, 336, 435, 535)


def load_source() -> np.ndarray:
    """Return the source crop as an RGB array with the stale labels removed.

    Returns
    -------
    numpy.ndarray
        The crop, padded top and bottom, with the old energy axis label,
        its tick marks and horizontal grid, the stack label and the
        clipped core-radius label painted out.
    """
    a = np.asarray(Image.open(SRC).convert("RGB")).copy()
    # Old horizontal grid of the energy panel: interpolate neutral grey pixels
    for y in OLD_GRID_ROWS:
        for yy in (y - 1, y, y + 1):
            row = a[yy, RIGHT_X0 + 2:RIGHT_X1 - 1].astype(int)
            grey = (np.ptp(row, axis=1) < 4) & (row[:, 0] > 150) & (row[:, 0] < 250)
            fill = (a[y - 4, RIGHT_X0 + 2:RIGHT_X1 - 1].astype(int)
                    + a[y + 4, RIGHT_X0 + 2:RIGHT_X1 - 1].astype(int)) // 2
            row[grey] = fill[grey]
            a[yy, RIGHT_X0 + 2:RIGHT_X1 - 1] = row
    a[0:RIGHT_Y1 + 4, 1200:RIGHT_X0 - 1] = 255  # old energy label and ticks
    a[288:436, 95:178] = 255  # "Stack of all events"
    a[598:, RIGHT_X0 - 40:] = 255  # bottom tick labels and clipped label
    h, w, _ = a.shape
    out = np.full((h + PAD_TOP + PAD_BOTTOM, w, 3), 255, dtype=np.uint8)
    out[PAD_TOP:PAD_TOP + h] = a
    return out


def make_plot() -> Path:
    """Draw the new axes and labels over the source crop and save the figure.

    Returns
    -------
    pathlib.Path
        Path of the written AVIF.
    """
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": FONT})
    img = load_source()
    h, w, _ = img.shape
    fig = plt.figure(figsize=(w / 100, h / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(img, interpolation="none")
    ax.set_xlim(0, w)
    ax.set_ylim(h, 0)
    ax.axis("off")
    p = PAD_TOP
    line = dict(color=INK, lw=2.2, solid_capstyle="butt")
    txt = dict(color=INK, fontsize=TICK_PT)

    # (a) time axis below the stack panel
    yb = LEFT_Y1 + p
    ax.plot([LEFT_X0, LEFT_X1], [yb, yb], **line)
    for t in range(-400, 201, 100):
        x = T_ZERO_X + PX_PER_S * t
        ax.plot([x, x], [yb, yb + 9], **line)
        lab = f"{t}".replace("-", "−")
        ax.text(x, yb + 14, lab, ha="center", va="top", **txt)
    ax.text((LEFT_X0 + LEFT_X1) / 2, yb + 58, "Time relative to ScS arrival [s]",
            ha="center", va="top", color=INK, fontsize=LABEL_PT)
    ax.text(137, (253 + LEFT_Y1) / 2 + p, "Stacked envelope\n(arb. units)",
            rotation=90, ha="center", va="center", color=INK,
            fontsize=LABEL_PT, linespacing=1.15)

    # Arrival labels above panel (a)
    for x, name in ((S_X, "S"), (T_ZERO_X, "ScS")):
        ax.plot([x, x], [p - 2, p - 18], **line)
        ax.text(x, p - 24, name, ha="center", va="bottom", color=INK,
                fontsize=LABEL_PT, fontweight="bold")

    # (b) normalised energy axis
    for e in (0.0, 0.5, 1.0):
        y = E_MIN_Y - e * (E_MIN_Y - E_MAX_Y) + p
        ax.plot([RIGHT_X0 - 9, RIGHT_X0], [y, y], **line)
        ax.text(RIGHT_X0 - 14, y, f"{e:.1f}", ha="right", va="center", **txt)
    ax.text(1214, (RIGHT_Y0 + RIGHT_Y1) / 2 + p, "Normalised ScS energy",
            rotation=90, ha="center", va="center", color=INK, fontsize=LABEL_PT)

    # (b) bottom axis: offset from 1830 km; top axis: absolute core radius
    yb = RIGHT_Y1 + p
    yt = RIGHT_Y0 + p
    for d in range(-100, 101, 50):
        x = R_ZERO_X + PX_PER_KM * d
        ax.text(x, yb + 14, f"{d}".replace("-", "−"), ha="center", va="top", **txt)
        ax.plot([x, x], [yt, yt - 9], **line)
        ax.text(x, yt - 14, f"{R_CORE + d}", ha="center", va="bottom", **txt)
    ax.text((RIGHT_X0 + RIGHT_X1) / 2, yb + 54, f"Offset from {R_CORE} km [km]",
            ha="center", va="top", color=INK, fontsize=LABEL_PT)
    ax.text((RIGHT_X0 + RIGHT_X1) / 2, yt - 52, "Core radius [km]",
            ha="center", va="bottom", color=INK, fontsize=LABEL_PT)

    # Panel letters
    for x, letter in ((20, "(a)"), (1180, "(b)")):
        ax.text(x, 8, letter, ha="left", va="top", color=INK,
                fontsize=LABEL_PT + 2, fontweight="bold")

    out = save_figure(fig, OUT_AVIF, avif_quality=80, dpi=100)
    plt.close(fig)
    return out


if __name__ == "__main__":
    print(make_plot())
