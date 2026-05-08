"""Generate Fig. 2.10 (`fig:exoplanet-cumulative`).

Cumulative number of confirmed exoplanets per discovery year, colour
coded by detection method. Data: NASA Exoplanet Archive `pscomppars`
table, columns `disc_year`, `discoverymethod`.

Run from the repository root with the `proteus` conda env active:

    python scripts/figures/L01_introduction/fig_exoplanet_cumulative.py

Re-running will (a) download a fresh CSV snapshot from the Archive,
(b) regenerate `book/01_introduction/figures/exoplanet_cumulative.avif`,
and (c) update the access-date metadata embedded in the data sidecar
(`scripts/figures/L01_introduction/data/`).

Caption / figure id : Fig. 2.10 / `fig:exoplanet-cumulative`
Markdown source     : book/01_introduction/introduction.md (around line 156)
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
OUT_AVIF = REPO_ROOT / "book/01_introduction/figures/exoplanet_cumulative.avif"

COLUMNS = ["pl_name", "disc_year", "discoverymethod"]
COLUMN_DESC = {
    "pl_name": "Planet name (string)",
    "disc_year": "Discovery year (integer)",
    "discoverymethod": "Discovery method (string)",
}


def fetch_data(refresh: bool = True) -> Path:
    """Download a fresh snapshot (or reuse the latest) and return CSV path."""
    fig_tag = "exoplanet_cumulative"
    if refresh or latest_snapshot(DATA_DIR, figure_id=fig_tag) is None:
        csv_path, _ = fetch(
            COLUMNS,
            DATA_DIR,
            column_descriptions=COLUMN_DESC,
            figure_id=fig_tag,
            purpose="Fig. 2.10 (fig:exoplanet-cumulative): cumulative confirmed exoplanets per discovery year, by method",
        )
        return csv_path
    return latest_snapshot(DATA_DIR, figure_id=fig_tag)


def make_plot(csv_path: Path) -> Path:
    apply_style()
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["disc_year"])
    df["disc_year"] = df["disc_year"].astype(int)

    methods = (df.groupby("discoverymethod").size()
                 .sort_values(ascending=False)
                 .index.tolist())
    years = np.arange(int(df["disc_year"].min()), int(df["disc_year"].max()) + 1)

    fig, ax = plt.subplots(figsize=(8, 4.6))
    cum_total = np.zeros_like(years, dtype=float)

    for method in methods:
        per_year = (df[df["discoverymethod"] == method]
                      .groupby("disc_year").size()
                      .reindex(years, fill_value=0)
                      .values)
        cum = per_year.cumsum()
        if cum[-1] < 5:
            continue  # skip negligible methods to keep the legend tractable
        color = METHOD_COLORS.get(method, "#888")
        ax.fill_between(years, cum_total, cum_total + cum, color=color,
                        alpha=0.85, linewidth=0, label=method)
        cum_total += cum

    ax.set_xlabel("Year of discovery")
    ax.set_ylabel("Cumulative number of confirmed exoplanets")
    ax.set_xlim(years[0], years[-1])
    ax.set_ylim(0, cum_total.max() * 1.05)
    ax.grid(axis="y", linestyle=":", alpha=0.3)
    ax.legend(loc="upper left", frameon=False, ncol=1)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    csv_path = fetch_data(refresh=True)
    avif = make_plot(csv_path)
    print(f"  data : {csv_path}")
    print(f"  plot : {avif}")


if __name__ == "__main__":
    main()
