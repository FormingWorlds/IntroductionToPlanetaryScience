"""Generate Fig. (`fig:barometric-profile`).

Isothermal atmospheric pressure profile P(z) / P_0 = exp(-z / H)
versus altitude in scale heights z / H from 0 to 6 in two panels:
(a) linear vertical axis showing steep exponential decay, and
(b) logarithmic vertical axis showing the linear decay in log space.
Both panels mark z = H (1/e approx 0.37), z = 2H (0.135), z = 3H,
and z = 4.6 H (below which 99% of atmospheric column mass sits).

Citations and provenance:
- Markdown source: book/05_atmospheres_1/atmospheres_1.md
  Heading: "The barometric formula"
- Equation of profile: book/05_atmospheres_1/atmospheres_1.md
  "P(z) = P_0 exp(-z/H)" (eq:barometric-formula)
- Scale height definition: book/05_atmospheres_1/atmospheres_1.md
  "H = kB T / (mu m_u g)" (eq:scale-height-preview)
- Numerical factors: book/05_atmospheres_1/atmospheres_1.md
  "Every scale height H, the pressure drops by a factor of e approx 2.718."
  "for an isothermal column, 99% of the mass lies below 4.6 H"
- Column mass relation: book/05_atmospheres_1/atmospheres_1.md
  "P_0 = m_col g, where m_col = int_0^infty rho dz is the column mass."
- Specification:
  "Plot P(z)/P0 = exp(-z/H) versus z/H from 0 to 6 on a linear axis
  (left panel) and on a log axis (right panel); mark z = H (1/e = 0.37),
  z = 2H (0.135), z = 3H, and the level below which 99 percent of the
  mass sits (z = 4.6 H) with dotted lines and labels; annotate that the
  fraction of column mass above z equals P(z)/P0."

Caption / figure id : `fig:barometric-profile`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/barometric_profile.avif"

BLUE = "#1f77b4"
LINE_GRAY = "0.55"


def panel_a(ax: plt.Axes) -> None:
    """Plot the isothermal barometric profile on a linear vertical axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axis for the linear pressure profile.
    """
    z = np.linspace(0.0, 6.0, 400)
    p = np.exp(-z)

    ax.plot(z, p, color=BLUE, lw=2.0)
    ax.fill_between(z, 0, p, color=BLUE, alpha=0.08)

    # Key levels specified by the subsection text and sketch instructions
    levels = [
        (1.0, np.exp(-1.0)),
        (2.0, np.exp(-2.0)),
        (3.0, np.exp(-3.0)),
        (4.6, np.exp(-4.6)),
    ]

    for zv, pv in levels:
        ax.plot([zv, zv], [0.0, pv], color=LINE_GRAY, linestyle=":", lw=1.0)
        ax.plot([0.0, zv], [pv, pv], color=LINE_GRAY, linestyle=":", lw=1.0)
        ax.plot(zv, pv, "o", color=BLUE, ms=5)

    ax.annotate(r"$z = H$ ($1/e \approx 0.37$)", xy=(1.0, np.exp(-1.0)),
                xytext=(1.4, 0.52), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
    ax.annotate(r"$z = 2H$ (0.135)", xy=(2.0, np.exp(-2.0)),
                xytext=(2.3, 0.34), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
    ax.annotate(r"$z = 3H$", xy=(3.0, np.exp(-3.0)),
                xytext=(3.4, 0.21), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
    ax.annotate(r"$z = 4.6\,H$" + "\n(99% mass below)", xy=(4.6, np.exp(-4.6)),
                xytext=(4.3, 0.22), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))

    ax.text(2.1, 0.78, "Fraction of column mass\nabove $z$ equals $P(z)/P_0$",
            fontsize=10,
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#f4f7fa",
                      edgecolor="#b0c4de", alpha=0.9))

    ax.set_xlim(0.0, 6.0)
    ax.set_ylim(0.0, 1.05)
    ax.set_xlabel(r"Altitude $z / H$")
    ax.set_ylabel(r"Pressure ratio $P(z) / P_0$")
    ax.set_title("(a) Linear scale", fontsize=11)


def panel_b(ax: plt.Axes) -> None:
    """Plot the isothermal barometric profile on a logarithmic vertical axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axis for the logarithmic pressure profile.
    """
    z = np.linspace(0.0, 6.0, 400)
    p = np.exp(-z)

    ax.plot(z, p, color=BLUE, lw=2.0)
    ax.set_yscale("log")

    # Key levels specified by the subsection text and sketch instructions
    levels = [
        (1.0, np.exp(-1.0)),
        (2.0, np.exp(-2.0)),
        (3.0, np.exp(-3.0)),
        (4.6, np.exp(-4.6)),
    ]

    for zv, pv in levels:
        ax.plot([zv, zv], [4e-3, pv], color=LINE_GRAY, linestyle=":", lw=1.0)
        ax.plot([0.0, zv], [pv, pv], color=LINE_GRAY, linestyle=":", lw=1.0)
        ax.plot(zv, pv, "o", color=BLUE, ms=5)

    ax.annotate(r"$z = H$ ($1/e \approx 0.37$)", xy=(1.0, np.exp(-1.0)),
                xytext=(1.4, 0.45), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
    ax.annotate(r"$z = 2H$ (0.135)", xy=(2.0, np.exp(-2.0)),
                xytext=(2.4, 0.16), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
    ax.annotate(r"$z = 3H$", xy=(3.0, np.exp(-3.0)),
                xytext=(3.4, 0.055), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
    ax.annotate(r"$z = 4.6\,H$" + "\n(99% mass below)", xy=(4.6, np.exp(-4.6)),
                xytext=(2.3, 0.0021), fontsize=10,
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))

    ax.set_xlim(0.0, 6.0)
    ax.set_ylim(1e-3, 1.5)
    ax.set_xlabel(r"Altitude $z / H$")
    ax.set_ylabel(r"Pressure ratio $P(z) / P_0$")
    ax.set_title("(b) Logarithmic scale", fontsize=11)


def make_plot() -> Path:
    """Build and save the two-panel barometric profile figure.

    Returns
    -------
    pathlib.Path
        Path to the saved AVIF image.
    """
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
    panel_a(axes[0])
    panel_b(axes[1])
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Execute figure generation and save the output AVIF."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()