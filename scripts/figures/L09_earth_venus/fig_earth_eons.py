"""Timeline of Earth's geologic eons and eras with a Phanerozoic zoom.

Caption / figure id: fig:earth-eons
Markdown source: book/09_earth_venus/earth_venus.md
Citation key: Gradstein2020

Boundary ages follow the Geologic Time Scale 2020 compilation: the eon
boundaries at 4000, 2500, and 538.8 Ma, the Archean and Proterozoic era
boundaries, and the Phanerozoic era boundaries at 251.9 and 66.0 Ma.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from scripts.figures._shared.style import apply_style, save_figure, text_color_on

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book" / "09_earth_venus" / "figures" / "earth_eons_timeline.avif"

T0 = 4540.0  # age of Earth in Ma
PHANEROZOIC_BASE = 538.8  # base of the Cambrian in Ma

# Eons as (name, old edge, young edge, fill color); pastel fills keep
# black labels readable and pass the ink-collision check.
EON_COLORS = {
    "Hadean": "#eb9c8d",
    "Archean": "#f5c986",
    "Proterozoic": "#cfe3a8",
    "Phanerozoic": "#a8d8e8",
}
EONS = [
    ("Hadean", T0, 4000.0),
    ("Archean", 4000.0, 2500.0),
    ("Proterozoic", 2500.0, PHANEROZOIC_BASE),
    ("Phanerozoic", PHANEROZOIC_BASE, 0.0),
]

# Eras of the Archean and Proterozoic, labelled at 65 degrees above the bar.
ERAS = [
    ("Eoarchean", 4000.0, 3600.0),
    ("Paleoarchean", 3600.0, 3200.0),
    ("Mesoarchean", 3200.0, 2800.0),
    ("Neoarchean", 2800.0, 2500.0),
    ("Paleoproterozoic", 2500.0, 1600.0),
    ("Mesoproterozoic", 1600.0, 1000.0),
    ("Neoproterozoic", 1000.0, PHANEROZOIC_BASE),
]

# Phanerozoic eras drawn on the zoom bar, shades of the Phanerozoic blue.
PHANEROZOIC_ERAS = [
    ("Paleozoic", PHANEROZOIC_BASE, 251.9, "#7fbcd9"),
    ("Mesozoic", 251.9, 66.0, "#a8d8e8"),
    ("Cenozoic", 66.0, 0.0, "#d3ecf5"),
]

# Vertical layout in data units.
BAR1_Y0, BAR1_Y1 = 2.1, 2.9
BAR2_Y0, BAR2_Y1 = 0.1, 0.9


def _zoom_x(t_ma):
    """Map a Phanerozoic age in Ma onto the full-width zoom bar."""
    return t_ma * T0 / PHANEROZOIC_BASE


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(11.5, 3.8))
    ax.set_xlim(T0, 0.0)
    ax.set_ylim(-0.55, 5.4)
    ax.axis("off")

    # Top bar: the four eons over the full age of Earth.
    for name, old, young in EONS:
        fill = EON_COLORS[name]
        ax.add_patch(
            Rectangle((young, BAR1_Y0), old - young, BAR1_Y1 - BAR1_Y0,
                      facecolor=fill, edgecolor="none", zorder=2)
        )
        ax.text(0.5 * (old + young), 0.5 * (BAR1_Y0 + BAR1_Y1), name,
                ha="center", va="center", fontsize=11,
                color=text_color_on(fill), zorder=4)

    # White separators at the internal era boundaries.
    for _, old, young in ERAS[1:]:
        ax.plot([old, old], [BAR1_Y0, BAR1_Y1], color="white", lw=1.2, zorder=3)

    # Era ticks and 45-degree labels above the top bar.
    for name, old, young in ERAS:
        center = 0.5 * (old + young)
        ax.plot([center, center], [BAR1_Y1, BAR1_Y1 + 0.12],
                color="0.4", lw=0.8, zorder=3)
        ax.text(center, BAR1_Y1 + 0.18, name, rotation=65,
                rotation_mode="anchor", ha="left", va="bottom",
                fontsize=10, color="0.35", zorder=4)

    # Boundary ages below the top bar.
    for t, label, ha in [(T0, "4.54 Ga", "left"), (4000.0, "4.0 Ga", "center"),
                         (2500.0, "2.5 Ga", "center")]:
        ax.text(t, BAR1_Y0 - 0.12, label, ha=ha, va="top",
                fontsize=10.5, color="0.25", zorder=4)

    # Bottom bar: the Phanerozoic stretched to full width.
    for name, old, young, fill in PHANEROZOIC_ERAS:
        x_old, x_young = _zoom_x(old), _zoom_x(young)
        ax.add_patch(
            Rectangle((x_young, BAR2_Y0), x_old - x_young, BAR2_Y1 - BAR2_Y0,
                      facecolor=fill, edgecolor="none", zorder=2)
        )
        ax.text(0.5 * (x_old + x_young), 0.5 * (BAR2_Y0 + BAR2_Y1), name,
                ha="center", va="center", fontsize=11,
                color=text_color_on(fill), zorder=4)

    # Boundary ages below the zoom bar.
    for t, label, ha in [(PHANEROZOIC_BASE, "539 Ma", "left"),
                         (251.9, "252 Ma", "center"),
                         (66.0, "66 Ma", "center"), (0.0, "0", "right")]:
        ax.text(_zoom_x(t), BAR2_Y0 - 0.12, label, ha=ha, va="top",
                fontsize=10.5, color="0.25", zorder=4)

    # Dashed fan lines tie the Phanerozoic block to its zoom bar.
    ax.plot([PHANEROZOIC_BASE, _zoom_x(PHANEROZOIC_BASE)], [BAR1_Y0, BAR2_Y1],
            color="0.6", lw=0.9, ls=(0, (4, 3)), zorder=1)
    ax.plot([0.0, 0.0], [BAR1_Y0, BAR2_Y1],
            color="0.6", lw=0.9, ls=(0, (4, 3)), zorder=1)

    # Black outlines around both bars.
    for y0, y1 in [(BAR1_Y0, BAR1_Y1), (BAR2_Y0, BAR2_Y1)]:
        ax.add_patch(
            Rectangle((0.0, y0), T0, y1 - y0, facecolor="none",
                      edgecolor="black", lw=0.8, zorder=5)
        )

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main():
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
