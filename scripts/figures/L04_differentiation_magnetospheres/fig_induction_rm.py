"""The induction equation and the magnetic Reynolds number.

Left: the two terms of the induction equation, advection and diffusion,
and their ratio Rm = U L / eta. Right: Rm for Earth's outer core against
the flow speed, with the critical range Rm_c of 10 to 100 shaded and the
lecture's estimate of about 1750 at U = 5e-4 m/s marked.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/induction_rm.avif"

L_CORE = 3.5e6  # m, outer-core shell thickness used in the lecture estimate
ETA = 1.0  # m^2/s, magnetic diffusivity of liquid iron used in the lecture
U_EARTH = 5e-4  # m/s


def make_plot() -> plt.Figure:
    """Build the two-panel figure, save it and return it."""
    apply_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.50, 3.57), gridspec_kw={"width_ratios": [1.15, 1.0]})
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 6)
    ax1.axis("off")
    ax1.set_title("(a) The induction equation", fontsize=11)
    ax1.text(5.0, 5.35, r"$\dfrac{\partial \vec{B}}{\partial t} = \nabla \times (\vec{v} \times \vec{B}) + \eta \nabla^2 \vec{B}$", ha="center", va="center", fontsize=14)
    for x, fc, ec, title, body in ((2.5, "#fdebd0", "#c46b1a", "advection", "flow stretches and\nfolds field lines:\namplification, $\\sim U B / L$"),
                                    (7.5, "#e8f1fa", "#4a6984", "diffusion", "ohmic resistance lets\nthe field decay,\n$\\sim \\eta B / L^2$")):
        ax1.add_patch(FancyBboxPatch((x - 2.45, 1.35), 4.9, 2.75, boxstyle="round,pad=0.05,rounding_size=0.2", facecolor=fc, edgecolor=ec, lw=1.2))
        ax1.text(x, 3.7, title, ha="center", va="center", fontsize=11, weight="bold", color=ec)
        ax1.text(x, 2.5, body, ha="center", va="center", fontsize=10)
    ax1.add_patch(FancyArrowPatch((3.6, 4.7), (2.7, 4.2), arrowstyle="-|>", mutation_scale=10, color="0.3", lw=1.0))
    ax1.add_patch(FancyArrowPatch((7.0, 4.7), (7.3, 4.2), arrowstyle="-|>", mutation_scale=10, color="0.3", lw=1.0))
    ax1.text(5.0, 0.6, r"$\mathrm{Rm} = \dfrac{\text{advection}}{\text{diffusion}} = \dfrac{U L}{\eta}$;  a dynamo needs $\mathrm{Rm} \gtrsim \mathrm{Rm}_c \sim 10$ to $100$", ha="center", va="center", fontsize=11)
    u = np.logspace(-6, -2, 200)
    ax2.loglog(u, u * L_CORE / ETA, color="#1f6db8", lw=2.2, label=r"$\mathrm{Rm} = UL/\eta$")
    ax2.axhspan(10, 100, color="#f4a261", alpha=0.35, label=r"$\mathrm{Rm}_c \sim 10$ to $100$")
    ax2.plot(U_EARTH, U_EARTH * L_CORE / ETA, "o", color="#c0392b", ms=8, zorder=5)
    ax2.annotate("Earth's outer core:\n" + r"$U \approx 5 \times 10^{-4}$ m s$^{-1}$" + "\n" + r"$\mathrm{Rm} \approx 1750$", xy=(U_EARTH, 1750), xytext=(1.2e-6, 8e3), fontsize=10, arrowprops=dict(arrowstyle="->", color="0.3", lw=0.9))
    ax2.set_xlabel(r"Flow speed $U$ (m s$^{-1}$)")
    ax2.set_ylabel(r"Magnetic Reynolds number $\mathrm{Rm}$")
    ax2.set_ylim(1, 1e5)
    ax2.legend(loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=2, fontsize=9, frameon=False)
    ax2.set_title("(b) Rm for Earth's outer core", fontsize=11)
    fig.tight_layout()
    save_figure(fig, OUT_AVIF, dpi=280)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
