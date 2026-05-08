"""Generate Fig. (`fig:solar-luminosity`).

Solar luminosity evolution L(t) / L_0, parametric standard-solar-model
form of Gough (1981) reproduced by Catling (2017):

    L(t) / L_0 = 1 / (1 + (2/5) * (1 - t / t_0))

with t_0 = 4.57 Gyr (today). At t = 0: L = 0.714 L_0.

Caption / figure id : `fig:solar-luminosity`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md
Citation key        : Gough1981 (form), Catling2017 (textbook)

Geological reference markers (caption text):
- detrital zircons: 4.4 Ga
- pillow basalts and sedimentary rocks: 3.8 Ga
- stromatolites: 3.5 Ga
- Cambrian radiation: 0.54 Ga
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/solar_luminosity.avif"

T0_GYR = 4.57          # solar age today, Gyr


def L_over_L0(t_gyr: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + (2.0 / 5.0) * (1.0 - t_gyr / T0_GYR))


def make_plot() -> Path:
    apply_style()
    t = np.linspace(0, T0_GYR, 400)
    L = L_over_L0(t)

    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.plot(t, L, color="#1f77b4", lw=2.0,
            label=r"$L(t)/L_0 = 1 / (1 + \frac{2}{5}(1 - t/t_0))$")

    # t = 0 reference (faint young Sun)
    ax.axvline(0, color="#d62728", linestyle=":", lw=1.0)
    ax.text(0.05, 0.78, f"$L = {L[0]:.2f}\\,L_\\odot$ at $t = 0$",
            color="#d62728", fontsize=10)

    # Today
    ax.axvline(T0_GYR, color="#ff7f0e", linestyle="--", lw=1.0)
    ax.text(T0_GYR - 0.05, 0.85, f"Today\n$t = {T0_GYR:.2f}$ Gyr",
            color="#ff7f0e", fontsize=10, ha="right")

    # Geological markers (caption text). Convert age-before-present (Ga)
    # to time-since-formation: t = t_0 - age.
    GEO_MARKERS = [
        (4.4, "Detrital zircons"),
        (3.8, "Pillow basalts /\nsedimentary rocks"),
        (3.5, "Stromatolites"),
        (0.54, "Cambrian\nradiation"),
    ]
    for age_Ga, label in GEO_MARKERS:
        t_form = T0_GYR - age_Ga
        L_at = L_over_L0(np.array([t_form]))[0]
        ax.plot(t_form, L_at, "o", color="black", ms=7, zorder=5)
        ax.annotate(label, xy=(t_form, L_at),
                    xytext=(t_form, L_at + 0.03),
                    fontsize=9, ha="center", color="black",
                    arrowprops=dict(arrowstyle="-", color="0.4", lw=0.4))

    ax.set_xlim(-0.05, T0_GYR + 0.05)
    ax.set_ylim(0.70, 1.04)
    ax.set_xlabel(r"Time since solar formation $t$ (Gyr)")
    ax.set_ylabel(r"$L(t) / L_\odot$")
    ax.set_title("Solar luminosity evolution (Gough 1981 standard-solar model)")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="lower right", frameon=True, fontsize=10)

    # Secondary x-axis: age before present (Ga)
    secax = ax.secondary_xaxis(
        "top", functions=(lambda t: T0_GYR - t, lambda a: T0_GYR - a))
    secax.set_xlabel("Age before present (Ga)")

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
