(lecture14)=
# Synthesis, Solar System in Context & Astrobiology

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to place our solar system within the observed exoplanet population, evaluate habitability as a coupled systems-level property rather than a single condition, derive the classical habitable-zone boundaries from stellar luminosity and the liquid-water condition, and identify the most promising targets and biggest open questions for life-detection efforts in the coming decade.
```

```{seealso}
**Slides:** [Download Lecture 14 (PDF)](../_static/slides/lecture14.pdf)
```

## Part 1: The solar system in the exoplanet context

### Recap: what this course has shown

Thirteen lectures have built a single argument from the bottom up.
Lectures 1 to 8 introduced protoplanetary disks, interior evolution and differentiation, atmospheres, surfaces, and internal structure.
Lectures 9 to 12 walked the solar system body by body: Earth and Venus ({ref}`Lecture 9 <lecture09>`), Mercury and Mars ({ref}`Lecture 10 <lecture10>`), the gas and ice giants ({ref}`Lecture 11 <lecture11>`), and small-body populations ({ref}`Lecture 12 <lecture12>`).
Lecture 13 showed how the same physics applies to several thousand planetary systems detected since 1995 {cite:p}`MayorQueloz1995`.

The thread is simple: physical processes shape planetary outcomes everywhere.
The diversity of planets in the galaxy, and the differences between Earth, Venus, and Mars, reflect the same physical levers operating across a wide range of boundary conditions.

This final lecture provides the synthesis.
Part 1 places the solar system inside the exoplanet population, identifying where it is typical and where it is atypical.
Part 2 reframes **habitability** as a coupled systems property, in which star, orbit, interior, atmosphere, surface, and biosphere all feed back on one another.
Part 3 turns to astrobiology: what we would look for, where we should look, and how confident we can be in the answers.
The blackboard derivation reconstructs the classical habitable zone from energy balance, closing with a wrap-up of the course as a whole.

### Planet formation theory meets observation

Dust in disks coagulates into pebbles forming **planetesimals**, bodies from roughly a kilometre across produced by the streaming instability.
Accreting pebbles and planetesimals build cores that trigger runaway gas accretion {cite:p}`Drazkowska2023,Lambrechts2012` ({numref}`fig:l14:formation-overview` and {numref}`fig:l14:envelope-accretion`).

```{figure} figures/drazkowska2023_growth_processes.avif
:align: center
:name: fig:l14:formation-overview
:width: 90%

Overview of the dust-to-planet growth processes operating in protoplanetary disks. Dust grains coagulate into pebbles whose radial drift can either be halted at pressure traps (planetesimal formation via the streaming instability) or accreted directly onto growing embryos. Larger embryos compete via runaway and oligarchic growth and, once massive enough, trigger gas envelope accretion. Reproduced from {cite:t}`Drazkowska2023`.
```

```{figure} figures/lambrechts2012_core_growth.avif
:align: center
:name: fig:l14:envelope-accretion
:width: 90%

Mass growth of a planetary core as a function of time at three orbital radii (0.5, 5, and 50 AU), comparing pebble accretion in the drift and Hill regimes (solid lines) with classical planetesimal accretion (grey dotted lines). Pebble accretion reaches 10 Earth masses well before the typical disk lifetime, while planetesimal accretion at 5 AU takes longer than the disk lifetime. The masses of Ceres and Pluto are marked for reference. Reproduced from {cite:t}`Lambrechts2012`.
```

ALMA images resolve disk gaps and rings formed by planets {cite:p}`Andrews2018` ({numref}`fig:l14:dsharp`).
Infrared excess indicates disk lifetimes of 3 to 5 Myr {cite:p}`Haisch2001`, defining the window for gas accretion.

```{figure} figures/andrews2018_dsharp_gallery.avif
:align: center
:name: fig:l14:dsharp
:width: 90%

Gallery of 240 GHz (1.25 mm) ALMA continuum images of 20 nearby protoplanetary disks from the DSHARP large programme. Concentric rings, gaps, and asymmetric features are nearly ubiquitous, and most are interpreted as signatures of planetary growth in progress. The combination of disk substructure surveys with disk dust mass measurements provides the strongest empirical constraints on the inputs to planet formation models. Reproduced from {cite:t}`Andrews2018`.
```

```{figure} figures/lambrechts2012_growth_time.avif
:align: center
:name: fig:l14:accretion-timescales
:width: 90%

Time required to grow a 10 Earth mass core as a function of distance from the star. The solid black line is pebble accretion in the Hill regime, the solid grey line is planetesimal accretion, and the dashed grey line is accretion of planetesimal fragments from a thin midplane layer. The red hatched band, roughly 1 to 10 Myr, is the interval over which the disk loses its gas, so a core that is to capture a gas envelope must reach 10 Earth masses before it. The pebble line stays below the band at every radius plotted, while the planetesimal line rises through it within a few AU and lies above it in the outer disk. Reproduced from {cite:t}`Lambrechts2012`.
```

Disk migration explains close-in giants and **resonant chains**, systems locked in near-integer period ratios {cite:p}`Paardekooper2023`.
Pebble accretion allows cores to reach envelope runaway within disk lifetimes ({numref}`fig:l14:accretion-timescales`).
Jupiter's early growth may have isolated the non-carbonaceous and carbonaceous (NC-CC) meteorite reservoirs {cite:p}`Kruijer2017` ({numref}`fig:l14:nccc-timeline`).
The **Nice model** (a late instability of the giant planets) and the **Grand Tack** (an inward and then outward migration of Jupiter) reproduce the depleted asteroid belt and the Trojan asteroids {cite:p}`Tsiganis2005,Walsh2011`.

```{figure} figures/lichtenberg2023_nccc_timeline.avif
:align: center
:name: fig:l14:nccc-timeline
:width: 80%

Timeline of solar system formation reconstructed from isotopic dating of meteoritic materials. The non-carbonaceous (NC, red) and carbonaceous (CC, blue) reservoirs maintain distinct isotopic signatures from CAI (calcium-aluminium-rich inclusion, among the earliest solids to condense in the solar system) formation onwards, indicating that they accreted in physically separated regions of the disk for at least the first 2--3 Myr. Reproduced from {cite:t}`Lichtenberg2023`.
```

Surveys reveal a **radius valley** at $\sim 1.8\,\Rearth$ separating super-Earths from sub-Neptunes {cite:p}`Fulton2017` ({numref}`fig:l14:fulton-valley`).
Photoevaporation by stellar XUV {cite:p}`Owen2017` and core-powered mass loss {cite:p}`Gupta2019` both predict a valley in the right location, and current data cannot yet reject either mechanism.

```{figure} figures/fulton2017_radius_valley.avif
:align: center
:name: fig:l14:fulton-valley
:width: 70%

The "Fulton gap" in the radius distribution of small close-in exoplanets. The two-dimensional map of planet size against incident stellar light shows a deficit of planets at $\sim 1.8\,\Rearth$ that separates a denser super-Earth population from a sub-Neptune population. The lower panel overlays the predictions of photoevaporation models, which can reproduce both the location and the slope of the valley with stellar irradiation. Reproduced from {cite:t}`Fulton2017`.
```

Meteorite reservoir separation may require Jupiter core growth within $\sim 1$ Myr of CAIs {cite:p}`Kruijer2017`.
Alternatively, the **snow line**, the disk radius where water ice condenses, divides reservoirs without an early core {cite:p}`Lichtenberg2021`.
This is unresolved and matters for whether Jupiter set the boundary conditions of inner-system planet formation.

Planets between $1$ and $4\,\Rearth$ are the most common exoplanets {cite:p}`Bryson2021`, yet the solar system contains none.
This absence may reflect pebble blocking by Jupiter, low solid density, or stochastic history.

**Population synthesis** models simulate planet formation to predict demographic outcomes ({numref}`fig:l14:popsyn`).
Synthetic populations produce super-Earths, confirming that their absence in the solar system requires a specific dynamical explanation.

```{figure} figures/drazkowska2023_population_synthesis.avif
:align: center
:name: fig:l14:popsyn
:width: 90%

Population synthesis predictions for planet mass versus orbital period assuming planetesimal accretion (panel A) and pebble accretion (panel B). Both models populate the super-Earth, hot Jupiter, warm gas giant, and cold gas giant regimes, with super-Earth mass fractions of $\sim 35\%$ in models with pebble accretion. Reproduced from {cite:t}`Drazkowska2023`.
```

### The solar system overlaid on the exoplanet diagram

The period-radius diagram highlights where our solar system differs from exoplanet architectures ({numref}`fig:l14:periodradius`).

```{figure} figures/raymond2022_period_radius.avif
:align: center
:name: fig:l14:periodradius
:width: 70%

