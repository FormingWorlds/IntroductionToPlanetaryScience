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

Thirteen lectures have built a single argument from the bottom up. Lectures 1 and 2 introduced the solar system and the protoplanetary disks in which planets form. Lectures 3 and 4 followed the heat and chemistry that drive interior evolution and differentiation. Lectures 5 and 6 added the atmospheres that sit on top of those interiors and connect the planet to the star above it. Lecture 7 examined the surfaces where interior, atmosphere, and external bombardment leave their record. Lecture 8 used seismology, gravity, and rotation to look back inside. Lectures 9 to 12 then walked the solar system body by body: Earth and Venus as the canonical comparative experiment ({ref}`Lecture 9 <lecture09>`), Mercury and Mars as the small-body endmembers ({ref}`Lecture 10 <lecture10>`), the gas and ice giants as different physical regimes altogether ({ref}`Lecture 11 <lecture11>`), and the small-body populations that record the formation epoch ({ref}`Lecture 12 <lecture12>`). Lecture 13 then stepped outside the solar system and showed how the same physics applies, statistically, to several thousand other planetary systems detected since 1995 {cite:p}`MayorQueloz1995`.

The thread that runs through all of this is simple: physical processes (accretion, gravity, radiation balance, phase change, escape, convection, weathering, biology) shape planetary outcomes, and the same processes operate everywhere. The diversity of planets in the galaxy, and the differences between Earth, Venus, and Mars, both reflect the same small set of physical levers operating across a wide range of boundary conditions.

This final lecture is the synthesis. It does three things in turn. Part 1 places the solar system inside the exoplanet population we now have, identifying where it is typical and where it is atypical. Part 2 reframes habitability not as a checklist or a one-dimensional zone but as a coupled systems property, in which star, orbit, interior, atmosphere, surface, and biosphere all feed back on one another. Part 3 turns to astrobiology proper: what we would actually look for, where we should look for it, and how confident we can be in the answers. The blackboard derivation between Parts 2 and 3 reconstructs the classical habitable zone from the simplest possible energy balance, and the lecture closes with a wrap-up of the course as a whole.

### Planet formation theory meets observation

Lectures 2, 3, and 12 already presented the modern picture of how planets form, but it is worth restating the structure compactly. A young star is surrounded for a few Myr by a disk of gas and dust whose total mass is a few percent of the stellar mass. Within that disk, sub-micron dust grains coagulate into millimetre-sized pebbles, which collect in pressure traps and form **planetesimals**, bodies from roughly a kilometre to a few hundred kilometres across, through the streaming instability, a gravitational clumping instability triggered once drifting pebbles pile up densely enough. Some planetesimals then grow further by sweeping up local material (oligarchic growth) and by accreting drifting pebbles (pebble accretion); the largest cores reach the threshold for runaway gas accretion before the disk dissipates and become gas giants {cite:p}`Drazkowska2023,Pollack1996,Lambrechts2012` ({numref}`fig:l14:formation-overview` and {numref}`fig:l14:envelope-accretion`).

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

Each of those steps has direct observational consequences. ALMA images of nearby protoplanetary disks resolve the gaps and rings that mark planetary formation in progress {cite:p}`ALMAPartnership2015,Andrews2018` ({numref}`fig:l14:dsharp`). Disk lifetimes inferred from infrared excess fractions cluster around 3 to 5 Myr {cite:p}`Haisch2001`, which sets the maximum time available for both terrestrial-planet assembly and gas-giant envelope accretion. Demographic surveys of mature systems then provide the endpoint distributions that any formation theory must reproduce.

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

The successes of this framework are real. Disk-driven migration explains why hot Jupiters exist in the first place and why several systems are caught in tight resonant chains, successions of planets whose orbital periods lock into near-integer ratios of one another: the planets formed further out and migrated inward through the gas disk before it dispersed {cite:p}`Paardekooper2023,Tsiganis2005`. Pebble accretion explains how gas-giant cores grow fast enough to trigger envelope runaway before the disk is gone {cite:p}`Lambrechts2012,Johansen2007` ({numref}`fig:l14:accretion-timescales`). The carbonaceous-versus-non-carbonaceous (NC--CC) meteorite dichotomy points to early reservoir separation in the inner solar system, and it can be reproduced if Jupiter's growing core opens a barrier in the disk that segregates inner and outer material {cite:p}`Kruijer2017,Lichtenberg2021` ({numref}`fig:l14:nccc-timeline`). The Nice model, in which the giant planets' orbits become dynamically unstable and settle into their present spacing after the gas disk is gone, and the Grand Tack, in which Jupiter migrates inward and then back outward through the disk, reproduce the orbital and small-body architecture of the present solar system, including the Trojan asteroids, small bodies clustered roughly 60 degrees ahead of and behind Jupiter in its orbit, and the depleted asteroid belt {cite:p}`Tsiganis2005,Walsh2011`.

```{figure} figures/lichtenberg2023_nccc_timeline.avif
:align: center
:name: fig:l14:nccc-timeline
:width: 80%

Timeline of solar system formation reconstructed from isotopic dating of meteoritic materials. The non-carbonaceous (NC, red) and carbonaceous (CC, blue) reservoirs maintain distinct isotopic signatures from CAI (calcium-aluminium-rich inclusion, among the earliest solids to condense in the solar system) formation onwards, indicating that they accreted in physically separated regions of the disk for at least the first 2--3 Myr. Reproduced from {cite:t}`Lichtenberg2023`.
```

Open questions remain, and they are interesting. The radius valley at $\sim 1.8\,\Rearth$ in the Kepler population, discovered by {cite:t}`Fulton2017`, tells us that close-in small planets divide cleanly into volatile-poor super-Earths and volatile-rich sub-Neptunes, but the physics that produces the gap is not yet decided. Photoevaporation by stellar XUV {cite:p}`Owen2017` and core-powered mass loss from internal residual heat {cite:p}`Gupta2019` both predict a valley in the right location, and current data are not sharp enough to reject either mechanism ({numref}`fig:l14:fulton-valley`).

```{figure} figures/fulton2017_radius_valley.avif
:align: center
:name: fig:l14:fulton-valley
:width: 70%

The "Fulton gap" in the radius distribution of small close-in exoplanets. The two-dimensional map of planet size against incident stellar light shows a deficit of planets at $\sim 1.8\,\Rearth$ that separates a denser super-Earth population from a sub-Neptune population. The lower panel overlays the predictions of photoevaporation models, which can reproduce both the location and the slope of the valley with stellar irradiation. Reproduced from {cite:t}`Fulton2017`.
```

A second open question is the timing of Jupiter's formation. The {cite:t}`Kruijer2017` interpretation of the NC--CC dichotomy requires Jupiter's core to reach pebble-isolation mass within $\sim 1$ Myr of CAI formation, which is fast even for pebble accretion. {cite:t}`Lichtenberg2021` and others have shown that the same isotopic dichotomy can be reproduced without requiring such an early Jupiter, if the snow line, the disk radius beyond which water ice can condense, itself acts as the reservoir barrier. This is currently unresolved and matters for whether Jupiter set the boundary conditions of inner-system planet formation, or whether the inner solar system was largely indifferent to Jupiter's growth history.

A third, and pedagogically important, question is why the solar system contains no super-Earth or sub-Neptune at all. The Kepler statistics show that planets in the radius range $1$ to $4\,\Rearth$ are the most common type of planet in the galaxy {cite:p}`Bryson2021`, and yet our system simply skips that range entirely. Whether this is because Jupiter blocked inner-system pebble flux, because the local solid surface density was unusually low, or because of stochastic dynamical history, is one of the central open problems in formation theory.

Population synthesis models, which simulate large numbers of forming planetary systems under varied initial conditions to predict the statistical distribution of outcomes, are built on top of the formation framework and now reproduce the broad distribution of observed exoplanet types in mass and orbital period ({numref}`fig:l14:popsyn`), but only if they include both planetesimal and pebble accretion contributions, atmospheric loss, and dynamical evolution. The "missing" super-Earths in the solar system are not a generic prediction of formation theory: they appear in the synthetic populations and so the failure to produce them in the solar system is, in the current models, a special outcome that requires explanation rather than the default.

```{figure} figures/drazkowska2023_population_synthesis.avif
:align: center
:name: fig:l14:popsyn
:width: 90%

Population synthesis predictions for planet mass versus orbital period assuming planetesimal accretion (panel A) and pebble accretion (panel B). Both models populate the super-Earth, hot Jupiter, warm gas giant, and cold gas giant regimes, with super-Earth mass fractions of $\sim 35\%$ in models with pebble accretion. Reproduced from {cite:t}`Drazkowska2023`.
```

### The solar system overlaid on the exoplanet diagram

The cleanest way to see the architecture our own system does not have is to plot the transiting population on a single period-radius diagram and mark the compact multi-planet systems on it ({numref}`fig:l14:periodradius`).

```{figure} figures/raymond2022_period_radius.avif
:align: center
:name: fig:l14:periodradius
:width: 70%

Census of confirmed transiting exoplanets in orbital period and planet size. Open circles are all transiting planets. The box in the top panel is the region used to define a compact multi, a system with at least two planets inside it, and the filled circles are the planets that meet that definition. The middle panel joins the planets of five compact multis whose sizes and spacings are unusually uniform (Kepler-11, Kepler-172, Kepler-374, Kepler-444, Kepler-1542), the "peas-in-a-pod" pattern. The bottom panel joins three systems that do not show it: WASP-47 and KOI-94 meet the compact-multi definition but span a wide range of planet sizes, and the young system V1298 Tau fails it. Reproduced from {cite:t}`Weiss2023`.
```

