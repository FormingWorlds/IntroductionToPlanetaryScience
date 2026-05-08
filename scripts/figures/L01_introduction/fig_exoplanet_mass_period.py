"""Generate Fig. 2.11 (`fig:exoplanet-mass-period`).

Planet mass (or M sin i) versus orbital period for confirmed
exoplanets, colour coded by detection method, with the eight Solar
System planets marked for reference.

Run from the repository root with the `proteus` conda env active:

    python scripts/figures/L01_introduction/fig_exoplanet_mass_period.py

Caption / figure id : Fig. 2.11 / `fig:exoplanet-mass-period`
Markdown source     : book/01_introduction/introduction.md (around line 164)
Data                : NASA Exoplanet Archive `pscomppars`, columns
                      pl_name, pl_bmassj, pl_bmasse, pl_orbper,
                      discoverymethod
Citation key        : NASAExoArchive2025
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scripts.figures._shared.exoarchive import fetch, latest_snapshot
from scripts.figures._shared.style import METHOD_COLORS, apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
OUT_AVIF = REPO_ROOT / "book/01_introduction/figures/exoplanet_mass_period.avif"

COLUMNS = ["pl_name", "pl_bmassj", "pl_bmasse", "pl_orbper", "discoverymethod"]
COLUMN_DESC = {
    "pl_name": "Planet name (string)",
    "pl_bmassj": "Best-determined mass or M sin i, Jupiter masses",
    "pl_bmasse": "Best-determined mass or M sin i, Earth masses",
    "pl_orbper": "Orbital period (days)",
    "discoverymethod": "Discovery method (string)",
}

# Solar system reference: mass in Earth masses, period in days.
SOLAR_SYSTEM = {
    "Mercury": (0.0553,    87.969),
    "Venus":   (0.815,    224.701),
    "Earth":   (1.0,      365.256),
    "Mars":    (0.107,    686.971),
    "Jupiter": (317.83,  4332.589),
    "Saturn":  (95.16,  10759.22),
    "Uranus":  (14.54,  30688.5),
    "Neptune": (17.15,  60182.0),
}


def fetch_data(refresh: bool = True) -> Path:
    fig_tag = "exoplanet_mass_period"
    if refresh or latest_snapshot(DATA_DIR, figure_id=fig_tag) is None:
        csv_path, _ = fetch(
            COLUMNS,
            DATA_DIR,
            column_descriptions=COLUMN_DESC,
            figure_id=fig_tag,
            purpose="Fig. 2.11 (fig:exoplanet-mass-period): planet mass vs orbital period scatter, by method",
        )
        return csv_path
    return latest_snapshot(DATA_DIR, figure_id=fig_tag)


def make_plot(csv_path: Path) -> Path:
    apply_style()
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["pl_orbper", "pl_bmasse"])

    fig, ax = plt.subplots(figsize=(8, 5.6))

    methods = (df.groupby("discoverymethod").size()
                 .sort_values(ascending=False)
                 .index.tolist())
    for method in methods:
        sub = df[df["discoverymethod"] == method]
        if len(sub) < 5:
            continue
        color = METHOD_COLORS.get(method, "#888")
        ax.scatter(sub["pl_orbper"], sub["pl_bmasse"], s=10,
                   color=color, alpha=0.55, edgecolors="none", label=method)

    # Solar system reference points
    for name, (mass, period) in SOLAR_SYSTEM.items():
        ax.scatter(period, mass, s=70, marker="*",
                   facecolor="gold", edgecolor="black", linewidth=0.6, zorder=5)
        ax.annotate(name, (period, mass), xytext=(6, 3),
                    textcoords="offset points", fontsize=8)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Orbital period (days)")
    ax.set_ylabel(r"Planet mass or $M\sin i$ ($M_\oplus$)")
    ax.set_xlim(0.1, 5e5)
    ax.set_ylim(1e-2, 1e5)
    ax.grid(which="both", linestyle=":", alpha=0.25)
    ax.legend(loc="lower right", frameon=False, fontsize=8, ncol=2)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    csv_path = fetch_data(refresh=True)
    avif = make_plot(csv_path)
    print(f"  data : {csv_path}")
    print(f"  plot : {avif}")


if __name__ == "__main__":
    main()
