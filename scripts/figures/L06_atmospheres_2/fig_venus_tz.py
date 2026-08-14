"""Generate Fig. (`fig:venus-tz`).

Venus thermal structure from the surface (737 K, 92 bar) up to
100 km, based on the Venus International Reference Atmosphere
(VIRA, Seiff 1985) and Venus Express radio-science (VeRa,
Tellmann 2009).

The H2SO4 cloud deck (48-70 km) is shaded yellow; the sub-cloud
haze (31-48 km) is shaded peach. The cold-collar inversion near
65 km (prominent at high latitudes in VeRa retrievals) is marked.

Caption / figure id : `fig:venus-tz`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md
Citation key        : Tellmann2009 (Seiff1985 for VIRA)

Reference points are the published VIRA mid-latitude tabulated
values; T(z) here is a piecewise-linear fit, not a direct
re-tabulation.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/venus_tz_profile.avif"

# (altitude_km, temperature_K) anchor points - VIRA / VeRa mid-latitudes
PROFILE = [
    (  0, 737.0),
    ( 10, 658.0),
    ( 20, 575.0),
    ( 30, 495.0),
    ( 40, 410.0),
    ( 50, 348.0),
    ( 55, 305.0),
    ( 60, 262.0),
    ( 64, 245.0),  # cold collar inversion
    ( 70, 230.0),
    ( 80, 195.0),
    ( 90, 175.0),
    (100, 165.0),
]
CLOUD_DECK = (48, 70)
SUBCLOUD_HAZE = (31, 48)


def make_plot() -> Path:
    apply_style()
    z = np.array([p[0] for p in PROFILE])
    T = np.array([p[1] for p in PROFILE])

    fig, ax = plt.subplots(figsize=(6.5, 8.5))

    # Shading
    ax.axhspan(*CLOUD_DECK, color="#f0e3a8", alpha=0.6, zorder=0,
               label="H$_2$SO$_4$ cloud deck (48-70 km)")
    ax.axhspan(*SUBCLOUD_HAZE, color="#fdebcb", alpha=0.55, zorder=0,
               label="Sub-cloud haze (31-48 km)")

    ax.plot(T, z, color="#a83232", lw=2.5,
            label="Venus T(z) (VIRA / Venus Express VeRa)")

    # Surface annotation
    ax.plot(737, 0, "o", color="#a83232", ms=8, zorder=5)
    ax.annotate("Surface\n(737 K, 92 bar)",
                xy=(737, 0), xytext=(645, 24),
                fontsize=10,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.5))

    # Cold-collar marker
    ax.annotate("Cold collar\n(~65 km)", xy=(245, 64),
                xytext=(360, 80),
                fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.6))

    ax.set_xlim(150, 800)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Temperature [K]")
    ax.set_ylabel("Altitude [km]")
    ax.set_title("Venus atmospheric thermal profile")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=True, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
