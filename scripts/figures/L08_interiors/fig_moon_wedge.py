"""Generate Fig. (`fig:moon-interior`).

Moon interior cross-section synthesising Apollo-era lunar seismology
and lunar laser ranging.

- Crust: ~34-43 km, anorthositic
- Silicate mantle to ~480 km from centre (partial-melt boundary)
- Liquid Fe-alloy outer core: ~330 km radius
- Solid inner core: ~240 km radius
- C/MR^2 = 0.3932 (Williams et al. 2014)

Caption / figure id : `fig:moon-interior`
Markdown source     : book/08_interiors/interiors.md
Citation keys       : Weber2011, Williams2014
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/moon_wedge.avif"

R_MOON = 1737.4  # km (mean radius)
R_PARTIAL_MELT = 480.0  # km (boundary layer)
R_LIQUID_CORE = 330.0   # km
R_INNER_CORE = 240.0    # km
CRUST_THICKNESS = 35.0  # km (representative)


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 8.5))

    R = R_MOON
    # Layers from outside to inside (full circles)
    ax.add_patch(Circle((0, 0), R, facecolor="#dcd6cd",
                        edgecolor="black", lw=1.2, label="Crust"))
    ax.add_patch(Circle((0, 0), R - CRUST_THICKNESS, facecolor="#a89784",
                        edgecolor="0.4", lw=0.4))
    ax.add_patch(Circle((0, 0), R_PARTIAL_MELT, facecolor="#c97356",
                        edgecolor="0.4", lw=0.6))
    ax.add_patch(Circle((0, 0), R_LIQUID_CORE, facecolor="#a13a35",
                        edgecolor="0.4", lw=0.6))
    ax.add_patch(Circle((0, 0), R_INNER_CORE, facecolor="#5d201b",
                        edgecolor="0.4", lw=0.6))

    # Wedge to expose layers (top-right quadrant cut)
    ax.add_patch(Wedge((0, 0), R, 0, 90, facecolor="#736356",
                       edgecolor="black", lw=0.6))
    ax.add_patch(Wedge((0, 0), R - CRUST_THICKNESS, 0, 90,
                       facecolor="#736356", edgecolor="0.4", lw=0.4))
    ax.add_patch(Wedge((0, 0), R_PARTIAL_MELT, 0, 90,
                       facecolor="#c97356", edgecolor="0.4", lw=0.4))
    ax.add_patch(Wedge((0, 0), R_LIQUID_CORE, 0, 90,
                       facecolor="#a13a35", edgecolor="0.4", lw=0.4))
    ax.add_patch(Wedge((0, 0), R_INNER_CORE, 0, 90,
                       facecolor="#5d201b", edgecolor="0.4", lw=0.4))

    # Wedge mantle label
    ax.text(R * 0.40, R * 0.40, "Silicate\nmantle",
            color="white", fontsize=12, weight="bold",
            ha="center", va="center")

    # Right-side fractional-radius scale
    sx = R + 120
    ax.plot([sx, sx], [-R, R], color="0.5", lw=0.8)
    fractions = [(R, "1.0\n(surface)"),
                 (R_PARTIAL_MELT, "0.28\n(core top)"),
                 (R_LIQUID_CORE, "0.22"),
                 (R_INNER_CORE, "0.14"),
                 (0, "0")]
    for r, label in fractions:
        ax.plot([sx - 20, sx + 20], [r, r], color="0.5", lw=0.8)
        ax.text(sx + 35, r, label, fontsize=9, va="center", color="0.3")
    ax.text(sx + 220, 0, r"Fractional radius $R/R_{\mathrm{Moon}}$",
            rotation=90, va="center", ha="center", fontsize=10, color="0.3")

    # External labels
    ax.annotate("Solid inner core ($\\sim$240 km)",
                xy=(R_INNER_CORE * 0.4, R_INNER_CORE * 0.5),
                xytext=(-1000, 1450),
                fontsize=10, color="0.2",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))
    ax.annotate("Liquid outer core ($\\sim$330 km)",
                xy=(R_LIQUID_CORE * 0.7, R_LIQUID_CORE * 0.4),
                xytext=(-1000, 1300),
                fontsize=10, color="0.2",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))
    ax.annotate("Partial-melt layer ($\\sim$480 km)",
                xy=(R_PARTIAL_MELT * 0.6, R_PARTIAL_MELT * 0.7),
                xytext=(-1000, 1150),
                fontsize=10, color="0.2",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))
    ax.annotate("Crust ($\\sim$30-40 km)",
                xy=(R * 0.95, -R * 0.25),
                xytext=(R + 380, -R * 0.4),
                fontsize=10, color="0.2",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    # Annotation box bottom-left
    ax.text(-R * 1.05, -R * 0.95,
            r"$R_{\mathrm{Moon}} = 1737.4$ km" + "\n"
            r"$R_{\mathrm{core,top}} \approx 480$ km" + "\n"
            r"$C/MR^2 = 0.3932$",
            fontsize=10,
            bbox=dict(facecolor="white", edgecolor="0.7", pad=4))

    lim = R + 1100
    ax.set_xlim(-lim, lim + 200)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Moon interior (Apollo seismology + lunar laser ranging)",
                 fontsize=12)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