Census of confirmed transiting exoplanets in orbital period and planet size. Open circles are all transiting planets. The box in the top panel is the region used to define a compact multi, a system with at least two planets inside it, and the filled circles are the planets that meet that definition. The middle panel joins the planets of five compact multis whose sizes and spacings are unusually uniform (Kepler-11, Kepler-172, Kepler-374, Kepler-444, Kepler-1542), the "peas-in-a-pod" pattern. The bottom panel joins three systems that do not show it: WASP-47 and KOI-94 meet the compact-multi definition but span a wide range of planet sizes, and the young system V1298 Tau fails it. Reproduced from {cite:t}`Weiss2023`.
```

A disk snow line creates a typical radial composition gradient {cite:p}`Weiss2023`, but four features are unusual:

1. No planets between $1\,\Rearth$ and $\sim 4\,\Rearth$, though most stars host one within 1 AU {cite:p}`Bergsten2022`.
2. Circular giant orbits at 5 and 10 AU rather than eccentric orbits.
3. No **hot Jupiter** or hot Neptune; close-in gas giants orbit $0.5$ to $1\%$ of Sun-like stars, and we have neither.
4. Irregular terrestrial spacings rather than uniform **peas-in-a-pod architectures** ({numref}`fig:l14:peas`; {cite:t}`Weiss2018`).

```{figure} figures/raymond2022_peas_in_a_pod.avif
:align: center
:name: fig:l14:peas
:width: 75%

Compact multi-planet systems with four or more transiting planets interior to 1.52 AU, ranked by their planet-radius dispersion (most uniform sizes at the top, greatest size diversity at the bottom). Point sizes scale logarithmically with planet radius. The solar system terrestrials, included for comparison, sit in the bottom quintile of size uniformity, showing that the peas-in-a-pod architecture prevalent in Kepler compact multis did not emerge in our own system. Reproduced from {cite:t}`Weiss2023`.
```

The **mass-radius diagram** evaluates bulk composition against theoretical equations of state ({numref}`fig:l14:massrad`).
Terrestrial planets follow the Earth-like rocky curve, while larger sub-Neptunes sit above it with volatile envelopes.

```{figure} figures/lichtenberg2025_mass_radius.avif
:align: center
:name: fig:l14:massrad
:width: 95%

Mass-radius diagram for rocky and small exoplanets from {cite:t}`Lichtenberg2025` Fig. 2. Data points are observed exoplanets with measured masses and radii, colour-coded by equilibrium temperature into **temperate** (blue), **bistable** (light blue, able to sit in either a temperate or a runaway-greenhouse climate state), **lava** (red), and **rock-vapour** (orange) regimes; symbol shape marks **high-priority** atmospheric-characterisation targets (diamonds) and lower-priority targets (circles). Labelled planets include TRAPPIST-1 b through h, GJ 367 b, GJ 1132 b, GJ 486 b, K2-18 b, K2-141 b, LHS 1140 b, L 98-59 b/c/d, GJ 1252 b, LTT 1445 A b, and several TOI targets. Theoretical equation-of-state tracks range from **100% Fe** (bottom) through **Earth-like** rocky and **100% MgSiO$_3$**, with volatile-rich tracks for **Earth-like + 50 wt% H$_2$O**, **magma ocean + 0.1 wt%** or **5.4 wt% H$_2$O**, and a **gas-dwarf birth + H/He boil-off** curve that bounds the potential sub-Neptune population (shaded at upper left). Solar-system terrestrials sit on the Earth-like curve; exoplanets above it either retain volatile envelopes (H/He, water, or melt-water mixtures) or are otherwise reshaped by magma-ocean outgassing and photoevaporation. Reproduced from {cite:t}`Lichtenberg2025`.
```

### "Is the solar system rare?"

Whether the solar system is rare remains unknown because survey limits have left much of its parameter space unobserved.
Detecting a planet in a 12-year Jupiter-like orbit requires decades of monitoring or radial-velocity baselines, making Gaia DR4 (scheduled for December 2026) the first survey sensitive to astrometric Jupiter analogues at scale.
Similarly, **Earth analogues** ($\Rearth$-sized planets in 1-year orbits around Sun-like G dwarfs) lie at the edge of current sensitivity and require upcoming missions such as PLATO (launch early 2027) and Gaia DR4/DR5.

Existing exoplanet statistics reflect a sample heavily biased toward close-in, massive planets, leaving the true distribution unsettled.
The inner solar system is atypical relative to known compact systems because our terrestrial planets are widely spaced and varied in mass rather than following a uniform peas-in-a-pod pattern.

The planet **occurrence rate** (the average number of planets per star in a given parameter range) depends strongly on stellar type ({numref}`fig:l14:mulders-occurrence`).
Rocky and sub-Neptune-sized planets on orbits with periods $< 50$ days are roughly twice as common around early M dwarfs as around F and G dwarfs, although whether this reflects formation efficiency or survey detection bias remains debated.

```{figure} figures/mulders2024_occurrence_vs_teff.avif
:align: center
:name: fig:l14:mulders-occurrence
:width: 80%

Overview of planet occurrence rates as a function of host-star effective temperature, for planets between $1$ and $4\,\Rearth$ on orbital periods $P < 50$ days, from {cite:t}`Mulders2024` Fig. 5. Rates were re-scaled assuming uniform occurrence in $\log P$ and $\log R$ for cross-study comparison. Plotted data are compiled from Howard+12, Mulders+15, Hardegree-Ullman+19, Yang+20, He+21, Sabotta+21, {cite:t}`Bergsten2022`, and Ment & Charbonneau 23 (see {cite:t}`Mulders2024` for full references). Across all studies, planet occurrence increases by roughly a factor of 2 from F dwarfs ($\sim 6500$ K) to early M dwarfs ($\sim 3500$ K); a break appears toward late M dwarfs, but those surveys sample only very short periods ($< 10$ d) so the late-M values are lower limits. The headline message is that small, close-in planets are most common around the most numerous class of stars in the galaxy. Reproduced from {cite:t}`Mulders2024`.
```

## Part 2: Habitability as a coupled systems property

### The stack of requirements

**Habitability** is the capacity of a planet to sustain surface liquid water, which emerges from a stack of coupled physical requirements rather than a single condition.
Earlier lectures developed these components in sequence: atmospheric retention in lecture 5, climate feedbacks in lecture 6, tectonics in lecture 7, comparative evolution of Earth, Venus, and Mars in lectures 9 and 10, and stellar context in lecture 13.

The stack spans requirements across the planetary system:
- Star: Stable luminosity over Gyr timescales, low flaring, and a long main-sequence lifetime.
- Orbit: Location in the liquid-water habitable zone, low eccentricity, and heat redistribution preventing atmospheric collapse.
- Planet bulk: Sufficient mass to retain volatiles over Gyr timescales and drive mantle convection.
- Atmosphere: Composition maintaining temperate conditions without runaway photochemistry.
- Interior: Internal heat driving mantle convection, outgassing, and dynamo generation.
- Surface and tectonics: Volatile recycling between the surface, atmosphere, and interior must close the carbon cycle.
- Biosphere: Biological feedbacks modifying atmospheric composition, surface albedo, and weathering.

Every level in the stack is necessary, but none is sufficient alone.
Habitability is a system property governed by coupled feedbacks.
Stellar radiation drives photochemistry, clouds affect albedo and temperature, temperature regulates weathering that draws down $\mathrm{CO_2}$, and outgassing replenishes $\mathrm{CO_2}$ through tectonic recycling.
Breaking any coupling can drift the climate into a state where surface liquid water cannot persist.

{numref}`fig:l14:habitability-factors`, from {cite:t}`MeadowsBarnes2018`, organizes these habitability factors into stellar, planetary-system, and planetary properties.
The diagram distinguishes properties by accessibility: direct observations, model interpretations, or theoretical constraints.
This distinction determines which couplings telescopes can actually test.

```{figure} figures/meadowsbarnes2018_habitability_factors.avif
:align: center
:name: fig:l14:habitability-factors
:width: 80%

Factors affecting planetary habitability: the currently understood stellar, planetary-system, and planetary properties that may impact whether a planet can sustain surface liquid water. Font colour denotes how each characteristic is accessible: blue for properties that could be observed directly with sufficiently powerful telescopes, green for those that require modelling interpretation, possibly constrained by observations, and orange for properties or processes accessible primarily through theoretical modelling. The larger the number of these factors that can be determined for a habitable zone candidate, the more robust the assessment of its habitability. Reproduced from {cite:t}`MeadowsBarnes2018`.
```

### The habitability coupling loop

On a **tidally locked planet**, rotation and orbital periods match so that one hemisphere permanently faces the star ({numref}`fig:l14:tidal-couplings`; {cite:p}`Wordsworth2022`).
Substellar clouds reflect starlight, super-rotating winds transport heat to the nightside, and antistellar cold-trapping can collapse the atmosphere.

```{figure} figures/wordsworth2022_tidally_locked_planet.avif
:align: center
:name: fig:l14:tidal-couplings
:width: 85%

