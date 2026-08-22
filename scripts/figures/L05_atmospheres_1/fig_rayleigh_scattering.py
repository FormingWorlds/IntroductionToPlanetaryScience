"""Generate Fig. (`fig:rayleigh-scattering`).

Two-panel schematic of Rayleigh scattering and sky colour:
(a) geometry sketch of the short noon path versus the long horizon
path through the atmosphere, with blue light scattered out of the
beam along the way, and (b) the relative Rayleigh cross-section
sigma proportional to lambda^-4 across the visible band, with the
blue-to-red scattering ratio annotated.

Caption / figure id : `fig:rayleigh-scattering`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md

The atmosphere shell in panel (a) is drawn thick for clarity; the
real shell is ~0.1% of Earth's radius, so the horizon slant path is
roughly 40 times the vertical path rather than the 3.5 shown.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/rayleigh_scattering.avif"

# Panel (a) geometry: observer at the origin, Earth centre below it
R_EARTH = 1.0
H_ATM = 0.18
CENTER = (0.0, -R_EARTH)

BLUE = "#1f6db8"
EARTH_FILL = "#c2cdd8"
SKY_FILL = "#cfe5ff"
SUN_NOON = "#f5c518"
SUN_SET = "#e8641b"


def wavelength_to_rgb(lam_nm: float) -> tuple[float, float, float]:
    """Return an approximate sRGB colour for a visible wavelength in nm."""
    lam = float(lam_nm)
    if lam < 440:
        r, g, b = -(lam - 440) / 60, 0.0, 1.0
    elif lam < 490:
        r, g, b = 0.0, (lam - 440) / 50, 1.0
    elif lam < 510:
        r, g, b = 0.0, 1.0, -(lam - 510) / 20
    elif lam < 580:
        r, g, b = (lam - 510) / 70, 1.0, 0.0
    elif lam < 645:
        r, g, b = 1.0, -(lam - 645) / 65, 0.0
    else:
        r, g, b = 1.0, 0.0, 0.0
    # Fade toward the band edges so the extremes are not oversaturated
    if lam < 420:
        fade = 0.3 + 0.7 * (lam - 380) / 40
    elif lam > 700:
        fade = 0.3 + 0.7 * (750 - lam) / 50
    else:
        fade = 1.0
    return tuple(np.clip(fade * np.array([r, g, b]), 0, 1))


def _scatter_arrows(ax, x0: float, y0: float, angles_deg, length: float = 0.085) -> None:
    """Draw short blue arrows leaving a scattering point on the beam."""
    for a in angles_deg:
        dx = length * np.cos(np.radians(a))
        dy = length * np.sin(np.radians(a))
        ax.add_patch(FancyArrowPatch(
            (x0, y0), (x0 + dx, y0 + dy),
            arrowstyle="->", mutation_scale=8, color=BLUE, lw=1.2))


def panel_a(ax) -> None:
    # Atmosphere annulus: outer sky-blue disc with the Earth disc on top
    # No stroked edges: the fill contrast draws the surface and shell arcs
    ax.add_patch(Circle(CENTER, R_EARTH + H_ATM, facecolor=SKY_FILL,
                        edgecolor="none", alpha=0.8, zorder=1))
    ax.add_patch(Circle(CENTER, R_EARTH, facecolor=EARTH_FILL,
                        edgecolor="none", zorder=2))

    # Horizon ray enters the shell where the observer's tangent line meets it
    x_entry = -np.sqrt((R_EARTH + H_ATM) ** 2 - R_EARTH**2)

    # Noon beam: vertical, short in-shell segment, stays pale yellow
    ax.plot([0, 0], [0.42, H_ATM], color=SUN_NOON, lw=2.6,
            solid_capstyle="round", zorder=3)
    ax.plot([0, 0], [H_ATM, 0.012], color=SUN_NOON, lw=2.6,
            solid_capstyle="round", zorder=3)
    _scatter_arrows(ax, 0.0, 0.13, (160, 205))
    _scatter_arrows(ax, 0.0, 0.065, (25, -20))

    # Sunset beam: long in-shell segment, reddening toward the observer
    ax.plot([-1.02, x_entry], [0, 0], color=SUN_NOON, lw=2.6,
            solid_capstyle="round", zorder=3)
    n_seg = 60
    xs = np.linspace(x_entry, -0.012, n_seg + 1)
    frac = np.linspace(0, 1, n_seg)
    seg_colors = [(1.0, 0.78 - 0.62 * f, 0.10 + 0.05 * f) for f in frac]
    segs = [[(xs[i], 0), (xs[i + 1], 0)] for i in range(n_seg)]
    ax.add_collection(LineCollection(segs, colors=seg_colors, lw=2.6,
                                     capstyle="round", zorder=3))
    for xp in (-0.52, -0.37, -0.22):
        _scatter_arrows(ax, xp, 0.0, (70, 115))

    # Blue light scattered elsewhere in the shell also reaches the eye
    ax.add_patch(FancyArrowPatch(
        (0.36, 0.09), (0.03, 0.012),
        arrowstyle="->", mutation_scale=9, color=BLUE, lw=1.2, zorder=3))

    # Suns and observer
    ax.add_patch(Circle((0, 0.46), 0.045, facecolor=SUN_NOON,
                        edgecolor="none", zorder=4))
    ax.add_patch(Circle((-1.06, 0), 0.045, facecolor=SUN_SET,
                        edgecolor="none", zorder=4))
    ax.plot(0, 0.005, marker="o", ms=5, color="black", zorder=5)

    ax.text(0.05, 0.44, "noon: short path,\nless blue removed",
            fontsize=9, ha="left", va="center")
    ax.text(-0.62, -0.075, "sunset: long path, blue scattered out,\n"
            "transmitted light reddened",
            fontsize=9, ha="center", va="top", zorder=6)
    ax.text(0.45, 0.16, "scattered blue\nfrom the whole sky",
            fontsize=9, ha="left", va="bottom", color=BLUE)
    ax.text(0.02, -0.045, "observer", fontsize=9, ha="left", va="top",
            zorder=6)
    ax.annotate("atmosphere\n(thickness exaggerated)",
                xy=(-0.50, 0.03), xytext=(-1.05, 0.24),
                fontsize=9, ha="left", va="center", color="0.35",
                arrowprops=dict(arrowstyle="-", color="0.6", lw=0.6))

    ax.set_xlim(-1.14, 1.05)
    ax.set_ylim(-0.16, 0.52)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(a) Two paths through the atmosphere", fontsize=11)


def panel_b(ax) -> None:
    lam = np.linspace(380, 750, 400)
    sigma = (550.0 / lam) ** 4

    # Colour the curve by the wavelength it represents
    pts = np.column_stack([lam, sigma]).reshape(-1, 1, 2)
    segs = np.concatenate([pts[:-1], pts[1:]], axis=1)
    colors = [wavelength_to_rgb(l) for l in lam[:-1]]
    ax.add_collection(LineCollection(segs, colors=colors, lw=3.0))

    # Marker labels sit in the empty regions beside the curve
    for lam_mark, xt, yt in ((450.0, 415.0, 1.55), (650.0, 668.0, 1.05)):
        s = (550.0 / lam_mark) ** 4
        ax.plot(lam_mark, s, "o", color="black", ms=5, zorder=4)
        ax.annotate(f"{lam_mark:.0f} nm", xy=(lam_mark, s),
                    xytext=(xt, yt), fontsize=9, ha="center",
                    arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    ratio = (650.0 / 450.0) ** 4
    ax.text(590, 2.9, "blue (450 nm) is scattered\n"
            rf"$\approx {ratio:.1f}\times$ more than red (650 nm)",
            fontsize=10, ha="center", va="center")

    ax.set_xlim(380, 750)
    ax.set_ylim(0, 4.7)
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel(r"Rayleigh cross-section $\sigma/\sigma(550\ \mathrm{nm})$")
    ax.set_title(r"(b) Scattering strength $\propto \lambda^{-4}$",
                 fontsize=11)
    ax.grid(linestyle=":", alpha=0.3)


def make_plot() -> Path:
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
    panel_a(axes[0])
    panel_b(axes[1])
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
