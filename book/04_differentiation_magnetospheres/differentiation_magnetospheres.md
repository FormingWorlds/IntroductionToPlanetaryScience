(lecture04)=
# Lecture 4: Chemical Differentiation & Magnetospheres

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to explain the processes of core formation and mantle differentiation, describe the requirements for planetary dynamo action, and compare magnetic field properties across the solar system.
```

## Accretion and early melting

In {ref}`lecture03` we showed that the gravitational energy released during accretion is more than sufficient to melt an Earth-mass body — producing a global **magma ocean**. We also saw that gravitational differentiation, the sinking of dense iron toward the centre, releases additional energy that helps sustain this molten state. In this lecture we explore the *chemical* consequences of that melting: how a once-homogeneous ball of rock and metal separates into the layered structure — core, mantle, crust — that we observe in the terrestrial planets today.

### Metal–silicate separation

When a growing planet reaches a sufficient size — roughly Moon-sized or larger — accretional heating and the decay of short-lived isotopes like ${}^{26}\mathrm{Al}$ ({ref}`lecture03`) produce widespread melting. In the resulting magma ocean, **metallic iron** (density $\sim 7000$ kg m$^{-3}$) is immiscible with **silicate melt** (density $\sim 3000$ kg m$^{-3}$). Iron droplets settle through the silicate liquid under gravity, eventually accumulating at the centre to form a metallic core {cite:p}`Lichtenberg2023`.

The settling velocity of iron droplets in a silicate magma ocean can be estimated using **Stokes' law** for the terminal velocity of a sphere falling through a viscous fluid:

$$
v_{\mathrm{Stokes}} = \frac{2}{9} \frac{\Delta\rho \, g \, r^2}{\mu}
$$ (eq:stokes-settling)

where $\Delta\rho \approx 4000$ kg m$^{-3}$ is the density contrast between metal and silicate, $g$ is the gravitational acceleration, $r$ is the droplet radius, and $\mu$ is the dynamic viscosity of the silicate melt. For centimetre-sized iron droplets ($r \sim 0.01$ m) in a low-viscosity magma ocean ($\mu \sim 0.1$ Pa s, $g \sim 5$ m s$^{-2}$ for an Earth-sized body during formation), this gives $v_{\mathrm{Stokes}} \sim 4$ m s$^{-1}$. At this rate, droplets could traverse a magma ocean thousands of kilometres deep in a matter of **days** — geologically instantaneous {cite:p}`Rubie2015`.

### The Moon-forming giant impact

The last major episode of melting and core formation on Earth was the **Moon-forming giant impact**, in which a Mars-sized body (often called Theia) collided with the proto-Earth approximately 4.5 billion years ago. This event was energetic enough to re-melt most of Earth's mantle (and vaporise parts of it), creating a final deep magma ocean from which the present-day core–mantle structure was established. The debris from the impact formed a disk around Earth that subsequently accreted to form the Moon.

```{figure} figures/planetary_differentiation.svg
:name: fig:planetary-differentiation
:width: 500px
:align: center

Differentiation of a terrestrial planet. Initially homogeneous accreted material (left) melts due to accretional and radiogenic heating, allowing dense metallic iron to sink and form a core while lighter silicates rise to form the mantle and crust (right). This process occurs rapidly once widespread melting begins. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```


## Core formation

The chemical consequences of core formation are profound: the separation of metal from silicate partitions the elements between the core and mantle according to their geochemical affinities.

### Goldschmidt classification

The geochemist Victor Goldschmidt classified elements into four categories based on their preferential association with different phases in a differentiating planet:

| Classification | Affinity | Examples |
|---------------|----------|----------|
| **Siderophile** ("iron-loving") | Metallic phase (core) | Fe, Ni, Co, W, Mo, Pt, Au, Ir |
| **Lithophile** ("rock-loving") | Silicate/oxide phase (mantle, crust) | Si, Mg, Al, Ca, Na, K, U, Th, Hf, rare earths |
| **Chalcophile** ("sulfur-loving") | Sulfide phase | Cu, Zn, Pb, S, Se, Ag |
| **Atmophile** ("atmosphere-loving") | Gas/volatile phase | H, C, N, O, noble gases |

This classification is not absolute — an element's behaviour depends on the pressure, temperature, and oxygen fugacity during metal–silicate equilibration. For example, silicon is predominantly lithophile under present-day Earth conditions but becomes increasingly siderophile at very high pressures, which is why Earth's core likely contains several weight percent silicon {cite:p}`Rubie2015`.

```{figure} figures/goldschmidt_classification.svg
:name: fig:goldschmidt
:width: 600px
:align: center

