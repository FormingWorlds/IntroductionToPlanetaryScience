# Course Development: Introduction to Planetary Science

**Course code:** WBAS002-05
**Institution:** Kapteyn Astronomical Institute, University of Groningen
**Level:** 2nd-year BSc Astronomy
**Credits:** 5 ECTS
**Duration:** 8 weeks (7 teaching weeks + 1 exam week)
**Period:** September–November 2026

---

## 1. Course Overview

### Objectives

Students completing this course will be able to:

- Describe the formation and evolution of planetary systems from protoplanetary disks to mature systems
- Explain the physical and chemical processes governing planetary interiors, surfaces, and atmospheres
- Compare and contrast the properties of solar system bodies across different categories (rocky planets, gas/ice giants, small bodies)
- Apply fundamental physics (thermodynamics, orbital mechanics, radiative transfer) to planetary science problems
- Evaluate exoplanet detection methods and interpret observational data in the context of planetary demographics
- Synthesize knowledge across sub-disciplines to assess planetary habitability

### Prerequisites

- Classical Mechanics (orbital dynamics, energy conservation)
- Thermodynamics (heat transfer, phase equilibria)
- Introduction to Astrophysics or equivalent (stellar structure basics, electromagnetic spectrum)
- Basic Python programming (for computational homework problems)

### Assessment

| Component | Weight | Format |
|-----------|--------|--------|
| Mid-term exam | 30% | Written, 60 minutes |
| Final exam | 70% | Written, 90 minutes, cumulative |

- **Homework sheets** (7 total) are **ungraded formative practice**. Students are strongly encouraged to complete them as preparation for exams; solutions are discussed in tutorial sessions.
- All lecture notes are custom-developed for this course (no required textbook).

### Weekly Structure

Each week consists of:
- 2 × 90-minute lectures
- 1 tutorial/exercise session (weeks with homework due)

### Week-by-Week Schedule

| Week | Lectures | Homework | Notes |
|------|----------|----------|-------|
| 1 | L1: Introduction & History; L2: Formation & Orbits | | |
| 2 | L3: Heat & Energy; L4: Differentiation & Magnetospheres | HW 1 due | |
| 3 | L5: Atmospheres I; L6: Atmospheres II | HW 2 due | |
| 4 | L7: Surfaces; **Mid-term exam (60 min)** | HW 3 due | Mid-term covers L1–7 |
| 5 | L8: Interiors; L9: Earth & Venus | HW 4 due | |
| 6 | L10: Mercury & Mars; L11: Gas & Ice Giants | HW 5 due | |
| 7 | L12: Small Bodies; L13: Exoplanets; L14: Synthesis | HW 6 due | 3 lectures this week |
| 8 | **Final exam (90 min)** | HW 7 due | Exam week |

---

## 2. Lecture Schedule

### Lecture 1: Introduction & History of Planetary Science

- Opening: The Pale Blue Dot — Voyager 1's 1990 image of Earth as a sub-pixel speck from 40 AU, reframing our world as one planet among many
- Three driving questions that structure the course: (1) How did our solar system form, and is it typical? (2) What determines whether a planet becomes habitable? (3) Are we alone?
- What is a planet? Historical definitions, the IAU debate, and classification schemes
- Brief history of planetary science: from antiquity through the space age to modern surveys
- Overview of the solar system: architecture, scale, and key properties
- **Blackboard derivation (~10 min):** Estimate the total mass of the solar system's planets from Newtonian gravity — derive the planet-to-star mass ratio from orbital period and semi-major axis using Kepler's third law and compare to the observed value
- Comparative planetology as a methodology
- Observational techniques: ground-based, space missions, in situ measurements
- Key spacecraft missions past, present, and planned (Voyager, Cassini, JWST, etc.)
- Recent advances: latest mission results (e.g., JWST, Mars Sample Return updates), new planetary discoveries, and emerging questions shaping the field

### Lecture 2: Planet Formation 101 & Orbital Dynamics

- Star formation and protoplanetary disks: observational evidence and structure
- Dust coagulation, pebble accretion, and planetesimal formation
- Runaway and oligarchic growth; giant planet core accretion vs. gravitational instability
- Kepler's laws and orbital elements
- Two-body problem, reduced mass, and vis-viva equation
- **Blackboard derivation (~10 min):** Derive the vis-viva equation from energy conservation in a Keplerian orbit (total energy = kinetic + gravitational potential, relate to semi-major axis)
- Orbital resonances: mean-motion resonances, Laplace resonance of the Galilean moons
- Tidal forces and tidal locking; Roche limit
- Planetary migration: types I, II, III and the Nice model
- Recent advances: ALMA disk substructure observations, pebble accretion refinements, new constraints on giant planet formation timescales

### Lecture 3: Planetary Heat & Energy Transport

- Energy sources: accretional heating, gravitational differentiation, radioactive decay, tidal heating
- Heat transport mechanisms: conduction, convection, radiation
- **Blackboard derivation (~10 min):** Derive the conductive cooling timescale τ ∼ L²/κ from the heat diffusion equation, and apply it to estimate cooling times for bodies of different sizes (asteroid vs. Moon vs. Earth)
- Thermal evolution of terrestrial planets: cooling models and parameterized convection
- Rayleigh number, Nusselt number, and convective vigor
- Thermal boundary layers and mantle convection basics
- Surface heat flow: Earth as calibration, comparison to Moon and Mars
- Tidal dissipation: Io as an extreme case, implications for icy moons
- Recent advances: InSight seismology results on Mars's interior heat flow, new tidal heating models for icy moons, updated radiogenic heating budgets

### Lecture 4: Chemical Differentiation & Magnetospheres

- Accretion and early melting: magma oceans and metal–silicate separation
- Core formation: siderophile element partitioning, Hf–W chronometry
- Mantle differentiation: major-element geochemistry, mantle reservoirs
- Volatile delivery and retention: role of impacts and outgassing
- Planetary magnetic fields: dynamo theory fundamentals
- Requirements for dynamo action: convecting, electrically conducting fluid
- **Blackboard derivation (~10 min):** Derive the magnetic Reynolds number Rm = UL/η from the induction equation, and estimate Rm for Earth's core to show that advection dominates over diffusion (dynamo feasibility criterion)
- Earth's geodynamo: structure, secular variation, reversals
- Comparative magnetospheres: Mercury (weak), Mars (remnant crustal), Jupiter (strong), Ganymede
- Magnetosphere–solar wind interaction: bow shock, magnetopause, magnetotail
- Auroral processes and radiation belts
- Recent advances: Juno magnetometer data on Jupiter's dynamo, BepiColombo measurements of Mercury's magnetosphere, Ganymede's magnetic environment from JUICE

### Lecture 5: Atmospheres I — Composition, Structure, & Dynamics

- Atmospheric composition: primary, secondary, and tertiary atmospheres
- Hydrostatic equilibrium and pressure–temperature profiles
- **Blackboard derivation (~10 min):** Derive the atmospheric scale height H = kT/mg from hydrostatic equilibrium (dP/dz = −ρg) combined with the ideal gas law, and compute H for Earth, Mars, and Venus
- Vertical structure: troposphere, stratosphere, mesosphere, thermosphere
- Radiative transfer basics: optical depth, absorption, emission
- Greenhouse effect: radiative–convective equilibrium
- Energy balance: albedo, effective temperature vs. surface temperature
- Atmospheric escape: Jeans escape, hydrodynamic escape, sputtering, photochemical escape
- Atmospheric retention: the role of gravity and temperature
- Recent advances: JWST detections of exoplanet atmospheres, revised atmospheric escape models, new constraints on early Earth and Mars atmospheric composition

### Lecture 6: Atmospheres II — Clouds, Weather, & Climate

- Cloud formation: condensation, nucleation, and cloud types across the solar system
- Venus: runaway greenhouse, sulfuric acid clouds, super-rotation
- **Blackboard derivation (~10 min):** Derive the Clausius-Clapeyron equation from thermodynamic phase equilibrium — starting from equal Gibbs free energies on the coexistence curve, obtain P_sat(T) = P_ref exp[−L_v/R_v(1/T − 1/T_ref)], and apply to predict cloud condensation across the solar system
- Mars: thin CO₂ atmosphere, dust storms, seasonal CO₂ cycle
- Titan: methane hydrological cycle, organic haze
- Giant planet atmospheres: banded structure, zones and belts, composition
- Atmospheric dynamics: Hadley cells, Coriolis effect, geostrophic balance
- Jet streams and vortices: Jupiter's Great Red Spot, Saturn's hexagon
- Climate evolution: faint young Sun problem, long-term climate feedbacks
- Carbonate–silicate cycle and climate regulation on Earth
- Recent advances: Venus atmospheric anomalies debate, Titan's methane cycle from Dragonfly mission planning, updated climate models for early Mars

