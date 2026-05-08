"""Generate Fig. (`fig:walker-loop`).

Schematic carbonate-silicate feedback loop redrawn after Walker,
Hays & Kasting (1981). Five boxes (T, rainfall, weathering, CO2,
greenhouse forcing) connected by arrows with explicit + or - signs;
the product of signs along the loop is negative -> stabilising
(climate thermostat).

Caption / figure id : `fig:walker-loop`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md
Citation key        : Walker1981
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/walker_loop.avif"

BOX_FACE = "#cfe5ff"


def _box(ax, x, y, w, h, text):
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                         boxstyle="round,pad=0.04,rounding_size=0.06",
                         facecolor=BOX_FACE, edgecolor="black", lw=1.0)
    ax.add_patch(box)
    ax.text(x, y, text, ha="center", va="center", fontsize=11)


def _clip_to_box(p0, p1, box_w, box_h):
    """Move p1 inward along (p0 -> p1) so it lands on box edge, not centre."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    norm = (dx ** 2 + dy ** 2) ** 0.5
    if norm == 0:
        return p1
    ux, uy = dx / norm, dy / norm
    # Distance from box centre p1 inward to its bounding edge along -(ux,uy)
    if abs(ux) * box_h > abs(uy) * box_w:
        # exits through left/right edge
        d = (box_w / 2) / abs(ux)
    else:
        # exits through top/bottom edge
        d = (box_h / 2) / abs(uy)
    return (p1[0] - ux * d, p1[1] - uy * d)


def _arrow(ax, p0, p1, sign, box_w, box_h):
    color_sign = "#1f6b3b" if sign == "+" else "#a02121"
    p0_clip = _clip_to_box(p1, p0, box_w, box_h)
    p1_clip = _clip_to_box(p0, p1, box_w, box_h)
    ax.add_patch(FancyArrowPatch(
        p0_clip, p1_clip, arrowstyle="->", mutation_scale=22,
        color="black", lw=1.4))
    # Sign label at midpoint, offset perpendicular
    mx, my = 0.5 * (p0_clip[0] + p1_clip[0]), 0.5 * (p0_clip[1] + p1_clip[1])
    dx, dy = p1_clip[0] - p0_clip[0], p1_clip[1] - p0_clip[1]
    norm = (dx ** 2 + dy ** 2) ** 0.5
    px, py = -dy / norm, dx / norm
    ax.text(mx + 0.05 * px, my + 0.05 * py, sign,
            color=color_sign, fontsize=22, weight="bold",
            ha="center", va="center")


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(11, 8))

    # Box positions arranged as a pentagon (roughly)
    nodes = {
        "T":         (0.5, 0.85),  # surface temperature
        "rain":      (0.88, 0.55),  # rainfall & runoff
        "weath":     (0.78, 0.18),  # silicate weathering
        "CO2":       (0.22, 0.18),  # atmospheric CO2
        "force":     (0.12, 0.55),  # greenhouse forcing
    }
    box_w, box_h = 0.18, 0.14

    _box(ax, *nodes["T"], box_w, box_h, "Surface\ntemperature $T$")
    _box(ax, *nodes["rain"], box_w, box_h, "Rainfall\n& runoff")
    _box(ax, *nodes["weath"], box_w, box_h, "Silicate\nweathering")
    _box(ax, *nodes["CO2"], box_w, box_h, "Atmospheric\nCO$_2$")
    _box(ax, *nodes["force"], box_w, box_h, "Greenhouse\nforcing")

    # Arrows along the loop with signs (T -> rain -> weath -> CO2 -> force -> T)
    def _edge(name_a, name_b):
        ax_, ay_ = nodes[name_a]
        bx_, by_ = nodes[name_b]
        # Pull endpoints back from box centres slightly
        return (ax_, ay_), (bx_, by_)

    for a, b, sign in [
        ("T", "rain", "+"),
        ("rain", "weath", "+"),
        ("weath", "CO2", "-"),
        ("CO2", "force", "+"),
        ("force", "T", "+"),
    ]:
        p0, p1 = _edge(a, b)
        _arrow(ax, p0, p1, sign, box_w, box_h)

    # Title and footer
    ax.set_title("Carbonate-silicate feedback (Walker, Hays & Kasting 1981)",
                 fontsize=13, weight="bold")
    ax.text(0.5, 0.02,
            r"Loop product:  $(+)(+)(-)(+)(+) = -$    "
            r"(negative feedback: climate thermostat)",
            fontsize=11, ha="center", style="italic")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
