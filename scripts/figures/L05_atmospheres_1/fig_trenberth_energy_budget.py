"""Generate Fig. (`fig:trenberth`).

Earth's globally averaged energy budget in W m^-2, adapted from the
satellite-era inventory of Trenberth et al. (2009): 340 incoming
shortwave splits into 100 reflected, 80 absorbed in the atmosphere,
and 160 absorbed at the surface; the surface emits 396 longwave and
receives 333 back-radiation; latent and sensible heat carry 97 to
the atmosphere; 240 outgoing longwave leaves at the top.

Caption / figure id : `fig:trenberth`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation key        : Trenberth2009
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/trenberth_energy_budget.avif"

YELLOW = "#e8a420"
RED = "#c93434"
GREEN = "#2e8b57"
GROUND = "#8b6648"
SKY = "#cfe5ff"
SPACE = "#1a2440"

# (label, x, y_from, y_to, flux W m^-2, colour, y_label)
# y_label None centres the label on the arrow; explicit values keep the
# rotated text inside the sky band and clear of the split line at 0.68
ARROWS = [
    ("Incoming solar 340",         0.07, 0.965, 0.680, 340, YELLOW, 0.78),
    ("Reflected 100",              0.15, 0.680, 0.965, 100, YELLOW, 0.80),
    ("Absorbed in atmosphere 80",  0.23, 0.680, 0.440,  80, YELLOW, 0.51),
    ("Absorbed at surface 160",    0.31, 0.680, 0.145, 160, YELLOW, None),
    ("Latent + sensible 97",       0.45, 0.145, 0.520,  97, GREEN, None),
    ("Surface LW 396",             0.57, 0.145, 0.600, 396, RED, None),
    ("Back-radiation 333",         0.66, 0.600, 0.145, 333, RED, None),
    ("Outgoing LW 240",            0.82, 0.600, 0.965, 240, RED, None),
]


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(9.5, 6.5))

    # Background bands: space, atmosphere, surface
    ax.add_patch(Rectangle((0, 0.90), 1, 0.10, color=SPACE))
    ax.add_patch(Rectangle((0, 0.14), 1, 0.76, color=SKY, alpha=0.6))
    ax.add_patch(Rectangle((0, 0.0), 1, 0.14, color=GROUND, alpha=0.85))

    ax.text(0.5, 0.95, "Space:   340 in  =  100 reflected  +  240 out",
            fontsize=11, ha="center", va="center", color="white",
            weight="bold")
    ax.text(0.5, 0.07, "Surface:   160 + 333  =  396 + 97",
            fontsize=11, ha="center", va="center", color="white",
            weight="bold")

    # Split node: the incoming beam divides into its three branches
    ax.plot([0.07, 0.31], [0.68, 0.68], color="0.45", lw=1.0)

    for label, x, y0, y1, flux, color, y_lab in ARROWS:
        lw = float(np.clip(flux / 45.0, 1.5, 8.0))
        ax.add_patch(FancyArrowPatch((x, y0), (x, y1),
                                     arrowstyle="->",
                                     mutation_scale=14 + lw,
                                     color=color, lw=lw))
        if y_lab is None:
            y_lab = 0.5 * (y0 + y1)
        ax.text(x - 0.033, y_lab, label, fontsize=10, color=color,
                ha="center", va="center", rotation=90)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title(r"Earth's global mean energy budget (W m$^{-2}$)",
                 fontsize=13)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