### Lecture 7: Planetary Surfaces — Geology, Geomorphology, & Geophysics

- Surface processes: impact cratering, volcanism, tectonics, erosion
- Impact cratering: mechanics, morphology (simple, complex, basins), crater counting and surface ages
- **Blackboard derivation (~10 min):** Derive the crater scaling law — relate impactor kinetic energy ½mv² to crater diameter using dimensional analysis with (E, ρ, g) to obtain D ~ (E/ρg)^{1/4}, then estimate the crater size from a 1 km asteroid impact on the Moon
- Volcanism: effusive vs. explosive, volcanic landforms across the solar system
- Tectonics: plate tectonics on Earth, stagnant lid on other terrestrial bodies
- Erosion and weathering: aeolian, fluvial, glacial, chemical
- Remote sensing of surfaces: spectroscopy, radar, altimetry
- Regolith formation and space weathering
- Cryovolcanism on icy bodies: Enceladus, Triton, Europa
- Recent advances: Perseverance rover surface analysis on Mars, DART mission impact results, new remote sensing of volcanic activity on Io and Venus

### Lecture 8: Planetary Interiors — Structure, Composition, & Dynamics

- Probing interiors: seismology, gravity field, moment of inertia
- **Blackboard derivation (~10 min):** Derive the moment of inertia factor C/MR² for a uniform sphere vs. a differentiated two-layer body (dense core + lighter mantle), and show how the measured value constrains core size
- Equations of state: relating pressure, density, and temperature at depth
- Earth's interior: crust, mantle, outer core, inner core
- Mantle rheology: viscous flow, mantle convection patterns
- Phase transitions: olivine–spinel–perovskite, post-perovskite
- Comparative interiors: Moon (small core), Mars (large core fraction), Mercury (large iron core)
- Giant planet interiors: metallic hydrogen, layered vs. dilute cores
- Ice giant interiors: water, ammonia, methane ices under extreme pressures
- Icy moon interiors: subsurface oceans (Europa, Enceladus, Titan)
- Recent advances: InSight seismology revealing Mars's core and mantle structure, revised models of Jupiter's dilute core from Juno gravity data, new constraints on Europa's ice shell thickness

### Lecture 9: Rocky Planets — Earth & Venus

**Structure**: descriptive-first (Earth then Venus) with a comparative payoff at the end.

**Part 1 — Earth as reference (~25 min)**

