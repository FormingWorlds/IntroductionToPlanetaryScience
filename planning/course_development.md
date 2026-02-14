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
- Comparative planetology as a methodology
- Observational techniques: ground-based, space missions, in situ measurements
- Key spacecraft missions past, present, and planned (Voyager, Cassini, JWST, etc.)
- **Blackboard derivation (~10 min):** Estimate the total mass of the solar system's planets from Newtonian gravity — derive the planet-to-star mass ratio from orbital period and semi-major axis using Kepler's third law and compare to the observed value

### Lecture 2: Planet Formation 101 & Orbital Dynamics

- Star formation and protoplanetary disks: observational evidence and structure
- Dust coagulation, pebble accretion, and planetesimal formation
- Runaway and oligarchic growth; giant planet core accretion vs. gravitational instability
- Kepler's laws and orbital elements
- Two-body problem, reduced mass, and vis-viva equation
- Orbital resonances: mean-motion resonances, Laplace resonance of the Galilean moons
- Tidal forces and tidal locking; Roche limit
- Planetary migration: types I, II, III and the Nice model
- **Blackboard derivation (~10 min):** Derive the vis-viva equation from energy conservation in a Keplerian orbit (total energy = kinetic + gravitational potential, relate to semi-major axis)

### Lecture 3: Planetary Heat & Energy Transport

- Energy sources: accretional heating, gravitational differentiation, radioactive decay, tidal heating
- Heat transport mechanisms: conduction, convection, radiation
- Thermal evolution of terrestrial planets: cooling models and parameterized convection
- Rayleigh number, Nusselt number, and convective vigor
- Thermal boundary layers and mantle convection basics
- Surface heat flow: Earth as calibration, comparison to Moon and Mars
- Tidal dissipation: Io as an extreme case, implications for icy moons
- **Blackboard derivation (~10 min):** Derive the conductive cooling timescale τ ∼ L²/κ from the heat diffusion equation, and apply it to estimate cooling times for bodies of different sizes (asteroid vs. Moon vs. Earth)

### Lecture 4: Chemical Differentiation & Magnetospheres

- Accretion and early melting: magma oceans and metal–silicate separation
- Core formation: siderophile element partitioning, Hf–W chronometry
- Mantle differentiation: major-element geochemistry, mantle reservoirs
- Volatile delivery and retention: role of impacts and outgassing
- Planetary magnetic fields: dynamo theory fundamentals
- Requirements for dynamo action: convecting, electrically conducting fluid
- Earth's geodynamo: structure, secular variation, reversals
- Comparative magnetospheres: Mercury (weak), Mars (remnant crustal), Jupiter (strong), Ganymede
- Magnetosphere–solar wind interaction: bow shock, magnetopause, magnetotail
- Auroral processes and radiation belts
- **Blackboard derivation (~10 min):** Derive the magnetic Reynolds number Rm = UL/η from the induction equation, and estimate Rm for Earth's core to show that advection dominates over diffusion (dynamo feasibility criterion)

### Lecture 5: Atmospheres I — Composition, Structure, & Dynamics

- Atmospheric composition: primary, secondary, and tertiary atmospheres
- Hydrostatic equilibrium and pressure–temperature profiles
- Vertical structure: troposphere, stratosphere, mesosphere, thermosphere
- Radiative transfer basics: optical depth, absorption, emission
- Greenhouse effect: radiative–convective equilibrium
- Energy balance: albedo, effective temperature vs. surface temperature
- Atmospheric escape: Jeans escape, hydrodynamic escape, sputtering, photochemical escape
- Atmospheric retention: the role of gravity and temperature
- **Blackboard derivation (~10 min):** Derive the atmospheric scale height H = kT/mg from hydrostatic equilibrium (dP/dz = −ρg) combined with the ideal gas law, and compute H for Earth, Mars, and Venus

### Lecture 6: Atmospheres II — Clouds, Weather, & Climate

- Cloud formation: condensation, nucleation, and cloud types across the solar system
- Venus: runaway greenhouse, sulfuric acid clouds, super-rotation
- Mars: thin CO₂ atmosphere, dust storms, seasonal CO₂ cycle
- Titan: methane hydrological cycle, organic haze
- Giant planet atmospheres: banded structure, zones and belts, composition
- Atmospheric dynamics: Hadley cells, Coriolis effect, geostrophic balance
- Jet streams and vortices: Jupiter's Great Red Spot, Saturn's hexagon
- Climate evolution: faint young Sun problem, long-term climate feedbacks
- Carbonate–silicate cycle and climate regulation on Earth
- **Blackboard derivation (~10 min):** Derive the planetary effective temperature from energy balance (absorbed stellar flux = emitted thermal flux), then add a single-layer greenhouse atmosphere to show how T_surface > T_eff