What does the comparison show? In four respects the solar system looks utterly typical: small rocky planets sit close to the star, gas giants sit further out, ice giants and small icy bodies sit further out still, and the radial composition gradient runs from rocky to icy. Compositional gradients of that kind are general consequences of forming planets in a disk with a snow line, and they appear in many exoplanet systems too {cite:p}`Weiss2023,Drazkowska2023`.

In four other respects, however, the solar system looks unusual:

1. **No super-Earth or sub-Neptune.** As just discussed, our system contains no planet between Earth ($1\,\Rearth$) and Neptune ($\sim 4\,\Rearth$). Yet the most common single class of planet detected in the Kepler survey lies in exactly that range, and most stars host at least one such planet within a 1 AU orbit {cite:p}`Bryson2021,Bergsten2022`.
2. **Wide, low-eccentricity, low-inclination giant orbits.** Jupiter and Saturn move on near-circular, nearly coplanar orbits at 5 and 10 AU. By contrast, many exoplanet systems detected by the radial-velocity method, which measures the Doppler shift of the star's own light as an orbiting planet pulls it back and forth, contain giant planets on substantially eccentric and inclined orbits, often with evidence for past dynamical instability.
3. **No hot Jupiter or hot Neptune.** Roughly $0.5$ to $1\%$ of Sun-like stars host a hot Jupiter, and the hot Neptune desert is bordered by a population of warm Neptunes. We have neither.
4. **Irregular inner-system spacing rather than peas-in-a-pod.** {cite:t}`Weiss2018` showed that planets in Kepler multi-planet systems tend to be very similar in size to one another and to be regularly spaced in period: the so-called "peas-in-a-pod" pattern. The solar system terrestrials cover a factor of $\sim 18$ in mass (Mercury at $0.055\,\Mearth$, Earth at $1\,\Mearth$) and are irregularly spaced. We are not in a peas-in-a-pod system ({numref}`fig:l14:peas`).

```{figure} figures/raymond2022_peas_in_a_pod.avif
:align: center
:name: fig:l14:peas
:width: 75%

Compact multi-planet systems with four or more transiting planets interior to 1.52 AU, ranked by their planet-radius dispersion (most uniform sizes at the top, greatest size diversity at the bottom). Point sizes scale logarithmically with planet radius. The solar system terrestrials, included for comparison, sit in the bottom quintile of size uniformity, showing that the peas-in-a-pod architecture prevalent in Kepler compact multis did not emerge in our own system. Reproduced from {cite:t}`Weiss2023`.
```

The mass-radius diagram offers a complementary view ({numref}`fig:l14:massrad`). Plotting bulk density implied by mass and radius for the planets in the solar system and for the exoplanets where both quantities are known, one sees that the rocky planets cluster along a narrow track set by the equation of state of silicate mantles and iron cores, while the larger planets spread out into the volatile-rich and the gas-dominated regimes. The solar system terrestrials sit firmly on the "Earth-like" composition curve. Many close-in exoplanet super-Earths sit on the same curve too, indicating that the population of bare rocky cores is real, but a substantial subset of slightly larger planets sits *above* the rocky line, indicating that they retain significant volatile envelopes that swell their radii relative to a pure-rock composition.

```{figure} figures/lichtenberg2025_mass_radius.avif
:align: center
:name: fig:l14:massrad
:width: 95%

Mass-radius diagram for rocky and small exoplanets from {cite:t}`Lichtenberg2025` Fig. 2. Data points are observed exoplanets with measured masses and radii, colour-coded by equilibrium temperature into **temperate** (blue), **bistable** (light blue, able to sit in either a temperate or a runaway-greenhouse climate state), **lava** (red), and **rock-vapour** (orange) regimes; symbol shape marks **high-priority** atmospheric-characterisation targets (diamonds) and lower-priority targets (circles). Labelled planets include TRAPPIST-1 b through h, GJ 367 b, GJ 1132 b, GJ 486 b, K2-18 b, K2-141 b, LHS 1140 b, L 98-59 b/c/d, GJ 1252 b, LTT 1445 A b, and several TOI targets. Theoretical equation-of-state tracks range from **100% Fe** (bottom) through **Earth-like** rocky and **100% MgSiO$_3$**, with volatile-rich tracks for **Earth-like + 50 wt% H$_2$O**, **magma ocean + 0.1 wt%** or **5.4 wt% H$_2$O**, and a **gas-dwarf birth + H/He boil-off** curve that bounds the potential sub-Neptune population (shaded at upper left). Solar-system terrestrials sit on the Earth-like curve; exoplanets above it either retain volatile envelopes (H/He, water, or melt-water mixtures) or are otherwise reshaped by magma-ocean outgassing and photoevaporation. Reproduced from {cite:t}`Lichtenberg2025`.
```

### "Is the solar system rare?"

The natural follow-up question is whether the solar system is actually rare, or whether we have just looked under the streetlamp and missed the dimmer corner of the parameter space where it lives. The honest answer is that we do not yet know, for two reasons:

First, the long-period detection floor is set by survey duration. Kepler monitored its target stars for about four years. To detect a planet in a 12-year (Jupiter-like) orbit with the same statistical confidence requires three full transits, and therefore requires either continuous monitoring for decades or radial-velocity baselines of comparable length. We are only just now starting to have those baselines, and Gaia DR4 (expected 2026) is the first survey with sensitivity to astrometric Jupiter analogues at scale.

Second, the Earth-analogue regime, that is, $\Rearth$-sized planets in 1-year orbits around Sun-like G dwarfs, is also at the edge of current sensitivity. PLATO (ESA, launch early 2027) is specifically designed for that regime. Combined with Gaia DR4/DR5, it will be the first survey with the cadence, the photometric precision, and the long enough baseline to determine whether Earth analogues exist around bright nearby stars.

The honest framing for the next decade is therefore this: the question of whether the solar system is rare or typical is a question about a distribution we have not yet observed. The current statistics tell us where we sit relative to a heavily biased sample of mostly close-in, mostly massive planets. Statements like "the solar system is unusual because it has no sub-Neptune" are correct as observations about the existing dataset, but their implication for the underlying distribution is not yet settled.

What we can say with confidence is that the inner solar system is *atypical* relative to known compact systems: our terrestrials are too widely spaced, too varied in mass, and too far apart to look like a Kepler peas-in-a-pod analogue. Whether this is bad luck, the fingerprint of Jupiter, or the most common outcome around stars where we have not yet looked carefully enough remains open.

The reverse statement, that planet *occurrence rates depend strongly on stellar type*, is by now well established. {numref}`fig:l14:mulders-occurrence` shows the close-in (period $< 50$ days) small-planet occurrence rate as a function of stellar effective temperature, compiled from a decade of Kepler, K2, and ground-based surveys: rocky and sub-Neptune-sized planets are roughly twice as common around early M dwarfs as around F and G dwarfs, and the trend continues into the late M regime. Whether this trend reflects formation efficiency in lower-mass disks or detection bias in different survey samples is still being debated, but the headline conclusion, that "Earth-sized planets are not rare around low-mass stars", is robust.

```{figure} figures/mulders2024_occurrence_vs_teff.avif
:align: center
:name: fig:l14:mulders-occurrence
:width: 80%

Overview of planet occurrence rates as a function of host-star effective temperature, for planets between $1$–$4\,\Rearth$ on orbital periods $P < 50$ days, from {cite:t}`Mulders2024` Fig. 5. Rates were re-scaled assuming uniform occurrence in $\log P$ and $\log R$ for cross-study comparison. Plotted data are compiled from Howard+12, Mulders+15, Hardegree-Ullman+19, Yang+20, He+21, Sabotta+21, {cite:t}`Bergsten2022`, and Ment & Charbonneau 23 (see {cite:t}`Mulders2024` for full references). Across all studies, planet occurrence increases by roughly a factor of 2 from F dwarfs ($\sim 6500$ K) to early M dwarfs ($\sim 3500$ K); a break appears toward late M dwarfs, but those surveys sample only very short periods ($< 10$ d) so the late-M values are lower limits. The headline message is that small, close-in planets are most common around the most numerous class of stars in the galaxy. Reproduced from {cite:t}`Mulders2024`.
```


## Part 2: Habitability as a coupled systems property

### The stack of requirements

The course has built up the physical picture of habitability piece by piece. Lecture 5 introduced the radiative balance, scale height, and atmospheric retention; lecture 6 added clouds, weather, and the carbonate-silicate cycle; lecture 7 added surface processes and tectonic regimes; lectures 9 and 10 made the comparative case study for Earth, Venus, and Mars; lecture 13 added the stellar dependence and the exoplanet evidence. By the end of the course we are in a position to step back and notice that habitability is not a single condition. It is a stack of necessary couplings.

The stack looks roughly like this:

- **Star.** The host star must be stable in luminosity over Gyr timescales, must not flare so often or so violently that the atmosphere is stripped, and must have a long enough main-sequence lifetime to allow biology to evolve and to be observed.
- **Orbit.** The planet must lie within the liquid-water habitable zone for that star, must have a low enough eccentricity to avoid extreme thermal cycling, and must rotate fast enough (or be coupled to its star in some other way) to redistribute heat and to avoid the day-night collapse of the atmosphere.
- **Planet bulk.** The planet must be massive enough to retain an atmosphere on Gyr timescales, to drive interior convection, and to maintain a volatile inventory against escape.
- **Atmosphere.** The atmospheric composition must keep the surface within a habitable temperature range, the photochemistry must not run away, and the escape rate must be slow enough to allow long-term retention.
- **Interior.** The interior heat budget must be high enough to drive mantle convection and outgassing, both because outgassing replenishes the atmosphere and because, in some configurations, mantle convection sustains the dynamo that protects the atmosphere from the stellar wind.
- **Surface and tectonics.** A regime that recycles volatiles between surface, atmosphere, and interior is needed to close the carbon cycle (plate tectonics on Earth, or some functional equivalent).
- **Biosphere, once it exists.** Biology in turn modifies all of the above by changing atmospheric composition, surface albedo, weathering rates, and even the long-term carbon cycle.

