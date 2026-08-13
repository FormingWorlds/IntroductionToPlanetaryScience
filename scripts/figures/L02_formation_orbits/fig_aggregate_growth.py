"""Generate Fig. (`fig:blum-aggregates`).

Brownian-coagulation growth of dust aggregates in microgravity, redrawn
from Blum & Wurm (2008), Fig. 2 (experimental data of Krause & Blum
2004). Main panel: mean aggregate mass in monomer masses against time
in monomer collision timescales, with the monodisperse coagulation
model curve of the source figure. Inset: fractal aggregates of 1.9 um
SiO2 monomers imaged in the space-shuttle experiments of Blum et al.
(2000), reproduced from the same figure.

Both the data points and the model curve are digitized from the
published figure (`data/aggregate_growth_digitized.json` holds the
values and the pixel calibration); the inset photograph is
`data/blum2008_inset.png`.

Caption / figure id : `fig:blum-aggregates`
Markdown source     : book/02_formation_orbits/formation_orbits.md
Citation key        : BlumWurm2008
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
DIGITIZED = DATA_DIR / "aggregate_growth_digitized.json"
INSET = DATA_DIR / "blum2008_inset.png"
OUT_AVIF = REPO_ROOT / "book/02_formation_orbits/figures/blum2008_aggregate_growth.avif"


def make_plot() -> Path:
    apply_style()
    data = json.loads(DIGITIZED.read_text())

    fig, ax = plt.subplots(figsize=(7.4, 6.0))

    curve = np.array(data["model_curve"])
    # The digitized samples wobble where the data markers occlude the curve;
    # a low-order fit in log-log recovers the smooth model line.
    lt, lm = np.log10(curve[:, 0]), np.log10(curve[:, 1])
    fit = np.polynomial.Polynomial.fit(lt, lm, 4)
    resid = np.abs(fit(lt) - lm)
    if resid.max() > 0.03:
        raise RuntimeError(f"curve smoothing residual too large: {resid.max():.3f} dex")
    tt = np.logspace(lt.min(), lt.max(), 300)
    ax.plot(tt, 10 ** fit(np.log10(tt)), color="#2b7bde", lw=2.4, zorder=2,
            label="Monodisperse coagulation model")

    pts = data["points"]
    t = np.array([p["t"] for p in pts])
    m = np.array([p["m"] for p in pts])
    err = np.array([[p["m"] - p["m_lo"] for p in pts],
                    [p["m_hi"] - p["m"] for p in pts]])
    ax.errorbar(t, m, yerr=err, fmt="x", color="#d62728", ms=10, mew=2.4,
                elinewidth=1.4, capsize=4, zorder=3,
                label="Microgravity experiments")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.09, 22)
    ax.set_ylim(1.0, 110)
    ax.set_xlabel(r"$t\,\tau^{-1}$", fontsize=14)
    ax.set_ylabel(r"$\bar{m}(t)\,m_0^{-1}$", fontsize=14)
    ax.tick_params(labelsize=12)
    ax.legend(loc="lower right", frameon=True, framealpha=0.92,
              edgecolor="none", fontsize=11)

    # Aggregate photograph, upper left, clear of curve and data.
    inset = fig.add_axes([0.16, 0.56, 0.36, 0.30])
    inset.imshow(mpimg.imread(INSET))
    inset.set_xticks([])
    inset.set_yticks([])
    for s in inset.spines.values():
        s.set_edgecolor("0.4")
    inset.set_title(r"$\varnothing$ 1.9 $\mu$m SiO$_2$", fontsize=11, pad=4)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  data : {DIGITIZED}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
