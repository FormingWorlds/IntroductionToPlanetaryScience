"""Generate Fig. (`fig:life-definition`).

Working definition of life schematic diagram illustrating:
- Three overlapping circles representing the core attributes:
  self-replicating, metabolising, and evolving chemical system.
- Central intersection marking Life (working definition).
- Two surrounding context boxes for solvent (water as default)
  and chemistry (carbon-based as default; silicon, ammonia and
  methane solvents not excluded).

Citations and provenance:
- Markdown source: book/14_synthesis/
  Heading: "What is life?" (book/14_synthesis/
- Definition: "The working definition, going back to {cite:t}`Lederberg1965`,
  is that life is a self-replicating, metabolising, evolving chemical
  system." (book/14_synthesis/
- Dominant biology: "The search for life elsewhere is dominated by
  carbon-based, water-as-solvent biology because we know its spectroscopic
  and geochemical fingerprints." (book/14_synthesis/
- Alternative biochemistries: "Alternative biochemistries (silicon-based,
  ammonia-solvent, methane-solvent) are not excluded in principle, but
  they are not our default working hypothesis." (book/14_synthesis/
- Sketch specification:
  "A diagram of the working definition: three overlapping circles labelled
  self-replicating, metabolising, evolving with 'life' at the centre, and
  around them two boxes 'solvent (water as default)' and 'chemistry
  (carbon-based as default; silicon, ammonia and methane solvents not
  excluded)'; clean, few words."

Caption / figure id : `fig:life-definition`
Markdown source     : book/14_synthesis/
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/14_synthesis/figures/life_definition.avif"


def draw_schematic(ax: plt.Axes) -> None:
    """Draw the working definition Venn diagram and surrounding context boxes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes on which to draw the schematic diagram.
    """
    ax.set_aspect("equal")
    ax.set_xlim(-4.9, 4.9)
    ax.set_ylim(-2.4, 2.6)
    ax.axis("off")

    # Equilateral triangle geometry for 3-circle Venn diagram
    # Centered at origin with offset d and radius R.
    d = 0.82
    radius = 1.38

    c_top = (0.0, d)
    c_left = (-d * np.cos(np.pi / 6), -d * 0.5)
    c_right = (d * np.cos(np.pi / 6), -d * 0.5)

    # Circle patches for the three attributes from Lederberg (1965):
    # Metabolising (amber), Self-replicating (blue), Evolving (green).
    circ_top = Circle(
        c_top, radius, facecolor="#fcebc2", edgecolor="#b8860b",
        alpha=0.40, lw=1.8, zorder=2,
    )
    circ_left = Circle(
        c_left, radius, facecolor="#d0e3fa", edgecolor="#2563eb",
        alpha=0.40, lw=1.8, zorder=2,
    )
    circ_right = Circle(
        c_right, radius, facecolor="#c9ebd5", edgecolor="#16a34a",
        alpha=0.40, lw=1.8, zorder=2,
    )

    ax.add_patch(circ_top)
    ax.add_patch(circ_left)
    ax.add_patch(circ_right)

    # Attribute labels positioned in the non-overlapping outer regions
    ax.text(
        0.0, d + 0.62, "Metabolising", ha="center", va="center",
        fontsize=11, weight="bold", color="#78350f", zorder=4,
    )
    ax.text(
        c_left[0] - 0.32, c_left[1] - 0.38, "Self-replicating", ha="center",
        va="center", fontsize=11, weight="bold", color="#1e3a8a", zorder=4,
    )
    ax.text(
        c_right[0] + 0.32, c_right[1] - 0.38, "Evolving", ha="center",
        va="center", fontsize=11, weight="bold", color="#14532d", zorder=4,
    )

    # Central Life badge at the intersection of all three circles
    ax.text(
        0.0, -0.05, "Life", ha="center", va="center",
        fontsize=13, weight="bold", color="#0f172a", zorder=5,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#ffffff",
                  edgecolor="#94a3b8", lw=1.0, alpha=0.92),
    )

    # Left box: Solvent (water as default,
    box_left = FancyBboxPatch(
        (-4.85, -1.25), 2.6, 2.5,
        boxstyle="round,pad=0.08,rounding_size=0.18",
        facecolor="#f0f6fc", edgecolor="#60a5fa", lw=1.3, zorder=3,
    )
    ax.add_patch(box_left)
    ax.text(
        -3.52, 0.65, "Solvent", ha="center", va="center",
        fontsize=11, weight="bold", color="#1e3a8a", zorder=4,
    )
    ax.text(
        -3.52, 0.08, "Water as default", ha="center", va="center",
        fontsize=10, color="#1e293b", zorder=4,
    )
    ax.text(
        -3.55, -0.62, "(ammonia and\nmethane solvents\nnot excluded)",
        ha="center", va="center", fontsize=10, color="#475569",
        style="italic", linespacing=1.2, zorder=4,
    )

    # Right box: Chemistry (carbon-based as default; alternatives not excluded)
    box_right = FancyBboxPatch(
        (2.25, -1.25), 2.6, 2.5,
        boxstyle="round,pad=0.08,rounding_size=0.18",
        facecolor="#fdfbf7", edgecolor="#d97706", lw=1.3, zorder=3,
    )
    ax.add_patch(box_right)
    ax.text(
        3.52, 0.65, "Chemistry", ha="center", va="center",
        fontsize=11, weight="bold", color="#78350f", zorder=4,
    )
    ax.text(
        3.52, 0.08, "Carbon-based\nas default", ha="center", va="center",
        fontsize=10, color="#1e293b", linespacing=1.25, zorder=4,
    )
    ax.text(
        3.55, -0.62, "(silicon-based\nchemistry\nnot excluded)",
        ha="center", va="center", fontsize=10, color="#475569",
        style="italic", linespacing=1.2, zorder=4,
    )

    # Schematic title designating diagram nature per instructions
    ax.set_title(
        "Working definition of life (schematic)",
        fontsize=12, pad=12, weight="bold",
    )


def make_plot() -> Path:
    """Build the working definition of life schematic and save to AVIF.

    Returns
    -------
    pathlib.Path
        Path to the saved AVIF image.
    """
    apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    draw_schematic(ax)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Execute figure generation and display the output path."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()