Each level in the stack is necessary. None of them by itself is sufficient. What makes habitability a *systems* property rather than a checklist is that the levels are *coupled*: the star drives the photochemistry, the photochemistry feeds back on the cloud structure, the cloud structure changes the albedo and the temperature, the temperature controls the weathering, the weathering pulls $\mathrm{CO_2}$ out of the atmosphere, the loss of $\mathrm{CO_2}$ depends on the interior outgassing rate, and the outgassing rate depends on the tectonic regime. Break any link and the system can drift into a regime where surface liquid water is no longer thermodynamically possible.

### The habitability coupling loop

The atmospheric segment of this coupled system is drawn in {numref}`fig:l14:tidal-couplings`, a schematic from the {cite:t}`Wordsworth2022` review for a tidally locked rocky planet, one whose rotation period equals its orbital period, so that the same hemisphere always faces the star. The schematic shows the atmosphere's response to one-sided irradiation: clouds form and reflect starlight near the substellar point, super-rotating winds transport heat from the dayside to the nightside, and condensable volatiles are cold-trapped at the antistellar point. In the extreme case the atmosphere collapses onto the nightside surface. Each arrow on the schematic corresponds to a process that the course has covered.

```{figure} figures/wordsworth2022_tidally_locked_planet.avif
:align: center
:name: fig:l14:tidal-couplings
:width: 85%

Schematic of the dynamical and climate processes in the atmosphere of a tidally locked rocky exoplanet. Stellar irradiation drives cloud formation and partial reflection near the substellar point, day-to-night heat transport by super-rotating winds, and cold-trapping of condensable volatiles at the antistellar point, where the atmosphere can collapse onto the surface. When the dominant condensable is water, this transport-and-trapping cycle is the planet's hydrological cycle. Whether it persists depends on the total water inventory and on factors such as tectonic regime, escape, and stellar evolution that this single snapshot does not capture. Reproduced from {cite:t}`Wordsworth2022`.
```

The full coupling loop extends beyond what the schematic draws: tracing it in the order star $\to$ atmosphere $\to$ surface $\to$ interior $\to$ star is a useful exercise. Stellar irradiation drives the radiative balance and the photochemistry, both of which were treated in {ref}`Lecture 5 <lecture05>`. The atmosphere transfers heat to the surface, where it controls weathering rates and the rate of carbonate-silicate breakdown ({ref}`Lecture 6 <lecture06>`, {ref}`Lecture 9 <lecture09>`). The surface couples to the interior through subduction, melting, and outgassing, which return volatiles either to space (via degassing followed by escape) or to the deep mantle (via subduction). The interior in turn is coupled back to the atmosphere by the volcanic flux of $\mathrm{CO_2}$, $\mathrm{H_2O}$, and $\mathrm{SO_2}$, and to the stellar wind by the dynamo's magnetic shielding ({ref}`Lecture 4 <lecture04>`).

This loop is the synthesis the course aims for. It captures why no single number, "the equilibrium temperature is right" or "the planet is in the habitable zone", is sufficient to predict whether a planet is habitable. The question is always: are *all* the loops closed, *over the right timescales*, *over the right history*, and *under the right boundary conditions*?

### The habitable zone is not a line

The classical habitable zone (HZ) is defined as the range of orbital distances around a given star at which an Earth-like planet could maintain liquid surface water. In the simplest one-dimensional radiative-convective model, this is a strip in orbital space, with an inner edge set by the runaway greenhouse limit and an outer edge set by the maximum $\mathrm{CO_2}$ greenhouse {cite:p}`Kasting1993,Kopparapu2013` ({numref}`fig:l14:kopparapu-hz`). The blackboard derivation in this lecture reconstructs both edges from a one-line energy balance.

```{figure} figures/kopparapu2014_hz_stellartype.avif
:align: center
:name: fig:l14:kopparapu-hz
:width: 80%

Habitable zone boundaries as a function of stellar effective temperature and planet mass, from {cite:t}`Kopparapu2014`. The inner HZ (left curves) and outer HZ (right curve) shift inward for cooler stars. Around M dwarfs, the HZ overlaps strongly with the tidal-locking radius and with spin-orbit resonance regions, where the planet's rotation period locks to a simple ratio of its orbital period, complicating habitability assessment in ways that the 1D HZ does not capture. Reproduced from {cite:t}`Kopparapu2014`.
```

This is a useful reference object. Two things, however, must be added immediately to use it sensibly. First, *two planets at the same orbital distance can end up with radically different climates depending on their water inventory, their tectonic regime, and their stellar evolution history.* Earth and Venus illustrate the point: Venus receives only $\sim 1.9\times$ Earth's solar flux but has a $737$ K, $92$ bar, $\mathrm{CO_2}$-dominated atmosphere with essentially no water, while Earth has a $288$ K surface and a stable hydrosphere ({ref}`Lecture 9 <lecture09>`). The difference is not in the present-day instellation alone but in the history of how the two planets evolved through their early molten phases and through 4.5 Gyr of solar luminosity evolution {cite:p}`Hamano2013,Way2016` ({numref}`fig:l14:runaway` shows how long habitable-zone planets around M dwarfs spend inside the runaway boundary during the host's pre-main-sequence phase).

```{figure} figures/lugerbarnes2015_runaway_duration.avif
:align: center
:name: fig:l14:runaway
:width: 75%

Duration of the runaway greenhouse phase for planets that formed at 10 Myr with abundant surface water, as a function of stellar mass (vertical axis) and orbital semi-major axis (horizontal axis), from the {cite:t}`LugerBarnes2015` water-loss calculation around M dwarfs. The solid black lines mark the empirical inner habitable zone (recent Venus and early Mars limits at 5 Gyr); the dashed lines mark the theoretical runaway and maximum greenhouse limits. Habitable-zone planets around late M dwarfs spend a substantial fraction of their first Gyr inside the runaway state, losing much of their initial water before the host star reaches the main sequence. Reproduced from {cite:t}`LugerBarnes2015`.
```

Second, the habitable zone is *time-dependent*. Stellar luminosity increases by roughly 30% over the main-sequence lifetime of a Sun-like star, so a planet inside the inner edge today might have been outside it 4 Gyr ago, and vice versa. M dwarfs are even more pathological: their pre-main-sequence high-luminosity phase lasts hundreds of Myr to a few Gyr, during which any planet now in the HZ was instead inside the runaway boundary {cite:p}`LugerBarnes2015`. A planet that is "in the HZ" today is not necessarily "habitable" if it spent most of its history outside that zone.

The right question is therefore not "is the planet in the HZ today?" but "does the planet's evolutionary trajectory through the HZ allow for the long-term presence of liquid water?". Trajectories matter more than snapshots. The next generation of habitability assessment, both for solar system bodies and for exoplanets, is built around coupled climate-evolution models rather than 1D HZ boundaries.

### Tectonic regime and the long-term thermostat

The carbonate-silicate cycle is the long-term temperature thermostat on Earth. Volcanism injects $\mathrm{CO_2}$ into the atmosphere; rainfall on silicate rocks weathers them and converts the dissolved $\mathrm{CO_2}$ into carbonate ions, which are deposited in the ocean as carbonate sediments and eventually subducted back into the mantle ({ref}`Lecture 6 <lecture06>`, {ref}`Lecture 9 <lecture09>`). The negative feedback comes from the temperature dependence of weathering: warmer climate means faster weathering, faster removal of $\mathrm{CO_2}$, and therefore cooler subsequent climate.

This thermostat operates only because three conditions are met simultaneously on Earth: (a) liquid water exists, (b) volcanism is active, and (c) plate tectonics removes the carbonates back into the mantle so the cycle does not run out. Break any one of these conditions and the thermostat fails. Venus is the textbook failure mode. Its surface dried out (either early or late, see {ref}`Lecture 9 <lecture09>`); without liquid water there is no weathering sink for $\mathrm{CO_2}$; volcanic outgassing continued; and the resulting $\mathrm{CO_2}$ has nowhere to go, so it accumulated to the present 92 bar atmosphere. **Stagnant-lid** worlds (planets whose outer shell forms a single immobile plate rather than being recycled by plate tectonics), like Venus, also do not subduct carbonates back into the mantle, so the cycle is one-way once the surface dries.

A major open question is whether plate tectonics is the *only* viable long-term thermostat, or whether stagnant-lid worlds with episodic resurfacing (the candidate Venus mode) can also maintain temperate climates over Gyr timescales. There is no consensus. For exoplanets, the question is currently academic in a hard sense: tectonic regime cannot be measured remotely with any current or near-term observation. This is one of the largest missing variables in exoplanet habitability assessment.

### Magnetic field as gatekeeper

Lecture 4 introduced the geodynamo and explained why an active magnetosphere protects the atmosphere from solar-wind ion-pickup escape. Lecture 10 made the case study explicit for Mars: Mars lost its global magnetic field in the late Noachian, with the original basin-demagnetisation analysis of {cite:t}`Acuna1999` placing the cessation at 4.1 to 3.9 Ga and the more recent {cite:t}`Mittelholz2020` re-analysis identifying two distinct episodes of dynamo activity, one at $\sim 4.5$ Ga and another at $\sim 3.7$ Ga, the latter extending into the early Hesperian. From then on Mars lost most of its remaining atmosphere through processes that an active dynamo would have suppressed {cite:p}`Jakosky2018,Acuna1999,Mittelholz2020`. The MAVEN mission constrained present-day escape rates and showed that they are consistent with a Mars that started with a substantially thicker $\mathrm{CO_2}$ atmosphere.

