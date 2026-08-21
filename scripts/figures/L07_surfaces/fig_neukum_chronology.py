"""Generate Fig. (`fig:neukum-chronology`).

Lunar crater chronology: the cumulative density of craters with
D >= 1 km expected on a surface of age T,

    N(1) = a [exp(lambda T) - 1] + b T

with the lunar coefficients of Neukum, Ivanov and Hartmann (2001):
a = 5.44e-14 km^-2, lambda = 6.93 Gyr^-1, b = 8.38e-4 km^-2 Gyr^-1.
The linear term carries the steady impact flux of the last ~3 Gyr;
the exponential term carries the much heavier early bombardment.

The figure also marks where the relation rests on returned samples
and where it does not. Robbins (2014) states that no sample has yet
been tied to a geologic unit dated between ~1 and 3 Ga or older than
3.92 Ga, so the curve is an interpolation across the first interval
and an extrapolation beyond the second.

Caption / figure id : `fig:neukum-chronology`
Markdown source     : book/07_surfaces/surfaces.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/07_surfaces/figures/neukum_chronology.avif"

# Neukum, Ivanov and Hartmann (2001) lunar chronology coefficients
A_EXP = 5.44e-14      # km^-2
LAMBDA = 6.93         # Gyr^-1
B_LIN = 8.38e-4       # km^-2 Gyr^-1

# Calibration coverage of the returned samples (Robbins 2014)
SAMPLE_GAP = (1.0, 3.0)       # Gyr, no dated unit in this interval
UNCONSTRAINED_ABOVE = 3.92    # Gyr, oldest dated unit

# Worked read-off used in the lecture text
READ_OFF_DENSITY = 1.0e-2     # km^-2


def _sci(value: float) -> str:
    """Render a coefficient as mathtext, so the label follows the constant."""
    mantissa, exponent = f"{value:.2e}".split("e")
    return rf"{mantissa} \times 10^{{{int(exponent)}}}"


def n_of_t(t: np.ndarray | float) -> np.ndarray | float:
    """Cumulative density of craters with D >= 1 km on a surface of age t."""
    return A_EXP * (np.exp(LAMBDA * t) - 1.0) + B_LIN * t


def age_from_density(n: float) -> float:
    """Invert the chronology for a measured crater density."""
    return brentq(lambda t: n_of_t(t) - n, 1e-6, 4.5)


def make_plot(show_readoff: bool = True) -> Path:
    """Draw the chronology; `show_readoff=False` omits the worked read-off."""
    apply_style()
    t = np.linspace(0.0, 4.5, 900)

    fig, ax = plt.subplots(figsize=(8.4, 5.8))

    ax.axvspan(*SAMPLE_GAP, color="#d9a441", alpha=0.16, lw=0)
    ax.axvspan(UNCONSTRAINED_ABOVE, 4.5, color="0.55", alpha=0.16, lw=0)

    ax.plot(t, n_of_t(t), color="black", lw=2.0,
            label="Neukum, Ivanov and Hartmann (2001)")

    if show_readoff:
        # Read-off: a measured crater density inverts to a surface age
        t_read = age_from_density(READ_OFF_DENSITY)
        ax.plot([0.0, t_read], [READ_OFF_DENSITY] * 2,
                color="#b02418", lw=1.2, ls="--")
        ax.plot([t_read, t_read], [1e-5, READ_OFF_DENSITY],
                color="#b02418", lw=1.2, ls="--")
        ax.plot([t_read], [READ_OFF_DENSITY], "o", color="#b02418", ms=6)

    ax.set_xlim(0.0, 4.5)
    # The curve passes 1 km^-2 near 4.4 Gyr, so the top of the axis has to
    # clear N(4.5) or the steepest part of the upturn is cut off
    ax.set_ylim(1e-5, 3e0)
    ax.set_yscale("log")
    ax.set_xlabel(r"Surface age $T$ [Gyr]")
    ax.set_ylabel(r"Cumulative crater density $N(\geq 1\,\mathrm{km})$ [km$^{-2}$]")
    ax.set_title("Lunar crater chronology")
    ax.grid(which="both", linestyle=":", alpha=0.3)

    ax.text(0.16, 3.2e-1,
            r"$N(1) = a\,[e^{\lambda T} - 1] + b\,T$",
            fontsize=12, va="center",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
                      edgecolor="0.7", alpha=1.0))
    ax.text(0.16, 8.6e-2,
            f"$a = {_sci(A_EXP)}$ km$^{{-2}}$\n"
            f"$\\lambda = {LAMBDA:g}$ Gyr$^{{-1}}$\n"
            f"$b = {_sci(B_LIN)}$ km$^{{-2}}$ Gyr$^{{-1}}$",
            fontsize=9, va="center", color="0.25")

    ax.text(1.22, 4.5e-3, "steady impact flux", fontsize=10, color="0.25")
    ax.text(3.02, 3.0e-1, "early bombardment", fontsize=10, color="0.25")

    ax.text(2.0, 2.2e-5, "no dated samples", fontsize=9, color="#8a6212",
            rotation=90, ha="center", va="bottom")
    ax.text(4.21, 2.2e-5, "unconstrained", fontsize=9, color="0.35",
            rotation=90, ha="center", va="bottom")

    if show_readoff:
        ax.text(0.16, 1.9e-2,
                f"measured $N(1) = 10^{{-2}}$ km$^{{-2}}$\n"
                f"$\\rightarrow T \\approx {t_read:.2f}$ Gyr",
                fontsize=9.5, color="#b02418", va="bottom")

    ax.legend(loc="lower right", frameon=True, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")
    for age in (1.0, 3.0, 3.5, 3.92, 4.2):
        print(f"  N(1) at T = {age:.2f} Gyr : {n_of_t(age):.3e} km^-2")
    print(f"  N(1) = {READ_OFF_DENSITY:.0e} km^-2 inverts to "
          f"T = {age_from_density(READ_OFF_DENSITY):.3f} Gyr")


if __name__ == "__main__":
    main()
