"""Generate Fig. (`fig:radiogenic-heat`).

Specific radiogenic heating rate of planetary material from CAI formation
to the present, on log-log axes, for both isotope families:

- short-lived ``26Al`` and ``60Fe`` in primitive chondritic rock (the
  material of early planetesimals), from their canonical initial
  abundances;
- the four long-lived isotopes in bulk-silicate-Earth rock, from the same
  parameters the lecture tabulates (heat production per kg of isotope, BSE
  concentration, half-life).

The heat production per kilogram of each short-lived isotope is computed
from its decay energy and half-life rather than copied, so the curve is
reproducible from the printed physics.

Caption / figure id : `fig:radiogenic-heat`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation keys       : Lichtenberg2023, Jaupart2015, CastilloRogez2009, Rugel2009
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
META = DATA_DIR / "radiogenic_heat_evolution.json"
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/radiogenic_heat_evolution.avif"

M_BSE = 4.0e24  # kg, bulk silicate Earth
AGE_MYR = 4500.0  # Myr since formation, matching the lecture text
MEV = 1.602176634e-13  # J per MeV
AMU = 1.66053907e-27  # kg
MYR = 3.156e13  # s

# Long-lived: (label, W/kg of isotope, BSE concentration kg/kg, half-life Myr,
# colour) -- identical to the lecture table.
LONG_LIVED = [
    (r"$^{238}$U", 9.5e-5, 20e-9, 4470.0, "#d62728"),
    (r"$^{235}$U", 5.7e-4, 0.14e-9, 704.0, "#2ca02c"),
    (r"$^{232}$Th", 2.6e-5, 80e-9, 14000.0, "#7f7f7f"),
    (r"$^{40}$K", 2.9e-5, 28e-9, 1250.0, "#1f77b4"),
]

# Short-lived, chondritic reservoir: (label, mass number, effective decay
# energy MeV, half-life Myr, initial isotope ratio (atomic), stable-partner
# mass fraction in chondritic rock, partner mass number, colour).
# 26Al/27Al and 60Fe/56Fe initial ratios and elemental abundances as
# tabulated in Lichtenberg et al. (2023); half-lives from Castillo-Rogez
# et al. (2009) and Rugel et al. (2009).
SHORT_LIVED = [
    (r"$^{26}$Al", 26, 3.12, 0.72, 5.25e-5, 8.65e-3, 27, "#ff7f0e"),
    (r"$^{60}$Fe", 60, 2.712, 2.62, 1.0e-8, 0.167, 56, "#8c564b"),
]

# Collision-free label positions (axes-fraction coordinates), frozen from a
# placement run over the rendered ink-occupancy map (residual overlap <= 1.3%).
LABELS = {
    r"$^{238}$U": (0.014, 0.225),
    r"$^{232}$Th": (0.014, 0.166),
    r"$^{40}$K": (0.914, 0.121),
    r"$^{235}$U": (0.943, 0.062),
    "long-lived total": (0.789, 0.406),
    r"$^{26}$Al": (0.412, 0.506),
    r"$^{60}$Fe": (0.540, 0.103),
}

# Leader lines for the labels that sit away from their curve, drawn from the
# label's anchor-facing edge to the curve (axes-fraction coordinates).
LEADERS = [
    ((0.010, 0.262), (0.004, 0.300)),   # 238U label -> curve start
    ((0.010, 0.203), (0.004, 0.282)),   # 232Th label -> curve start
    ((0.952, 0.150), (0.996, 0.220)),   # 40K label -> curve end
]


def short_lived_H(mass_number: int, e_mev: float, t12_myr: float) -> float:
    """Heat production in W per kg of the pure isotope."""
    lam = math.log(2.0) / (t12_myr * MYR)
    n_per_kg = 1.0 / (mass_number * AMU)
    return lam * n_per_kg * e_mev * MEV


def curves():
    t = np.logspace(math.log10(0.1), math.log10(AGE_MYR), 600)  # Myr since CAI
    out = []
    total_ll = np.zeros_like(t)
    for lab, h, c, t12, colour in LONG_LIVED:
        q = h * c * 2.0 ** ((AGE_MYR - t) / t12)
        total_ll += q
        out.append((lab, q, colour, "-", 1.6))
    out.append(("long-lived total", total_ll, "black", "-", 2.4))
    for lab, A, e_mev, t12, ratio, partner_frac, A_partner, colour in SHORT_LIVED:
        h_iso = short_lived_H(A, e_mev, t12)
        c0 = partner_frac * ratio * (A / A_partner)
        q = h_iso * c0 * 2.0 ** (-t / t12)
        out.append((lab, q, colour, "--", 1.8))
    return t, out


def write_metadata(t, series) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ll = {lab: q for lab, q, *_ in series}
    total = ll["long-lived total"]
    META.write_text(json.dumps({
        "purpose": "Fig. fig:radiogenic-heat: specific radiogenic heating vs time, both isotope families",
        "reservoirs": {
            "long_lived": "bulk silicate Earth, concentrations as in the lecture table",
            "short_lived": "primitive chondritic rock (Al 0.865 wt%, 56Fe 16.7 wt%)",
        },
        "initial_ratios": {"26Al/27Al": 5.25e-5, "60Fe/56Fe": 1.0e-8},
        "H_W_per_kg_isotope": {
            "26Al": round(short_lived_H(26, 3.12, 0.72), 4),
            "60Fe": round(short_lived_H(60, 2.712, 2.62), 5),
        },
        "long_lived_total_now_W_per_kg": float(total[-1]),
        "long_lived_total_now_TW_BSE": round(float(total[-1]) * M_BSE / 1e12, 2),
        "long_lived_total_start_TW_BSE": round(float(total[0]) * M_BSE / 1e12, 2),
        "ratio_start_to_now": round(float(total[0] / total[-1]), 2),
        "sources": "Isotope table as in the lecture (after Jaupart et al. 2015; Turcotte & Schubert 2002); short-lived parameters after Lichtenberg et al. (2023); half-lives Castillo-Rogez et al. (2009), Rugel et al. (2009)",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    t, series = curves()
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    for lab, q, colour, ls, lw in series:
        ax.loglog(t, q, color=colour, ls=ls, lw=lw)
        x_ax, y_ax = LABELS[lab]
        ax.text(x_ax, y_ax, lab, transform=ax.transAxes, fontsize=9,
                color=colour if lab != "long-lived total" else "black")
    for (x1, y1), (x2, y2) in LEADERS:
        ax.plot([x1, x2], [y1, y2], transform=ax.transAxes,
                color="0.6", lw=0.6, clip_on=False)
    write_metadata(t, series)

    ax.set_xlim(0.1, AGE_MYR)
    ax.set_ylim(1e-14, 3e-6)
    ax.set_xlabel("Time after CAI formation (Myr)")
    ax.set_ylabel(r"Specific heating rate (W kg$^{-1}$ of rock)")
    ax.axvline(AGE_MYR, color="0.75", lw=0.8)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  meta : {META}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
