"""Generate Fig. (`fig:hf-w-chronometry`).

Bar chart of tungsten-182 anomalies in planetary mantles, expressed
as epsilon-182W (parts per 10^4 deviation from chondrites).

Caption / figure id : `fig:hf-w-chronometry`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : Kleine2009, Kruijer2017Mars

Numerics live in `data/hf_w_anomalies.json`; see that sidecar for
per-reservoir provenance.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_FILE = Path(__file__).resolve().parent / "data/hf_w_anomalies.json"
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/hf_w_chronometry.avif"

COLORS = {
    "Chondrites (reference)": "#888888",
    "Bulk silicate Earth": "#1f77b4",
    "SNC meteorites (Mars)": "#d62728",
    "Lunar mantle": "#7f7f7f",
}


def make_plot() -> Path:
    apply_style()
    data = json.loads(DATA_FILE.read_text())
    reservoirs = data["reservoirs"]

    labels = [r["label"].replace(" (", "\n(") for r in reservoirs]
    values = np.array([r["epsilon_182W"] for r in reservoirs])
    errors = np.array([r["uncertainty"] for r in reservoirs])
    colors = [COLORS[r["label"]] for r in reservoirs]

    fig, ax = plt.subplots(figsize=(8.0, 5.2))
    x = np.arange(len(reservoirs))
    bars = ax.bar(x, values, yerr=errors, capsize=4, color=colors,
                  edgecolor="black", lw=0.6, ecolor="black",
                  error_kw=dict(lw=1.0))

    # Value labels above bars
    for xi, v, err in zip(x, values, errors):
        sign = "+" if v >= 0 else ""
        ax.text(xi, v + err + 0.07, f"{sign}{v:.1f}",
                ha="center", va="bottom", fontsize=11)

    ax.axhline(0, color="0.4", linestyle="--", lw=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel(r"$\varepsilon^{182}\mathrm{W}$  (parts per $10^4$ deviation from chondrites)")
    ax.set_title("Tungsten-182 anomalies in planetary mantles")
    ax.set_ylim(-0.3, 2.4)
    ax.grid(axis="y", linestyle=":", alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  data : {DATA_FILE}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
