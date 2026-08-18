"""Generate Fig. (`fig:core-convection-drivers`).

Two-panel schematic of the two buoyancy sources that drive convection
in Earth's liquid outer core:

(a) Thermal convection: the core is hotter than the mantle, so heat
    flows out across the core-mantle boundary. The cooling from above
    makes fluid near the CMB dense; it sinks, while hot buoyant fluid
    rises from depth.
(b) Compositional convection: the inner core grows as iron
    crystallises at the inner-core boundary. Crystallisation rejects
    the light elements (S, Si, O) into the liquid, and the resulting
    buoyant, light-element-rich fluid rises; the latent heat released
    at the ICB adds thermal buoyancy.

Geometry: radii to scale (R = 6371 km, CMB at r = 3480 km, ICB at
r = 1220 km); the flow arrows are illustrative.

Caption / figure id : `fig:core-convection-drivers`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Roberts2013
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

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
    ax.add_patch(Circle((0, 0), R_SURF, facecolor=C_MANTLE,
                        edgecolor="0.3", lw=1.2, zorder=1))
    ax.add_patch(Circle((0, 0), R_CMB, facecolor=C_OUTER,
                        edgecolor="0.35", lw=1.0, zorder=2))
    ax.add_patch(Circle((0, 0), R_ICB, facecolor=C_INNER,
                        edgecolor="0.3", lw=1.0, zorder=3))


def radial_arrow(ax, ang, r0, r1, color, lw=1.8, wiggle=0.0, zorder=5):
    """Arrow from radius r0 to r1 at position angle ang (degrees)."""
    x0, y0 = _pol(r0, ang)
    x1, y1 = _pol(r1, ang)
    style = f"arc3,rad={wiggle}" if wiggle else "arc3"
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
                                 arrowstyle="-|>", mutation_scale=13,
                                 connectionstyle=style, color=color,
                                 lw=lw, zorder=zorder))


def draw_thermal(ax: plt.Axes) -> None:
    draw_shell(ax)
    # heat crossing the CMB into the mantle
    for ang in (90, 30, -30, -90, 150, 210):
        radial_arrow(ax, ang, R_CMB + 0.01, R_CMB + 0.22, C_HOT, lw=2.0)
    # convection: hot fluid rises (right), cooled fluid sinks (left)
    for ang in (45, -45):
        radial_arrow(ax, ang, R_ICB + 0.06, R_CMB - 0.06, C_HOT,
                     wiggle=0.25)
    for ang in (135, 225):
        radial_arrow(ax, ang, R_CMB - 0.06, R_ICB + 0.06, C_COLD,
                     wiggle=0.25)

    ax.annotate("heat flow\ninto the mantle", xy=(0.0, 0.79),
                xytext=(0.0, 1.12), fontsize=9, ha="center",
                color=C_HOT, zorder=6,
                arrowprops=dict(arrowstyle="->", color=C_HOT, lw=1.0,
                                shrinkB=2))
    ax.annotate("hot fluid\nrises", xy=_pol(0.42, 45),
                xytext=(1.06, 0.06), fontsize=8.5, ha="left",
                color=C_HOT, zorder=6,
                arrowprops=dict(arrowstyle="->", color=C_HOT, lw=1.0,
                                shrinkB=2))
    ax.annotate("cooled fluid\nsinks", xy=_pol(0.42, 135),
                xytext=(-1.06, 0.06), fontsize=8.5, ha="right",
                color=C_COLD, zorder=6,
                arrowprops=dict(arrowstyle="->", color=C_COLD, lw=1.0,
                                shrinkB=2))
    ax.annotate("mantle", xy=(0.0, -0.88), fontsize=9, ha="center",
                color="#7a5c1e", zorder=6)
    ax.set_title("(a) thermal convection: the core cools", fontsize=11)


def draw_compositional(ax: plt.Axes) -> None:
    draw_shell(ax)
    # the growing inner core
    ax.add_patch(Circle((0, 0), R_ICB + 0.05, facecolor="none",
                        edgecolor="0.25", lw=1.1, ls="--", zorder=4))
    # iron crystallises onto the inner core
    for ang in (200, 250):
        radial_arrow(ax, ang, R_ICB + 0.13, R_ICB + 0.015, "0.25",
                     lw=1.5)
    # light-element-rich buoyant fluid rises from the ICB
    for ang in (0, 45, 90, 135):
        radial_arrow(ax, ang, R_ICB + 0.03, R_CMB - 0.05, C_LIGHT,
                     wiggle=0.3)

    ax.annotate("inner core grows:\niron crystallises,\nlatent heat released",
                xy=_pol(R_ICB + 0.10, 225), xytext=(-1.52, -0.98),
                fontsize=8.5, ha="left", color="0.15", zorder=6,
                arrowprops=dict(arrowstyle="->", color="0.25", lw=1.0,
                                shrinkB=2))
    ax.annotate("light elements\n(S, Si, O) expelled:\nbuoyant fluid rises",
                xy=_pol(0.40, 45), xytext=(0.80, 0.86), fontsize=8.5,
                ha="left", color=C_LIGHT, zorder=6,
                arrowprops=dict(arrowstyle="->", color=C_LIGHT, lw=1.0,
                                shrinkB=2))
    ax.annotate("outer core", xy=(0.0, -0.42), fontsize=9, ha="center",
                color="#1a4a6e", zorder=6)
    ax.set_title("(b) compositional convection: the inner core grows",
                 fontsize=11)


def make_plot() -> Path:
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10.6, 5.4))
    for ax in (ax_a, ax_b):
        ax.set_xlim(-1.55, 1.55)
        ax.set_ylim(-1.25, 1.25)
        ax.set_aspect("equal")
        ax.axis("off")
    draw_thermal(ax_a)
    draw_compositional(ax_b)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
