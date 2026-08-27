"""Generate Fig. (`fig:hot-jupiters`).

Confirmed exoplanets in mass-period space, colour coded by detection
method, with the hot-Jupiter population (P < 10 d, M > 0.1 M_J)
highlighted by red circles and the eight Solar System planets marked
as black stars for reference.

Caption / figure id : `fig:hot-jupiters`
Markdown source     : book/02_formation_orbits/formation_orbits.md
Data                : NASA Exoplanet Archive `pscomppars`
Citation key        : NASAExoplanetArchive2026
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from scripts.figures._shared.exoarchive import fetch, latest_snapshot
from scripts.figures._shared.style import METHOD_COLORS, apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
OUT_AVIF = REPO_ROOT / "book/02_formation_orbits/figures/hot_jupiter_mass_period.avif"

COLUMNS = ["pl_name", "pl_bmassj", "pl_orbper", "discoverymethod"]
COLUMN_DESC = {
    "pl_name": "Planet name (string)",
    "pl_bmassj": "Best-determined mass or M sin i, Jupiter masses",
    "pl_orbper": "Orbital period (days)",
    "discoverymethod": "Discovery method (string)",
}

# Hot-Jupiter selection thresholds.
HJ_PERIOD_D = 10.0
HJ_MASS_MJ = 0.1

# Solar system reference: mass in Jupiter masses, period in days.
SOLAR_SYSTEM = {
    "Mercury": (1.74e-4,    87.969),
    "Venus":   (2.56e-3,   224.701),
    "Earth":   (3.15e-3,   365.256),
    "Mars":    (3.37e-4,   686.971),
    "Jupiter": (1.0,      4332.589),
    "Saturn":  (0.299,   10759.22),
    "Uranus":  (0.0457,  30688.5),
    "Neptune": (0.0540,  60182.0),
}

# Per-planet label offsets (points) to keep neighbouring labels apart.
LABEL_OFFSETS = {
    "Mercury": (8, 3),
    "Venus":   (8, -11),
    "Earth":   (8, 3),
    "Mars":    (8, -11),
    "Jupiter": (8, -11),
    "Saturn":  (8, -11),
    "Uranus":  (-36, 5),
    "Neptune": (8, 3),
}


def fetch_data(refresh: bool = False) -> Path:
    fig_tag = "hot_jupiter_mass_period"
    if refresh or latest_snapshot(DATA_DIR, figure_id=fig_tag) is None:
        csv_path, _ = fetch(
            COLUMNS,
            DATA_DIR,
            column_descriptions=COLUMN_DESC,
            figure_id=fig_tag,
            purpose="Fig. fig:hot-jupiters: mass-period scatter with hot-Jupiter selection",
        )
        return csv_path
    return latest_snapshot(DATA_DIR, figure_id=fig_tag)


def make_plot(csv_path: Path) -> Path:
    apply_style()
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["pl_orbper", "pl_bmassj"])

    fig, ax = plt.subplots(figsize=(8.6, 5.6))

    methods = (df.groupby("discoverymethod").size()
                 .sort_values(ascending=False)
                 .index.tolist())
    for method in methods:
        sub = df[df["discoverymethod"] == method]
        if len(sub) < 20:
            continue
        color = METHOD_COLORS.get(method, "#888")
        ax.scatter(sub["pl_orbper"], sub["pl_bmassj"], s=9,
                   color=color, alpha=0.5, edgecolors="none", label=method)

    # Hot-Jupiter selection overlay.
    hj = df[(df["pl_orbper"] < HJ_PERIOD_D) & (df["pl_bmassj"] > HJ_MASS_MJ)]
    ax.scatter(hj["pl_orbper"], hj["pl_bmassj"], s=34, facecolors="none",
               edgecolors="#d62728", linewidths=0.7,
               label=f"Hot Jupiters (n={len(hj)})", zorder=4)

    # Selection thresholds, labelled inside the axes away from data clumps.
    ax.axvline(HJ_PERIOD_D, color="#777", lw=0.8, linestyle=":", zorder=2)
    ax.axhline(HJ_MASS_MJ, color="#777", lw=0.8, linestyle=":", zorder=2)
    ax.text(HJ_PERIOD_D * 1.6, 1.3e-4, r"$P = 10$ d", rotation=90,
            fontsize=8, color="#555", va="bottom")
    ax.text(1.3e5, HJ_MASS_MJ * 1.25, r"$M = 0.1\,M_{\mathrm{J}}$",
            fontsize=8, color="#555")

    for name, (mass, period) in SOLAR_SYSTEM.items():
        ax.scatter(period, mass, s=80, marker="*",
                   facecolor="black", edgecolor="white", linewidth=0.4,
                   zorder=5)
        ax.annotate(name, (period, mass), xytext=LABEL_OFFSETS[name],
                    textcoords="offset points", fontsize=8, zorder=6)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Orbital period (days)")
    ax.set_ylabel(r"Planet mass or $M\sin i$ ($M_{\mathrm{J}}$)")
    ax.set_xlim(0.3, 1e6)
    ax.set_ylim(1e-4, 50)
    ax.grid(which="both", linestyle=":", alpha=0.25)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14),
              frameon=False, fontsize=8, ncol=4)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    csv_path = fetch_data(refresh=False)
    avif = make_plot(csv_path)
    print(f"  data : {csv_path}")
    print(f"  plot : {avif}")


if __name__ == "__main__":
    main()
