"""Fourier's law and the thermal conductivity of planetary materials.

Left: a slab with a linear temperature profile and the conductive heat
flux q = -k dT/dz. Right: thermal conductivities of the materials the
lecture tabulates, on a logarithmic axis.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/fourier_conductivity.avif"

# material, k in W/m/K (range as low, high), from the lecture table
MATERIALS = [
    ("Air", 0.025, 0.025),
    ("Water ice", 2.2, 2.2),
    ("Silicate rock\n(upper mantle)", 3.0, 5.0),
    ("Bridgmanite\n(lower mantle)", 5.0, 10.0),
    ("Iron (solid)", 80.0, 80.0),
]


def make_plot() -> plt.Figure:
    """Build the two-panel figure, save it and return it."""
    apply_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.0), gridspec_kw={"width_ratios": [1.0, 1.1]})
    z = np.linspace(0, 1, 100)
    grad = (1 - z).reshape(-1, 1)
    ax1.imshow(grad, extent=(0.0, 1.0, 0.0, 1.0), cmap="coolwarm", aspect="auto", origin="lower", alpha=0.85)
    ax1.set_xlim(-0.05, 1.9)
    ax1.set_ylim(-0.15, 1.15)
    ax1.axis("off")
    ax1.text(0.5, 1.06, r"cold surface $T_s$", ha="center", va="bottom", fontsize=10, color="#2b8cbe")
    ax1.text(0.5, -0.06, r"hot interior $T_i$", ha="center", va="top", fontsize=10, color="#d7301f")
    ax1.add_patch(FancyArrowPatch((1.15, 0.2), (1.15, 0.8), arrowstyle="-|>", mutation_scale=16, color="0.1", lw=2.2))
    ax1.text(1.25, 0.5, r"$q = -k\,\dfrac{\mathrm{d}T}{\mathrm{d}z}$", ha="left", va="center", fontsize=12)
    ax1.text(1.25, 0.25, "heat flows down\nthe gradient", ha="left", va="center", fontsize=10, color="0.3")
    ax1.set_title("(a) Fourier's law in a slab", fontsize=11)
    names = [m[0] for m in MATERIALS]
    lo = np.array([m[1] for m in MATERIALS])
    hi = np.array([m[2] for m in MATERIALS])
    y = np.arange(len(names))
    ax2.barh(y, hi - lo * 0.999, left=lo, color="#7fb3d5", edgecolor="0.2", height=0.55)
    for yi, l, h in zip(y, lo, hi):
        ax2.plot([l, h], [yi, yi], color="#1f4e79", lw=6, solid_capstyle="butt")
        label = f"{l:g}" if l == h else f"{l:g} to {h:g}"
        ax2.text(h * 1.35, yi, label, va="center", fontsize=10)
    ax2.set_xscale("log")
    ax2.set_xlim(0.01, 500)
    ax2.set_yticks(y)
    ax2.set_yticklabels(names, fontsize=10)
    ax2.set_xlabel(r"Thermal conductivity $k$ (W m$^{-1}$ K$^{-1}$)")
    ax2.set_title("(b) Conductivity of planetary materials", fontsize=11)
    ax2.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
