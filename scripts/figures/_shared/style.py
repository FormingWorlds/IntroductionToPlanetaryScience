"""Shared matplotlib style for all course figures.

Keeps the visual identity of the lecture notes consistent: serif math,
sans-serif labels, mid-density grid, no top/right spines unless needed,
and a 200-dpi PNG-then-AVIF pipeline that matches the figure_triage.py
expectations (native pixel width >= declared :width: in MyST).

Use:
    from scripts.figures._shared.style import apply_style, save_figure
    apply_style()
    fig, ax = plt.subplots(...)
    ...
    save_figure(fig, "book/01_introduction/figures/<name>.avif")
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

# Detection-method colour palette used across L01 / L13 exoplanet figures.
METHOD_COLORS = {
    "Transit":             "#1f77b4",  # blue
    "Radial Velocity":     "#d62728",  # red
    "Imaging":             "#2ca02c",  # green
    "Microlensing":        "#9467bd",  # purple
    "Transit Timing Variations": "#ff7f0e",  # orange
    "Eclipse Timing Variations": "#bcbd22",  # olive
    "Astrometry":          "#17becf",  # cyan
    "Pulsar Timing":       "#8c564b",  # brown
    "Pulsation Timing Variations": "#e377c2",  # pink
    "Orbital Brightness Modulation": "#7f7f7f",  # grey
    "Disk Kinematics":     "#666666",
    "Other":               "#888888",
}


def apply_style() -> None:
    """Set matplotlib rcParams for course figures."""
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans"],
        "mathtext.fontset": "dejavuserif",
        "axes.labelsize": 11,
        "axes.titlesize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.linestyle": ":",
        "grid.alpha": 0.3,
        "figure.dpi": 200,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.facecolor": "white",
    })


def save_figure(
    fig: plt.Figure,
    avif_path: str | Path,
    *,
    avif_quality: int = 75,
    keep_png: bool = False,
) -> Path:
    """Save figure as a high-resolution PNG, convert to AVIF, return AVIF path.

    Parameters
    ----------
    fig
        The matplotlib figure to save.
    avif_path
        Final AVIF path (typically `book/<lecture>/figures/<name>.avif`).
    avif_quality
        AVIF q parameter. 65 is the project default for photographic
        figures; 75–80 for text/line-heavy plots.
    keep_png
        Keep the intermediate PNG alongside the AVIF if True.
    """
    avif = Path(avif_path)
    avif.parent.mkdir(parents=True, exist_ok=True)
    png = avif.with_suffix(".png")
    fig.savefig(png)
    if not shutil.which("magick"):
        raise RuntimeError("ImageMagick `magick` is required to convert PNG to AVIF")
    subprocess.check_call([
        "magick", str(png),
        "-quality", str(avif_quality),
        "-define", "avif:effort=6",
        str(avif),
    ])
    if not keep_png:
        png.unlink(missing_ok=True)
    return avif
