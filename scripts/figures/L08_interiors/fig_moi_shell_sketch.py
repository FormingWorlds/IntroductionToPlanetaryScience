"""Generate Fig. (`fig:moi-shell-sketch`).

Sketch of the shell decomposition behind the moment of inertia integral
(eq:moi-integral): a spherically symmetric body of radius R spinning
about a vertical axis, one thin shell of radius r and thickness dr
highlighted, and a mass element dm on that shell at perpendicular
distance r_perp = r sin(theta) from the rotation axis.

Caption / figure id : `fig:moi-shell-sketch`
Markdown source     : book/08_interiors/interiors.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/moi_shell_sketch.avif"

BODY_COLOR = "#f3e2c0"
SHELL_COLOR = "#c98a4b"
AXIS_COLOR = "#444444"
ELEMENT_COLOR = "#8c564b"

R_BODY = 1.0
R_SHELL = 0.66      # shell radius r (inner edge)
DR = 0.08           # shell thickness dr
THETA_DEG = 42.0    # colatitude of the mass element, from the rotation axis


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(5.4, 5.6))
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.42, 1.55)
    ax.set_aspect("equal")
    ax.axis("off")

    # Body, highlighted shell (an annulus drawn as a 360 deg wedge), rim lines
    ax.add_patch(Circle((0, 0), R_BODY, facecolor=BODY_COLOR,
                        edgecolor="black", lw=1.2, zorder=1))
    ax.add_patch(Wedge((0, 0), R_SHELL + DR, 0, 360, width=DR,
                       facecolor=SHELL_COLOR, edgecolor="black",
                       lw=0.6, zorder=2))

    # Rotation axis with spin arrow
    ax.plot([0, 0], [-1.10, 1.35], color=AXIS_COLOR, lw=1.2,
            linestyle=(0, (5, 3)), zorder=3)
    spin = Arc((0, 1.22), 0.5, 0.16, theta1=210, theta2=500,
               color=AXIS_COLOR, lw=1.1, zorder=3)
    ax.add_patch(spin)
    ax.annotate("", xy=(0.25, 1.24), xytext=(0.22, 1.19),
                arrowprops=dict(arrowstyle="->", color=AXIS_COLOR, lw=1.1))
    ax.text(0.32, 1.30, r"$\omega$", fontsize=13, color=AXIS_COLOR)
    ax.text(-0.08, 1.08, "rotation axis", fontsize=9, color=AXIS_COLOR,
            ha="right")

    # Mass element dm on the shell mid-line at colatitude theta
    th = np.deg2rad(THETA_DEG)
    r_mid = R_SHELL + 0.5 * DR
    ex, ey = r_mid * np.sin(th), r_mid * np.cos(th)
    ax.plot(ex, ey, "o", color=ELEMENT_COLOR, ms=9, zorder=5)
    # label placed outside the shell ring, in the clear band below the surface
    ax.annotate(r"$dm$", (ex + 0.09, ey + 0.07), fontsize=12,
                color=ELEMENT_COLOR, zorder=5)

    # Radius vector r, colatitude arc theta, perpendicular distance r_perp
    ax.plot([0, ex], [0, ey], color="black", lw=1.2, zorder=4)
    ax.text(0.27, 0.16, r"$r$", fontsize=13)
    ax.add_patch(Arc((0, 0), 0.52, 0.52, theta1=90 - THETA_DEG, theta2=90,
                     color="black", lw=1.0, zorder=4))
    ax.text(0.07, 0.36, r"$\theta$", fontsize=12)
    ax.plot([0, ex], [ey, ey], color=ELEMENT_COLOR, lw=1.2,
            linestyle=(0, (3, 2)), zorder=4)
    # short label above the mid-point of the dashed line; the caption spells
    # out r_perp = r sin(theta)
    ax.text(0.28, ey - 0.10, r"$r_\perp$", fontsize=12,
            color=ELEMENT_COLOR, ha="center")

    # Shell thickness dr, a short double arrow across the shell at lower right
    phi = np.deg2rad(-35.0)
    x0, x1 = R_SHELL - 0.02, R_SHELL + DR + 0.02
    p0 = (x0 * np.cos(phi), x0 * np.sin(phi))
    p1 = (x1 * np.cos(phi), x1 * np.sin(phi))
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="<->", color="black",
                                 lw=1.0, mutation_scale=8, shrinkA=0,
                                 shrinkB=0, zorder=5))
    ax.text(p1[0] + 0.07, p1[1] - 0.10, r"$dr$", fontsize=12)
    # in the body interior, clear of the shell ring and the radius
    # construction lines
    ax.text(-0.28, -0.35, r"$\rho(r)$", fontsize=12, ha="center")

    # Shell mass, spelt out once below the sketch
    ax.text(0, -1.22, r"shell: $dm_{\rm shell} = 4\pi r^2 \rho(r)\,dr$",
            fontsize=11, ha="center", va="top")

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