Periodic table coloured by Goldschmidt classification: siderophile (iron-loving), lithophile (rock-loving), chalcophile (sulfur-loving), and atmophile (atmosphere-loving) elements. The classification reflects the preferential partitioning of elements during core–mantle differentiation. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

### Partition coefficients

The degree to which a siderophile element partitions into the metal phase is quantified by the **metal–silicate partition coefficient**:

$$
D_i^{\mathrm{met/sil}} = \frac{C_i^{\mathrm{metal}}}{C_i^{\mathrm{silicate}}}
$$ (eq:partition-coefficient)

where $C_i^{\mathrm{metal}}$ and $C_i^{\mathrm{silicate}}$ are the concentrations of element $i$ in the metallic and silicate phases, respectively. A strongly siderophile element like iridium (Ir) has $D^{\mathrm{met/sil}} \sim 10^4$–$10^6$, meaning it overwhelmingly partitions into the core. The measured depletion of siderophile elements in Earth's mantle — Ir is depleted by a factor of $\sim 1000$ relative to chondritic abundances — is among the strongest pieces of evidence that Earth underwent core formation {cite:p}`Rubie2015`.

Partition coefficients depend strongly on **pressure**, **temperature**, and **oxygen fugacity** ($f_{\mathrm{O_2}}$). The high-pressure conditions at the base of a deep magma ocean (40–60 GPa) significantly change the partitioning behaviour of many elements. This is an active area of experimental geochemistry: by reproducing deep magma ocean conditions in the laboratory, researchers can constrain the pressure–temperature conditions under which Earth's core formed.

### Hf–W chronometry: timing core formation

The most powerful tool for dating core formation is the **hafnium–tungsten** (Hf–W) isotopic system. The short-lived isotope ${}^{182}\mathrm{Hf}$ decays to ${}^{182}\mathrm{W}$ with a half-life of only 8.9 million years. Crucially, hafnium is **lithophile** (stays in the mantle) while tungsten is **moderately siderophile** (extracted into the core). This means:

- If core formation occurs **early** (while ${}^{182}\mathrm{Hf}$ is still alive), the Hf stays in the mantle and continues to produce ${}^{182}\mathrm{W}$ there, while the W already extracted into the core is no longer replenished. The mantle ends up with an **excess** of ${}^{182}\mathrm{W}$ relative to chondritic meteorites (which never differentiated).

- If core formation occurs **late** (after ${}^{182}\mathrm{Hf}$ has fully decayed), all the ${}^{182}\mathrm{W}$ has already been produced and is distributed uniformly. The mantle would have a chondritic ${}^{182}\mathrm{W}$ abundance — no excess.

The magnitude of the ${}^{182}\mathrm{W}$ excess in a planet's mantle, expressed as $\varepsilon^{182}\mathrm{W}$ (parts per 10,000 deviation from chondritic), therefore acts as a **clock** for core formation {cite:p}`Kleine2009`:

- **Earth:** $\varepsilon^{182}\mathrm{W} \approx +2$ — indicating that the bulk of core formation was completed within approximately **30–60 Myr** after solar system formation.
- **Mars:** $\varepsilon^{182}\mathrm{W} \approx +3$ to $+5$ — a larger excess indicating earlier and more rapid core formation, within approximately **10–20 Myr**. This is consistent with Mars being a smaller body that completed its accretion faster.
- **Moon:** The Moon's $\varepsilon^{182}\mathrm{W}$ is close to Earth's, consistent with formation from debris of the giant impact.


## Mantle differentiation

Core formation is not the end of chemical differentiation. As the magma ocean cools and crystallises, it produces further chemical layering within the silicate mantle itself.

### Magma ocean crystallisation

As the magma ocean loses heat (primarily by radiation from its surface), it begins to solidify. In a deep magma ocean, crystallisation starts at the **base** — where pressure raises the melting point above the local temperature — and progresses upward {cite:p}`ElkinsTanton2012`. The first minerals to crystallise from the deep magma ocean are high-pressure phases: **bridgmanite** (Mg-perovskite, $\mathrm{MgSiO_3}$) in the lower mantle, followed by **olivine** ($\mathrm{(Mg,Fe)_2SiO_4}$) and other phases at shallower depths as the magma ocean solidifies from the bottom up.

### Incompatible element enrichment

During crystallisation, elements that do not fit easily into the crystal lattice of the solidifying minerals — so-called **incompatible elements** — are progressively concentrated in the remaining liquid. The most important incompatible elements include the heat-producing isotopes uranium (U), thorium (Th), and potassium (K), which were introduced in {ref}`lecture03` as the sources of long-lived radiogenic heating.

As crystallisation proceeds, these incompatible elements are squeezed into an ever-smaller volume of residual liquid, which eventually solidifies to form the **crust**. This is why the continental crust is enriched in U, Th, and K by a factor of $\sim$50–100 relative to the upper mantle, and why roughly half of Earth's radiogenic heat is produced in the thin crustal layer despite it representing less than 1% of Earth's mass.