Schematic of the dynamical and climate processes in the atmosphere of a tidally locked rocky exoplanet. Stellar irradiation drives cloud formation and partial reflection near the substellar point, day-to-night heat transport by super-rotating winds, and cold-trapping of condensable volatiles at the antistellar point, where the atmosphere can collapse onto the surface. When the dominant condensable is water, this transport-and-trapping cycle is the planet's hydrological cycle. Whether it persists depends on the total water inventory and on factors such as tectonic regime, escape, and stellar evolution that this single snapshot does not capture. Reproduced from {cite:t}`Wordsworth2022`.
```

The full coupling loop links the star, atmosphere, surface, and interior.
Stellar irradiation drives radiative balance and photochemistry ({ref}`Lecture 5 <lecture05>`), while atmospheric heating controls surface weathering and carbonate-silicate breakdown ({ref}`Lecture 6 <lecture06>`, {ref}`Lecture 9 <lecture09>`).
Subduction returns volatiles to the deep mantle, interior outgassing supplies $\mathrm{CO_2}$, $\mathrm{H_2O}$, and $\mathrm{SO_2}$, and dynamo shielding deflects the stellar wind ({ref}`Lecture 4 <lecture04>`).

Neither equilibrium temperature nor habitable zone position alone determines habitability.
A planet remains habitable only if all coupling loops remain closed across geological history under appropriate boundary conditions.

### The habitable zone is not a line

The **habitable zone** (HZ) is the orbital range around a star where an Earth-like planet can maintain liquid surface water.
Its boundaries are set by the runaway greenhouse limit and maximum $\mathrm{CO_2}$ greenhouse {cite:p}`Kopparapu2013` ({numref}`fig:l14:kopparapu-hz`).

```{figure} figures/kopparapu2014_hz_stellartype.avif
:align: center
:name: fig:l14:kopparapu-hz
:width: 80%

Habitable zone boundaries as a function of stellar effective temperature and planet mass, from {cite:t}`Kopparapu2014`. The inner HZ (left curves) and outer HZ (right curve) shift inward for cooler stars. Around M dwarfs, the HZ overlaps strongly with the tidal-locking radius and with spin-orbit resonance regions, where the planet's rotation period locks to a simple ratio of its orbital period, complicating habitability assessment in ways that the 1D HZ does not capture. Reproduced from {cite:t}`Kopparapu2014`.
```

Venus receives $\sim 1.9\times$ Earth's solar flux but has a $737$ K, $92$ bar atmosphere without water, while Earth maintains a $288$ K surface and stable hydrosphere ({ref}`Lecture 9 <lecture09>`).
This divergence reflects different histories through early molten phases and solar luminosity evolution {cite:p}`Hamano2013` ({numref}`fig:l14:runaway`).

```{figure} figures/lugerbarnes2015_runaway_duration.avif
:align: center
:name: fig:l14:runaway
:width: 75%

Duration of the runaway greenhouse phase for planets that formed at 10 Myr with abundant surface water, as a function of stellar mass (vertical axis) and orbital semi-major axis (horizontal axis), from the {cite:t}`LugerBarnes2015` water-loss calculation around M dwarfs. The solid black lines mark the empirical inner habitable zone (recent Venus and early Mars limits at 5 Gyr); the dashed lines mark the theoretical runaway and maximum greenhouse limits. Habitable-zone planets around late M dwarfs spend a substantial fraction of their first Gyr inside the runaway state, losing much of their initial water before the host star reaches the main sequence. Reproduced from {cite:t}`LugerBarnes2015`.
```

The habitable zone is also time-dependent, as stellar luminosity increases by roughly 30% over the main sequence.
Around M dwarfs, planets now in the HZ spent hundreds of Myr inside the runaway greenhouse boundary {cite:p}`LugerBarnes2015`.

Habitability therefore depends on evolutionary trajectories, requiring coupled climate-evolution models rather than static 1D HZ boundaries.

### Tectonic regime and the long-term thermostat

The **carbonate-silicate cycle** is Earth's long-term thermostat by balancing volcanic $\mathrm{CO_2}$ outgassing with silicate weathering and carbonate subduction ({ref}`Lecture 6 <lecture06>`, {ref}`Lecture 9 <lecture09>`).
Warmer surface temperatures increase weathering rates, accelerating $\mathrm{CO_2}$ removal and cooling the planet.

This thermostat requires liquid water, active volcanism, and plate tectonic recycling.
Venus illustrates the failure of this mechanism ({ref}`Lecture 9 <lecture09>`).
Without liquid water, silicate weathering ceases, allowing outgassed $\mathrm{CO_2}$ to accumulate into its 92 bar atmosphere.
**Stagnant-lid** worlds (planets whose outer shell forms a single immobile plate rather than being recycled by plate tectonics) do not subduct carbonates into the mantle.

Whether stagnant-lid planets with episodic resurfacing can sustain temperate climates over Gyr timescales remains unresolved.
Because planetary tectonic regimes cannot be measured remotely with current or near-term observations, this is one of the largest missing variables in assessing exoplanet habitability.

### Magnetic field as gatekeeper

Lecture 4 and Lecture 10 showed how an active **magnetosphere**, a planetary magnetic shield, protects an atmosphere from solar-wind ion-pickup escape.
Mars lost its global magnetic field early in its history, with remanent magnetization indicating dynamo activity until $\sim 3.7$ Ga near the Noachian-Hesperian boundary, later than the 4.1 to 3.9 Ga estimated from basin demagnetisation {cite:p}`Acuna1999,Mittelholz2020`.
Mars subsequently lost most of its atmosphere to space, consistent with MAVEN constraints indicating an initially thicker $\mathrm{CO_2}$ atmosphere {cite:p}`Jakosky2018`.

However, a magnetic field is not strictly required for atmospheric retention, as Venus retains its $\sim 92$ bar atmosphere without one.
A magnetic field instead shifts the balance of escape mechanisms.
Without one, atmospheric losses are dominated by **nonthermal escape**: pickup ions, sputtering, and ionospheric outflow.
Whether these losses matter on Gyr timescales depends on planetary mass, the atmospheric column, stellar wind strength, and dynamo timing.
For exoplanets around active M dwarfs like TRAPPIST-1, whether an active dynamo is required for atmospheric retention remains an open question.

### Water delivery and planetary evolution

Planetary water inventories are often framed around delivery from **carbonaceous chondrites** (primitive, volatile-rich meteorites) versus comets and their relative D/H ratios.
However, internal planetary evolution dominates over initial delivery in setting inner solar system water budgets.

Earth, Venus, and Mars accreted broadly similar volatile inventories per unit silicate mass {cite:p}`Lichtenberg2023`.
Their present-day water inventories differ by orders of magnitude because each planet processed its initial inventory differently {cite:p}`Hamano2013`.

```{figure} figures/lichtenberg2023_magma_ocean_differentiation.avif
:align: center
:name: fig:l14:magma-diff
:width: 70%

Schematic of magma-ocean stage differentiation on a forming rocky planet. The initially molten silicate mantle separates from a denser metal phase that sinks to form the core, while volatiles partition between the molten silicate and an overlying steam atmosphere. The fraction sequestered in the mantle versus outgassed into the atmosphere is decisive for the planet's later atmospheric evolution. Reproduced from {cite:t}`Lichtenberg2023`.
```

The first mechanism is volatile partitioning during the early molten phase, when the mantle is wholly or largely molten (a **magma ocean**).
Water and carbon partition between the core, mantle, and overlying steam atmosphere according to magma redox state, solidification timescale, and crystallisation depth {cite:p}`Hirschmann2012` ({numref}`fig:l14:magma-diff`).
Different boundary conditions produce divergent atmospheric end states from identical initial budgets.

Accretion timing also controls volatile retention.
Planetesimals accreting within the first $\sim 1$ Myr after CAI formation are heated above the water-ice melting point by short-lived radionuclides ($^{26}\mathrm{Al}$, half-life $\sim 0.7$ Myr) and lose water by dehydration.
Bodies accreting later beyond the snow line retain their volatiles {cite:p}`Lichtenberg2023`.
Building blocks formed early are therefore systematically dryer than late-formed ones.

The second mechanism is atmospheric escape during the magma ocean phase.
Under an EUV-bright young Sun, hydrodynamic escape can remove water before the magma ocean solidifies ({ref}`Lecture 9 <lecture09>`; {cite:t}`Hamano2013`).
For Venus, with $\sim 1.9$ times Earth's instellation, prolonged magma ocean solidification allowed extensive hydrogen escape, preventing liquid water accumulation ({numref}`fig:l14:hamano-typeII`).

```{figure} figures/hamano2013_typeI_typeII.avif
:align: center
:name: fig:l14:hamano-typeII
:width: 70%

