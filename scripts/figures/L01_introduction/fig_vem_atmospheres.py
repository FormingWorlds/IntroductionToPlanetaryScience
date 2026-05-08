"""Generate Fig. (`fig:vem-atmospheres`).

Two-panel bar chart of surface temperature and surface pressure for
Venus, Earth, and Mars, with the dominant atmospheric species
labelled. The point is to show the ~500 K range in T_surf and ~10^4
range in P_surf despite the three planets having broadly similar bulk
compositions.

Data: NASA Planetary Fact Sheet (Williams 2024); see
`solar_system_planets.json`.

Caption / figure id : `fig:vem-atmospheres`
Markdown source     : book/01_introduction/introduction.md (around line 353)
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
OUT_AVIF = REPO_ROOT / "book/01_introduction/figures/venus_earth_mars_atmospheres.avif"

BODIES = ["Venus", "Earth", "Mars"]


def make_plot() -> Path:
    apply_style()
    df = pd.read_csv(DATA_CSV)
    df = df.set_index("body").loc[BODIES].reset_index()

    fig, ax_T = plt.subplots(figsize=(7.5, 4.4))
    ax_P = ax_T.twinx()

    x = np.arange(len(BODIES))
    width = 0.35

    bars_T = ax_T.bar(x - width / 2, df["Tsurf_K"], width,
                      color="#d62728", alpha=0.85, label="Surface temperature")
    bars_P = ax_P.bar(x + width / 2, df["Psurf_bar"], width,
                      color="#1f77b4", alpha=0.85, label="Surface pressure")

    # Annotate species below x-axis
    for xi, body in zip(x, BODIES):
        sp = df[df["body"] == body]["dominant_species"].iloc[0]
        sp_label = {"CO2": r"$\mathrm{CO_2}$",
                    "N2":  r"$\mathrm{N_2}/\mathrm{O_2}$"}.get(sp, sp)
        ax_T.annotate(sp_label, (xi, 0), xytext=(0, -32),
                      textcoords="offset points",
                      ha="center", fontsize=10, color="dimgray")

    ax_T.set_xticks(x)
    ax_T.set_xticklabels(BODIES, fontsize=11)
    ax_T.set_ylabel(r"Surface temperature $T_s$ (K)", color="#d62728")
    ax_T.tick_params(axis="y", labelcolor="#d62728")
    ax_T.set_ylim(0, 800)

    ax_P.set_yscale("log")
    ax_P.set_ylabel(r"Surface pressure $P_s$ (bar, log scale)", color="#1f77b4")
    ax_P.tick_params(axis="y", labelcolor="#1f77b4")
    ax_P.set_ylim(1e-3, 200)

    # Value labels on each bar
    for bar, val in zip(bars_T, df["Tsurf_K"]):
        ax_T.text(bar.get_x() + bar.get_width() / 2, val + 15,
                  f"{int(val)} K", ha="center", fontsize=9, color="#a83232")
    for bar, val in zip(bars_P, df["Psurf_bar"]):
        if val >= 1e-3:
            label = f"{val:.3g} bar"
            ax_P.text(bar.get_x() + bar.get_width() / 2, val * 1.4,
                      label, ha="center", fontsize=9, color="#1d4d80")

    ax_T.spines["top"].set_visible(False)
    ax_P.spines["top"].set_visible(False)
    ax_T.grid(False)
    ax_P.grid(False)

    fig.subplots_adjust(bottom=0.18)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  data : {DATA_CSV}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
