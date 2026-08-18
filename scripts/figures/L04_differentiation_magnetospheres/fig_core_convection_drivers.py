"""Generate Fig. (`fig:core-convection-drivers`).

Two-panel quarter-section cutout of Earth showing the two buoyancy
sources that drive convection in the liquid outer core:

(a) Thermal convection: the mantle extracts heat across the
    core-mantle boundary, so the core cools from above. The cooled
    fluid at the top of the outer core is dense and sinks; hot fluid
    rises from depth.
(b) Compositional convection: iron crystallises onto the growing
    inner core and the light elements (S, Si, O) are rejected into
    the liquid at the inner-core boundary. The buoyant,
    light-element-rich fluid rises, displaced fluid sinks back, and
    the latent heat released at the ICB adds thermal buoyancy.

Geometry: quarter wedge (0 to 90 degrees), radii to scale
(R = 6371 km, CMB at r = 3480 km, ICB at r = 1220 km); the flow
arrows are illustrative.

Caption / figure id : `fig:core-convection-drivers`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Roberts2013
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, FancyArrowPatch, Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/core_convection_drivers.avif")

R_SURF = 1.0
R_CMB = 3480.0 / 6371.0
R_ICB = 1220.0 / 6371.0

C_MANTLE = "#f5deb3"
C_OUTER = "#cfe3f2"
C_INNER = "0.62"
C_HOT = "#d62728"
C_COLD = "#1f77b4"
C_LIGHT = "#2ca02c"


def _pol(r: float, ang_deg: float) -> tuple[float, float]:
    a = np.deg2rad(ang_deg)
    return r * np.cos(a), r * np.sin(a)


def draw_shell(ax: plt.Axes) -> None:
    """Quarter-section cutout, layers outside in, radii to scale."""
    for r_out, r_in, fill in ((R_SURF, R_CMB, C_MANTLE),
                              (R_CMB, R_ICB, C_OUTER),
                              (R_ICB, 0.0, C_INNER)):
        ax.add_patch(Wedge((0, 0), r_out, 0, 90, width=r_out - r_in,
                           facecolor=fill, edgecolor="0.35", lw=0.9,
                           zorder=1))


def radial_arrow(ax, ang, r0, r1, color, lw=1.8, wiggle=0.0, zorder=5):
    """Arrow from radius r0 to r1 at position angle ang (degrees)."""
    x0, y0 = _pol(r0, ang)
    x1, y1 = _pol(r1, ang)
    style = f"arc3,rad={wiggle}" if wiggle else "arc3"
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
                                 arrowstyle="-|>", mutation_scale=13,
                                 connectionstyle=style, color=color,
                                 lw=lw, zorder=zorder))


def leader(ax, text, xy_text, xy_tip, color, ha, va="center", fs=9):
    """Label outside the wedge with a thin leader arrow to its target."""
    ax.annotate(text, xy=xy_tip, xytext=xy_text, fontsize=fs, ha=ha,
                va=va, color=color, zorder=6,
                arrowprops=dict(arrowstyle="->", color=color, lw=1.0,
                                shrinkA=4, shrinkB=2))


def layer_labels(ax) -> None:
    """Layer names below the horizontal cut face, staggered to fit."""
    for text, xy_tip, xy_text in (("inner core", (0.10, 0.06), (0.04, -0.26)),
                                  ("outer core", (0.37, 0.06), (0.40, -0.10)),
                                  ("mantle", (0.78, 0.06), (0.80, -0.10))):
        ax.annotate(text, xy=xy_tip, xytext=xy_text, fontsize=9,
                    ha="center", va="top", color="0.25", zorder=6,
                    arrowprops=dict(arrowstyle="-|>", color="0.4",
                                    lw=1.0))


def draw_thermal(ax: plt.Axes) -> None:
    draw_shell(ax)
    layer_labels(ax)
    # the mantle extracts heat across the CMB
    for ang in (25, 50, 75):
        radial_arrow(ax, ang, R_CMB - 0.03, R_CMB + 0.20, C_HOT, lw=2.0)
    # circulation: hot fluid rises, cooled fluid sinks
    radial_arrow(ax, 33, R_ICB + 0.05, R_CMB - 0.05, C_HOT, wiggle=0.2)
    radial_arrow(ax, 62, R_CMB - 0.05, R_ICB + 0.05, C_COLD, wiggle=0.2)

    leader(ax, "heat extracted by the mantle:\nthe core cools from above",
           (0.72, 1.00), _pol(R_CMB + 0.10, 50), C_HOT, ha="left")
    leader(ax, "hot fluid\nrises", (1.12, 0.30), _pol(0.44, 33), C_HOT,
           ha="left")
    leader(ax, "cooled fluid\nsinks", (-0.12, 0.48), _pol(0.40, 62),
           C_COLD, ha="right")
    ax.set_title("(a) thermal convection: the core cools", fontsize=11)


def draw_compositional(ax: plt.Axes) -> None:
    draw_shell(ax)
    # the growing inner core
    r_grow = R_ICB + 0.045
    ax.add_patch(Arc((0, 0), 2 * r_grow, 2 * r_grow, theta1=0,
                     theta2=90, ls="--", color="0.25", lw=1.1, zorder=4))
    # iron crystallises onto the inner core
    for ang in (15, 40):
        radial_arrow(ax, ang, R_ICB + 0.115, R_ICB + 0.015, "0.25",
                     lw=1.5)
    # buoyant light-element-rich fluid rises; displaced fluid returns
    for ang in (58, 80):
        radial_arrow(ax, ang, R_ICB + 0.04, R_CMB - 0.05, C_LIGHT,
                     wiggle=0.25)
    radial_arrow(ax, 30, R_CMB - 0.05, R_ICB + 0.10, C_COLD, wiggle=0.2,
                 lw=1.5)

    leader(ax, "iron crystallises onto the\ngrowing inner core (dashed);\nlatent heat released",
           (0.55, -0.14), _pol(R_ICB + 0.07, 15), "0.15", ha="center",
           va="top", fs=8.5)
    leader(ax, "light elements (S, Si, O)\nexpelled: buoyant\nfluid rises",
           (-0.12, 0.72), _pol(0.42, 80), C_LIGHT, ha="right", fs=8.5)
    leader(ax, "displaced fluid\nsinks back", (1.12, 0.35),
           _pol(0.42, 30), C_COLD, ha="left", fs=8.5)
    ax.set_title("(b) compositional convection: the inner core grows",
                 fontsize=11)


def make_plot() -> Path:
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.8, 5.6))
    for ax in (ax_a, ax_b):
        ax.set_xlim(-0.80, 1.72)
        ax.set_ylim(-0.42, 1.30)
        ax.set_aspect("equal")
        ax.axis("off")
    draw_thermal(ax_a)
    draw_compositional(ax_b)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
