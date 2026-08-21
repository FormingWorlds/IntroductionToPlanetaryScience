"""Generate Fig. (`fig:maven-o-loss-channels`).

Present-day oxygen loss rates from Mars by escape channel, after
Jakosky et al. (2018) Fig. 6: O ion escape, photochemical escape, and
sputtering, plus the combined total. Channels with a published range
are drawn as a horizontal bar between the range ends; single-value
channels are drawn as one marker.

Caption / figure id : `fig:maven-o-loss-channels`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation key        : Jakosky2018
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/maven_o_loss_channels.avif"

BLUE = "#1f77b4"

# log10 of the loss rate in s^-1, after Jakosky et al. (2018) Fig. 6.
# A 2-tuple is a published range; a 1-tuple is a single value.
CHANNELS = [
    ("O ion loss",         (24.44, 25.09)),
    ("Photochemical loss", (25.41, 25.67)),
    ("Sputtering loss",    (24.44,)),
    ("Total O loss",       (25.79,)),
]


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(7.0, 3.4))

    for i, (name, vals) in enumerate(CHANNELS):
        color = "black" if name == "Total O loss" else BLUE
        if len(vals) == 2:
            ax.plot(vals, [i, i], color=color, lw=2.2,
                    marker="o", markersize=7, solid_capstyle="round")
        else:
            ax.plot(vals[0], i, color=color, marker="o", markersize=7)

    ax.set_yticks(range(len(CHANNELS)))
    ax.set_yticklabels([name for name, _ in CHANNELS], fontsize=11)
    ax.set_xlim(24, 28)
    ax.set_ylim(-0.6, len(CHANNELS) - 0.4)
    ax.set_xlabel(r"$\log_{10}$ O loss rate (s$^{-1}$)")
    ax.set_title("Present-day oxygen loss from Mars", fontsize=12, pad=8)
    ax.grid(axis="x", linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
