"""Generate Fig. (`fig:moon-nearside`).

Annotated LROC Wide Angle Camera mosaic of the lunar nearside
(NASA/GSFC/Arizona State University, PIA14011, public domain).
Arrows point at the bright anorthositic highlands crust, the dark
basaltic maria, and Mare Tranquillitatis with the Apollo 11 landing
site. The source image is downloaded once into
output_files/source_images/ and reused on later runs.

Caption / figure id : `fig:moon-nearside`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : Wood1970
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/"
            "moon_nearside_annotated.avif")
SRC = REPO_ROOT / "output_files/source_images/PIA14011.jpg"
SRC_URL = "https://images-assets.nasa.gov/image/PIA14011/PIA14011~orig.jpg"


def fetch_source() -> Path:
    if not SRC.exists():
        SRC.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(SRC_URL, SRC)
    return SRC


def label(ax, text, color, xy_text, xy_tail, xy_tip, ha):
    ax.annotate(text, xy=xy_text, ha=ha, va="top",
                fontsize=11, color=color)
    ax.annotate("", xy=xy_tip, xytext=xy_tail,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5))


def make_plot() -> Path:
    apply_style()
    img = Image.open(fetch_source())

    fig, ax = plt.subplots(figsize=(7.4, 7.4))
    ax.imshow(img, cmap="gray")

    # Dark basaltic maria: Mare Imbrium, upper left
    label(ax, "basaltic maria\n(later lava flows)", "#c9c9d6",
          (35, 40), (200, 135), (467, 358), "left")
    # Apollo 11 site at the south-western edge of Mare Tranquillitatis
    label(ax, "Mare Tranquillitatis\n(Apollo 11, 1969)", "#e8c04a",
          (1365, 40), (1190, 135), (977, 692), "right")
    # Bright anorthositic highlands, southern hemisphere
    label(ax, "anorthositic highlands crust\n(bright, floated plagioclase)",
          "#efe9d8", (1365, 1300), (1150, 1295), (830, 1120), "right")

    ax.set_xlim(0, img.size[0])
    ax.set_ylim(img.size[1], 0)
    ax.axis("off")
    fig.tight_layout(pad=0.15)
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
