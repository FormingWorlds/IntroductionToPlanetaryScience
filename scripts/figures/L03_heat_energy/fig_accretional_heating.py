"""Accretional heating against body size.

Left: the gravitational energy released in assembling a uniform sphere,
E_acc = 3/5 G M^2/R, for bodies of Earth's mean density. Right: the
temperature rise E_acc/(M c_p) if all of it were retained, with Earth's
value from the notes marked. Both scale as R^2 per unit mass, so small
bodies gain little heat from accretion and large ones melt.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/accretional_heating.avif"

G = 6.674e-11
M_EARTH = 5.97e24  # kg, as in the notes
R_EARTH = 6.37e6  # m, as in the notes
C_P = 1200.0  # J/kg/K, as in the notes
RHO = M_EARTH / (4.0 / 3.0 * np.pi * R_EARTH**3)


def make_plot() -> plt.Figure:
    """Build the two-panel figure, save it and return it."""
    apply_style()
    r = np.logspace(5, np.log10(8e6), 200)
    m = 4.0 / 3.0 * np.pi * RHO * r**3
    e_acc = 0.6 * G * m**2 / r
    dt = e_acc / (m * C_P)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.0))
    ax1.loglog(r / 1e3, e_acc, color="#1f6db8", lw=2.2)
    ax1.plot(R_EARTH / 1e3, 0.6 * G * M_EARTH**2 / R_EARTH, "o", color="#c0392b", ms=8, zorder=5)
    ax1.annotate(r"Earth: $2.2 \times 10^{32}$ J", xy=(R_EARTH / 1e3, 2.2e32), xytext=(160, 1e31),
                 fontsize=10, arrowprops=dict(arrowstyle="->", color="0.3", lw=0.9))
    ax1.set_xlabel("Body radius (km)")
    ax1.set_ylabel(r"$E_{\mathrm{acc}} = \frac{3}{5}\,G M^2 / R$ (J)")
    ax1.set_title("(a) Energy released by accretion", fontsize=11)
    ax1.text(250, 1e24, r"uniform sphere at Earth's mean density: $E_{\mathrm{acc}} \propto R^5$", fontsize=10, color="0.3")
    ax2.loglog(r / 1e3, dt, color="#1f6db8", lw=2.2)
    ax2.plot(R_EARTH / 1e3, 0.6 * G * M_EARTH / (R_EARTH * C_P), "o", color="#c0392b", ms=8, zorder=5)
    ax2.annotate(r"Earth: $\approx 30\,000$ K", xy=(R_EARTH / 1e3, 3.0e4), xytext=(300, 2e4),
                 fontsize=10, arrowprops=dict(arrowstyle="->", color="0.3", lw=0.9))
    ax2.set_xlabel("Body radius (km)")
    ax2.set_ylabel(r"$\Delta T = E_{\mathrm{acc}} / (M c_p)$ (K)")
    ax2.set_title("(b) Temperature rise if all heat is retained", fontsize=11)
    ax2.set_ylim(3, 1e5)
    ax2.text(250, 8, r"$c_p = 1200$ J kg$^{-1}$ K$^{-1}$; $\Delta T \propto R^2$", fontsize=10, color="0.3")
    fig.tight_layout()
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
