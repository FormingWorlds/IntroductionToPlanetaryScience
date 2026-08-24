"""Generate Fig. (`fig:convection-regimes`).

Two-panel schematic of mantle convection end-members:
(a) whole-mantle convection: a single circulation pattern from CMB
    to surface, with the 660 km discontinuity only weakly impeding
    flow.
(b) layered convection: separate cells in upper and lower mantle,
    decoupled by the 660 km phase transition.

The drawn radius of the 660 km boundary is exaggerated. To scale the
upper mantle is 23% of the mantle thickness, which leaves too little
room for a legible arrow, so the boundary is placed at 45% instead.
The captions state that the figure is schematic and not to scale.

Caption / figure id : `fig:convection-regimes`
Markdown source     : book/08_interiors/interiors.md
Citation key        : Schubert2001
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/convection_regimes.avif"

R_TOTAL = 1.0          # surface radius (normalised; R_E = 6371 km)
R_660 = 0.800          # 660 km discontinuity, radius exaggerated (true: 0.896)
R_CMB = 0.546          # core-mantle boundary at 2891 km depth
CORE_COLOR = "#c0524a"
MANTLE_COLOR = "#f6f4f2"
COLD_DOWN = "#1f77b4"
HOT_UP = "#e07a3a"


def radial_arrow(ax, phi_deg: float, r0: float, r1: float, color: str,
                 lw: float, head: float) -> None:
    """Draw one curved arrow along the radius `phi_deg`, from `r0` to `r1`."""
    phi = np.radians(phi_deg)
    start = (r0 * np.cos(phi), r0 * np.sin(phi))
    end = (r1 * np.cos(phi), r1 * np.sin(phi))
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle="->", mutation_scale=head, color=color,
        lw=lw, connectionstyle="arc3,rad=0.18"))


def draw_panel(ax, mode: str) -> None:
    # The 660 km ring is dashed where flow crosses it and solid where it
    # blocks flow, so the line style carries the physics of each regime.
    if mode == "whole":
        ring = dict(edgecolor="0.55", lw=0.9, linestyle="--")
    else:
        ring = dict(edgecolor="0.35", lw=1.8, linestyle="-")
    # Surface, 660, CMB rings
    ax.add_patch(Circle((0, 0), R_TOTAL, facecolor=MANTLE_COLOR,
                        edgecolor="black", lw=1.0))
    ax.add_patch(Circle((0, 0), R_660, facecolor=MANTLE_COLOR, **ring))
    ax.add_patch(Circle((0, 0), R_CMB, facecolor=CORE_COLOR,
                        edgecolor="black", lw=1.0))
    ax.text(0, 0, "Core", ha="center", va="center", fontsize=11,
            color="white", weight="bold")

    # 660 km label, offset inward so it clears the dashed ring itself
    r_label = R_660 - 0.075
    ax.text(r_label * np.cos(np.radians(110)),
            r_label * np.sin(np.radians(110)),
            "660 km", color="0.4", fontsize=8, ha="center", va="center")

    # Surface label above
    ax.text(0, R_TOTAL + 0.08, "Surface", ha="center", fontsize=9, color="0.3")

    # Plumes
    if mode == "whole":
        ax.set_title("(a) Whole-mantle convection", fontsize=11)
        # 6 alternating plumes from CMB to surface, passing through 660
        for i, phi_deg in enumerate(range(20, 360, 60)):
            up = i % 2 == 0
            r0, r1 = R_CMB + 0.02, R_TOTAL - 0.02
            radial_arrow(ax, phi_deg, r0 if up else r1, r1 if up else r0,
                         HOT_UP if up else COLD_DOWN, 2.0, 14)
        ax.text(0, -1.18, "Single circulation\nfrom CMB to surface",
                ha="center", va="top", fontsize=9, color="0.3")
    else:
        ax.set_title("(b) Layered convection", fontsize=11)
        # Lower-mantle cells, from the CMB up to the 660 km boundary
        for i, phi_deg in enumerate(range(20, 360, 60)):
            up = i % 2 == 0
            r0, r1 = R_CMB + 0.02, R_660 - 0.02
            radial_arrow(ax, phi_deg, r0 if up else r1, r1 if up else r0,
                         HOT_UP if up else COLD_DOWN, 1.8, 12)
        # Upper-mantle cells, offset by 30 degrees from the lower ones so
        # the two layers read as decoupled rather than aligned.
        for i, phi_deg in enumerate(range(50, 360, 60)):
            up = i % 2 == 1
            r0, r1 = R_660 + 0.02, R_TOTAL - 0.02
            radial_arrow(ax, phi_deg, r0 if up else r1, r1 if up else r0,
                         HOT_UP if up else COLD_DOWN, 1.6, 10)
        ax.text(0, -1.18, "Upper- and lower-mantle\ncells separated by 660 km",
                ha="center", va="top", fontsize=9, color="0.3")

    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.40, 1.18)
    ax.set_aspect("equal")
    ax.axis("off")


def make_plot() -> Path:
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 6.0))
    draw_panel(axes[0], "whole")
    draw_panel(axes[1], "layered")
    fig.suptitle("Mantle convection regimes", fontsize=12, y=0.98)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80, dpi=300)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
