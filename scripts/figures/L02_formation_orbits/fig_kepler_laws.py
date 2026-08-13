"""Generate Fig. (`fig:kepler-laws`).

English redrawing of Hankwang's Kepler-laws diagram (Wikimedia Commons,
CC BY 2.5): two elliptical orbits sharing the Sun at one focus, the
equal-area sectors of the second law on the inner orbit, and the foci,
semi-major-axis and planet labels of the original. On top of the source
design: the Sun drawn as a warm disc, an equal-areas annotation between
the two sectors, planet labels moved clear of the curves on thin
leaders, and labels enlarged for the notes display size.

The geometry is taken verbatim from the source SVG, which encodes it in
exact coordinates: inner orbit a=500, b=400 with focus separation 300
(so F1 sits at the origin and F2 at (600, 0)); outer orbit a=700, b=500,
focus separation 490, rotated 42 degrees about the shared focus; both
planets and all sector boundary points lie on their ellipses to within
the source's own rounding. Coordinates here are in the source's units
with its y axis flipped to matplotlib's.

Outputs the site SVG and the deck PDF, so the deck does not depend on an
external SVG converter.

Caption / figure id : `fig:kepler-laws`
Markdown source     : book/02_formation_orbits/formation_orbits.md
Citation key        : (credit line in caption: Hankwang, CC BY 2.5)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from scripts.figures._shared.style import apply_style


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_SVG = REPO_ROOT / "book/02_formation_orbits/figures/kepler_laws.svg"
DECK_SVG = REPO_ROOT / "slides/lecture02/figures/kepler_laws.svg"
DECK_PDF = REPO_ROOT / "slides/lecture02/figures/kepler_laws.pdf"

PURPLE = "#880088"
TEAL = "#008888"
GREY = "#444444"
SUN = "#e8a33d"
SUN_EDGE = "#8a5a10"
NOTE = "#555555"
SECTOR = "#dddddd"

# Source viewBox: x -258..987, y -405..930 (y down). Everything below works
# in source units with y negated for matplotlib.
XLIM = (-258, 987)
YLIM = (-930, 405)
ROT = np.deg2rad(-42)  # SVG rotate(42) in a y-down frame = -42 deg in y-up


def rot(p: np.ndarray) -> np.ndarray:
    """Rotate y-up points by the outer orbit's angle about the origin."""
    c, s = np.cos(ROT), np.sin(ROT)
    return p @ np.array([[c, s], [-s, c]])


def ellipse(a: float, b: float, cx: float, n: int = 400) -> np.ndarray:
    t = np.linspace(0, 2 * np.pi, n)
    return np.column_stack([cx + a * np.cos(t), b * np.sin(t)])


def sector(a: float, b: float, cx: float, p0, p1) -> np.ndarray:
    """Focus-anchored sector of the inner ellipse from p0 to p1 (y-up)."""
    t0 = np.arctan2(p0[1] / b, (p0[0] - cx) / a)
    t1 = np.arctan2(p1[1] / b, (p1[0] - cx) / a)
    if t1 < t0:
        t1 += 2 * np.pi
    t = np.linspace(t0, t1, 120)
    arc = np.column_stack([cx + a * np.cos(t), b * np.sin(t)])
    return np.vstack([[0, 0], arc, [0, 0]])


