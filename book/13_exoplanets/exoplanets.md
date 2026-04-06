(lecture13)=
# Lecture 13: Exoplanets, Detection Methods, Demographics & Characterisation

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe the main exoplanet detection methods and their observational biases, interpret the period-radius diagram and its key features (radius valley, hot Neptune desert, peas-in-a-pod), apply the transit and radial velocity geometry to derive planetary mass, radius, and bulk density, and evaluate JWST-era atmospheric characterisation results and their implications for habitability and biosignatures.
```

```{note}
**Status:** Detailed bullet outline below. Full prose sections to be written in a subsequent pass. The lecture follows the same descriptive-first, payoff-at-the-end structure as L9-L12: detection methods (Part 1), then demographics and architectures (Part 2), then characterisation, habitability, and the comparative payoff (Part 3).
```


## Part 1: How we find exoplanets

### Historical context

- **1992**: Wolszczan & Frail discover the first confirmed exoplanets around pulsar **PSR B1257+12** via pulse-timing variations; three terrestrial-mass bodies
- These were not the planets anyone was looking for, and remain the reminder that exoplanets can form in extreme environments (post-supernova debris)
- **1995**: Mayor & Queloz discover **51 Pegasi b**, the first exoplanet around a sun-like star, via radial velocity at ELODIE (Nobel Prize 2019)
- **Surprise**: a Jupiter-mass planet on a 4.2-day orbit, right next to its star, contradicting the expectation that gas giants form and stay at $\sim$5 AU
- This one detection launched the **migration revolution** and re-opened planet-formation theory to disk-driven and high-eccentricity mechanisms
- Subsequent expansion: ground-based RV surveys $\rightarrow$ CoRoT (2006) $\rightarrow$ Kepler (2009) $\rightarrow$ K2, TESS, CHEOPS, JWST
- Present count: $>$6000 confirmed exoplanets, $\sim$4000 planetary systems, as of 2025 (NASA Exoplanet Archive)

### Radial velocity method

- The star wobbles around the system's barycentre as the planet orbits
- Observable: periodic Doppler shift in stellar absorption lines
- Semi-amplitude
- $$K_\star = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{(M_\star + m_p)^{2/3}} \frac{1}{\sqrt{1 - e^2}}$$
- Typical scales: Jupiter around a Sun-like star gives $K \sim 12$ m/s; Earth gives $K \sim 0.09$ m/s; super-Earths fall in between
- **$m \sin i$ degeneracy**: RV alone gives only the minimum mass; the true mass requires an independent measurement of the orbital inclination (transit, astrometry, or direct imaging)
- Instrumental evolution: ELODIE $\sim$10 m/s (1995) $\rightarrow$ HARPS $\sim$1 m/s (2003) $\rightarrow$ ESPRESSO $\sim$10 cm/s (2018); current floor limited by **stellar noise** (granulation, spots, p-modes), not photon statistics
- Strongest yields: long-period massive planets around bright quiet stars (selection bias against low-mass, long-period, rapidly-rotating hosts)

### Transit method

- When the planetary orbit is aligned near edge-on, the planet periodically blocks a fraction of the stellar disk
- **Transit depth** (primary observable): $\delta = (R_p/R_\star)^2$
- For a Jupiter around the Sun: $\delta \sim 1\%$; for an Earth: $\delta \sim 10^{-4}$ ($\sim$80 ppm)
- Transit **duration, ingress shape, and limb-darkened light curve** constrain impact parameter, inclination, and $R_\star$
- **Geometric transit probability** $\approx R_\star / a$: only $\sim$0.5% for Earth--Sun, $\sim$10% for hot Jupiters — a strong bias toward short periods
- Missions:
  - **CoRoT** (2006--2013): first space-based transit survey
  - **Kepler** (2009--2013) + **K2** (2014--2018): monitored $\sim$150{,}000 stars continuously; produced the first statistically complete exoplanet sample
  - **TESS** (2018--): all-sky, bright nearby stars, thousands of planets for follow-up
  - **CHEOPS** (2019--): precision photometry for known targets
  - **PLATO** (launch 2026): terrestrial planets in the habitable zones of Sun-like stars; designed for true Earth-analogue searches
- Selection bias: short periods, large planets, bright/quiet stars

### Blackboard derivation (~10 min): Transit depth, radial velocity, and bulk density

- **Transit depth** (~2 min): drop a disk of radius $R_p$ across a uniformly bright stellar disk of radius $R_\star$
- $$\frac{\Delta F}{F} = \left(\frac{R_p}{R_\star}\right)^2$$
- Direct observable $\rightarrow$ $R_p$ if $R_\star$ is known (from stellar models or interferometry)

- **Radial velocity semi-amplitude** (~5 min): conservation of momentum for a two-body system
- Star and planet orbit the barycentre with speeds $v_\star$ and $v_p$; $M_\star v_\star = m_p v_p$
- Circular orbit, edge-on ($i = 90^\circ$): $v_p = 2\pi a_p / P$, $v_\star = (m_p / M_\star) v_p$
- Kepler's third law: $a = \big(GM_\star P^2 / 4\pi^2\big)^{1/3}$
- Combining: $K_\star \propto m_p \sin i / M_\star^{2/3} P^{1/3}$ (the full prefactor gives the equation above)

- **Combine both observables** (~3 min): RV gives $m_p \sin i$; transit constrains $\sin i \approx 1$
- Therefore $R_p$ **and** $m_p$, hence bulk density
- $$\bar{\rho}_p = \frac{3 m_p}{4\pi R_p^3}$$
- **Key insight**: the transit+RV combination breaks the $m \sin i$ degeneracy and turns exoplanets from abstract detections into **physical objects** with measurable bulk composition

### Direct imaging

- Spatially resolve the planet from the star
- Extreme challenges: contrast of $10^{-6}$ to $10^{-10}$ at sub-arcsecond separations
- Techniques:
  - **Coronagraphs** block the stellar light inside the focal plane (Lyot, apodised, vortex designs)
  - **Adaptive optics** correct atmospheric turbulence in real time
  - **Angular differential imaging (ADI)** and **spectral differential imaging (SDI)** suppress residual speckles
- Current sensitivity:
  - Ground-based (SPHERE, GPI, SCExAO): young ($<$100 Myr), self-luminous giant planets at $>$10 AU from nearby stars
  - Space-based (JWST NIRCam/MIRI coronagraphs): deeper into the infrared, reaches older / cooler planets
- Notable directly imaged systems: **HR 8799** (four giants, multi-epoch astrometry), **Beta Pictoris b/c**, **51 Eri b**, **PDS 70 b/c** (first planet discovered still inside a protoplanetary disk gap, recap from {ref}`lecture02`)
- **JWST 2023**: first direct image of an exoplanet atmosphere with MIRI (Carter et al. 2023, Miles et al. 2023)
- Selection bias: young, massive, wide-orbit, self-luminous planets — a complementary slice of parameter space to transits and RV

### Astrometry

- Measure the **spatial wobble** of the star against background reference stars as it orbits the system barycentre
- Amplitude: $\alpha = (m_p / M_\star)(a / d)$, requiring microarcsecond precision for Jupiter-analogues
- **Hipparcos** (1989--1993): first astrometric missions; marginal planetary sensitivity
- **Gaia** (2014--): billion-star astrometric survey at $\sim$20--50 microarcsecond precision
- **Gaia DR3 (2022)**: published the first candidate astrometric exoplanet (Gaia-BH1 / astrometric Jupiter analogues)
- **Gaia DR4** (expected 2026) will release time-series astrometry and is projected to deliver $10^2$--$10^3$ confirmed astrometric exoplanets
- **Gaia DR5** (expected late 2020s) will push into the sub-Jovian regime for nearby stars
- Complementary to RV: astrometry provides **inclination** directly, breaking the $m \sin i$ degeneracy
- Sensitive to long-period planets where RV time baselines are insufficient
- Particular strength: wide-orbit gas giants around nearby sun-like stars — the "Jupiter analogue" regime that other methods miss

### Microlensing

- A foreground star + planet passes in front of a background source; the planet perturbs the stellar microlensing light curve
- Sensitivity: planets near the Einstein ring radius ($\sim$1--10 AU for typical lens geometries)
- Finds planets at distances of **kiloparsecs**, unreachable by any other method
- Events are **one-shot** (no follow-up possible)
- **OGLE, MOA, KMTNet** surveys ongoing
- **Nancy Grace Roman Space Telescope** (launch 2027): microlensing exoplanet survey expected to find $\sim$1000--3000 planets including free-floating rogue planets

### Timing methods

- **Transit timing variations (TTVs)**: gravitational interactions between planets in a multi-planet system perturb each other's transit times
- Provide **dynamical masses** independent of RV, especially valuable for small planets where RV is infeasible (Kepler-11, Kepler-36, TRAPPIST-1)
- **Pulsar timing**: the original method (Wolszczan & Frail 1992)
- **Eclipse timing variations** in binary star systems: some circumbinary planets first detected this way (e.g., Kepler-16 b, "Tatooine")

### Detection biases summary

- Dedicated slide showing the (mass, period) coverage of each method on a single plot
- **Transit**: short periods ($<$100 days), large $R_p/R_\star$ ratios, bias toward M-dwarf and close-in systems
- **RV**: 1--10 yr periods, massive planets around bright quiet stars
- **Direct imaging**: wide orbits ($>$10 AU), young hot planets around nearby stars
- **Astrometry**: wide orbits, massive planets, nearby stars (sweet spot: Jupiter analogues at 5--20 AU)
- **Microlensing**: 1--10 AU, any stellar type, far distances, unrepeatable
- **Timing**: existing multi-planet or compact systems
- **The "shape" of the exoplanet archive** (the observed population) reflects these biases as much as it reflects the true underlying distribution — a critical caveat when reading the period-radius diagram


## Part 2: Demographics and architectures

### The Kepler revolution

- Kepler monitored $\sim$150{,}000 main-sequence stars for $\sim$4 years continuously
- First **statistically complete** exoplanet sample: every candidate's detection efficiency is computable, allowing occurrence-rate inference
- Key result: planets are **common**, and small planets are the most common of all
- Occurrence rates (Kepler + TESS combined, approximate):
  - $\gtrsim$1 planet per star on average
  - $\sim$50\% of Sun-like stars host a small ($R < 4\,\Rearth$) planet within 1 AU
  - Hot Jupiters: $\sim$0.5--1\% of sun-like stars
  - Earth-like planets in the habitable zone ($\eta_\oplus$): 0.1--0.6 depending on definition and uncertainty (Bryson et al. 2021)

### The period-radius diagram

- The central empirical object of exoplanet demographics
- X-axis: orbital period (log); Y-axis: planet radius (log)
- **Populations visible as clusters**:
  - **Hot Jupiters** ($R > 10\,\Rearth$, $P < 10$ d)
  - **Warm and cold Jupiters** (intermediate periods)
  - **Sub-Neptunes / mini-Neptunes** ($R \sim 2$--$4\,\Rearth$)
  - **Super-Earths** ($R \sim 1$--$1.8\,\Rearth$)
  - **Terrestrial analogues** ($R < 1.5\,\Rearth$, long period, largely unexplored)

### The radius valley (Fulton gap)

- **Fulton et al. 2017**: high-resolution Keck follow-up of Kepler targets reveals a deficit of planets at $R \sim 1.8\,\Rearth$
- Splits the population into **super-Earths** (rocky, $R < 1.8\,\Rearth$) and **sub-Neptunes** (volatile-rich, $R > 1.8\,\Rearth$)
- **Two competing interpretations**:
  1. **Photoevaporation**: XUV stellar flux strips primordial H/He envelopes from close-in planets (Owen & Wu 2013)
  2. **Core-powered mass loss**: residual internal heat from the rocky core drives envelope escape (Ginzburg et al. 2018; Gupta & Schlichting 2019)
- Both mechanisms predict the valley location as a function of period, mass, and stellar age — current data do not yet fully discriminate, but both require a population of close-in rocky planets whose atmospheres were stripped
- **Implication**: super-Earths may be the bare cores of former sub-Neptunes, not a distinct formation channel

### The hot Neptune desert

- Depletion of Neptune-mass planets ($\sim$10--100 $\Mearth$) at short periods
- Attributed to photoevaporation + Roche-lobe overflow on a population formed with thick H/He envelopes but low gravitational binding
- Edge of the desert is well-defined in the data (Mazeh et al. 2016)

### Planetary system architectures

- **Peas in a pod** (Weiss et al. 2018): planets within multi-planet systems tend to be similar in size and uniformly spaced in period
- Suggests formation is a **smooth, local process** rather than driven by stochastic large impacts
- **Compact multi-planet systems**: TRAPPIST-1 (7 planets within 0.06 AU), Kepler-90 (8 planets), TOI-178 (6 planets in resonant chain)
- **Resonant chains**: TRAPPIST-1 has 5 adjacent mean-motion resonances; evidence for early disk-driven migration into resonance followed by long-term stability
- Not every system is "peas in a pod": radial-velocity-selected samples show substantial architectural diversity

### Hot Jupiters and migration

- Hot Jupiters must have **formed further out** (beyond the ice line, $\sim$3--5 AU) and **migrated inward** to their present orbits
- Three competing mechanisms:
  1. **Disk migration** (Type II): torques from a gas-rich disk drive inward drift while the disk is still present ($\lesssim$few Myr)
  2. **High-eccentricity migration**: a distant perturber (giant planet or binary companion) drives Kozai-Lidov oscillations; once the perihelion is close enough, tidal dissipation circularises the orbit at short period
  3. **Planet-planet scattering**: dynamical instability in a multi-giant system ejects one and leaves survivors on eccentric orbits that tidally circularise
- Observational discriminants:
  - **Obliquities** (angle between stellar spin and orbital axis) measured via Rossiter-McLaughlin effect: many hot Jupiters are misaligned, favouring high-eccentricity migration for a substantial fraction
  - **Companion multiplicity**: hot Jupiters are often lonely — lacking nearby companions — consistent with dynamical histories that cleared neighbours
- Current consensus: all three mechanisms operate; their relative contributions depend on host-star type and system architecture

### Super-Earth and sub-Neptune composition

- **Bulk-density comparison** between rocky and volatile-rich categories
- Some sub-Neptunes consistent with "water worlds": $\gtrsim$10--20\% H$_2$O by mass
- Others consistent with "gas dwarfs": rocky core + H/He envelope
- **K2-18 b** and the **hycean world** hypothesis (Madhusudhan et al. 2023): a sub-class with shallow surface oceans under thick H$_2$-rich atmospheres, opening a new candidate habitable regime — but the interpretation is contested
- **Venus-analogue** versus **water-world** ambiguity for close-in small planets: the same bulk density can match very different atmospheric histories

### M dwarf planets

- M dwarfs are the most abundant star type in the galaxy ($\sim$75\% of all stars)
- They host short-period small planets at high occurrence rates
- The **geometric transit probability** is high because the stars are small and close: easier to find habitable-zone planets in transit around M dwarfs than around G stars
- Concern: M dwarf flares, XUV flux, and long pre-main-sequence high-luminosity phases could strip atmospheres from early planets (Luger & Barnes 2015)
- **TRAPPIST-1**: seven Earth-sized planets around an ultra-cool dwarf at 12 pc; the reference laboratory for M dwarf habitability


## Part 3: Characterisation, habitability, and the comparative payoff

### Transmission spectroscopy during transit

- During transit, a fraction of stellar light passes through the planet's atmosphere
- Absorption imprints a wavelength-dependent signal on the transit depth
- Effective depth: $\delta(\lambda) = [R_p + nH(\lambda)]^2 / R_\star^2$ where $H = k_B T / \mu g$ is the atmospheric scale height
- Detectable species: H$_2$O, CO, CO$_2$, CH$_4$, Na, K, SO$_2$, H$_2$S, and more
- **Cloud suppression**: high-altitude clouds or hazes can mute or erase the spectral features, flattening the observed spectrum
- Typical signal size: 100--1000 ppm for hot Jupiters, 10--100 ppm for sub-Neptunes, $\lesssim$10 ppm for rocky planets (extremely demanding)

### Emission spectroscopy and phase curves

- **Secondary eclipse** (when the planet passes behind the star): direct measurement of the planet's dayside thermal flux
- **Phase curves**: continuous monitoring across the orbit to map day-night temperature contrast and wind circulation
- Strong heat redistribution implies a thick atmosphere; weak redistribution implies thin or no atmosphere
- Joint transit + secondary eclipse + phase curve data yield a self-consistent atmospheric radiative-transfer model

### JWST era results (2022--2025)

- **WASP-39 b** (early-release science, Rustamkulov et al. 2023, Alderson et al. 2023, Ahrer et al. 2023): first JWST transmission spectrum of a hot Jupiter; clean detections of H$_2$O, CO, CO$_2$, Na, K, and **photochemical SO$_2$** (Tsai et al. 2023) — first unambiguous evidence for disequilibrium photochemistry in an exoplanet atmosphere
- **HD 189733 b**: H$_2$S detection (Fu et al. 2024), probing sulphur chemistry and metallicity
- **WASP-107 b**: methane depletion implies vertical mixing + photochemistry (Dyrek et al. 2024); retrieved high interior temperature
- **K2-18 b** (Madhusudhan et al. 2023): CH$_4$ and CO$_2$ detected in transmission; **tentative DMS (dimethyl sulphide) detection** claimed as a potential biosignature
  - Community response has been sceptical: the DMS feature is at the edge of JWST sensitivity, heavily dependent on retrieval assumptions, and rebuttals argue for alternative molecules or instrument systematics (Glein 2024, Wogan et al. 2024)
  - Regardless of outcome, K2-18 b is the pedagogical case study for **how biosignature claims are tested and revised** in real time
- **TRAPPIST-1 b** (Greene et al. 2023): MIRI thermal emission at 15 $\mu$m consistent with a **bare rock dayside** (no substantial atmosphere); planet is dark and hot
- **TRAPPIST-1 c** (Zieba et al. 2023): similar non-detection — rules out Venus-like thick CO$_2$ atmospheres for both inner TRAPPIST-1 planets
- **Rocky-planet atmosphere non-detections**: LHS 475 b (Lustig-Yaeger et al. 2023), GJ 486 b (Moran et al. 2023), GJ 1132 b (May et al. 2023) — consistent with thin or absent atmospheres, strengthening the case that **M dwarf XUV flux strips the atmospheres** of early close-in planets
- **55 Cancri e** (Hu et al. 2024): MIRI thermal emission + phase curve; tentative detection of a secondary **CO/CO$_2$-rich atmosphere** around this "super-Earth lava world" — the first atmospheric detection on a rocky world around a sun-like star, though still being scrutinised
- **TOI-561 b** (Patel et al. 2023, subsequent follow-up): ultra-short-period rocky planet orbiting a metal-poor thick-disk star; tentative evidence for a thin atmosphere or surface composition signal; case study in marginal detections
- Direct imaging spectra: **HIP 65426 b**, **VHS 1256 b** (Miles et al. 2023) yielded mid-IR spectra with atmospheric features detected for the first time at these wavelengths

### The habitable zone revisited

- 1D radiative-convective climate models (Kasting et al. 1993; Kopparapu et al. 2013) define classical HZ boundaries
- **Inner edge** (runaway greenhouse): set by the Simpson-Nakajima limit (blackboard recap from {ref}`lecture09`)
- **Outer edge** (maximum CO$_2$ greenhouse): limit beyond which CO$_2$ ice condensation suppresses the greenhouse effect
- **History dependence matters** (recap from {ref}`lecture09` Earth-Venus divergence): climate-evolution trajectories, not snapshot HZ boundaries, determine which planets stay habitable
- For M dwarfs: habitable zone is close in, planets are likely **tidally locked**, and the pre-main-sequence high-luminosity phase can trigger early runaway greenhouse on planets that later enter the HZ
- 3D GCM modelling (e.g., Way et al. 2016, Wordsworth 2015, Turbet et al. 2021) gives more realistic boundaries and reveals cloud feedbacks that extend the HZ

### Biosignature gases and the challenge of false positives

- Classical biosignature gases: **O$_2$**, **O$_3$**, **CH$_4$**, **N$_2$O** — disequilibrium indicators
- The strongest signal is a **disequilibrium combination**: e.g., O$_2$ + CH$_4$ together cannot coexist without continuous replenishment
- **Abiotic false positives**:
  - Photolysis of H$_2$O on dry worlds can produce abiotic O$_2$ (Wordsworth & Pierrehumbert 2014)
  - CO$_2$ photolysis generates O$_2$ in CO$_2$-rich atmospheres
  - Volcanic outgassing and serpentinisation can produce abiotic CH$_4$
- Biosignature detection is an **inverse problem**: a single gas means little, context and combinations are everything
- **DMS** (K2-18 b) has been proposed as a biosignature because no significant abiotic pathway is known on Earth — but "not known on Earth" is not the same as "impossible elsewhere"

### Comparative payoff: the solar system in the exoplanet landscape

- **What is typical in the exoplanet archive?**
  - Most planets orbit M dwarfs (by number of host stars)
  - Most planets are sub-Neptune sized
  - Most planetary systems are compact and "peas in a pod"
  - Hot Jupiters are rare ($\sim$1\%)
- **How does the solar system compare?**
  - Sun is a G dwarf: uncommon as a host star
  - No planet between Earth and Neptune in radius: the solar system **skips the most common planet class**
  - No hot Jupiter or hot Neptune: clean inner architecture
  - No compact "peas in a pod" inner system: Mercury, Venus, Earth, Mars are irregularly spaced
  - Giant planets on wide, near-circular, low-inclination orbits: atypical relative to dynamically hot exoplanet systems
- **Is the solar system rare or just drawn from a wide distribution?** Current answer: **not clear yet**. Detection biases favour short-period, massive systems; Jupiter analogues are only now accessible via RV + Gaia DR4/DR5
- **Key insight**: the solar system is not obviously typical, but whether it is genuinely rare or just in a sparsely sampled corner of parameter space depends on the long-period, low-mass detection floor of the next decade
- Forward reference: the HZ is not a line but a history-dependent trajectory (recap from {ref}`lecture09`); single-snapshot habitability is insufficient; climate-evolution models must be coupled to detection ({ref}`lecture14`)

### Frontier missions, part 1: transits and atmospheres (2026--2035)

- **PLATO** (ESA, launch 2026): photometric survey for small planets in the habitable zones of **Sun-like stars** — the primary goal is finding true Earth analogues around G dwarfs; complements Kepler by observing brighter stars so that RV follow-up is feasible
- **Ariel** (ESA, launch 2029): dedicated transmission + emission spectroscopy of $\sim$1000 exoplanet atmospheres across 0.5--7.8 $\mu$m; statistical characterisation of atmospheric composition as a function of planet and host properties
- **Roman Space Telescope** (NASA, launch 2027): wide-field microlensing + coronagraphic imaging; expected to deliver $\sim$1000--3000 microlensing planets and technology demonstration for future direct-imaging flagships

### Frontier missions, part 2: direct imaging of Earth analogues (2030s--2040s)

- **Habitable Worlds Observatory** (HWO, NASA concept): top priority of the 2020 US Decadal Survey; space-based coronagraph at $\sim$6 m class, targeting direct imaging and spectral characterisation of Earth-like planets around $\sim$25 nearby sun-like stars; launch target 2040s
- **LIFE** (ESA concept, Quanz et al.\ 2022): mid-infrared nulling interferometer to directly detect and spectrally characterise the thermal emission of Earth-analogue exoplanets; complementary to HWO in wavelength coverage (targets CO$_2$, O$_3$, H$_2$O, CH$_4$ in mid-IR)
- **Extremely Large Telescopes** (ELT 39 m, GMT 25 m, TMT 30 m, all ground-based, first light 2028--early 2030s): high-contrast imaging + high-resolution spectroscopy of nearby exoplanet atmospheres, including Proxima Centauri b (potentially)
- Collectively, these missions will push exoplanet science from **statistical demography** (where we are today) to **individual characterisation of potentially habitable worlds**
- **Open question**: what combination of evidence would constitute convincing detection of life on another world? A single gas? A combination? Temporal variability? This is the frontier that sets the design goals for all the missions above (forward to {ref}`lecture14`)


## Summary and takeaways

- Exoplanets went from zero confirmed cases in 1991 to $>$6000 in 2025: a complete revolution in the observational picture of planetary systems
- **Each detection method has a distinct bias**, and the observed planet population reflects the union of those biases as much as it reflects the true distribution
- **Kepler showed that planets are common** — most stars host at least one, and small planets are the most common of all
- The **radius valley** at $\sim$1.8 $\Rearth$ is the defining demographic feature, and points to atmospheric mass loss as a universal process in close-in planet evolution
- **JWST has moved exoplanet atmospheres from a promise to a routine capability**, with disequilibrium chemistry (WASP-39 b SO$_2$) and rocky-planet atmosphere constraints (TRAPPIST-1, 55 Cnc e, TOI-561 b) representing the current frontier
- **The solar system is not an obviously typical system**: no sub-Neptunes, no compact inner architecture, no hot giants — but the "typical" distribution is still under observational construction
- **Habitability is a history-dependent trajectory**, not a line on an HR diagram; biosignature detection is an inverse problem with unavoidable false-positive challenges
- The **2026--2040 mission queue** (PLATO, Ariel, Roman, HWO, LIFE, ELT) will push from demography to individual characterisation of potentially habitable worlds


## References

```{bibliography}
:filter: docname in docnames
```
