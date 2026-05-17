"""Generate Fig. 2.18 (`fig:ss-mass-budget`).

Mass budget of the solar system: a two-panel pie chart.
- Left panel: Sun vs total planetary mass.
- Right panel: planet masses.

Data are static (JPL Solar System Dynamics) and stored
verbatim in `data/solar_system_masses.csv` next to this script. Update
the CSV (and bump its sidecar JSON) only when planetary mass values are
formally revised in the Fact Sheet.

Caption / figure id : Fig. 2.18 / `fig:ss-mass-budget`
Markdown source     : book/01_introduction/introduction.md (around line 322)
Citation key        : NASAFactSheet
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
CSV = DATA_DIR / "solar_system_masses.csv"
META = DATA_DIR / "solar_system_masses.json"
OUT_AVIF = REPO_ROOT / "book/01_introduction/figures/ss_mass_budget.avif"

# Solar mass: 1.98892e30 kg (CODATA 2018)
M_SUN_KG = 1.98892e30


def write_data() -> None:
    """Static data block. Written once; do not regenerate from secondary sources."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    rows = [
        # name, mass [Earth masses], notes
        ("Mercury",  0.0553,  ""),
        ("Venus",    0.815,   ""),
        ("Earth",    1.0,     "M_Earth = 5.9722e24 kg"),
        ("Mars",     0.107,   ""),
        ("Jupiter",  317.83,  ""),
        ("Saturn",    95.16,  ""),
        ("Uranus",    14.54,  ""),
        ("Neptune",   17.15,  ""),
    ]
    df = pd.DataFrame(rows, columns=["body", "mass_earth_units", "notes"])
    df.to_csv(CSV, index=False)
    META.write_text(json.dumps({
        "purpose": "Fig. 2.18 (fig:ss-mass-budget): solar system mass budget pie",
        "source": "JPL Solar System Dynamics",
        "source_url": "https://nssdc.gsfc.nasa.gov/planetary/factsheet/",
        "retrieved_date": "2026-04-23",
        "citation_key": "NASAFactSheet",
        "columns": {
            "body":              "Planet name (string).",
            "mass_earth_units":  "Planet mass in Earth masses (M_Earth = 5.9722e24 kg).",
            "notes":              "Free-form notes.",
        },
        "constants": {
            "M_sun_kg": M_SUN_KG,
            "M_earth_kg": 5.9722e24,
        },
        "license_note": "JPL Solar System Dynamics content is in the public domain (NASA).",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    if not CSV.exists():
        write_data()
    df = pd.read_csv(CSV)

    M_earth_kg = 5.9722e24
    df["mass_kg"] = df["mass_earth_units"] * M_earth_kg
    total_planet_kg = df["mass_kg"].sum()

    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))

    # Left: Sun vs all planets
    sun_pct = M_SUN_KG / (M_SUN_KG + total_planet_kg) * 100.0
    plt_pct = 100.0 - sun_pct
    axes[0].pie(
        [sun_pct, plt_pct],
        labels=[f"Sun\n{sun_pct:.2f}%", f"Planets\n{plt_pct:.2f}%"],
        colors=["#f4c542", "#5b8def"],
        startangle=90, counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 1.0},
        textprops={"fontsize": 11},
    )
    axes[0].set_title("Sun vs planets")

    # Right: among the planets
    sizes = df["mass_kg"] / total_planet_kg * 100.0
    colors = ["#bb6c44", "#e09e58", "#1e88e5", "#d62728",
              "#cc8f3d", "#e6c97a", "#76d6e2", "#3a87bd"]
    axes[1].pie(
        sizes,
        labels=[f"{n}\n{p:.1f}%" for n, p in zip(df["body"], sizes)],
        colors=colors,
        startangle=90, counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 1.0},
        textprops={"fontsize": 9},
    )
    axes[1].set_title("Among the planets")

    fig.suptitle("Mass budget of the solar system", fontsize=12, y=0.98)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    write_data()  # idempotent; refreshes sidecar metadata
    out = make_plot()
    print(f"  data : {CSV}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
