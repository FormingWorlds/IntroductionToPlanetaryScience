"""Generate Fig. (`fig:lunar-magma-ocean`).

Schematic radial structure of the lunar magma ocean at the end of
solidification, redrawn after Elkins-Tanton (2012). Concentric
rings: Fe core, lower-mantle cumulates, dense ilmenite-rich
shell, pyroxenite/dunite cumulates, urKREEP layer, anorthositic
crust.

Caption / figure id : `fig:lunar-magma-ocean`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : ElkinsTanton2012

Pure schematic; layer thicknesses are not to lunar scale (the crust
is exaggerated for visibility), but layer order and naming follow
Elkins-Tanton (2012, Annu. Rev. Earth Planet. Sci. 40).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/elkinstanton2012_lunar_magma_ocean.avif"

# Concentric layers: (label, outer radius fraction, color)
# Inner-to-outer; radii are proportional, exaggerated for clarity.
LAYERS = [
    ("Fe core",                       0.18, "#1a1a1a"),
    ("Lower-mantle cumulates",        0.65, "#2e6f2e"),
    ("Pyroxenite / dunite cumulates", 0.82, "#5aa55a"),
    ("Dense ilmenite-rich layer",     0.86, "#7a4a2a"),
    ("urKREEP layer",                 0.93, "#d4a017"),
    ("Anorthosite crust (~40 km)",    1.00, "#e6dec0"),
]


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 7.5))
    R = 1.0  # outer radius

    # Draw layers as filled disks, outermost first so inner overlays
    radii = [r for _, r, _ in LAYERS]
    colors = [c for _, _, c in LAYERS]
    labels = [l for l, _, _ in LAYERS]

    for r, c in zip(reversed(radii), reversed(colors)):
        ax.add_patch(Wedge((0, 0), r, 0, 360, facecolor=c, edgecolor="none"))

    # Outline of the Moon
    ax.add_patch(Wedge((0, 0), R, 0, 360, facecolor="none",
                       edgecolor="black", lw=1.0))

    # Centre label
    ax.text(0, 0, "Fe\ncore", color="white", ha="center", va="center",
            fontsize=11, weight="bold")

    # Outside annotations with arrows
    annot_specs = [
        ("Anorthosite crust (~40 km)", (R, 0.0), (1.55, 0.55), "left"),
        ("urKREEP layer", (0.97, -0.18), (1.55, -0.30), "left"),
        ("Pyroxenite / dunite\ncumulates", (0.74, 0.50), (1.0, 1.20), "left"),
        ("Dense ilmenite-rich layer\n(sinks after crystallisation)",
         (-0.74, 0.55), (-1.7, 1.05), "right"),
        ("Lower-mantle cumulates", (-0.40, -0.45), (-1.05, -1.25), "right"),
    ]
    for text, target, anchor, ha in annot_specs:
        ax.annotate(text, xy=target, xytext=anchor,
                    fontsize=10, ha=ha, va="center", weight="bold",
                    arrowprops=dict(arrowstyle="->", lw=0.9, color="black"))

    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-1.7, 1.7)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Schematic of the lunar magma ocean end-state\n"
                 "(anorthosite crust + urKREEP + cumulate mantle "
                 "+ ilmenite overturn + Fe core)",
                 fontsize=12)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
