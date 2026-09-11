"""Space weathering of a regolith grain and its spectral signature.

Panel (a) is a schematic cross-section of a regolith grain with an
amorphous rim that holds nanophase iron, bombarded by solar wind ions,
micrometeorites and cosmic rays. Panel (b) shows qualitative reflectance
spectra of a fresh and a mature surface: the mature surface is darker,
redder and has a shallower 1 micrometre band. No reflectance values are
implied.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/07_surfaces/figures/space_weathering.avif"

HOST = "#ece7dd"
RIM = "#c2b49e"
EDGE = "#524638"
WIND = "#1f6db8"
METEOR = "#3a3a3a"
SPLASH = "#c44018"
COSMIC = "#7b3294"
FRESH = "#1f6db8"
MATURE = "#b22222"


def _top(x: np.ndarray) -> np.ndarray:
    """Return the height of the grain surface at position x."""
    return 3.6 - 0.02 * (x - 5.0) ** 2 - 0.55 * np.exp(-((x - 7.3) / 0.5) ** 2)


def panel_a(ax: plt.Axes) -> None:
    """Draw the weathered grain cross-section with its three agents."""
    ax.set_xlim(0.0, 10.0)
    ax.set_ylim(0.0, 8.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(a) Regolith grain cross-section (schematic)", fontsize=11)
    x = np.linspace(0.5, 9.5, 200)
    y_top = _top(x)
    y_rim = y_top + 0.85
    host = np.vstack([np.column_stack([x, y_top]), [[9.5, 0.5], [0.5, 0.5]]])
    rim = np.vstack([np.column_stack([x, y_rim]), np.column_stack([x[::-1], y_top[::-1]])])
    ax.add_patch(Polygon(host, closed=True, facecolor=HOST, edgecolor=EDGE, lw=1.2, zorder=1))
    ax.add_patch(Polygon(rim, closed=True, facecolor=RIM, edgecolor=EDGE, lw=1.2, zorder=2))
    rng = np.random.default_rng(7)
    for bx in np.linspace(0.9, 9.2, 22):
        by = float(_top(np.array([bx]))[0]) + 0.2 + 0.5 * rng.random()
        ax.add_patch(Circle((bx, by), 0.06 + 0.06 * rng.random(), facecolor="#1a1a1a",
                            edgecolor="none", zorder=3))
    # Solar wind ions implanted into the rim
    for sx in (2.6, 3.4, 4.2):
        ax.add_patch(FancyArrowPatch((sx - 0.3, 6.9), (sx, float(_top(np.array([sx]))[0]) + 0.95),
                                     arrowstyle="-|>", mutation_scale=11, color=WIND, lw=1.4, zorder=5))
    ax.text(3.6, 7.1, "solar wind ions\n" + r"($\mathrm{H^+}$, $\mathrm{He^{2+}}$)", ha="center",
            va="bottom", fontsize=10, color=WIND)
    # Micrometeorite impact with melt splash
    ax.add_patch(FancyArrowPatch((8.6, 6.9), (7.35, 4.15), arrowstyle="-|>", mutation_scale=12,
                                 color=METEOR, lw=1.4, ls="--", zorder=5))
    ax.text(8.4, 7.1, "micrometeorite\n" + r"(10 to 70 km s$^{-1}$)", ha="center", va="bottom",
            fontsize=10, color=METEOR)
    for dx, dy in ((6.6, 5.2), (6.9, 5.7), (7.5, 5.8), (7.9, 5.3), (7.1, 4.9)):
        ax.plot([7.3, dx], [4.05, dy], color=SPLASH, lw=1.0, ls=":", zorder=4)
        ax.add_patch(Circle((dx, dy), 0.07, facecolor=SPLASH, edgecolor="none", zorder=5))
    ax.text(6.55, 5.7, "melt splash\nand vapour", ha="right", va="center", fontsize=10, color=SPLASH)
    # Cosmic ray track through the rim into the host grain
    ax.add_patch(FancyArrowPatch((1.0, 6.9), (1.0, 2.8), arrowstyle="-|>", mutation_scale=10,
                                 color=COSMIC, lw=1.2, ls="-.", zorder=5))
    ax.text(1.0, 7.1, "cosmic\nrays", ha="center", va="bottom", fontsize=10, color=COSMIC)
    # Callouts for the rim and the nanophase iron
    ax.annotate("amorphous rim\n(top ~100 nm)", xy=(1.6, float(_top(np.array([1.6]))[0]) + 0.3),
                xytext=(0.75, 2.4), ha="left", va="center", fontsize=10, color=EDGE,
                arrowprops=dict(arrowstyle="->", color=EDGE, lw=0.9))
    ax.annotate("nanophase iron\nblobs (few to\nseveral hundred nm)", xy=(8.9, float(_top(np.array([8.9]))[0]) + 0.4),
                xytext=(7.0, 1.35), ha="center", va="center", fontsize=10, color="#1a1a1a",
                arrowprops=dict(arrowstyle="->", color="#1a1a1a", lw=0.9))
    ax.text(2.9, 1.4, "crystalline host grain", ha="center", va="center", fontsize=10, color=EDGE)


def panel_b(ax: plt.Axes) -> None:
    """Draw qualitative reflectance spectra of fresh and mature surfaces."""
    lam = np.linspace(0.4, 2.5, 300)
    band = np.exp(-((lam - 1.0) / 0.15) ** 2)
    fresh = 0.58 + 0.02 * (lam - 0.4) - 0.16 * band - 0.05 * np.exp(-((lam - 2.0) / 0.2) ** 2)
    mature = 0.27 + 0.055 * (lam - 0.4) - 0.05 * band
    ax.plot(lam, fresh, color=FRESH, lw=2.2, label="fresh surface")
    ax.plot(lam, mature, color=MATURE, lw=2.2, label="mature, space-weathered surface")
    ax.legend(loc="upper right", fontsize=10, framealpha=0.95)
    ax.add_patch(FancyArrowPatch((1.6, float(np.interp(1.6, lam, fresh)) - 0.02),
                                 (1.6, float(np.interp(1.6, lam, mature)) + 0.02),
                                 arrowstyle="-|>", mutation_scale=11, color="0.3", lw=1.2))
    ax.text(1.66, 0.46, "darkening\n(lower albedo)", ha="left", va="center", fontsize=10, color="0.3")
    ax.annotate(r"1 $\mu$m band shallower", xy=(1.0, float(np.interp(1.0, lam, mature)) - 0.01),
                xytext=(0.95, 0.12), ha="left", va="center", fontsize=10, color=MATURE,
                arrowprops=dict(arrowstyle="->", color=MATURE, lw=0.9))
    ax.text(2.1, 0.255, "reddening\n(steeper slope)", ha="center", va="center", fontsize=10, color=MATURE)
    ax.annotate("deep band", xy=(0.97, 0.44), xytext=(0.5, 0.36), ha="left", va="center", fontsize=10,
                color=FRESH, arrowprops=dict(arrowstyle="->", color=FRESH, lw=0.9))
    ax.set_xlim(0.4, 2.5)
    ax.set_ylim(0.05, 0.78)
    ax.set_yticks([])
    ax.set_xlabel(r"Wavelength ($\mu$m)")
    ax.set_ylabel("Reflectance (qualitative)")
    ax.set_title("(b) Reflectance spectra (schematic)", fontsize=11)


def make_plot() -> plt.Figure:
    """Build the two-panel figure, save it and return it."""
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.0), gridspec_kw={"width_ratios": [1.15, 1.0]})
    panel_a(axes[0])
    panel_b(axes[1])
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.14, wspace=0.12)
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
