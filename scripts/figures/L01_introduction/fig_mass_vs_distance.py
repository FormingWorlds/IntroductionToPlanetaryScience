"""Generate Fig. (`fig:mass-vs-distance`).

Planetary mass versus orbital semi-major axis on a log-log scale.
Companion to fig:density-vs-distance: this view emphasises the
extreme concentration of mass in Jupiter rather than the rocky-vs-gas
density gradient.

Data: JPL Solar System Dynamics, Planetary Physical Parameters,
https://ssd.jpl.nasa.gov/planets/phys_par.html. Values agree with
the NASA Planetary Fact Sheet (NSSDC) to all quoted significant
figures; NSSDC has been offline for maintenance since August 2025
so the live JPL SSD page is the active primary source. See
`solar_system_planets.json` for column descriptions and units.

Caption / figure id : `fig:mass-vs-distance`
Markdown source     : book/01_introduction/introduction.md
Citation key        : NASAFactSheet
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_CSV = Path(__file__).resolve().parent / "data" / "solar_system_planets.csv"
OUT_AVIF = REPO_ROOT / "book/01_introduction/figures/mass_vs_distance.avif"

# Per-planet label offsets in (dx, dy) points. Close pairs on the
# log-log axes (Venus-Earth, Uranus-Neptune) are staggered so the
# labels are visually separated from each other and from their markers.
LABEL_OFFSETS = {
    "Mercury": (10, 12),
    "Venus":   (-34, -18),
    "Earth":   (10, 12),
    "Mars":    (10, 12),
    "Jupiter": (10, 12),
    "Saturn":  (10, 12),
    "Uranus":  (-34, 12),
    "Neptune": (10, 12),
}


def make_plot() -> Path:
    apply_style()
    df = pd.read_csv(DATA_CSV)

    fig, ax = plt.subplots(figsize=(7.5, 4.5))

    is_terrestrial = df["mass_earth_units"] < 10.0
    rocky = df[is_terrestrial]
    giants = df[~is_terrestrial]

    ax.scatter(rocky["semi_major_axis_AU"], rocky["mass_earth_units"],
               s=120, facecolor="#d62728", edgecolor="black", linewidth=0.6,
               label="Terrestrial planets", zorder=4)
    ax.scatter(giants["semi_major_axis_AU"], giants["mass_earth_units"],
               s=120, facecolor="#5b8def", edgecolor="black", linewidth=0.6,
               label="Giant planets", zorder=4)

    for _, row in df.iterrows():
        ax.annotate(
            row["body"],
            (row["semi_major_axis_AU"], row["mass_earth_units"]),
            xytext=LABEL_OFFSETS[row["body"]], textcoords="offset points",
            fontsize=10,
        )

    # Horizontal reference line: sum of all planetary masses except Jupiter.
    # Jupiter alone exceeds this value (it sits above the line), illustrating
    # the >50% mass concentration in a single body.
    is_jupiter = df["body"] == "Jupiter"
    sum_no_jupiter = df.loc[~is_jupiter, "mass_earth_units"].sum()
    ax.axhline(sum_no_jupiter, color="gray", linestyle="--", linewidth=1.0)
    ax.text(0.32, sum_no_jupiter * 1.10,
            r"sum of all planets except Jupiter ($\approx$"
            f"{sum_no_jupiter:.0f}"
            r"$\,M_\oplus$)",
            fontsize=8, color="gray")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Orbital semi-major axis (AU)")
    ax.set_ylabel(r"Planetary mass ($M_\oplus$)")
    ax.set_xlim(0.3, 50)
    ax.set_ylim(0.03, 1000)
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="lower right", frameon=False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  data : {DATA_CSV}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
