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

- Earth as reference: plate tectonics, hydrosphere, biosphere coupling
- Earth's unique properties: magnetic field, liquid water, active geology
- Earth's climate system: ocean circulation, ice ages, Milankovitch cycles
- Venus: Earth's "twin" — similarities and divergences
- Venus surface: Magellan radar mapping, volcanic plains, tesserae, coronae
- Venus atmosphere: dense CO₂, sulfuric acid clouds, super-rotation
- Runaway greenhouse on Venus: implications for climate science
- **Blackboard derivation (~10 min):** Derive the runaway greenhouse threshold — show that outgoing longwave radiation reaches a maximum in a moist atmosphere (the Simpson–Nakajima limit): when absorbed stellar flux exceeds this limit, surface temperature diverges. Estimate the critical solar flux and compare to Venus's orbit
- Missing water on Venus: D/H ratio constraints
- Comparative habitability: why Earth and Venus diverged
- Recent advances: DAVINCI and VERITAS mission concepts for Venus, EnVision ESA mission, new models of Venus's volcanic and climatic history, updated constraints on early Earth's habitability

### Lecture 10: Rocky Planets — Mercury & Mars

- Mercury: orbit and spin–orbit resonance (3:2)
- Mercury's interior: large iron core, thin mantle, MESSENGER and BepiColombo results
- Mercury's surface: heavily cratered, smooth plains, hollows
- Mercury's exosphere and magnetosphere
- Mars: geological history (Noachian, Hesperian, Amazonian epochs)
- Evidence for past water: valley networks, outflow channels, mineral signatures
- Mars today: thin atmosphere, seasonal dynamics, methane detections
- **Blackboard derivation (~10 min):** Derive the Jeans escape flux — starting from the Maxwell–Boltzmann velocity distribution, integrate above the escape velocity to obtain the escape parameter λ = GMm/kTr and the escape rate, then compare H₂ vs. CO₂ escape from Mars
- Olympus Mons, Valles Marineris, and the hemispheric dichotomy
- Mars exploration: rovers, orbiters, sample return plans
- Mars habitability: past and present prospects
- Recent advances: Perseverance sample caching and Mars Sample Return status, BepiColombo Mercury flybys, Curiosity long-term climate record from Gale crater, subsurface water detections by radar

### Lecture 11: Gas & Ice Giants — Jupiter, Saturn, Uranus, Neptune

