(lecture12)=
# Lecture 12: Meteorites, Asteroids, Minor Planets & Comets

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to classify meteorites and use isotopic chronometers to date the early solar system, describe the dynamics and populations of the asteroid belt and trans-Neptunian region, explain the origin and structure of comets, and use small bodies as formation fossils that record the solar system's dynamical and chemical history.
```

```{note}
**Status:** Detailed bullet outline below. Full prose sections to be written in a subsequent pass. The lecture follows the same descriptive-first, payoff-at-the-end structure as L9--L11: meteorites (Part 1), then populations and dynamics (Part 2), then messengers and visitors (Part 3). Pluto is covered here as a Kuiper Belt / dwarf planet, not in L11.
```


## Part 1: Meteorites — samples of the early solar system

### Why meteorites matter

- The oldest rocks available for direct laboratory analysis — older than any terrestrial or lunar sample
- Provide the **absolute age of the solar system** (4.567 Gyr, from CAI Pb--Pb dating)
- Record the composition and processes of the protoplanetary disk before planets even existed
- Complement sample-return missions (Apollo, Hayabusa2, OSIRIS-REx) with a much larger and more diverse inventory
- Approximately 70{,}000 classified meteorites to date, with more recovered from Antarctic and desert hot spots every year

### Meteorite classification overview

- Broadest division: **chondrites** (primitive, undifferentiated) vs **achondrites** and **irons** (from differentiated parent bodies)
- Further divided by chemistry, mineralogy, and oxygen isotope ratios
- Oxygen isotope plots ($\delta^{17}\mathrm{O}$ vs $\delta^{18}\mathrm{O}$) are the "fingerprint" for parent body identification — each meteorite group clusters at a distinct position

### Chondrites: the most primitive material

- Three major groups: **ordinary chondrites (H, L, LL)**, **carbonaceous chondrites (CI, CM, CV, CO, CR, CK, CH, CB)**, **enstatite chondrites (EH, EL)**
- Ordinary chondrites: most common falls ($\sim$80%), rocky with chondrules
- **Carbonaceous chondrites**: least altered, richest in volatiles and organics, closest to solar composition
  - **CI chondrites**: the most primitive, no chondrules, near-perfect match to solar photosphere composition (Orgueil is the canonical example)
- **Enstatite chondrites**: unusually reduced (Fe mostly metallic), likely formed close to the Sun

### Chondrules and CAIs

- **CAIs (Calcium--Aluminium-rich Inclusions)**: mm-scale refractory inclusions; the **oldest known solar system solids** at 4.567 Gyr
- Formation: flash-heated in the protoplanetary disk, condensed from hot gas at $>$1400 K
- **Chondrules**: mm-scale igneous spherules that make up most chondrite mass
- Formed by rapid melting and cooling (seconds to minutes, peaks $>$1500 K)
- Formation mechanism debated: nebular shocks, current sheets, X-wind model, planetesimal collisions
- Chondrule ages cluster 2--4 Myr after CAIs, overlapping with planetesimal formation

### Isotopic dating of the early solar system

- **Long-lived chronometers**: Pb--Pb, Rb--Sr, Sm--Nd
- **Extinct (short-lived) chronometers**: $^{26}\mathrm{Al}$--$^{26}\mathrm{Mg}$, $^{53}\mathrm{Mn}$--$^{53}\mathrm{Cr}$, $^{182}\mathrm{Hf}$--$^{182}\mathrm{W}$, $^{129}\mathrm{I}$--$^{129}\mathrm{Xe}$, $^{244}\mathrm{Pu}$--Xe (recap from {ref}`lecture03`)
- Cross-calibration between long-lived and extinct chronometers gives the first $\sim$100 Myr of solar system history to $\sim$Myr precision
- CAIs $\rightarrow$ chondrules $\rightarrow$ planetesimal differentiation $\rightarrow$ core formation $\rightarrow$ giant impacts — each step can be dated

### Blackboard derivation (~10 min): The Pb--Pb isochron age of CAIs

- Start from the radioactive decay law:

$$
N(t) = N_0\,e^{-\lambda t}, \quad \lambda = \frac{\ln 2}{t_{1/2}}
$$

- Use the double Pb--Pb chronometer: $^{238}\mathrm{U} \rightarrow {}^{206}\mathrm{Pb}$ ($t_{1/2} = 4.47$ Gyr) and $^{235}\mathrm{U} \rightarrow {}^{207}\mathrm{Pb}$ ($t_{1/2} = 0.704$ Gyr)
- Express the daughter/reference ratios:

$$
\frac{{}^{206}\mathrm{Pb}^*}{{}^{204}\mathrm{Pb}} \quad \text{vs} \quad \frac{{}^{207}\mathrm{Pb}^*}{{}^{204}\mathrm{Pb}}
$$

- Derive the **isochron equation**: for a cogenetic suite of samples, the slope of a plot of $^{207}$Pb/$^{204}$Pb vs $^{206}$Pb/$^{204}$Pb gives the age directly via:

$$
\mathrm{slope} = \frac{{}^{235}\mathrm{U}/{}^{238}\mathrm{U}\big|_\mathrm{now}\,\cdot\,(e^{\lambda_{235}t} - 1)}{e^{\lambda_{238}t} - 1}
$$

- Apply to CAIs: **age = $4567.30 \pm 0.16$ Myr** (Connelly et al.\ 2012) — the most precise absolute age in planetary science
- **Key insight**: the Pb--Pb isochron is self-calibrating (no assumption about initial Pb composition needed) because of the two parallel U decay systems

### Meteorites as probes of parent body processes

- **Petrographic types** (1--7): record thermal metamorphism and aqueous alteration on the parent asteroid
  - Types 3--1: increasing aqueous alteration (water--rock reaction)
  - Types 4--6: increasing thermal metamorphism
- **Shock stages** (S1--S6): record impact pressure, from unshocked to heavily melted
- **Differentiated meteorites**: iron meteorites sample asteroid cores, pallasites sample core--mantle boundaries, HED meteorites (howardite, eucrite, diogenite) sample the Vesta crust
- **Martian meteorites** (SNC group) and **lunar meteorites**: identified by trapped atmospheric gases and oxygen isotope ratios matching each body

### The NC--CC isotopic dichotomy: three interpretations

- **Observation**: meteorites split cleanly into two isotopic reservoirs — non-carbonaceous (NC) and carbonaceous (CC) — in multiple elements ($^{50}$Ti, $^{54}$Cr, $^{48}$Ca, $^{94}$Mo)
- The two groups did not mix for at least the first $\sim$3--4 Myr of solar system history
- **But what does this mean physically? Three competing interpretations:**

- **1. Jupiter as an early physical barrier (Kruijer et al.\ 2017)**
  - Hf--W chronology combined with isotope data: Jupiter's core grew to $\sim$20 $\Mearth$ within the first $\sim$1 Myr
  - Once formed, it gravitationally blocked inward drift of outer-disk pebbles
  - NC reservoir = inner disk, isolated from CC material after Jupiter's barrier was in place
  - This was the first widely accepted interpretation and drives the "Jupiter formed early" narrative

- **2. Snow-line migration and pebble isolation (Lichtenberg et al.\ 2021, Science)**
  - Showed that the bifurcation can arise without Jupiter acting as a physical barrier
  - Mechanism: migration of the water snow line during disk evolution, combined with Jupiter's growth to pebble-isolation mass
  - Early inner-disk planetesimals form dry (NC); later outer-disk planetesimals form ice-rich (CC) once the snow line has moved outward
  - Jupiter's role is to stop pebble drift at its orbit (pebble isolation) rather than to act as a mechanical dam
  - Relaxes the requirement for a $\sim$1 Myr Jupiter; allows a wider range of Jupiter-formation timescales

- **3. Temporal (age) dichotomy (Bizzarro, Connelly, Johansen and collaborators)**
  - Argue that NC and CC do not represent two separate spatial reservoirs but two formation **epochs**
  - NC planetesimals formed early ($\lesssim$1 Myr), from initially solar-composition material
  - CC planetesimals formed later ($\gtrsim$2--3 Myr), after cold outer-disk material drifted inward as pebbles
  - The isotopic difference reflects the evolving disk composition over time, not a fixed spatial partition
  - Consistent with streaming instability / pebble-accretion models of planetesimal formation at distinct epochs
  - Supported by high-precision Pb--Pb and Hf--W ages showing that CC parent bodies are systematically younger than NC parent bodies

- **What they agree on**: all three scenarios require the solar system to have structural or temporal order imprinted on its reservoirs very early, consistent with rapid Jupiter formation
- **What they disagree on**: whether the bifurcation is spatial (barrier model), dynamical (snow-line + pebble isolation), or temporal (epoch-based)
- Actively debated as of 2024--2025; distinguishing the scenarios requires higher-precision chronometry and dynamical modelling
- **Pedagogical point**: the same data can support very different physical pictures; the current three-way debate is a good illustration of how planetary science works in practice


## Part 2: Small body populations and dynamics

### The asteroid belt: structure and dynamics

- $\sim$1.2 million known asteroids larger than 1 km
- Total mass $\sim 4 \times 10^{-4}\,\Mearth$, dominated by Ceres ($\sim$30% of the belt mass by itself)
- Orbital range: 2.1--3.3 AU (main belt), plus Hildas (3.9 AU), Trojans (5.2 AU), and near-Earth objects interior to 1.3 AU perihelion
- **Kirkwood gaps**: depletions in the asteroid distribution at mean-motion resonances with Jupiter (2:1 at 3.3 AU, 3:1 at 2.5 AU, 5:2 at 2.8 AU)
- Gaps are **dynamical sinks**: asteroids swept into resonances have their eccentricities pumped and are ejected onto planet-crossing orbits — the main source of near-Earth asteroids

### Asteroid families and taxonomy

- **Collisional families**: groups of asteroids with similar orbits, the fragments of a single disrupted parent body (Eos, Koronis, Themis, Vesta families)
- **Spectral taxonomy**: classifies asteroids by surface reflectance
  - **C-type** (carbonaceous, dark, hydrated): $\sim$75% of the outer belt; carbonaceous chondrite analogues
  - **S-type** (silicaceous, bright, rocky): $\sim$17% of the population; ordinary chondrite analogues
  - **M-type** (metallic): $\sim$10%; iron meteorite analogues; 16 Psyche is the largest example
  - Plus rarer types: V (basaltic, Vesta family), D (primitive outer belt), P/K (transitional)
- Taxonomy correlates with heliocentric distance: rocky/metal inner belt, carbonaceous outer belt
- This mirrors the volatile gradient in the protoplanetary disk — the asteroid belt preserves a compositional snapshot of the inner-to-outer disk transition

### Near-Earth asteroids (NEAs) and impact hazard

- $\sim$35{,}000 known NEAs, plus continual discoveries
- Source: main-belt asteroids delivered via Kirkwood gaps + the **Yarkovsky effect** (thermal radiation force that slowly changes semi-major axis)
- **Impact frequency** scales with size:
  - 1 km impactors: once per $\sim$500 kyr (civilisation-ending event; $\sim$100 MT energy)
  - 100 m impactors: once per $\sim$10 kyr (Tunguska-scale, $\sim$10 MT)
  - 10 m impactors: once per year (airburst; Chelyabinsk 2013 at $\sim$20 m injured $\sim$1500 people)
- **Deflection strategies**: kinetic impact (DART demonstrated 2022), nuclear standoff (theoretical), gravity tractor (proposed), ion beam (proposed)
- Planetary defence infrastructure: NEOWISE, Catalina Sky Survey, LSST/Vera Rubin Observatory (starting 2025, expected to increase discovery rate by $\sim$10$\times$)

### Ceres and the dwarf planets of the inner solar system

- **Ceres**: largest body in the asteroid belt, $R \approx 470$ km, only dwarf planet in the inner solar system
- Dawn mission (2015--2018): hydrated surface, bright salt deposits in Occator crater, possible subsurface brine reservoirs
- Ceres may be a **displaced outer solar system body** that migrated inward during the Nice model rearrangement
- Only inner-solar-system object in the dwarf planet class

### The Kuiper Belt and scattered disk

- **Classical Kuiper Belt**: objects in circular orbits 30--55 AU
- **Cold classical population**: pristine, never scattered by Neptune, retain primordial binary pairs
- **Hot classical population**: scattered inward during the Nice Model instability
- **Resonant objects**: trapped in mean-motion resonances with Neptune
  - 3:2 resonance ("**plutinos**"): contains Pluto and hundreds of others
  - 2:1 resonance ("twotinos"): less populated
- **Scattered disk**: highly eccentric orbits with perihelia near Neptune, aphelia to $\sim$100 AU or beyond
- **Detached objects**: extreme trans-Neptunian objects with perihelia $>$40 AU, dynamically decoupled from Neptune
- Orbital architecture is a fossil record of Neptune's outward migration during the Nice model instability (recap from {ref}`lecture02`)

### Pluto and the dwarf planets

- **Pluto**: $R = 1188$ km, orbit 29--49 AU, 248-year period, 3:2 resonance with Neptune
- Large moon **Charon** ($R = 606$ km) — the Pluto--Charon system is effectively a binary
- Four small additional moons (Styx, Nix, Kerberos, Hydra)
- **New Horizons flyby (2015)**: revealed astonishing diversity
  - Sputnik Planitia: nitrogen ice glacier with active convection (recap from {ref}`lecture07`)
  - Water-ice mountains up to $\sim$3 km tall
  - Tectonic rifts and possible cryovolcanic features
  - Thin nitrogen atmosphere ($\sim$10 $\mu$bar, in slow escape)
  - Evidence for a possible subsurface liquid water ocean (Nimmo et al.\ 2016)
- **Charon**: ancient cratered surface and a red polar cap from captured Pluto atmosphere
- Extended mission target: **(486958) Arrokoth**, a cold classical KBO imaged 2019, a contact binary, remarkably pristine

### The other dwarf planets

- **Eris**: slightly more massive than Pluto (its discovery in 2005 triggered the IAU planet redefinition); scattered-disk object, perihelion 38 AU, aphelion 97 AU
- **Haumea**: elongated fast-rotating body with a ring system; fragment of a giant collision, parent of a dynamical family
- **Makemake**: classical KBO, methane-ice surface
- **Sedna**: extreme trans-Neptunian object, perihelion 76 AU, aphelion $\sim$900 AU; possible inner Oort cloud member
- **Gonggong, Quaoar, Orcus, Salacia**: additional TNO dwarf planet candidates

### The Oort cloud

- Theoretical spherical reservoir of icy bodies at $\sim$2000--50{,}000 AU, proposed by Oort (1950) to explain the observed distribution of long-period comet orbits
- **Never directly observed** — inferred entirely from the dynamical statistics of incoming long-period comets
- Estimated population: $10^{11}$--$10^{12}$ objects, total mass a few Earth masses
- Origin: planetesimals scattered outward by the giant planets during the early dynamical instability
- Outer Oort cloud is weakly bound and susceptible to perturbations from passing stars and galactic tides
- **Long-period comets** are Oort Cloud objects deflected inward by these perturbations
- The inner Oort cloud (Hills cloud) is a proposed reservoir at $\sim$2000--20{,}000 AU that may be the source of bodies like Sedna

### Comets: composition and activity

- "Dirty snowballs" (Whipple 1950) or "icy dirtballs" — mixtures of water ice, CO, $\mathrm{CO_2}$, methane, ammonia, organic molecules, and silicate/carbonaceous dust
- **Nucleus** typically 1--30 km across, albedo $\sim$4% (very dark)
- As a comet approaches the Sun, sublimating ices produce:
  - **Coma**: extended gas/dust envelope, $10^4$--$10^6$ km
  - **Ion (plasma) tail**: blue, pointing anti-sunward, shaped by solar wind
  - **Dust tail**: yellow/white, curved, shaped by radiation pressure
- Two tails pointing in different directions — a diagnostic feature

### Short-period vs long-period comets

- **Short-period comets** ($P < 200$ yr): orbits in or near the ecliptic; Jupiter-family comets (JFCs, from the scattered disk via Neptune interactions) or Halley-type (intermediate)
- **Long-period comets** ($P > 200$ yr): isotropic inclination distribution, eccentric orbits, come from the Oort cloud
- Dynamical evidence: the Kuiper Belt / scattered disk feeds short-period comets via Neptune scattering; the Oort cloud feeds long-period comets via galactic tides and passing stars
- **Halley's Comet** ($P = 76$ yr) is an intermediate case — likely a long-period comet captured into a shorter orbit by planetary perturbations

### The D/H ratio debate

- Earth's ocean D/H ratio sits between cometary and chondritic values
- Some comets (67P/Churyumov--Gerasimenko) have D/H far from Earth's oceans
- Other comets (103P/Hartley 2) have D/H close to Earth's value
- Individual comets span a factor of $\sim$3 in D/H
- **Implication**: Earth's water was not delivered solely by comets of one type; a mixture of carbonaceous chondrite + comet sources is consistent with the data (Alexander et al.\ 2012, 2019)
- Challenges simple "comets brought Earth's water" narratives
- Active research area tying meteoritics, cometary science, and early-Earth geochemistry together


## Part 3: Messengers and visitors

### Rosetta at comet 67P/Churyumov--Gerasimenko

- ESA mission, 2014--2016; first to orbit a comet and deploy a lander (**Philae**)
- Philae touchdown (November 2014): first soft landing on a comet nucleus (though it bounced and ended up in a partially shaded location)
- **Duck-shaped bilobed nucleus**: likely a contact binary formed by gentle merger of two primordial cometesimals
- Detected water vapour with **D/H ratio $\sim$3$\times$ Earth's oceans** — challenges the "comets delivered Earth's water" hypothesis
- Organic molecules including **glycine** (simplest amino acid), phosphorus, and complex hydrocarbons
- Very low bulk density ($\sim$0.5 g/cm$^3$) $\rightarrow$ $\sim$75% porosity
- Directly observed outbursts, jets, surface evolution, and mass loss rates through perihelion passage
- A transformative mission for cometary science

### Sample return missions

- **Hayabusa** (JAXA, 2010): first asteroid sample return, tiny sample ($\sim$1500 grains) from (25143) Itokawa (S-type); proof of concept
- **Hayabusa2** (JAXA, 2020): returned 5.4 g from (162173) Ryugu (C-type), water-bearing, organic-rich, amino acids and nucleobases identified
- **OSIRIS-REx** (NASA, 2023): returned $\sim$70 g from (101955) Bennu (B-type); hydrated clays, carbonates, phosphates, organics; first US asteroid sample return
- Sample analysis is still in early phases — first results include nucleobases, evidence for aqueous alteration, and possible prebiotic organics
- These samples provide laboratory-quality data far exceeding what any spectrometer in space can achieve

### DART and planetary defence

- Recap from {ref}`lecture07`: NASA DART mission impacted **Dimorphos** (September 2022)
- Orbital period around Didymos changed by $\sim$33 minutes
- First successful active planetary defence test
- **Hera follow-up** (ESA, launched October 2024, arrival 2026): will survey the DART impact site, measure the resulting crater, and refine the momentum transfer efficiency

### Lucy mission to the Jupiter Trojans

- **Lucy** (NASA, launched 2021): first mission to visit Jupiter's Trojan asteroids
- 12-year tour, visiting 1 main-belt asteroid (Dinkinesh, 2023; revealed an unexpected satellite moonlet) and 8 Trojans (2027--2033)
- Trojans occupy Jupiter's L4 and L5 Lagrange points; possibly captured from the outer solar system during Nice model instability
- Targets include Eurybates, Patroclus, Leucus, and others

### Psyche: the metal world

- **Psyche** (NASA, launched October 2023): en route to (16) Psyche, largest M-type asteroid
- Possibly an exposed planetary core (from a differentiated planetesimal whose mantle was stripped)
- Arrival 2029
- Will measure bulk composition, internal structure, and any remnant magnetisation — direct test of the core-fragment hypothesis

### Interstellar visitors

- **1I/'Oumuamua** (October 2017): first confirmed interstellar object
  - Elongated shape, inferred from its light curve
  - Non-gravitational acceleration unexplained
  - Nature still debated (natural cometary outgassing, nitrogen ice chunk, hydrogen iceberg, exotic?)
- **2I/Borisov** (August 2019): first clearly cometary interstellar object
  - Coma, dust tail, composition broadly similar to solar system comets (with enhanced CO)
  - Probed the interior of another planetary system through its outgassing
- **3I/ATLAS** (July 2025): third confirmed interstellar object, currently being characterised
- Population estimates: $\sim$10{,}000 interstellar objects larger than 100 m may be in the inner solar system at any time
- **Vera Rubin Observatory** (LSST, first light 2025) is expected to discover $\sim$1 ISO per year
- Planned mission: **ESA Comet Interceptor** (launch 2029) — will wait at L2 and intercept a pristine long-period comet or an interstellar object as it enters the inner solar system

### Open questions and frontier topics

- Exact composition and structure of the Oort cloud
- Origin of the trans-Neptunian "extreme" population and the Planet Nine hypothesis
- Did Earth's water come from comets, asteroids, or a mix? (D/H evidence is ambiguous)
- How did the isotopic NC--CC dichotomy form and survive? (three competing interpretations above)
- What does the compositional diversity of interstellar visitors tell us about planet formation across the galaxy?
- How complete is the population of Potentially Hazardous Asteroids, and how will LSST change our inventory?


## Summary and takeaways

- **Small bodies are the formation fossils** of the solar system — everything that didn't become a planet
- **Inner small bodies** (main belt) = rocky leftovers; **outer small bodies** (KBOs, comets) = icy leftovers
- The compositional gradient with heliocentric distance mirrors the temperature gradient in the protoplanetary disk ({ref}`lecture02`)
- The orbital architecture records the dynamical history of the giant planets (Nice Model, Grand Tack; {ref}`lecture02`)
- **Meteorites** provide direct ground-truth on ages and compositions that spacecraft missions can only constrain indirectly — the Pb--Pb age of CAIs at $4567.30 \pm 0.16$ Myr is the most precise number in planetary science
- The **NC--CC dichotomy** remains one of the most important open problems: three competing interpretations (Jupiter barrier, snow-line migration, temporal epoch) each make testable predictions
- **Recent missions** (OSIRIS-REx, Hayabusa2, DART, Lucy, Psyche, Rosetta) have transformed the field; future missions (Hera, Comet Interceptor, LSST) will transform it again
- **Interstellar visitors** are a new frontier that connects solar system science directly to exoplanet studies (forward reference to {ref}`lecture13` and {ref}`lecture14`)


## References

```{bibliography}
:filter: docname in docnames
```
