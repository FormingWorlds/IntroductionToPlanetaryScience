"""Generate Fig. (`fig:saturn-schematic`).

Schematic radial structure of Saturn highlighting the helium-rain
layer between molecular and metallic hydrogen, and the diffuse
heavy-element core inferred from ring-seismology constraints
(Mankovich 2021, Helled 2020).

Caption / figure id : `fig:saturn-schematic`
Markdown source     : book/08_interiors/interiors.md
Citation keys       : Mankovich2021, Helled2020
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/saturn_interior_schematic.avif"

# Concentric layers (outer to inner): label, outer fractional radius, color.
# Boundaries follow the Mankovich 2021 ring-seismology fuzzy core extending
# to ~0.60 R_Sat, with the molecular/metallic-H transition at ~0.70 R_Sat
# bracketing the He-rain layer (Guillot 1999; Nettelmann 2013; Helled 2020).
LAYERS = [
    ("Molecular H$_2$\ngas to liquid",                 1.00, "#bca3d6"),
    ("Helium-rain layer\nHe droplets settle",         0.78, "#f0e3a8"),
    ("Metallic hydrogen\n(conducting; dynamo source)", 0.70, "#7a559e"),
    ("Diffuse core (gradational)\n~17 M$_\\oplus$ heavy elements", 0.55, "#c08e57"),
]


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(9.5, 7.5))

    # Draw outermost-first so inner overlays
    for _, r, c in LAYERS:
        ax.add_patch(Circle((0, 0), r, facecolor=c, edgecolor="black", lw=0.7))

    # Annotation arrows (right side); each anchor placed at the actual
    # mid-radius of the corresponding layer along an angle that points
    # the arrow into that layer specifically.
    import numpy as np
    label_xs = [1.2, 1.2, 1.2, 1.2]
    label_ys = [0.78, 0.30, -0.20, -0.78]
    # (layer mid-radius, anchor angle in degrees)
    anchor_polar = [
        (0.89, 70),    # molecular H2 (upper-right)
        (0.74, 28),    # He-rain (right)
        (0.625, -25),  # metallic-H (lower-right)
        (0.275, -65),  # diffuse core (lower-right, deep in)
    ]
    for (label, _, _), x_l, y_l, (r_anchor, theta_deg) in zip(
            LAYERS, label_xs, label_ys, anchor_polar):
        theta = np.radians(theta_deg)
        xy = (r_anchor * np.cos(theta), r_anchor * np.sin(theta))
        ax.annotate(label, xy=xy, xytext=(x_l, y_l),
                    fontsize=10, ha="left", va="center",
                    arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    ax.set_xlim(-1.2, 2.5)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Saturn's interior: helium rain and diffuse core",
                 fontsize=12)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
