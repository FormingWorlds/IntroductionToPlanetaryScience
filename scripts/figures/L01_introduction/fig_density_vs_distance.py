"""Generate Fig. (`fig:density-vs-distance`).

Bulk density of the eight solar-system planets versus orbital
semi-major axis on a log-x scale, illustrating the rocky-versus-gas
density gradient set by the protoplanetary disk's temperature
structure. A horizontal reference line marks the uncompressed
density of typical silicate mantle rock (~3300 kg m^-3).

Data: JPL Solar System Dynamics, Planetary Physical Parameters,
https://ssd.jpl.nasa.gov/planets/phys_par.html. Values agree with
the NASA Planetary Fact Sheet (NSSDC) to all quoted significant
figures; NSSDC has been offline for maintenance since August 2025
so the live JPL SSD page is the active primary source. See sibling
`solar_system_planets.json` for full column descriptions and units.

Caption / figure id : `fig:density-vs-distance`
Markdown source     : book/01_introduction/introduction.md
Citation key        : NASAFactSheet
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_CSV = Path(__file__).resolve().parent / "data" / "solar_system_planets.csv"
OUT_AVIF = REPO_ROOT / "book/01_introduction/figures/density_vs_distance.avif"

# Constants used to derive bulk density from the CSV columns.
M_EARTH_KG = 5.9722e24
RHO_WATER = 1000.0       # kg / m^3, reference for "less dense than water"
RHO_ROCK = 3300.0        # kg / m^3, uncompressed silicate mantle rock (olivine / peridotite)

# Per-planet label offsets in (dx, dy) points to keep text from
# overlapping any markers, the reference lines, or neighbouring labels.
# Venus is dropped below its marker to separate from Earth; all other
# labels sit above their markers, with Saturn raised to avoid the
# liquid-water reference line at 1000 kg/m^3.
LABEL_OFFSETS = {
    "Mercury": (10, 12),
    "Venus":   (10, -18),
    "Earth":   (10, 12),
    "Mars":    (10, 12),
    "Jupiter": (10, 12),
    "Saturn":  (10, 18),
    "Uranus":  (-36, 12),
    "Neptune": (10, 12),
}


def compute_densities(df: pd.DataFrame) -> pd.DataFrame:
    """Return df with an added bulk-density column in kg/m^3."""
    mass_kg = df["mass_earth_units"] * M_EARTH_KG
    radius_m = df["radius_km"] * 1.0e3
    volume_m3 = (4.0 / 3.0) * np.pi * radius_m ** 3
    df = df.copy()
    df["density_kg_m3"] = mass_kg / volume_m3
    return df


def make_plot() -> Path:
    apply_style()
    df = compute_densities(pd.read_csv(DATA_CSV))

    fig, ax = plt.subplots(figsize=(7.5, 4.5))

    # Colour-code rocky vs giant (mass < 1 M_earth threshold leaves Mars
    # off the rocky side, so use 0.05 M_earth -> giant heuristic instead).
    is_terrestrial = df["mass_earth_units"] < 10.0
    rocky = df[is_terrestrial]
    giants = df[~is_terrestrial]

    ax.scatter(rocky["semi_major_axis_AU"], rocky["density_kg_m3"],
               s=120, facecolor="#d62728", edgecolor="black", linewidth=0.6,
               label="Terrestrial planets", zorder=4)
    ax.scatter(giants["semi_major_axis_AU"], giants["density_kg_m3"],
               s=120, facecolor="#5b8def", edgecolor="black", linewidth=0.6,
               label="Giant planets", zorder=4)

    for _, row in df.iterrows():
        ax.annotate(
            row["body"],
            (row["semi_major_axis_AU"], row["density_kg_m3"]),
            xytext=LABEL_OFFSETS[row["body"]], textcoords="offset points",
            fontsize=10,
        )

    ax.axhline(RHO_WATER, color="gray", linestyle="--", linewidth=1.0)
    ax.text(0.32, RHO_WATER * 1.05, r"density of liquid water",
            fontsize=8, color="gray")

    ax.axhline(RHO_ROCK, color="saddlebrown", linestyle="--", linewidth=1.0)
    ax.text(0.32, RHO_ROCK * 1.04,
            r"uncompressed silicate rock ($\sim$3300 kg m$^{-3}$)",
            fontsize=8, color="saddlebrown")

    ax.set_xscale("log")
    ax.set_xlabel("Orbital semi-major axis (AU)")
    ax.set_ylabel(r"Bulk density (kg m$^{-3}$)")
    ax.set_xlim(0.3, 50)
    ax.set_ylim(0, 6500)
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  data : {DATA_CSV}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