- Jupiter: composition, internal structure, atmospheric dynamics
- Jupiter's moons: Galilean satellites (Io, Europa, Ganymede, Callisto) and their diversity
- Saturn: ring system structure, dynamics, origin and evolution
- Saturn's moons: Titan (atmosphere, lakes), Enceladus (plumes, subsurface ocean)
- Planetary rings: composition, Roche limit, shepherding moons, ring–moon interactions
- **Blackboard derivation (~10 min):** Derive the Roche limit — equate the tidal force from the planet on a satellite element with the satellite's self-gravity to obtain d_Roche ≈ 2.46 R_p (ρ_p/ρ_s)^{1/3}, and apply to Saturn's rings
- Uranus: extreme axial tilt, muted atmosphere, interior structure
- Neptune: atmospheric activity, Great Dark Spot, internal heat excess
- Triton: retrograde orbit, captured KBO, cryovolcanism
- Ice giant exploration: current knowledge gaps and future mission concepts
- Recent advances: Juno extended mission results (Jupiter's interior and moons), JUICE mission en route to Jupiter system, James Webb observations of Uranus and Neptune ring systems, Cassini legacy analysis of Saturn and Enceladus

### Lecture 12: Meteorites, Asteroid Belt, Minor Planets & Comets

- Meteorite classification: chondrites (ordinary, carbonaceous, enstatite), achondrites, irons, stony-irons
- Chondrules and CAIs: oldest solar system solids, formation conditions
- Isotopic dating: Pb–Pb, Al–Mg, Hf–W chronometry
- **Blackboard derivation (~10 min):** Derive the radioactive decay law N(t) = N₀ e^{−λt} and the isochron equation for the Pb–Pb system, then show how the slope of the isochron gives the age of the oldest solar system solids (CAIs, 4.567 Gyr)
- Meteorites as probes of early solar system conditions and parent body processes
- Asteroid belt: structure, orbital families, resonance gaps (Kirkwood gaps)
- Asteroid taxonomy: C-, S-, M-types and compositional mapping
- Near-Earth asteroids: impact hazard, deflection strategies
- Kuiper Belt and scattered disk: orbital structure, Pluto and dwarf planets
- Oort cloud: theoretical framework and observational constraints
- Comets: composition (ices, dust, organics), activity, tails (ion and dust)
- Short-period vs. long-period comets: dynamical origins
- Rosetta mission to 67P: key results
- Recent advances: OSIRIS-REx sample return from Bennu, DART planetary defense results, Lucy mission to Trojan asteroids, new Kuiper Belt object discoveries and interstellar object detections

### Lecture 13: Exoplanets — Detection Methods, Demographics, & Characterization

- Historical context: first detections (pulsar planets, 51 Peg b)
- Radial velocity method: Doppler wobble, mass–period sensitivity
- Transit method: light curves, radius determination, Kepler/TESS missions
- **Blackboard derivation (~10 min):** Derive the transit depth (ΔF/F = (R_p/R_★)², ~2 min geometry), then the radial velocity semi-amplitude K from momentum conservation (~5 min), and show how combining both measurements yields mass, radius, and bulk density of an exoplanet (~3 min)
- Direct imaging: coronagraphy, high-contrast techniques, current capabilities
- Other methods: astrometry (Gaia), microlensing, timing variations
- Exoplanet demographics: occurrence rates, period–radius distribution, the radius valley
- Hot Jupiters, super-Earths, sub-Neptunes: formation and migration theories
- Atmospheric characterization: transmission and emission spectroscopy
- JWST results: atmospheric detections, thermal emission maps
- Habitability beyond the solar system: habitable zone concept, biosignatures
- Recent advances: JWST atmospheric characterization of rocky exoplanets (TRAPPIST-1 system), updated exoplanet occurrence rates from Kepler/TESS, Gaia astrometric planet detections, direct imaging breakthroughs

### Lecture 14: Synthesis — Solar System in Context & Astrobiology

- Our solar system as one planetary system among many: what is typical, what is unusual?
- Planet formation theory meets observations: successes and open questions
- Habitability as a systems property: star, orbit, planet, atmosphere, interior coupling
- **Blackboard derivation (~10 min):** Derive the habitable zone boundaries — from L_★ = 4πd²F and the condition that surface temperature allows liquid water, obtain the inner and outer HZ distances as a function of stellar luminosity, and compare for G, K, and M dwarfs
- Water in the universe: origin, delivery mechanisms, and distribution
- Astrobiology: requirements for life, extremophiles, biosignature gases
- Solar system targets for life detection: Mars, Europa, Enceladus, Titan
- Exoplanet targets and future missions: HWO, LIFE, ground-based ELTs
- Open questions and frontiers in planetary science
- Course synthesis: connecting formation to present-day diversity
- Recent advances: new constraints on habitable zone boundaries from 3D climate models, biosignature false-positive debates, upcoming mission landscape (HWO, LIFE, Dragonfly), and the latest results connecting solar system and exoplanet science

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
| 9 | Rocky planets: Earth & Venus | Not started | Medium |
| 10 | Rocky planets: Mercury & Mars | Not started | Medium |
| 11 | Gas & ice giants | Not started | Medium |
| 12 | Meteorites, asteroids, minor planets & comets | Not started | Medium |
| 13 | Exoplanets | Not started | Medium |
| 14 | Synthesis & astrobiology | Not started | Low |

**Priority rationale:** Lectures 1–8 cover foundational topics needed before planet-specific lectures; Lectures 9–13 build on these; Lecture 14 synthesizes the full course.

#### Lecture Slides (14 sets, PDF from LaTeX)

Each lecture requires a companion PDF slide deck compiled from LaTeX source files. The slides should cover the same content as the corresponding lecture notes in the Jupyter Book, distilled into a visual presentation format suitable for classroom delivery.

| # | Lecture | Status | Priority |
|---|--------|--------|----------|
| 1 | Introduction & history | Draft complete | High |
| 2 | Planet formation & orbital dynamics | Not started | High |
| 3 | Planetary heat & energy transport | Not started | High |
| 4 | Chemical differentiation & magnetospheres | Not started | High |
| 5 | Atmospheres I | Not started | High |
| 6 | Atmospheres II | Not started | High |
| 7 | Planetary surfaces | Not started | High |
| 8 | Planetary interiors | Not started | High |
| 9 | Rocky planets: Earth & Venus | Not started | Medium |
| 10 | Rocky planets: Mercury & Mars | Not started | Medium |
| 11 | Gas & ice giants | Not started | Medium |
| 12 | Meteorites, asteroids, minor planets & comets | Not started | Medium |
| 13 | Exoplanets | Not started | Medium |
| 14 | Synthesis & astrobiology | Not started | Low |

**Slide infrastructure (complete):**
- Custom Beamer theme: `slides/common/beamerthemeIPS.sty` — dark navy/teal palette, Inter + Fira Math fonts (XeLaTeX), `\ipscontain` for background images, `\sectionimage`/`\breakslide`/`\keyresult`/`\source` helper commands, thin accent-line frame titles, minimal footline (author | short title | slide number)
- Shared math macros: `slides/common/macros.tex` — mirrors `_config.yml` definitions
- Build system: `slides/Makefile` with `avif2png` target (AVIF→PNG auto-conversion for XeLaTeX), `latexmk -xelatex`; also integrated into root `Makefile` via `make slides`
- `.gitignore`: ignores LaTeX build artifacts and generated PNG/JPG

**Lecture 1 slides (draft complete, needs review):**
- `slides/lecture01/lecture01.tex` — 61 pages (50 content frames + 8 section dividers + title + break + closing)
- 22 images across 30 AVIF files in `slides/lecture01/figures/` (~30 content images + 8 unique section transition backgrounds)
- Section transition images: Earth (Apollo 17), Pluto (New Horizons), Flammarion engraving, Saturn (Cassini equinox), Sun (SDO), Mars (Rosetta/OSIRIS), VLT laser guide star, Milky Way
- Exoplanet discovery plots: sourced directly from NASA Exoplanet Archive (`exoplanetarchive.ipac.caltech.edu/exoplanetplots/`)
- Final slide links to Lecture 2 with title background image
- Known issues to address in next review pass: verify all slide content fits within frame boundaries at different projector resolutions; some slides with dense tables or equations may benefit from font size adjustments

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
4. **Phase 2a — Lecture slides (Lectures 1–8):** 🔄 In progress (L1 draft complete; L2–L8 not started). PDF slide decks from LaTeX, covering the same content as the Jupyter Book notes for classroom delivery. The slide decks should be visually engaging and include key figures from the lecture notes, but distilled into a presentation format suitable for teaching. Each slide deck should be consistent in style and formatting across lectures. The slides should cover a lecture of about 90 minutes, with a mix of text, equations, and figures to effectively communicate the material. The slide decks should be designed to complement the lecture notes, not duplicate them, and should focus on the key concepts and takeaways for each lecture.
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