Two distinct types of terrestrial planet defined by the {cite:t}`Hamano2013` model. Panel (a) shows magma-ocean solidification time as a function of orbital distance and instellation for a range of initial water inventories; planets inside a critical orbital distance ($\sim 0.77$ AU around a Sun-like star) cannot solidify their magma oceans before most of their water is lost to hydrodynamic escape ("Type II"), while planets further out solidify quickly and retain most of their water ("Type I"). Panel (b) shows the resulting final water inventories at the end of magma-ocean solidification. Modified from {cite:t}`Hamano2013` as reproduced in {cite:t}`Lichtenberg2023`.
```

The third mechanism is long-term mantle-atmosphere volatile exchange.
On planets with active plate tectonics, outgassing and subduction balance to maintain steady surface inventories over billions of years.
On stagnant-lid planets, weak return flow causes surface inventories to drift.
On small bodies that lose interior convection (such as the Moon, or Mars after $\sim 1$ Ga), volcanic outgassing ceases.

The fourth mechanism is stellar evolution.
For M-dwarf planets, the luminous pre-main-sequence phase keeps the habitable zone within the runaway greenhouse boundary for the first few hundred Myr ({ref}`Lecture 13 <lecture13>`; {cite:t}`LugerBarnes2015`).
For G dwarfs, the faint young Sun of 4 Gyr ago required stronger greenhouse warming, while stellar brightening gradually shifts the habitable zone outward.

Radiogenic clocks in meteorites and lunar samples show that core formation, magma ocean crystallisation, and silicate differentiation finished within the first $\sim 100$ Myr {cite:p}`Lichtenberg2023`.
These early interior processes established the boundary conditions for all subsequent atmospheric evolution.

Present-day water inventories are therefore set primarily by internal planetary evolution rather than initial delivery.
The D/H ratios from {ref}`Lecture 12 <lecture12>` constrain delivery combined with evolutionary processing.
Likewise, exoplanet atmospheric water observations reflect the integrated history of accretion, magma-ocean processing, escape, outgassing, and tectonic recycling.

### The Drake equation and its limitations

The **Drake equation** is a heuristic factorisation used to organise questions about the abundance of communicating civilisations in the galaxy, originally written for the 1961 Green Bank meeting {cite:p}`Drake1965`:

$$
N = R_\star \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L \,.
$$

Here $R_\star$ is the rate of star formation in the galaxy, $f_p$ is the fraction of stars with planets, $n_e$ is the number of habitable-zone planets per system, $f_l$ is the fraction of habitable planets on which life arises, $f_i$ is the fraction where intelligence evolves, $f_c$ is the fraction that develops detectable broadcasting technology, and $L$ is the average lifetime of the communicative phase.
Multiplying these factors yields $N$, the expected number of communicating civilisations in the galaxy at any given time.

The equation separates the problem into distinct disciplinary inputs, making plain that only the first three factors are currently constrained by observation.
Stellar astrophysics determines $R_\star$, while exoplanet surveys show that $f_p$ is of order unity ({ref}`Lecture 13 <lecture13>`).
For Sun-like stars, Kepler and TESS constrain $n_e$ to between $0.1$ and $0.6$ depending on the habitability definition {cite:p}`Bryson2021`.
In contrast, the remaining four factors ($f_l$, $f_i$, $f_c$, $L$) lack quantitative empirical constraints.
Earth provides the sole data point for $f_l$, whereas $f_i$, $f_c$, and $L$ have no statistical constraints beyond our own lineage and the last $\sim 100$ years.

The Drake equation is a qualitative framework rather than a predictive estimator, because point estimates of $N$ face five fundamental limitations:

1. Coupled factors: biospheres co-evolve with planetary interiors and atmospheres, so the emergence of intelligence or communication cannot be strictly separated into independent multiplicative terms.
2. Orders-of-magnitude uncertainty: published estimates for $f_l$, $f_i$, $f_c$, and $L$ span four to ten orders of magnitude, causing the product to reflect input priors rather than measurements.
3. Non-equilibrium contingency: the origin of life is a historical, non-equilibrium process rather than a steady-state chain with stationary transition probabilities.
4. Assumed uniformity: the single-parameter formulation averages across diverse stellar environments, planet types, and atmospheric histories.
5. Anthropic selection: Earth is our only observed example of life, creating an observer selection effect that complicates extrapolation.

{cite:t}`SandbergDrexlerOrd2018` quantified this uncertainty by sampling each factor from its published range of scientific estimates ({numref}`fig:l14:sandberg-drake`).
Propagating these broad distributions reveals that roughly one third of the posterior probability mass falls below $N = 1$ in the Milky Way, and about ten percent falls below the threshold for being alone in the observable universe.
{cite:t}`SandbergDrexlerOrd2018` argue that this dissolves the **Fermi paradox**, the apparent contradiction between high estimates of extraterrestrial civilisations and the lack of observational evidence.
The silence of the galaxy is fully consistent with current knowledge once the genuine uncertainty in the inputs is acknowledged.

The broad posterior in {numref}`fig:l14:sandberg-drake` arises because unconstrained factors spanning multiple decades require log-uniform priors rather than uniform priors.
Taking the logarithm converts the product into a sum:

$$
\log_{10} N = \log_{10}(R_\star f_p n_e) + \log_{10} f_l + \log_{10} f_i + \log_{10} f_c + \log_{10} L \,,
$$

The distribution of $\log_{10} N$ is the convolution of the individual log-factor distributions.
If the four unconstrained factors are log-uniform over $[-10, 0]$, their sum spans $[-40, 0]$ with a central peak and tails extending to $\log_{10} N \sim -30$.
Combining these terms with the bounded astronomical prefactor $R_\star f_p n_e$ yields a posterior distribution stretching across $\sim 30$ decades.
Broad priors on multiplicative factors inevitably generate wide product distributions, showing that any point estimate of $N$ is determined by prior choice rather than data.

```{figure} figures/sandberg2018_drake_posterior.avif
:align: center
:name: fig:l14:sandberg-drake
:width: 80%

