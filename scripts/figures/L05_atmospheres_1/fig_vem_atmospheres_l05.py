"""Generate the Lecture 5 copy of `fig:vem-atmospheres` (`fig:l05-vem-atmospheres`).

Same plot as the Lecture 1 figure, drawn from the shared planet table in
scripts/figures/L01_introduction/data/solar_system_planets.csv, written to
the Lecture 5 figure folder.
"""

from __future__ import annotations

from pathlib import Path

from scripts.figures._shared import style
from scripts.figures.L01_introduction import fig_vem_atmospheres as base

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/venus_earth_mars_atmospheres.avif"


def make_plot() -> Path:
    """Draw the Lecture 1 plot into the Lecture 5 figure path."""
    base.OUT_AVIF = OUT_AVIF
    base.save_figure = style.save_figure
    return base.make_plot()


def main() -> None:
    """Generate the figure and report its path."""
    print(f"  plot : {make_plot()}")


if __name__ == "__main__":
    main()
