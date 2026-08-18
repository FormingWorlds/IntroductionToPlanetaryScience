"""Generate Fig. (`fig:dynamo-scaling`).

Predicted versus observed (or simulated) dipole field strength for
convection-driven dynamos, illustrating the buoyancy-flux scaling law
of the lecture notes. Grey crosses sketch the collapse of numerical
dynamo simulations onto a single line; the coloured markers place the
dynamo-hosting solar-system bodies on the same relation.

Caption / figure id : `fig:dynamo-scaling`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : ChristensenAubert2006, OlsonChristensen2006

Illustrative schematic after Christensen & Aubert (2006) and Olson &
Christensen (2006); the scatter is drawn to emulate the published
collapse, not digitized from it.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/christensen2006_dynamo_scaling.avif"

# (name, predicted, observed, colour, label offset in points)
PLANETS = [
    ("Jupiter", 20.0, 20.0, "#d62728", (10, -14)),
    ("Saturn", 1.6, 1.8, "#ff9f2e", (10, -14)),
    ("Earth", 0.63, 0.71, "#2e6cb0", (10, -14)),
    ("Ganymede", 0.08, 0.10, "#44aa50", (10, -14)),
    ("Mercury", 0.05, 0.056, "#8c3c96", (10, -14)),
]


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(6.2, 6.2))

    rng = np.random.default_rng(42)
    log_x = rng.uniform(-1.85, 1.9, 70)
    log_y = log_x + rng.normal(0.0, 0.16, log_x.size)
    # Keep the neighbourhood of each planet marker and its label free
    # of crosses so the annotations sit clear of all ink
    keep = np.ones(log_x.size, dtype=bool)
    for _, px, py, _, _ in PLANETS:
        keep &= ~((np.abs(log_x - np.log10(px)) < 0.34)
                  & (np.abs(log_y - np.log10(py)) < 0.26))
    log_x, log_y = log_x[keep], log_y[keep]
    ax.plot(10.0**log_x, 10.0**log_y, "+", color="0.6", ms=7, mew=1.4,
            ls="none", label="Numerical dynamo simulations", zorder=2)

    line = np.array([1e-2, 1e2])
    ax.plot(line, line, color="black", lw=1.5,
            label="Scaling-law prediction", zorder=3)

    for name, x, y, colour, (dx, dy) in PLANETS:
        ax.plot(x, y, "o", color=colour, ms=11, mec="black", mew=1.0,
                zorder=4)
        ax.annotate(name, (x, y), textcoords="offset points",
                    xytext=(dx, dy), fontsize=11, fontweight="bold",
                    zorder=5)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-2, 1e2)
    ax.set_ylim(1e-2, 1e2)
    ax.set_aspect("equal")
    ax.set_xlabel(r"Predicted dipole field (non-dim.) "
                  r"$\propto \sqrt{\rho \mu_0}\,(F_q D)^{1/3}$")
    ax.set_ylabel("Observed / simulated dipole field (non-dim.)")
    ax.set_title("Convection-driven planetary dynamos:\n"
                 "scaling of dipole field with buoyancy flux and shell thickness")
    ax.legend(loc="upper left", frameon=True)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
