"""Generate Fig. 4.2 (`fig:short-lived-decay`).

Decay curves for the principal short-lived radionuclides ^26Al and
^60Fe over the first 10 Myr of solar-system history.

Half-lives are static physical constants; we record their literature
values in the data sidecar so each value is traceable.

Caption / figure id : Fig. 4.2 / `fig:short-lived-decay`
Markdown source     : book/03_heat_energy/heat_energy.md (around line 73)
Citation keys       : Lugmair2003 (^26Al t_1/2), Rugel2009 (^60Fe t_1/2)
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
META = DATA_DIR / "short_lived_radionuclides.json"
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/short_lived_decay.avif"

# Half-lives in Myr. Each value is documented (with primary reference)
# in the JSON sidecar that this script writes/refreshes.
HALF_LIVES_MYR = {
    "26Al": 0.717,    # Lugmair & Galer 2003; LA-MC-ICPMS
    "60Fe": 2.62,     # Rugel et al. 2009 PRL; AMS half-life redetermination
}

# Initial canonical solar-system isotopic ratios (relative to the stable
# reference isotope), used for the y-axis "fraction remaining" panel.
INITIAL_RATIOS = {
    "26Al": 5.25e-5,  # ^26Al/^27Al at CAI formation, MacPherson et al. 2012
    "60Fe": 1.0e-8,   # ^60Fe/^56Fe initial; Tang & Dauphas 2012, Trappitsch et al. 2018
}


def write_data() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps({
        "purpose": "Fig. 4.2 (fig:short-lived-decay): exponential decay of 26Al and 60Fe",
        "half_lives_Myr": HALF_LIVES_MYR,
        "half_life_references": {
            "26Al": {
                "value_Myr": 0.717,
                "uncertainty_Myr": 0.024,
                "reference": "Lugmair & Galer (2003)",
                "doi": "10.1016/0016-7037(94)90419-7",
            },
            "60Fe": {
                "value_Myr": 2.62,
                "uncertainty_Myr": 0.04,
                "reference": "Rugel et al. (2009)",
                "doi": "10.1103/PhysRevLett.103.072502",
            },
        },
        "initial_solar_system_ratios": INITIAL_RATIOS,
        "initial_ratio_references": {
            "26Al/27Al": "MacPherson et al. (2012); canonical CAI value 5.25e-5",
            "60Fe/56Fe": "Tang & Dauphas (2012), Trappitsch et al. (2018); ~1e-8",
        },
        "license_note": "Half-lives and isotopic ratios are public scientific data.",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    write_data()

    t = np.linspace(0, 10, 400)  # Myr
    fig, ax = plt.subplots(figsize=(7, 4.4))

    colors = {"26Al": "#d62728", "60Fe": "#1f77b4"}
    labels = {"26Al": r"$^{26}\mathrm{Al}\;(t_{1/2}=0.72\,\mathrm{Myr})$",
              "60Fe": r"$^{60}\mathrm{Fe}\;(t_{1/2}=2.62\,\mathrm{Myr})$"}
    for iso, hl in HALF_LIVES_MYR.items():
        n_over_n0 = 0.5 ** (t / hl)
        ax.plot(t, n_over_n0, color=colors[iso], lw=2.0, label=labels[iso])

    ax.axhline(0.5, color="gray", lw=0.6, linestyle=":")
    ax.set_xlabel("Time after CAI formation (Myr)")
    ax.set_ylabel(r"$N(t)/N_0$")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.02)
    ax.legend(loc="upper right", frameon=False)
    ax.grid(linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  meta : {META}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
