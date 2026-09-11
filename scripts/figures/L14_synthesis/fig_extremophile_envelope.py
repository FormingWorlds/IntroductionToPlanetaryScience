"""Generate Fig. (`fig:extremophile-envelope`).

Two-row schematic comparing the temperature envelope of Earth life with
the astrobiological potential of icy-moon ocean worlds:
(a) Temperature axis from -30 to 130 deg C showing the known envelope of
    Earth life (-20 to 122 deg C) with the classical temperate surface
    range (0 to 40 deg C) as an inner bar, and labelled extreme
    environments at their temperatures (subglacial lakes at -20 deg C,
    hydrothermal vents above 120 deg C).
(b) A second axis row for icy-moon ocean worlds (Europa, Enceladus, Titan)
    marked as 'liquid water in contact with rock, outside the classical
    habitable zone' without invented temperatures.

Citations and provenance:
- Markdown source: book/14_synthesis/synthesis.md:488-499
  Heading: "Extremophiles and the redefinition of 'habitable'"
- Extremophile temperature limits: synthesis.md:493
  "Earth life occupies environments from hydrothermal vents over 120 deg C
  to subglacial lakes at -20 deg C"
- Icy moons astrobiology targets: synthesis.md:497-498
  "Icy moons (Europa, Enceladus, Titan) became primary astrobiology targets"
  "liquid water in contact with rock and a chemical free-energy gradient"
- Specification: material_13.txt:15
  "A temperature axis figure (x from -30 to 130 degrees C) showing the range
  of Earth life as a bar from -20 to 122 degrees C, with the classical
  temperate surface range (0 to 40 degrees C) as an inner bar, labelled
  environments at their temperatures (subglacial lakes -20, hydrothermal
  vents above 120), and below it a second axis row for icy-moon ocean
  worlds (Europa, Enceladus, Titan) marked as 'liquid water in contact with
  rock, outside the classical habitable zone'; no invented temperatures
  for the moons, use labels only."

Caption / figure id : `fig:extremophile-envelope`
Markdown source     : book/14_synthesis/synthesis.md
Material source     : material_13.txt
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/14_synthesis/figures/extremophile_envelope.avif"

# Palette: muted sage for Earth envelope, sky blue for temperate surface,
# and ocean blue for icy moons.
COLOR_ENVELOPE_BG = "#d8ede1"
COLOR_ENVELOPE_EDGE = "#2d6a4f"
COLOR_ENVELOPE_TEXT = "#153e28"

COLOR_TEMPERATE_BG = "#cfe5ff"
COLOR_TEMPERATE_EDGE = "#1f6db8"
COLOR_TEMPERATE_TEXT = "#0f3661"

COLOR_MOON_BG = "#f4f8fb"
COLOR_MOON_CARD = "#ffffff"
COLOR_MOON_BORDER = "#7baad4"
COLOR_MOON_HEADER = "#1d4f7c"
COLOR_BANNER_BG = "#dcecf8"
COLOR_BANNER_EDGE = "#2f6fa8"
COLOR_BANNER_TEXT = "#153e68"


def panel_a(ax: plt.Axes) -> None:
    """Plot the temperature envelope of Earth life on a linear axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axis for the temperature range comparison.
    """
    # Temperature axis limits: -30 to 130 deg C (material_13.txt:15)
    ax.set_xlim(-30, 130)
    ax.set_ylim(0, 1.0)
    ax.set_xticks([-20, 0, 20, 40, 60, 80, 100, 120])
    ax.set_xlabel(r"Temperature ($^\circ\mathrm{C}$)", fontsize=10)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(False)
    ax.set_title("(a) Earth life temperature envelope (schematic)", fontsize=11)

    # Full Earth life envelope: -20 to 122 deg C (material_13.txt:15)
    rect_outer = Rectangle(
        (-20, 0.38), 145, 0.28,
        facecolor=COLOR_ENVELOPE_BG, edgecolor=COLOR_ENVELOPE_EDGE,
        lw=1.2, zorder=2,
    )
    ax.add_patch(rect_outer)

    # Classical temperate surface range: 0 to 40 deg C (material_13.txt:15)
    rect_inner = Rectangle(
        (0, 0.38), 40, 0.28,
        facecolor=COLOR_TEMPERATE_BG, edgecolor=COLOR_TEMPERATE_EDGE,
        lw=1.2, zorder=3,
    )
    ax.add_patch(rect_inner)

    # Label for broad extremophile envelope inside the 40-122 span
    ax.text(
        81, 0.52, r"Earth life envelope (-20 to over 120 $^\circ\mathrm{C}$)",
        ha="center", va="center", fontsize=10,
        color=COLOR_ENVELOPE_TEXT, weight="bold", zorder=4,
        bbox=dict(facecolor=COLOR_ENVELOPE_BG, edgecolor="none", pad=1.5, alpha=0.9),
    )

    # Label for classical temperate range below bar
    ax.annotate(
        "Temperate Earth surface conditions (schematic range)",
        xy=(20, 0.38), xytext=(20, 0.15),
        ha="center", va="top", fontsize=10,
        color=COLOR_TEMPERATE_TEXT, weight="bold",
        arrowprops=dict(arrowstyle="->", color=COLOR_TEMPERATE_EDGE, lw=1.0),
        zorder=5,
        bbox=dict(facecolor="white", edgecolor="none", pad=1.5, alpha=0.9),
    )

    # Subglacial lakes at -20 deg C (synthesis.md:493, material_13.txt:15)
    ax.annotate(
        r"Subglacial lakes (-20 $^\circ\mathrm{C}$)",
        xy=(-20, 0.66), xytext=(-20, 0.84),
        ha="left", va="bottom", fontsize=10, color=COLOR_ENVELOPE_EDGE,
        arrowprops=dict(arrowstyle="->", color=COLOR_ENVELOPE_EDGE, lw=1.0),
        zorder=5,
        bbox=dict(facecolor="white", edgecolor="none", pad=1.5, alpha=0.9),
    )

    # Hydrothermal vents above 120 deg C (synthesis.md:493, material_13.txt:15)
    ax.annotate(
        r"Hydrothermal vents (above 120 $^\circ\mathrm{C}$)",
        xy=(122, 0.66), xytext=(122, 0.84),
        ha="right", va="bottom", fontsize=10, color=COLOR_ENVELOPE_EDGE,
        arrowprops=dict(arrowstyle="->", color=COLOR_ENVELOPE_EDGE, lw=1.0),
        zorder=5,
        bbox=dict(facecolor="white", edgecolor="none", pad=1.5, alpha=0.9),
    )


def panel_b(ax: plt.Axes) -> None:
    """Draw the second axis row for icy-moon ocean worlds with labels only.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axis for icy-moon astrobiology targets.
    """
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title("(b) Icy-moon ocean worlds (schematic)", fontsize=11)

    # Background card enclosing the ocean worlds panel
    bg_card = FancyBboxPatch(
        (0.02, 0.04), 0.96, 0.90,
        boxstyle="round,pad=0.01,rounding_size=0.03",
        facecolor=COLOR_MOON_BG, edgecolor="#b0cbe5", lw=1.0, zorder=1,
    )
    ax.add_patch(bg_card)

    # Three primary icy-moon targets (synthesis.md:497, material_13.txt:15)
    moons = ["Europa", "Enceladus", "Titan"]
    xs = [0.05, 0.36, 0.67]
    card_width = 0.28
    for name, x in zip(moons, xs):
        m_box = FancyBboxPatch(
            (x, 0.50), card_width, 0.38,
            boxstyle="round,pad=0.01,rounding_size=0.03",
            facecolor=COLOR_MOON_CARD, edgecolor=COLOR_MOON_BORDER,
            lw=1.0, zorder=2,
        )
        ax.add_patch(m_box)
        ax.text(
            x + card_width / 2, 0.72, name,
            ha="center", va="center", fontsize=11,
            weight="bold", color=COLOR_MOON_HEADER, zorder=3,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.0, alpha=0.9),
        )
        ax.text(
            x + card_width / 2, 0.59, "Subsurface ocean",
            ha="center", va="center", fontsize=10,
            color="#444444", zorder=3,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.0, alpha=0.9),
        )

    # Core habitability marking across all three targets (material_13.txt:15)
    banner = FancyBboxPatch(
        (0.05, 0.10), 0.90, 0.32,
        boxstyle="round,pad=0.01,rounding_size=0.03",
        facecolor=COLOR_BANNER_BG, edgecolor=COLOR_BANNER_EDGE,
        lw=1.0, zorder=2,
    )
    ax.add_patch(banner)
    ax.text(
        0.50, 0.26,
        "liquid water in contact with rock, outside the classical habitable zone",
        ha="center", va="center", fontsize=10, weight="bold",
        color=COLOR_BANNER_TEXT, zorder=3,
        bbox=dict(facecolor=COLOR_BANNER_BG, edgecolor="none", pad=1.5, alpha=0.9),
    )


def make_plot() -> Path:
    """Build the extremophile envelope figure and save to AVIF.

    Returns
    -------
    pathlib.Path
        Path to the saved figure file.
    """
    apply_style()
    fig, axes = plt.subplots(2, 1, figsize=(7.2, 4.2), height_ratios=[1.3, 0.9])
    panel_a(axes[0])
    panel_b(axes[1])
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Execute figure generation and display the output path."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()