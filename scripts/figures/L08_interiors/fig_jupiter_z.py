"""Generate Fig. (`fig:jupiter-z`).

Schematic comparison of Jupiter's heavy-element mass fraction Z(r):

- Classical compact-core picture (pre-Juno): Z ~ 1 inside r/R < 0.1,
  near-solar envelope (~0.02) elsewhere.
- Dilute-core picture (Juno-inferred; Wahl+2017): Z ~ 0.20-0.25 at
  the centre, declining gradually over the inner ~0.4-0.5 of the
  radius to envelope values.

Caption / figure id : `fig:jupiter-z`
Markdown source     : book/08_interiors/interiors.md
Citation key        : Wahl2017
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/jupiter_z.avif"

Z_ENVELOPE = 0.02


def make_plot() -> Path:
    apply_style()
    r = np.linspace(0, 1, 600)

    # Classical compact-core: step function
    Z_classical = np.where(r < 0.10, 1.0, Z_ENVELOPE)

    # Dilute core: smooth tanh decline from ~0.25 to ~0.02 over r ~ 0.05-0.45
    Z_dilute = Z_ENVELOPE + (0.25 - Z_ENVELOPE) * \
               0.5 * (1.0 - np.tanh((r - 0.30) / 0.06))

    fig, ax = plt.subplots(figsize=(8.5, 5.5))

    # Shaded "dilute-core" region 0 < r/R < 0.45
    ax.axvspan(0, 0.45, color="#cfe5ff", alpha=0.35, zorder=0)
    ax.text(0.22, 0.65, "Dilute-core region\n(Z smoothly decreasing)",
            fontsize=10, color="#1f4e79", ha="center")

    ax.plot(r, Z_classical, color="0.4", linestyle="--", lw=2.0,
            label="Classical compact core\n(pre-Juno models)")
    ax.plot(r, Z_dilute, color="#1f4e79", lw=2.5,
            label="Dilute core (Juno-inferred;\nWahl+2017)")

    # H molecular/metallic transition reference
    ax.axvline(0.80, color="0.5", linestyle=":", lw=0.8)
    ax.text(0.81, 0.5, "H molecular/metallic\ntransition", rotation=90,
            color="0.4", fontsize=9, va="center", ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel(r"Fractional radius $r / R_{\mathrm{Jup}}$")
    ax.set_ylabel(r"Heavy-element mass fraction $Z(r)$")
    ax.set_title("Jupiter's heavy-element distribution: classical vs dilute core")
    ax.legend(loc="upper right", frameon=True, fontsize=10)
    ax.grid(linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
