"""Generate Fig. (`fig:snowball-bistability`).

Energy balance with ice-albedo feedback:

    OLR(T)        = epsilon_eff * sigma T^4         (red curve)
    Absorbed(T)   = (1 - alpha(T)) * S/4            (blue curve)
    alpha(T)      = alpha_warm + (alpha_ice - alpha_warm) *
                    [1 - tanh((T - T0)/dT)] / 2

The system has three steady states where the curves cross: a stable
"snowball" cold state, an unstable deglaciation threshold, and a
stable warm state.

Caption / figure id : `fig:snowball-bistability`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md

Parameter choices anchor the warm-stable equilibrium near 286 K
(consistent with caption text), the threshold near 268 K, and the
snowball state near 246 K.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/snowball_bistability.avif"

SIGMA = 5.670374419e-8  # W/m^2/K^4
S_TODAY = 1361.0        # W/m^2 solar constant
EPSILON_EFF = 0.62      # effective grey emissivity (fixed CO2 greenhouse)
ALPHA_ICE = 0.6
ALPHA_WARM = 0.30
T0 = 268.0              # K, midpoint of albedo transition
DT = 6.0                # K, half-width of albedo transition


def albedo(T: np.ndarray) -> np.ndarray:
    return ALPHA_WARM + (ALPHA_ICE - ALPHA_WARM) * 0.5 * (1.0 - np.tanh((T - T0) / DT))


def OLR(T: np.ndarray) -> np.ndarray:
    return EPSILON_EFF * SIGMA * T ** 4


def absorbed(T: np.ndarray) -> np.ndarray:
    return (1.0 - albedo(T)) * S_TODAY / 4.0


def make_plot() -> Path:
    apply_style()
    T = np.linspace(220, 320, 600)

    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.plot(T, OLR(T), color="#d62728", lw=2.0,
            label=r"Outgoing longwave $\sigma T^4$")
    ax.plot(T, absorbed(T), color="#1f77b4", lw=2.0,
            label=r"Absorbed solar $(1 - \alpha(T))\, S/4$")

    # Find equilibria (sign changes of OLR-absorbed)
    diff = OLR(T) - absorbed(T)
    sign_changes = np.where(np.diff(np.sign(diff)))[0]
    eq_T = []
    for i in sign_changes:
        # Linear interpolate
        t1, t2 = T[i], T[i + 1]
        d1, d2 = diff[i], diff[i + 1]
        t_eq = t1 - d1 * (t2 - t1) / (d2 - d1)
        eq_T.append(t_eq)

    # Plot equilibria with labels
    eq_labels = [
        ("Snowball\nstable", "#1f4e79"),
        ("Unstable\n(deglaciation\nthreshold)", "#1f6b3b"),
        ("Warm\nstable", "#a14a25"),
    ]
    for t_eq, (label, color) in zip(eq_T, eq_labels):
        flux_eq = OLR(np.array([t_eq]))[0]
        ax.plot(t_eq, flux_eq, "o", color="black", ms=8, zorder=5)
        ax.text(t_eq, flux_eq + 25, f"{t_eq:.0f} K",
                ha="center", fontsize=10)
        # Region labels
        if "Snowball" in label:
            ax.text(t_eq - 10, flux_eq - 15, label, color=color,
                    fontsize=10, ha="right", va="top")
        elif "Unstable" in label:
            ax.text(t_eq, flux_eq + 70, label, color=color,
                    fontsize=10, ha="center")
        else:
            ax.text(t_eq + 10, flux_eq + 30, label, color=color,
                    fontsize=10, ha="left")

    ax.set_xlim(220, 320)
    ax.set_ylim(0, 500)
    ax.set_xlabel("Surface temperature [K]")
    ax.set_ylabel(r"Energy flux [W m$^{-2}$]")
    ax.set_title("Ice-albedo feedback and snowball bistability")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
