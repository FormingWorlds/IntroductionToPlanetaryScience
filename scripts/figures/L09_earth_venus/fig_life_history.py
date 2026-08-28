"""Timeline of major events in the history of life on Earth.

Caption / figure id: fig:earth-life-history
Markdown source: book/09_earth_venus/earth_venus.md
Citation keys: Mojzsis1996; Dodd2017; Nutman2016; Lyons2014; Catling2020;
Hoffman2017; Gradstein2020

Event ages are representative round numbers from the cited sources; the
eon boundaries follow the Geologic Time Scale 2020 compilation.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from scripts.figures._shared.style import apply_style, save_figure, text_color_on
from scripts.figures.L09_earth_venus.fig_earth_eons import (
    EON_COLORS,
    EONS,
    PHANEROZOIC_BASE,
    T0,
)

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book" / "09_earth_venus" / "figures" / "earth_life_timeline.avif"

# Events as (age in Ma, label, stem level). Levels stagger the 45-degree
# labels; a label may cover younger events only if their stems are shorter,
# which the level assignment below guarantees.
EVENTS = [
    (4540.0, "Earth forms", 2),
    (4300.0, "liquid water oceans", 1),
    (3770.0, "oldest claimed biosignatures", 3),
    (3480.0, "oldest stromatolites", 1),
    (2400.0, "Great Oxidation Event", 2),
    (1870.0, "first probable eukaryote fossils", 1),
    (1050.0, "multicellular algae", 3),
    (571.0, "Ediacaran biota", 3),
    (539.0, "Cambrian explosion", 1),
    (66.0, "end-Cretaceous impact", 2),
]

# Glaciation intervals drawn as bands on the eon strip, labelled below it.
BANDS = [
    (2450.0, 2220.0, "Huronian glaciations"),
    (717.0, 635.0, "snowball glaciations"),
]
BAND_COLOR = "#9ecae1"

STRIP_Y0, STRIP_Y1 = 0.0, 0.5
LEVEL_TOPS = {1: 1.6, 2: 2.6, 3: 3.6}


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(11.5, 5.0))
    ax.set_xlim(4650.0, -60.0)
    ax.set_ylim(-0.55, 5.8)
    ax.grid(False)

    # Eon strip along the bottom.
    for name, old, young in EONS:
        fill = EON_COLORS[name]
        ax.add_patch(
            Rectangle((young, STRIP_Y0), old - young, STRIP_Y1 - STRIP_Y0,
                      facecolor=fill, edgecolor="none", zorder=2)
        )
        ax.text(0.5 * (old + young), 0.5 * (STRIP_Y0 + STRIP_Y1), name,
                ha="center", va="center", fontsize=8,
                color=text_color_on(fill), zorder=5)
    for boundary in (4000.0, 2500.0, PHANEROZOIC_BASE):
        ax.plot([boundary, boundary], [STRIP_Y0, STRIP_Y1],
                color="white", lw=1.2, zorder=3)
    ax.add_patch(
        Rectangle((0.0, STRIP_Y0), T0, STRIP_Y1 - STRIP_Y0, facecolor="none",
                  edgecolor="black", lw=0.8, zorder=6)
    )

    # Glaciation bands overlie the strip and are labelled below it.
    for old, young, label in BANDS:
        ax.add_patch(
            Rectangle((young, STRIP_Y0), old - young, STRIP_Y1 - STRIP_Y0,
                      facecolor=BAND_COLOR, edgecolor="none",
                      alpha=0.9, zorder=4)
        )
        ax.text(0.5 * (old + young), -0.08, label, ha="center", va="top",
                fontsize=8, color="0.3", zorder=5)

    # Lollipop events: stem from the strip top, marker, 45-degree label.
    for age, label, level in EVENTS:
        top = LEVEL_TOPS[level]
        ax.plot([age, age], [STRIP_Y1, top], color="0.45", lw=1.3, zorder=3)
        ax.plot([age], [top], marker="o", ms=5, color="0.25", zorder=4)
        ax.annotate(label, xy=(age, top), xytext=(4, 4),
                    textcoords="offset points", rotation=45,
                    rotation_mode="anchor", ha="left", va="bottom",
                    fontsize=9, color="0.2", zorder=5)

    ax.set_xticks([4000, 3000, 2000, 1000, 0])
    ax.set_xticklabels(["4", "3", "2", "1", "0"])
    ax.set_xlabel("Age (Ga)")
    ax.set_yticks([])
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main():
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
