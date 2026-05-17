"""Generate Fig. (`fig:vem-atmospheres`).

Two-panel bar chart of surface temperature and surface pressure for
Venus, Earth, and Mars, with the dominant atmospheric species
labelled. The point is to show the ~500 K range in T_surf and ~10^4
range in P_surf despite the three planets having broadly similar bulk
compositions.

Data: JPL Solar System Dynamics; see
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
    ax_P.set_ylim(1e-3, 500)

    # Value labels on each bar. Use `bar_label` with a fixed pixel
    # padding so labels sit a consistent visual distance above each
    # bar, including the very short Mars pressure bar on the log
    # y-axis (where a multiplicative offset is inadequate). Mars
    # surface pressure (6.36e-3 bar) uses scientific notation so the
    # label string is narrow enough to clear the adjacent T bar.
    def _fmt_p(v: float) -> str:
        if v < 0.01:
            exp = int(np.floor(np.log10(v)))
            mant = v / 10.0 ** exp
            return rf"${mant:.2f}{{\times}}10^{{{exp}}}$ bar"
        if v >= 10:
            return f"{v:.0f} bar"
        return f"{v:.2f} bar"

    ax_T.bar_label(bars_T,
                   labels=[f"{int(v)} K" for v in df["Tsurf_K"]],
                   padding=8, fontsize=9, color="#a83232")
    # Pressure labels: Venus and Earth sit just above their own bars
    # with 8 px of padding. Mars is plotted on a log P axis so its
    # 6e-3 bar bar is tiny; the label is hard-pinned at y = 0.06 bar
    # (well above the 210 K T-bar label across the gap) to remove any
    # ambiguity about which bar each label belongs to.
    MARS_P_LABEL_Y = 0.06
    for bar, body, v in zip(bars_P, BODIES, df["Psurf_bar"]):
        x_center = bar.get_x() + bar.get_width() / 2
        if body == "Mars":
            ax_P.annotate(_fmt_p(v), (x_center, MARS_P_LABEL_Y),
                          xytext=(0, 0), textcoords="offset points",
                          ha="center", va="bottom",
                          fontsize=9, color="#1d4d80")
        else:
            ax_P.annotate(_fmt_p(v), (x_center, v),
                          xytext=(0, 8), textcoords="offset points",
                          ha="center", va="bottom",
                          fontsize=9, color="#1d4d80")

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
