"""Generate Fig. (`fig:msr-architecture`).

Block flow diagram of the Mars Sample Return (MSR) campaign concept
illustrating the six-stage architecture from sample caching at Jezero
crater to terrestrial curation and laboratory analysis.

The campaign concept follows the architecture described in
book/10_mercury_mars/and
1. Perseverance collects and caches sample tubes at Jezero crater
   ("samples cached by Perseverance at Jezero",.
2. Sample Retrieval Lander with a Mars Ascent Vehicle arrives at Mars.
3. Mars Ascent Vehicle launches sample container into Mars orbit.
4. Earth Return Orbiter captures container in Mars orbit.
5. Earth entry and landing of sample container.
6. Curation and laboratory analysis for definitive biosignatures
   ("definitive biosignatures from past or present Martian life",
.

A note records that the architecture and schedule are being
rebaselined following the 2024 cost review.

Caption / figure id : `fig:msr-architecture`
Markdown source     : book/10_mercury_mars/(lines 729-734)
Material source     :(lines 1-14)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/10_mercury_mars/figures/msr_architecture.avif"

# Color palette: warm terracotta for Mars, muted blue for Earth return
MARS_BG = "#faeee9"
MARS_EDGE = "#b95332"
MARS_HEADER = "#8f2f18"

EARTH_BG = "#edf4fa"
EARTH_EDGE = "#2f6fa8"
EARTH_HEADER = "#1d4f7c"

NOTE_BG = "#f5f5f5"
NOTE_EDGE = "#b0b0b0"
TEXT_DARK = "#222222"
ARROW_TRANSIT = "#444444"

# Box geometry and content for the six stages
BOX_STAGES = [
    # Row 1: Mars surface and ascent (left to right)
    (
        0.30, 3.45, 2.90, 1.55,
        "1. Sample caching",
        "Perseverance collects\nand caches sample\ntubes at Jezero",
        MARS_BG, MARS_EDGE, MARS_HEADER,
    ),
    (
        3.55, 3.45, 2.90, 1.55,
        "2. Retrieval lander",
        "Sample Retrieval\nLander with Mars\nAscent Vehicle (MAV)",
        MARS_BG, MARS_EDGE, MARS_HEADER,
    ),
    (
        6.80, 3.45, 2.90, 1.55,
        "3. Mars ascent",
        "Launch of sample\ncontainer into\nMars orbit",
        MARS_BG, MARS_EDGE, MARS_HEADER,
    ),
    # Row 2: Earth return and curation (right to left)
    (
        6.80, 1.15, 2.90, 1.55,
        "4. Orbital capture",
        "Earth Return Orbiter\ncaptures container\nin Mars orbit",
        EARTH_BG, EARTH_EDGE, EARTH_HEADER,
    ),
    (
        3.55, 1.15, 2.90, 1.55,
        "5. Earth return",
        "Earth entry and\nlanding of sample\ncontainer",
        EARTH_BG, EARTH_EDGE, EARTH_HEADER,
    ),
    (
        0.30, 1.15, 2.90, 1.55,
        "6. Sample analysis",
        "Curation and\nlaboratory analysis\nfor biosignatures",
        EARTH_BG, EARTH_EDGE, EARTH_HEADER,
    ),
]


def draw_boxes(ax: plt.Axes) -> None:
    """Draw the six campaign stage boxes with titles and descriptions.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes for the schematic diagram.
    """
    for x, y, w, h, title, body, bg, edge, h_color in BOX_STAGES:
        patch = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0,rounding_size=0.12",
            facecolor=bg, edgecolor=edge, lw=1.3,
        )
        ax.add_patch(patch)
        xc = x + w / 2.0
        ax.text(
            xc, y + h - 0.32, title,
            fontsize=10, fontweight="bold", ha="center", va="center",
            color=h_color,
        )
        ax.text(
            xc, y + (h - 0.42) / 2.0, body,
            fontsize=10, ha="center", va="center",
            color=TEXT_DARK, linespacing=1.2,
        )


def draw_arrows(ax: plt.Axes) -> None:
    """Draw connecting flow arrows between consecutive campaign stages.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes for the schematic diagram.
    """
    # Row 1 flow: Stage 1 -> Stage 2 -> Stage 3 (Mars surface to orbit)
    ax.add_patch(FancyArrowPatch(
        (3.22, 4.225), (3.53, 4.225),
        arrowstyle="-|>", mutation_scale=14, lw=1.5, color=MARS_EDGE,
    ))
    ax.add_patch(FancyArrowPatch(
        (6.47, 4.225), (6.78, 4.225),
        arrowstyle="-|>", mutation_scale=14, lw=1.5, color=MARS_EDGE,
    ))

    # Vertical transition: Stage 3 -> Stage 4 (Mars orbit rendezvous)
    ax.add_patch(FancyArrowPatch(
        (8.25, 3.42), (8.25, 2.73),
        arrowstyle="-|>", mutation_scale=14, lw=1.5, color=ARROW_TRANSIT,
    ))
    ax.text(
        8.05, 3.075, "Mars orbit\nrendezvous",
        fontsize=10, ha="right", va="center", color=ARROW_TRANSIT,
    )

    # Row 2 flow: Stage 4 -> Stage 5 -> Stage 6 (Earth return and analysis)
    ax.add_patch(FancyArrowPatch(
        (6.78, 1.925), (6.47, 1.925),
        arrowstyle="-|>", mutation_scale=14, lw=1.5, color=EARTH_EDGE,
    ))
    ax.add_patch(FancyArrowPatch(
        (3.53, 1.925), (3.22, 1.925),
        arrowstyle="-|>", mutation_scale=14, lw=1.5, color=EARTH_EDGE,
    ))


def draw_rebaseline_note(ax: plt.Axes) -> None:
    """Draw note box indicating architecture rebaselining after 2024 review.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes for the schematic diagram.
    """
    note_patch = FancyBboxPatch(
        (0.30, 0.15), 9.40, 0.70,
        boxstyle="round,pad=0,rounding_size=0.10",
        facecolor=NOTE_BG, edgecolor=NOTE_EDGE, lw=0.9, ls="--",
    )
    ax.add_patch(note_patch)
    ax.text(
        5.0, 0.50,
        "Note: Campaign architecture and schedule are being rebaselined\n"
        "after the 2024 cost review; concept shown is schematic.",
        fontsize=10, ha="center", va="center", style="italic",
        color="#333333", linespacing=1.25,
    )


def make_plot() -> Path:
    """Build the Mars Sample Return architecture schematic figure.

    Returns
    -------
    pathlib.Path
        Path to the saved AVIF figure file.
    """
    apply_style()
    fig, ax = plt.subplots(figsize=(7.8, 4.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # Title: labelled as schematic per course guidelines
    ax.text(
        5.0, 5.68, "Mars Sample Return Campaign Concept (Schematic)",
        fontsize=12, fontweight="bold", ha="center", va="center",
    )

    # Phase section headers
    ax.text(
        0.30, 5.20, "On Mars: collection and ascent",
        fontsize=10.5, fontweight="bold", ha="left", va="center",
        color=MARS_HEADER,
    )
    ax.text(
        0.30, 2.95, "Return to Earth: capture, entry, analysis",
        fontsize=10.5, fontweight="bold", ha="left", va="center",
        color=EARTH_HEADER,
    )

    # Draw diagram components
    draw_boxes(ax)
    draw_arrows(ax)
    draw_rebaseline_note(ax)

    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Build the figure and display the output path."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()