### Lecture 7: Planetary Surfaces — Geology, Geomorphology, & Geophysics

- Surface processes: impact cratering, volcanism, tectonics, erosion
- Impact cratering: mechanics, morphology (simple, complex, basins), crater counting and surface ages
- Volcanism: effusive vs. explosive, volcanic landforms across the solar system
- Tectonics: plate tectonics on Earth, stagnant lid on other terrestrial bodies
- Erosion and weathering: aeolian, fluvial, glacial, chemical
- Remote sensing of surfaces: spectroscopy, radar, altimetry
- Regolith formation and space weathering
- Cryovolcanism on icy bodies: Enceladus, Triton, Europa
- **Blackboard derivation (~10 min):** Derive the crater scaling law — relate impactor kinetic energy ½mv² to crater diameter using dimensional analysis and the pi-scaling theorem, then estimate the crater size from a 1 km asteroid impact on the Moon

### Lecture 8: Planetary Interiors — Structure, Composition, & Dynamics

- Probing interiors: seismology, gravity field, moment of inertia
- Equations of state: relating pressure, density, and temperature at depth
- Earth's interior: crust, mantle, outer core, inner core
- Mantle rheology: viscous flow, mantle convection patterns
- Phase transitions: olivine–spinel–perovskite, post-perovskite
- Comparative interiors: Moon (small core), Mars (large core fraction), Mercury (large iron core)
- Giant planet interiors: metallic hydrogen, layered vs. dilute cores
- Ice giant interiors: water, ammonia, methane ices under extreme pressures
- Icy moon interiors: subsurface oceans (Europa, Enceladus, Titan)
- **Blackboard derivation (~10 min):** Derive the moment of inertia factor C/MR² for a uniform sphere vs. a differentiated two-layer body (dense core + lighter mantle), and show how the measured value constrains core size

### Lecture 9: Rocky Planets — Earth & Venus

- Earth as reference: plate tectonics, hydrosphere, biosphere coupling
- Earth's unique properties: magnetic field, liquid water, active geology
- Earth's climate system: ocean circulation, ice ages, Milankovitch cycles
- Venus: Earth's "twin" — similarities and divergences
- Venus surface: Magellan radar mapping, volcanic plains, tesserae, coronae
- Venus atmosphere: dense CO₂, sulfuric acid clouds, super-rotation
- Runaway greenhouse on Venus: implications for climate science
- Missing water on Venus: D/H ratio constraints
- Comparative habitability: why Earth and Venus diverged
- **Blackboard derivation (~10 min):** Derive the runaway greenhouse threshold — starting from the outgoing longwave radiation limit (Simpson–Nakajima limit), show that there is a maximum flux a moist atmosphere can radiate, and estimate the critical solar flux at which Venus lost its water

### Lecture 10: Rocky Planets — Mercury & Mars

- Mercury: orbit and spin–orbit resonance (3:2)
- Mercury's interior: large iron core, thin mantle, MESSENGER and BepiColombo results
- Mercury's surface: heavily cratered, smooth plains, hollows
- Mercury's exosphere and magnetosphere
- Mars: geological history (Noachian, Hesperian, Amazonian epochs)
- Evidence for past water: valley networks, outflow channels, mineral signatures
- Mars today: thin atmosphere, seasonal dynamics, methane detections
- Olympus Mons, Valles Marineris, and the hemispheric dichotomy
- Mars exploration: rovers, orbiters, sample return plans
- Mars habitability: past and present prospects
- **Blackboard derivation (~10 min):** Derive the Jeans escape flux — starting from the Maxwell–Boltzmann velocity distribution, integrate above the escape velocity to obtain the escape parameter λ = GMm/kTr and the escape rate, then compare H₂ vs. CO₂ escape from Mars

### Lecture 11: Gas & Ice Giants — Jupiter, Saturn, Uranus, Neptune