The lesson, however, is not as simple as "no magnetic field means no atmosphere". Venus has retained its $\sim 92$ bar atmosphere without a global magnetic field, so the relationship is not deterministic. What a magnetic field does is *shift the balance of escape mechanisms*. Without one, the dominant losses are nonthermal: pickup ions, sputtering, and ionospheric outflow. Whether these matter on Gyr timescales depends on the planet's mass, its atmospheric column, the strength of the stellar wind, and the timing of the dynamo's onset and shutdown. For exoplanets around active M dwarfs, the question of whether an active dynamo is *required* for atmospheric retention is a major unresolved research problem and is one of the reasons the TRAPPIST-1 system is such an important target.

### Water delivery and planetary evolution

There is a temptation when teaching planetary water inventories to make the question one of *delivery*: how much water arrived from carbonaceous chondrites (primitive, volatile-rich meteorites) versus comets, what was the relative D/H (deuterium-to-hydrogen) ratio of each, and what does that imply about the source mixture? That framing was reasonable a decade ago, but it is increasingly clear that *delivery is not the dominant lever for inner solar system water inventories*. Planetary evolution is.

The key point is this: Earth, Venus, and Mars likely received broadly similar volatile inventories during accretion. They formed in roughly the same region of the disk, from roughly the same mixture of chondritic precursors, with broadly similar bulk water budgets per unit silicate mass {cite:p}`Lichtenberg2023`. Their present-day water inventories differ by orders of magnitude, but those differences reflect *what each body did with its initial inventory*, not the source mixture of accreted material {cite:p}`Hamano2013`. The mechanisms that matter for the inner solar system are processes internal to the planet, not exotic delivery histories.

```{figure} figures/lichtenberg2023_magma_ocean_differentiation.avif
:align: center
:name: fig:l14:magma-diff
:width: 70%

Schematic of magma-ocean stage differentiation on a forming rocky planet. The initially molten silicate mantle separates from a denser metal phase that sinks to form the core, while volatiles partition between the molten silicate and an overlying steam atmosphere. The fraction sequestered in the mantle versus outgassed into the atmosphere is decisive for the planet's later atmospheric evolution. Reproduced from {cite:t}`Lichtenberg2023`.
```

The first lever is *magma ocean partitioning*. During the early molten phase, when a forming rocky planet's mantle is wholly or largely molten (a **magma ocean**), a planet's water and carbon partition between an iron-rich core, a silicate mantle, and a steam atmosphere overhead. The fraction sequestered in the mantle versus outgassed into the atmosphere depends on the redox state of the magma, on the solidification timescale, and on the depth at which crystallisation begins {cite:p}`ElkinsTanton2012,Hirschmann2012` ({numref}`fig:l14:magma-diff`). Different boundary conditions lead to very different end states even for identical starting inventories.

The starting timing also matters. The temperatures reached by accreting planetesimals depend on their formation time and on snow-line position. Bodies that accrete in the first $\sim 1$ Myr after CAI formation are heated above the water-ice melting point by short-lived radionuclides ($^{26}\mathrm{Al}$ in particular, with a half-life of only $\sim 0.7$ Myr) and lose much of their primordial water through dehydration. Bodies that accrete later, beyond the snow line, retain their volatiles {cite:p}`Lichtenberg2023`. The composition of the inner solar system terrestrials therefore depends on *when* their building blocks formed, not just on *where*, and the early-formed component is systematically dryer than the late-formed component.

The second lever is *atmospheric escape during the magma ocean phase*. Under a young, EUV-bright Sun, hydrodynamic escape can drag water out of the upper atmosphere fast enough to deplete a fraction of the inventory before the magma ocean has even solidified ({ref}`Lecture 9 <lecture09>`; {cite:t}`Hamano2013`). This is the "Type II" Hamano scenario for Venus: with $\sim 1.9$ times Earth's instellation, Venus's magma ocean took long enough to solidify that hydrogen escape ran far longer and hotter than on Earth, and a substantial fraction of the initial water never made it to the surface as liquid ({numref}`fig:l14:hamano-typeII`).

```{figure} figures/hamano2013_typeI_typeII.avif
:align: center
:name: fig:l14:hamano-typeII
:width: 70%

Two distinct types of terrestrial planet defined by the {cite:t}`Hamano2013` model. Panel (a) shows magma-ocean solidification time as a function of orbital distance and instellation for a range of initial water inventories; planets inside a critical orbital distance ($\sim 0.77$ AU around a Sun-like star) cannot solidify their magma oceans before most of their water is lost to hydrodynamic escape ("Type II"), while planets further out solidify quickly and retain most of their water ("Type I"). Panel (b) shows the resulting final water inventories at the end of magma-ocean solidification. Modified from {cite:t}`Hamano2013` as reproduced in {cite:t}`Lichtenberg2023`.
```

The third lever is *mantle-atmosphere exchange over Gyr*. Once the planet is solid and tectonically active, volcanic outgassing continues to feed the atmosphere with volatiles, while subduction and weathering pull volatiles back into the mantle. On a planet with active plate tectonics this loop can run for billions of years and keep the surface inventory roughly steady. On a stagnant-lid planet, the outgassing flux still operates but the return flow is much weaker, so the surface inventory drifts one-way. On a body too small to maintain interior convection (the Moon, Mars after $\sim 1$ Ga), even outgassing slows to a trickle.

The fourth lever is *the stellar evolution history*. The pre-main-sequence high-luminosity phase is decisive for M-dwarf planets, whose habitable zone passes through the runaway boundary during the first few hundred Myr ({ref}`Lecture 13 <lecture13>`; {cite:t}`LugerBarnes2015`). For G dwarfs the effect is smaller but still relevant: the faint young Sun of 4 Gyr ago needed a stronger greenhouse to keep Earth from freezing, and the Sun's slow brightening sets the long-term drift of the inner HZ edge.

The same picture can be told from the inside as well as the outside. Radiogenic clocks recorded in meteorites and in the Moon's chemistry show that core formation, magma ocean crystallisation, and the major silicate differentiation events on the Earth, Mars, and the asteroid parent bodies were all completed within the first $\sim 100$ Myr of solar system history {cite:p}`Lichtenberg2023,Dauphas2017,Kruijer2017`. The interior boundary conditions for atmospheric evolution were therefore largely set early, and any subsequent atmospheric history is layered on top of an interior whose primary differentiation was already done.

The implication, and the reason this section is in the synthesis lecture rather than the formation lecture, is that *the present-day water inventory of an inner solar system body is set primarily by its internal evolution, not by its delivery budget alone*. The D/H debate from {ref}`Lecture 12 <lecture12>` is therefore a constraint on delivery *plus* processing combined, not on delivery alone. The same argument applies to exoplanets: when JWST or LIFE detects (or fails to detect) water on an exoplanet atmosphere, what we are constraining is the entire integrated history of accretion, magma-ocean processing, escape, outgassing, and tectonic recycling, not the source mixture of accreted ice. *Planetary evolution is the dominant lever for inner solar system habitability.*

### The Drake equation and its limitations

The framing tool that astronomers traditionally use to organise the question "how many habitable or inhabited planets are there in the galaxy?" is the {cite:t}`Drake1965` equation, originally written as a heuristic factorisation for the 1961 Green Bank meeting:

$$
N = R_\star \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L \,.
$$

Here $R_\star$ is the rate of formation of new stars in the galaxy, $f_p$ is the fraction of those stars that have planets, $n_e$ is the number of planets per system that are within the habitable zone, $f_l$ is the fraction of habitable-zone planets on which life arises, $f_i$ is the fraction of those on which intelligence evolves, $f_c$ is the fraction of intelligent species that develop the technology to broadcast detectable signals, and $L$ is the average lifetime of the broadcasting phase. Drake originally defined $n_e$ more broadly as the number of planets per star with an environment suitable for life; the habitable-zone shorthand used here is the modern operationalisation. Multiplying these together gives $N$, the number of communicating civilisations expected to exist in the galaxy at any one time.

The equation has real pedagogical value. It separates the question into clearly distinct inputs. It shows where astronomy, planetary science, biology, and sociology each contribute. And, crucially for this course, it makes plain that *only the first three factors* ($R_\star$, $f_p$, $n_e$) are now constrained by direct observation. The first is set by stellar astrophysics. The second has been measured, by Kepler and its successors, to be of order unity ({ref}`Lecture 13 <lecture13>`). The third has been measured by Kepler and TESS and will be sharpened by PLATO; depending on the exact definition of "habitable", current values lie in the range $0.1$ to $0.6$ for Sun-like stars {cite:p}`Bryson2021`.

The remaining four factors are not constrained in any quantitative sense at all. We have one data point for $f_l$ (life arose on Earth at least once), no data points for $f_i$ outside of our own lineage, no data points for $f_c$ outside of the last $\sim 100$ years, and no statistical handle whatsoever on $L$ for technological civilisations in general.

This course's view of the Drake equation is that it is *a framing tool, not an estimator*, and that there are five reasons not to take any specific numerical value of $N$ derived from it seriously:

1. **The factors are not independent.** Biospheres co-evolve with their atmospheres, with their interiors, and (eventually) with technological civilisations. The probability that intelligence arises is not separable from the probability that biology arises in the first place; the lifetime of a communicating phase is not separable from the conditions that allowed that phase to begin. Treating these as independent factors and multiplying them together discards the structure that connects them.
2. **Most factors are unconstrained by orders of magnitude.** $f_l$, $f_i$, $f_c$, and $L$ each span at least four to ten orders of magnitude in the published literature. The product of factors that are individually uncertain by orders of magnitude inherits all of those uncertainties, and the resulting "answer" is essentially a restatement of the priors that went in.
3. **It treats a contingent process as a steady-state pipeline.** The origin of life is a deeply non-equilibrium process that, on Earth, may have involved a cascade of historical accidents that need not repeat. The Drake equation factorises this as if it were a Markov chain with stationary transition probabilities. It is not.
4. **It implicitly assumes uniformity.** The equation describes "a" type of life-bearing planet around "a" type of star, and silently ignores the diversity of planet types, atmospheric histories, and stellar environments that this course has spent thirteen lectures establishing. A real galactic estimate would need to integrate over these distributions, not reduce them to single factors.
5. **Anthropic selection in the only data point.** Earth is the *only* example we know of in which life arose. We are observing the galaxy from a planet on which it did, which biases any extrapolation from our own case in ways that are very hard to quantify.

