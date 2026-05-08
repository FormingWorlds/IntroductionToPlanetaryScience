"""Generate Fig. (`fig:icegiant-interior`).

Three-layer schematic of an ice giant interior (Uranus or Neptune):

- H/He envelope: ~20% by mass
- Hot dense ice / superionic layer (water, ammonia, methane):
  ~60-70% by mass
- Rocky/icy core: ~10-20% by mass

Caption / figure id : `fig:icegiant-interior`
Markdown source     : book/08_interiors/interiors.md
Citation key        : Helled2020
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/icegiant_interior.avif"

LAYERS = [
    ("H/He envelope\n~20% by mass",                            1.00, "#a8c8ec"),
    ("Hot dense ice/superionic layer\n~60-70% by mass",        0.78, "#3a6c92"),
    ("Rocky/icy core\n~10-20% by mass",                        0.18, "#7a4a2a"),
]


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(9.5, 7.5))

    for _, r, c in LAYERS:
        ax.add_patch(Circle((0, 0), r, facecolor=c, edgecolor="black", lw=0.7))

    # Annotation lines pointing into each layer's actual mid-radius
    import numpy as np
    label_xs = [1.2, 1.2, 1.2]
    label_ys = [0.65, 0.0, -0.65]
    # mid-radii of layers: H/He envelope 0.89; ice 0.48; rocky core 0.09
    anchor_polar = [
        (0.89, 60),    # H/He envelope (upper-right)
        (0.48, 0),     # ice/superionic (right)
        (0.09, -60),   # rocky core (deep, lower-right)
    ]
    for (label, _, _), x_l, y_l, (r_anchor, theta_deg) in zip(
            LAYERS, label_xs, label_ys, anchor_polar):
        theta = np.radians(theta_deg)
        xy = (r_anchor * np.cos(theta), r_anchor * np.sin(theta))
        ax.annotate(label, xy=xy, xytext=(x_l, y_l),
                    fontsize=10, ha="left", va="center",
                    arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    ax.set_xlim(-1.2, 2.6)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Ice giant interior (Uranus/Neptune three-layer model)",
                 fontsize=12)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
