"""Generate Fig. (`fig:outgassing-speciation`).

Two-panel figure showing the equilibrium partitioning of Earth's
volatile inventory between the magma ocean and the outgassed
atmosphere as a function of mantle oxygen fugacity. Panel (a): mass of
each volatile species dissolved in the fully molten mantle. Panel (b):
partial pressure of each species in the overlying atmosphere. Both are
computed with the CALLIOPE outgassing code for the bulk silicate Earth
H/C/N/S inventory of Krijt et al. (2023), a magma ocean at 2000 K, and
a fully molten mantle.

Requires the fwl-calliope package (https://github.com/FormingWorlds/CALLIOPE).

Caption / figure id : `fig:outgassing-speciation`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : Krijt2023, Nicholls2024, Hirschmann2012
"""
from __future__ import annotations

import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from calliope.constants import volatile_species
from calliope.solve import equilibrium_atmosphere

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/"
            "outgassing_speciation_fO2.avif")

# Bulk silicate Earth volatile inventory [kg], Krijt et al. (2023),
# Protostars and Planets VII, Tables 1 and 2.
EARTH_HCNS = {"H": 5.6e20, "C": 3.1e21, "N": 3.7e19, "S": 1.0e21}

PLANET = {"M_mantle": 4.03e24, "gravity": 9.81, "radius": 6.371e6}
T_MAGMA = 2000.0

DIW_START = 3.5
DIW_GRID = np.arange(-4.0, 4.01, 0.25)

# Starting guess that pins the CO2-dominated solution branch at the
# oxidised starting point; each subsequent solve reuses its neighbour.
CANONICAL_GUESS = {"H2O": 5.0, "CO2": 1500.0, "N2": 3.0, "S2": 1e-3}

SPECIES_COLORS = {
    "H2O": "#1f77b4",
    "H2":  "#17becf",
    "CO2": "#d62728",
    "CO":  "#ff7f0e",
    "CH4": "#8c564b",
    "N2":  "#2ca02c",
    "S2":  "#9467bd",
    "SO2": "#e377c2",
    "H2S": "#bcbd22",
}

ATM_SPECIES = ["H2O", "H2", "CO2", "CO", "CH4", "N2", "S2", "SO2", "H2S"]
MELT_SPECIES = ["H2O", "CO2", "CO", "CH4", "N2", "S2"]


def solve_at(diw: float, p_guess: dict) -> dict:
    """Solve the outgassing equilibrium at one oxygen fugacity.

    Parameters
    ----------
    diw
        Oxygen fugacity as a log10 shift relative to the iron-wustite
        buffer.
    p_guess
        Starting partial pressures [bar] for the solver, keys 'H2O',
        'CO2', 'N2', 'S2'.

    Returns
    -------
    dict
        CALLIOPE output dictionary with per-species partial pressures,
        atmosphere masses, and dissolved masses.
    """
    ddict = {**PLANET, "T_magma": T_MAGMA, "Phi_global": 1.0,
             "fO2_shift_IW": diw}
    for sp in volatile_species:
        ddict[f"{sp}_included"] = 1
        ddict[f"{sp}_initial_bar"] = 0.0
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return equilibrium_atmosphere(EARTH_HCNS, ddict, p_guess=p_guess,
                                      print_result=False)


def sweep() -> dict[float, dict]:
    """Sweep the fO2 grid by continuation from the oxidised anchor.

    Returns
    -------
    dict
        Mapping from each grid value of the IW shift to the CALLIOPE
        output dictionary at that point.
    """
    results: dict[float, dict] = {}
    anchor = solve_at(DIW_START, CANONICAL_GUESS)
    results[DIW_START] = anchor

    def guess_from(res: dict) -> dict:
        return {s: max(float(res[f"{s}_bar"]), 1e-10)
                for s in ("H2O", "CO2", "N2", "S2")}

    upward = sorted(d for d in DIW_GRID if d > DIW_START)
    downward = sorted((d for d in DIW_GRID if d < DIW_START), reverse=True)
    for branch in (upward, downward):
        prev = anchor
        for diw in branch:
            prev = solve_at(diw, guess_from(prev))
            results[diw] = prev
    return results


def make_plot() -> Path:
    apply_style()
    results = sweep()
    diws = np.array(sorted(d for d in results if d in DIW_GRID))

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(9.2, 4.0), sharex=True)

    for sp in MELT_SPECIES:
        m = np.array([results[d][f"{sp}_kg_liquid"] for d in diws])
        ax_a.plot(diws, m, color=SPECIES_COLORS[sp], lw=1.8,
                  label=sp.replace("2", "$_2$").replace("H4", "H$_4$"))
    ax_a.set_yscale("log")
    ax_a.set_ylim(1e14, 1e23)
    ax_a.set_xlabel(r"oxygen fugacity, $\Delta$IW [dex]")
    ax_a.set_ylabel("mass dissolved in magma ocean [kg]")
    ax_a.set_title("(a) dissolved in the melt", fontsize=11)
    ax_a.legend(ncol=2, loc="lower right", framealpha=0.9)

    for sp in ATM_SPECIES:
        p = np.array([results[d][f"{sp}_bar"] for d in diws])
        ax_b.plot(diws, p, color=SPECIES_COLORS[sp], lw=1.8,
                  label=sp.replace("2", "$_2$").replace("H4", "H$_4$"))
    ax_b.set_yscale("log")
    ax_b.set_ylim(1e-4, 3e3)
    ax_b.set_xlabel(r"oxygen fugacity, $\Delta$IW [dex]")
    ax_b.set_ylabel("atmospheric partial pressure [bar]")
    ax_b.set_title("(b) outgassed atmosphere", fontsize=11)
    ax_b.legend(ncol=2, loc="lower center", framealpha=0.9)

    fig.tight_layout(pad=0.5)
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
