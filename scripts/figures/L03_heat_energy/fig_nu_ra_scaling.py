"""Generate Fig. (`fig:nu-ra-scaling`).

Schematic Nusselt-Rayleigh scaling: Nu = 1 below Ra_c (pure
conduction), Nu ~ Ra^{1/3} above (boundary-layer scaling, after the
asymptotic boundary-layer theory of Howard 1966 and Malkus 1954).
The shaded band marks Earth's mantle (Ra ~ 1e7 to 1e8).

Caption / figure id : `fig:nu-ra-scaling`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : (textbook scaling; cited as Turcotte2002 in body)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/nu_ra_scaling.avif"

RA_C = 1708.0


def make_plot() -> Path:
    apply_style()
    Ra = np.logspace(2, 11, 400)

    # Conduction below Ra_c, Nu ~ Ra^(1/3) above (with the canonical
    # prefactor that gives Nu = 1 at Ra = Ra_c, i.e. continuous at the
    # bifurcation).
    Nu = np.ones_like(Ra)
    above = Ra > RA_C
    Nu[above] = (Ra[above] / RA_C) ** (1.0 / 3.0)

    fig, ax = plt.subplots(figsize=(7, 4.4))
    ax.plot(Ra, Nu, color="#1f77b4", lw=2.0,
            label=r"$\mathrm{Nu}(\mathrm{Ra})$")

    ax.axvline(RA_C, color="#d62728", lw=1.0, linestyle="--",
               label=fr"$\mathrm{{Ra}}_c = {RA_C:.0f}$")

    # Earth-mantle band
    ax.axvspan(1e7, 1e8, color="#ff7f0e", alpha=0.18,
               label=r"Earth's mantle (Ra $\sim 10^7$-$10^8$)")

    # Asymptotic slope label
    ax.annotate(r"$\mathrm{Nu} \propto \mathrm{Ra}^{1/3}$",
                xy=(3e9, (3e9 / RA_C) ** (1.0 / 3.0)),
                xytext=(0, 15), textcoords="offset points",
                fontsize=11, color="#1f77b4", ha="center")
    
    # Conduction label
    ax.annotate(r"$\mathrm{Nu} = 1$ (conduction)",
                xy=(3e2, 1.0),
                xytext=(0, 15), textcoords="offset points",
                fontsize=10, color="#1f77b4", ha="center")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e2, 1e11)
    ax.set_ylim(0.5, 1e3)
    ax.set_xlabel("Rayleigh number $\\mathrm{Ra}$")
    ax.set_ylabel("Nusselt number $\\mathrm{Nu}$")
    ax.set_title("Heat-transport efficiency: $\\mathrm{Nu}$ vs $\\mathrm{Ra}$")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="lower right", frameon=False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
