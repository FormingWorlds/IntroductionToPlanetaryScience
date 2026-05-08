"""Generate Fig. (`fig:mars-wedge`).

Mars interior labelled cross-section in the wedge style used for
Earth and the Moon. Dimensions from InSight body waves (Stahler
2021, Khan 2021):

- Mean radius: 3389.5 km
- Core radius: 1830 +/- 40 km (-> r/R = 0.54)
- Crust thickness: ~25-45 km (InSight landing site), up to ~70 km
  beneath the southern highlands
- C/MR^2 = 0.364

Caption / figure id : `fig:mars-wedge`
Markdown source     : book/08_interiors/interiors.md
Citation keys       : Stahler2021, Khan2021
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/mars_wedge.avif"

R_MARS = 3389.5  # km
R_CORE = 1830.0  # km
CRUST_THICKNESS = 35.0  # km (representative of InSight site)


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 8.5))

    R = R_MARS
    # Full circles (back layers)
    ax.add_patch(Circle((0, 0), R, facecolor="#e1d2bc",
                        edgecolor="black", lw=1.2))
    ax.add_patch(Circle((0, 0), R - CRUST_THICKNESS, facecolor="#a17c5a",
                        edgecolor="0.4", lw=0.4))
    ax.add_patch(Circle((0, 0), R_CORE, facecolor="#9c2f29",
                        edgecolor="0.4", lw=0.6, linestyle="--"))

    # Wedge cut (top-right) showing layers solid
    ax.add_patch(Wedge((0, 0), R, 0, 90, facecolor="#a17c5a",
                       edgecolor="black", lw=0.6))
    ax.add_patch(Wedge((0, 0), R_CORE, 0, 90, facecolor="#a13a35",
                       edgecolor="0.4", lw=0.4))

    # Wedge labels
    ax.text(R * 0.55, R * 0.55, "Silicate\nmantle",
            color="white", fontsize=12, weight="bold",
            ha="center", va="center")
    ax.text(R_CORE * 0.5, R_CORE * 0.5, "Liquid\nFe-S\ncore",
            color="white", fontsize=11, weight="bold",
            ha="center", va="center")

    # Right-side fractional-radius scale
    sx = R + 250
    ax.plot([sx, sx], [-R, R], color="0.5", lw=0.8)
    fractions = [(R, "1.0\n(surface)"),
                 (R_CORE, "0.54\n(CMB)"),
                 (0, "0")]
    for r, label in fractions:
        ax.plot([sx - 40, sx + 40], [r, r], color="0.5", lw=0.8)
        ax.text(sx + 80, r, label, fontsize=9, va="center", color="0.3")
    ax.text(sx + 500, 0, r"Fractional radius $R/R_{\mathrm{Mars}}$",
            rotation=90, va="center", ha="center", fontsize=10, color="0.3")

    # Crust annotation pointer
    ax.annotate("Crust ($\\sim$25-45 km)",
                xy=(R * 0.99, -R * 0.10),
                xytext=(R + 600, -R * 0.20),
                fontsize=10, color="0.2",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    # Bottom-left info box
    ax.text(-R * 1.05, -R * 0.95,
            r"$R_{\mathrm{core}} = 1830$ km" + "\n"
            r"$R_{\mathrm{Mars}} = 3389.5$ km" + "\n"
            r"$C/MR^2 = 0.364$",
            fontsize=10,
            bbox=dict(facecolor="white", edgecolor="0.7", pad=4))

    lim = R + 1300
    ax.set_xlim(-lim, lim + 500)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Mars interior (InSight-constrained), labelled cross-section",
                 fontsize=12)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