Posterior probability distribution for the number $N$ of communicating civilisations in the observable universe, computed by {cite:t}`SandbergDrexlerOrd2018` by Monte-Carlo sampling each Drake-equation factor from its published range of estimates rather than from a single point estimate. (Top) Probability density: the distribution is heavily bimodal, with one peak below $N \sim 10^{-20}$ and another near $N \sim 1$ to $10^5$. The red circles mark Drake-style point estimates from the literature. (Middle) Cumulative distribution: roughly one third of the probability mass lies below $N = 1$, corresponding to "we are alone in the Milky Way"; only about $10\%$ of the probability mass lies below the much lower threshold $N \ll 1$ corresponding to "we are alone in the observable universe". (Bottom) Cumulative distribution of distance to the nearest civilisation. The two vertical lines mark the boundary "alone in the Milky Way" (red) and "alone in the observable universe" (blue). Reproduced from {cite:t}`SandbergDrexlerOrd2018`.
```

### The Fermi paradox

The **Fermi paradox** is the question of why we observe no evidence of spacefaring civilisations, summarised as "where is everybody?".
Because the Milky Way is about $10^{10}$ years old, an early spacefaring civilisation could have crossed the galaxy at sub-relativistic speeds.
Yet, we observe no evidence of any such civilisation.

Proposed resolutions address different Drake-equation factors or observational limits:
- **Rare-life hypothesis:** $f_l$ is very small because life is hard to start.
- **Rare-intelligence hypothesis:** $f_i$ is the bottleneck because technological intelligence rarely follows from biology.
- **Great filter:** $L$ is short because civilisations self-terminate before covering the galaxy.
- **Detection threshold:** signals exist but remain below current sensitivity or use unrecognised encoding.
- **Zoo scenarios:** civilisations deliberately conceal themselves or avoid contact.

The Fermi paradox is a tool for thinking rather than a piece of evidence.
It is a check on intuition for Drake-equation estimates.
An estimate of $N \sim 10^4$ requires a mechanism that keeps civilisations invisible.
An estimate of $N \sim 1$ dissolves the paradox but raises the question of why life is so rare.

## Blackboard derivation: The habitable zone boundaries

````{admonition} Blackboard derivation: The habitable zone boundaries
:class: tip

The aim of this derivation is to reconstruct the inner and outer edges of the classical habitable zone from a one-line energy balance, without invoking any radiative-convective machinery. The inputs are the inverse-square law and the Stefan-Boltzmann law; the outputs are the orbital distances at which an Earth-like planet around a star of luminosity $L_\star$ can support liquid surface water. After deriving the result in general, we will compare HZ widths for G, K, and M dwarfs.

**Setup.** A star of bolometric luminosity $L_\star$ irradiates a planet at orbital distance $d$. The flux at the planet's orbit is

$$
F_\star(d) = \frac{L_\star}{4\pi d^2}\,.
$$

The planet absorbs a fraction $(1 - A_B)$ of the incident flux, where $A_B$ is the Bond albedo. For a fast-rotating spherical planet, the absorbed power per unit area, averaged over the whole planet, is $(1 - A_B) F_\star / 4$, because the projected area is $\pi R_p^2$ but the radiating area is $4\pi R_p^2$. Equating absorbed and emitted power gives the equilibrium temperature

$$
T_{\mathrm{eq}}(d) = \left[\frac{L_\star (1 - A_B)}{16\pi\sigma\epsilon d^2}\right]^{1/4}\,,
$$

where $\epsilon$ is the effective emissivity of the atmosphere (which in the bare-rock limit is $1$) and $\sigma$ is the Stefan-Boltzmann constant. For Earth around the Sun, plugging in $A_B \approx 0.3$, $\epsilon \approx 1$, $L_\star = \Lsun$, and $d = 1$ AU gives $T_{\mathrm{eq}} \approx 255$ K. The actual surface temperature is $\sim 288$ K because the greenhouse effect adds $\sim 33$ K.

**Effective stellar flux scaling.** The cleanest way to express habitable-zone boundaries is in terms of the **effective stellar flux** $S_{\rm eff}$, defined as the top-of-atmosphere stellar flux at the HZ boundary divided by Earth's present TOA flux $S_\oplus = 1361$ W/m$^2$. Because $F_{\rm TOA} = L_\star / (4\pi d^2)$, the orbital distance corresponding to a given $S_{\rm eff}$ is

$$
d = (1\,\mathrm{AU}) \sqrt{\frac{L_\star/\Lsun}{S_{\rm eff}}}\,.
$$

The full 1D radiative-convective climate calculations of {cite:t}`Kopparapu2013` give the Kopparapu boundaries directly in $S_{\rm eff}$ values for Sun-like stars; we simply read them off and apply the formula above.

**Inner edge: the Simpson-Nakajima limit.** As recapped in {ref}`Lecture 9 <lecture09>`, the inner edge of the HZ is set by the runaway greenhouse limit. In a moist atmosphere, the outgoing longwave radiation (OLR) is bounded above by a critical value $F_{\rm OLR}^{\rm max} \approx 280$ W/m$^2$ set by the saturation pressure of water vapour {cite:p}`Pierrehumbert2010,Goldblatt2013`. Once the absorbed stellar flux exceeds this limit, the surface cannot reach radiative equilibrium and the oceans are driven into the atmosphere. For Sun-like stars, the {cite:t}`Kopparapu2013` runaway greenhouse limit corresponds to $S_{\rm in,eff} \approx 1.06$, giving

$$
d_{\rm in} = (1\,\mathrm{AU})/\sqrt{1.06} \approx 0.97\,\mathrm{AU}.
$$

Venus at $0.72$ AU receives $S_{\rm eff} \approx 1.9$ and sits well inside the inner edge.

**Outer edge: the maximum $\mathrm{CO_2}$ greenhouse.** The outer edge is set by a different mechanism. For $\mathrm{CO_2}$-rich atmospheres at low temperatures, increasing the atmospheric $\mathrm{CO_2}$ inventory does *not* warm the planet indefinitely: above a certain partial pressure, $\mathrm{CO_2}$ begins to condense out as ice clouds and surface ice rather than acting as a greenhouse gas. The maximum greenhouse warming achievable from any $\mathrm{CO_2}$ atmosphere therefore corresponds to a minimum stellar flux below which the surface cannot be kept above 273 K. The {cite:t}`Kopparapu2013` outer-edge limit for Sun-like stars is $S_{\rm out,eff} \approx 0.35$, giving

$$
d_{\rm out} = (1\,\mathrm{AU})/\sqrt{0.35} \approx 1.69\,\mathrm{AU}.
$$

Mars at $1.52$ AU is just inside the outer edge.

**Comparing across stellar types.** The habitable zone is therefore a stellar-mass-dependent strip that scales as $\sqrt{L_\star}$. Plugging in luminosities for representative spectral types:

- **G dwarfs** (Sun, $L \sim \Lsun$): $d_{\rm in} \approx 0.97$ AU, $d_{\rm out} \approx 1.69$ AU. Width $\sim 0.7$ AU. Lifetime $\sim 10$ Gyr. Modest stellar activity. The reference case for "typical" habitability.
- **K dwarfs** (e.g. $\epsilon$ Eri at $L \sim 0.3\,\Lsun$): $d_{\rm in} \approx 0.53$ AU, $d_{\rm out} \approx 0.93$ AU. Long main-sequence lifetimes ($\sim 17$ to $70$ Gyr across the K range, $\sim 24$ Gyr for $\epsilon$ Eri), modest flares, stable photospheres, and an HZ that is far enough out to avoid most tidal-locking and pre-main-sequence problems. {cite:t}`CuntzGuinan2016` argued on these grounds that K dwarfs may be the *most habitable* class of host star. Their UV/X-ray output is modest after the first Gyr ({numref}`fig:l14:cuntz-xray`), and their long lifetimes give biology more time to develop.
- **M dwarfs** (e.g. TRAPPIST-1, $L \sim 5 \times 10^{-4}\,\Lsun$): $d_{\rm in} \approx 0.022$ AU, $d_{\rm out} \approx 0.038$ AU. The HZ is inside the orbit of Mercury. Stars are extremely long-lived (up to $10^{12}$ yr), so the system has time, but the HZ is so close to the star that all planets are tidally locked, are exposed to intense stellar wind, and the most extreme cases (late M / ultracool dwarfs like TRAPPIST-1) went through a Gyr-long pre-main-sequence high-luminosity phase during which any HZ planet was in the runaway greenhouse state {cite:p}`LugerBarnes2015`. Early M dwarfs (M0 to M3) have much shorter pre-main-sequence phases of $\sim 50$ to $150$ Myr but still face the tidal-locking and flare-activity challenges.

The lifetimes quoted in the bullets above are not arbitrary: they follow from a one-line scaling. The total nuclear energy a star can release on the main sequence is proportional to the mass of hydrogen available for fusion, $E_{\rm nuc} \propto M_\star$, while its luminosity follows the empirical mass-luminosity relation $L_\star \propto M_\star^{3.5}$ for low- and intermediate-mass stars. The main-sequence lifetime is therefore the energy budget divided by the burn rate,

$$
t_{\rm MS} \;\sim\; \frac{E_{\rm nuc}}{L_\star} \;\propto\; \frac{M_\star}{M_\star^{3.5}} \;=\; M_\star^{-2.5} \,.
$$

Normalising on the Sun ($t_{\rm MS,\odot} \approx 10$ Gyr), this gives $t_{\rm MS} \approx 10\,(M_\star/\Msun)^{-2.5}$ Gyr. A K dwarf at $M_\star \approx 0.7\,\Msun$ then has $t_{\rm MS} \approx 10 \times 0.7^{-2.5} \approx 24$ Gyr; a $0.5\,\Msun$ early M dwarf has $\approx 57$ Gyr; and a $0.1\,\Msun$ M dwarf naively gives $\approx 3 \times 10^3$ Gyr, which is already longer than the age of the universe and which detailed stellar models extend further (to $\sim 10^{12}$ yr) once the fully convective regime keeps the entire hydrogen reservoir accessible to the core. The headline point is that *cooler stars give biology more time*, by a factor that grows steeply with decreasing stellar mass, which is the central reason the K-dwarf and M-dwarf habitable zones are taken seriously despite their other problems.

```{figure} figures/cuntz_guinan_xray_lyman.avif
:align: center
:name: fig:l14:cuntz-xray
:width: 75%

Lyman-$\alpha$ and X-ray irradiances, in erg s$^{-1}$ cm$^{-2}$, received by a planet at the homeothermic distance of its star, the distance at which it absorbs the same flux as Earth does from the Sun. Bars are grouped by spectral type and coloured by stellar age; the wide bar of each pair is Lyman-$\alpha$ and the narrow, paler bar is X-ray. Note the logarithmic vertical axis. At fixed age the irradiance rises by over 100 to 500 times from G2--8 to M4--6 dwarfs, and for a given star it falls by up to 500 times in X-rays between 0.1 and 5 Gyr while the Lyman-$\alpha$ decline is much gentler. Early K dwarfs are the compromise {cite:t}`CuntzGuinan2016` favour: long-lived and common, but without the extreme and long-lasting high-energy irradiation of the M dwarfs. Reproduced from {cite:t}`CuntzGuinan2016`.
```

The 1D values listed above for $d_{\rm in}$ are themselves a simplification. Three-dimensional global climate models that resolve clouds give a different answer for tidally locked planets around M dwarfs. {cite:t}`Yang2013` showed that on a planet that always presents the same face to its star, strong convection at the substellar point lifts thick water clouds that drive the local albedo above $\sim 0.6$ and act as a *stabilising* feedback against runaway warming ({numref}`fig:l14:yang-clouds`). The result is that the inner edge of the HZ, defined as the largest stellar flux at which surface temperature stays below the runaway threshold, shifts inward by roughly a factor of two relative to the 1D Kopparapu boundary. The 1D HZ therefore *under-estimates* the inner edge of the M-dwarf HZ, and the corresponding occurrence of habitable planets around M dwarfs is correspondingly larger than the 1D values would suggest.

```{figure} figures/yang2013_tidally_locked_clouds.avif
:align: center
:name: fig:l14:yang-clouds
:width: 90%

