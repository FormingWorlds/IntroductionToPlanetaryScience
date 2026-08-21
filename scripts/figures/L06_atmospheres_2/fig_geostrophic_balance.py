"""Generate Fig. (`fig:geostrophic-balance`).

Force-balance schematic of the geostrophic wind in the Northern
Hemisphere: the pressure-gradient force -grad(P)/rho (blue, toward
low pressure) balances the Coriolis force -f k x v_g (red, toward
high pressure), so the wind v_g blows parallel to the isobars with
low pressure to its left.

Caption / figure id : `fig:geostrophic-balance`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md
Citation key        : Pierrehumbert2010
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/geostrophic_balance.avif"

BLUE = "#1f6db8"
RED = "#b22222"


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(7.0, 5.2))

    # Isobars: low pressure at the top, high pressure at the bottom
    for y in (0.22, 0.78):
        ax.plot([0.03, 0.97], [y, y], color="0.45", linestyle="--",
                lw=1.2)
    ax.text(0.95, 0.80, r"$P_0 - \delta P$   (low pressure)",
            fontsize=11, ha="right", va="bottom", color="0.35")
    ax.text(0.95, 0.20, r"$P_0$   (high pressure)",
            fontsize=11, ha="right", va="top", color="0.35")

    # Air parcel at the balance point
    x0, y0 = 0.40, 0.50
    ax.plot(x0, y0, "o", color="black", ms=7, zorder=5)

    # Pressure-gradient force: toward low pressure (up)
    ax.add_patch(FancyArrowPatch((x0, y0), (x0, 0.74),
                                 arrowstyle="->", mutation_scale=20,
                                 color=BLUE, lw=2.4))
    ax.text(x0 - 0.02, 0.64,
            "Pressure-gradient force\n" + r"$-\nabla P / \rho$",
            fontsize=11, ha="right", va="center", color=BLUE)

    # Coriolis force: toward high pressure (down), equal and opposite
    ax.add_patch(FancyArrowPatch((x0, y0), (x0, 0.26),
                                 arrowstyle="->", mutation_scale=20,
                                 color=RED, lw=2.4))
    ax.text(x0 - 0.02, 0.36,
            "Coriolis force\n" + r"$-f\,\hat{k} \times \mathbf{v}_g$",
            fontsize=11, ha="right", va="center", color=RED)

    # Geostrophic wind: parallel to the isobars, low pressure on its left
    ax.add_patch(FancyArrowPatch((x0, y0), (0.82, y0),
                                 arrowstyle="->", mutation_scale=22,
                                 color="black", lw=2.6))
    ax.text(0.62, 0.525, r"$\mathbf{v}_g$", fontsize=13,
            ha="center", va="bottom")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title("Geostrophic balance (Northern Hemisphere)",
                 fontsize=12)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
