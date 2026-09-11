"""The carbonate-silicate thermostat on terrestrial planets.

Liquid water and active volcanism are both required to regulate CO2 over Gyr.
Without water, CO2 accumulates to 92 bar; without volcanism, it drops to 6 mbar.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/thermostat_failure.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(8.8, 4.4))
    ax.set_xlim(0.0, 11.2)
    ax.set_ylim(0.0, 5.5)
    ax.axis("off")
    ax.set_title("The thermostat needs both ingredients", fontsize=11, pad=10)

    # Box coordinates: two columns and two rows
    bx1 = 3.10
    bw = 3.65
    gap = 0.40
    bx2 = bx1 + bw + gap

    # Column headers (Liquid water: yes / no)
    ax.text(
        bx1 + bw / 2,
        5.0,
        "Liquid water: yes",
        ha="center",
        va="center",
        fontsize=10,
        weight="bold",
        color="0.2",
    )
    ax.text(
        bx2 + bw / 2,
        5.0,
        "Liquid water: no",
        ha="center",
        va="center",
        fontsize=10,
        weight="bold",
        color="0.2",
    )

    # Row headers (Active volcanism: yes / no)
    ax.text(
        bx1 - 0.35,
        3.7,
        "Active volcanism: yes",
        ha="right",
        va="center",
        fontsize=10,
        weight="bold",
        color="0.2",
    )
    ax.text(
        bx1 - 0.35,
        1.5,
        "Active volcanism: no",
        ha="right",
        va="center",
        fontsize=10,
        weight="bold",
        color="0.2",
    )

    # Four cells of the 2x2 matrix:
    # 1. Earth (yes water, yes volcanism)
    # 2. Venus (no water, yes volcanism)
    # 3. Mars (yes water, no volcanism)
    # 4. No cycle (no water, no volcanism)
    boxes = [
        (
            bx1,
            2.8,
            bw,
            1.8,
            "Earth",
            "#1b663e",
            "Thermostat works",
            r"$\mathrm{CO_2}$ regulated over Gyr",
            "#e8f5e9",
            "#2ca25f",
        ),
        (
            bx2,
            2.8,
            bw,
            1.8,
            "Venus",
            "#8a450b",
            "Weathering stops, volcanic",
            r"$\mathrm{CO_2}$ accumulates: 92 bar",
            "#fdebd0",
            "#c46b1a",
        ),
        (
            bx1,
            0.6,
            bw,
            1.8,
            "Mars (after about 3 Ga)",
            "#154c80",
            "Source broken, weathering and",
            r"escape draw $\mathrm{CO_2}$ down: 6 mbar",
            "#e8f1fa",
            "#1f6db8",
        ),
        (
            bx2,
            0.6,
            bw,
            1.8,
            "No cycle",
            "0.3",
            "No water or volcanism",
            "Thermostat fails",
            "#f0f2f5",
            "#4a6984",
        ),
    ]

    for x, y, w, h, title, tc, l1, l2, bg, edge in boxes:
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0,rounding_size=0.15",
            facecolor=bg,
            edgecolor=edge,
            lw=1.5,
        )
        ax.add_patch(patch)
        xc = x + w / 2.0
        ax.text(
            xc,
            y + 1.35,
            title,
            ha="center",
            va="center",
            fontsize=10,
            weight="bold",
            color=tc,
        )
        ax.text(xc, y + 0.85, l1, ha="center", va="center", fontsize=10, color="0.2")
        ax.text(xc, y + 0.45, l2, ha="center", va="center", fontsize=10, color="0.2")

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