Climate response of tidally locked rocky planets to varying stellar flux from a 3D general-circulation model with clouds, from {cite:t}`Yang2013`. (a) Substellar surface temperature, (b) stratospheric water vapour mixing ratio, (c) planetary albedo, and (d) greenhouse warming, all as functions of incident stellar flux for spin-orbit resonances 1:1, 2:1, 6:1, a 1:1 case with clouds suppressed (red dashed), and a 1:1 case around a K dwarf (blue). The grey band marks the 1D habitable-zone limit. Substellar convective clouds drive the planetary albedo to $\sim 0.6$ in the 1:1 cases and prevent the surface from running away even at twice the 1D inner-edge flux; with clouds suppressed (red dashed), the runaway sets in at much lower flux. Reproduced from {cite:t}`Yang2013`.
```

The combined effect of these climatological corrections is captured in the {cite:t}`Shields2016` summary diagram ({numref}`fig:l14:shields-mdwarf-hz`), which compiles the 1D Kopparapu boundaries together with 3D GCM corrections from a number of independent groups and overlays the known M-dwarf and FGK habitable-zone planets. The figure makes two points at once. First, the 3D inner edge for slowly rotating and tidally locked planets lies at roughly 1.7 to 2.2 times the flux of the 1D inner edge across the whole FGKM range, so it is well inside it. Second, the tidal-locking radius (grey dashed curve) cuts across the M-dwarf HZ, so essentially every M-dwarf HZ planet known today is tidally locked and is therefore in the regime where the cloud corrections matter.

```{figure} figures/shields2016_hz_tidally_locked.avif
:align: center
:name: fig:l14:shields-mdwarf-hz
:width: 80%

Habitable-zone limits in the stellar effective temperature--stellar flux plane for FGKM hosts, from the {cite:t}`Shields2016` review of M-dwarf habitability. Note that stellar flux increases to the left. The green and blue solid curves are the {cite:t}`Kopparapu2013` 1D inner (runaway greenhouse) and outer (maximum-$\mathrm{CO_2}$ greenhouse) edges. The two dotted curves are inner edges computed with the CAM3 general-circulation model: red for slowly rotating and tidally locked planets, black for rapidly rotating planets. The grey dashed curve is the tidal-locking radius. Single-model inner-edge estimates are plotted as the legend symbols, for a dry planet around a G dwarf (Abe et al. 2011), for Earth with the LMD Generic model (Leconte et al. 2013), from {cite:t}`Yang2013`, and with a modified radiative-transfer code (Wolf & Toon 2014). Filled circles are solar system planets, including early Venus and early Mars, and known exoplanets; magenta marks those interior to the 1D inner edge and green those within the 1D habitable zone. The red curve lies at about 1.7 to 2.2 times the flux of the green one, so clouds move the inner edge substantially closer to the star, and that is the regime almost every M-dwarf planet in the figure occupies. Reproduced from {cite:t}`Shields2016`, after Yang et al. (2014).
```

The tidal-locking radius itself is not a free parameter: it follows from how fast tides can despin a rotating planet. For a rocky planet of mass $M_p$, radius $R_p$, moment of inertia $I_p \approx \alpha_p M_p R_p^2$ (with the dimensionless moment-of-inertia factor $\alpha_p \approx 0.33$ for an Earth-like differentiated body), tidal Love number $k_{2,p}$, and quality factor $Q_p$, orbiting a star of mass $M_\star$ at semi-major axis $a$, the timescale to despin from an initial spin rate $\omega_0$ to synchronous rotation is, to order of magnitude,

$$
\tau_{\rm lock} \;\sim\; \frac{\omega_0 \, a^6 \, I_p \, Q_p}{3 \, G \, M_\star^2 \, k_{2,p} \, R_p^5} \,.
$$

The strong $a^6$ dependence (an inverse-cube tidal force squared) means the answer changes by many orders of magnitude across the HZ. Plugging in Earth-like parameters ($\alpha_p \approx 0.33$, $k_{2,p} \approx 0.3$, $Q_p \approx 100$, $\omega_0 \sim 2\pi/(\text{day})$) for an Earth analogue at $a = 1$ AU around the Sun gives $\tau_{\rm lock} \sim 10^{12}$ yr, comfortably longer than the age of the universe, so an Earth analogue at 1 AU around a Sun-like star is not tidally locked. For a TRAPPIST-1 b analogue, however, $a \approx 0.011$ AU and $M_\star \approx 0.08\,\Msun$ shrink the numerator and the denominator together; the strong $a^6$ scaling dominates, so the net effect is that $\tau_{\rm lock}$ drops by many orders of magnitude to $\sim 10^7$ yr or shorter (the precise value depends on the highly uncertain $Q_p$), which is in any case far shorter than the $\sim 8$ Gyr age of the TRAPPIST-1 system. Every TRAPPIST-1 inner planet has therefore had ample time to reach a tidally locked or near-locked spin state, and the same conclusion holds for essentially every M-dwarf HZ planet known today. The 3D climate corrections in {numref}`fig:l14:shields-mdwarf-hz` are not an academic complication: they apply to the regime in which essentially all M-dwarf HZ planets sit.

**Key insight.** The HZ as derived above is a useful 1D radiative limit. It is *well-defined* as a thermodynamic boundary on the location of liquid surface water, but it is *not* a sufficient condition for habitability. Real habitability also depends on planetary boundary conditions (volatile inventory, tectonic regime, escape history, magnetic shielding, evolutionary trajectory) that the 1D HZ ignores. Part 2's coupling loop is the qualitative version of what a full 3D climate-evolution model computes quantitatively for an individual planet.
````

## Part 3: Astrobiology and the search for life

### What is life?

Astrobiology operates without an agreed-upon definition of life.
The working definition, going back to {cite:t}`Lederberg1965`, is that **life** is a self-replicating, metabolising, evolving chemical system.
This operational definition lets us decide what to look for.

The search for life elsewhere is dominated by carbon-based, water-as-solvent biology because we know its spectroscopic and geochemical fingerprints.
Alternative biochemistries (silicon-based, ammonia-solvent, methane-solvent) are not excluded in principle, but they are not our default working hypothesis.

### Extremophiles and the redefinition of "habitable"

Historically, the operational definition of "habitable" assumed conditions under which temperate Earth surface organisms thrive.
The discovery of **extremophiles**, organisms thriving far outside that range, has substantially relaxed this definition.

Earth life occupies environments from hydrothermal vents over 120 $^\circ$C to subglacial lakes at $-20$ $^\circ$C, saturated brine, and hyperacidic drainage.
The implication for astrobiology is that the classical HZ, defined for surface liquid water on a temperate Earth-like planet, may be too restrictive.
Subsurface oceans on icy moons and high-pressure environments cannot be excluded on energetic grounds.

Icy moons (Europa, Enceladus, Titan) became primary astrobiology targets, formalised in NASA's *Roadmap to Ocean Worlds* {cite:p}`HendrixVance2019`.
None are in the classical HZ, yet all have liquid water in contact with rock and a chemical free-energy gradient ({ref}`Lecture 11 <lecture11>`).

### Origin of life on Earth

The origin of life on Earth remains an unsolved scientific problem with several competing hypotheses:

- **RNA world**: the hypothesis that self-replicating RNA preceded protein-based metabolism.
  This model is supported by catalytic ribozymes in modern organisms and the ribosome, but prebiotic nucleotides do not easily polymerise without templating and are unstable on long timescales.
- **Metabolism-first**: the hypothesis that chemical autocatalytic cycles preceded genetic information storage.
  Submarine alkaline hydrothermal vents produce $\mathrm{H_2}$, methane, and redox disequilibrium gradients between fluid and seawater that resemble primitive metabolism {cite:p}`Russell2014`.
- **Surface "warm little ponds"**: the hypothesis that wet-dry cycling in shallow surface pools concentrates and polymerises prebiotic nucleotides {cite:p}`Sasselov2020`.
- **Panspermia**: the hypothesis that life arrived on meteorites or comets, which relocates the origin question to another planetary body rather than solving it.

The earliest direct evidence of life on Earth dates to about 3.5 Ga from microbial mat structures in Australia and South Africa.
Possible isotopic and morphological biosignatures have been claimed at $\sim 3.8$ Ga in Isua banded iron formations {cite:p}`Mojzsis1996` and, more controversially, up to $\sim 4.3$ Ga in the Nuvvuagittuq Supracrustal Belt (minimum age $\sim 3.77$ Ga) {cite:p}`Dodd2017`.
If validated, life arose within a few hundred Myr of the cooling of Earth's surface.

The unknown frequency of abiogenesis represents the largest uncertainty in quantitative habitability estimates, leaving $f_l$ in the Drake equation unconstrained.
A second independent origin of life on Mars or an icy moon would provide the first empirical constraint on $f_l$.

### Biosignatures: what would we look for?

A **biosignature** is an observable feature whose presence is more easily explained by biology than by abiotic processes alone.
{cite:t}`Schwieterman2018` divide remotely detectable biosignatures into atmospheric gases, surface reflectance features, and temporal variability.
{cite:t}`Catling2018` evaluate candidate biosignatures within a Bayesian framework that updates the probability of life given planetary and stellar context ({numref}`fig:l14:catling-framework` and {numref}`fig:l14:catling-bayes`).

```{figure} figures/catling2018_assessment_framework.avif
:align: center
:name: fig:l14:catling-framework
:width: 75%