### Mantle reservoirs

The crystallisation of a magma ocean does not produce a perfectly homogeneous mantle. Instead, it creates compositionally distinct **mantle reservoirs** that persist to the present day:

- **Depleted MORB mantle (DMM):** The upper mantle source of mid-ocean ridge basalts (MORBs) has been depleted in incompatible elements by billions of years of partial melting and crustal extraction. This is the most voluminous mantle reservoir.

- **Enriched mantle:** Deep mantle plumes that produce ocean island basalts (OIBs, e.g., Hawaii, Iceland) sample reservoirs that are enriched in incompatible elements — possibly representing less-processed primordial mantle material or recycled oceanic crust.

### The lunar magma ocean

The Moon provides the clearest example of magma ocean crystallisation. The Moon's **anorthositic crust** — a layer of light-coloured, feldspar-rich rock — is thought to have formed by flotation of low-density plagioclase crystals on top of the lunar magma ocean. Beneath the crust lies a layer enriched in **KREEP** (potassium, rare earth elements, and phosphorus) — the last residual liquid to crystallise, concentrated in incompatible elements just as the theory predicts {cite:p}`ElkinsTanton2012`.


## Volatile delivery and retention

The chemical differentiation discussed so far concerns the refractory (high-temperature) components of planets. But the **volatile elements** — hydrogen, carbon, nitrogen, sulfur, and the noble gases — are equally important, because they form the raw materials for atmospheres, oceans, and ultimately life.

### The classical view and its revision

The classical picture of volatile delivery held a simple dichotomy: the inner solar system formed **hot and dry** (inside the snow line at $\sim$2–3 AU), while volatile-rich material was confined to the outer solar system. Water and other volatiles were then delivered to the terrestrial planets *late*, primarily by carbonaceous chondrite-like bodies scattered inward from the outer asteroid belt or beyond.

Recent work has substantially revised this picture. Several independent lines of evidence now indicate that **volatile-bearing material was present in the inner solar system from early times**:

- {cite:p}`Alexander2019a` and {cite:p}`Alexander2019b` showed through quantitative models of elemental and isotopic fractionations that **all chondrite groups** — including non-carbonaceous (ordinary, enstatite) chondrites traditionally associated with the dry inner disk — accreted water ice. This implies that even inner solar system planetesimals formed at temperatures below the snow line ($\sim$150–170 K) or incorporated icy material, challenging the simple "dry inner / wet outer" paradigm.

- {cite:p}`Lichtenberg2021` demonstrated that the migration of the **snow line** during the protoplanetary disk's evolution, combined with Jupiter's growth to pebble-isolation mass, created a **bifurcation** in planetesimal populations. Early-formed planetesimals accreted ice-rich material regardless of their formation location, while late-formed inner disk planetesimals were desiccated after Jupiter blocked the inward drift of icy pebbles. This mechanism explains both the non-carbonaceous/carbonaceous (NC–CC) isotopic dichotomy observed in meteorites and the volatile gradient across the inner solar system.

- {cite:p}`Grewal2019` and {cite:p}`Grewal2021` used isotopic evidence for carbon, nitrogen, and sulfur to show that volatile delivery to Earth involved contributions from both inner (enstatite-like) and outer (carbonaceous) reservoirs. Nitrogen isotopes reveal that inner and outer solar system protoplanets accreted from **isotopically distinct** nitrogen reservoirs very early, implying that volatile budgets were largely set during primary accretion rather than solely by a late veneer of carbonaceous material.

These findings suggest that the volatile inventory of terrestrial planets is determined by a complex interplay of disk thermal evolution, giant planet formation timing, and the mixing of multiple source reservoirs {cite:p}`Krijt2023`.

### Outgassing from the magma ocean

Regardless of how volatiles were delivered, much of a planet's initial volatile budget is dissolved in the silicate magma ocean. As the magma ocean cools and crystallises, dissolved volatiles are released to form a **secondary atmosphere** through **outgassing** {cite:p}`Hirschmann2012`.

The speciation of the outgassed atmosphere depends critically on the **oxygen fugacity** of the magma:

- Under **reducing** conditions (low $f_{\mathrm{O_2}}$): the dominant outgassed species are $\mathrm{H_2}$, CO, and $\mathrm{N_2}$
- Under **oxidising** conditions (high $f_{\mathrm{O_2}}$, like present-day Earth): the dominant species are $\mathrm{H_2O}$, $\mathrm{CO_2}$, and $\mathrm{N_2}$

The solubility of water in silicate melt follows a square-root law:

