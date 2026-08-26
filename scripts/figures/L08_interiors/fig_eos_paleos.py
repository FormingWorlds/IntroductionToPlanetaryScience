"""Generate Fig. (`fig:eos-paleos`).

Density as a function of pressure for the three canonical planet-building
materials, iron, MgSiO3 silicate, and water, from the PALEOS multiphase
equation-of-state tables of Attia et al. (2026). Each panel shows two
isotherms (300 K and 4000 K) spanning conditions from a small rocky body
to the deep interior of a giant planet, with the stable phase labelled
along each curve and Earth's central pressure marked for scale.

The plot reads only the committed sidecar `data/eos_paleos.json`.
The sidecar is extracted from the PALEOS pressure-temperature lookup
tables (Zenodo, doi:10.5281/zenodo.19000316) by `build_data()`:

    .venv/bin/python -m scripts.figures.L08_interiors.fig_eos_paleos \
        --rebuild <dir with paleos_*_eos_table_pt.dat>

Caption / figure id : `fig:eos-paleos`
Markdown source     : book/08_interiors/interiors.md
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/eos_paleos.avif"
DATA_FILE = Path(__file__).resolve().parent / "data/eos_paleos.json"

MATERIALS = ["iron", "mgsio3", "water"]
PANEL_TITLES = {"iron": "Iron", "mgsio3": r"Silicate (MgSiO$_3$)",
                "water": r"Water (H$_2$O)"}
TABLE_FILES = {m: f"paleos_{m}_eos_table_pt.dat" for m in MATERIALS}

# Isotherm targets: cold surface-like vs deep-interior temperature
T_TARGETS = [300.0, 4000.0]
# Pressure window: ~0.1 GPa (small-body interiors) to 1e4 GPa (giant planets)
P_MIN, P_MAX = 1.0e8, 1.2e13
DOWNSAMPLE = 3
P_EARTH_CENTRE = 3.64e11    # Pa, PREM central pressure

COLD_COLOR = "#1f77b4"
HOT_COLOR = "#d62728"
EARTH_COLOR = "#555555"


def build_data(table_dir: str | Path) -> Path:
    """Extract the plotted isotherms from the PALEOS lookup tables.

    Parameters
    ----------
    table_dir : str or Path
        Directory holding the three `paleos_*_eos_table_pt.dat` tables
        from Zenodo record doi:10.5281/zenodo.19000316.

    Returns
    -------
    Path
        The written JSON sidecar (`DATA_FILE`).
    """
    table_dir = Path(table_dir)
    out = {
        "source": "PALEOS P-T lookup tables, Attia et al. (2026)",
        "doi": "10.5281/zenodo.19000316",
        "pressure_window_Pa": [P_MIN, P_MAX],
        "materials": {},
    }
    for mat in MATERIALS:
        fn = table_dir / TABLE_FILES[mat]
        P, T, rho = np.loadtxt(fn, usecols=(0, 1, 2), unpack=True)
        phase = np.loadtxt(fn, usecols=(9,), dtype=str)
        t_grid = np.unique(T)
        isotherms = []
        for t_target in T_TARGETS:
            # nearest grid temperature in log space, matching the table's
            # log-uniform T grid
            t_near = t_grid[np.argmin(np.abs(np.log10(t_grid)
                                             - np.log10(t_target)))]
            m = (T == t_near) & (P >= P_MIN) & (P <= P_MAX)
            if not m.any():
                raise ValueError(
                    f"{mat}: no table rows at T = {t_near} K inside "
                    f"[{P_MIN:.3g}, {P_MAX:.3g}] Pa"
                )
            order = np.argsort(P[m])
            p_iso, r_iso, ph_iso = P[m][order], rho[m][order], phase[m][order]
            # contiguous same-phase runs at full resolution, for labels
            runs, i0 = [], 0
            for i in range(1, len(ph_iso)):
                if ph_iso[i] != ph_iso[i - 1]:
                    runs.append({"phase": ph_iso[i0],
                                 "P_min": float(p_iso[i0]),
                                 "P_max": float(p_iso[i - 1])})
                    i0 = i
            runs.append({"phase": ph_iso[i0], "P_min": float(p_iso[i0]),
                         "P_max": float(p_iso[-1])})
            keep = np.unique(np.r_[np.arange(0, len(p_iso), DOWNSAMPLE),
                                   len(p_iso) - 1])
            isotherms.append({
                "T_K": float(t_near),
                "P_Pa": [float(f"{v:.6g}") for v in p_iso[keep]],
                "rho_kgm3": [float(f"{v:.6g}") for v in r_iso[keep]],
                "phase_runs": runs,
            })
        out["materials"][mat] = {"isotherms": isotherms}
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(out, indent=1))
    return DATA_FILE


PHASE_LABELS = {
    "solid-alpha-bcc": r"$\alpha$-Fe",
    "solid-epsilon-hcp": r"$\varepsilon$-Fe",
    "solid-lpcen": "cen",
    "solid-hpcen": "hpcen",
    "solid-brg": "brg",
    "solid-ppv": "ppv",
    "solid-ice-VI": "VI",
    "solid-ice-VII": "ice VII",
    "solid-ice-X": "ice X",
    "liquid": "liquid",
    "supercritical": "supercritical fluid",
}


# Along-run position fraction per isotherm role and phase ID, overriding
# the default placement where a label would sit on the Earth-centre marker
POS_FRAC = {
    "mgsio3": {"cold": {"solid-ppv": 0.62}},
    "water": {"cold": {"solid-ice-X": 0.78},
              "hot": {"supercritical": 0.25}},
}

# Extra perpendicular clearance in points for labels whose curve bends
# strongly, where the straight-tangent offset underestimates the gap
PAD_EXTRA = {
    "water": {"hot": {"supercritical": 8.0}},
}


def _label_runs(ax, iso: dict, color: str, above: bool,
                min_decades: float = 0.45,
                frac_overrides: dict[str, float] | None = None,
                pad_overrides: dict[str, float] | None = None) -> None:
    """Label each phase run of one isotherm at its geometric-mean pressure.

    Cold-isotherm labels go above the curve and hot-isotherm labels below
    it: the cold curve is the denser (upper) branch everywhere, so both
    regions are free of the other curve. Each label is offset perpendicular
    to the local curve direction in display space, far enough that its own
    text box clears the curve even on the steep high-pressure branch.
    """
    p = np.array(iso["P_Pa"])
    r = np.array(iso["rho_kgm3"])
    fontsize = 8.5
    for run in iso["phase_runs"]:
        p0, p1 = run["P_min"], run["P_max"]
        if np.log10(p1 / p0) < min_decades:
            continue
        text = PHASE_LABELS.get(run["phase"], run["phase"])
        # above-curve labels sit toward the low-P end of their run, keeping
        # them clear of the steep high-P region where the isotherms merge
        frac = 0.42 if above else 0.5
        if frac_overrides:
            frac = frac_overrides.get(run["phase"], frac)
        pm = p0 * (p1 / p0) ** frac
        rm = np.interp(np.log10(pm), np.log10(p), r)
        # local curve direction in display coordinates
        pa, pb = pm * 0.85, pm * 1.18
        ra = np.interp(np.log10(pa), np.log10(p), r)
        rb = np.interp(np.log10(pb), np.log10(p), r)
        (xa, ya), (xb, yb) = ax.transData.transform(
            [(pa / 1e9, ra), (pb / 1e9, rb)])
        dx, dy = xb - xa, yb - ya
        norm = np.hypot(dx, dy)
        nx, ny = (-dy / norm, dx / norm) if above else (dy / norm, -dx / norm)
        # clearance: project the label's half-extent onto the normal
        half_w = 0.5 * len(text) * fontsize * 0.62
        half_h = 0.62 * fontsize
        pad = 4.0
        if pad_overrides:
            pad += pad_overrides.get(run["phase"], 0.0)
        off = abs(nx) * half_w + abs(ny) * half_h + pad
        ax.annotate(text, (pm / 1e9, rm), textcoords="offset points",
                    xytext=(nx * off, ny * off), fontsize=fontsize,
                    color=color, ha="center", va="center",
                    bbox=dict(fc="white", ec="none", alpha=0.65, pad=0.4))


def make_plot() -> Path:
    apply_style()
    data = json.loads(DATA_FILE.read_text())
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.9))

    for ax, mat in zip(axes, MATERIALS):
        isos = data["materials"][mat]["isotherms"]
        cold, hot = isos[0], isos[1]
        for iso, color, ls in [(cold, COLD_COLOR, "-"),
                               (hot, HOT_COLOR, "--")]:
            p_gpa = np.array(iso["P_Pa"]) / 1e9
            ax.plot(p_gpa, iso["rho_kgm3"], ls, color=color, lw=1.8,
                    label=f"{iso['T_K']:.0f} K")
            # phase-boundary markers as short vertical bars on the curve
            for run in iso["phase_runs"][:-1]:
                pb = run["P_max"] / 1e9
                rb = np.interp(np.log10(pb), np.log10(p_gpa),
                               iso["rho_kgm3"])
                ax.plot(pb, rb, "|", color=color, ms=9, mew=1.4)
        ax.axvline(P_EARTH_CENTRE / 1e9, color=EARTH_COLOR, lw=1.0,
                   linestyle=":", zorder=1)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(P_MIN / 1e9, P_MAX / 1e9)
        rho_all = np.r_[cold["rho_kgm3"], hot["rho_kgm3"]]
        # bottom margin leaves room for the below-curve phase labels
        ax.set_ylim(rho_all.min() * 0.68, rho_all.max() * 1.2)
        ax.set_title(PANEL_TITLES[mat], fontsize=11)
        ax.set_xlabel("Pressure [GPa]")
        ax.legend(loc="upper left", frameon=False)
        # label after scales and limits are set: the perpendicular offsets
        # in _label_runs use the display-space transform
        _label_runs(ax, cold, COLD_COLOR, above=True,
                    frac_overrides=POS_FRAC.get(mat, {}).get("cold"),
                    pad_overrides=PAD_EXTRA.get(mat, {}).get("cold"))
        _label_runs(ax, hot, HOT_COLOR, above=False,
                    frac_overrides=POS_FRAC.get(mat, {}).get("hot"),
                    pad_overrides=PAD_EXTRA.get(mat, {}).get("hot"))
    axes[0].set_ylabel(r"Density [kg m$^{-3}$]")
    # above the iron curve at 364 GPa, in the clear upper-left region
    axes[0].text(P_EARTH_CENTRE / 1e9 * 1.3, 2.4e4, "Earth centre",
                 rotation=90, fontsize=8, color=EARTH_COLOR, va="center")

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rebuild", metavar="TABLE_DIR",
                        help="re-extract data/eos_paleos.json from the "
                             "PALEOS tables in TABLE_DIR")
    args = parser.parse_args()
    if args.rebuild:
        print(f"  data : {build_data(args.rebuild)}")
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
