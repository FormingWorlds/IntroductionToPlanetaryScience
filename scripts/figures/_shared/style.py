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


def text_color_on(fill) -> str:
    """Pick black or white label text, whichever gives the higher WCAG
    contrast ratio against the given fill colour."""
    from matplotlib.colors import to_rgb

    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
           for c in to_rgb(fill)]
    lum = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    return "white" if 1.05 / (lum + 0.05) >= (lum + 0.05) / 0.05 else "black"


def save_figure(
    fig: plt.Figure,
    avif_path: str | Path,
    *,
    avif_quality: int = 75,
    keep_png: bool = False,
    dpi: int | None = None,
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
        figures; 75-80 for text/line-heavy plots.
    keep_png
        Keep the intermediate PNG alongside the AVIF if True.
    dpi
        Render resolution. Defaults to the 200 dpi in `apply_style`. Raise it
        for a figure that also appears full-width on a slide, where 200 dpi
        leaves fewer pixels than the projector paints.
    """
    avif = Path(avif_path)
    avif.parent.mkdir(parents=True, exist_ok=True)
    png = avif.with_suffix(".png")
    fig.savefig(png, **({"dpi": dpi} if dpi else {}))
    _crop_to_even(png)
    _encode_avif(png, avif, avif_quality)
    if not keep_png:
        png.unlink(missing_ok=True)
    return avif


def _crop_to_even(png: Path) -> None:
    """Trim an odd width or height by one pixel before the AVIF encode.

    AV1 encodes 4:2:0 frames in even dimensions; an odd PNG comes back with a
    dark padding column or row on its right or bottom edge that renders as a
    grey bar in the browser and on the slides. The trimmed pixel is the tight
    bbox margin, so no content is lost.
    """
    from PIL import Image

    with Image.open(png) as im:
        w, h = im.size
        if w % 2 == 0 and h % 2 == 0:
            return
        im.crop((0, 0, w - w % 2, h - h % 2)).save(png)


def _is_avif(path: Path) -> bool:
    """True if the file really contains AVIF bytes (ftyp brand at offset 4)."""
    with open(path, "rb") as fh:
        head = fh.read(32)
    return b"ftyp" in head[:16] and (b"avif" in head or b"avis" in head)


def _encode_avif(png: Path, avif: Path, quality: int) -> None:
    """Encode PNG to AVIF and verify the result; magick first, ffmpeg fallback.

    A broken heif delegate makes magick write non-AVIF bytes under the .avif
    name with exit status 0, so the bytes are checked rather than the status.
    """
    if shutil.which("magick"):
        subprocess.call(
            ["magick", str(png), "-quality", str(quality),
             "-define", "avif:effort=6", str(avif)],
            stderr=subprocess.DEVNULL,
        )
        if avif.exists() and _is_avif(avif):
            return
    if not shutil.which("ffmpeg"):
        raise RuntimeError("no working AVIF encoder: magick failed and ffmpeg is missing")
    crf = max(0, min(63, 63 - int(quality * 0.6)))
    subprocess.check_call(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(png),
         "-c:v", "libsvtav1", "-crf", str(crf), "-frames:v", "1",
         "-f", "avif", str(avif)],
    )
    if not _is_avif(avif):
        raise RuntimeError(f"AVIF encode produced non-AVIF bytes: {avif}")