The four-component framework for assessing exoplanet biosignatures from {cite:t}`Catling2018`. The left side characterises the host star and the planet's external context; the right side characterises the planet's internal properties; the centre searches for biosignatures and tests for false positives. Each branch corresponds to a class of measurement that the next generation of telescopes is being designed to deliver. Reproduced from {cite:t}`Catling2018`.
```

```{figure} figures/catling2018_bayesian_framework.avif
:align: center
:name: fig:l14:catling-bayes
:width: 80%

A Bayesian framework for biosignature assessment. Spectral or photometric observations of an exoplanet must be combined with prior probabilities (from theory and from observations of the broader population) to compute the posterior probability that the planet hosts life. Detection is therefore not a yes-or-no statement about a single observation but a quantitative inference from a chain of measurements. Reproduced from {cite:t}`Catling2018`.
```

On Earth, single gas biosignatures include $\mathrm{O_2}$ ($\sim 21\%$), photochemical $\mathrm{O_3}$, biogenic $\mathrm{CH_4}$, and $\mathrm{N_2O}$.
The most diagnostic signatures are combinations in **chemical disequilibrium**, where coexisting gases react rapidly and require continuous resupply.
{cite:t}`Krissansen2018` calculated an available Gibbs energy of about 2326 J/mol for modern Earth, compared to about 136 J/mol for Mars.
On the Archean Earth (roughly 4.0 to 2.5 billion years ago), coexisting $\mathrm{CH_4}$, $\mathrm{CO_2}$, $\mathrm{N_2}$, and liquid $\mathrm{H_2O}$ formed a disequilibrium biosignature that cannot persist abiotically ({numref}`fig:l14:biosig-gases`).

```{figure} figures/schwieterman2018_biosignature_gases.avif
:align: center
:name: fig:l14:biosig-gases
:width: 90%

Wavelength-resolved infrared absorption features for ten potential biosignature gases ($\mathrm{O_2}$, $\mathrm{O_3}$, $\mathrm{N_2O}$, $\mathrm{CH_4}$, $\mathrm{CH_3Cl}$, $\mathrm{C_2H_6}$, $\mathrm{NH_3}$, DMS, DMDS, $\mathrm{CH_3SH}$). Each panel plots the line-by-line absorption strength versus wavelength from $0.4$ to $20\,\mu\mathrm{m}$. Different molecules have characteristic absorption regions: $\mathrm{O_3}$ near $9.6\,\mu\mathrm{m}$, $\mathrm{CH_4}$ at $3.3$ and $7.7\,\mu\mathrm{m}$, $\mathrm{N_2O}$ across the mid-infrared, and DMS/DMDS in the $6$ to $15\,\mu\mathrm{m}$ window (with characteristic bands near $6$-$7$, $8$-$12$, and $14$-$15\,\mu$m). Reproduced from {cite:t}`Schwieterman2018`.
```

Atmospheric composition reflects the integrated history of escape, weathering, and biology.
Earth's atmosphere is highly fractionated relative to solar composition, showing noble gas and hydrogen depletion alongside $\mathrm{O_2}$ enrichment that abiotic processes cannot sustain in the presence of liquid water.
Such fractionation patterns provide circumstantial evidence for life ({numref}`fig:l14:biosig-classes`).

```{figure} figures/schwieterman2018_biosignature_classes.avif
:align: center
:name: fig:l14:biosig-classes
:width: 95%

