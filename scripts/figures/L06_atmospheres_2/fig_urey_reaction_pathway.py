"""The Urey reaction pathway for silicate weathering and carbonate deposition.

Atmospheric carbon dioxide dissolves in rainwater, weathers silicate rock,
and is carried by rivers to the ocean to form sedimentary carbonate rock.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/urey_reaction_pathway.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(9.5, 4.4))
    fig.subplots_adjust(left=0.03, right=0.97, top=0.92, bottom=0.08)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title("The Urey reaction pathway", fontsize=11)

    ax.text(
        5.0, 4.15,
        r"$\mathrm{CaSiO_3} + \mathrm{CO_2} + \mathrm{H_2O} \longrightarrow \mathrm{CaCO_3} + \mathrm{SiO_2} + \mathrm{H_2O}$",
        fontsize=10, ha="center", va="center",
    )

    boxes = [
        (0.15, 1.25, "#eef4f8", "#4a6984", "$\\mathrm{CO_2}$ in the\natmosphere"),
        (1.65, 1.45, "#e8f1fa", "#1f6db8", "dissolves in\nrainwater: weak\ncarbonic acid"),
        (3.35, 1.45, "#fdebd0", "#c46b1a", "weathers silicate\nrock ($\\mathrm{CaSiO_3}$)"),
        (5.05, 1.55, "#e8f1fa", "#1f6db8", "rivers carry\n$\\mathrm{Ca^{2+}},\\ \\mathrm{HCO_3^-},\\ \\mathrm{SiO_2}$\nto the ocean"),
        (6.85, 2.95, "#e8f5e9", "#2ca25f", "$\\mathrm{CaCO_3}$ precipitates\n(shells, skeletons, abiotic grains)\ndeposited as sedimentary rock"),
    ]

    y_box = 1.9
    h_box = 1.7
    y_c = y_box + h_box / 2

    for i, (x, w, fc, ec, text) in enumerate(boxes):
        patch = FancyBboxPatch(
            (x, y_box), w, h_box,
            boxstyle="round,pad=0.02,rounding_size=0.1",
            facecolor=fc, edgecolor=ec, lw=1.2,
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y_c, text, fontsize=10, ha="center", va="center", color="0.15")
        if i < 4:
            next_x = boxes[i + 1][0]
            ax.add_patch(FancyArrowPatch(
                (x + w + 0.035, y_c), (next_x - 0.035, y_c),
                arrowstyle="-|>", mutation_scale=10, color="0.3", lw=1.3,
            ))

    ax.text(
        5.0, 1.15,
        r"net effect: $\mathrm{CO_2}$ drawn out of the atmosphere into carbonate rock, the long-term carbon sink",
        fontsize=10, ha="center", va="center", color="0.2",
    )

    ax.add_patch(FancyArrowPatch(
        (0.5, 0.55), (9.5, 0.55),
        arrowstyle="simple,tail_width=4,head_width=14,head_length=14",
        facecolor="#4a6984", edgecolor="none",
    ))

    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