What the Drake equation *is* good for is organising a discussion. It shows where the deep ignorance lies (everything to the right of $n_e$), and it makes it easy to see how a specific claim about the prevalence of life depends on which factor you push. What it should *not* be used for is generating numerical estimates of the form "there are $10^4$ communicating civilisations in the Milky Way". Those numbers reflect the priors going in, not anything we have measured.

{cite:t}`SandbergDrexlerOrd2018` made this point quantitatively. Instead of multiplying together best-guess values for each Drake-equation factor, they sampled each factor from the published distribution of estimates (which often span ten or more orders of magnitude), Monte-Carlo'd the product, and asked what the resulting posterior distribution for $N$ actually looks like ({numref}`fig:l14:sandberg-drake`). The result is striking: when the orders-of-magnitude uncertainty in $f_l$, $f_i$, and the other "soft" factors is propagated honestly, roughly one third of the posterior probability mass sits below $N = 1$ in the Milky Way, and about ten percent below the much lower threshold corresponding to "alone in the entire observable universe". In other words, both "we are alone in the Milky Way" and (with smaller but non-negligible probability) "we are alone in the observable universe" are consistent with current scientific knowledge, not because they are the most likely outcomes, but because the priors do not exclude them. This is what {cite:t}`SandbergDrexlerOrd2018` mean by *dissolving the Fermi paradox*: the paradox depends on a point estimate of $N$ that the data do not support, and the apparent silence of the universe is unsurprising once the genuine uncertainty in the inputs is admitted.

It is worth seeing in one line why the bimodality in {numref}`fig:l14:sandberg-drake` arises. Because the published estimates of $f_l$, $f_i$, $f_c$, and $L$ each span many orders of magnitude with no preferred central value, the natural prior on each factor is *log-uniform* rather than uniform. Taking $\log_{10}$ of the Drake equation turns the product into a sum,

$$
\log_{10} N = \log_{10}(R_\star f_p n_e) + \log_{10} f_l + \log_{10} f_i + \log_{10} f_c + \log_{10} L \,,
$$

so the distribution of $\log_{10} N$ is the *convolution* of the distributions of the individual log-factors. If each of the four uncertain factors is independently log-uniform on, say, $[-10, 0]$ (ten orders of magnitude each), then $\sum_{k=1}^4 \log_{10} f_k$ is a sum of four independent uniform variables on $[-10, 0]$, supported on $[-40, 0]$, with a quasi-Gaussian central peak by the central limit theorem and substantial tail probability extending to $\log_{10} N \sim -30$ or below. The distribution is therefore broad enough that even after fixing the astronomically constrained prefactor $R_\star f_p n_e$, the posterior on $N$ stretches across $\sim 30$ decades and the cumulative probability of $N < 1$ is large. The bimodality in the published Sandberg posterior comes from combining log-uniform soft factors with a bounded astronomical prefactor; the lesson is that *broad priors on multiplicative factors generate broad and often skewed product distributions*, and any "best estimate" for $N$ is dominated by the prior choice rather than by the data.

```{figure} figures/sandberg2018_drake_posterior.avif
:align: center
:name: fig:l14:sandberg-drake
:width: 80%

Posterior probability distribution for the number $N$ of communicating civilisations in the observable universe, computed by {cite:t}`SandbergDrexlerOrd2018` by Monte-Carlo sampling each Drake-equation factor from its published range of estimates rather than from a single point estimate. (Top) Probability density: the distribution is heavily bimodal, with one peak below $N \sim 10^{-20}$ and another near $N \sim 1$ to $10^5$. The red circles mark Drake-style point estimates from the literature. (Middle) Cumulative distribution: roughly one third of the probability mass lies below $N = 1$, corresponding to "we are alone in the Milky Way"; only about $10\%$ of the probability mass lies below the much lower threshold $N \ll 1$ corresponding to "we are alone in the observable universe". (Bottom) Cumulative distribution of distance to the nearest civilisation. The two vertical lines mark the boundary "alone in the Milky Way" (red) and "alone in the observable universe" (blue). Reproduced from {cite:t}`SandbergDrexlerOrd2018`.
```

### The Fermi paradox

The Fermi paradox is a closely related framing question, often summarised as "where is everybody?" and attributed to Enrico Fermi over lunch at Los Alamos in 1950. The argument runs roughly as follows. Even with conservative estimates for the Drake-equation factors, the Milky Way is old enough (about $10^{10}$ years) that any spacefaring civilisation that arose more than a few million years ago could have crossed the galaxy many times over at sub-relativistic speeds. We see no evidence of any such civilisation. Why not?

There is no shortage of proposed resolutions, none of which can be tested directly. Among the more commonly discussed:

- **Rare-life hypothesis:** $f_l$ is far smaller than astronomers tend to assume. Life is very hard to start, and the Earth got lucky.
- **Rare-intelligence hypothesis:** $f_i$ is the bottleneck. Life is common, but technological intelligence rarely follows from biology.
- **Great filter ahead:** $L$ is short. Civilisations self-terminate or otherwise stop broadcasting before they cover much of the galaxy.
- **Detection threshold:** Signals exist but are below current sensitivity, are intermittent, or are encoded in ways we do not recognise.
- **Zoo and similar speculative scenarios:** Civilisations exist but are deliberately concealed, are not interested in contact, or operate on energy and signalling scales we are not yet able to imagine.

The pedagogical framing for this course is that the Fermi paradox is *a question, not an answer*. It is most useful as a check on intuition about how confident one should be in particular Drake-equation factors. If you find yourself estimating $N \sim 10^4$, the Fermi paradox forces you to ask where those civilisations are and what mechanism is keeping them invisible. If your estimate is $N \sim 1$, the paradox dissolves but is replaced by the equally hard question of why life is so rare. Either way, the paradox is a tool for thinking, not a piece of evidence.


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
T_{\rm eq}(d) = \left[\frac{L_\star (1 - A_B)}{16\pi\sigma\epsilon d^2}\right]^{1/4}\,,
$$

where $\epsilon$ is the effective emissivity of the atmosphere (which in the bare-rock limit is $1$) and $\sigma$ is the Stefan-Boltzmann constant. For Earth around the Sun, plugging in $A_B \approx 0.3$, $\epsilon \approx 1$, $L_\star = \Lsun$, and $d = 1$ AU gives $T_{\rm eq} \approx 255$ K. The actual surface temperature is $\sim 288$ K because the greenhouse effect adds $\sim 33$ K.

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
- **K dwarfs** (e.g. $\epsilon$ Eri at $L \sim 0.3\,\Lsun$): $d_{\rm in} \approx 0.53$ AU, $d_{\rm out} \approx 0.93$ AU. Long main-sequence lifetimes ($\sim 30$ to $70$ Gyr), modest flares, stable photospheres, and an HZ that is far enough out to avoid most tidal-locking and pre-main-sequence problems. {cite:t}`CuntzGuinan2016` argued on these grounds that K dwarfs may be the *most habitable* class of host star. Their UV/X-ray output is modest after the first Gyr ({numref}`fig:l14:cuntz-xray`), and their long lifetimes give biology more time to develop.
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

Astrobiology operates without an agreed-upon definition of life. The working definition usually adopted, going back to {cite:t}`Lederberg1965` and the Viking-era discussions, is that life is *a self-replicating, metabolising, evolving chemical system*. This is a deliberately operational definition: it is not the philosophically deepest definition possible, but it is the one that lets us decide what to look for.

The chemical baseline is also a working assumption. Carbon-based, water-as-solvent biology is the only example we have, and the search for life elsewhere is dominated by it because we know what the spectroscopic and geochemical fingerprints of carbon-water life look like. Alternative biochemistries (silicon-based, ammonia-solvent, methane-solvent) are not excluded in principle, but they are extremely difficult to design search strategies for, and they are not our default working hypothesis.

### Extremophiles and the redefinition of "habitable"

For most of the 20th century, the operational definition of "habitable" was approximately "the conditions under which a temperate Earth surface organism would thrive". The discovery, beginning in the 1960s and accelerating through the 1990s, of *extremophile* organisms thriving far outside that range has substantially relaxed the definition.

Earth life occupies environments from black-smoker hydrothermal vents at over 120 $^\circ$C, through hyperacidic mine drainage at pH below 1, to subglacial lakes at $-20$ $^\circ$C, to saturated brine, to the highly radioactive cores of nuclear reactors (the bacterium *Deinococcus radiodurans* survives doses $\sim 1000$ times the lethal human dose), to dry permafrost, to high-altitude clouds. Tardigrades, lichens, and certain cyanobacteria can survive total desiccation and decades of vacuum exposure. The implication for astrobiology is that the classical HZ, defined for surface liquid water on a temperate Earth-like planet, may be too restrictive. Subsurface oceans on icy moons and high-pressure environments such as the Venus cloud layer cannot be excluded a priori on energetic grounds.

This is the context in which the icy moons (Europa, Enceladus, Titan, Ganymede, Callisto) became the dominant solar system astrobiology targets, formalised in NASA's *Roadmap to Ocean Worlds* {cite:p}`HendrixVance2019`. None of them are in the classical HZ. All of them have, or have plausibly had, liquid water in contact with rock and a chemical free-energy gradient of some kind ({ref}`Lecture 11 <lecture11>`).

