"""Three-stage schematic of impact crater formation.

Panel (a) shows contact and compression, panel (b) excavation of the
transient cavity, and panel (c) the modification stage with a simple
bowl-shaped crater on the left and a complex crater with a central
peak and terraces on the right. Cross-sections are schematic and not
to scale.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon, Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/07_surfaces/figures/impact_stages.avif"

GROUND = "#e8dfcf"
GROUND_EDGE = "#6b5e4a"
SHOCK = "#c0392b"
RAREF = "#1f6db8"
INK = "#2a2a2a"
LABEL = dict(fontsize=10, color=INK)
ARROW = dict(arrowstyle="->", color=INK, lw=0.9)


def _setup(ax: plt.Axes, title: str) -> None:
    """Apply the shared limits, aspect and title of one panel."""
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-2.3, 1.9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=11)


def panel_a(ax: plt.Axes) -> None:
    """Draw contact and compression: projectile, contact zone, shock fronts."""
    _setup(ax, "(a) Contact and compression")
    ax.add_patch(Rectangle((-3.0, -2.3), 6.0, 2.3, facecolor=GROUND,
                           edgecolor="none", zorder=1))
    ax.plot([-3.0, 3.0], [0.0, 0.0], color=GROUND_EDGE, lw=1.2, zorder=2)
    ax.add_patch(Circle((0.0, 0.55), 0.55, facecolor="#8c7b6b",
                        edgecolor=INK, lw=1.0, zorder=3))
    ax.add_patch(Circle((0.0, 0.05), 0.22, facecolor="#f39c12",
                        edgecolor="#b9770e", lw=0.8, zorder=4))
    # Hemispherical shock fronts in the target and in the projectile
    for r in (0.5, 0.9, 1.3):
        ax.add_patch(Arc((0.0, 0.0), 2 * r, 2 * r, theta1=180, theta2=360,
                         color=SHOCK, lw=1.3, ls="--", zorder=5))
    for r in (0.45, 0.8):
        ax.add_patch(Arc((0.0, 0.1), 2 * r, 2 * r, theta1=25, theta2=155,
                         color=SHOCK, lw=1.3, ls="--", zorder=5))
    ax.add_patch(FancyArrowPatch((0.0, 1.75), (0.0, 1.18), arrowstyle="-|>",
                                 mutation_scale=14, color=INK, lw=1.5, zorder=6))
    ax.text(0.2, 1.5, r"$v \approx 10$ to $70$ km s$^{-1}$", ha="left",
            va="center", **LABEL)
    ax.annotate("projectile", xy=(-0.5, 0.75), xytext=(-2.9, 1.3),
                ha="left", va="center", arrowprops=ARROW, **LABEL)
    ax.annotate("vaporised and\nmelted zone", xy=(0.22, 0.05),
                xytext=(1.3, 0.45), ha="left", va="center",
                arrowprops=ARROW, **LABEL)
    ax.annotate("shock waves\n" + r"($P \sim 100$ GPa)", xy=(0.92, -0.92),
                xytext=(1.5, -1.55), ha="left", va="center",
                arrowprops=ARROW, **LABEL)
    ax.text(-2.9, -2.0, "target", ha="left", va="center", **LABEL)


def panel_b(ax: plt.Axes) -> None:
    """Draw excavation: transient cavity, ejecta curtain, rarefaction wave."""
    _setup(ax, "(b) Excavation")
    half_d, depth = 1.5, 1.0  # depth to diameter ratio 1:3
    xc = np.linspace(-half_d, half_d, 80)
    yc = -depth * (1.0 - (xc / half_d) ** 2)
    ground = np.vstack([[[-3.0, -2.3], [-3.0, 0.0]], np.column_stack([xc, yc]),
                        [[3.0, 0.0], [3.0, -2.3]]])
    ax.add_patch(Polygon(ground, closed=True, facecolor=GROUND,
                         edgecolor="none", zorder=1))
    ax.plot([-3.0, -half_d], [0.0, 0.0], color=GROUND_EDGE, lw=1.2, zorder=2)
    ax.plot([half_d, 3.0], [0.0, 0.0], color=GROUND_EDGE, lw=1.2, zorder=2)
    ax.plot(xc, yc, color=GROUND_EDGE, lw=1.4, zorder=2)
    # Ejecta blanket wedges at the rim and ballistic ejecta arrows
    for s in (-1, 1):
        ax.add_patch(Polygon([[s * half_d, 0.0], [s * 2.6, 0.0],
                              [s * half_d, 0.22]], facecolor="#b59b7a",
                             edgecolor=GROUND_EDGE, lw=0.6, zorder=3))
        for dx, dy, rad in ((1.1, 1.2, 0.35), (0.7, 0.6, 0.45)):
            ax.add_patch(FancyArrowPatch(
                (s * (half_d - 0.25), 0.05), (s * (half_d + dx), dy),
                connectionstyle=f"arc3,rad={-s * rad}", arrowstyle="-|>",
                mutation_scale=10, color="#8e5a3c", lw=1.3, zorder=6))
    # Expanding shock front and the rarefaction wave behind it
    ax.add_patch(Arc((0.0, 0.0), 3.8, 3.8, theta1=195, theta2=345,
                     color=SHOCK, lw=1.3, ls="--", zorder=4))
    ax.add_patch(Arc((0.0, 0.0), 2.8, 2.8, theta1=200, theta2=340,
                     color=RAREF, lw=1.3, ls=":", zorder=4))
    # Dimensions of the transient cavity
    ax.add_patch(FancyArrowPatch((-half_d, 0.3), (half_d, 0.3),
                                 arrowstyle="<->", mutation_scale=9,
                                 color=INK, lw=0.9, zorder=6))
    ax.text(0.0, 0.5, r"diameter $D$", ha="center", va="center", **LABEL)
    ax.add_patch(FancyArrowPatch((0.0, 0.0), (0.0, -depth),
                                 arrowstyle="<->", mutation_scale=9,
                                 color=INK, lw=0.9, zorder=6))
    ax.text(0.0, 0.76, r"depth $\approx D/3$", ha="center", va="center", **LABEL)
    ax.text(0.0, 1.05, "transient cavity", ha="center", va="center", **LABEL)
    ax.text(-2.95, 1.6, "ejecta curtain\n(ballistic paths)", ha="left",
            va="center", **LABEL)
    ax.text(2.95, 1.6, "ejecta\nblanket", ha="right", va="center", **LABEL)
    ax.annotate("shock front", xy=(-1.34, -1.34), xytext=(-2.95, -2.05),
                ha="left", va="center", arrowprops=ARROW, **LABEL)
    ax.annotate("rarefaction wave\n(decompression)", xy=(0.99, -0.99),
                xytext=(2.95, -1.95), ha="right", va="center",
                arrowprops=ARROW, **LABEL)


def panel_c(ax: plt.Axes) -> None:
    """Draw modification: a simple bowl crater and a complex crater."""
    _setup(ax, "(c) Modification")
    # Simple crater (left half): raised rim, bowl, breccia lens
    xs = np.linspace(-2.6, -0.4, 60)
    ys = -0.6 * np.sin(np.pi * (xs + 2.6) / 2.2) ** 1.0
    left = np.vstack([[[-3.0, -2.3], [-3.0, 0.0], [-2.75, 0.15], [-2.6, 0.0]],
                      np.column_stack([xs, ys]), [[-0.4, 0.0], [-0.25, 0.15],
                                                  [0.0, 0.0], [0.0, -2.3]]])
    ax.add_patch(Polygon(left, closed=True, facecolor=GROUND,
                         edgecolor=GROUND_EDGE, lw=1.2, zorder=1))
    lens_x = np.linspace(-2.2, -0.8, 30)
    lens = np.vstack([np.column_stack([lens_x, -0.6 * np.sin(np.pi * (lens_x + 2.6) / 2.2)]),
                      np.column_stack([lens_x[::-1], -0.6 * np.sin(np.pi * (lens_x[::-1] + 2.6) / 2.2) + 0.18])])
    ax.add_patch(Polygon(lens, closed=True, facecolor="#b59b7a",
                         edgecolor=GROUND_EDGE, lw=0.6, zorder=2))
    # Complex crater (right half): terraces, flat floor, central peak
    prof = [(0.2, 0.0), (0.45, 0.15), (0.6, -0.05), (0.85, -0.05), (0.95, -0.3),
            (1.2, -0.3), (1.3, -0.5), (1.65, -0.5), (1.85, -0.05), (2.05, -0.5),
            (2.4, -0.5), (2.5, -0.3), (2.75, -0.3), (2.85, -0.05), (3.0, 0.0)]
    right = [[0.2, -2.3]] + prof + [[3.0, -2.3]]
    ax.add_patch(Polygon(right, closed=True, facecolor=GROUND,
                         edgecolor=GROUND_EDGE, lw=1.2, zorder=1))
    ax.plot([0.1, 0.1], [-2.3, 1.9], color="0.6", lw=0.8, ls=":", zorder=3)
    ax.text(-1.5, 1.55, "simple crater\n(small)", ha="center", va="center", **LABEL)
    ax.text(1.6, 1.55, "complex crater\n(large)", ha="center", va="center", **LABEL)
    ax.annotate("slumped walls", xy=(-2.3, -0.35), xytext=(-2.95, 0.75),
                ha="left", va="center", arrowprops=ARROW, **LABEL)
    ax.annotate("slumped debris", xy=(-1.5, -0.5), xytext=(-1.5, -1.7),
                ha="center", va="center", arrowprops=ARROW, **LABEL)
    ax.annotate("terraces", xy=(0.9, -0.18), xytext=(0.45, 1.0),
                ha="left", va="center", arrowprops=ARROW, **LABEL)
    ax.annotate("central peak\n(floor rebound)", xy=(1.85, -0.08),
                xytext=(2.95, 0.45), ha="right", va="center",
                arrowprops=ARROW, **LABEL)
    ax.annotate("flat floor", xy=(2.2, -0.5), xytext=(2.2, -1.7),
                ha="center", va="center", arrowprops=ARROW, **LABEL)


def make_plot() -> plt.Figure:
    """Build the three-panel figure, save it and return it."""
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.9))
    panel_a(axes[0])
    panel_b(axes[1])
    panel_c(axes[2])
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.02, wspace=0.05)
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
