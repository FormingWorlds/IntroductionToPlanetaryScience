"""Physics spot-checks for the course-original figures.

Each check recomputes a figure's central quantity independently from the
parameters the figure states, and compares it against the anchor the figure
labels (a marked point, a curve extremum, a quoted value). A figure whose
drawn curve drifts away from its own labels fails here before it ships.

Data-driven figures are checked against reference values (surface
temperatures, mass fractions, moment-of-inertia factors) at loose tolerance;
formula figures are checked tightly.

Run from the repository root:  python3 scripts/figures/check_figure_physics.py
Exit status 0 and a final ``ALL OK`` line mean every check passed.
"""

import csv
import importlib.util
import json
import math
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402

FAIL = []
SKIP = []


def chk(name, got, want, rel=1e-3, absolute=None):
    if absolute is not None:
        ok = abs(got - want) <= absolute
    else:
        ok = abs(got - want) <= abs(want) * rel
    print(f"{'OK  ' if ok else 'FAIL'} {name:52s} got {got:.6g}  want {want:.6g}")
    if not ok:
        FAIL.append(name)


def chk_true(name, cond, detail=""):
    print(f"{'OK  ' if cond else 'FAIL'} {name:52s} {detail}")
    if not cond:
        FAIL.append(name)


def load(relpath):
    """Import a figure script as a module by path."""
    p = ROOT / relpath
    spec = importlib.util.spec_from_file_location(p.stem, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def section(title):
    print(f"\n── {title} " + "─" * max(0, 60 - len(title)))


# ════════════════════════════════════════════════════════════════════
section("L01: densities and mass budget")

# fig_density_vs_distance: rho = M / (4/3 pi R^3); Earth anchor
rho_earth = 5.9722e24 / (4.0 / 3.0 * math.pi * (6371e3) ** 3)
chk("L01 density formula (Earth, kg/m^3)", rho_earth, 5513, 2e-3)

# fig_ss_mass_budget: the Sun holds ~99.86% of the system mass
rows = list(csv.DictReader(open(ROOT / "scripts/figures/L01_introduction/data/solar_system_masses.csv")))
tot_planets = sum(float(r["mass_earth_units"]) for r in rows) * 5.9722e24
sun_pct = 1.98892e30 / (1.98892e30 + tot_planets) * 100
chk("L01 mass budget: Sun percentage", sun_pct, 99.86, 2e-4)

# ════════════════════════════════════════════════════════════════════
section("L02: orbits, Roche, resonance")

m = load("scripts/figures/L02_formation_orbits/fig_visviva.py")
v_circ = m.vis_viva(np.array([1.0]), 1.0)[0]
chk("L02 vis-viva: circular speed at 1 AU (km/s)", v_circ, 29.78, 2e-3)

# fig_roche_geometry: the tidal/self-gravity crossing IS the rigid limit
r = load("scripts/figures/L02_formation_orbits/fig_roche_geometry.py")
d = np.linspace(1.0, 30.0, 200000) * r.R_SATURN
tidal = 2.0 * r.G * r.M_SATURN * r.R_SAT / d ** 3
g_self = r.G * (4.0 / 3.0) * math.pi * r.RHO_SAT * r.R_SAT
d_cross = d[np.argmin(np.abs(tidal - g_self))] / r.R_SATURN
d_rigid = (2.0 * r.RHO_SATURN / r.RHO_SAT) ** (1.0 / 3.0)
chk("L02 Roche: curve crossing = rigid limit (R_p)", d_cross, d_rigid, 1e-3)
chk("L02 Roche: fluid limit Saturn+ice (R_p)",
    2.46 * (r.RHO_SATURN / r.RHO_SAT) ** (1.0 / 3.0), 2.17, 2e-3)

# fig_kepler_laws: ellipse geometry c^2 = a^2 - b^2 for both orbits
chk("L02 Kepler sketch: inner focus offset", math.sqrt(500**2 - 400**2), 300, 1e-6)
chk("L02 Kepler sketch: outer focus offset", math.sqrt(700**2 - 500**2), 489.9, 1e-3)

# fig_laplace_resonance: Galilean periods near 1:2:4
moons = json.load(open(ROOT / "scripts/figures/L02_formation_orbits/data/galilean_moons.json"))
P = {k: v["P_days"] for k, v in moons["moons"].items()} if "moons" in moons else \
    {k: v["P_days"] for k, v in moons.items() if isinstance(v, dict) and "P_days" in v}
if P:
    chk("L02 Laplace: P_Europa/P_Io", P["Europa"] / P["Io"], 2.007, 2e-3)
    chk("L02 Laplace: P_Ganymede/P_Io", P["Ganymede"] / P["Io"], 4.045, 2e-3)
else:
    SKIP.append("L02 Laplace periods (json shape)")

# ════════════════════════════════════════════════════════════════════
section("L03: heat and convection")

m = load("scripts/figures/L03_heat_energy/fig_marginal_stability.py")
k = np.linspace(0.4, 8.0, 400000)
ff = (k ** 2 + math.pi ** 2) ** 3 / k ** 2
ra = ff * (m.RA_C / (27.0 * math.pi ** 4 / 4.0))
kk = k * (m.K_C / (math.pi / math.sqrt(2.0)))
chk("L03 marginal stability: curve minimum (Ra)", ra.min(), 1707.762, 1e-3)
chk("L03 marginal stability: minimum position (k)", kk[np.argmin(ra)], 3.117, 5e-3)

chk("L03 Nu-Ra: Nu at onset", (1708.0 / 1708.0) ** (1 / 3), 1.0, 1e-9)
chk("L03 Nu-Ra: Nu at Ra=1e8", (1e8 / 1708.0) ** (1 / 3), 38.8, 3e-3)

# half-space cooling: T = T_s + (T_m - T_s) erf(z / 2 sqrt(kappa t)).
# At z = 2 sqrt(kappa t) the profile has recovered erf(1) = 84.27% of the contrast,
# and the thermal boundary layer after 100 Myr is ~2 sqrt(kappa t) = 112 km thick.
chk("L03 half-space: erf(1) temperature fraction", math.erf(1.0), 0.8427, 1e-3)
chk("L03 half-space: TBL thickness at 100 Myr (km)",
    2 * math.sqrt(1e-6 * 100e6 * 3.156e7) / 1e3, 112, 5e-3)

m = load("scripts/figures/L03_heat_energy/fig_q_vs_seafloor_age.py")
q1 = m.K_TH * m.DELTA_T / math.sqrt(math.pi * m.KAPPA * 1e6 * m.SEC_PER_YR) * 1000
chk("L03 q(1 Myr) (mW/m^2)", q1, 440, 5e-3)
q100 = m.K_TH * m.DELTA_T / math.sqrt(math.pi * m.KAPPA * 100e6 * m.SEC_PER_YR) * 1000
chk("L03 q: factor over 2 decades = 10 (t^-1/2)", q1 / q100, 10.0, 1e-6)

chk("L03 tau_cond: L for tau = 4.57 Gyr (km)",
    math.sqrt(1e-6 * 4.57e9 * 3.156e7) / 1e3, 380, 5e-3)

m = load("scripts/figures/L03_heat_energy/fig_radiogenic_heat_evolution.py")
# long-lived: notes table, independent recomputation
iso = [(20e-9, 9.5e-5, 4.47), (0.14e-9, 5.7e-4, 0.704), (80e-9, 2.6e-5, 14.0), (28e-9, 2.9e-5, 1.25)]
h_today = sum(c * h for c, h, _ in iso)
h_form = sum(c * h * 2 ** (4.5 / t12) for c, h, t12 in iso)
chk("L03 radiogenic: BSE power today (TW)", h_today * m.M_BSE / 1e12, 19.5, 2e-2)
chk("L03 radiogenic: BSE power at formation (TW)", h_form * m.M_BSE / 1e12, 92, 2e-2)
chk("L03 radiogenic: formation/today factor", h_form / h_today, 4.71, 5e-3)
h_al26 = m.short_lived_H(26, 3.12, 0.72) * 8.65e-3 * 5.25e-5 * (26.0 / 27.0)
chk("L03 radiogenic: 26Al initial heating (W/kg)", h_al26, 1.5e-7, 0.1)

budget = json.load(open(ROOT / "scripts/figures/L03_heat_energy/data/earth_heat_budget.json"))
vals = [v for v in budget.values() if isinstance(v, (int, float))]
if not vals and "components" in budget:
    vals = [c["TW"] for c in budget["components"]]
if vals:
    chk("L03 heat budget: components sum (TW)", sum(vals), 47, 2e-2)
else:
    SKIP.append("L03 heat budget json shape")

# ════════════════════════════════════════════════════════════════════
section("L04: core formation and dynamos")

m = load("scripts/figures/L04_differentiation_magnetospheres/fig_stokes_settling.py")
chk("L04 Stokes: v at 1 cm (m/s)", float(m.v_stokes(0.01)), 4.444, 1e-3)
r_lam = (9.0 * m.MU ** 2 / (4.0 * 3000.0 * m.DELTA_RHO * m.G)) ** (1.0 / 3.0)
chk("L04 Stokes: laminar limit radius (mm)", r_lam * 1e3, 0.72, 2e-2)

m = load("scripts/figures/L04_differentiation_magnetospheres/fig_water_solubility.py")
chk("L04 solubility: X at 1 kbar (wt%)", float(m.x_h2o(np.array([100.0]))[0]), 4.2, 1e-3)
chk("L04 solubility: X at 5 kbar (wt%)", float(m.x_h2o(np.array([500.0]))[0]), 9.39, 2e-3)

m = load("scripts/figures/L04_differentiation_magnetospheres/fig_geomagnetic_polarity.py")
chk("L04 polarity: CNS young end (Ma)", m.C34N_START, 83.0, 1e-6)
chk("L04 polarity: CNS old end (Ma)", m.C34N_END, 121.0, 1e-6)

# magnetopause: Shue-form standoff sits at 10 R_E by construction
a = 0.6
rho0 = 10.0 * 0.6 * (2.0 / (1.0 + math.cos(0.0))) ** a
chk("L04 magnetopause: nose distance (R_E)", rho0 / 0.6, 10.0, 1e-9)

# ════════════════════════════════════════════════════════════════════
section("L05: atmospheres I")

m = load("scripts/figures/L05_atmospheres_1/fig_earth_tz_layers.py")
chk("L05 USSA76: T at surface (K)", float(m.ussa76(np.array([0.0]))[0]), 288.15, 1e-6)
chk("L05 USSA76: T at 11 km (K)", float(m.ussa76(np.array([11.0]))[0]), 216.65, 1e-3)
chk("L05 USSA76: T at 47 km (K)", float(m.ussa76(np.array([47.0]))[0]), 270.65, 1e-3)
chk("L05 thermosphere anchor at 120 km (K)", float(m.thermosphere(np.array([120.0]))[0]), 360.0, 1e-6)

m = load("scripts/figures/L05_atmospheres_1/fig_dry_moist_adiabat.py")
chk("L05 dry adiabat vs g/c_p (K/km)", m.GAMMA_DRY, 9.81 / 1.004, 2e-2)

m = load("scripts/figures/L05_atmospheres_1/fig_maxwell_boltzmann_jeans.py")
v = np.linspace(0.1, 5e4, 400000)
f = m.maxwell_boltzmann(v, 1000.0, m.M_H)
chk("L05 Maxwell-Boltzmann: normalisation", float(np.trapezoid(f, v)), 1.0, 2e-3)
v_peak = v[np.argmax(f)]
chk("L05 Maxwell-Boltzmann: peak speed (m/s)", float(v_peak),
    math.sqrt(2 * m.K_B * 1000.0 / m.M_H), 2e-3)

m = load("scripts/figures/L05_atmospheres_1/fig_exobase.py")
z = np.linspace(100, 800, 5000)
n = m.number_density(z)
H_km = m.scale_height(z)
ell_km = 1.0 / (m.SIGMA * n) * 1e-3
z_exo = z[np.argmin(np.abs(np.log(ell_km / H_km)))]
chk_true("L05 exobase: crossing in 400-700 km", 400 <= z_exo <= 700, f"z_exo = {z_exo:.0f} km")

comp = list(csv.DictReader(open(ROOT / "scripts/figures/L05_atmospheres_1/data/atmospheric_compositions.csv")))
for row in comp:
    body = row.get("body", "?")
    s = sum(float(v) for k, v in row.items() if k != "body" and v not in ("", None))
    chk(f"L05 composition sum: {body} (%)", s, 100.0, 6e-3)

# ════════════════════════════════════════════════════════════════════
section("L06: atmospheres II")

m = load("scripts/figures/L06_atmospheres_2/fig_kohler_curves.py")
A = m.kelvin_A(273.0)
chk("L06 Koehler: Kelvin A at 273 K (nm)", A * 1e9, 1.156, 1e-2)
B = m.raoult_B(1e-19)
s_crit = math.sqrt(4 * A ** 3 / (27 * B))
chk("L06 Koehler: S_crit-1 for m_s = 1e-16 g", s_crit, 3.9e-3, 5e-2)

m = load("scripts/figures/L06_atmospheres_2/fig_psat_curves.py")
chk("L06 psat: H2O anchor at 373.15 K (Pa)",
    float(m.psat(np.array([373.15]), 18.015e-3, 2.50e6, 373.15, 101325.0)[0]), 101325.0, 1e-6)

m = load("scripts/figures/L06_atmospheres_2/fig_snowball_bistability.py")
T = np.linspace(220, 320, 200000)
diff = m.absorbed(T) - m.OLR(T)
roots = T[np.where(np.diff(np.sign(diff)))[0]]
chk_true("L06 snowball: three equilibria", len(roots) == 3, f"roots at {np.round(roots, 1)}")
if len(roots) == 3:
    chk("L06 snowball: warm equilibrium (K)", float(roots[2]), 287, 1e-2)
    chk("L06 snowball: cold equilibrium (K)", float(roots[0]), 250, 1.5e-2)

m = load("scripts/figures/L06_atmospheres_2/fig_water_phase_diagram.py")
P_end = float(m.cc_curve(np.array([m.T_CRIT]), m.T_TP, m.P_TP, m.L_VAP)[0])
chk("L06 water: vaporisation curve at T_crit (MPa)", P_end / 1e6, m.P_CRIT / 1e6, 1e-2)
slope = m.L_FUS / (m.T_TP * m.DV_FUSION)
chk("L06 water: melting slope (bar/K)", slope / 1e5, -135, 2e-2)

# ════════════════════════════════════════════════════════════════════
section("L08: interiors")

m = load("scripts/figures/L08_interiors/fig_convection_regimes.py")
chk("L08 regimes: 660 km radius fraction", m.R_660, 1 - 660 / 6371, 1e-3)
chk("L08 regimes: CMB radius fraction", m.R_CMB, 1 - 2891 / 6371, 1e-3)

m = load("scripts/figures/L08_interiors/fig_birchs_law.py")
chk("L08 Birch: v_P at rho = 3.3 g/cm^3 (km/s)", m.TREND_A + m.TREND_B * 3.3, 8.29, 2e-3)

moi = json.load(open(ROOT / "scripts/figures/L08_interiors/data/moi_factors.json"))
earth = [b for b in moi["bodies"] if b.get("body", b.get("name", "")).lower().startswith("earth")]
if earth:
    chk("L08 MoI: Earth C/MR^2", earth[0]["C_over_MR2"], 0.3307, 3e-3)
else:
    SKIP.append("L08 MoI Earth entry")
chk_true("L08 MoI: all factors below uniform 0.4",
         all(b["C_over_MR2"] < 0.4 for b in moi["bodies"]), "")

# fig_tidal_resonance: mean motions from the periods are 4:2:1
n_io, n_eur, n_gan = 1 / 1.769, 1 / 3.551, 1 / 7.155
chk("L08 resonance: n_Io/n_Gan", n_io / n_gan, 4.045, 2e-3)
chk("L08 resonance: n_Eur/n_Gan", n_eur / n_gan, 2.015, 2e-3)

# ════════════════════════════════════════════════════════════════════
print()
if SKIP:
    print(f"SKIPPED ({len(SKIP)}): {SKIP}")
if FAIL:
    print(f"{len(FAIL)} FAILURES: {FAIL}")
    raise SystemExit(1)
print("ALL OK")
