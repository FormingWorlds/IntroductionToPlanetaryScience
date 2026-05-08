"""Generate Fig. (`fig:greenhouse-effect`).

Schematic of the one-layer grey-greenhouse model: incoming stellar
shortwave (1-A)F_*/4, surface emission sigma T_s^4, atmospheric
absorption + emission epsilon * sigma T_a^4 up and down.

Caption / figure id : `fig:greenhouse-effect`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation key        : Pierrehumbert2010
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/greenhouse_one_layer.avif"

YELLOW = "#e8a420"
RED = "#c93434"
GROUND = "#8b6648"
SKY = "#cfe5ff"
SPACE = "#1a2440"


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(7.5, 7.0))

    # Background bands
    ax.add_patch(Rectangle((0, 0.85), 1, 0.15, color=SPACE))
    ax.add_patch(Rectangle((0, 0.15), 1, 0.70, color=SKY, alpha=0.6))
    ax.add_patch(Rectangle((0, 0.0), 1, 0.15, color=GROUND, alpha=0.7))

    # Top of atmosphere line and label
    ax.plot([0, 1], [0.85, 0.85], "k-", lw=0.8)
    ax.text(0.5, 0.96, "One-layer greenhouse model",
            fontsize=13, ha="center", va="center", color="white",
            weight="bold")
    ax.text(0.5, 0.87, "Top of atmosphere", fontsize=9,
            ha="center", color="white")

    # Atmospheric layer box
    layer_y0, layer_y1 = 0.46, 0.56
    ax.add_patch(Rectangle((0.15, layer_y0), 0.70,
                           layer_y1 - layer_y0,
                           facecolor="white", edgecolor="black", lw=1.0))
    ax.text(0.5, 0.51,
            r"Atmospheric layer  ($\varepsilon$, $T_a$)",
            ha="center", va="center", fontsize=11)

    # Surface label
    ax.text(0.5, 0.075,
            r"Surface  (temperature $T_s$)",
            ha="center", va="center", fontsize=12, weight="bold",
            color="white")

    # 1) incoming SW (yellow, downward) just left of centre
    ax.add_patch(FancyArrowPatch((0.18, 0.95), (0.18, 0.16),
                                 arrowstyle="->", mutation_scale=18,
                                 color=YELLOW, lw=2.2))
    ax.text(0.22, 0.75, r"$(1-A) F_\star / 4$",
            color=YELLOW, fontsize=11, ha="left", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5,
                      alpha=0.7))

    # 2) Surface IR up (red): from surface to atmospheric layer
    ax.add_patch(FancyArrowPatch((0.4, 0.16), (0.4, layer_y0 - 0.005),
                                 arrowstyle="->", mutation_scale=18,
                                 color=RED, lw=2.0))
    ax.text(0.42, 0.32, r"$\sigma T_s^4$",
            color=RED, fontsize=11, ha="left", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    # 3) Atmosphere transmits part of surface IR straight to space
    # (red arrow rising through layer to space at the right side)
    ax.add_patch(FancyArrowPatch((0.62, 0.16), (0.62, 0.95),
                                 arrowstyle="->", mutation_scale=14,
                                 color=RED, lw=1.4, alpha=0.6))
    ax.text(0.55, 0.70, r"$(1-\varepsilon)\,\sigma T_s^4$",
            color=RED, fontsize=10, ha="right", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    # 4) Atmospheric layer emits up (epsilon * sigma * T_a^4)
    ax.add_patch(FancyArrowPatch((0.78, layer_y1 + 0.005),
                                 (0.78, 0.95),
                                 arrowstyle="->", mutation_scale=18,
                                 color=RED, lw=2.0))
    ax.text(0.78, 0.74,
            r"$\varepsilon\,\sigma T_a^4$ (up)",
            color=RED, fontsize=10, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    # 5) Atmospheric layer emits down
    ax.add_patch(FancyArrowPatch((0.78, layer_y0 - 0.005),
                                 (0.78, 0.16),
                                 arrowstyle="->", mutation_scale=18,
                                 color=RED, lw=2.0))
    ax.text(0.78, 0.32,
            r"$\varepsilon\,\sigma T_a^4$ (down)",
            color=RED, fontsize=10, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
