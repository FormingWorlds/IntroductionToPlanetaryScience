"""Generate Fig. (`fig:tau-one`).

Two-panel schematic of the atmospheric "photosphere" concept:
(a) Beer-Lambert attenuation I/I_0 = exp(-tau) with the tau=1
emission level marked at I/I_0 = 1/e, and (b) cartoon of an
atmosphere where photons emitted from tau<~1 escape but those from
deeper are reabsorbed.

Caption / figure id : `fig:tau-one`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/tau_one_schematic.avif"

RED = "#b22222"
BLUE = "#1f6db8"
SKY = "#cfe5ff"
DARK = "#3a3a3a"


def panel_a(ax) -> None:
    tau = np.linspace(0, 5, 400)
    I = np.exp(-tau)
    ax.plot(tau, I, color=RED, lw=2.0)
    ax.fill_between(tau, 0, I, color=RED, alpha=0.10)

    ax.axvline(1, color="0.4", linestyle="--", lw=0.9)
    ax.axhline(np.exp(-1), color="0.4", linestyle=":", lw=0.9)
    ax.plot(1, np.exp(-1), "o", color="black", ms=6)
    ax.annotate(r"$\tau=1$, $I/I_0 = 1/e \approx 0.37$",
                xy=(1, np.exp(-1)), xytext=(1.7, 0.5),
                fontsize=10,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1.0)
    ax.set_xlabel(r"Optical depth $\tau$")
    ax.set_ylabel(r"Transmitted intensity $I/I_0$")
    ax.set_title("(a) Beer-Lambert attenuation", fontsize=11)
    ax.grid(linestyle=":", alpha=0.3)


def panel_b(ax) -> None:
    # Vertical schematic: surface bottom, atmosphere, space top
    ax.add_patch(Rectangle((0, 0.0), 1.0, 0.18, color="#cdd9e6"))
    ax.add_patch(Rectangle((0, 0.18), 1.0, 0.62, color=SKY, alpha=0.7))
    ax.add_patch(Rectangle((0, 0.80), 1.0, 0.20, color=DARK))

    # Tau=1 emission level (dashed)
    ax.plot([0.0, 1.0], [0.55, 0.55], "k--", lw=1.0)
    ax.text(0.02, 0.56, r"$\tau \approx 1$ emission level",
            fontsize=10, va="bottom")

    # Surface label
    ax.text(0.5, 0.07, "Surface", color="black", fontsize=11,
            ha="center", weight="bold")
    # Space label (placed inside the dark band, well above arrow tips)
    ax.text(0.5, 0.92, "Space", color="white", fontsize=12,
            ha="center", weight="bold")

    # Photons from tau<1 escape (red arrows above tau=1 line, stop at
    # space band); rightmost arrow stays left of the escape label box
    for x_ in (0.46, 0.57, 0.68):
        ax.add_patch(FancyArrowPatch(
            (x_, 0.55), (x_, 0.78),
            arrowstyle="->", mutation_scale=12, color=RED, lw=1.4))
    ax.text(0.97, 0.68, "photons from\n" + r"$\tau \lesssim 1$"
            "\nescape to space",
            fontsize=9, ha="right", va="center", color=RED,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5,
                      alpha=0.85))

    # Deep IR photons reabsorbed: the upward path ends at an absorption
    # point (dot) below tau=1; short stubs radiating from the dot show
    # isotropic re-emission, with every tip staying below the tau=1 line
    for x_ in (0.24, 0.38):
        ax.plot([x_, x_], [0.18, 0.47], color=RED, lw=1.4,
                solid_capstyle="round")
        ax.plot(x_, 0.47, "o", ms=5, color=RED)
        for dx, dy in ((-0.045, 0.045), (0.045, 0.045), (0.0, -0.065)):
            ax.add_patch(FancyArrowPatch(
                (x_, 0.47), (x_ + dx, 0.47 + dy),
                arrowstyle="->", mutation_scale=9, color=RED, lw=1.1))
    ax.text(0.05, 0.36, "deep IR\nphotons\nreabsorbed",
            fontsize=9, ha="left", va="center", color=RED)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(b) The atmospheric photosphere", fontsize=11)


def make_plot() -> Path:
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    panel_a(axes[0])
    panel_b(axes[1])
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
