# Self-made figure reconstruction — roadmap

This is a working document for the systematic reconstruction of every
self-made figure in the lecture notes. Each figure that does **not**
have a script in `scripts/figures/<lecture>/` and needs one is listed
below. The order matches the lectures.

Each entry has:

- **id** — figure label / fig-id
- **status** — `done`, `in-progress`, `pending`, `needs-question`
- **strategy** — `data-plot` (regenerate from public data), `schematic`
  (programmatic schematic), `caption-fix` (figure is fine, only
  metadata pointer needs adding)
- **notes** — what data is plotted, where it comes from, anything
  unusual

## Already migrated (commit `332726e`, 2026-05-08)

| id | strategy | script |
|---|---|---|
| `fig:exoplanet-cumulative` | data-plot, live | `L01/fig_exoplanet_cumulative.py` |
| `fig:exoplanet-mass-period` | data-plot, live | `L01/fig_exoplanet_mass_period.py` |
| `fig:ss-mass-budget` | data-plot, static | `L01/fig_ss_mass_budget.py` |
| `fig:short-lived-decay` | data-plot, static | `L03/fig_short_lived_decay.py` |
| `fig:composition-bar` | data-plot, static | `L05/fig_composition_bar.py` |

## L01 introduction

| id | status | strategy | notes |
|---|---|---|---|
| `fig:eta-earth` | pending | data-plot | Posterior on η⊕ from Bryson 2021 — already cited. Reconstruct from Bryson's published distribution. |
| `fig:density-vs-distance` | pending | data-plot, static | Bulk density vs semi-major axis for the 8 planets. Reuse `solar_system_masses.csv`; add radius column. |
| `fig:mass-vs-distance` | pending | data-plot, static | Same datasets as above. |
| `fig:vem-atmospheres` | pending | data-plot, static | Surface T and P bars for Venus, Earth, Mars. NASA Fact Sheet. |
| `fig:planet-sizes` | pending | data-plot, static | Visual size comparison of the 8 planets. |
| `fig:terrestrial-planets` | pending | mosaic | Compositing four NASA images — could be mechanical. |
| `fig:trappist1-system` | pending | schematic / data-plot | TRAPPIST-1 orbital architecture diagram; data from Agol+ 2021. |

## L02 formation_orbits

| id | status | strategy | notes |
|---|---|---|---|
| `fig:orbital-elements` | pending | schematic | Six classical orbital elements diagram. |
| `fig:visviva` | pending | data-plot | Orbital speed v(r) from vis-viva for Earth and Halley's comet. |
| `fig:laplace-resonance` | pending | schematic | Galilean moon orbital periods 1:2:4. |
| `fig:roche-geometry` | pending | schematic | Roche limit geometry with two satellites. |
| `fig:kepler1` (?) | pending | schematic | Maybe in markdown. |

## L03 heat_energy

| id | status | strategy | notes |
|---|---|---|---|
| `fig:earth-heat-budget` | pending | data-plot | 47 TW heat budget, decomposed. Davies & Davies 2010. |
| `fig:convection-cells` | pending | schematic | Rayleigh-Bénard cells. |
| `fig:tau-cond-vs-size` | pending | data-plot | τ_cond = L²/κ for various L. |
| `fig:half-space-cooling` | pending | data-plot | erfc temperature profiles. |
| `fig:marginal-stability` | pending | data-plot | Ra_c curve. |
| `fig:nu-ra-scaling` | pending | schematic + data-plot | Nu ~ Ra^(1/3). |
| `fig:lid-regimes` | pending | schematic | Mobile vs stagnant lid. |
| `fig:q-vs-age` | pending | data-plot | Heat flux vs seafloor age. Stein & Stein 1992. |
| `fig:tidal-flexing` | pending | schematic | Eccentric tidal heating. |
| `fig:laplace-resonance-tidal` | pending | schematic | (Same as fig:laplace-resonance? May duplicate.) |

## L04 differentiation_magnetospheres

| id | status | strategy | notes |
|---|---|---|---|
| `fig:stokes-settling` | pending | data-plot | Stokes velocity vs droplet radius. |
| `fig:lunar-magma-ocean` | pending | schematic | Cumulate stratigraphy redrawn after Elkins-Tanton. |
| `fig:water-solubility` | pending | data-plot | H2O solubility in basalt. Newman & Lowenstern 2002 etc. |
| `fig:geomagnetic-polarity` | pending | data-plot | Last 170 Myr polarity bars. Cande & Kent 1995 / Ogg 2020. |