### Origin of life on Earth

The origin of life on Earth is a central scientific problem in astrobiology's adjacent fields, and it is not solved. There are several major hypotheses, none of which has been demonstrated to be the correct answer, and the honest framing for an undergraduate course is to present them as competing, not as a settled story.

- **RNA world.** Self-replicating RNA preceded protein-based metabolism. The hypothesis is supported by the discovery of catalytic ribozymes, RNA molecules that can speed up reactions the way protein enzymes do, in modern organisms and by the central role that RNA still plays in the ribosome. The main problem is that the prebiotic chemistry of RNA is hard: the nucleotides do not easily polymerise without templating, and they are not stable on the timescales required.
- **Metabolism-first, alkaline hydrothermal vents.** Chemical autocatalytic cycles preceded information storage. The hypothesis is supported by the geochemistry of submarine alkaline hydrothermal vents, which produce $\mathrm{H_2}$, methane, and disequilibrium gradients between fluid and seawater that closely resemble the redox conditions used by primitive metabolism {cite:p}`Russell2014`.
- **Surface "warm little ponds".** Wet-dry cycling in shallow surface pools concentrates and polymerises prebiotic molecules. The hypothesis goes back to Darwin's 1871 letter to Hooker and has been revived by experimental work showing that wet-dry cycles can polymerise nucleotides {cite:p}`Sasselov2020`.
- **Panspermia.** Life arrived from elsewhere, on a meteorite or a comet. This does not solve the problem; it relocates it. If life originated on Mars and was delivered to Earth by impact ejecta, the question simply becomes "how did life arise on Mars?".

The earliest direct evidence of life on Earth dates to about 3.5 Ga (microbial mat structures in Australia and South Africa). Possible isotopic and morphological biosignatures have been claimed in rocks dating back to $\sim 3.8$ Ga (the Isua banded-iron-formation light-carbon isotopic signatures, {cite:p}`Mojzsis1996`) and to the minimum age of $\sim 3.77$ Ga of cross-cutting zircon constraints in the Nuvvuagittuq Supracrustal Belt, with the $^{146}\mathrm{Sm}$-$^{142}\mathrm{Nd}$ date on the underlying Nuvvuagittuq metabasaltic unit pushing the controversial upper bound to $\sim 4.3$ Ga {cite:p}`Dodd2017`. If those earliest claims hold up, life may have arisen within a few hundred Myr of the cooling of the Earth's surface, which would place a striking upper limit on the timescale required for biology to start.

The honest framing is that we do not know how, when, where, or how easily life originates. This is the largest single uncertainty in any quantitative habitability estimate, and it is why $f_l$ in the Drake equation is unconstrained. It is also why the search for life on Mars and the icy moons matters so much: a *second* independent origin of life, on any other body, would constrain $f_l$ enormously.

### Biosignatures: what would we look for?

A biosignature is an observable feature whose presence is more easily explained by biology than by abiotic processes alone. The strategic context for the next decade of biosignature searches is set by the US National Academies' *Astrobiology Strategy for the Search for Life in the Universe* {cite:p}`NAS2018`. {cite:t}`Schwieterman2018` organise the remotely detectable biosignatures into three canonical classes (following Meadows 2006, 2008): atmospheric gases (direct or indirect metabolic by-products), surface reflectance features (spectral signatures from biological pigments), and temporal variability (time-dependent modulations driven by biology). Two further classes, isotopic signatures and morphological evidence, are diagnostic only for in-situ measurements on returned samples and are not realistically accessible at exoplanet distances. {cite:t}`Catling2018` complement this taxonomy with a Bayesian framework for assessing how strongly any candidate biosignature should update our prior probability of life given the surrounding planetary and stellar context ({numref}`fig:l14:catling-framework` and {numref}`fig:l14:catling-bayes`).

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

The classical *atmospheric gas* biosignatures are:

- **Oxygen ($\mathrm{O_2}$)** and its photochemical product **ozone ($\mathrm{O_3}$).** On Earth, $\mathrm{O_2}$ is produced almost exclusively by oxygenic photosynthesis and is present in the atmosphere at $\sim 21\%$. Without continuous biological replenishment it would be removed in $\sim 10^7$ years by reaction with reduced surface minerals.
- **Methane ($\mathrm{CH_4}$).** Biologically produced by methanogens, microorganisms that generate methane as a metabolic by-product, and by anaerobic decomposition. It is present in Earth's atmosphere at the ppm level despite being photochemically destroyed on a $\sim 10$-year timescale.
- **Nitrous oxide ($\mathrm{N_2O}$).** Produced almost exclusively by biology on Earth, chiefly through denitrification, the microbial conversion of nitrate to nitrogen gases.
- **Disequilibrium combinations.** The most diagnostic biosignature is not a single gas but a *combination* in chemical disequilibrium: $\mathrm{O_2}$ and $\mathrm{CH_4}$ together, for example, cannot coexist for more than a few years without continuous resupply. {cite:t}`Krissansen2018` quantified the disequilibrium approach by Gibbs-energy minimisation and showed that the modern Earth atmosphere-ocean system carries a disequilibrium of about 2326 J/mol, an order of magnitude above the abiotic Mars and Titan disequilibria of about 100 J/mol. They further argued that the coexistence of $\mathrm{CH_4}$, $\mathrm{CO_2}$, $\mathrm{N_2}$, and liquid $\mathrm{H_2O}$ on the Archean Earth (roughly 4.0 to 2.5 billion years ago) is even more diagnostic for *remote* detection than the modern $\mathrm{O_2}$-$\mathrm{CH_4}$ redox couple, because the Archean reaction cannot persist abiotically on any planet with liquid water ({numref}`fig:l14:biosig-gases`).

```{figure} figures/schwieterman2018_biosignature_gases.avif
:align: center
:name: fig:l14:biosig-gases
:width: 90%

Wavelength-resolved infrared absorption features for ten potential biosignature gases ($\mathrm{O_2}$, $\mathrm{O_3}$, $\mathrm{N_2O}$, $\mathrm{CH_4}$, $\mathrm{CH_3Cl}$, $\mathrm{C_2H_6}$, $\mathrm{NH_3}$, DMS, DMDS, $\mathrm{CH_3SH}$). Each panel plots the line-by-line absorption strength versus wavelength from $0.4$ to $20\,\mu\mathrm{m}$. Different molecules have characteristic absorption regions: $\mathrm{O_3}$ near $9.6\,\mu\mathrm{m}$, $\mathrm{CH_4}$ at $3.3$ and $7.7\,\mu\mathrm{m}$, $\mathrm{N_2O}$ across the mid-infrared, and DMS/DMDS in the $6$ to $15\,\mu\mathrm{m}$ window (with characteristic bands near $6$-$7$, $8$-$12$, and $14$-$15\,\mu$m). Reproduced from {cite:t}`Schwieterman2018`.
```

The reason disequilibrium combinations are so diagnostic is that the bulk solar system abundances of the key elements (H, C, N, O, Na, Mg, Al, Si, P, S, Cl, K, Ca, Fe, etc.) span more than ten orders of magnitude, and the relative abundances in any given planetary atmosphere depend strongly on the integrated history of escape, weathering, and biology. Earth's atmosphere is *highly* fractionated relative to the solar composition: it is depleted in noble gases by orders of magnitude, depleted in hydrogen by even more, and *enriched* in $\mathrm{O_2}$ to a level that no abiotic process can sustain on a planet with reduced surface minerals exposed to liquid water. The detection of strong fractionation patterns of this kind is itself a circumstantial biosignature, even before specific gas combinations are considered ({numref}`fig:l14:biosig-classes` summarises the three remotely detectable biosignature classes).

```{figure} figures/schwieterman2018_biosignature_classes.avif
:align: center
:name: fig:l14:biosig-classes
:width: 95%

The three classes of remotely detectable biosignatures: gaseous (left), surface (middle), and temporal (right). Gaseous biosignatures are produced as direct or indirect by-products of biological processes (e.g. photosynthetic $\mathrm{O_2}$, photochemically derived $\mathrm{O_3}$). Surface biosignatures are spectral signatures imparted by reflected light interacting with biological pigments (e.g. the vegetation red edge). Temporal biosignatures are time-dependent variations in atmospheric or surface properties caused by biology (e.g. the seasonal Keeling curve in Earth's $\mathrm{CO_2}$). A convincing biosignature claim should ideally combine evidence from more than one of these classes. Reproduced from {cite:t}`Schwieterman2018`.
```

Surface biosignatures include the so-called *vegetation red edge*, a sharp jump in surface reflectance at $\sim 700$ nm that is characteristic of chlorophyll-bearing plants on Earth. Photometric surface variability that follows a seasonal cycle, as Earth's $\mathrm{O_2}$ and $\mathrm{CH_4}$ do, would be a strong indicator of an active, modulated biosphere.

Returned-sample biosignatures, available only for solar system targets accessed by spacecraft, can include morphological structures (microfossils), specific organic molecules (amino acids, lipids), and isotopic patterns characteristic of biological metabolism (e.g. light-carbon enrichment in photosynthetic carbon).

### False positives and the inverse problem

The hardest problem in biosignature science is that essentially every candidate biosignature gas has a known abiotic production pathway under some plausible planetary conditions. {cite:t}`Meadows2018` and {cite:t}`Schwieterman2018` review the false-positive landscape in detail. A few canonical examples:

