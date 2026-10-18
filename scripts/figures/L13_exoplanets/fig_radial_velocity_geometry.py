"""Geometry of the radial velocity method.

A star and its planet orbit their common barycentre. Seen from the observer,
the star moves away (lines redshifted), across the line of sight (no shift,
the planet transits if the orbit is edge-on) and towards the observer (lines
blueshifted). The three phases are shown in the orbit, in a sketch of the
stellar absorption spectrum, and on the radial velocity curve.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/13_exoplanets/figures/radial_velocity_geometry.avif"

RED = "#c0392b"
BLUE = "#1f6db8"
GREY = "0.35"
STAR = "#f5b700"

# Orbital angle theta of the star, counter-clockwise, observer towards -y.
# The star's radial velocity (positive away from the observer) is K cos(theta).
PHASES = [
    {"label": "1", "theta": 0.0, "color": RED, "text": "moving away:\nredshift"},
    {"label": "2", "theta": np.pi / 2, "color": GREY, "text": "across the line of sight:\nno shift (transit)"},
    {"label": "3", "theta": np.pi, "color": BLUE, "text": "moving towards us:\nblueshift"},
]


def _orbit_panel(ax: plt.Axes) -> None:
    """Draw the top-down view of the star and planet orbits."""
    r_star, r_planet = 0.22, 1.0  # star orbit exaggerated for visibility
    phi = np.linspace(0, 2 * np.pi, 300)
    ax.plot(r_planet * np.cos(phi), r_planet * np.sin(phi), ls="--", lw=0.9, color="0.6")
    ax.plot(r_star * np.cos(phi), r_star * np.sin(phi), ls="--", lw=0.9, color="0.6")
    ax.plot(0, 0, marker="+", ms=9, mew=1.6, color="black")
    ax.text(0.04, -0.27, "barycentre", fontsize=9, color="0.25", ha="left", va="top")

    for ph in PHASES:
        th = ph["theta"]
        xs, ys = r_star * np.cos(th), r_star * np.sin(th)
        xp, yp = -r_planet * np.cos(th), -r_planet * np.sin(th)
        ax.add_patch(Circle((xs, ys), 0.07, facecolor=STAR, edgecolor=ph["color"], lw=1.8, zorder=4))
        ax.add_patch(Circle((xp, yp), 0.045, facecolor="#5d6d7e", edgecolor=ph["color"], lw=1.4, zorder=4))
        # Velocity arrow of the star, tangent to its orbit (counter-clockwise motion)
        vx, vy = -np.sin(th), np.cos(th)
        ax.add_patch(
            FancyArrowPatch(
                (xs + 0.08 * vx, ys + 0.08 * vy),
                (xs + 0.33 * vx, ys + 0.33 * vy),
                arrowstyle="-|>",
                mutation_scale=11,
                color=ph["color"],
                lw=1.6,
                zorder=5,
            )
        )
        # Phase number next to the star and the planet
        ox, oy = np.cos(th), np.sin(th)
        ax.text(xs + 0.17 * ox, ys + 0.17 * oy + 0.05, ph["label"], color=ph["color"], fontsize=11,
                fontweight="bold", ha="center", va="center")
        ax.text(xp - 0.16 * ox, yp - 0.16 * oy, ph["label"], color=ph["color"], fontsize=11,
                fontweight="bold", ha="center", va="center")

    ax.add_patch(FancyArrowPatch((0, -1.3), (0, -1.62), arrowstyle="-|>", mutation_scale=14, color="black", lw=1.4))
    ax.text(-0.06, -1.46, "to the observer", fontsize=9, ha="right", va="center")
    ax.text(0, 1.5, "yellow: star; grey: planet\narrows: velocity of the star\nstar orbit not to scale",
            fontsize=9, color="0.3", ha="center", va="top")
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.68, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(a) Star and planet orbit the barycentre", fontsize=10)


def _spectrum_panel(ax: plt.Axes) -> None:
    """Sketch a short stretch of the stellar spectrum at the three phases."""
    lam = np.linspace(0, 10, 1000)
    lines = [1.6, 3.3, 4.4, 6.2, 7.9]
    depths = [0.55, 0.35, 0.7, 0.45, 0.6]
    shift = {"1": 0.35, "2": 0.0, "3": -0.35}  # exaggerated Doppler shift
    for k, ph in enumerate(PHASES):
        y0 = 2.2 * (len(PHASES) - 1 - k)
        flux = np.ones_like(lam)
        for lc, d in zip(lines, depths):
            flux -= d * np.exp(-0.5 * ((lam - lc - shift[ph["label"]]) / 0.12) ** 2)
        ax.plot(lam, y0 + flux, color=ph["color"], lw=1.5)
        for lc in lines:
            ax.plot([lc, lc], [y0 + 0.2, y0 + 1.1], ls=":", lw=0.9, color="0.5")
        ax.text(-0.25, y0 + 0.6, ph["label"], color=ph["color"], fontsize=11, fontweight="bold",
                ha="right", va="center")
        ax.text(10.15, y0 + 0.55, ph["text"], color=ph["color"], fontsize=9, ha="left", va="center")
    ax.set_xlim(-0.6, 10)
    ax.set_ylim(-0.1, 2.2 * len(PHASES) - 0.9)
    ax.set_xlabel("Wavelength (dotted: rest wavelengths)", fontsize=9)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    ax.set_title("(b) Stellar absorption lines (shifts exaggerated)", fontsize=10)


CURVE_LABEL_OFFSET = {"1": (0.035, 0.25, "left"), "2": (-0.035, -0.3, "right"), "3": (0.0, 0.42, "center")}

def _curve_panel(ax: plt.Axes) -> None:
    """Plot the radial velocity curve with the three phases marked."""
    t = np.linspace(0, 1.25, 500)
    ax.plot(t, np.cos(2 * np.pi * t), color="black", lw=1.6)
    ax.axhline(0, color="0.6", ls=":", lw=0.9)
    for ph in PHASES:
        tp = ph["theta"] / (2 * np.pi)
        ax.plot(tp, np.cos(ph["theta"]), "o", ms=8, color=ph["color"], zorder=4)
        # Each label sits on the side of its marker that the curve leaves free
        dx, dy, ha = CURVE_LABEL_OFFSET[ph["label"]]
        ax.text(tp + dx, np.cos(ph["theta"]) + dy, ph["label"], color=ph["color"], fontsize=11,
                fontweight="bold", ha=ha, va="center")
    ax.add_patch(FancyArrowPatch((1.0, 0.0), (1.0, 1.0), arrowstyle="<|-|>", mutation_scale=9, color=RED, lw=1.3))
    ax.text(1.03, 0.5, r"$K_\star$", color=RED, fontsize=11, ha="left", va="center")
    ax.set_xlim(-0.03, 1.25)
    ax.set_ylim(-1.35, 1.45)
    ax.set_xlabel("Time (orbital periods)", fontsize=9)
    ax.set_ylabel(r"$v_r / K_\star$", fontsize=10)
    ax.text(1.24, -1.25, "+ away from the observer", fontsize=9, color="0.3", ha="right", va="bottom")
    ax.set_title("(c) Radial velocity of the star", fontsize=10)


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig = plt.figure(figsize=(8.6, 4.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.0, 1.25], height_ratios=[1.15, 1.0], wspace=0.05, hspace=0.45)
    _orbit_panel(fig.add_subplot(gs[:, 0]))
    _spectrum_panel(fig.add_subplot(gs[0, 1]))
    _curve_panel(fig.add_subplot(gs[1, 1]))
    save_figure(fig, OUT_AVIF, dpi=280)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