The three classes of remotely detectable biosignatures: gaseous (left), surface (middle), and temporal (right). Gaseous biosignatures are produced as direct or indirect by-products of biological processes (e.g. photosynthetic $\mathrm{O_2}$, photochemically derived $\mathrm{O_3}$). Surface biosignatures are spectral signatures imparted by reflected light interacting with biological pigments (e.g. the vegetation red edge). Temporal biosignatures are time-dependent variations in atmospheric or surface properties caused by biology (e.g. the seasonal Keeling curve in Earth's $\mathrm{CO_2}$). A convincing biosignature claim should ideally combine evidence from more than one of these classes. Reproduced from {cite:t}`Schwieterman2018`.
```

Surface biosignatures include the **vegetation red edge**, a sharp reflectance jump at $\sim 700$ nm characteristic of chlorophyll-bearing plants.
Temporal biosignatures comprise seasonal cycles in atmospheric gas abundances (such as $\mathrm{CO_2}$ and $\mathrm{CH_4}$) and seasonal surface reflectance variations from vegetation growth.

Returned-sample biosignatures, accessible only via spacecraft missions in the solar system, include microfossils, specific organic molecules (amino acids and lipids), and metabolic isotopic patterns such as light-carbon enrichment.

### False positives and the inverse problem

Most candidate biosignature gases have a known abiotic production pathway under plausible planetary conditions {cite:p}`Meadows2018`:
- Abiotic $\mathrm{O_2}$ from **photolysis** (the breakdown of a molecule by absorbed stellar light) of $\mathrm{H_2O}$ followed by hydrogen escape, especially around active M dwarfs, or from $\mathrm{CO_2}$ photolysis {cite:p}`Wordsworth2014`.
- Abiotic $\mathrm{CH_4}$ from **serpentinisation** (the reaction of olivine with water to form serpentine minerals and release hydrogen), or volcanic outgassing at low oxygen fugacity.
- Abiotic $\mathrm{N_2O}$ from lightning chemistry and photochemical pathways.
- Dimethyl sulfide ($\mathrm{(CH_3)_2S}$, DMS) is the notable exception: it lacks known abiotic sources on Earth, but one could exist elsewhere.

Biosignature detection is therefore an **inverse problem**: a single detection cannot prove life.
Robust life detection requires context, gas combinations, and multi-wavelength observations that constrain planetary state, escape history, and atmospheric composition together.

### Solar system targets for life detection

The solar system contains five plausible targets for life detection.

**Mars** ({ref}`Lecture 10 <lecture10>`) is the most direct path to laboratory-based life detection on another world.
Curiosity and Perseverance established that Mars had liquid water, neutral pH, and complex organic molecules at $\sim 3.5$ to $4$ Ga.
Present-day habitability is more uncertain: the methane variability detected by Curiosity is intriguing but cannot be interpreted as biological without independent corroboration.
The Mars Sample Return campaign remains the most direct path to laboratory analysis of returned material in full spatial and chemical context {cite:p}`MeyerMSPG2022`.

**Europa** ({ref}`Lecture 11 <lecture11>`) has a global subsurface saltwater ocean confirmed by Galileo induced magnetic field measurements and surface brine chemistry.
NASA's Europa Clipper (launched October 2024, arriving 2030) will conduct $\sim 50$ flybys to characterise ice shell thickness, ocean chemistry, and surface activity {cite:p}`Howell2020`.

**Enceladus** ({ref}`Lecture 11 <lecture11>`) ejects samples of its subsurface ocean directly into space through its south-polar plume.
Cassini detected $\mathrm{H_2}$ from active serpentinisation at the rocky core, macromolecular organics, and sodium phosphates indicating phosphorus-rich ocean chemistry {cite:p}`Waite2017,Postberg2023`.
Proposed missions like the Enceladus Orbilander would sample plume material for organics, isotopes, and cellular structures.

**Titan** ({ref}`Lecture 11 <lecture11>`) is the only body other than Earth with stable surface liquids today, featuring methane and ethane lakes and active prebiotic photochemistry.
NASA's Dragonfly rotorcraft (launch 2028, arrival 2034) will sample surface chemistry directly at Selk crater with mass spectrometry {cite:p}`Lorenz2018`.

**Venus cloud layer.** {cite:t}`Greaves2021` claimed phosphine ($\mathrm{PH_3}$) in the temperate cloud deck at altitudes of $50$ to $60$ km as a possible biosignature lacking known abiotic sources.
Reanalyses of JCMT and ALMA data showed the spectral feature was at the instrumental sensitivity limit and consistent with mesospheric $\mathrm{SO_2}$ {cite:p}`Lincowski2021` ({numref}`fig:l14:phosphine`).
Independent observations failed to confirm the detection, setting lower upper limits.

```{figure} figures/lincowski2021_phosphine_so2.avif
:align: center
:name: fig:l14:phosphine
:width: 90%

Spectral simulations of the 266.94 GHz feature claimed as $\mathrm{PH_3}$ in the Venus clouds, showing that the same data are also consistent with mesospheric $\mathrm{SO_2}$ at the few-hundred-ppb level (rising from $\sim 30$ ppb at 78 km to $\sim 400$ ppb at 100 km altitude). The original {cite:t}`Greaves2021` detection sits at the edge of the instrumental noise floor and the alternative $\mathrm{SO_2}$ interpretation cannot be excluded. Reproduced from {cite:t}`Lincowski2021`.
```

The Venus phosphine episode parallels the K2-18 b DMS controversy on the exoplanet side.
In both cases, data at instrumental sensitivity limits allow plausible abiotic explanations that have not been ruled out.
Extraordinary claims about biosignatures require extraordinary verification through independent datasets.

Upcoming missions to Venus will provide higher-precision data.
The DAVINCI descent probe will measure cloud chemistry and noble gases in situ, while EnVision and VERITAS (targeting 2031) will map the atmosphere and surface.
These missions will resolve the phosphine claim and constrain present-day Venus cloud chemistry.

**Pedagogical point.** The Venus phosphine and K2-18 b DMS cases show that claims about life-relevant chemistry must clear a high bar through better data rather than rhetoric.
Both controversies drive the design of next-generation instruments and missions.

### Exoplanet life detection: the strategy

Exoplanet life detection relies entirely on spatially unresolved transmission, emission, or reflectance spectra ({numref}`fig:l14:lhs475b-spectrum`, {numref}`fig:l14:trappist1b`).

```{figure} figures/lustigyaeger2023_lhs475b_spectrum.avif
:align: center
:name: fig:l14:lhs475b-spectrum
:width: 85%

JWST/NIRSpec G395H transmission spectrum of the Earth-sized rocky exoplanet LHS 475 b (black points), compared with model atmospheres of various compositions. The data rule out clear hydrogen-dominated atmospheres at $1\times$ to $100\times$ solar metallicity at high significance (top panel). High mean molecular weight atmospheres (pure $\mathrm{H_2O}$, $\mathrm{CO_2}$-dominated, Earth-like) and a featureless airless-body spectrum remain consistent with the data, while a clear $\mathrm{CH_4}$-dominated atmosphere is weakly disfavoured (bottom panel). This is representative of what current JWST observations can and cannot say about the atmospheres of rocky exoplanets around nearby M dwarfs. Reproduced from {cite:t}`LustigYaeger2023`.
```

```{figure} figures/greene2023_trappist1b_eclipse.avif
:align: center
:name: fig:l14:trappist1b
:width: 80%

JWST MIRI secondary eclipse light curve of TRAPPIST-1 b at 15 $\mu$m. The observed eclipse depth corresponds to a measured dayside brightness temperature of $T_d \approx 503$ K, consistent with the 508 K bare-rock zero-redistribution prediction and indicating that the planet has no thick atmosphere to redistribute heat. Reproduced from {cite:t}`Greene2023`.
```

As shown for K2-18 b in {ref}`Lecture 13 <lecture13>`, a single-snapshot atmospheric detection is insufficient to establish the presence of biology ({numref}`fig:l14:k218b-spec`, {numref}`fig:l14:k218b-post`).

```{figure} figures/madhusudhan2023_k218b_spectrum.avif
:align: center
:name: fig:l14:k218b-spec
:width: 90%

JWST transmission spectrum of K2-18 b from {cite:t}`Madhusudhan2023`. The combined NIRSpec and NIRISS data show clear $\mathrm{CH_4}$ and $\mathrm{CO_2}$ absorption features and the tentative DMS feature near 3.4 $\mu$m. The spectrum is consistent with a sub-Neptune atmosphere overlying either a "hycean" (hydrogen atmosphere over a global liquid-water ocean) layer or a deeper mini-Neptune envelope. Reproduced from {cite:t}`Madhusudhan2023`.
```

```{figure} figures/madhusudhan_k218b_dms_post.avif
:align: center
:name: fig:l14:k218b-post
:width: 90%

Posterior probability distributions for the mixing ratios of $\mathrm{CH_4}$, $\mathrm{CO_2}$, and DMS in the atmosphere of K2-18 b, for three retrievals that differ only in how many instrument offsets are allowed to float: none (blue), one (orange), and two (pink). The horizontal bars give each distribution's median and $1\sigma$ interval. $\mathrm{CH_4}$ and $\mathrm{CO_2}$ are recovered at about $5\sigma$ and $3\sigma$ and their posteriors shift only slightly between the three cases. The DMS posterior behaves in the opposite way: $2.4\sigma$ with no offset, about $1\sigma$ with one, and no longer significant with two. That sensitivity to a nuisance parameter is exactly the inverse-problem issue that makes single-snapshot biosignature claims hard to validate. Reproduced from {cite:t}`Madhusudhan2023`.
```

A convincing biosignature detection requires chemical disequilibrium, temporal variability, environmental context excluding abiotic pathways, and independent confirmation.
The Habitable Worlds Observatory (HWO; {cite:t}`NAS2021`) will use a $\sim 6$ m space-based **coronagraph** (an instrument masking starlight to image faint planets) to characterise Earth-like planets around $\sim 25$ Sun-like stars in the 2040s.
Complementing this, the LIFE concept uses a mid-infrared **nulling interferometer** (an array cancelling starlight by destructive interference) to measure diagnostic biosignature gases {cite:p}`Quanz2022` ({numref}`fig:l14:life-yields`).

```{figure} figures/quanz2022_life_yields.avif
:align: center
:name: fig:l14:life-yields
:width: 90%

Predicted total exoplanet detection yields for the LIFE concept during a 2.5-year search phase, as a function of mirror aperture diameter ($D = 1$ to $3.5$ m), shown for two assumed instrument scenarios (lower and upper bars). A 3.5 m aperture LIFE configuration would detect of order $500$ to $800$ planets in total; for the 2 m reference case, {cite:t}`Quanz2022` report up to $\sim 550$ detectable planets, of which 25 to 45 are rocky planets orbiting within the empirical habitable zone of their host stars. Reproduced from {cite:t}`Quanz2022`.
```

Dedicated exoplanet life-detection flagships are expected in the 2040s following 2030s statistical surveys.
Future observatories will constrain $f_l$, transforming the search for life into an empirical science.

## Course wrap-up

### The five biggest things we have learned

1. **Planet formation** is a physical process governed by accretion, gravity, and disk dynamics, producing a predictable diversity of outcomes.
2. **Planetary interiors** are heat engines whose evolution drives surface tectonics, volcanic outgassing, magnetic dynamos, and long-term habitability on Gyr timescales.
3. **Atmospheres** are dynamic systems that form, evolve, escape, and react with interiors and surfaces, so no default atmosphere exists.
4. **Habitability** is a coupled systems property linking stellar, orbital, planetary, and biospheric factors across star, atmosphere, surface, and interior.
5. The **solar system** is a detailed reference case, while the exoplanet population provides the statistical context for what is typical.

### The five biggest open questions

1. Whether the **origin of life** is a rare accident or a generic chemical inevitability remains the largest uncertainty in quantitative habitability estimates.
2. The **radius valley** between super-Earths and sub-Neptunes tests whether photoevaporation, core-powered mass loss, or distinct formation channels govern atmospheric loss.
3. When **Jupiter** formed determines whether it was the architect of the inner solar system, shaping the NC-CC dichotomy and Earth-like system rarity.
4. **Mars Sample Return** provides the most direct test of whether Mars was ever inhabited, recalibrating our prior on $f_l$.
5. Determining whether the **solar system** is rare or typical using PLATO, Gaia DR4/DR5, and long-baseline RV will yield a probabilistic answer.

### The next decade

The mission queue from now to roughly 2040 is unusually rich.
Dates reflect planning targets as of September 2026.

Through 2030, JWST continues to deliver exoplanet atmospheric spectra.
Europa Clipper arrives at Jupiter in 2030 to study ice-shell and ocean chemistry.
JUICE arrives at Jupiter in 2031, entering Ganymede orbit in 2034.
Roman launched in August 2026, followed by PLATO in 2027, Dragonfly in 2028, and Ariel in 2029.

In the 2030s, Dragonfly arrives at Titan in 2034, and Ariel delivers its statistical exoplanet atmosphere survey.
ELT ({numref}`fig:l14:elt-milkyway`), GMT, and TMT come online for high-contrast imaging and high-resolution spectroscopy of nearby exoplanets.
DAVINCI, EnVision, and VERITAS deliver Venus results, alongside planned Mars Sample Return delivery.
A recommended Uranus orbiter targets launch in the mid-to-late 2030s at the earliest.

```{figure} figures/elt_milkyway.avif
:name: fig:l14:elt-milkyway
:width: 700px
:align: center

The Milky Way arcs over ESO's Extremely Large Telescope under construction on Cerro Armazones in the Chilean Atacama Desert, with the partially-clad dome visible at lower left (August 2025). With its 39 m segmented primary mirror, the ELT will be the largest optical/near-infrared telescope ever built when it sees first light in 2029 and will, together with GMT and TMT, enable the first direct-imaging searches for atmospheric biosignatures on rocky planets around nearby M dwarfs. Image credit: C. Letelier/ESO {cite:p}`ESOELT2025`.
```

In the 2040s, HWO and LIFE concept maturation transitions into hardware.
This enables direct atmospheric characterisation and multi-line biosignature searches on Earth-analogue exoplanets.

### Final framing

Planetary science has become the science of comparative climate, interior, and life-hosting trajectories.
The solar system is the reference system, but no longer the benchmark.
The exoplanet population provides the statistical context that the solar system on its own cannot.
The questions covered across this course are open questions on a moving frontier.

A course like this is necessarily a snapshot.
Specific topics, such as the Drake equation or the radius valley mechanism, will look different in 2030 than today.
The physics and the questions, however, will be largely the same.
The central lesson of these fourteen lectures is the **systems-level view**, the principle that habitability, formation, escape, weathering, and biology form a single coupled problem with consistent physical principles across the galaxy.

## References

```{bibliography}
:filter: docname in docnames
```
