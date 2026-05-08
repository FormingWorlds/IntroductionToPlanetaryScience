"""Generate Fig. (`fig:xuv-evolution`).

Schematic evolution of the XUV-to-bolometric luminosity ratio
L_XUV / L_bol for G-dwarf, early-M, and late-M (TRAPPIST-1 like)
stars.

All spectral types pass through a saturated plateau at
L_XUV / L_bol ~ 10^-3, then decay as a power law. The saturation
phase lasts ~100 Myr for G-dwarfs but >= 1 Gyr for late-M stars.

Caption / figure id : `fig:xuv-evolution`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation keys       : Ribas2005 (G-dwarfs), Wordsworth2022 (M-dwarf
                      prolonged saturation discussion)

This is explicitly a schematic, not a reproduction of any single
dataset. Per-spectral-type saturation timescales and decay slopes
are representative.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/xuv_evolution.avif"

LOG_LRATIO_SAT = -3.0  # saturation plateau

# (label, t_sat_Gyr, decay_slope_alpha, color)
TRACKS = [
    ("G-dwarf (Sun-like)",         0.10, 1.20, "#e0a92a"),
    ("Early M-dwarf",              0.40, 1.10, "#b04020"),
    ("Late M-dwarf (TRAPPIST-1-like)", 1.00, 1.00, "#5c3e7c"),
]


def L_XUV_over_L_bol(t_gyr: np.ndarray, t_sat: float, alpha: float) -> np.ndarray:
    sat = 10.0 ** LOG_LRATIO_SAT
    ratio = np.where(t_gyr < t_sat,
                     sat,
                     sat * (t_gyr / t_sat) ** -alpha)
    return ratio


def make_plot() -> Path:
    apply_style()
    t = np.logspace(-2, 1, 600)

    fig, ax = plt.subplots(figsize=(8.5, 6.0))

    # Saturation regime band
    ax.axhspan(10 ** LOG_LRATIO_SAT * 0.5, 10 ** LOG_LRATIO_SAT * 2,
               color="#fce6c4", alpha=0.55, zorder=0)
    ax.text(0.012, 1.5e-3, "Saturated regime", color="#9b6818",
            fontsize=10, style="italic")

    for label, t_sat, alpha, color in TRACKS:
        ratio = L_XUV_over_L_bol(t, t_sat, alpha)
        ax.plot(t, ratio, color=color, lw=2.5, label=label)

    # Anchor markers
    # Present-day Sun: t = 4.6 Gyr, L_XUV/L_bol ~ 6e-7 (Ribas 2005)
    ax.plot(4.6, 6e-7, "o", color="#e0a92a", ms=9,
            mec="black", mew=0.5, zorder=5)
    ax.annotate("Present-day\nSun",
                xy=(4.6, 6e-7), xytext=(2.5, 1.5e-6),
                fontsize=10, color="#9b7818",
                arrowprops=dict(arrowstyle="->", color="#9b7818", lw=0.8))

    # TRAPPIST-1 today: ~7.6 Gyr, L_XUV/L_bol ~ 1e-4
    ax.plot(7.6, 1e-4, "o", color="#5c3e7c", ms=9,
            mec="black", mew=0.5, zorder=5)
    ax.annotate("TRAPPIST-1\ntoday",
                xy=(7.6, 1e-4), xytext=(4.0, 5e-5),
                fontsize=10, color="#3e2854",
                arrowprops=dict(arrowstyle="->", color="#3e2854", lw=0.8))

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-2, 1e1)
    ax.set_ylim(1e-7, 3e-3)
    ax.set_xlabel("Age (Gyr)")
    ax.set_ylabel(r"$L_{\mathrm{XUV}} / L_{\mathrm{bol}}$")
    ax.set_title("Stellar XUV luminosity evolution for low-mass stars")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="lower left", frameon=True, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
