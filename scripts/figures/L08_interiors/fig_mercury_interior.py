"""Generate Fig. (`fig:mercury-interior`).

Concentric-circle schematic of Mercury's interior from the MESSENGER-era
synthesis. A thin crust and silicate mantle overlie a large iron core; the
core radius is ~83% of the planetary radius and holds ~74% of the mass, the
values used in the notes and Worksheet 4. The core is drawn layered: a
possible thin solid Fe-S layer at its top, a liquid Fe-Ni-S outer core, and
an inferred solid inner core.

The layer radii follow the fractional radii the numbers imply, so the drawing
is close to scale (unlike the not-to-scale layer proportions of many textbook
cutaways): the thin mantle over an enormous core is the point of the figure.

Caption / figure id : `fig:mercury-interior`
Markdown source     : book/08_interiors/interiors.md
Citation keys       : Margot2007, MargotHauck2018
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/mercury_interior.avif"

# Fractional radii (planetary radius = 1.0). Core top at 0.83 R follows the
# notes; the ~400 km mantle fills 0.83-0.98 and the ~30-50 km crust the outer
# ~2%, so the thin shell over an enormous core reads directly from the drawing.
R_SURFACE = 1.00
R_CRUST_BASE = 0.980       # crust base; crust is the outer ~2% (~49 km)
R_FES_TOP = 0.830          # top of the core = 83% R; mantle fills 0.83-0.98
R_FES_BASE = 0.800         # base of the thin solid Fe-S layer (~30-90 km)
R_INNER = 0.35             # inferred solid inner core

C_CRUST = "#8a6a44"
C_MANTLE = "#d8b98c"
C_FES = "#8a7d3f"
C_LIQUID = "#cd5c5c"
C_INNER = "#6e241c"
LEADER = "0.45"


def ring(ax, r_outer: float, color: str, edge: str = "black",
         lw: float = 1.0, ls: str = "-") -> None:
    """Draw a filled disc of radius `r_outer`; inner layers overlay it."""
    ax.add_patch(Circle((0, 0), r_outer, facecolor=color, edgecolor=edge,
                        lw=lw, linestyle=ls, zorder=1))


def leader(ax, r_mid: float, phi_deg: float, xtext: float, ytext: float,
           text: str) -> None:
    """Label a layer: a thin line from the ring at `phi_deg` to right-side text."""
    phi = np.radians(phi_deg)
    x0, y0 = r_mid * np.cos(phi), r_mid * np.sin(phi)
    ax.annotate(
        text, xy=(x0, y0), xytext=(xtext, ytext),
        ha="left", va="center", fontsize=10, color="0.15",
        arrowprops=dict(arrowstyle="-", color=LEADER, lw=0.8,
                        connectionstyle="arc3,rad=0.0"), zorder=5)


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.0, 6.0))

    # Discs from outside in; each overlays the previous.
    ring(ax, R_SURFACE, C_CRUST)               # crust (outer skin)
    ring(ax, R_CRUST_BASE, C_MANTLE)           # silicate mantle
    ring(ax, R_FES_TOP, C_FES)                 # thin solid Fe-S layer
    ring(ax, R_FES_BASE, C_LIQUID)             # liquid Fe-Ni-S outer core
    ring(ax, R_INNER, C_INNER, ls="--", lw=1.0)  # inferred solid inner core

    xt = 1.28
    leader(ax, 0.5 * (R_CRUST_BASE + R_SURFACE), 62, xt, 0.95,
           "Crust\n~30-50 km thick")
    leader(ax, 0.5 * (R_FES_TOP + R_CRUST_BASE), 40, xt, 0.50,
           "Silicate mantle\n~400 km thick")
    leader(ax, 0.5 * (R_FES_BASE + R_FES_TOP), 18, xt, 0.10,
           "Solid Fe-S layer (?)\n~30-90 km")
    leader(ax, 0.5 * (R_INNER + R_FES_BASE), -24, xt, -0.40,
           "Liquid Fe-Ni-S\nouter core")
    leader(ax, 0.5 * R_INNER, -60, xt, -0.90,
           "Solid inner core (?)\ninferred")

    # Whole-core statistics, scoped to the entire iron core (all three
    # sub-layers), kept off the liquid-layer leader so the two are not conflated.
    ax.text(-1.12, 1.05, "Iron core (all layers):\n~83% R, ~74% mass",
            ha="left", va="top", fontsize=10, color="0.15")

    ax.set_title("Mercury's interior structure (post-MESSENGER model)",
                 fontsize=13, pad=14)
    ax.set_xlim(-1.15, 2.35)
    ax.set_ylim(-1.20, 1.20)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80, dpi=300)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