$$
X_{\mathrm{H_2O}} \propto p_{\mathrm{H_2O}}^{1/2}
$$ (eq:water-solubility)

where $X_{\mathrm{H_2O}}$ is the mole fraction of dissolved water and $p_{\mathrm{H_2O}}$ is the partial pressure of water vapour above the melt. This means that as the atmosphere thickens with outgassed $\mathrm{H_2O}$, the magma ocean can retain an increasing fraction of its water in solution — a self-limiting feedback that determines the partitioning of water between the interior and the atmosphere {cite:p}`Hirschmann2012`.

### Impact erosion versus delivery

Giant impacts deliver volatiles but can also **strip** them away. A sufficiently energetic impact can eject a significant fraction of a planet's atmosphere and even erode surface volatiles. The net effect depends on the size, velocity, and angle of impact: small, frequent impacts tend to deliver more volatiles than they remove, while rare giant impacts can be net erosive. The balance between delivery and erosion is a key uncertainty in reconstructing the volatile histories of the terrestrial planets.

We will return to the fate of these outgassed atmospheres — their composition, structure, and long-term evolution — in {ref}`lecture05` and {ref}`lecture06`.


## Planetary magnetic fields and dynamo theory

The differentiation of a planet into a metallic core and silicate mantle sets the stage for one of the most important geophysical phenomena: the generation of a planetary **magnetic field** by dynamo action in the liquid metallic core.

### Why magnetic fields matter

Planetary magnetic fields play several critical roles:

- **Atmospheric shielding:** A global magnetic field deflects the charged particles of the solar wind, reducing atmospheric erosion by sputtering and ion pickup. Mars, which lost its global field $\sim$4 Gyr ago, has since lost much of its atmosphere ({ref}`lecture10`).
- **Surface habitability:** By deflecting energetic particles, magnetic fields reduce the radiation dose at a planet's surface — potentially important for the survival of surface life.
- **Geological record:** Magnetic minerals in rocks record the direction and intensity of the ambient field when they cool through their Curie temperature, providing a "tape recorder" of magnetic field history (paleomagnetism).
- **Interior probe:** The existence, strength, and morphology of a magnetic field provide direct constraints on the physical state, composition, and dynamics of a planet's deep interior.

### The induction equation

The generation and evolution of magnetic fields in a conducting fluid is governed by the **magnetic induction equation**, derived from Maxwell's equations combined with Ohm's law:

$$
\pdv{\vec{B}}{t} = \nabla \times (\vec{v} \times \vec{B}) + \eta \nabla^2 \vec{B}
$$ (eq:induction-equation)

where $\vec{B}$ is the magnetic field, $\vec{v}$ is the fluid velocity, and $\eta$ is the **magnetic diffusivity**:

$$
\eta = \frac{1}{\mu_0 \sigma}
$$ (eq:magnetic-diffusivity)

with $\mu_0 = 4\pi \times 10^{-7}$ H m$^{-1}$ (permeability of free space) and $\sigma$ the electrical conductivity of the fluid.

The induction equation contains two competing terms {cite:p}`Roberts2013`:

1. **Advection term** $\nabla \times (\vec{v} \times \vec{B})$: fluid motions stretch, compress, and twist magnetic field lines, amplifying the field. This term creates new magnetic flux.

2. **Diffusion term** $\eta \nabla^2 \vec{B}$: ohmic resistance causes magnetic field lines to diffuse through the fluid and decay. This term destroys magnetic flux.

The balance between these two terms determines whether a magnetic field can be sustained.

### Requirements for dynamo action

For a self-sustaining dynamo — one that can generate and maintain a magnetic field against ohmic decay — three conditions must be met:

1. **An electrically conducting fluid:** The core must contain a fluid with sufficient electrical conductivity ($\sigma$) to carry the currents that generate the field. In terrestrial planets, this is liquid iron (alloyed with lighter elements like S, Si, O). In gas giants, it is metallic hydrogen.

2. **Convection:** The fluid must be in vigorous motion. In planetary cores, this convection is driven by thermal buoyancy (the core is hotter than the overlying mantle) and/or compositional buoyancy (crystallisation of the inner core releases light elements that rise).

3. **Sufficient flow vigour:** The fluid motions must be fast enough, and occur on large enough scales, that advection dominates over diffusion. This criterion is quantified by the **magnetic Reynolds number** $\mathrm{Rm}$, which must exceed a critical value $\mathrm{Rm}_c \sim 10$–$100$.

```{figure} figures/geodynamo_schematic.svg
:name: fig:geodynamo-schematic
:width: 450px
:align: center

Schematic of the geodynamo mechanism. Convective motions in the electrically conducting liquid outer core stretch and twist magnetic field lines, generating Earth's predominantly dipolar magnetic field. The Coriolis force organises the flow into columnar structures aligned with the rotation axis. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```


