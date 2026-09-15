"""Generate Fig. (`fig:fulton-radius-valley`).

Radius distribution of the 900 short-period planets of the California-
Kepler Survey (Fulton et al. 2017, their Table 2, VizieR J/AJ/154/109),
drawn as raw counts in logarithmic radius bins. The radius valley near
1.8 Earth radii separates the super-Earth and sub-Neptune peaks without
any completeness correction, which the paper applies on top.

Caption / figure id : fig:fulton-radius-valley (notes) and a deck hero frame
Deck source         : slides/lecture05/lecture05.tex
Citation key        : Fulton2017
"""
from __future__ import annotations

import io
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_TSV = Path(__file__).resolve().parent / "data/fulton2017_cks_table2.tsv"
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/fulton2017_radius_valley.avif"

P_MAX_DAYS = 100.0
R_MIN, R_MAX, N_BINS = 0.7, 20.0, 20
X_TICKS = [0.7, 1.0, 1.3, 1.8, 2.4, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0]


def load_sample() -> pd.DataFrame:
    """Read the VizieR TSV export of Table 2 and keep P < 100 days."""
    lines = [l for l in DATA_TSV.read_text().splitlines(keepends=True)
             if not l.startswith("#") and l.strip()]
    df = pd.read_csv(io.StringIO("".join(lines)), sep="\t", skiprows=[1, 2])
    df.columns = [c.strip() for c in df.columns]
    df = df.apply(pd.to_numeric, errors="coerce")
    return df[(df["Per"] < P_MAX_DAYS) & (df["Rad"] > 0)]


def make_plot() -> Path:
    apply_style()
    sample = load_sample()
    edges = np.logspace(np.log10(R_MIN), np.log10(R_MAX), N_BINS + 1)
    counts, _ = np.histogram(sample["Rad"], bins=edges)

    fig, ax = plt.subplots(figsize=(5.76, 3.6))
    ax.bar(edges[:-1], counts, width=np.diff(edges), align="edge",
           color="#9ecae1", edgecolor="#2c7f8c", linewidth=0.8)
    ax.set_xscale("log")
    ax.set_xlim(R_MIN, R_MAX)
    ax.set_xticks(X_TICKS)
    ax.set_xticklabels([f"{x:g}" for x in X_TICKS])
    ax.minorticks_off()
    ax.set_ylim(0, 180)
    ax.set_xlabel(r"Planet radius ($R_\oplus$)")
    ax.set_ylabel("Number of planets")
    ax.grid(axis="y", linestyle=":", alpha=0.3)

    # Population labels; the valley label sits above the dip with a leader
    ax.annotate("Super-Earths", xy=(1.08, 136), ha="center", va="bottom",
                fontsize=11, color="#c2452e", weight="bold")
    ax.annotate("Sub-Neptunes", xy=(2.95, 112), ha="center", va="bottom",
                fontsize=11, color="#2c7f8c", weight="bold")
    ax.annotate("Radius valley", xy=(1.76, 72), xytext=(1.76, 165),
                ha="center", va="center", fontsize=11, color="0.25",
                weight="bold",
                arrowprops=dict(arrowstyle="->", color="0.25", lw=1.2))
    ax.text(0.98, 0.95, f"{len(sample)} CKS planets, $P < {P_MAX_DAYS:.0f}$ d",
            transform=ax.transAxes, ha="right", va="top", fontsize=9,
            color="0.35")

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80, dpi=280)


def main() -> None:
    """Build the figure and report the output path."""
    print(f"  plot : {make_plot()}")


if __name__ == "__main__":
    main()
