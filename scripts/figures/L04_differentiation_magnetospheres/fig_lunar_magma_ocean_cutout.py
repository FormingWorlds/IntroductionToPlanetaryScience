"""Generate Fig. (`fig:lunar-magma-ocean`).

Section cutout (quarter wedge) of the Moon at the end of magma-ocean
solidification. Five layers, outside in: the anorthositic flotation
crust, the thin urKREEP layer (the last residual liquid), the dense
ilmenite-rich cumulates, the pyroxenite and dunite cumulate mantle,
and the iron core. Each layer carries a colour-matched label with an
arrow. Thin outer layers are exaggerated in thickness so they stay
visible; the stratigraphy follows Elkins-Tanton (2012, Annu. Rev.
Earth Planet. Sci. 40, 113).

Caption / figure id : `fig:lunar-magma-ocean`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : ElkinsTanton2012, Wood1970, Warren1985
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/"
            "lunar_magma_ocean_cutout.avif")

# Layers, inside out: (outer radius fraction, fill colour, label colour).
# Thin outer layers are exaggerated so they render visibly.
LAYERS = [
    ("core", 0.22, "#9a9aa5", "#4d4d58"),
    ("cumulates", 0.900, "#9dc49a", "#3f6b44"),
    ("ilmenite", 0.945, "#3e5c41", "#3e5c41"),
    ("urkreep", 0.972, "#f0c419", "#a97f00"),
    ("crust", 1.000, "#efe9d8", "#857c5e"),
]


def pol(r, deg):
    a = np.deg2rad(deg)
    return r * np.cos(a), r * np.sin(a)


def arc_label(ax, text, color, deg, r_target, r_text=1.16):
    """Colour-matched label outside the arc with an arrow into the layer."""
    xt, yt = pol(r_text, deg)
    ax.annotate(text, xy=(xt, yt), ha="left", va="center",
                fontsize=10, color=color)
    x0, y0 = pol(r_text - 0.015, deg)
    x1, y1 = pol(r_target, deg)
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.3))


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(6.8, 6.6))

    r_in = 0.0
    for _name, r_out, fill, _lab in LAYERS:
        ax.add_patch(Wedge((0, 0), r_out, 0, 90, width=r_out - r_in,
                           facecolor=fill, edgecolor="0.35", lw=0.8))
        r_in = r_out

    # Thin outer layers: labels along the arc
    arc_label(ax, "anorthositic crust\n(floated plagioclase)",
              LAYERS[4][3], 72, 0.986)
    arc_label(ax, "urKREEP\n(last residual liquid)",
              LAYERS[3][3], 52, 0.9585)
    arc_label(ax, "ilmenite-rich cumulates\n(dense, prone to sinking)",
              LAYERS[2][3], 32, 0.912)

    # Wide inner layers: labels below the horizontal cut face
    ax.annotate("pyroxenite and dunite\ncumulates", xy=(0.62, -0.12),
                ha="center", va="top", fontsize=10, color=LAYERS[1][3])
    ax.annotate("", xy=(0.62, 0.10), xytext=(0.62, -0.10),
                arrowprops=dict(arrowstyle="-|>", color=LAYERS[1][3], lw=1.3))
    ax.annotate("iron core", xy=(0.10, -0.12), ha="center", va="top",
                fontsize=10, color=LAYERS[0][3])
    ax.annotate("", xy=(0.10, 0.08), xytext=(0.10, -0.10),
                arrowprops=dict(arrowstyle="-|>", color=LAYERS[0][3], lw=1.3))

    ax.set_xlim(-0.04, 1.50)
    ax.set_ylim(-0.30, 1.20)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout(pad=0.2)
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
