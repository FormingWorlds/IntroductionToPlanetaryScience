"""Generate Fig. (`fig:laplace-resonance`).

Two-panel schematic of the Galilean Laplace resonance:
(a) Circular orbits of Io, Europa, Ganymede around Jupiter to scale,
    with a labelled "conjunction line".
(b) Bar chart of orbital periods, normalised to Io's, showing the
    1 : 2 : 4 commensurability.

Orbital data: JPL Solar System Dynamics (Galilean moon pages);
periods: 1.769138, 3.551181, 7.154553 days.

Caption / figure id : `fig:laplace-resonance`
Markdown source     : book/02_formation_orbits/formation_orbits.md
Citation key        : NASAFactSheet
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
META = DATA_DIR / "galilean_moons.json"
OUT_AVIF = REPO_ROOT / "book/02_formation_orbits/figures/laplace_resonance.avif"
# The same figure also appears in L03 (heat_energy.md) as fig:laplace-resonance-tidal,
# so we mirror the AVIF there to keep the two lectures' figure trees self-contained.
OUT_AVIF_MIRROR = REPO_ROOT / "book/03_heat_energy/figures/laplace_resonance.avif"

# Galilean moons: semi-major axis (10^3 km), orbital period (days), color.
MOONS = {
    "Io":       {"a_kkm": 421.800,  "P_days": 1.769138, "color": "#d62728"},
    "Europa":   {"a_kkm": 671.100,  "P_days": 3.551181, "color": "#1f77b4"},
    "Ganymede": {"a_kkm": 1070.400, "P_days": 7.154553, "color": "#2ca02c"},
}


def write_metadata() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps({
        "purpose": "Fig. fig:laplace-resonance: Galilean orbits + period commensurability",
        "source": "NASA / JPL planetary fact sheets",
        "source_url": "https://nssdc.gsfc.nasa.gov/planetary/factsheet/joviansatfact.html",
        "retrieved_date": "2026-04-23",
        "citation_key": "NASAFactSheet",
        "moons": MOONS,
        "license_note": "NASA fact-sheet content is public domain.",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    write_metadata()

    fig, (ax_orbits, ax_periods) = plt.subplots(1, 2, figsize=(10, 4.5))

    # Panel (a): orbits
    theta = np.linspace(0, 2 * np.pi, 360)
    for name, p in MOONS.items():
        a = p["a_kkm"]
        ax_orbits.plot(a * np.cos(theta), a * np.sin(theta),
                       color=p["color"], lw=1.5, label=name)
        # Conjunction-snapshot point at theta=0
        ax_orbits.plot(a, 0, "o", color=p["color"],
                       markeredgecolor="black", markersize=8, zorder=5)

    # Jupiter at origin (visually exaggerated for legibility)
    ax_orbits.plot(0, 0, "o", color="orange", markersize=22,
                   markeredgecolor="brown", label="Jupiter")

    # Conjunction line annotation
    ax_max = MOONS["Ganymede"]["a_kkm"] * 1.1
    ax_orbits.annotate("conjunction\nline",
                       xy=(MOONS["Ganymede"]["a_kkm"], 0),
                       xytext=(MOONS["Ganymede"]["a_kkm"] * 1.05, 200),
                       fontsize=9, color="dimgray",
                       arrowprops=dict(arrowstyle="-", color="dimgray", lw=0.7))

    ax_orbits.set_aspect("equal")
    ax_orbits.set_xlim(-ax_max, ax_max * 1.4)
    ax_orbits.set_ylim(-ax_max, ax_max)
    ax_orbits.set_xlabel(r"$x$ ($10^3$ km)")
    ax_orbits.set_ylabel(r"$y$ ($10^3$ km)")
    ax_orbits.set_title("(a) Galilean satellite orbits")
    ax_orbits.legend(loc="lower left", frameon=False, fontsize=9)
    ax_orbits.grid(linestyle=":", alpha=0.3)

    # Panel (b): period commensurability
    P_io = MOONS["Io"]["P_days"]
    names = list(MOONS.keys())
    periods_norm = [MOONS[n]["P_days"] / P_io for n in names]
    colors = [MOONS[n]["color"] for n in names]

    y_pos = np.arange(len(names))
    ax_periods.barh(y_pos, periods_norm, color=colors, alpha=0.85,
                    edgecolor="black", linewidth=0.6)
    for i, (n, ratio) in enumerate(zip(names, periods_norm)):
        Pd = MOONS[n]["P_days"]
        ratio_label = f"{Pd:.3f} d  ($\\approx {round(ratio)}P_{{Io}}$)" if i > 0 \
            else f"{Pd:.3f} d  ($= 1P_{{Io}}$)"
        ax_periods.text(ratio + 0.08, i, ratio_label,
                        va="center", fontsize=9)

    ax_periods.set_yticks(y_pos)
    ax_periods.set_yticklabels(names, fontsize=10)
    ax_periods.invert_yaxis()
    ax_periods.set_xlabel("Orbital period / Io's orbital period")
    ax_periods.set_xlim(0, 5.5)
    ax_periods.set_title("(b) Period commensurability 1 : 2 : 4")
    ax_periods.grid(axis="x", linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    import shutil
    out = make_plot()
    OUT_AVIF_MIRROR.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(out, OUT_AVIF_MIRROR)
    print(f"  meta : {META}")
    print(f"  plot : {out}")
    print(f"  mirror: {OUT_AVIF_MIRROR}")


if __name__ == "__main__":
    main()
