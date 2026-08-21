"""Generate Fig. (`fig:fulton-radius-valley`).

Annotated reproduction of the completeness-corrected planet radius
histogram of Fulton et al. (2017), their Fig. 7 (top panel), from the
authors' arXiv source (1703.10375, file radius_dist_cks_naked.pdf,
kept verbatim in `data/`). The original panel is rendered to pixels,
the axes are calibrated from the printed tick positions, and three
labels (super-Earths, sub-Neptunes, radius valley) are drawn on top
in data coordinates.

Caption / figure id : `fig:fulton-radius-valley`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation key        : Fulton2017
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pymupdf

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
SRC_PDF = Path(__file__).resolve().parent / "data/fulton2017_radius_dist_cks_naked.pdf"
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/fulton2017_radius_valley.avif"

DPI = 200

# Printed tick values of the original panel: radius in Earth radii
# (log axis) and occurrence per star (linear axis, top to bottom).
X_TICK_VALUES = [0.7, 1.0, 1.3, 1.8, 2.4, 3.5, 4.5, 6.0, 8.0, 12.0, 20.0]
Y_TICK_VALUES = [0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0.00]


def render_panel() -> np.ndarray:
    """Render the original panel PDF to an RGB pixel array."""
    page = pymupdf.open(SRC_PDF)[0]
    pix = page.get_pixmap(dpi=DPI)
    img = np.frombuffer(pix.samples, dtype=np.uint8)
    return img.reshape(pix.height, pix.width, pix.n)[:, :, :3].copy()


def calibrate() -> tuple[np.poly1d, np.poly1d]:
    """Fit data-to-pixel maps from the panel's vector tick strokes.

    The major ticks are the only strokes of their exact length in the
    PDF (8 pt vertical on the bottom spine, 7 pt horizontal on the left
    spine), so they identify the axes without any raster heuristics.
    Returns (x_of_logr, y_of_occ): pixel column as a function of
    log10(radius), pixel row as a function of occurrence.
    """
    page = pymupdf.open(SRC_PDF)[0]
    segs = []
    for d in page.get_drawings():
        for item in d["items"]:
            if item[0] == "l":
                p1, p2 = item[1], item[2]
                segs.append((p1.x, p1.y, p2.x, p2.y))

    # Both opposing spines carry the same tick strokes; dedup by position.
    xticks = sorted({round(s[0], 2) for s in segs
                     if abs(s[0] - s[2]) < 0.01
                     and 7.5 < abs(s[1] - s[3]) < 8.5})
    yticks = sorted({round(s[1], 2) for s in segs
                     if abs(s[1] - s[3]) < 0.01
                     and 6.5 < abs(s[0] - s[2]) < 7.5})
    if len(xticks) != len(X_TICK_VALUES) or len(yticks) != len(Y_TICK_VALUES):
        raise RuntimeError(
            f"tick-stroke detection changed: {len(xticks)} x / "
            f"{len(yticks)} y ticks found; the source PDF differs from "
            "the one this calibration was built for")

    scale = DPI / 72.0  # PDF points to rendered pixels
    xticks = np.array(xticks) * scale
    yticks = np.array(yticks) * scale
    cx = np.polyfit(np.log10(X_TICK_VALUES), xticks, 1)
    cy = np.polyfit(sorted(Y_TICK_VALUES, reverse=True), yticks, 1)
    rx = np.max(np.abs(np.polyval(cx, np.log10(X_TICK_VALUES)) - xticks))
    ry = np.max(np.abs(np.polyval(cy, sorted(Y_TICK_VALUES, reverse=True))
                       - yticks))
    if rx >= 3 or ry >= 3:
        raise RuntimeError(
            f"calibration residual too large (x {rx:.1f} px, y {ry:.1f} px); "
            "tick strokes misidentified in the source PDF")
    return np.poly1d(cx), np.poly1d(cy)


def make_plot() -> Path:
    apply_style()
    img = render_panel()
    x_of_logr, y_of_occ = calibrate()

    def px(radius: float, occ: float) -> tuple[float, float]:
        return float(x_of_logr(np.log10(radius))), float(y_of_occ(occ))

    H, W = img.shape[:2]
    fig, ax = plt.subplots(figsize=(W / DPI, H / DPI))
    ax.imshow(img, interpolation="lanczos")
    ax.set_axis_off()
    ax.grid(False)

    annotations = [
        ("Super-Earths", "#c2452e", (1.31, 0.104), (1.31, 0.0845), "center"),
        ("Sub-Neptunes", "#2c7f8c", (3.9, 0.105), (2.55, 0.096), "center"),
        ("Radius valley", "0.25", (1.7, 0.1155), (1.8, 0.049), "center"),
    ]
    for label, color, text_rp, tip_rp, ha in annotations:
        ax.annotate(label, xy=px(*tip_rp), xytext=px(*text_rp),
                    ha=ha, va="center", fontsize=13, color=color,
                    weight="bold",
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.4))

    ax.set_position([0, 0, 1, 1])
    fig.set_size_inches(W / DPI, H / DPI)
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
