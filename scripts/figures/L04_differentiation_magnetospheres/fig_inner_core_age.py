"""The inner-core age debate on one timeline.

Two lines of evidence place the nucleation of Earth's inner core within
the past 0.5 to 1 Gyr: the high thermal conductivity of iron (Labrosse
2015) and the rise of the dipole field strength in the paleomagnetic
record (Nimmo 2015). Before that the geodynamo ran on thermal
convection alone.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/inner_core_age.avif"


def make_plot() -> plt.Figure:
    """Build the timeline, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(9.0, 3.8))
    ax.add_patch(Rectangle((0.54, 2.2), 4.0, 0.5, facecolor="#f4a261", alpha=0.6, edgecolor="none"))
    ax.text(2.54, 2.45, "thermally driven geodynamo", ha="center", va="center", fontsize=10)
    ax.add_patch(Rectangle((0.0, 2.2), 0.54, 0.5, facecolor="#7fb3d5", alpha=0.7, edgecolor="none"))
    ax.text(0.27, 2.45, "compositional\nconvection", ha="center", va="center", fontsize=9)
    ax.plot([1.0, 0.5], [1.15, 1.15], color="#c0392b", lw=4.0, solid_capstyle="butt")
    ax.text(1.08, 1.15, "inner-core age from the thermal conductivity of iron:\n0.5 to 1 Gyr (Labrosse 2015)", ha="right", va="center", fontsize=10, color="#c0392b")
    ax.plot([1.0, 0.5], [0.45, 0.45], color="#1f6db8", lw=4.0, solid_capstyle="butt")
    ax.text(1.08, 0.45, "dipole strength rises 0.5 to 1.0 Ga:\nonset of inner-core nucleation (Nimmo 2015)", ha="right", va="center", fontsize=10, color="#1f6db8")
    ax.plot([0.54, 0.54], [0.1, 2.15], color="0.2", lw=1.0, ls="--")
    ax.text(0.58, 1.9, "nucleation, 0.54 Ga", ha="right", va="bottom", fontsize=10)
    ax.text(4.50, 2.8, "Earth forms", ha="left", va="bottom", fontsize=10)
    ax.plot([4.54, 4.54], [0.1, 2.75], color="0.2", lw=1.0, ls="--")
    ax.set_xlim(4.7, -0.05)
    ax.set_ylim(0, 3.2)
    ax.set_yticks([])
    ax.set_xlabel("Time before present (Ga)")
    ax.set_title("When did Earth's inner core nucleate?", fontsize=11)
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