## L05 atmospheres_1 (composition_bar already done)

| id | status | strategy | notes |
|---|---|---|---|
| `fig:dry-moist-adiabat` | pending | data-plot | Lapse rate curves. Static thermodynamics. |
| `fig:earth-tz-layers` | pending | data-plot | US Standard Atmosphere 1976. |
| `fig:titan-tz-hasi` | pending | data-plot | Huygens HASI profile (Fulchignoni 2005). |
| `fig:tau-one` | pending | schematic + data-plot | τ=1 photosphere illustration. |
| `fig:greenhouse-effect` | pending | schematic | One-layer greenhouse fluxes. |
| `fig:exobase` | pending | data-plot | Mean free path vs scale height. |
| `fig:mb-jeans` | pending | data-plot | Maxwell-Boltzmann distributions. |
| `fig:xuv-evolution` | pending | data-plot | XUV/Lbol vs age for G/K/M. Ribas/Tu/Selsis. |

## L06 atmospheres_2

| id | status | strategy | notes |
|---|---|---|---|
| `fig:psat-curves` | pending | data-plot | Clausius-Clapeyron for H2O, CO2, CH4. |
| `fig:kohler-curves` | pending | data-plot | Köhler curves. |
| `fig:water-phase-diagram` | pending | schematic + data-plot | P-T phase diagram of water. |
| `fig:venus-tz` | pending | data-plot | VIRA Venus T(z). |
| `fig:hadley-observed` | pending | data-plot | Streamfunction climatology. ERA5. |
| `fig:coriolis` | pending | schematic | Coriolis geometry. |
| `fig:geostrophic-balance` | pending | schematic | Geostrophic vector diagram. |
| `fig:venus-zonal-winds` | pending | data-plot | Venera 9-12 wind profile. |
| `fig:solar-luminosity` | pending | data-plot | Gough 1981 / Bahcall et al. |
| `fig:snowball-bistability` | pending | schematic + data-plot | EBM hysteresis. |
| `fig:walker-loop` | pending | schematic | Carbonate-silicate cycle. |

## L07 surfaces

(Most figures in L07 are external mission imagery. Will check.)

## L08 interiors

| id | status | strategy | notes |
|---|---|---|---|
| `fig:birchs-law` | pending | data-plot | Birch's vP-density relation. |
| `fig:adams-williamson` | pending | data-plot | PREM test. |
| `fig:prem-profile` | pending | data-plot | PREM tabulated profile. Dziewonski & Anderson 1981. |
| `fig:convection-regimes` | pending | schematic | Whole-mantle vs layered. |

## L09 earth_venus

| id | status | strategy | notes |
|---|---|---|---|
| `fig:lammer-accretion` | pending | schematic | After Lammer 2018. |
| `fig:lammer-carbsil` | pending | schematic | Carbon-silicate cartoon. |
| `fig:trappist1` | pending | data-plot / mosaic | Compare TRAPPIST-1 to inner solar system. (May be redundant with L01.) |

(External ones in L09 — Hamano, Way, Gillmann, Lebrun, Honing, Smrekar — already attributed.)

## L10 mercury_mars

(All major figures attributed externally; just one hand-drawn schematic.)

| id | status | strategy | notes |
|---|---|---|---|
| `fig:kite-schematic` | pending | schematic | Mars climate cartoon after Kite & Carter 2022. |

## L11 gas_ice_giants

(Mostly external mission imagery; spot-check.)

## L12 small_bodies

| id | status | strategy | notes |
|---|---|---|---|

Almost all figures are external — only check.

## L13 exoplanets

| id | status | strategy | notes |
|---|---|---|---|
| `fig:transitgeom` | pending | schematic | Transit geometry. |
| `fig:obliquitypathways` | pending | schematic | Obliquity migration cartoon. |

## L14 synthesis

(All major figures attributed externally; spot-check.)

## Working order

1. L01 (six figures)
2. L02 (four schematics + visviva)
3. L03 (ten figures)
4. L04 (four figures)
5. L05 (eight figures)
6. L06 (eleven figures)
7. L07-L14 spot-check (fewer figures each)

Atomic commits per figure (or per small related batch within one
lecture). After every commit, verify the build, the rendered figure,
and the caption fit; then push.