- Jupiter: composition, internal structure, atmospheric dynamics
- Jupiter's moons: Galilean satellites (Io, Europa, Ganymede, Callisto) and their diversity
- Saturn: ring system structure, dynamics, origin and evolution
- Saturn's moons: Titan (atmosphere, lakes), Enceladus (plumes, subsurface ocean)
- Planetary rings: composition, Roche limit, shepherding moons, ring–moon interactions
- Uranus: extreme axial tilt, muted atmosphere, interior structure
- Neptune: atmospheric activity, Great Dark Spot, internal heat excess
- Triton: retrograde orbit, captured KBO, cryovolcanism
- Ice giant exploration: current knowledge gaps and future mission concepts
- **Blackboard derivation (~10 min):** Derive the Roche limit — equate the tidal force from the planet on a satellite element with the satellite's self-gravity to obtain d_Roche ≈ 2.46 R_p (ρ_p/ρ_s)^{1/3}, and apply to Saturn's rings

### Lecture 12: Meteorites, Asteroid Belt, Minor Planets & Comets

- Meteorite classification: chondrites (ordinary, carbonaceous, enstatite), achondrites, irons, stony-irons
- Chondrules and CAIs: oldest solar system solids, formation conditions
- Isotopic dating: Pb–Pb, Al–Mg, Hf–W chronometry
- Meteorites as probes of early solar system conditions and parent body processes
- Asteroid belt: structure, orbital families, resonance gaps (Kirkwood gaps)
- Asteroid taxonomy: C-, S-, M-types and compositional mapping
- Near-Earth asteroids: impact hazard, deflection strategies
- Kuiper Belt and scattered disk: orbital structure, Pluto and dwarf planets
- Oort cloud: theoretical framework and observational constraints
- Comets: composition (ices, dust, organics), activity, tails (ion and dust)
- Short-period vs. long-period comets: dynamical origins
- Rosetta mission to 67P: key results
- **Blackboard derivation (~10 min):** Derive the radioactive decay law N(t) = N₀ e^{−λt} and the isochron equation for the Pb–Pb system, then show how the slope of the isochron gives the age of the oldest solar system solids (CAIs, 4.567 Gyr)

### Lecture 13: Exoplanets — Detection Methods, Demographics, & Characterization

- Historical context: first detections (pulsar planets, 51 Peg b)
- Radial velocity method: Doppler wobble, mass–period sensitivity
- Transit method: light curves, radius determination, Kepler/TESS missions
- Direct imaging: coronagraphy, high-contrast techniques, current capabilities
- Other methods: astrometry (Gaia), microlensing, timing variations
- Exoplanet demographics: occurrence rates, period–radius distribution, the radius valley
- Hot Jupiters, super-Earths, sub-Neptunes: formation and migration theories
- Atmospheric characterization: transmission and emission spectroscopy
- JWST results: atmospheric detections, thermal emission maps
- Habitability beyond the solar system: habitable zone concept, biosignatures
- **Blackboard derivation (~10 min):** Derive the transit depth equation (ΔF/F = (R_p/R_★)²) and the radial velocity semi-amplitude K from the two-body problem, then show how combining both yields both mass and radius (and hence bulk density) of an exoplanet

### Lecture 14: Synthesis — Solar System in Context & Astrobiology

- Our solar system as one planetary system among many: what is typical, what is unusual?
- Planet formation theory meets observations: successes and open questions
- Habitability as a systems property: star, orbit, planet, atmosphere, interior coupling
- Water in the universe: origin, delivery mechanisms, and distribution
- Astrobiology: requirements for life, extremophiles, biosignature gases
- Solar system targets for life detection: Mars, Europa, Enceladus, Titan
- Exoplanet targets and future missions: HWO, LIFE, ground-based ELTs
- Open questions and frontiers in planetary science
- Course synthesis: connecting formation to present-day diversity
- **Blackboard derivation (~10 min):** Derive the habitable zone boundaries — from L_★ = 4πd²F and the condition that surface temperature allows liquid water, obtain the inner and outer HZ distances as a function of stellar luminosity, and compare for G, K, and M dwarfs

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

**Priority rationale:** Lectures 1–8 cover foundational topics needed before planet-specific lectures; Lectures 9–13 build on these; Lecture 14 synthesizes the full course.

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

### Development Sequence

1. **Phase 1 — Lecture notes (Lectures 1–8):** Core foundational content, needed first since all other lectures build on these.
2. **Phase 2 — Homework sheets 1–4 + mid-term exam:** Homework covering Lectures 1–8 and mid-term covering Lectures 1–7, developed in parallel with Phase 1.
3. **Phase 3 — Lecture notes (Lectures 9–14):** Planet-specific, exoplanets, and synthesis lectures.
4. **Phase 4 — Homework sheets 5–7 + final exam:** Remaining homework and cumulative final exam.
5. **Phase 5 — Review and polish:** Cross-referencing between lectures, consistency check, equation sheet compilation.
