"""Generate Fig. (`fig:moi-two-layer`).

Conceptual illustration of the moment of inertia factor as a probe of
differentiation. Left panel: cutaway views of three two-layer spheres
with the same outer radius and the same core/mantle density contrast
f = rho_c/rho_m = 2.5, differing only in core radius fraction
x = R_c/R. Right panel: the two-layer relation
C/MR^2 = (2/5) [(f-1)x^5 + 1] / [(f-1)x^3 + 1] as a function of x,
with the three cutaway configurations marked. All numbers are computed
from the relation; the x = 0.546 case reproduces the worked Earth
example of the blackboard derivation.

Caption / figure id : `fig:moi-two-layer`
Markdown source     : book/08_interiors/interiors.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/moi_two_layer.avif"

F_CONTRAST = 2.5           # rho_c / rho_m, the blackboard-example value
CORE_FRACTIONS = [0.0, 0.30, 0.546]   # x = R_c/R per cutaway; 0.546 = Earth example
PANEL_LABELS = ["Uniform sphere", "Small dense core", "Large dense core\n(Earth-like)"]

MANTLE_COLOR = "#e8c88f"
CORE_COLOR = "#8c564b"
CURVE_COLOR = "#1f77b4"
UNIFORM_COLOR = "#d62728"


def moi_factor(x: np.ndarray | float, f: float = F_CONTRAST) -> np.ndarray | float:
    """Moment of inertia factor of a two-layer sphere.

    Parameters
    ----------
    x : array_like
        Core radius fraction R_c/R in [0, 1].
    f : float
        Core-to-mantle density ratio rho_c/rho_m.

    Returns
    -------
    array_like
        C/MR^2 from the two-layer relation (eq:moi-two-layer).
    """
    return 0.4 * ((f - 1.0) * np.asarray(x) ** 5 + 1.0) / ((f - 1.0) * np.asarray(x) ** 3 + 1.0)


def draw_cutaway(ax, cx: float, cy: float, r: float, x: float) -> None:
    """Draw one cutaway sphere: mantle disc, core disc, quarter cut open."""
    ax.add_patch(Circle((cx, cy), r, facecolor=MANTLE_COLOR,
                        edgecolor="black", lw=1.0, zorder=2))
    if x > 0:
        ax.add_patch(Circle((cx, cy), r * x, facecolor=CORE_COLOR,
                            edgecolor="black", lw=0.8, zorder=3))
        # open a quarter wedge so the layering reads as a cutaway
        ax.add_patch(Wedge((cx, cy), r, 0, 90, facecolor="white",
                           edgecolor="black", lw=1.0, zorder=4))
        ax.plot([cx, cx + r * x], [cy, cy], color="black", lw=0.8, zorder=5)
        # a fixed point offset keeps the label box clear of the radius line
        ax.annotate(r"$R_c$", (cx + 0.55 * r * x, cy),
                    textcoords="offset points", xytext=(0, 4),
                    va="bottom", fontsize=9, zorder=6)


def make_plot() -> Path:
    apply_style()
    fig, (ax_l, ax_r) = plt.subplots(
        1, 2, figsize=(10, 4.4), gridspec_kw={"width_ratios": [1.15, 1.0]})

    # Left: three cutaway spheres on a common baseline
    ax_l.set_xlim(-0.2, 6.6)
    ax_l.set_ylim(-1.6, 1.9)
    ax_l.set_aspect("equal")
    ax_l.axis("off")
    radius = 0.95
    centers = [0.9, 3.2, 5.5]
    for cx, x, label in zip(centers, CORE_FRACTIONS, PANEL_LABELS):
        draw_cutaway(ax_l, cx, 0.35, radius, x)
        val = float(moi_factor(x))
        ax_l.text(cx, -0.95, label, ha="center", va="top", fontsize=10)
        ax_l.text(cx, 1.45, rf"$C/MR^2 = {val:.3f}$", ha="center",
                  va="bottom", fontsize=10.5, weight="bold")
    ax_l.text(3.2, -1.55,
              rf"Same outer radius, density contrast $\rho_c/\rho_m = {F_CONTRAST}$",
              ha="center", va="top", fontsize=9.5, style="italic")

    # Right: the two-layer relation with the three configurations marked
    xg = np.linspace(0.0, 1.0, 400)
    ax_r.plot(xg, moi_factor(xg), color=CURVE_COLOR, lw=2.0)
    ax_r.axhline(0.4, color=UNIFORM_COLOR, linestyle="--", lw=1.4)
    ax_r.text(0.02, 0.402, r"uniform sphere: $2/5$",
              color=UNIFORM_COLOR, fontsize=9.5, va="bottom")
    for x in CORE_FRACTIONS:
        val = float(moi_factor(x))
        ax_r.plot(x, val, "o", color=CORE_COLOR, ms=7, zorder=5)
        if x == 0.0:
            # below the flat start of the curve, clear of the 2/5 line text
            ax_r.annotate(f"{val:.3f}", (x, val), textcoords="offset points",
                          xytext=(10, -22), fontsize=9)
        else:
            # the curve descends to the right, so below-left is clear
            ax_r.annotate(f"{val:.3f}", (x, val), textcoords="offset points",
                          xytext=(-8, -16), ha="right", fontsize=9)
    ax_r.set_xlabel(r"Core radius fraction $x = R_c/R$")
    ax_r.set_ylabel(r"$C/MR^2$")
    ax_r.set_xlim(0, 1)
    ax_r.set_ylim(0.30, 0.42)
    ax_r.set_title(
        r"$\dfrac{C}{MR^2} = \dfrac{2}{5}\,\dfrac{(f-1)x^5 + 1}{(f-1)x^3 + 1}$,"
        rf"  $f = {F_CONTRAST}$", fontsize=11)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
