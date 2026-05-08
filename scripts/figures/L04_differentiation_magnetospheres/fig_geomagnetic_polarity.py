"""Generate Fig. (`fig:geomagnetic-polarity`).

Schematic geomagnetic polarity timescale for the past 170 Myr.
Black bars mark normal polarity, white bars reversed polarity. The
Cretaceous Normal Superchron (C34n, ~83-121 Ma) is the long
uninterrupted black band in the middle of the plot.

Caption / figure id : `fig:geomagnetic-polarity`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Gradstein2020

This is a schematic: chron boundaries are generated as alternating
intervals with realistic mean rates (~3 / Myr in the Cenozoic,
~2 / Myr pre-C34n) using a fixed random seed for reproducibility,
with the C34n boundary placed explicitly. Exact chron ages should
be looked up in the Geologic Time Scale 2020 compilation.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/geomagnetic_polarity_timescale.avif"

T_MAX_MA = 170.0
C34N_START = 83.0   # young end (Ma)
C34N_END = 121.0    # old end (Ma)


def _gen_intervals(t_start: float, t_end: float,
                   mean_length: float, rng: np.random.Generator,
                   start_polarity: str = "normal") -> list[tuple[float, float, str]]:
    """Generate alternating polarity intervals between t_start and t_end."""
    intervals: list[tuple[float, float, str]] = []
    t = t_start
    polarity = start_polarity
    while t < t_end:
        # Exponentially distributed chron length with mean = mean_length
        L = rng.exponential(mean_length)
        L = max(L, 0.05)
        nxt = min(t + L, t_end)
        intervals.append((t, nxt, polarity))
        t = nxt
        polarity = "reversed" if polarity == "normal" else "normal"
    return intervals


def make_plot() -> Path:
    apply_style()
    rng = np.random.default_rng(seed=42)

    # 0 - C34N_START (young end of CNS): Cenozoic + early Mesozoic post-CNS
    # ~3-4 reversals/Myr -> mean chron length ~0.3 Myr
    pre_cns = _gen_intervals(0.0, C34N_START, mean_length=0.3, rng=rng,
                             start_polarity="normal")
    # CNS itself: single normal block
    cns = [(C34N_START, C34N_END, "normal")]
    # Pre-CNS Jurassic - Cretaceous: ~2 reversals/Myr -> mean ~0.5 Myr
    post_cns = _gen_intervals(C34N_END, T_MAX_MA, mean_length=0.5, rng=rng,
                              start_polarity="reversed")
    intervals = pre_cns + cns + post_cns

    fig, ax = plt.subplots(figsize=(11.5, 3.3))
    bar_y = 0.0
    bar_h = 1.0
    for t0, t1, pol in intervals:
        color = "black" if pol == "normal" else "white"
        ax.add_patch(Rectangle((t0, bar_y), t1 - t0, bar_h,
                               facecolor=color, edgecolor="none"))

    # Outline around the bar
    ax.add_patch(Rectangle((0.0, bar_y), T_MAX_MA, bar_h,
                           fill=False, edgecolor="black", lw=1.0))

    # CNS annotation
    cns_mid = 0.5 * (C34N_START + C34N_END)
    ax.annotate("Cretaceous Normal Superchron (C34n)",
                xy=(cns_mid, bar_y + bar_h),
                xytext=(cns_mid, bar_y + bar_h + 1.3),
                ha="center", fontsize=11,
                arrowprops=dict(arrowstyle="-", color="black", lw=0.8))

    # Era bars below the polarity bar
    era_y = bar_y - 0.55
    era_h = 0.10
    # Mesozoic: 252.2 - 66.0 Ma; we draw 66 - 170 (capped)
    ax.add_patch(Rectangle((66.0, era_y), T_MAX_MA - 66.0, era_h,
                           color="0.6"))
    ax.text(0.5 * (66.0 + T_MAX_MA), era_y - 0.25, "Mesozoic",
            color="0.4", ha="center", va="top", fontsize=10)
    # Cenozoic: 66 - 0 Ma
    ax.add_patch(Rectangle((0.0, era_y), 66.0, era_h, color="0.6"))
    ax.text(0.5 * 66.0, era_y - 0.25, "Cenozoic",
            color="0.4", ha="center", va="top", fontsize=10)

    ax.set_xlim(T_MAX_MA, 0)  # young to right
    ax.set_ylim(era_y - 0.7, bar_y + bar_h + 2.4)
    ax.set_xlabel("Age (Ma)")
    ax.set_yticks([])
    ax.set_title("Geomagnetic polarity timescale, last 170 Myr "
                 "(black = normal, white = reversed)", pad=10)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="x", which="both", direction="out")

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
