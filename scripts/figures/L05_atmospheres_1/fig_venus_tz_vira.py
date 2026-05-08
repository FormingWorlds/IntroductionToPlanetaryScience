"""Generate Fig. (`fig:venus-tz-vira`).

Venus T(z) profile combining Pioneer Venus / VIRA (Seiff 1985)
lower-atmosphere data with VeRa (Venus Express) radio-occultation
results (Tellmann 2009). Falls monotonically from 735 K, 92 bar
surface through the cloud deck (48-70 km) to the mesopause near
100 km.

Caption / figure id : `fig:venus-tz-vira`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation keys       : Seiff1985, Tellmann2009
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/venus_tz_vira.avif"

PROFILE = [
    (  0, 735.0),
    ( 10, 658.0),
    ( 20, 575.0),
    ( 30, 495.0),
    ( 40, 410.0),
    ( 50, 348.0),
    ( 60, 262.0),
    ( 70, 230.0),
    ( 80, 200.0),
    ( 90, 175.0),
    (100, 165.0),  # mesopause
    (120, 175.0),
    (140, 195.0),
]


def make_plot() -> Path:
    apply_style()
    z = np.array([p[0] for p in PROFILE])
    T = np.array([p[1] for p in PROFILE])

    fig, ax = plt.subplots(figsize=(6.0, 8.0))

    # Cloud deck shading
    ax.axhspan(48, 70, color="#f0e3a8", alpha=0.5, zorder=0)
    ax.text(170, 59, "Cloud deck\n(48 to 70 km)", color="#9b7b18",
            fontsize=10, va="center", style="italic")

    ax.plot(T, z, color="#e07a3a", lw=2.5)

    # Surface
    ax.plot(735, 0, "o", color="#e07a3a", ms=7, zorder=5)
    ax.annotate("Surface\n735 K, 92 bar",
                xy=(735, 0), xytext=(620, 22),
                fontsize=10,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.5))

    # Mesopause
    ax.plot(165, 100, "o", color="#e07a3a", ms=7, zorder=5)
    ax.annotate("Mesopause\n~100 km",
                xy=(165, 100), xytext=(280, 110),
                fontsize=10,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.5))

    ax.set_xlim(150, 800)
    ax.set_ylim(0, 150)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Altitude (km)")
    ax.set_title("Venus T(z) (VIRA / VeRa)")
    ax.grid(linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