## Blackboard derivation: The magnetic Reynolds number

```{admonition} Blackboard derivation: The magnetic Reynolds number $\mathrm{Rm}$
:class: tip

**Goal:** Derive the magnetic Reynolds number $\mathrm{Rm} = UL/\eta$ from the induction equation by dimensional analysis, and estimate $\mathrm{Rm}$ for Earth's outer core to demonstrate that advection dominates over diffusion — the fundamental criterion for dynamo action.

**Setup.**

We start from the magnetic induction equation derived in the previous section (Eq. {eq}`eq:induction-equation`):

$$
\pdv{\vec{B}}{t} = \underbrace{\nabla \times (\vec{v} \times \vec{B})}_{\text{advection}} + \underbrace{\eta \nabla^2 \vec{B}}_{\text{diffusion}}
$$

We want to determine which term dominates for a given flow. If advection wins, the flow can amplify magnetic field; if diffusion wins, any field decays away.

**Derivation.**

We use **dimensional analysis** to estimate the magnitude of each term. Let $U$ be a characteristic flow velocity, $L$ a characteristic length scale, and $B$ the field strength.

**Advection term:**

$$
|\nabla \times (\vec{v} \times \vec{B})| \sim \frac{UB}{L}
$$

since the curl introduces a factor of $1/L$ and the cross product introduces a factor of $UB$.

**Diffusion term:**

$$
|\eta \nabla^2 \vec{B}| \sim \frac{\eta B}{L^2}
$$

since each spatial derivative introduces a factor of $1/L$, and $\nabla^2$ involves two spatial derivatives.

The ratio of the advection term to the diffusion term defines the **magnetic Reynolds number**:

$$
\mathrm{Rm} = \frac{|{\text{advection}}|}{|{\text{diffusion}}|} = \frac{UB/L}{\eta B/L^2}
$$

Notice that the magnetic field strength $B$ **cancels** — this is an important result. The magnetic Reynolds number is a property of the **flow**, not of the field:

$$
\boxed{\mathrm{Rm} = \frac{UL}{\eta}}
$$ (eq:magnetic-reynolds)

When $\mathrm{Rm} \gg 1$, advection dominates: the magnetic field is "frozen in" to the fluid and carried along with the flow. When $\mathrm{Rm} \ll 1$, diffusion dominates: the field decays regardless of the flow.

For a self-sustaining dynamo, numerical simulations and theory indicate that the critical value is $\mathrm{Rm}_c \sim 10$–$100$, depending on the flow geometry.

**Application: Earth's outer core.**

For Earth's outer core, the relevant parameters are {cite:p}`Schubert2001`:

| Parameter | Symbol | Value |
|-----------|:------:|:-----:|
| Outer core radius | $L$ | $\sim 3.5 \times 10^6$ m |
| Typical flow velocity | $U$ | $\sim 5 \times 10^{-4}$ m s$^{-1}$ |
| Magnetic diffusivity | $\eta$ | $\sim 1$ m$^2$ s$^{-1}$ |

This gives:

$$
\mathrm{Rm}_\oplus = \frac{UL}{\eta} = \frac{5 \times 10^{-4} \times 3.5 \times 10^6}{1} \approx 1750
$$

Since $\mathrm{Rm}_\oplus \approx 1750 \gg \mathrm{Rm}_c$, advection overwhelmingly dominates over diffusion in Earth's outer core. The flow is vigorous enough to sustain dynamo action.

We can also estimate the **ohmic diffusion timescale** — how long the field would take to decay if the flow suddenly stopped:

$$
\tau_{\mathrm{ohm}} \sim \frac{L^2}{\eta} = \frac{(3.5 \times 10^6)^2}{1} \approx 1.2 \times 10^{13} \text{ s} \approx 400{,}000 \text{ yr}
$$

This is much less than Earth's age (4.5 Gyr), confirming that the field cannot be a relic — it must be **continuously regenerated** by dynamo action.

**Note:** Paleomagnetic measurements of ancient rocks show that Earth has had a magnetic field for at least **3.4–3.5 billion years** {cite:p}`Tarduno2010`. This places a strong constraint on the thermal and compositional evolution of the core: the convective driving mechanism must have been sustained over most of Earth's history.
```


## Earth's geodynamo

With the theoretical framework established, we now examine how the dynamo operates in Earth's core.

### Core structure

Earth's core extends from the centre of the planet to a depth of 2890 km (the core–mantle boundary). It comprises two distinct regions:

- **Inner core** (radius 0–1220 km): Solid iron–nickel alloy. The inner core is slowly growing as the outer core cools and crystallises at the inner core boundary.

