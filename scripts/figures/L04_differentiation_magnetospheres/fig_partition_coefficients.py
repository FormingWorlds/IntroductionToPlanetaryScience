"""Generate Fig. (`fig:partitioning-pressure`).

Schematic pressure dependence of the metal-silicate partition
coefficients of Ni and Co, the two elements that anchor the
deep-magma-ocean equilibration argument:

    log10 D = a + b * P    (Eq. eq:d-parameterisation at constant T, fO2)

The lines are schematic fits chosen to reproduce the behaviour
established experimentally (Siebert et al. 2013 Science; Fischer et
al. 2015 GCA): D(Ni) and D(Co) decrease with pressure, converge
toward each other, and reach the values required by the bulk silicate
Earth (D_Ni ~ 26, D_Co ~ 24 from core/mantle mass balance with the
McDonough 2003 compositions; Fischer et al. 2015 place single-stage
equilibration at 54 +/- 5 GPa) at pressures near 40-60 GPa.

Caption / figure id : `fig:partitioning-pressure`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : Siebert2013, Rubie2015
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/"
            "siebert2013_partition_coefficients.avif")

# Schematic linear fits in log10 D vs P (constant T ~ 3500 K, fO2 ~ IW-2).
# Anchors: low-pressure D(Ni) ~ 10^4, D(Ni)/D(Co) ~ 5 at low P, and both
# elements reaching their BSE-required values at ~55 GPa.
NI = dict(a=4.0, b=-0.0472, color="#d62728", label="Ni")
CO = dict(a=3.3, b=-0.0380, color="#ff7f0e", label="Co")

# D required by core/mantle mass balance (mantle Ni 1960 ppm, Co 105 ppm,
# McDonough & Sun 1995; core Ni 5.2 wt%, Co 0.25 wt%, McDonough 2003):
# D_Ni ~ 26, D_Co ~ 24. Band spans D = 20-32.
BAND_LO, BAND_HI = np.log10(20.0), np.log10(32.0)

# Equilibration pressure window inferred from the experiments.
P_LO, P_HI = 40.0, 60.0


def make_plot() -> Path:
    apply_style()
    p = np.linspace(0.0, 75.0, 200)

    fig, ax = plt.subplots(figsize=(7.2, 5.0))

    ax.axvspan(P_LO, P_HI, color="#1f77b4", alpha=0.10, zorder=0)
    ax.axhspan(BAND_LO, BAND_HI, color="0.55", alpha=0.30, zorder=1)

    for el, p_lab, dy in ((NI, 22.0, 0.12), (CO, 22.0, -0.30)):
        d = el["a"] + el["b"] * p
        ax.plot(p, d, color=el["color"], lw=2.2, zorder=3)
        ax.annotate(el["label"], xy=(p_lab, el["a"] + el["b"] * p_lab + dy),
                    color=el["color"], fontsize=11, fontweight="bold",
                    ha="center", va="center")

    ax.annotate("$D$ required to match the\nmantle's Ni and Co content",
                xy=(4, (BAND_LO + BAND_HI) / 2), fontsize=9.5,
                color="0.25", va="center")
    ax.annotate("inferred equilibration\npressure 40–60 GPa",
                xy=(50, 3.55), fontsize=9.5, color="#1f77b4",
                ha="center", va="top")

    ax.set_xlim(0, 79)
    ax.set_ylim(0, 4.3)
    ax.set_xlabel("Pressure (GPa)")
    ax.set_ylabel(r"$\log_{10}\, D^{\mathrm{met/sil}}$")
    ax.set_title("Metal–silicate partitioning of Ni and Co vs pressure\n"
                 r"(schematic, at $T \approx 3500$ K, $f_{\mathrm{O_2}} \approx$ IW$-$2)")

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
