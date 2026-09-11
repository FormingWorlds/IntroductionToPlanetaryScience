"""The faint young Sun paradox and proposed warming mechanisms.

Effective temperature evolves as 255 K * (L/L_sun)**(1/4), with L/L_sun rising
linearly from 0.70 at 4.5 Ga (text gives 0.71 yielding 234 K) to 1.0 today.
Adding a 33 K greenhouse offset leaves early Earth below freezing despite liquid water.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/faint_young_sun.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(9.0, 4.2), gridspec_kw={"width_ratios": [1.15, 1.0]}
    )

    # (a) The faint young Sun paradox
    time = np.linspace(4.5, 0.0, 200)
    L_rel = 0.70 + 0.30 * (1.0 - time / 4.5)
    T_eff = 255.0 * (L_rel ** 0.25)
    T_surf = T_eff + 33.0

    ax1.axhspan(185, 273, facecolor="#e8f1fa", alpha=0.6, zorder=0)
    ax1.axhline(273, color="#4a6984", linestyle="--", lw=1.2, label="Freezing point (273 K)")

    ax1.plot(time, T_surf, color="#c0392b", lw=2.0, label=r"Surface $T$ ($T_{\mathrm{eff}} + 33\ \mathrm{K}$)")
    ax1.plot(time, T_eff, color="#1f6db8", lw=2.0, label=r"Effective $T_{\mathrm{eff}} = 255\ (L/L_\odot)^{1/4}\ \mathrm{K}$")

    evidence = [
        (4.4, "zircon oxygen\nisotopes (4.4 Ga)", 196),
        (3.8, "pillow basalts and\nsedimentary rocks (3.8 Ga)", 214),
        (3.5, "stromatolites (3.5 Ga)", 228),
    ]
    for age, label, y_pos in evidence:
        ax1.plot(age, 185, "^", color="#2ca25f", markersize=7, clip_on=False, zorder=5)
        ax1.text(
            age - 0.12,
            y_pos,
            label,
            ha="left",
            va="bottom",
            fontsize=9,
            color="#2ca25f",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.0),
        )

    ax1.set_xlim(4.8, -0.1)
    ax1.set_ylim(185, 322)
    ax1.set_xlabel("Time before present (Ga)", fontsize=10)
    ax1.set_ylabel("Temperature (K)", fontsize=10)
    ax1.set_title("(a) The faint young Sun paradox", fontsize=11)
    ax1.legend(loc="upper left", frameon=False, fontsize=9)

    # (b) Proposed solutions
    ax2.set_xlim(-0.2, 9.5)
    ax2.set_ylim(-0.6, 4.6)
    ax2.set_yticks([0, 4])
    ax2.set_yticklabels(["faint Sun\nsurface temperature", "liquid water"], fontsize=10)
    ax2.set_xticks([])
    ax2.spines["bottom"].set_visible(False)

    ax2.axhline(0, color="0.4", linestyle="--", lw=1.2)
    ax2.axhline(4, color="#1f6db8", linestyle="--", lw=1.2)

    solutions = [
        ("CO2 at 10 to 1000 times present", "#c0392b", "#fdebd0"),
        ("biogenic CH4\n(long lifetime in an anoxic atmosphere)", "#c46b1a", "#fdebd0"),
        ("N2 at 2 to 3 times present\n(pressure broadening)", "#4a6984", "#e8f1fa"),
        ("lower albedo\n(less land, fewer clouds)", "#2ca25f", "#e8f5e9"),
    ]

    for i, (text_label, col, fill_col) in enumerate(solutions):
        ax2.add_patch(Rectangle((0.4, i), 1.0, 1.0, facecolor=fill_col, edgecolor="0.7", lw=1.0))
        arrow = FancyArrowPatch(
            (0.9, i + 0.15),
            (0.9, i + 0.85),
            arrowstyle="-|>",
            mutation_scale=14,
            color=col,
            lw=2.5,
        )
        ax2.add_patch(arrow)
        ax2.text(1.8, i + 0.5, text_label, ha="left", va="center", fontsize=10, color=col)

    ax2.set_title("(b) Proposed solutions", fontsize=11)

    fig.tight_layout()
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
