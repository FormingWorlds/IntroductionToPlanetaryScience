"""Condensing cloud species across solar system atmospheres.

Condensation depends on temperature and vapour composition under the
Clausius-Clapeyron equation across different planetary atmospheres.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/cloud_species_map.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, axes = plt.subplots(1, 5, figsize=(9.5, 4.6))

    # Five horizontal panels, one per planet
    titles = ["Earth", "Venus", "Mars", "Titan", "Jupiter / Saturn"]
    for ax, title in zip(axes, titles):
        ax.set_title(title, fontsize=11)
        ax.set_xlim(0, 1)
        ax.set_xticks([])

    ax_e, ax_v, ax_m, ax_t, ax_j = axes

    # Earth
    # "Earth: H2O clouds (liquid droplets and ice crystals), with cloud base at ~1 to 2 km"
    ax_e.set_ylim(0, 10)
    ax_e.set_ylabel("Altitude (km)", fontsize=10)
    ax_e.set_yticks([0, 2, 4, 6, 8, 10])
    ax_e.add_patch(Rectangle((0.12, 1.0), 0.76, 1.0, facecolor="#e8f1fa", edgecolor="#1f6db8", lw=1.5))
    ax_e.text(0.5, 2.7, "$\\mathrm{H_2O}$\ncloud base\n1 to 2 km", ha="center", va="bottom", fontsize=10, color="#1f6db8")

    # Venus
    # "Venus: H2SO4 (sulfuric acid) droplets at 48 to 70 km altitude"
    ax_v.set_ylim(0, 80)
    ax_v.set_ylabel("Altitude (km)", fontsize=10)
    ax_v.set_yticks([0, 20, 40, 60, 80])
    ax_v.add_patch(Rectangle((0.08, 48), 0.84, 22, facecolor="#fdebd0", edgecolor="#c46b1a", lw=1.5))
    ax_v.text(0.5, 59, "$\\mathrm{H_2SO_4}$\ndroplets\n48 to 70 km", ha="center", va="center", fontsize=10, color="#c46b1a")

    # Mars
    # "Mars: CO2 ice and H2O ice clouds at high altitude"
    ax_m.set_ylim(0, 10)
    ax_m.set_ylabel("Height", fontsize=10)
    ax_m.set_yticks([])
    ax_m.add_patch(Rectangle((0.12, 6.8), 0.76, 1.4, facecolor="#e8f1fa", edgecolor="#4a6984", lw=1.5))
    ax_m.text(0.5, 7.5, "$\\mathrm{CO_2}$ ice", ha="center", va="center", fontsize=10, color="#4a6984")
    ax_m.add_patch(Rectangle((0.12, 4.8), 0.76, 1.4, facecolor="#e8f1fa", edgecolor="#1f6db8", lw=1.5))
    ax_m.text(0.5, 5.5, "$\\mathrm{H_2O}$ ice", ha="center", va="center", fontsize=10, color="#1f6db8")
    ax_m.text(0.5, 8.8, "high altitude", ha="center", va="center", fontsize=10, color="0.3", style="italic")

    # Titan
    # "Titan: CH4 and C2H6 (ethane) clouds near the surface"
    ax_t.set_ylim(0, 10)
    ax_t.set_ylabel("Height", fontsize=10)
    ax_t.set_yticks([])
    ax_t.add_patch(Rectangle((0.12, 0.6), 0.76, 2.0, facecolor="#e8f5e9", edgecolor="#2ca25f", lw=1.5))
    ax_t.text(0.5, 1.6, "$\\mathrm{CH_4}$ and\n$\\mathrm{C_2H_6}$", ha="center", va="center", fontsize=10, color="#2ca25f")
    ax_t.text(0.5, 3.2, "near the\nsurface", ha="center", va="bottom", fontsize=10, color="0.3", style="italic")

    # Jupiter / Saturn
    # "Jupiter/Saturn: Layered NH3, NH4SH, and H2O clouds at successively deeper levels"
    ax_j.set_ylim(10, 0)
    ax_j.set_ylabel("Depth increases", fontsize=10)
    ax_j.set_yticks([])
    ax_j.add_patch(Rectangle((0.10, 1.0), 0.65, 1.8, facecolor="#e8f1fa", edgecolor="#4a6984", lw=1.5))
    ax_j.text(0.425, 1.9, "$\\mathrm{NH_3}$", ha="center", va="center", fontsize=10, color="#4a6984")
    ax_j.add_patch(Rectangle((0.10, 3.8), 0.65, 1.8, facecolor="#fdebd0", edgecolor="#c46b1a", lw=1.5))
    ax_j.text(0.425, 4.7, "$\\mathrm{NH_4SH}$", ha="center", va="center", fontsize=10, color="#c46b1a")
    ax_j.add_patch(Rectangle((0.10, 6.6), 0.65, 1.8, facecolor="#e8f1fa", edgecolor="#1f6db8", lw=1.5))
    ax_j.text(0.425, 7.5, "$\\mathrm{H_2O}$", ha="center", va="center", fontsize=10, color="#1f6db8")
    ax_j.add_patch(FancyArrowPatch((0.86, 1.2), (0.86, 8.2), arrowstyle="-|>", mutation_scale=12, color="0.3", lw=1.5))

    # Overall title and bottom note:
    fig.suptitle("Which species condenses where", fontsize=11)
    fig.text(0.5, 0.02, "the same Clausius-Clapeyron physics in every case", ha="center", va="bottom", fontsize=10, color="0.3")
    fig.tight_layout(rect=[0, 0.06, 1, 0.95])
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