- **Abiotic $\mathrm{O_2}$.** Photolysis, the breakdown of a molecule by absorbed stellar light, of $\mathrm{H_2O}$ followed by hydrogen escape can produce abiotic $\mathrm{O_2}$ on dry worlds, especially around active M dwarfs where the early high XUV phase can drive massive hydrogen loss {cite:p}`Wordsworth2014,LugerBarnes2015`. $\mathrm{CO_2}$ photolysis in $\mathrm{CO_2}$-rich atmospheres also generates $\mathrm{O_2}$.
- **Abiotic $\mathrm{CH_4}$.** Serpentinisation, the reaction of olivine with water to form serpentine minerals and release hydrogen, generates $\mathrm{CH_4}$ abiotically, as does volcanic outgassing at low oxygen fugacity.
- **Abiotic $\mathrm{N_2O}$.** Lightning chemistry and certain photochemical pathways can produce small but non-trivial $\mathrm{N_2O}$ abundances.
- **Abiotic dimethyl sulphide ($\mathrm{(CH_3)_2S}$, DMS).** No significant abiotic source is known on Earth, which is why DMS has been proposed as a biosignature, but "not known on Earth" is not the same as "impossible elsewhere".

Biosignature detection is therefore an *inverse problem*: a single detection cannot prove life. What is needed is *context, combinations, and the absence of plausible abiotic explanations*. This is the design principle behind the next generation of life-detection missions, both in the solar system and for exoplanets: not a single observation but a multi-line, multi-target, multi-wavelength campaign that constrains the planet's physical state, escape history, and atmospheric composition all together.

### Solar system targets for life detection

The solar system contains five plausible targets for life detection. None of them is the obvious right answer, and all of them are scientifically interesting.

**Mars** (recap from {ref}`Lecture 10 <lecture10>`). Mars is the most direct path to laboratory-based life detection on another world. Curiosity and Perseverance have established that Mars had liquid water, neutral pH, and complex organic molecules in surface environments at $\sim 3.5$ to $4$ Ga. Past habitability is no longer in serious dispute. Present-day habitability is more uncertain: the methane variability detected by Curiosity is intriguing but not interpretable as biological without independent corroboration. The Mars Sample Return campaign, although the architecture and schedule were re-baselined in 2024 and 2025, remains the most direct path to laboratory analysis of returned material with the spatial and chemical context needed for confident interpretation {cite:p}`MeyerMSPG2022`.

**Europa** (recap from {ref}`Lecture 11 <lecture11>`). Europa has a global subsurface saltwater ocean confirmed by induced magnetic field measurements during the Galileo mission and by surface chemistry consistent with brine. NASA's Europa Clipper, launched in October 2024, will arrive in the Jupiter system in 2030 and conduct $\sim 50$ close flybys of Europa to characterise the ice shell thickness, the ocean chemistry, and any signs of recent or ongoing surface activity {cite:p}`Howell2020`. ESA's JUICE mission, launched in 2023, will study Europa, Ganymede, and Callisto from the Jovian system, with a particular focus on Ganymede's subsurface ocean.

**Enceladus** (recap from {ref}`Lecture 11 <lecture11>`). Enceladus is in many ways the most direct astrobiology target available because it ejects samples of its subsurface ocean directly into space through its south-polar plume. Cassini flew through that plume multiple times and detected $\mathrm{H_2}$ at concentrations consistent with active serpentinisation between the ocean and the rocky core, organic molecules including aromatic and macromolecular compounds, and (most recently) sodium phosphates that imply phosphorus-rich ocean chemistry suitable for terrestrial-style biochemistry {cite:p}`Waite2017,Postberg2023`. An "Enceladus Orbilander" concept, recommended by the {cite:t}`NAS2022` decadal survey, would directly sample plume material for organics, isotopes, and conceivably cellular structures.

**Titan** (recap from {ref}`Lecture 11 <lecture11>`). Titan has a complete hydrocarbon hydrology with methane and ethane lakes, an active prebiotic photochemistry generating complex organics in the atmosphere and on the surface, and the likely transient appearance of liquid water from impact-melt events. NASA's Dragonfly rotorcraft mission (launch 2028, arrival 2034) will explore the Selk crater region, sampling the surface chemistry directly with mass spectrometry {cite:p}`Lorenz2018`. Titan is the most chemically complex environment in the solar system after Earth, and it is the only place other than Earth where stable surface liquids exist today.

**Venus cloud layer.** The {cite:t}`Greaves2021` claim of phosphine ($\mathrm{PH_3}$) detection in the temperate Venus cloud deck at altitudes of $50$ to $60$ km was originally framed as a possible biosignature, on the grounds that no significant abiotic phosphine source is known under terrestrial planetary conditions. The community response was sceptical, and rightly so. Reanalysis of the same JCMT and ALMA data found that the phosphine spectral feature was at the edge of the instrumental sensitivity, that alternative molecular identifications (notably $\mathrm{SO_2}$ in the Venus mesosphere) reproduced the data well, and that independent observations either failed to confirm the original detection or were consistent with much lower upper limits {cite:p}`Lincowski2021` ({numref}`fig:l14:phosphine`).

```{figure} figures/lincowski2021_phosphine_so2.avif
:align: center
:name: fig:l14:phosphine
:width: 90%

Spectral simulations of the 266.94 GHz feature claimed as $\mathrm{PH_3}$ in the Venus clouds, showing that the same data are also consistent with mesospheric $\mathrm{SO_2}$ at the few-hundred-ppb level (rising from $\sim 30$ ppb at 78 km to $\sim 400$ ppb at 100 km altitude). The original {cite:t}`Greaves2021` detection sits at the edge of the instrumental noise floor and the alternative $\mathrm{SO_2}$ interpretation cannot be excluded. Reproduced from {cite:t}`Lincowski2021`.
```

The Venus phosphine episode is the *direct analogue* of the K2-18b DMS controversy on the exoplanet side. In both cases, the data are at the edge of the instrumental sensitivity, the molecular identification is contested, and plausible abiotic explanations exist that have not been ruled out. In both cases, the appropriate response is *neither* "this is biology" *nor* "the original team was incompetent". The right response is: extraordinary claims about biosignatures require extraordinary verification, and the path forward is a *better dataset*, ideally from independent instruments.

For Venus that better dataset is on the way. The DAVINCI atmospheric descent probe will measure the cloud chemistry and noble gas inventory in situ, EnVision will provide high-resolution surface and atmospheric mapping, and VERITAS, currently targeting a 2031 launch subject to NASA budget decisions, will provide high-resolution surface topography and mineralogy. None of these missions are designed primarily as life-detection missions, but the data they return will resolve the phosphine claim one way or another and will radically improve the constraints on the present-day Venus cloud chemistry.

**Pedagogical point.** The Venus phosphine and the K2-18b DMS cases are the same lesson under two different telescopes: claims about life-relevant chemistry on other worlds must clear a high bar, and the right way to resolve them is through better data, not through louder rhetoric. Both cases are valuable for the field even if both end up being non-detections, because they have driven the design of the next generation of instruments and missions.

### Exoplanet life detection: the strategy

Detecting life on an exoplanet is harder than detecting life on a solar system body because we cannot return a sample, we cannot land an instrument, and we cannot resolve the surface. All we have is the integrated transmission, emission, or reflectance spectrum of the planet ({numref}`fig:l14:lhs475b-spectrum` and {numref}`fig:l14:trappist1b` illustrate what current JWST observations can and cannot say about the atmospheres of small rocky planets around nearby M dwarfs).

```{figure} figures/lustigyaeger2023_lhs475b_spectrum.avif
:align: center
:name: fig:l14:lhs475b-spectrum
:width: 85%

JWST/NIRSpec G395H transmission spectrum of the Earth-sized rocky exoplanet LHS 475 b (black points), compared with model atmospheres of various compositions. The data rule out hydrogen-dominated atmospheres at $1\times$ to $100\times$ solar metallicity at high significance, and weakly disfavour pure $\mathrm{CH_4}$ or pure $\mathrm{H_2O}$ envelopes (top panel). High mean molecular weight atmospheres ($\mathrm{CO_2}$-dominated, Earth-like) and a featureless airless-body spectrum remain consistent with the data (bottom panel). This is representative of what current JWST observations can and cannot say about the atmospheres of rocky exoplanets around nearby M dwarfs. Reproduced from {cite:t}`LustigYaeger2023`.
```

```{figure} figures/greene2023_trappist1b_eclipse.avif
:align: center
:name: fig:l14:trappist1b
:width: 80%

JWST MIRI secondary eclipse light curve of TRAPPIST-1 b at 15 $\mu$m. The observed eclipse depth corresponds to a measured dayside brightness temperature of $T_d \approx 503$ K, consistent with the 508 K bare-rock zero-redistribution prediction and indicating that the planet has no thick atmosphere to redistribute heat. Reproduced from {cite:t}`Greene2023`.
```

The K2-18b case from {ref}`Lecture 13 <lecture13>` shows what a single-snapshot atmospheric detection looks like at the current state of the art and shows why it is *not enough* on its own to establish the presence of biology ({numref}`fig:l14:k218b-spec` shows the spectrum, {numref}`fig:l14:k218b-post` the corresponding posterior mixing-ratio distributions).

```{figure} figures/madhusudhan2023_k218b_spectrum.avif
:align: center
:name: fig:l14:k218b-spec
:width: 90%

JWST transmission spectrum of K2-18b from {cite:t}`Madhusudhan2023`. The combined NIRSpec and NIRISS data show clear $\mathrm{CH_4}$ and $\mathrm{CO_2}$ absorption features and the tentative DMS feature near 3.4 $\mu$m. The spectrum is consistent with a sub-Neptune atmosphere overlying either a "hycean" (hydrogen atmosphere over a global liquid-water ocean) layer or a deeper mini-Neptune envelope. Reproduced from {cite:t}`Madhusudhan2023`.
```