- **Outer core** (radius 1220–3480 km from the centre, or depth 2890–5150 km): Liquid iron alloy. The outer core is about 5–10% less dense than pure liquid iron, indicating the presence of dissolved light elements (S, Si, O, C, H). This is the region where the geodynamo operates.

### Driving mechanisms

Convection in the outer core is driven by two sources of buoyancy {cite:p}`Roberts2013`:

1. **Thermal convection:** The core is hotter than the overlying mantle, so heat flows outward. As the core cools, the temperature drop drives thermal buoyancy.

2. **Compositional convection:** As the inner core crystallises, it preferentially incorporates iron and rejects light elements (S, Si, O) into the liquid outer core. This light, buoyant fluid rises, providing a powerful source of convection. The latent heat released by crystallisation further contributes to thermal buoyancy.

Compositional convection is thought to be the dominant driver of the present-day geodynamo. The growth of the inner core — currently at a rate of about 0.5 mm per year — provides a steady supply of both compositional buoyancy and latent heat.

### Field morphology

Earth's magnetic field at the surface is predominantly **dipolar** — resembling the field of a bar magnet — with the dipole axis tilted approximately 11° from the rotation axis. The surface field strength ranges from about 25 $\mu$T near the equator to about 65 $\mu$T near the poles, with a mean of about 45 $\mu$T.

### Secular variation

The magnetic field is not static. It varies on timescales from years to millions of years:

- **Secular variation:** The field changes measurably on decadal to century timescales. The non-dipole components of the field drift, grow, and decay, reflecting the turbulent flow in the outer core.

- **South Atlantic Anomaly:** A region of anomalously weak field strength over the South Atlantic, where the field is about 30% weaker than the global average at that latitude. This is the surface expression of a reversed-flux patch at the core–mantle boundary.

- **Westward drift:** Many features of the non-dipole field drift westward at roughly 0.2° per year, consistent with a differential rotation between the outer core and the mantle.

### Polarity reversals

On longer timescales, the geomagnetic field undergoes **polarity reversals** — the north and south magnetic poles swap. Key facts about reversals:

- The current reversal rate is roughly **4–5 reversals per million years**, though this rate has varied significantly over geological time.
- A reversal takes approximately **1000–10,000 years** to complete, during which the field weakens, becomes complex (multipolar), and re-establishes in the opposite polarity.
- During the Cretaceous Normal Superchron (~84–124 Ma), the field maintained a single polarity for about 40 million years.

The most compelling evidence for reversals comes from **magnetic stripes** on the ocean floor: as new oceanic crust forms at mid-ocean ridges, the magnetic minerals record the ambient field direction. The result is a symmetric pattern of normally and reversely magnetised stripes on either side of the ridge — a key piece of evidence for both seafloor spreading and geomagnetic reversals {cite:p}`Tarduno2010`.

```{figure} figures/geomagnetic_polarity_timescale.svg
:name: fig:geomagnetic-polarity
:width: 500px
:align: center

Geomagnetic polarity timescale showing normal (black) and reversed (white) polarity intervals over the past 169 million years. The pattern of reversals is irregular and unpredictable, reflecting the chaotic dynamics of the geodynamo. The Cretaceous Normal Superchron (a prolonged interval of constant polarity) is visible in the right portion of the timescale. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```


## Comparative magnetospheres

Magnetic fields vary enormously across the solar system. Comparing them reveals how dynamo action depends on a planet's size, composition, thermal state, and rotational dynamics.

### Magnetic field comparison

| Body | Field type | Surface field | Dipole moment (relative to Earth) | Notes |
|------|-----------|:---:|:---:|-------|
| **Earth** | Active dynamo | 25–65 $\mu$T | 1 | Liquid Fe outer core, growing inner core |
| **Mercury** | Active dynamo | ~0.3 $\mu$T | $\sim 5 \times 10^{-4}$ | Weak; thin liquid shell {cite:p}`Anderson2012` |
| **Venus** | None detected | $< 0.01$ $\mu$T | $< 10^{-5}$ | No dynamo despite large iron core |
| **Mars** | Remnant crustal | Up to ~1500 nT | — | Dynamo died ~4.1 Ga {cite:p}`Acuna1999` |
| **Jupiter** | Active dynamo | ~400–1400 $\mu$T | $\sim 20{,}000$ | Metallic H dynamo {cite:p}`Connerney2022` |
| **Saturn** | Active dynamo | ~20 $\mu$T | ~600 | Remarkably axisymmetric |
| **Ganymede** | Active dynamo | ~0.7 $\mu$T | $\sim 1.5 \times 10^{-3}$ | Only moon with intrinsic dynamo |

### Mercury