- Earth's bulk properties: $T_s = 288$ K, $P_s = 1$ bar, $\mathrm{N_2/O_2}$ atmosphere; the three-way coupling of plate tectonics, biosphere, and liquid water
- Plate tectonics recap from Lecture 7; subduction as the return leg of the mantle-cooling loop; volcanism–weathering–climate link
- Earth's magnetic field recap from Lecture 4: shielding of the atmosphere, forward reference to Mars in Lecture 10
- Hydrosphere and cryosphere: ocean mass and thermohaline circulation (scoped to one slide); ice-albedo feedback recap; ocean chemistry and carbonate buffering
- Earth's climate system: scoped tight, only to the extent needed to motivate Venus (Lectures 5–6 already cover the mechanisms). Faint young Sun problem recap; Milankovitch cycles
- **What "Earth's climate has been extraordinarily stable" does and does not mean**: liquid-water bounds over 4 Gyr, but temperature swings of >10 K in the past; past swings paced by orbital/volcanic/tectonic drivers on $10^4$–$10^6$ yr timescales; anthropogenic warming is a different mechanism that bypasses the silicate-weathering feedback
- Snowball Earth episodes: Sturtian (~720 Ma), Marinoan (~635 Ma), possibly Huronian (~2.4 Ga); ice-albedo runaway once ice reaches ~30° latitude; escape via volcanic CO₂ accumulation under the ice; correlation with the rise of complex life; relevance for the Venus comparison (Earth's alternative failure mode)
- **Anthropogenic climate change as a physical phenomenon**: greenhouse effect recap from Lecture 5 applied to present-day Earth; CO₂ from 280 ppm (pre-industrial) to >420 ppm (2024); rate ~100× faster than natural deglaciation; forcing ~2 W/m² and observed ~1.2 K warming since 1880; why the carbonate-silicate thermostat cannot save us on human timescales (0.5 Myr equilibrium); ocean acidification. Physical, not political — the science is well understood
- Biosphere's geological footprint: Great Oxidation Event (~2.4 Ga), carbonate platforms as biotic CO₂ sink; biosignature framing for Lectures 13–14

**Part 2 — Venus as the alien twin (~30 min)**

- Venus overview: 0.815 $M_\oplus$, 0.950 $R_\oplus$, similar bulk composition, but $P_s = 92$ bar, $T_s = 735$ K, CO₂-dominated, 243-day retrograde rotation, no detectable global field, desiccated
- Mission history: Mariner 2 (1962), Venera series (1967–1982 — landers, surface images, soil chemistry), Pioneer Venus (1978), Magellan (1990–94 SAR mapping), Venus Express (2006–2014), Akatsuki (2015–present)
- Surface morphology: unimodal topography (vs Earth's bimodal); volcanic plains (~80%); tesserae as candidate ancient crustal blocks; coronae as unique volcano-tectonic features; global resurfacing age ~300–700 Ma; catastrophic vs steady-state resurfacing debate
- Venus interior and tectonic regime: similar core/mantle to Earth, but stagnant-lid today; no plate boundaries; no global field; candidate explanations (absence of inner core, stagnant-lid insulation, slow rotation) — connects to Lecture 4 debate; no seismic data yet
- Venus atmosphere: 96.5% CO₂, sulfuric acid cloud decks (48–70 km), super-rotation (4-day cloud tops vs 243-day surface), unknown UV absorber
- Runaway greenhouse on Venus: mechanism recap from Lectures 5–6; consequence for present-day water inventory (~20 ppm)
- **Blackboard derivation (~10 min):** Derive the Simpson–Nakajima runaway greenhouse threshold — show that outgoing longwave radiation reaches a maximum in a moist atmosphere set by the water-vapour saturation profile; numerically ~280–350 W/m²; critical solar flux reached at ~0.95 AU; Venus at 0.72 AU receives ~1.9× Earth's flux, well beyond the limit
- **When did Venus lose its water?** Two competing scenarios, unresolved:
  1. **Early loss during the magma-ocean / initial runaway** (Hamano et al. 2013, Nature): magma ocean never solidified under an optically thick steam atmosphere; H photolysed and escaped under young-Sun EUV; Venus never had liquid surface water
  2. **Later loss after a temperate early phase**: Venus had liquid oceans for ~0.5–2 Gyr; runaway was triggered as solar luminosity rose (e.g., Way et al. 2016)
  Both scenarios match present-day observations (dry CO₂ atmosphere + enriched D/H); future DAVINCI noble-gas data should help discriminate
- D/H ratio: ~150× Earth's value; implies at least a shallow global ocean equivalent; direct observational evidence of hydrodynamic hydrogen escape
- Volcanic activity today: long debate resolved in part by Herrick & Hensley (2023) who identified morphological changes at Maat Mons in archival Magellan data; thermal anomalies at Shalbatana and Idunn Mons; SO₂ variability in the upper atmosphere

**Part 3 — Comparative payoff (~15 min)**

- Why did Earth and Venus diverge? Same bulk composition, similar size, same formation region. Four switches that flipped differently: solar flux (0.72 vs 1 AU), water loss history, rotation rate, tectonic regime
- Failure mode of the carbonate-silicate cycle on Venus: once the ocean evaporates, the CO₂ sink disappears but the volcanic source continues; no thermodynamic path back
- Implications for habitability: the habitable zone is not a line but a set of history-dependent trajectories; forward reference to Lecture 13 exoplanet habitability
- Recent advances and upcoming missions: DAVINCI+ (NASA, ~2029), VERITAS (NASA, late 2020s), EnVision (ESA, 2031); first new orbital missions in decades; active research on early Venus climate (Way 2016, Turbet 2021); phosphine debate (Lecture 6)

### Lecture 10: Rocky Planets — Mercury & Mars

**Structure**: descriptive-first (Mercury then Mars) with comparative payoff at the end.

**Part 1 — Mercury, the metal world (~25 min)**

- Overview: mass 0.055 $M_\oplus$, radius 0.383 $R_\oplus$, highest uncompressed density; orbit 0.39 AU, $e = 0.206$ (most eccentric planet); preview of the "why so dense?" problem (giant impact vs evaporation)
- Spin–orbit resonance: 88-day orbit, 59-day rotation, 3:2 resonance driven by tidal evolution with permanent quadrupole (Correia & Laskar 2004); solar day of ~176 Earth days; fixed "hot poles" and "warm poles"
- Interior: core mass fraction ~70% (unique in the solar system); liquid outer + solid inner core (MESSENGER libration); thin mantle ~400 km; $C/MR^2 \approx 0.346$; weak active dynamo with ~480 km northward offset
- Surface morphology: lunar-like cratered terrain, smooth volcanic plains (~3.7–3.9 Ga), lobate scarps (~1–3 km thrust faults recording ~7 km radial contraction), hollows (MESSENGER discovery, Blewett 2011), Caloris Basin and antipodal chaotic terrain
- **Polar volatiles (dedicated slide)**: water ice in permanently shadowed craters; Arecibo radar-bright detection (1991), MESSENGER neutron and imaging confirmation; cold traps maintained by Mercury's 2° obliquity; hottest planet hosts ~100 K surfaces
- Exosphere and magnetosphere: collisionless Na/K/Ca/Mg/H/He exosphere; sodium tail millions of km long; compact magnetosphere ($r_\mathrm{mp} \sim 1.5 R_\mathrm{Mercury}$); reconnection rate ~10× Earth's
- Mission history: Mariner 10 (1974–75), MESSENGER (2011–2015), BepiColombo (ESA/JAXA flybys 2021–2024, orbit insertion 2026; MPO + MMO orbiters); open questions for BepiColombo on core composition, polar ice inventory, magnetosphere variability

**Part 2 — Mars, the watery past (~30 min)**

- Overview: mass 0.107 $M_\oplus$, radius 0.532 $R_\oplus$, mean density 3.93 g/cm³ (lowest rocky planet); orbit 1.52 AU, obliquity 25°; 6 mbar CO₂ atmosphere, $T \approx 210$ K
- **Phobos and Deimos (dedicated slide)**: small irregular moons, C-type spectra, low density → high porosity; Phobos orbital decay will destroy it in 30–50 Myr; origin debate (captured asteroids vs giant-impact debris); **JAXA MMX mission** (launch 2026, return 2031) will land on Phobos and return $\geq$10 g regolith, definitively settling the origin
- Interior: core radius 1830 ± 40 km (~54% of $R$); liquid outer core (InSight S-wave shadow); light-element rich (S, O) explaining low density; no inner core → no dynamo today; crustal thickness 24–72 km; $C/MR^2 \approx 0.364$
- Geological epochs: Noachian (>3.7 Ga; valley networks, clay minerals, active dynamo), Hesperian (~3.7–3.0 Ga; outflow channels, volcanism, sulfates), Amazonian (3.0 Ga–present; cold, dry, sporadic volcanism); mineral sequence phyllosilicates → sulfates → ferric oxides (Bibring 2006)
- Surface highlights: hemispheric dichotomy (~6 km), Olympus Mons (21.9 km tall, 600 km diameter; long-lived stationary plume), Tharsis Bulge, Valles Marineris (4000 km rift), Hellas Basin, polar caps (seasonal CO₂ + permanent H₂O ice)
- Evidence for past water: valley networks, outflow channels, phyllosilicates (OMEGA, CRISM), sulfates (Opportunity, Curiosity), deltas and lakebeds (Jezero, Gale, Eberswalde), jökulhlaup-style outburst features
- Early Mars climate puzzle: faint young Sun vs evidence for sustained liquid water; pure CO₂ insufficient; candidates include reducing H₂/CH₄ greenhouse, H₂-CO₂ CIA (Wordsworth 2017, 2021), impact- or volcanism-driven episodic warming
- Mars today: thin CO₂ atmosphere, global dust storms (2007, 2018), seasonal CO₂ cycle (~25% of atmosphere), recurring slope lineae (likely dry granular flow), **methane variability** (Curiosity detections ~0.5 ppb background + transient spikes vs ExoMars TGO upper limits; interpretation unresolved; ambiguity is the honest state)
- **Blackboard derivation (~10 min):** Derive the Jeans escape flux — starting from the Maxwell–Boltzmann velocity distribution, integrate above the escape velocity to obtain $\lambda = GMm/(k_B T r)$ and the Jeans flux $\Phi_J = n\,(k_B T/2\pi m)^{1/2}(1+\lambda)e^{-\lambda}$; apply to Mars with $T_\mathrm{exo} \sim 270$ K: H₂ ($\lambda \approx 6$) escapes, CO₂ ($\lambda \approx 130$) does not; conclude that non-thermal processes (solar wind pickup, photochemical) dominate CO₂ loss
- MAVEN escape constraints: present-day total ~1–2 kg/s, dominated by photochemical O escape; solar-storm enhancement ~10×; integrated over 4 Gyr consistent with loss of ~0.5–0.8 bar CO₂ and ~15–25 m water-equivalent layer
- **Exploration history (two slides):** 
  1. Mariner 4 (1965), Viking 1 & 2 (1976), Pathfinder + Sojourner (1997), Mars Global Surveyor, Mars Odyssey, Mars Express, MRO, Spirit & Opportunity (2004–2018)
  2. Curiosity (2012–), InSight (2018–2022), Perseverance + Ingenuity (2021–), Tianwen-1 + Zhurong (2021–), UAE Hope (2021–), ExoMars Trace Gas Orbiter (2016–)
- Mars habitability: Noachian conditions analogous to early Earth (hydrothermal systems, mineral diversity, organics); subsurface habitability possible today; subglacial lake debate (Orosei 2018 vs conductive-clay alternative)
- **Mars Sample Return**: Perseverance caching in Jezero; **2024 re-baselining announced major cost and schedule overrun**; architecture under review with NASA study teams; return date uncertain but likely early-to-mid 2030s; scientific imperative remains

**Part 3 — Comparative payoff (~15 min)**

- Mercury vs Mars as limiting cases: Mercury is too small + too close; Mars is medium-sized + too far. Both bracket Earth in the size–distance phase space
- Size and distance set the trajectory: interior cooling rate ($L^2/\kappa$) and gravitational retention ($\lambda$) are the two fundamental controls; many other properties are consequences
- The timing problem: Mercury's dynamo persists despite its small size; Mars' dynamo died early (4.1–3.9 Ga, Mittelholz 2020); Earth's dynamo still active via inner core crystallisation; Venus' dynamo shutdown time unknown
- What makes a rocky planet habitable? (synthesised from L9 + L10) (1) liquid water, (2) active geology for volatile recycling, (3) magnetic shielding (debated), (4) long-term climate stability. Earth ticks all four; Venus and Mars failed on at least two; Mercury never had a chance
- Recent advances and upcoming missions: Mars Sample Return (NASA/ESA, schedule in flux), BepiColombo (2026 orbit insertion), ExoMars Rosalind Franklin (~2028), JAXA MMX (2026 launch, 2031 return), Curiosity long-baseline results, subsurface radar reservoirs (contested), Ingenuity helicopter legacy, Perseverance ongoing geochemistry

### Lecture 11: Gas & Ice Giants — Jupiter, Saturn, Uranus, Neptune

**Structure**: descriptive-first (gas giants, then ice giants) with comparative payoff and exploration frontier in Part 3. Moons are integrated into planet narratives rather than given a separate section.

**Part 1 — The gas giants, Jupiter & Saturn (~35 min)**

- Gas giant overview: composition dominated by H₂/He, no solid surface, rapid rotation (~10 hr) driving Coriolis-dominated circulation, both emit more energy than they receive
- Jupiter interior: molecular H₂/He envelope, metallic H transition at ~100 GPa, dilute core extending to 30–50% of radius (Wahl 2017, Militzer 2022); central ~4000 GPa, ~20,000 K
- Jupiter atmosphere and weather: zone/belt structure, ~15 alternating zonal jets (up to 180 m/s), Great Red Spot (>350 yr, shrinking), Great Blue Spot magnetic anomaly, Io-powered aurorae
- **Dedicated slides for Io, Europa, Ganymede, Callisto** — four Galilean moons spanning volcanic (Io tidal heat ~10¹⁴ W), ocean world (Europa ice shell + ~100 km ocean), intrinsic dynamo (Ganymede), and undifferentiated ancient (Callisto outside Laplace resonance, least interesting geologically but lowest radiation environment)
- Jupiter's rings and small moons: faint dusty system from micrometeorite gardening of Amalthea/Metis/Adrastea/Thebe
- Saturn interior and rotation: helium rain at 1–3 Mbar provides excess luminosity (~2× absorbed flux); dilute core likely; rotation period uncertain (~10.7 hr from Cassini ring seismology); dipole almost perfectly axially aligned (challenge for dynamo theory)
- Saturn atmosphere and weather: equatorial jet ~400 m/s, hexagonal polar jet (Rossby wave), Great White Storms every ~30 years
- Saturn's rings — structure and composition: A–G rings, >95% water ice, Cassini Division from Mimas 2:1 resonance, total mass ~Mimas-scale, ring–moon interactions
- Saturn's rings — age and evolution: young-rings consensus (Iess 2019, Crida 2019) ~100 Myr based on Cassini grand-finale mass; ongoing ring-rain losses imply ~100 Myr lifetime; debate continues (Wisdom 2022); pedagogical lesson that solar system bodies evolve on sub-Gyr timescales
- **Blackboard derivation (~10 min):** Derive the Roche limit — equate the tidal force from the planet on a satellite element with the satellite's self-gravity to obtain $d_\mathrm{R} \approx 2.46\,R_p\,(\rho_p/\rho_s)^{1/3}$; apply to Saturn's rings ($d_\mathrm{R} \approx 126{,}000$ km matching the A ring outer edge)
- **Dedicated slides for Titan** (N₂ atmosphere + methane cycle + subsurface water-ammonia ocean; Dragonfly mission 2028/2034) **and Enceladus** (tiger stripes, plumes, silica nanoparticles, phosphate detection, global ocean + hydrothermal activity)
- Other Saturnian moons (one slide): Iapetus two-faced hemispheres, Mimas Herschel crater, Hyperion chaotic rotation, Phoebe captured KBO, Dione/Rhea/Tethys mid-sized icy moons

**Part 2 — The ice giants, Uranus & Neptune (~25 min)**

- Ice giant overview: composition ≲20% H₂/He envelope, bulk dominated by "ices" (H₂O, NH₃, CH₄); only visited once each by Voyager 2 (1986, 1989); most under-explored planets
- Uranus: 98° axial tilt (giant-impact origin, Morbidelli 2012), 42-year polar seasons, muted atmosphere becoming more active near equinox, anomalously low internal heat flow (~10% of Neptune's)
- Neptune: fastest winds in the solar system (~580 m/s despite weakest solar input), Great Dark Spot (transient, unlike Jupiter's GRS), internal heat ~2.6× absorbed flux
- Ice giant interiors: layered rocky core + ice mantle + H₂/He atmosphere; **superionic ice** layer at >100 GPa >2000 K (Millot 2019) supports dynamo generation; multipolar fields tilted 59° (Uranus) and 47° (Neptune) from rotation, offset from centre
- **Dedicated slide for Triton**: captured Kuiper Belt object (retrograde high-inclination orbit), young surface, active nitrogen cryovolcanism, thin N₂ atmosphere (14 μbar), orbital decay → collision/disruption in 3.6 Gyr, proxy for KBO science (Lecture 12)
- Ice giant rings: Uranus 13 narrow rings (stellar occultation 1977), Neptune 5 ring arcs (Voyager 1989), both dark carbon-rich material; JWST high-resolution imaging 2023

**Part 3 — Comparative payoff and exploration frontier (~15 min)**

- Why gas and ice giants diverged: core-accretion timing, disk mass, migration history (Nice model recap); ice giants are a natural intermediate outcome
- Common themes: internal heat excesses (except Uranus), zonal jets faster with distance, electrically conducting fluid dynamos, diverse moon and ring systems, exoplanet-analogue laboratories
- What we still don't know: ice/rock/gas fractions in ice giants, Neptune heat source, Uranus heat deficit, Saturn ring age detail, Jupiter dilute core origin, Callisto ocean, Saturn hexagon persistence
- Ongoing missions: Juno extended (2025+, Io/Europa/Amalthea flybys), Cassini legacy analysis, JWST Uranus/Neptune observations
- **Dedicated slide: JUICE vs Europa Clipper** — two ocean world missions launching within 18 months of each other (Clipper Oct 2024 → 2030; JUICE April 2023 → 2031 → Ganymede orbit 2034); complementary depth vs breadth targets; simultaneous Jovian system operations in the 2030s
- Dragonfly to Titan: 2028 launch, 2034 arrival, rotorcraft, prebiotic chemistry + impact-heated transient liquid water at Selk crater
- **Dedicated slide: Voyager legacy** — only spacecraft to visit Uranus and Neptune; still operational in the interstellar medium; power declining toward ~2030 end of life; our ice giant knowledge is 40 years out of date
- Future ice giant missions: 2023 US Decadal Survey prioritised a Uranus orbiter as the top flagship mission for the 2030s; mission concepts in study phase; launch window early 2030s; atmospheric entry probe + magnetosphere + moon reconnaissance

### Lecture 12: Meteorites, Asteroids, Minor Planets & Comets

Lecture follows the same descriptive-first, payoff-at-the-end structure as L9–L11: meteorites (Part 1), then populations and dynamics (Part 2), then messengers and visitors (Part 3). Pluto is covered here as a Kuiper Belt / dwarf planet, not in L11.

**Part 1: Meteorites — samples of the early solar system**

- Why meteorites matter: oldest rocks available for lab analysis, absolute ages, ~70,000 classified falls
- Meteorite classification: chondrites (ordinary, carbonaceous, enstatite) vs achondrites vs irons; oxygen isotope fingerprinting
- Chondrites: OC (H/L/LL), CC (CI/CM/CV/CO/CR/CK/CH/CB), EC (EH/EL); CI chondrites match solar photosphere
- Chondrules and CAIs: CAIs are oldest solar system solids (4.567 Gyr), chondrules form 2–4 Myr later
- Isotopic dating: long-lived (Pb–Pb, Rb–Sr, Sm–Nd) vs extinct (²⁶Al, ⁵³Mn, ¹⁸²Hf, ¹²⁹I, ²⁴⁴Pu) chronometers
- **Blackboard derivation (~10 min):** Pb–Pb isochron dating. Start from N(t) = N₀ e^{−λt}, use the double U→Pb decay system, derive the isochron equation, apply to CAIs for the 4567.30 ± 0.16 Myr age (Connelly et al. 2012). Key insight: self-calibrating via parallel ²³⁵U and ²³⁸U decay
- Petrographic types (1–7), shock stages (S1–S6), differentiated meteorites (irons, pallasites, HEDs from Vesta), Martian (SNC) and lunar meteorites
- **The NC–CC isotopic dichotomy — three competing interpretations:**
  1. **Jupiter as early physical barrier (Kruijer et al. 2017):** Hf–W chronology + isotope data; Jupiter core to ~20 M⊕ by ~1 Myr; gravitationally blocks pebble drift
  2. **Snow-line migration + pebble isolation (Lichtenberg et al. 2021, Science):** bifurcation without Jupiter as a physical dam; relaxes Jupiter formation timescale
  3. **Temporal / age dichotomy (Bizzarro, Connelly, Johansen):** NC and CC are formation epochs, not spatial reservoirs; CC planetesimals systematically younger
- Meta-note: what all three agree on (early structural/temporal order) vs what they disagree on (spatial vs dynamical vs temporal cause); actively debated as of 2024–2025

**Part 2: Small body populations and dynamics**

- Asteroid belt: ~1.2 million known, total mass ~4×10⁻⁴ M⊕, dominated by Ceres (~30%)
- Kirkwood gaps as dynamical sinks at mean-motion resonances with Jupiter (2:1, 3:1, 5:2)
- Collisional families (Eos, Koronis, Themis, Vesta)
- Spectral taxonomy: C-type, S-type, M-type, V, D, P/K; heliocentric compositional gradient mirrors disk
- Near-Earth asteroids: ~35,000 known; Yarkovsky delivery from resonances; impact frequency scaling; DART demonstrated kinetic deflection 2022; LSST/Rubin to increase discovery rate ~10×
- Ceres and the Dawn mission: hydrated surface, salt deposits, possible subsurface brines; possibly a displaced outer-solar-system body
- Kuiper Belt structure: classical (cold/hot), resonant (plutinos at 3:2, twotinos at 2:1), scattered disk, detached objects; fossil record of Neptune migration
- Pluto and Charon: New Horizons 2015 revelations (Sputnik Planitia convection, water-ice mountains, thin N₂ atmosphere, possible subsurface ocean); Arrokoth flyby 2019 as pristine cold classical KBO
- Other dwarf planets: Eris, Haumea (ring + family), Makemake, Sedna, Gonggong, Quaoar, Orcus, Salacia
- Oort cloud: theoretical reservoir at 2000–50,000 AU, never directly observed, inferred from long-period comet statistics, ~10¹¹–10¹² objects
- Comets: "dirty snowballs", nucleus 1–30 km, coma, ion tail (anti-sunward), dust tail (curved); two tails as diagnostic
- Short-period comets (JFCs from scattered disk) vs long-period comets (from Oort cloud); Halley as intermediate case
- The D/H debate: 67P vs Hartley 2 span factor of ~3 in D/H; Earth's oceans consistent with mix of CC + comet sources; comets alone cannot explain Earth's water

**Part 3: Messengers and visitors**

- Rosetta at 67P/Churyumov–Gerasimenko: first orbit + lander (Philae), bilobed nucleus as contact binary, D/H ~3× Earth's, glycine and organic molecules, ~75% porosity
- Sample-return missions: Hayabusa (Itokawa S-type, tiny sample), Hayabusa2 (Ryugu C-type, 5.4 g, organics + amino acids), OSIRIS-REx (Bennu B-type, ~70 g, hydrated clays + prebiotic organics); lab-quality data far beyond in-situ spectroscopy
- DART at Dimorphos + Hera follow-up (launched October 2024, arrival 2026)
- Lucy to Jupiter Trojans (launched 2021, 8 Trojans 2027–2033, Dinkinesh flyby 2023 revealed satellite moonlet)
- Psyche (launched October 2023, arrival 2029): test of exposed-core hypothesis for M-type asteroid
- Interstellar visitors: 1I/'Oumuamua (2017, elongated, non-grav acceleration unexplained), 2I/Borisov (2019, clearly cometary), 3I/ATLAS (2025, under characterisation)
- LSST/Rubin expected to find ~1 ISO/year; ESA Comet Interceptor (launch 2029) waiting at L2 for pristine long-period comet or ISO

**Part 3 (comparative payoff) / Summary**

- Small bodies = formation fossils; inner (rocky) vs outer (icy) split mirrors disk temperature structure (L2)
- Orbital architecture records giant planet migration history (Nice model, Grand Tack; L2)
- Pb–Pb age of CAIs at 4567.30 ± 0.16 Myr is the most precise number in planetary science
- Three-way NC–CC debate illustrates how the same data can support different physical pictures
- Recent mission bonanza (OSIRIS-REx, Hayabusa2, DART, Lucy, Psyche, Rosetta) + upcoming (Hera, Comet Interceptor, LSST) are transforming the field
- Interstellar visitors connect solar system science directly to exoplanets (forward to L13/L14)

### Lecture 13: Exoplanets, Detection Methods, Demographics & Characterisation

Lecture follows the same descriptive-first, payoff-at-the-end structure as L9–L12: detection methods (Part 1), then demographics and architectures (Part 2), then characterisation, habitability, and the comparative payoff (Part 3).

**Part 1: How we find exoplanets**

- Historical context: 1992 pulsar planets (Wolszczan & Frail, PSR B1257+12), 1995 51 Peg b (Mayor & Queloz, Nobel 2019), the "hot Jupiter surprise" that launched the migration revolution
- Current count: >6000 confirmed exoplanets as of 2025
- Radial velocity: Doppler wobble, K scaling, m sin i degeneracy, HARPS → ESPRESSO to ~10 cm/s, stellar-noise floor
- Transit: depth δ = (Rp/R★)², geometric probability ≈ R★/a, limb darkening; CoRoT → Kepler → K2 → TESS → CHEOPS → PLATO
- **Blackboard derivation (~10 min):** transit depth geometry (~2 min) + RV semi-amplitude K from momentum conservation (~5 min) + combine to get mass, radius, and bulk density, breaking the m sin i degeneracy (~3 min)
- Direct imaging: contrast ratios, coronagraphs + AO, ADI/SDI; SPHERE/GPI/SCExAO on the ground, JWST NIRCam/MIRI in space; HR 8799, β Pic b/c, PDS 70 b/c, first JWST-imaged atmospheres 2023
- **Astrometry gets its own slide**: Gaia at 20–50 μas, DR3 first candidates 2022, DR4 (~2026) expected to deliver 10²–10³ confirmed astrometric exoplanets, DR5 pushing into sub-Jovian regime; breaks m sin i degeneracy; sweet spot = wide-orbit Jupiter analogues
- Microlensing: OGLE/MOA/KMTNet now, Roman 2027 expected to find ~1000–3000 planets + free-floating rogues
- Timing methods: TTVs (dynamical masses for small planets, Kepler-11/36, TRAPPIST-1), pulsar timing, eclipse timing in binaries (Kepler-16 b)
- Detection-bias summary slide: (mass, period) coverage per method; the shape of the exoplanet archive reflects biases as much as underlying distribution

**Part 2: Demographics and architectures**

- Kepler revolution: ~150,000-star statistically complete sample; ≥1 planet per star on average; η⊕ estimates 0.1–0.6
- Period–radius diagram: hot Jupiters, warm/cold Jupiters, sub-Neptunes, super-Earths, terrestrial analogues
- **Radius valley / Fulton gap** at ~1.8 R⊕: photoevaporation (Owen & Wu 2013) vs core-powered mass loss (Ginzburg et al. 2018) interpretations
- Hot Neptune desert + its well-defined edge (Mazeh et al. 2016)
- Peas in a pod (Weiss et al. 2018): similar sizes, uniform spacing in multi-planet systems → smooth local formation
- Compact resonant chains: TRAPPIST-1 (7 planets), Kepler-90 (8), TOI-178 (6-resonance)
- Hot Jupiter migration: disk (Type II), high-eccentricity (Kozai-Lidov + tides), planet-planet scattering; Rossiter-McLaughlin obliquities + companion multiplicity as discriminants
- Super-Earth / sub-Neptune composition: bare rocky cores vs water worlds vs gas dwarfs; K2-18 b hycean hypothesis (contested)
- M dwarf planets: ~75% of all stars, high transit probability, high occurrence rates, but XUV flares and long pre-MS threaten early atmospheres; TRAPPIST-1 as reference lab

**Part 3: Characterisation, habitability, and comparative payoff**

- Transmission spectroscopy: δ(λ) scale-height arguments, cloud suppression, detectable species
- Emission spectroscopy + phase curves: dayside flux, day-night redistribution, thick vs thin atmospheres
- **JWST era results 2022–2025:**
  - WASP-39 b (ERS): SO₂ photochemistry (Tsai et al. 2023), first disequilibrium chemistry detection
  - HD 189733 b H₂S; WASP-107 b methane depletion + vertical mixing
  - K2-18 b CH₄/CO₂ + tentative DMS claim (Madhusudhan et al. 2023) and the community pushback (Glein 2024, Wogan et al. 2024) as the case study in how biosignature claims are tested
  - TRAPPIST-1 b, c MIRI thermal emission → bare rock, rules out thick CO₂ atmospheres (Greene et al. 2023, Zieba et al. 2023)
  - LHS 475 b, GJ 486 b, GJ 1132 b: rocky-planet atmosphere non-detections → M dwarf XUV stripping consistent
  - **55 Cancri e** (Hu et al. 2024): MIRI thermal emission + phase curve; tentative CO/CO₂-rich atmosphere on a super-Earth lava world
  - **TOI-561 b**: ultra-short-period rocky planet, metal-poor thick-disk host, tentative thin-atmosphere signal
  - Direct imaging spectra: HIP 65426 b, VHS 1256 b (Miles et al. 2023)
- Habitable zone revisited: 1D (Kasting, Kopparapu) vs 3D (Way, Wordsworth, Turbet) boundaries; inner edge = Simpson-Nakajima runaway (recap L9), outer edge = max CO₂ greenhouse; M dwarf tidal locking + pre-MS history matters
- Biosignature gases: O₂, O₃, CH₄, N₂O, disequilibrium combinations; false positives (H₂O photolysis, CO₂ photolysis, abiotic volcanic CH₄); DMS not-known-on-Earth ≠ impossible elsewhere
- **Solar system in the exoplanet landscape:**
  - Most planets: sub-Neptunes around M dwarfs in compact peas-in-a-pod systems
  - Solar system skips the most common planet class, no hot giants, irregular inner-system spacing, wide low-e giants
  - Not obviously typical, but "rare vs undersampled" question depends on the next decade's long-period sensitivity floor
- **Frontier missions, two slides:**
  - Slide A (transits + atmospheres, 2026–2035): PLATO (ESA 2026, Earth analogues around G dwarfs), Ariel (ESA 2029, ~1000 atmospheres), Roman (NASA 2027, microlensing + coronagraph demo)
  - Slide B (direct imaging of Earth analogues, 2030s–2040s): HWO (NASA, ~6 m coronagraph, ~25 nearby sun-like stars), LIFE (ESA concept, mid-IR nulling interferometer), ELT/GMT/TMT (ground-based, first light 2028–2030s)
- Open-ended question: what combination of evidence would constitute convincing life detection? Forward reference to L14

### Lecture 14: Synthesis, Solar System in Context & Astrobiology

Capstone synthesis lecture. Unlike L9–L13, the structure is integration-first rather than object-first: solar system in exoplanet context (Part 1), habitability as a coupled systems property (Part 2), astrobiology and the search for life (Part 3), and a course wrap-up.

**Part 1: The solar system in the exoplanet context**

- Recap the course thread: physical processes shape planetary outcomes, and the same processes operate everywhere
- Solar system overlaid on the exoplanet period-radius diagram (dedicated slide)
- Where the solar system is typical (rocky inner / giant outer / icy outermost) vs atypical (no super-Earth or sub-Neptune, wide low-e giants, no hot giants, irregular spacing, no resonant chain)
- Formation theory successes (disk migration → hot Jupiters, pebble accretion → giant cores, NC–CC → reservoir separation, Nice + Grand Tack → architecture) vs open questions (radius valley mechanism, super-Earth vs sub-Neptune pathway, Jupiter timing, why no super-Earth here)
- "Is the solar system rare?" → unanswerable until Gaia DR4/DR5, PLATO, and longer RV baselines complete the long-period + small-planet survey

**Part 2: Habitability as a coupled systems property**

- Stack of necessary couplings: star, orbit, planet, atmosphere, interior, surface/tectonics, biosphere — each level necessary, not sufficient; coupling is what makes it a systems property
- **Dedicated habitability coupling diagram slide**: bidirectional arrows between star, orbit, interior, surface, atmosphere, biosphere; each arrow corresponds to a process from L1–L13
- HZ is not a line: Earth–Venus divergence (recap L9) + history-dependent exoplanet HZ (recap L13); trajectories matter more than snapshots
- Tectonic regime + carbonate–silicate thermostat (recap L6/L7/L9); plate vs stagnant lid; open question whether plate tectonics is the only viable long-term thermostat
- Magnetic field as gatekeeper (recap L4/L10); Mars case study; not strictly required but shifts the escape balance
- **Water delivery + planetary evolution** (revised framing per Lichtenberg in prep / inner-solar-system review): water inventory of inner SS bodies is set primarily by **internal evolution**, not by delivery budget alone. Mechanisms that matter:
  - Magma ocean partitioning between mantle and atmosphere
  - Atmospheric escape during the magma ocean phase (Hamano et al. 2013, recap L9)
  - Mantle–atmosphere exchange under plate tectonics
  - Tectonic regime: stagnant-lid worlds drift one-way
  - Stellar evolution (especially M dwarf pre-MS phase, recap L13)
- Earth, Venus, Mars likely received broadly similar volatile inventories; present differences reflect what each body did with them under different boundary conditions
- D/H from L12 is therefore a constraint on **delivery + processing combined**, not on delivery alone
- **Drake equation**: present the heuristic factorisation, then **be very critical** of its limitations:
  - Factors are not independent
  - Most factors are unconstrained by orders of magnitude
  - Treats a contingent non-equilibrium process as a steady-state pipeline
  - Implicit single-life-type / single-star-type assumption
  - Anthropic selection effects in our only data point
  - It is a framing tool, not an estimator
- **Fermi paradox**: presented as a question, not an answer; possible resolutions listed (rare-life, rare-intelligence, great filter ahead, detection threshold, zoo) without endorsement

**Blackboard derivation (~10 min):** Habitable zone boundaries from L★ = 4πd²F. Equilibrium temperature for fast-rotating planet, then inner edge from Simpson–Nakajima runaway greenhouse limit (recap L9) and outer edge from maximum CO₂ greenhouse. Solve for d_in and d_out; compare HZ for G, K, M dwarfs. Key insight: the HZ is a stellar-mass-dependent strip in orbital space; real habitability needs the boundary conditions the 1D HZ ignores.

**Part 3: Astrobiology and the search for life**

- What is life? Working definition (self-replicating, metabolising, evolving chemical system); operational definition is the one that lets us search; carbon + water as working baseline
- Extremophiles: thermophiles, psychrophiles, acidophiles, halophiles, radiation-resistant, desiccation-tolerant; classical HZ may be too restrictive
- **Origin of life on Earth** (kept in, presented honestly as unsolved): RNA world, metabolism-first / submarine vents, surface warm ponds, panspermia; earliest evidence ~3.5 Ga; honest framing that we do not know how, when, where, or how easily life originates
- Biosignatures: gases (O₂, O₃, CH₄, N₂O, DMS), disequilibrium combinations, surface "red edge", morphological + isotopic signatures, temporal variability
- False positives revisited (inverse-problem framing from L13)
- **Solar system targets for life detection:**
  - Mars: past habitability established, present uncertain; MSR re-baselining
  - Europa: Europa Clipper arrival 2030
  - Enceladus: Orbilander concept
  - Titan: Dragonfly arrival 2034
  - **Venus cloud layer + phosphine**: kept in, but **be sceptical as for K2-18 b DMS** — the data are at the edge of sensitivity, the molecular ID is contested, plausible abiotic explanations exist; pedagogical point identical to DMS
- Exoplanet life-detection strategy: single-snapshot atmospheric detection insufficient (K2-18 b lesson); needs multi-line, multi-target campaign; HWO + LIFE designed for this; earliest plausible robust detection in the 2040s

**Course wrap-up**

- Five biggest things learned: formation as physical process, interiors as heat engines, atmospheres as evolving systems, habitability as coupled, solar system as one example
- Five biggest open questions: origin of life, radius valley, Jupiter timing, Mars habitability history, solar system rare or typical
- Next decade timeline (now–2030, 2026–2030, 2030s, 2040s)
- Final framing: planetary science has become the science of comparative climate, interior, and life-hosting trajectories; the frontier is moving fast

---

## 3. Homework Sheets

All homework sheets are **ungraded formative practice**. Each contains 4–6 problems mixing analytical derivations, order-of-magnitude estimates, and conceptual questions. Some sheets include computational components (Python/Jupyter notebooks).

### Homework 1: Orbits & Formation
**Follows:** Lectures 1–2
**Due:** Week 2
**Topics covered:**
- Applying Kepler's laws: orbital periods, semi-major axes, eccentricities
- Vis-viva equation applications
- Tidal forces: Roche limit calculation for different bodies
- Orbital resonances: calculate resonance ratios for Galilean moons
- Order-of-magnitude estimate: disk mass required to form the solar system

**Format:** Problem set (analytical)

### Homework 2: Thermal Evolution & Differentiation
**Follows:** Lectures 3–4
**Due:** Week 3
**Topics covered:**
- Heat conduction: cooling timescales for bodies of different sizes
- Rayleigh number calculation and convective regime assessment
- Radioactive heating: calculate present-day vs. early solar system heat production
- Core formation: siderophile partitioning problem
- Magnetic Reynolds number and dynamo feasibility for different planets

**Format:** Problem set (analytical + one computational component: thermal evolution model)

### Homework 3: Atmospheres
**Follows:** Lectures 5–6
**Due:** Week 4
**Topics covered:**
- Hydrostatic equilibrium: derive and apply scale heights for different planets
- Radiative equilibrium: effective temperature vs. actual surface temperature
- Greenhouse effect: simple 1-layer and N-layer atmosphere models
- Atmospheric escape: Jeans escape rates for different species on Earth, Mars, Titan
- Cloud condensation: predict cloud layers in a giant planet atmosphere

**Format:** Problem set (analytical + one computational component: radiative balance model)

### Homework 4: Surfaces & Interiors
**Follows:** Lectures 7–8
**Due:** Week 5
**Topics covered:**
- Crater counting: derive surface ages from crater size–frequency distributions
- Impact energy: calculate energy released by impactors of different sizes and velocities
- Moment of inertia: constrain internal structure from C/MR² values
- Isostasy: crustal thickness variations and gravitational anomalies
- Interior pressure: estimate central pressure of a terrestrial planet

**Format:** Problem set (analytical)

### Homework 5: Terrestrial Planets
**Follows:** Lectures 9–10
**Due:** Week 6
**Topics covered:**
- Comparative climatology: Venus vs. Earth energy balance and greenhouse warming
- D/H ratio: estimate water loss from Venus
- Mars atmospheric pressure: relate to surface temperature and volatile inventory
- Spin–orbit resonance: derive Mercury's 3:2 resonance from tidal arguments
- Geological timelines: place key events on Mars and Earth in context

**Format:** Problem set (analytical + conceptual)

### Homework 6: Giant Planets & Small Bodies
**Follows:** Lectures 11–12
**Due:** Week 7
**Topics covered:**
- Giant planet structure: estimate metallic hydrogen transition pressure
- Ring dynamics: Roche limit, ring particle size distribution, shepherding moon forces
- Meteorite ages: isotopic dating problem using decay systems
- Kirkwood gaps: calculate resonance locations in the asteroid belt
- Comet activity: sublimation rates and gas production as a function of heliocentric distance

**Format:** Problem set (analytical + one computational component: N-body or orbital integration)

### Homework 7: Exoplanets & Synthesis
**Follows:** Lectures 13–14
**Due:** Week 8 (before final exam)
**Topics covered:**
- Radial velocity: derive minimum mass from stellar wobble data
- Transit depth: calculate planet radius from light curve
- Habitable zone: calculate inner and outer edges for stars of different spectral types
- Transmission spectroscopy: estimate atmospheric signal strength for different planet types
- Synthesis: compare solar system planet properties with exoplanet population statistics

**Format:** Problem set (analytical + one computational component: transit light curve fitting or HZ calculation)

---

## 4. Exam Structure

### Mid-term Exam

**Timing:** Week 4 (replaces one lecture slot, after Lecture 7)
**Weight:** 30%
**Duration:** 60 minutes
**Scope:** Lectures 1–7

**Coverage:**
- Planet formation and orbital dynamics (Lecture 2)
- Thermal processes and energy transport (Lecture 3)
- Chemical differentiation and magnetospheres (Lecture 4)
- Atmospheric structure, composition, and dynamics (Lectures 5–6)
- Surface processes and geology (Lecture 7)

**Format:**
- Part A: Short-answer questions (conceptual understanding, ~40%)
- Part B: Longer quantitative problems (derivations and calculations, ~60%)
- Closed book; equation sheet provided

### Final Exam

**Timing:** Week 8 (exam week)
**Weight:** 70%
**Duration:** 90 minutes
**Scope:** Cumulative (Lectures 1–14, emphasis on Lectures 8–14)

**Coverage:**
- All topics from the mid-term (broadly tested, ~30% of final)
- Planetary interiors (Lecture 8)
- Rocky planets: Earth, Venus, Mercury, Mars (Lectures 9–10)
- Gas and ice giants (Lecture 11)
- Small bodies: meteorites, asteroids, comets (Lecture 12)
- Exoplanets (Lecture 13)
- Synthesis and astrobiology (Lecture 14)

**Format:**
- Part A: Short-answer questions (conceptual understanding, ~30%)
- Part B: Longer quantitative problems (derivations and calculations, ~50%)
- Part C: Essay/synthesis question requiring integration across topics (~20%)
- Closed book; equation sheet provided

---

## 5. Development Roadmap

### Materials to Create

#### Lecture Notes (14 sets)

| # | Lecture | Status | Priority |
|---|--------|--------|----------|
| 1 | Introduction & history | Verified | High |
| 2 | Planet formation & orbital dynamics | Verified | High |
| 3 | Planetary heat & energy transport | Verified | High |
| 4 | Chemical differentiation & magnetospheres | Verified | High |
| 5 | Atmospheres I | Verified | High |
| 6 | Atmospheres II | Verified | High |
| 7 | Planetary surfaces | Verified | High |
| 8 | Planetary interiors | Verified | High |
| 9 | Rocky planets: Earth & Venus | Outline drafted | Medium |
| 10 | Rocky planets: Mercury & Mars | Outline drafted | Medium |
| 11 | Gas & ice giants | Draft + figures cleaned (8 arxiv scientific figures + 32 NASA mission images) | Medium |
| 12 | Meteorites, asteroids, minor planets & comets | Outline drafted | Medium |
| 13 | Exoplanets | Outline drafted | Medium |
| 14 | Synthesis & astrobiology | Draft + figures cleaned (27 arxiv-sourced figures, max 2 per source) | Low |

**Priority rationale:** Lectures 1–8 cover foundational topics needed before planet-specific lectures; Lectures 9–13 build on these; Lecture 14 synthesizes the full course.

#### Lecture Slides (14 sets, PDF from LaTeX)

Each lecture requires a companion PDF slide deck compiled from LaTeX source files. The slides should cover the same content as the corresponding lecture notes in the Jupyter Book, distilled into a visual presentation format suitable for classroom delivery.

| # | Lecture | Status | Priority |
|---|--------|--------|----------|
| 1 | Introduction & history | Draft complete | High |
| 2 | Planet formation & orbital dynamics | Draft complete | High |
| 3 | Planetary heat & energy transport | Draft complete | High |
| 4 | Chemical differentiation & magnetospheres | Draft complete | High |
| 5 | Atmospheres I | Draft complete | High |
| 6 | Atmospheres II | Draft complete | High |
| 7 | Planetary surfaces | Draft complete | High |
| 8 | Planetary interiors | Draft complete | High |
| 9 | Rocky planets: Earth & Venus | Not started | Medium |
| 10 | Rocky planets: Mercury & Mars | Notes draft + figure cleanup pass | Medium |
| 11 | Gas & ice giants | Not started | Medium |
| 12 | Meteorites, asteroids, minor planets & comets | Not started | Medium |
| 13 | Exoplanets | Not started | Medium |
| 14 | Synthesis & astrobiology | Not started | Low |

**Slide infrastructure (complete):**
- Custom Beamer theme: `slides/common/beamerthemeIPS.sty`: dark navy/teal palette, Inter + Fira Math fonts (XeLaTeX), `\ipscontain` for background images, `\sectionimage`/`\breakslide`/`\keyresult`/`\source` helper commands, thin accent-line frame titles, minimal footline (author, short title, slide number)
- Shared math macros: `slides/common/macros.tex` mirrors `_config.yml` definitions
- Build system: `slides/Makefile` with `avif2png` and `svg2pdf` targets (auto-conversion for XeLaTeX via `magick` and `cairosvg`), `latexmk -xelatex`; integrated into root `Makefile` via `make slides`
- `.gitignore`: ignores LaTeX build artifacts and generated PNG/PDF in slide figure directories

**Lectures 1-8 slides (all built cleanly, expanded to 60+ frames each):**
- L1: `slides/lecture01/lecture01.tex`, 61 pages
- L2: `slides/lecture02/lecture02.tex`, 61 pages
- L3: `slides/lecture03/lecture03.tex`, 60 pages
- L4: `slides/lecture04/lecture04.tex`, 60 pages
- L5: `slides/lecture05/lecture05.tex`, 60 pages
- L6: `slides/lecture06/lecture06.tex`, 60 pages
- L7: `slides/lecture07/lecture07.tex`, 60 pages
- L8: `slides/lecture08/lecture08.tex`, 60 pages
- All 105 em-dash instances across the 8 decks replaced per CLAUDE.md style
- All SVG figures in column layouts audited and constrained with `width=\linewidth, keepaspectratio` to prevent overflow
- `slides/Makefile` updated with `svg2pdf` target using `cairosvg` (L2-L6 had SVG references that xelatex could not resolve before this fix)
- Second pass added: recent-developments frames (Juno, JUICE, Europa Clipper, OSIRIS-REx, Hayabusa2, DART, JWST MAPS, Perseverance, BepiColombo, Psyche, MAVEN, InSight, Tarduno paleomagnetism), dedicated physics-derivation frames (Rayleigh number comparison, Nusselt scaling, adiabatic gradient, Jeans parameter, energy-limited escape, partition coefficients, Hf-W chronometer, magnetopause derivation, tidal dissipation rate), and deeper notes-coverage frames (mantle reservoirs, mantle plumes, snowball Earth, runaway greenhouse, Milankovitch cycles, thermal tides, super-ionic ice, Ganymede interior, crater size-frequency distribution)

Each slide deck requires:
- LaTeX source file (Beamer presentation class) using the custom IPS theme (`slides/common/beamerthemeIPS.sty`)
- Compiled PDF for distribution to students (built via `make slides` from project root)
- Figures and diagrams consistent with the Jupyter Book lecture notes
- All raster images in AVIF format (`.avif`); the build system auto-converts to PNG for XeLaTeX

#### Homework Sheets (7 sets, each with solutions)

| # | Homework | Follows Lectures | Status |
|---|----------|-----------------|--------|
| 1 | Orbits & Formation | 1–2 | Not started |
| 2 | Thermal Evolution & Differentiation | 3–4 | Not started |
| 3 | Atmospheres | 5–6 | Not started |
| 4 | Surfaces & Interiors | 7–8 | Not started |
| 5 | Terrestrial Planets | 9–10 | Not started |
| 6 | Giant Planets & Small Bodies | 11–12 | Not started |
| 7 | Exoplanets & Synthesis | 13–14 | Not started |

Each homework requires:
- Problem sheet (PDF, from LaTeX or Jupyter notebook source)
- Full solutions (for instructors)
- Student solution template (partial solutions / answer boxes)

#### Exams (2 sets, each with solutions)

| Exam | Scope | Status |
|------|-------|--------|
| Mid-term | Lectures 1–7 | Not started |
| Final | Lectures 1–14 (cumulative) | Not started |

Each exam requires:
- Exam paper
- Full solutions and marking scheme
- Equation sheet

### Reusable Material from course2025

The previous iteration (12 lectures, 9 tutorials) provides a foundation to draw from. Key assets:

- **Tutorial problems:** Many problems from tutorials 1–9 can be adapted for the new homework sheets, particularly:
  - Tutorial 1 (Dynamics): Jupyter notebooks on resonances and N-body → Homework 1
  - Tutorial 2 (Heat): Analytical problems → Homework 2
  - Tutorial 3 (Atmospheres): Analytical problems → Homework 3
  - Tutorial 4 (Surfaces & interiors): Can be split across Homeworks 4 and 5
  - Tutorial 5 (Magnetospheres): Problems → fold into Homework 2
  - Tutorials 7–8 (Minor planets, comets): Combine → Homework 6
  - Tutorial 9 (Planet formation): Fold into Homework 1

- **Exam questions:** Previous mid-term and final exams provide a question bank to draw from and adapt.

- **Lecture slides:** Previous lecture content provides reference material, though all notes will be rewritten as custom lecture notes rather than slide decks.

### Technical Standards

- **Image format:** All raster images use AVIF (`.avif`). Do not commit JPEG or PNG files. Convert with `magick input.jpg -quality 65 output.avif`. SVG vector graphics are kept as-is. The Makefiles auto-convert AVIF→PNG for LaTeX/XeLaTeX builds.
- **Fonts:** Inter (sans-serif text) via fontspec/XeLaTeX; Fira Math (sans-serif math) via unicode-math. Used in both Jupyter Book PDF and Beamer slides.
- **Citations:** Chicago author-date style via custom pybtex plugin. Use `{cite:p}` and `{cite:t}` roles exclusively.

### Development Sequence

1. **Phase 1a — Lecture notes (Lectures 1–8):** ✅ Complete. Core foundational content, needed first since all other lectures build on these.
2. **Phase 1b — Lecture notes images (Lectures 1–8):** ✅ Complete. Figures and diagrams for the first 8 lectures. We want to end up with about 10–15 figures per lecture, including:
   - Diagrams of planetary interiors, atmospheres, and surfaces; physical and chemical processes; and comparative planetology schematics
   - Plots of observational data (e.g., planetary demographics, atmospheric profiles)
   - Conceptual illustrations (e.g., orbital resonances, heat transport mechanisms)
3. **Phase 1c — Lecture notes verification (Lectures 1–8):** ✅ Complete. Double check consistency of all notes and pedagogic approach. Deeply verify the scientific validity of all content, in particular of all derivations and equations, facts and values of any parameters, constants, and calculations. Double check all figures, and ensure all derivations are clear and correct before moving on to slides. Validate that the lecture notes are self-contained and can be understood without external references, as they will be the primary resource for students. Verify all references and citations for accuracy and relevance. Ensure all BibTeX entries use Chicago author-date format (custom pybtex style in `src/ips_styles/chicago.py`), include DOIs where available, and link to open-access sources (NASA ADS preferred, then arXiv, then publisher open access).
4. **Phase 2a — Lecture slides (Lectures 1–8):** 🔄 In progress (L1–L8 first drafts complete; needs review and refinement). PDF slide decks from LaTeX, covering the same content as the Jupyter Book notes for classroom delivery. The slide decks should be visually engaging and include key figures from the lecture notes, but distilled into a presentation format suitable for teaching. Each slide deck should be consistent in style and formatting across lectures. The slides should cover a lecture of about 90 minutes, with a mix of text, equations, and figures to effectively communicate the material. The slide decks should be designed to complement the lecture notes, not duplicate them, and should focus on the key concepts and takeaways for each lecture.
5. **Phase 3 — Homework sheets 1–4 + mid-term exam:** Homework covering Lectures 1–8 and mid-term covering Lectures 1–7.
6. **Phase 4a — Lecture notes (Lectures 9–14):** Planet-specific, exoplanets, and synthesis lectures.
7. **Phase 4b — Lecture notes images (Lectures 9–14):** Find and create figures and diagrams for the first 8 lectures, which are needed to complete the lecture notes and ensure they are visually informative. We want to end up with about 10–15 figures per lecture, including:
   - Diagrams of planetary interiors, atmospheres, and surfaces; physical and chemical processes; and comparative planetology schematics
   - Plots of observational data (e.g., planetary demographics, atmospheric profiles)
   - Conceptual illustrations (e.g., orbital resonances, heat transport mechanisms)
8. **Phase 4c — Lecture notes verification (Lectures 9–14):** Double check consistency of all notes and pedagogic approach. Deeply verify the scientific validity of all content, in particular of all derivations and equations, facts and values of any parameters, constants, and calculations. Double check all figures, and ensure all derivations are clear and correct before moving on to slides. Validate that the lecture notes are self-contained and can be understood without external references, as they will be the primary resource for students. Verify all references and citations for accuracy and relevance. Ensure all BibTeX entries use Chicago author-date format, include DOIs, and link to open-access sources (NASA ADS preferred).
9. **Phase 5 — Lecture slides (Lectures 9–14):** PDF slide decks from LaTeX for these remaining lecture notes, covering the same content as the Jupyter Book notes for classroom delivery. The slide decks should be visually engaging and include key figures from the lecture notes, but distilled into a presentation format suitable for teaching. Each slide deck should be consistent in style and formatting across lectures. The slides should cover a lecture of about 90 minutes, with a mix of text, equations, and figures to effectively communicate the material. The slide decks should be designed to complement the lecture notes, not duplicate them, and should focus on the key concepts and takeaways for each lecture.
10. **Phase 6 — Homework sheets 5–7 + final exam:** Remaining homework and cumulative final exam.
11. **Phase 7 — Review and polish:** Cross-referencing between lectures, consistency check, equation sheet compilation.