```{figure} figures/madhusudhan_k218b_dms_post.avif
:align: center
:name: fig:l14:k218b-post
:width: 90%

Posterior probability distributions for the mixing ratios of $\mathrm{CH_4}$, $\mathrm{CO_2}$, and DMS in the atmosphere of K2-18b, for three retrievals that differ only in how many instrument offsets are allowed to float: none (blue), one (orange), and two (pink). The horizontal bars give each distribution's median and $1\sigma$ interval. $\mathrm{CH_4}$ and $\mathrm{CO_2}$ are recovered at about $5\sigma$ and $3\sigma$ and their posteriors shift only slightly between the three cases. The DMS posterior behaves in the opposite way: $2.4\sigma$ with no offset, about $1\sigma$ with one, and no longer significant with two. That sensitivity to a nuisance parameter is exactly the inverse-problem issue that makes single-snapshot biosignature claims hard to validate. Reproduced from {cite:t}`Madhusudhan2023`.
```

A *convincing* biosignature detection on an exoplanet would therefore require some combination of the following:

1. **Multiple independent gases in disequilibrium**, ideally one oxidising and one reducing, that cannot coexist over photochemical timescales without continuous resupply.
2. **Temporal variability** consistent with a biological cycle (seasonal, diurnal, or longer).
3. **Geological context** (planet mass, radius, host-star type, age, escape history) that excludes the most obvious abiotic production pathways.
4. **Independent confirmation** by a different instrument, wavelength range, or observatory.

The Habitable Worlds Observatory (HWO) and the LIFE concept are designed for exactly this multi-line, multi-target campaign. HWO is a NASA flagship, prioritised in the {cite:t}`NAS2021` decadal survey, that will use a $\sim 6$ m space-based coronagraph, an instrument that masks the star's light so that a much fainter nearby planet becomes visible, in the visible and near-infrared to directly image and spectrally characterise Earth-like planets around $\sim 25$ nearby Sun-like stars. The launch target is the early 2040s. LIFE (Large Interferometer For Exoplanets) is an ESA-led concept for a mid-infrared nulling interferometer, an array of telescopes that combines their light so the starlight cancels by destructive interference while the planet's light does not, that would target the same population in a complementary wavelength range, where the diagnostic biosignature gases ($\mathrm{O_3}$, $\mathrm{H_2O}$, $\mathrm{CH_4}$, $\mathrm{CO_2}$) all have strong spectral features {cite:p}`Quanz2022` ({numref}`fig:l14:life-yields`).

```{figure} figures/quanz2022_life_yields.avif
:align: center
:name: fig:l14:life-yields
:width: 90%

Predicted total exoplanet detection yields for the LIFE mission during a 2.5-year search phase, as a function of mirror aperture diameter ($D = 1$ to $3.5$ m), shown for two assumed instrument scenarios (lower and upper bars). A 3.5 m aperture LIFE configuration would detect of order $500$ to $800$ planets in total; the per-category breakdown reported by {cite:t}`Quanz2022` includes $\sim 25$ rocky habitable-zone planets around FGK stars, with the remainder distributed across larger rocky planets, sub-Neptunes, and sub-Jovians. Reproduced from {cite:t}`Quanz2022`.
```

The earliest plausible robust detection of biosignatures on an Earth-like exoplanet is, on the current mission timelines, in the 2040s rather than the 2030s. The 2030s will be the era of statistical atmospheric characterisation (Ariel), of better demographic constraints (PLATO, Roman), and of solar system in-situ work (Europa Clipper, JUICE, Dragonfly, EnVision, Mars Sample Return on the re-baselined schedule). The flagship life-detection missions for exoplanets come a decade later.

The course's frank assessment, reading the 2026 mission queue and the JWST atmospheric results so far, is that we do not yet know whether life is common in the galaxy or vanishingly rare. We do not yet know whether the solar system is rare or typical. The next generation of telescopes will tell us, and *either answer will be profound*: a positive detection would change biology, philosophy, and our place in the cosmos; a negative result, after a decade of dedicated searches, would put a hard upper limit on $f_l$ and force a revision of how we think about the origin of life. For the first time, the question "are we alone?" is becoming an empirical one rather than a philosophical one, and the answer will arrive within the careers of the students in this room.


## Course wrap-up

### The five biggest things we have learned

1. **Planet formation is a physical process**, governed by accretion, gravity, and disk dynamics, not by chance. It produces a predictable diversity of outcomes, and the same laws operate everywhere.
2. **Planetary interiors are heat engines** whose evolution drives surface tectonics, volcanic outgassing, magnetic dynamos, and ultimately the long-term habitability of the surface, all on Gyr timescales.
3. **Atmospheres are not static.** They form, evolve, escape, react with their interiors, and feed back on surfaces and biospheres. There is no such thing as a "default" atmosphere; every atmosphere has a history.
4. **Habitability is a coupled systems property.** It depends on stellar, orbital, planetary, and biospheric factors operating *together* over time, and no single parameter on its own ("temperature in the HZ") is sufficient to predict it. The course's central qualitative framework is the coupling loop of Part 2, which links star, atmosphere, surface, and interior.
5. **The solar system is one example** in a much larger population. It is useful as a reference system because we know it in extraordinary detail, but it is not, on current evidence, an obvious benchmark for what counts as typical. The exoplanet population is now the statistical context against which solar-system results have to be read.

### The five biggest open questions

1. **How does life originate?** And how often does it originate, given a planet that meets the necessary conditions? Is the origin of life on Earth a rare accident or a generic chemical inevitability? This is the largest single uncertainty in any quantitative habitability estimate.
2. **What sets the radius valley?** Is it photoevaporation, core-powered mass loss, or distinct formation channels for super-Earths and sub-Neptunes? The answer matters because it tells us how universal atmospheric loss is.
3. **When did Jupiter form**, and was Jupiter the architect of the inner solar system or one player among many? The answer affects how we interpret the NC--CC dichotomy and how we think about the rarity of Earth-like systems.
4. **Was Mars ever inhabited?** And if so, when did it stop, and why? Mars Sample Return is the most direct path to answering this, and the answer either way will recalibrate our prior on $f_l$.
5. **Is the solar system rare or typical?** And what would an answer look like? PLATO + Gaia DR4/DR5 + a decade of long-baseline RV will start to provide the data, but the answer will be probabilistic rather than yes-or-no.

### The next decade

The mission queue from now to roughly 2040 is unusually rich. The graphic version of the next paragraph is the standard "mission timeline" figure that NASA, ESA, and JAXA all maintain; the verbal version is below.
All dates below are planning targets as of early 2026 and are commonly revised by months to years over the course of mission development.

**Now to 2030.** JWST continues to deliver atmospheric spectra of every accessible exoplanet. Europa Clipper arrives at Jupiter in 2030 and begins its 50-flyby ice-shell and ocean-chemistry campaign. JUICE is in cruise and arrives at Jupiter in 2031; its dedicated Ganymede orbital phase begins in 2034. BepiColombo enters Mercury orbit in 2026. The Mars Sample Return architecture is being re-baselined; samples are still cached at Jezero awaiting the new return plan. DART/Hera continue to characterise the Didymos system after the kinetic deflection test. Lucy completed its main-belt flybys of Dinkinesh (2023) and Donaldjohanson (2025) and is in cruise to its first Jupiter Trojan encounter, Eurybates, in August 2027. Roman launches in late 2026, PLATO in early 2027, Dragonfly in 2028, and Ariel in 2029.

**2030s.** Europa Clipper science peaks. JUICE begins Ganymede orbit. Dragonfly arrives at Titan in 2034 and rotorcraft surface science begins. Ariel delivers its statistical exoplanet atmosphere survey. ELT ({numref}`fig:l14:elt-milkyway`), GMT, and TMT come online for high-contrast imaging and high-resolution spectroscopy of nearby exoplanets. DAVINCI, EnVision, and VERITAS deliver Venus atmospheric, surface, and subsurface results. Mars Sample Return delivery, if the re-baselined plan holds, is also in this decade. Uranus orbiter mission concept advances toward a probable launch in the early 2030s.

```{figure} figures/elt_milkyway.avif
:name: fig:l14:elt-milkyway
:width: 700px
:align: center

The Milky Way arcs over ESO's Extremely Large Telescope under construction on Cerro Armazones in the Chilean Atacama Desert, with the partially-clad dome visible at lower left (August 2025). With its 39 m segmented primary mirror, the ELT will be the largest optical/near-infrared telescope ever built when it sees first light in 2028 and will, together with GMT and TMT, enable the first direct-imaging searches for atmospheric biosignatures on rocky planets around nearby M dwarfs. Image credit: C. Letelier/ESO {cite:p}`ESOELT2025`.
```

**2040s.** HWO and LIFE concept maturation transitions into hardware. The first plausible direct atmospheric characterisation of Earth-analogue exoplanets becomes possible. A full multi-line biosignature campaign on the most promising targets can be designed and executed. Whatever the answer, it will fundamentally change planetary science.

### Final framing

Planetary science has, over the lifetime of the students in this room, become *the science of comparative climate, interior, and life-hosting trajectories*. The solar system is the reference system, but no longer the benchmark. The exoplanet population provides the statistical context that the solar system on its own cannot. The questions this course has covered are open questions, not closed ones. The frontier is moving fast: if you continue in this field, what you learn next will change what this lecture says.

That last point is the honest one to end on. A course like this is necessarily a snapshot. The Drake equation, the K2-18 b DMS claim, the Venus phosphine claim, the radius valley mechanism, the timing of Jupiter's formation, the Mars Sample Return architecture: every one of these will look different to a student reading this lecture in 2030 than it does today. The physics and the questions, however, will be largely the same. If you take away one thing from these fourteen lectures, let it be the *systems-level view*: that habitability, formation, escape, weathering, and biology are not separate problems but a single coupled problem with one consistent set of physical principles, the same set of principles wherever you go in the galaxy. *That* is what the course has been about.


## References

```{bibliography}
:filter: docname in docnames
```