def arrow(ax, pts: np.ndarray, color: str) -> None:
    """Motion arrow: the source's cubic bezier shaft with a stroked head."""
    p0, p1, p2, p3 = pts[:4]
    t = np.linspace(0, 1, 60)[:, None]
    shaft = ((1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1
             + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3)
    ax.plot(shaft[:, 0], shaft[:, 1], color=color, lw=2.0)
    for tip in (pts[4], pts[5]):
        ax.plot([p3[0], tip[0]], [p3[1], tip[1]], color=color, lw=2.0)


def make_plot() -> None:
    apply_style()
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "dejavuserif",
        "svg.fonttype": "path",
        "axes.grid": False,
        # The shared style's tight bbox would re-crop the canvas and shrink
        # the drawing; this figure must fill its canvas like the source.
        "savefig.bbox": "standard",
    })

    width_in = 6.225
    # Canvas ratio exactly the viewBox ratio, axes full-bleed, so the equal
    # aspect never letterboxes and the drawing fills the canvas like the source.
    fig = plt.figure(
        figsize=(width_in, width_in * (YLIM[1] - YLIM[0]) / (XLIM[1] - XLIM[0])))
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    fs = 92 * width_in * 72 / (XLIM[1] - XLIM[0])   # source units -> points
    fsub = fs * 60 / 80

    # ---- inner orbit (purple), y-up: source y negated ----
    # equal-area sectors, drawn first so the strokes sit on top
    for p0, p1 in (((-170, -136), (0, -320)), ((600, -320), (679, -261))):
        poly = sector(500, 400, 300, p0, p1)
        ax.add_patch(mpatches.Polygon(poly, closed=True, facecolor=SECTOR,
                                      edgecolor=PURPLE, lw=1.6,
                                      linestyle=(0, (3, 3)), zorder=1))
    e1 = ellipse(500, 400, 300)
    ax.plot(e1[:, 0], e1[:, 1], color=PURPLE, lw=2.6, zorder=3)
    ax.plot([-200, 800], [0, 0], color=PURPLE, lw=1.6,
            dashes=[10, 3.5, 1.7, 3.5], zorder=2)
    ax.plot([300, 300], [-69, 69], color=PURPLE, lw=1.6,
            dashes=[10, 3.5, 1.7, 3.5], zorder=2)
    ax.add_patch(plt.Circle((600, 0), 11, color=PURPLE, zorder=4))     # F2
    ax.add_patch(plt.Circle((0, -320), 14, color=PURPLE, zorder=4))    # planet 1
    arrow(ax, np.array([(200, -415), (262, -423), (302, -424), (358, -419),
                        (315, -433), (313, -411)]), PURPLE)

    # ---- outer orbit (teal), rotated about the shared focus ----
    e2 = rot(ellipse(700, 500, 490))
    ax.plot(e2[:, 0], e2[:, 1], color=TEAL, lw=2.6, zorder=3)
    axis2 = rot(np.array([(-210, 0), (1190, 0)]))
    ax.plot(axis2[:, 0], axis2[:, 1], color=TEAL, lw=1.6,
            dashes=[10, 3.5, 1.7, 3.5], zorder=2)
    tick2 = rot(np.array([(490, -69), (490, 69)]))
    ax.plot(tick2[:, 0], tick2[:, 1], color=TEAL, lw=1.6,
            dashes=[10, 3.5, 1.7, 3.5], zorder=2)
    f3 = rot(np.array([(980.0, 0.0)]))[0]
    ax.add_patch(plt.Circle(f3, 11, color=TEAL, zorder=4))             # F3
    p2 = rot(np.array([(490.0, -500.0)]))[0]
    ax.add_patch(plt.Circle(p2, 14, color=TEAL, zorder=4))             # planet 2
    arrow(ax, rot(np.array([(390, -465), (452, -473), (492, -474), (548, -469),
                            (505, -483), (503, -461)])), TEAL)

    # ---- Sun at the common focus ----
    ax.add_patch(plt.Circle((0, 0), 24, facecolor=SUN, edgecolor=SUN_EDGE,
                             lw=2, zorder=5))

    # ---- labels, positions from the source (y negated), baseline-anchored ----
    def label(x, y, parts, color):
        text = "".join(parts)
        ax.text(x, y, text, color=color, fontsize=fs, va="baseline",
                ha="left", zorder=6)

    # Planet labels sit clear of the curves and arrows, tied by leaders;
    # the positions are collision-checked against the rendered ink.
    ax.text(-116, -515, "Planet 1", color=PURPLE, fontsize=fs, ha="left",
            va="bottom", zorder=6)
    ax.plot([-45, -5], [-425, -338], color="0.55", lw=0.8, zorder=5)
    ax.text(-228, -875, "Planet 2", color=TEAL, fontsize=fs, ha="left",
            va="bottom", zorder=6)
    ax.plot([-62, 22], [-778, -712], color="0.55", lw=0.8, zorder=5)
    # The second law, stated where it acts: between the two sectors.
    ax.text(620, -120, r"$\mathrm{A_1 = A_2}$", color=NOTE, fontsize=fs * 0.75,
            ha="center", va="center", zorder=6)

    label(585, 30, [r"$\mathrm{F_2}$"], PURPLE)
    label(500, -45, [r"$\mathrm{a_1}$"], PURPLE)
    label(-99, -200, [r"$\mathrm{A_1}$"], PURPLE)
    label(510, -260, [r"$\mathrm{A_2}$"], PURPLE)
    label(-10, 30, [r"$\mathrm{F_1}$ (Sun)"], GREY)
    label(560, -600, [r"$\mathrm{a_2}$"], TEAL)
    label(710, -630, [r"$\mathrm{F_3}$"], TEAL)

    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    for out in (OUT_SVG, DECK_SVG, DECK_PDF):
        out.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out, transparent=False, facecolor="white")
        print(f"  wrote {out}")


if __name__ == "__main__":
    make_plot()