Mercury possesses a weak but **active** dynamo — its surface field is only about 1% of Earth's. The MESSENGER mission revealed that Mercury's field is strongly offset northward from the planet's centre, suggesting an unusual dynamo geometry. Mercury's liquid outer core shell is thought to be relatively thin (perhaps only a few hundred kilometres), which limits the vigour of convection and the resulting field strength {cite:p}`Anderson2012`.

### Venus

Venus presents a puzzle: it is nearly identical to Earth in size and bulk composition, and should have a liquid iron core, yet it has **no detected magnetic field**. Several explanations have been proposed:

- **Slow rotation:** Venus rotates extremely slowly (243-day period), but numerical dynamo simulations show that slow rotation alone does not prevent dynamo action.
- **No inner core:** If Venus's core is entirely liquid (no solid inner core has nucleated), then compositional convection — the dominant driver of Earth's dynamo — would be absent. Thermal convection alone may be insufficient.
- **Stagnant lid tectonics:** Without plate tectonics, the mantle may not extract heat from the core efficiently enough to drive vigorous core convection.

The relative importance of these factors remains debated. Venus's lack of a magnetic field likely reflects a combination of reduced core cooling (due to stagnant lid tectonics insulating the core) and potentially the absence of an inner core {cite:p}`dePaterLissauer2010`.

### Mars

Mars has no global magnetic field today, but the Mars Global Surveyor spacecraft discovered intense **remnant crustal magnetism** in the ancient southern highlands — patches of magnetisation with surface field strengths up to $\sim$1500 nT, far stronger than crustal magnetisation on Earth {cite:p}`Acuna1999`. These crustal magnetic anomalies are absent in the younger northern lowlands and in large impact basins (Hellas, Argyre, Isidis), indicating that:

1. Mars once had an active dynamo that magnetised the ancient crust.
2. The dynamo shut down approximately **4.1 Gyr ago** (before the large basins formed), after which newly formed crust was not magnetised.
3. The loss of the global magnetic field left Mars's atmosphere unshielded against solar wind erosion — likely contributing to the dramatic atmospheric loss that transformed Mars from a warmer, wetter world to the cold, thin-atmosphere planet we see today (see {ref}`lecture10`).

```{figure} figures/mars_crustal_magnetism.avif
:name: fig:mars-crustal-magnetism
:width: 550px
:align: center

Global map of Mars's crustal magnetic field from the Mars Global Surveyor (MGS) MAG/ER experiment. Red and blue regions indicate strong crustal magnetisation in opposite polarities, concentrated in the ancient southern highlands. The younger northern lowlands and large impact basins (Hellas, Argyre) show little to no magnetisation, indicating the dynamo had ceased before these features formed {cite:p}`Acuna1999`. Credit: NASA/Goddard Space Flight Center, public domain.
```

### Jupiter

Jupiter has the **strongest magnetic field** of any planet — roughly 20,000 times Earth's dipole moment. The field is generated by convection in Jupiter's deep interior, where hydrogen is compressed to a metallic state (at pressures above $\sim$100 GPa, hydrogen becomes an electrical conductor). The Juno mission has mapped Jupiter's magnetic field in unprecedented detail, revealing a surprisingly complex and asymmetric field at the surface, with a concentrated magnetic flux patch in the northern hemisphere — the "Great Blue Spot" {cite:p}`Connerney2022`.

### Ganymede

Jupiter's largest moon Ganymede is the only moon in the solar system with its own **intrinsic dynamo**. Its surface field of $\sim$0.7 $\mu$T implies a small but actively convecting liquid iron core. The existence of Ganymede's dynamo is surprising given the moon's small size and is not yet fully understood — it may be sustained by tidal heating or compositional convection from a freezing core {cite:p}`dePaterLissauer2010`.


## Magnetosphere–solar wind interaction

A planetary magnetic field does not exist in isolation — it interacts dynamically with the **solar wind**, the continuous stream of charged particles (mostly protons and electrons) flowing outward from the Sun at speeds of 300–800 km s$^{-1}$, carrying an embedded magnetic field (the interplanetary magnetic field, or IMF) {cite:p}`Kivelson1995`.

### Magnetopause standoff distance

The boundary between the planetary magnetic field and the solar wind is the **magnetopause**. Its distance is determined by pressure balance between the solar wind dynamic pressure and the magnetic pressure of the planet's field:

$$
\frac{1}{2} \rho_{\mathrm{sw}} v_{\mathrm{sw}}^2 = \frac{B_{\mathrm{mp}}^2}{2\mu_0}
$$ (eq:magnetopause-pressure)

where $\rho_{\mathrm{sw}}$ and $v_{\mathrm{sw}}$ are the solar wind density and velocity, and $B_{\mathrm{mp}}$ is the magnetic field strength at the magnetopause. For a dipole field ($B \propto r^{-3}$), this yields a **standoff distance** of approximately:

$$
r_{\mathrm{mp}} \approx 10 \, R_\oplus
$$ (eq:magnetopause-distance)

for Earth under typical solar wind conditions.

### Magnetosphere structure

The interaction between the solar wind and the planetary field creates a complex structure {cite:p}`Kivelson1995`:

- **Bow shock:** The supersonic solar wind is decelerated to subsonic speeds at the bow shock, located roughly 3 $R_\oplus$ upstream of the magnetopause. This is analogous to the shock wave in front of a supersonic aircraft.

- **Magnetosheath:** The shocked, heated solar wind plasma flows around the magnetopause in this turbulent region between the bow shock and magnetopause.

- **Magnetotail:** On the night side, the magnetic field is stretched into a long tail extending more than 200 $R_\oplus$ downstream, where magnetic reconnection events release energy and accelerate particles.

- **Plasmasphere:** A torus of cool, dense plasma trapped on closed magnetic field lines in the inner magnetosphere, co-rotating with Earth.

```{figure} figures/magnetosphere_structure.svg
:name: fig:magnetosphere
:width: 600px
:align: center

Structure of Earth's magnetosphere, showing the bow shock, magnetopause, magnetosheath, magnetotail, and Van Allen radiation belts. The solar wind (arriving from the left) is deflected around the magnetopause, while the magnetic field is compressed on the dayside and stretched into a long tail on the nightside. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

### Auroral processes

When solar wind particles enter the magnetosphere — primarily through reconnection events in the magnetotail — they are channelled along magnetic field lines toward the polar regions. As these energetic particles (mostly electrons) plunge into the upper atmosphere, they collide with atmospheric atoms and molecules, exciting them to emit light. This is the **aurora** (aurora borealis in the north, aurora australis in the south) {cite:p}`Kivelson1995`:

- **Green light** (557.7 nm): Excited atomic oxygen, O, at altitudes of ~100–200 km
- **Red light** (630.0 nm): Excited atomic oxygen at higher altitudes (~200–400 km)
- **Blue/violet light**: Excited molecular nitrogen, $\mathrm{N_2}$, at lower altitudes

Aurorae are observed on other magnetised planets as well — Jupiter's aurorae, powered by its enormous magnetosphere and the volcanic output of Io, are among the most luminous in the solar system.

```{figure} figures/aurora.avif
:name: fig:aurora
:width: 550px
:align: center

The aurora australis (southern lights) photographed from the International Space Station. Charged particles from the solar wind, channelled along Earth's magnetic field lines into the polar regions, excite atmospheric oxygen and nitrogen to produce the characteristic green and red glow. Credit: NASA/ISS Crew Earth Observations, public domain.
```

### Van Allen radiation belts

Earth's magnetosphere traps energetic charged particles in two toroidal regions known as the **Van Allen radiation belts** {cite:p}`dePaterLissauer2010`:

- **Inner belt** (centred at $\sim 1.5 \, R_\oplus$): Primarily energetic protons (10–100 MeV), produced by the decay of neutrons created in cosmic ray collisions with the atmosphere.
- **Outer belt** (centred at $\sim 4$–$5 \, R_\oplus$): Primarily energetic electrons (0.1–10 MeV), injected during geomagnetic storms and accelerated by wave–particle interactions.

The radiation belts pose a hazard to spacecraft electronics and to astronauts. They also demonstrate the double-edged nature of magnetic fields: while the magnetosphere shields the surface from the bulk of the solar wind, it also traps a population of highly energetic particles that would not be present without the field.


## Recent advances

NASA's Juno mission has produced the most detailed map of Jupiter's magnetic field to date {cite:p}`Connerney2022`. The data reveal a surprisingly complex field morphology: in the northern hemisphere, the field shows strong non-dipolar features, including a localised patch of reversed polarity (the "Great Blue Spot") that may reflect the dynamics of a deep-seated dynamo operating in the metallic hydrogen layer ({ref}`lecture08`). These measurements provide direct constraints on the depth and nature of convection driving Jupiter's dynamo.

ESA/JAXA's **BepiColombo** mission has completed multiple Mercury flybys en route to orbital insertion, providing new measurements of Mercury's magnetosphere. Preliminary data confirm Mercury's weak but active dipolar field and have revealed unexpected features in the magnetospheric structure, including the role of sodium ions in magnetospheric dynamics {cite:p}`Anderson2012`.

ESA's **JUICE** mission, en route to the Jupiter system, will conduct the first detailed investigation of Ganymede's intrinsic magnetic field — the only moon in the solar system known to generate its own dynamo. Understanding how a body as small as Ganymede ($R = 2634$ km) maintains an active dynamo remains an open question in planetary magnetism, with implications for the thermal state and composition of its iron core.


## References

```{bibliography}
:filter: docname in docnames
```
