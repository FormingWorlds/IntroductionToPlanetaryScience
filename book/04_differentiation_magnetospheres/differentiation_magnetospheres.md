(lecture04)=
# Chemical Differentiation & Magnetospheres

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to explain the processes of core formation and mantle differentiation, describe the requirements for planetary dynamo action, and compare magnetic field properties across the solar system.
```

```{seealso}
**Slides:** [Download Lecture 4 (PDF)](../_static/slides/lecture04.pdf)
```

## Accretion and early melting

In {ref}`Lecture 3 <lecture03>` we showed that the gravitational energy released during accretion is more than sufficient to melt an Earth-mass body, producing a global **magma ocean**. We also saw that gravitational differentiation, the sinking of dense iron toward the centre, releases additional energy that helps sustain this molten state. In this lecture we explore the *chemical* consequences of that melting: how a once-homogeneous ball of rock and metal separates into the layered structure (core, mantle, crust) that we observe in the terrestrial planets today.

### Metal–silicate separation

When a growing planet reaches a sufficient size (roughly Moon-sized or larger), accretional heating and the decay of short-lived isotopes like ${}^{26}\mathrm{Al}$ ({ref}`Lecture 3 <lecture03>`) produce widespread melting. In the resulting magma ocean, **metallic iron** (density $\sim 7000$ kg m$^{-3}$) is immiscible with **silicate melt** (density $\sim 3000$ kg m$^{-3}$). Iron droplets settle through the silicate liquid under gravity, eventually accumulating at the centre to form a metallic core {cite:p}`Lichtenberg2023`.

The settling velocity of iron droplets in a silicate magma ocean can be estimated using **Stokes' law** for the terminal velocity of a sphere falling through a viscous fluid:

$$
v_{\mathrm{Stokes}} = \frac{2}{9} \frac{\Delta\rho \, g \, r^2}{\mu}
$$ (eq:stokes-settling)

where $\Delta\rho \approx 4000$ kg m$^{-3}$ is the density contrast between metal and silicate, $g$ is the gravitational acceleration, $r$ is the droplet radius, and $\mu$ is the dynamic viscosity of the silicate melt. For centimetre-sized iron droplets ($r \sim 0.01$ m) in a low-viscosity magma ocean ($\mu \sim 0.1$ Pa s, $g \sim 5$ m s$^{-2}$ for an Earth-sized body during formation), this gives $v_{\mathrm{Stokes}} \sim 4$ m s$^{-1}$. Strictly, Stokes' law holds only while the flow around the droplet stays laminar, which for these parameters requires droplet radii below roughly a millimetre; centimetre-sized droplets settle turbulently at roughly $0.5$ m s$^{-1}$ instead {cite:p}`Rubie2003`. Either way, droplets traverse a magma ocean thousands of kilometres deep within days to weeks, geologically instantaneous {cite:p}`Rubie2015`.

```{figure} figures/stokes_settling.avif
:name: fig:stokes-settling
:width: 550px
:align: center

Stokes settling velocity for an iron droplet in a low-viscosity silicate magma ocean as a function of droplet radius (Eq. {eq}`eq:stokes-settling`), assuming $\Delta\rho = 4000$ kg m$^{-3}$, $g = 5$ m s$^{-2}$, and $\mu = 0.1$ Pa s. The Stokes curve gives $\sim 4$ m s$^{-1}$ for centimetre-sized droplets; submillimetre droplets are far slower and are more likely to remain suspended by convection. The dashed vertical line marks the laminar limit ($\mathrm{Re} \approx 1$, near $r \approx 0.7$ mm): to its right the flow around the droplet is turbulent and the Stokes curve is an upper bound, with centimetre droplets actually settling at roughly $0.5$ m s$^{-1}$ {cite:p}`Rubie2003`, so a 1000 km magma ocean is crossed within weeks rather than days. The strong $r^2$ dependence is the central reason that iron-silicate separation is geologically instantaneous once droplets coalesce {cite:p}`Rubie2015`.
```

### The Moon-forming giant impact

The last major episode of melting and core formation on Earth was the **Moon-forming giant impact**, in which a Mars-sized body (often called Theia) collided with the proto-Earth approximately 4.5 billion years ago. This event was energetic enough to re-melt most of Earth's mantle (and vaporise parts of it), creating a final deep magma ocean from which the present-day core–mantle structure was established. The debris from the impact formed a disk around Earth that subsequently accreted to form the Moon. The end result of this differentiation sequence ({numref}`fig:planetary-differentiation`) is a layered planet: an iron core, silicate mantle, and thin crust.

```{figure} figures/planetary_differentiation.svg
:name: fig:planetary-differentiation
:width: 500px
:align: center

Differentiation of a terrestrial planet. Initially homogeneous accreted material (left) melts due to accretional and radiogenic heating, allowing dense metallic iron to sink and form a core while lighter silicates rise to form the mantle and crust (right). This process occurs rapidly once widespread melting begins. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```

### Giant impacts and mantle stripping

Not every giant impact ends with the impactor being fully incorporated into the target, as in the Earth-Moon case. For the appropriate geometry (oblique, high-velocity) and mass ratio, a giant impact can *remove* more silicate mantle than it delivers, leaving behind a body with an anomalously large metallic core relative to its present bulk silicate fraction. This **mantle-stripping** mechanism is the leading explanation for Mercury's highly unusual iron budget, and a candidate explanation for the two most striking large-scale asymmetries in the inner solar system: Mars's hemispheric dichotomy and the basaltic-surface contrast between the lunar near- and far-side.

**Mercury's anomalously large core.** Mercury has a metallic core mass fraction of roughly $65$–$70\%$ (see {ref}`Lecture 8 <lecture08>` and {ref}`Lecture 10 <lecture10>`), compared to $\sim 32\%$ for Earth and $\sim 24\%$ for Mars. This is difficult to produce by condensation chemistry alone under any reasonable protoplanetary-disk thermal model. The leading hypothesis, going back to {cite:t}`Benz1988` and updated with **smoothed-particle hydrodynamics (SPH)** simulations by {cite:t}`Benz2007` ({numref}`fig:benz2007-mercury-impact`; SPH is a mesh-free numerical method in which the fluid is represented by a swarm of Lagrangian "particles" whose density, pressure and velocity are computed by local kernel averaging; it is the standard tool for simulating catastrophic impacts), is that Mercury's protoplanet experienced a **hit-and-run giant impact**: an oblique collision with a differentiated body of comparable mass, moving at several escape velocities, from which a partially disrupted remnant re-accretes rather than being fully absorbed. The impact ejected a disproportionate fraction of Mercury's silicate mantle into heliocentric orbit, some of which re-accreted as a thin silicate veneer while the bulk of it was lost to the Sun or to other protoplanets. The result is a stripped-down mantle with an intact metallic core.

```{figure} figures/benz2007_mercury_impact.avif
:name: fig:benz2007-mercury-impact
:width: 650px
:align: center

Smoothed-particle hydrodynamics (SPH) simulation of a hit-and-run giant impact on proto-Mercury from {cite:t}`Benz2007`. Frames show the pre-impact configuration (top left), the encounter at closest approach with deep tidal disruption of both bodies (top right), and two later stages during which silicate mantle material is preferentially ejected to heliocentric orbit while the iron-rich metallic cores reassemble into a single body (bottom). The final remnant retains essentially its original core mass but loses $\sim 50$–$70\%$ of its pre-impact silicate mantle, yielding the observed Mercury core mass fraction of $\sim 65$–$70\%$. Colour encodes iron (red) vs silicate (blue). Reproduced from {cite:t}`Benz2007`.
```

**Mars's hemispheric dichotomy** ({ref}`Lecture 10 <lecture10>`) describes the $\sim 6$ km elevation difference and $\sim 30$ km crustal-thickness difference between the smooth, young northern lowlands and the ancient, heavily cratered southern highlands. {cite:t}`AndrewsHanna2008` and {cite:t}`Marinova2008` argued that this dichotomy is the relaxed signature of a single **Borealis-scale mega-impact** (a giant impact on the scale of the putative Borealis basin, an elliptical $\sim 10{,}000$ km feature covering most of Mars's northern hemisphere that is the largest single impact structure yet proposed in the solar system) that excavated the northern hemisphere early in Mars's history. In contrast to the Mercury case, the Mars dichotomy impact was not net erosive to the bulk planet: it redistributed crust laterally rather than stripping bulk silicate mass to space.

**Earth-Moon system**. The Moon-forming impact is at the other extreme of the giant-impact mass-ratio spectrum: a Mars-sized impactor delivered most of its mass to Earth, contributed the material that assembled into the Moon, and left Earth with essentially the bulk composition it had before. Earth is thus a *net accretion* outcome of its giant impact, not a net-stripping outcome. Mercury and Earth are the two endpoints of the same underlying process; Mars's dichotomy is an intermediate case where the impact reshaped the surface without substantially modifying the bulk-silicate mass budget.

The giant-impact mantle-stripping framework has two implications that return in later lectures: (i) it naturally explains why Mercury's surface composition is iron- and sulfur-depleted relative to ordinary chondrites and enstatite chondrites (the silicate was stripped before it could be incorporated), and (ii) it places a lower bound on the terminal-bombardment velocity distribution in the inner solar system, which constrains the architecture of giant-planet migration during terrestrial-planet assembly ({ref}`Lecture 2 <lecture02>`).


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

This classification ({numref}`fig:goldschmidt`) is not absolute: an element's behaviour depends on the pressure, temperature, and oxygen fugacity during metal–silicate equilibration. For example, silicon is predominantly lithophile under present-day Earth conditions but becomes increasingly siderophile at very high pressures, which is why Earth's core likely contains several weight percent silicon {cite:p}`Rubie2015`.

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

where $C_i^{\mathrm{metal}}$ and $C_i^{\mathrm{silicate}}$ are the concentrations of element $i$ in the metallic and silicate phases, respectively. A strongly siderophile element like iridium (Ir) has $D^{\mathrm{met/sil}} \sim 10^4$–$10^6$, meaning it overwhelmingly partitions into the core. The measured depletion of siderophile elements in Earth's mantle (Ir is depleted by a factor of $\sim 1000$ relative to chondritic abundances) is among the strongest pieces of evidence that Earth underwent core formation {cite:p}`Rubie2015`.

Partition coefficients depend strongly on **pressure**, **temperature**, and **oxygen fugacity** ($f_{\mathrm{O_2}}$). The high-pressure conditions at the base of a deep magma ocean (40–60 GPa) significantly change the partitioning behaviour of many elements. This is an active area of experimental geochemistry: by reproducing deep magma ocean conditions in the laboratory, researchers can constrain the pressure–temperature conditions under which Earth's core formed.

### Equilibration depth and the P–T–$f_{\mathrm{O_2}}$ dependence

If metal droplets really do equilibrate with silicate liquid all the way down a deep magma ocean before pooling at the base, then the **final** metal composition, and therefore the partitioning of siderophile elements between the final core and the final mantle, is determined by the $(P, T, f_{\mathrm{O_2}})$ conditions reached at the *deepest* equilibration depth. This is the central insight linking high-pressure mineral physics to core-formation chronology {cite:p}`Rubie2015`.

Empirically, partition coefficients follow a **Nernst-type regression** (a standard thermodynamic parameterisation used in experimental geochemistry, analogous to the Nernst equation in electrochemistry) of the form:

$$
\log_{10} D_i^{\mathrm{met/sil}} = a_i + \frac{b_i}{T} + c_i \frac{P}{T} + d_i \cdot \log_{10} f_{\mathrm{O_2}}
$$ (eq:d-parameterisation)

where the coefficients $a_i, b_i, c_i, d_i$ are fit to laboratory experiments at controlled $(P, T, f_{\mathrm{O_2}})$ and the fitting is performed individually for each element $i$. Experimental data show that several moderately siderophile elements (Ni, Co, W, V, Mo, Cr) have $D^\mathrm{met/sil}$ values that **decrease** as pressure increases: at 1 GPa a given element may have $D \sim 10^4$, while at 50 GPa the same element may partition far less strongly into the metal, with $D \sim 10^2$ or less. This pressure dependence is the crux of the argument for deep-magma-ocean equilibration.

The observed **present-day** depletions of siderophile elements in Earth's mantle (for example, Ni depletion is only a factor of $\sim 30$ compared to chondritic, not the factor of $\sim 10^4$ expected from low-pressure partitioning) can only be reproduced if the metal–silicate equilibration took place at pressures of **40–60 GPa** and temperatures of **3000–4000 K**. This corresponds to the base of a magma ocean extending down to roughly half of Earth's mantle depth, i.e. $\sim 1000$–$1500$ km below the proto-surface. That is the sense in which the depleted-siderophile signature of the bulk silicate Earth "remembers" the equilibration depth {cite:p}`Rubie2015`. {numref}`fig:partitioning-pressure` shows the experimental basis for this constraint: partition coefficients for several moderately siderophile elements converge on the BSE depletion level only at pressures of $\sim 40$–$60$ GPa.

```{figure} figures/siebert2013_partition_coefficients.avif
:name: fig:partitioning-pressure
:width: 620px
:align: center

Metal–silicate partition coefficients for moderately siderophile elements (Ni, Co, V, Cr) as a function of pressure, from laboratory metal–silicate equilibration experiments spanning $1$ to $75$ GPa at magma-ocean-relevant temperatures. Coloured curves are fits of the form of Eq. {eq}`eq:d-parameterisation` with $f_{\mathrm{O_2}}$ at 2 log-units below the iron-wüstite (IW) buffer. The horizontal grey band marks the depletion level required to match the present-day bulk silicate Earth (BSE) composition. All four elements converge on that band at pressures near $40$–$60$ GPa, which constrains the equilibration depth during core formation to the base of a $\sim 1000$–$1500$ km deep magma ocean. Redrawn from {cite:t}`Siebert2013`; see also {cite:t}`Rubie2015`.
```

The **oxygen fugacity** $f_{\mathrm{O_2}}$ adds another dimension. It is conventionally quoted relative to the **iron-wüstite (IW) buffer**, a reference redox state defined by the equilibrium $\mathrm{Fe} + \tfrac{1}{2}\mathrm{O_2} \rightleftharpoons \mathrm{FeO}$ that is the redox equivalent of a $\mathrm{pH}$ standard in aqueous chemistry. During Earth's accretion, $f_{\mathrm{O_2}}$ is thought to have evolved from roughly 4–5 log-units below the IW buffer (deeply reducing, in equilibrium with iron metal) to its present mantle value near IW–2 (moderately reducing). Increasing $f_{\mathrm{O_2}}$ oxidises iron from the metal to the silicate, shifts the metal–silicate equilibrium in favour of silicate for most transition metals, and therefore reduces $D^\mathrm{met/sil}$. Self-consistent **continuous accretion models** solve for $(P, T, f_{\mathrm{O_2}})$ as a function of accreted mass and produce the observed present-day siderophile depletions as a natural outcome of a deep, progressively oxidising magma ocean rather than a single late equilibration event {cite:p}`Rubie2015`.

The practical implication for chronology is that the simplified "instantaneous closure" model used for the Hf–W worked example below is not a literal description of the physics: core formation is a continuous process that proceeds in step with accretion. The Hf–W "model age" is the age that one would infer if the whole core-extraction process were compressed into a single event with the same final siderophile depletion pattern. Detailed accretion simulations typically find that this model age is protracted to roughly twice the actual equilibration time of any single droplet, which is why Earth's Hf–W model age is $\sim 30$–$60$ Myr while individual droplets in the deep magma ocean were equilibrating on timescales of days (cf. {numref}`fig:stokes-settling`).

### Hf–W chronometry: timing core formation

The most powerful tool for dating core formation is the **hafnium–tungsten** (Hf–W) isotopic system. The short-lived isotope ${}^{182}\mathrm{Hf}$ decays to ${}^{182}\mathrm{W}$ with a half-life of only 8.9 million years. Crucially, hafnium is **lithophile** (stays in the mantle) while tungsten is **moderately siderophile** (extracted into the core). This means:

- If core formation occurs **early** (while ${}^{182}\mathrm{Hf}$ is still alive), the Hf stays in the mantle and continues to produce ${}^{182}\mathrm{W}$ there, while the W already extracted into the core is no longer replenished. The mantle ends up with an **excess** of ${}^{182}\mathrm{W}$ relative to chondritic meteorites (which never differentiated).

- If core formation occurs **late** (after ${}^{182}\mathrm{Hf}$ has fully decayed), all the ${}^{182}\mathrm{W}$ has already been produced and is distributed uniformly. The mantle would have a chondritic ${}^{182}\mathrm{W}$ abundance, i.e. no excess.

The magnitude of the ${}^{182}\mathrm{W}$ excess in a planet's mantle, expressed as $\varepsilon^{182}\mathrm{W}$ (parts per 10,000 deviation from chondritic), therefore acts as a **clock** for core formation {cite:p}`Kleine2009`:

- **Earth:** $\varepsilon^{182}\mathrm{W} \approx +2$, indicating that the bulk of core formation was completed within approximately **30–60 Myr** after solar system formation.
- **Mars:** the bulk martian mantle has $\varepsilon^{182}\mathrm{W} \approx +0.37 \pm 0.05$, estimated from enriched shergottites, whose source Hf/W ratio is closest to the bulk-mantle value (depleted shergottites can reach $\varepsilon^{182}\mathrm{W} \approx +1.8$). This indicates that Mars accreted within the first $\sim 10$ Myr and completed its magma-ocean crystallisation within $\sim 20$–$25$ Myr, with crust formation following $\sim 15$ Myr later. Mars is consistent with a smaller body that completed its accretion faster than Earth {cite:p}`Kruijer2017Mars`.
- **Moon:** The Moon's $\varepsilon^{182}\mathrm{W}$ is close to Earth's, consistent with formation from debris of the giant impact.

The relative timing of these events across the solar system is summarised in {numref}`fig:hf-w-chronometry`, which places planetesimal core formation, Mars accretion, the Moon-forming giant impact, and Earth's three growth stages on a single logarithmic time-after-CAI axis.

#### Worked example: from $\varepsilon^{182}\mathrm{W}$ to a core-formation age

In the simplest two-stage model, core formation is treated as a single instantaneous event at time $t_c$ after the first solids (calcium-aluminium-rich inclusions, CAIs) condensed at $t = 0$. Before $t_c$ the planet's precursor material is assumed to be chondritic; at $t_c$ the metal instantaneously segregates from the silicate and carries essentially all of the tungsten into the core, leaving the mantle with elevated $\mathrm{Hf/W}$. The residual $^{182}\mathrm{Hf}$ in the mantle then decays in place, producing an excess of $^{182}\mathrm{W}$ that is not diluted by unradiogenic tungsten from the core. Integrating the decay from $t_c$ to today yields:

$$
\varepsilon^{182}\mathrm{W}_\mathrm{BSE} = \mathcal{Q}_\mathrm{W} \cdot \left[\frac{(\mathrm{Hf}/\mathrm{W})_\mathrm{BSE}}{(\mathrm{Hf}/\mathrm{W})_\mathrm{CHUR}} - 1\right] \cdot \left(\frac{{}^{182}\mathrm{Hf}}{{}^{180}\mathrm{Hf}}\right)_{\!\!\!0} \cdot e^{-\lambda t_c}
$$ (eq:hfw-age)

where $\mathcal{Q}_\mathrm{W} \approx 10^4$ is the $\varepsilon$-notation prefactor, $(^{182}\mathrm{Hf}/^{180}\mathrm{Hf})_0 \approx 1.02 \times 10^{-4}$ is the initial hafnium isotopic ratio at CAI formation, and $\lambda = \ln 2 / t_{1/2} = 7.79 \times 10^{-2}$ Myr$^{-1}$ is the $^{182}\mathrm{Hf}$ decay constant ($t_{1/2} = 8.9$ Myr). The bracketed term is the mantle Hf/W enrichment factor: for Earth's bulk silicate mantle ($\mathrm{BSE}$), $(\mathrm{Hf}/\mathrm{W})_\mathrm{BSE}/(\mathrm{Hf}/\mathrm{W})_\mathrm{CHUR} \approx 18$, so the factor in brackets is $\approx 17$.

Plugging in the observed Earth value $\varepsilon^{182}\mathrm{W}_\mathrm{BSE} \approx +2$:

$$
e^{-\lambda t_c} = \frac{2}{10^4 \cdot 17 \cdot 1.02 \times 10^{-4}} \approx 0.115
$$

$$
t_c = -\frac{\ln 0.115}{\lambda} \approx \frac{2.16}{0.0779\ \mathrm{Myr}^{-1}} \approx 28 \text{ Myr}
$$

That is, the simplest instantaneous-closure model yields a core-formation age of $\sim 28$ Myr after CAI formation for Earth, close to the lower end of the $30$–$60$ Myr range quoted above. The $30$–$60$ Myr range reflects more realistic models in which core formation is **protracted** rather than instantaneous, with many small equilibration events accompanying ongoing accretion. The effective "model age" is then longer than the instantaneous-closure result because earlier-extracted tungsten does not fully cease to be replenished. For Mars, applying the same formula with a lower mantle enrichment factor $(\mathrm{Hf}/\mathrm{W})_\mathrm{BSE}/(\mathrm{Hf}/\mathrm{W})_\mathrm{CHUR} \approx 4$ (Mars is more reduced, and its smaller metallic core extracted a smaller fraction of the bulk W) and $\varepsilon^{182}\mathrm{W} \approx +0.4$ returns a two-stage instantaneous-closure age near $\sim 25$ Myr. Combined Hf-W and $^{146}\mathrm{Sm}$-$^{142}\mathrm{Nd}$ systematics of martian meteorites {cite:p}`Kruijer2017Mars` place Mars's accretion within the first $\sim 10$ Myr, magma-ocean crystallisation at $\sim 20$–$25$ Myr, and crust formation $\sim 15$ Myr after that, again faster than Earth and consistent with a small body that accreted its final mass before $^{182}\mathrm{Hf}$ was fully extinct.

The key pedagogical point is that the Hf–W system is only useful as a chronometer while $^{182}\mathrm{Hf}$ is still detectably alive, i.e. within roughly five half-lives, or $\sim 45$ Myr after CAIs. Any core formation completed later than that leaves no $\varepsilon^{182}\mathrm{W}$ signature, which is why Hf–W cannot be applied to, for example, the core nucleation of Earth's **inner core** (which happened billions of years later and is instead constrained by thermal-evolution modelling, see {ref}`Lecture 8 <lecture08>`).

```{figure} figures/mezger2020_accretion_timescales.avif
:name: fig:hf-w-chronometry
:width: 700px
:align: center

Summary of timescales for the accretion and differentiation of solar-system bodies and their connection to Earth's formation, on a logarithmic axis of time after CAI condensation (0.1 to 100 Ma). After the collapse of the solar nebula, CAIs and chondrules form first; planetesimal cores ($^{182}\mathrm{Hf}$-$^{182}\mathrm{W}$) differentiate within the first $\sim 1$ Myr; Mars accretion completes within $\sim 5$ Myr; Jupiter must form before the NC/CC isotopic dichotomy is established; Earth assembly is split into Stage I (proto-Earth, $\sim 90\%$ vol.), Stage II (Moon-forming giant impact, $\sim 10\%$ vol.) and Stage III (late accretion, $\sim 0.5\%$ vol.). Reproduced from {cite:p}`Mezger2020`, Fig. 5.
```


## Mantle differentiation

Core formation is not the end of chemical differentiation. As the magma ocean cools and crystallises, it produces further chemical layering within the silicate mantle itself.

### Magma ocean crystallisation

As the magma ocean loses heat (primarily by radiation from its surface), it begins to solidify. In a deep magma ocean, crystallisation starts at the **base** (where pressure raises the melting point above the local temperature) and progresses upward {cite:p}`ElkinsTanton2012`. The first minerals to crystallise from the deep magma ocean are high-pressure phases: **bridgmanite** (Mg-perovskite, $\mathrm{MgSiO_3}$) in the lower mantle, followed by **olivine** ($\mathrm{(Mg,Fe)_2SiO_4}$) and other phases at shallower depths as the magma ocean solidifies from the bottom up.

The sequence of minerals that crystallise at progressively shallower depths is controlled by the intersection of the magma ocean's adiabat with the peridotite solidus (the temperature below which solid phases are stable). Because the solidus rises more steeply with pressure than the adiabat does, the base of the magma ocean reaches the solidus first. Once solidification begins, the growing crystal fraction displaces liquid upward, compositionally enriching the remaining liquid in the incompatible elements (U, Th, K, and the rare earths). The late stages of crystallisation are therefore marked by a buoyant, volatile- and heat-producing-element-enriched residual liquid concentrated at the top of the mantle ({numref}`fig:magma-ocean-crystallisation`).

```{figure} figures/elkinstanton2012_magma_ocean_crystallisation.avif
:name: fig:magma-ocean-crystallisation
:width: 620px
:align: center

Schematic of magma-ocean crystallisation in a terrestrial planet, from {cite:t}`ElkinsTanton2012`. The ordinate is fractional-depth in the mantle and the abscissa is time as the magma ocean cools. The dense mineral assemblage (bridgmanite, magnesiowüstite, majorite) solidifies first at the base of the mantle (green region, bottom right), with the crystallisation front migrating upward as heat is lost to space from the surface. Olivine and orthopyroxene crystallise at progressively shallower depths (blue region), and the final residual liquid (yellow) is concentrated near the top of the mantle before it solidifies. Incompatible elements (U, Th, K, REE, H$_2$O) partition preferentially into the residual liquid and are enriched in the last-to-crystallise layer, which then becomes the source of much of Earth's heat-producing crust and of the Moon's KREEP layer ({numref}`fig:lunar-magma-ocean`). Reproduced from {cite:t}`ElkinsTanton2012`.
```

### Incompatible element enrichment

During crystallisation, elements that do not fit easily into the crystal lattice of the solidifying minerals, so-called **incompatible elements**, are progressively concentrated in the remaining liquid. The most important incompatible elements include the heat-producing isotopes uranium (U), thorium (Th), and potassium (K), which were introduced in {ref}`Lecture 3 <lecture03>` as the sources of long-lived radiogenic heating.

As crystallisation proceeds, these incompatible elements are squeezed into an ever-smaller volume of residual liquid, which eventually solidifies to form the **crust**. This is why the continental crust is enriched in U, Th, and K by a factor of $\sim$50–100 relative to the upper mantle, and why roughly half of Earth's radiogenic heat is produced in the thin crustal layer despite it representing less than 1% of Earth's mass.

### Mantle reservoirs

The crystallisation of a magma ocean does not produce a perfectly homogeneous mantle. Instead, it creates compositionally distinct **mantle reservoirs** that persist to the present day:

- **Depleted MORB mantle (DMM):** The upper mantle source of mid-ocean ridge basalts (MORBs) has been depleted in incompatible elements by billions of years of partial melting and crustal extraction. This is the most voluminous mantle reservoir.

- **Enriched mantle:** Deep mantle plumes that produce ocean island basalts (OIBs, e.g., Hawaii, Iceland) sample reservoirs that are enriched in incompatible elements, possibly representing less-processed primordial mantle material or recycled oceanic crust.

### The lunar magma ocean

The Moon provides the clearest example of magma ocean crystallisation. The Moon's **anorthositic crust** (a layer of light-coloured, feldspar-rich rock) is thought to have formed by flotation of low-density plagioclase crystals on top of the lunar magma ocean. Beneath the crust lies a layer enriched in **KREEP** (the acronym is formed from the chemical symbols **K**, Rare **E**arth **E**lements, and **P** for phosphorus): the last residual liquid to crystallise, concentrated in incompatible elements just as the theory predicts {cite:p}`ElkinsTanton2012`. The prefix **"ur"** in "urKREEP" is the geochemical convention for "primordial" or "original-source", so **urKREEP** denotes the unmixed, first-crystallised KREEP reservoir before any subsequent partial-melting or mixing events redistributed it.

The Moon is particularly diagnostic because its small size and single-plate tectonic regime have largely preserved the original magma-ocean stratigraphy. Apollo and Luna sample returns identified three chemically distinct lunar lithologies that line up almost perfectly with the predicted crystallisation sequence: (i) a $\sim 40$–$50$ km **anorthositic highlands crust** formed by plagioclase flotation; (ii) a cumulate pyroxenite-to-dunite mantle beneath the crust, with compositional layering that records progressive mafic-mineral crystallisation; and (iii) an **ilmenite-bearing, KREEP-enriched residual layer** at the base of the crust or the top of the mantle, which is thought to have undergone gravitational overturn (the dense ilmenite-rich layer sinking while the underlying buoyant layers rose) early in lunar history ({numref}`fig:lunar-magma-ocean`).

```{figure} figures/elkinstanton2012_lunar_magma_ocean.avif
:name: fig:lunar-magma-ocean
:width: 580px
:align: center

Schematic structure of the lunar magma ocean at the end of solidification, redrawn after {cite:t}`ElkinsTanton2012`. The outer $\sim 40$–$50$ km is an anorthositic crust formed by flotation of plagioclase on top of the crystallising magma ocean (pale layer, top). Beneath it a thin **urKREEP** layer (yellow) represents the last $\sim 1\%$ of the original magma ocean to solidify and is concentrated in incompatible trace elements, including the heat-producing isotopes $^{40}\mathrm{K}$, $^{235,238}\mathrm{U}$, and $^{232}\mathrm{Th}$. The pyroxenite and dunite cumulates (green band) solidified from the magma ocean during the intermediate crystallisation stages. Beneath the urKREEP layer, dense ilmenite-rich cumulates (dark-green band near the top of the cumulate region) formed near the end of crystallisation are gravitationally unstable and sank toward the core, producing the **lunar mantle overturn** that dominated lunar tectonics in the first $\sim 500$ Myr after crystallisation. An iron core sits at the centre. Schematic after {cite:t}`ElkinsTanton2012`.
```


## Volatile delivery and retention

The chemical differentiation discussed so far concerns the refractory (high-temperature) components of planets. But the **volatile elements** (hydrogen, carbon, nitrogen, sulfur, and the noble gases) are equally important, because they form the raw materials for atmospheres, oceans, and ultimately life.

### The classical view and its revision

The classical picture of volatile delivery held a simple dichotomy: the inner solar system formed **hot and dry** (inside the snow line at $\sim$2–3 AU), while volatile-rich material was confined to the outer solar system. Water and other volatiles were then delivered to the terrestrial planets *late*, primarily by carbonaceous chondrite-like bodies scattered inward from the outer asteroid belt or beyond.

Recent work has substantially revised this picture. Several independent lines of evidence now indicate that **volatile-bearing material was present in the inner solar system from early times**:

- {cite:p}`Alexander2019a` and {cite:p}`Alexander2019b` showed through quantitative models of elemental and isotopic fractionations that **all chondrite groups**, including non-carbonaceous (ordinary, enstatite) chondrites traditionally associated with the dry inner disk, accreted water ice. This implies that even inner solar system planetesimals formed at temperatures below the snow line ($\sim$150–170 K) or incorporated icy material, challenging the simple "dry inner / wet outer" paradigm.

- {cite:p}`Lichtenberg2021` demonstrated that the migration of the **snow line** during the protoplanetary disk's evolution, combined with Jupiter's growth to pebble-isolation mass, created a **bifurcation** in planetesimal populations. Early-formed planetesimals accreted ice-rich material regardless of their formation location, while late-formed inner disk planetesimals were desiccated after Jupiter blocked the inward drift of icy pebbles. This mechanism explains both the non-carbonaceous/carbonaceous (NC–CC) isotopic dichotomy observed in meteorites and the volatile gradient across the inner solar system.

- {cite:p}`Grewal2019` and {cite:p}`Grewal2021` used isotopic evidence for carbon, nitrogen, and sulfur to show that volatile delivery to Earth involved contributions from both inner (enstatite-like) and outer (carbonaceous) reservoirs. Nitrogen isotopes reveal that inner and outer solar system protoplanets accreted from **isotopically distinct** nitrogen reservoirs very early, implying that volatile budgets were largely set during primary accretion rather than solely by a late veneer of carbonaceous material.

These findings suggest that the volatile inventory of terrestrial planets is determined by a complex interplay of disk thermal evolution, giant planet formation timing, and the mixing of multiple source reservoirs {cite:p}`Krijt2023`. The two-reservoir picture inherited from snow-line migration in the Class I and Class II disk stages is summarised in {numref}`fig:lichtenberg2021-snowline`.

```{figure} figures/lichtenberg2021_fig1.avif
:name: fig:lichtenberg2021-snowline
:width: 600px
:align: center

Snow line migration in the protoplanetary disk produces two distinct bursts of planetesimal formation. Early planetesimals (Reservoir I, red) form just inside the inward-migrating water snow line during the Class I disk stage and accrete ice-rich material; later planetesimals (Reservoir II, blue) form in the outer disk during the Class II stage once Jupiter has reached pebble-isolation mass and blocked the inward drift of icy pebbles to the inner disk. The two reservoirs are spatially and temporally separated, providing a natural explanation for the non-carbonaceous/carbonaceous (NC/CC) isotopic dichotomy observed in meteorites. Reproduced from {cite:t}`Lichtenberg2021`.
```

### Outgassing from the magma ocean

Regardless of how volatiles were delivered, much of a planet's initial volatile budget is dissolved in the silicate magma ocean. As the magma ocean cools and crystallises, dissolved volatiles are released to form a **secondary atmosphere** through **outgassing** {cite:p}`Hirschmann2012`.

The speciation of the outgassed atmosphere depends critically on the **oxygen fugacity** of the magma:

- Under **reducing** conditions (low $f_{\mathrm{O_2}}$): the dominant outgassed species are $\mathrm{H_2}$, CO, and $\mathrm{N_2}$
- Under **oxidising** conditions (high $f_{\mathrm{O_2}}$, like present-day Earth): the dominant species are $\mathrm{H_2O}$, $\mathrm{CO_2}$, and $\mathrm{N_2}$

The solubility of water in silicate melt follows a square-root law:

$$
X_{\mathrm{H_2O}} \propto p_{\mathrm{H_2O}}^{1/2}
$$ (eq:water-solubility)

where $X_{\mathrm{H_2O}}$ is the mole fraction of dissolved water and $p_{\mathrm{H_2O}}$ is the partial pressure of water vapour above the melt. This means that as the atmosphere thickens with outgassed $\mathrm{H_2O}$, the magma ocean can retain an increasing fraction of its water in solution, a self-limiting feedback that determines the partitioning of water between the interior and the atmosphere ({numref}`fig:water-solubility`) {cite:p}`Hirschmann2012`.

```{figure} figures/water_solubility.avif
:name: fig:water-solubility
:width: 550px
:align: center

Solubility of H$_2$O in basaltic silicate melt as a function of the H$_2$O partial pressure above the melt, on a log-log scale. The straight line on log-log axes is the signature of the Henrian square-root law of Eq. {eq}`eq:water-solubility`, which arises because dissolved water speciates predominantly as OH$^-$ groups in the melt. A 1 kbar magma ocean atmosphere can dissolve $\sim 4$ wt% H$_2$O; a 5 kbar atmosphere can dissolve $\sim 9$ wt%. The plot uses $K \approx 0.42$ wt% MPa$^{-1/2}$ representative of basalt at 1573 K {cite:p}`Hirschmann2012`.
```

### Impact erosion versus delivery

Giant impacts deliver volatiles but can also **strip** them away. Impact erosion operates in two distinct regimes, depending on the size of the impactor relative to the target.

**Local erosion by ordinary impacts.** A large, fast impactor vaporises itself and part of the target surface; the expanding vapour plume can accelerate the overlying air beyond the escape velocity. The maximum airmass a single such event can remove is the atmosphere above the plane tangent to the surface at the impact point {cite:p}`MeloshVickery1989`. For a thin atmosphere (scale height $H \ll R$), the airmass above the tangent plane is only a fraction

$$
f_\mathrm{tp} \approx \frac{H}{2R}
$$ (eq:tangent-plane-fraction)

of the global inventory, about $6 \times 10^{-4}$ for present-day Earth ($H \approx 8$ km). A single ordinary impact therefore barely dents an atmosphere; tangent-plane erosion matters through the *cumulative* effect of many impacts over the bombardment epoch. Per unit impactor mass, the most efficient eroders are small planetesimals only just large enough (km-scale for present-day Earth) to expel air locally: they spend their energy on the atmosphere alone, whereas a giant impact invests most of its energy in ground motion, of which only the fraction approaching escape velocity couples into atmospheric loss {cite:p}`Schlichting2015`.

**Global erosion by giant impacts.** A giant impact shakes the entire planet: the shock from the impact propagates through the interior and sets the ground into motion everywhere, including the antipode. Wherever the local ground velocity $v_\mathrm{ground}$ approaches the escape velocity,

$$
v_\mathrm{ground} \gtrsim v_\mathrm{esc},
$$ (eq:ground-motion-blowoff)

the overlying atmospheric column is expelled. One-dimensional shock-hydrodynamic calculations of this mechanism show that the loss is far from total: even in the Moon-forming impact, the ground over most of the globe moves at only a few km s$^{-1}$, well below Earth's $v_\mathrm{esc} \approx 11$ km s$^{-1}$, so the event removes only $\sim 20\%$ of the pre-impact atmosphere and most of the atmosphere survives {cite:p}`GendaAbe2003`. A surface ocean changes this conclusion substantially: vaporisation of the ocean and its lower **shock impedance** (the product of density and wave speed, which sets how efficiently ground motion transmits into the layer above) couple the ground motion to the atmosphere far more efficiently, enhancing the loss {cite:p}`GendaAbe2005`. This ocean effect has been invoked to explain why Venus (whose protoplanets likely lacked surface oceans) retains roughly 50 times more $^{36}\mathrm{Ar}$ than Earth: remnants of the noble-gas-rich primordial atmosphere survived on Venus but were lost from ocean-covered proto-Earth {cite:p}`GendaAbe2005`.

The implication for Earth is that any **primordial H$_2$-He envelope** captured from the protoplanetary disk was not removed in a single blow. Its removal required the combination of repeated impact erosion during accretion and sustained thermal escape driven by the young Sun's high XUV (X-ray and extreme-ultraviolet) output ({ref}`Lecture 5 <lecture05>`), leaving behind a secondary outgassed atmosphere of the kind described in the previous subsection. For Mars, whose escape velocity ($\approx 5$ km s$^{-1}$) is less than half of Earth's, both erosion channels are more effective at equal impact energy. A Borealis-scale impact ({cite:t}`Marinova2008`) plausibly removed a substantial fraction of the earliest atmosphere, and the long-term solar-wind-driven escape after the dynamo shutdown did the rest ({ref}`Lecture 10 <lecture10>`).

The balance between delivery and erosion is a key uncertainty in reconstructing the volatile histories of the terrestrial planets: the same planetesimal population that delivers volatile-rich material also erodes the growing atmosphere, and the net outcome depends on the impactor size distribution, velocity distribution, and volatile content {cite:p}`Schlichting2015`. Earth's present atmospheric and ocean inventory likely reflects the integrated outcome of both processes superimposed on the secondary outgassing from the final magma ocean.

We will return to the fate of these outgassed atmospheres (their composition, structure, and long-term evolution) in {ref}`Lecture 5 <lecture05>` and {ref}`Lecture 6 <lecture06>`.


## Planetary magnetic fields and dynamo theory

The differentiation of a planet into a metallic core and silicate mantle sets the stage for one of the most important geophysical phenomena: the generation of a planetary **magnetic field** by dynamo action in the liquid metallic core.

### Why magnetic fields matter

Planetary magnetic fields play several critical roles:

- **Atmospheric shielding:** A global magnetic field deflects the charged particles of the solar wind, reducing atmospheric erosion by sputtering and ion pickup. Mars, which lost its global field $\sim$4 Gyr ago, has since lost much of its atmosphere ({ref}`Lecture 10 <lecture10>`).
- **Surface habitability:** By deflecting energetic particles, magnetic fields reduce the radiation dose at a planet's surface, potentially important for the survival of surface life.
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

For a self-sustaining dynamo (one that can generate and maintain a magnetic field against ohmic decay), three conditions must be met:

1. **An electrically conducting fluid:** The core must contain a fluid with sufficient electrical conductivity ($\sigma$) to carry the currents that generate the field. In terrestrial planets, this is liquid iron (alloyed with lighter elements like S, Si, O). In gas giants, it is metallic hydrogen.

2. **Convection:** The fluid must be in vigorous motion. In planetary cores, this convection is driven by thermal buoyancy (the core is hotter than the overlying mantle) and/or compositional buoyancy (crystallisation of the inner core releases light elements that rise).

3. **Sufficient flow vigour:** The fluid motions must be fast enough, and occur on large enough scales, that advection dominates over diffusion. This criterion is quantified by the **magnetic Reynolds number** $\mathrm{Rm}$, which must exceed a critical value $\mathrm{Rm}_c \sim 10$–$100$.

The basic picture is summarised in {numref}`fig:geodynamo-schematic`: convective columns aligned with the rotation axis stretch and twist field lines in the conducting outer core, regenerating the field against ohmic decay.

```{figure} figures/geodynamo_schematic.svg
:name: fig:geodynamo-schematic
:width: 450px
:align: center

Schematic of the geodynamo mechanism. Convective motions in the electrically conducting liquid outer core stretch and twist magnetic field lines, generating Earth's predominantly dipolar magnetic field. The Coriolis force organises the flow into columnar structures aligned with the rotation axis. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```


## Blackboard derivation: The magnetic Reynolds number

```{admonition} Blackboard derivation: The magnetic Reynolds number $\mathrm{Rm}$
:class: tip

**Goal:** Derive the magnetic Reynolds number $\mathrm{Rm} = UL/\eta$ from the induction equation by dimensional analysis, and estimate $\mathrm{Rm}$ for Earth's outer core to demonstrate that advection dominates over diffusion, the fundamental criterion for dynamo action.

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

Notice that the magnetic field strength $B$ **cancels**: this is an important result. The magnetic Reynolds number is a property of the **flow**, not of the field:

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

We can also estimate the **ohmic diffusion timescale**, how long the field would take to decay if the flow suddenly stopped:

$$
\tau_{\mathrm{ohm}} \sim \frac{L^2}{\eta} = \frac{(3.5 \times 10^6)^2}{1} \approx 1.2 \times 10^{13} \text{ s} \approx 400{,}000 \text{ yr}
$$

This is much less than Earth's age (4.5 Gyr), confirming that the field cannot be a relic; it must be **continuously regenerated** by dynamo action.

**Note:** Paleomagnetic measurements of ancient rocks show that Earth has had a magnetic field for at least **3.4–3.5 billion years** {cite:p}`Tarduno2010`. This places a strong constraint on the thermal and compositional evolution of the core: the convective driving mechanism must have been sustained over most of Earth's history.
```


## Earth's geodynamo

With the theoretical framework established, we now examine how the dynamo operates in Earth's core.

### Core structure

Earth's core extends from the centre of the planet to a depth of 2890 km (the core–mantle boundary). It comprises two distinct regions:

- **Inner core** (radius 0–1220 km): Solid iron–nickel alloy. The inner core is slowly growing as the outer core cools and crystallises at the inner core boundary.

- **Outer core** (radius 1220–3480 km from the centre, or depth 2890–5150 km): Liquid iron alloy. The outer core is about 5–10% less dense than pure liquid iron, indicating the presence of dissolved light elements (S, Si, O, C, H). This is the region where the geodynamo operates ({numref}`fig:earth-interior`).

```{figure} figures/earth_interior.avif
:name: fig:earth-interior
:width: 500px
:align: center

Cross-section of Earth's interior, showing the solid inner core ($r < 1220$ km), the liquid iron-alloy outer core (1220–3480 km), the silicate mantle (from $\sim 30$ km depth at the crust base down to 2890 km at the core-mantle boundary), and the thin crust. The geodynamo operates in the convecting outer core; the inner core grows slowly as light elements are expelled into the outer core. Credit: NASA/JPL-Caltech/SwRI/J.E.P. Connerney (PIA25063), public domain.
```

The structure above is inferred primarily from seismology: the travel times of $P$ and $S$ waves through Earth, recorded by global seismometer networks, constrain the density and elastic-wave velocities as a function of depth ({numref}`fig:prem`). The most widely used reference profile is the **Preliminary Reference Earth Model** {cite:p}`Dziewonski1981`.

```{figure} figures/prem_profile.avif
:name: fig:prem
:width: 550px
:align: center

Preliminary Reference Earth Model (PREM) seismic $P$-wave velocity ($V_p$, blue), $S$-wave velocity ($V_s$, red), and density ($\rho$, green) versus depth. The vanishing $V_s$ in the outer core (2890–5150 km depth) is direct evidence that this region cannot support transverse elastic waves, i.e. it is liquid; the discontinuous jumps in density at the core-mantle boundary (CMB) and inner-core boundary (ICB) record the metal-silicate interface and the latent heat of inner-core crystallisation respectively. Curve digitised from {cite:t}`Dziewonski1981`.
```

### Driving mechanisms

Convection in the outer core is driven by two sources of buoyancy {cite:p}`Roberts2013`:

1. **Thermal convection:** The core is hotter than the overlying mantle, so heat flows outward. As the core cools, the temperature drop drives thermal buoyancy.

2. **Compositional convection:** As the inner core crystallises, it preferentially incorporates iron and rejects light elements (S, Si, O) into the liquid outer core. This light, buoyant fluid rises, providing a powerful source of convection. The latent heat released by crystallisation further contributes to thermal buoyancy.

Compositional convection is thought to be the dominant driver of the present-day geodynamo. The growth of the inner core, currently at a rate of about 0.5 mm per year, provides a steady supply of both compositional buoyancy and latent heat.

### Field morphology

Earth's magnetic field at the surface is predominantly **dipolar** (resembling the field of a bar magnet), with the dipole axis tilted approximately 11° from the rotation axis. The surface field strength ranges from about 25 $\mu$T near the equator to about 65 $\mu$T near the poles, with a mean of about 45 $\mu$T.

### Secular variation

The magnetic field is not static. It varies on timescales from years to millions of years:

- **Secular variation:** The field changes measurably on decadal to century timescales. The non-dipole components of the field drift, grow, and decay, which traces the turbulent flow in the outer core.

- **South Atlantic Anomaly:** A region of anomalously weak field strength over the South Atlantic, where the field is about 30% weaker than the global average at that latitude. This is the surface expression of a reversed-flux patch at the core–mantle boundary.

- **Westward drift:** Many features of the non-dipole field drift westward at roughly 0.2° per year, consistent with a differential rotation between the outer core and the mantle.

### Polarity reversals

On longer timescales, the geomagnetic field undergoes **polarity reversals**: the north and south magnetic poles swap. Key facts about reversals:

- The average reversal rate over the past few million years is roughly **4–5 reversals per million years**, though this rate has varied significantly over geological time and the present epoch (the Brunhes normal chron, since $\sim 780$ ka) has not seen a reversal.
- A reversal takes approximately **1000–10,000 years** to complete, during which the field weakens, becomes complex (multipolar), and re-establishes in the opposite polarity.
- During the Cretaceous Normal Superchron (~83–121 Ma), the field maintained a single polarity for about 38 million years.

The most compelling evidence for reversals comes from **magnetic stripes** on the ocean floor: as new oceanic crust forms at mid-ocean ridges, the magnetic minerals record the ambient field direction. The result is a symmetric pattern of normally and reversely magnetised stripes on either side of the ridge, a key piece of evidence for both seafloor spreading and geomagnetic reversals. The compiled polarity timescale for the past 170 Myr is shown in {numref}`fig:geomagnetic-polarity`.

```{figure} figures/geomagnetic_polarity_timescale.avif
:name: fig:geomagnetic-polarity
:width: 750px
:align: center

Geomagnetic polarity timescale for the past 170 Myr. Black bars mark intervals of normal polarity (north magnetic pole near the geographic north), white bars mark reversed polarity. The reversal rate has varied from $\sim 4$–$5$ per Myr in the late Cenozoic to essentially zero during the Cretaceous Normal Superchron (CNS, C34n, $\sim 83$–$121$ Ma), shown as the long uninterrupted black band in the middle of the panel. The Mesozoic and Cenozoic era intervals (boundary at $\sim 66$ Ma) are marked below the axis. Reversals appear statistically consistent with a non-stationary Poisson process, as expected for the chaotic dynamics of the geodynamo. Schematic; boundary ages are approximate and should not be read to better than $\sim 1$ Myr. Exact chron ages follow the Geologic Time Scale 2020 compilation {cite:p}`Gradstein2020`.
```


## Comparative magnetospheres

Magnetic fields vary enormously across the solar system. Comparing them reveals how dynamo action depends on a planet's size, composition, thermal state, and rotational dynamics.

### Magnetic field comparison

| Body | Field type | Surface field | Dipole moment (relative to Earth) | Notes |
|------|-----------|:---:|:---:|-------|
| **Earth** | Active dynamo | 25–65 $\mu$T | 1 | Liquid Fe outer core, growing inner core |
| **Mercury** | Active dynamo | ~0.3 $\mu$T | $\sim 5 \times 10^{-4}$ | Weak; thin liquid shell {cite:p}`Anderson2012` |
| **Venus** | None detected | $< 0.01$ $\mu$T | $< 10^{-5}$ | No dynamo despite large iron core |
| **Mars** | Remnant crustal | Up to ~1500 nT | n/a | Dynamo ceased $\sim 4.1$-$3.7$ Ga {cite:p}`Acuna1999,Mittelholz2020` |
| **Jupiter** | Active dynamo | ~400–1400 $\mu$T | $\sim 20{,}000$ | Metallic H dynamo {cite:p}`Connerney2022` |
| **Saturn** | Active dynamo | ~20 $\mu$T | ~600 | Remarkably axisymmetric |
| **Uranus** | Active dynamo | ~10–100 $\mu$T | ~50 | Multipolar, tilted ~59° and offset from centre |
| **Neptune** | Active dynamo | ~10–60 $\mu$T | ~28 | Multipolar, tilted ~47° and offset from centre |
| **Ganymede** | Active dynamo | ~0.7 $\mu$T | $\sim 1.5 \times 10^{-3}$ | Only moon with intrinsic dynamo |

These nine bodies span four orders of magnitude in surface field strength and a range of morphologies from cleanly dipolar (Earth, Jupiter, Saturn, Ganymede) to weak and offset (Mercury) to strongly multipolar (Uranus, Neptune), as illustrated in {numref}`fig:planetary-dipole-moments`.

```{figure} figures/soderlund2020_planetary_field_morphologies.avif
:name: fig:planetary-dipole-moments
:width: 700px
:align: center

Radial magnetic field at the surfaces of (a) Mercury, (b) Earth, (c) Jupiter, (d) Saturn, (e) Uranus, and (f) Neptune, in Mollweide projections. Earth, Jupiter, and Saturn are predominantly dipolar with the dipole axis approximately aligned with the rotation axis; Uranus and Neptune are clearly multipolar with dipoles tilted by $\sim 59°$ and $\sim 47°$ respectively and offset from the planet centre; Mercury's field is weak and asymmetric, with the dipole offset $\sim 500$ km northward. Field intensities span four orders of magnitude (note the per-panel colour scales). Reproduced from {cite:p}`Soderlund2020`, Fig. 1.
```

The same nine-decade range can be understood as a single dynamical family by placing each body in the parameter space of dimensionless dipole moment versus local Rossby number. {numref}`fig:dipole-scaling` shows the strongly dipolar regime (top-left, dark shading) and multipolar regime (lower-right, light shading) inferred from numerical dynamo models, with the eight planets and Ganymede plotted at their estimated control-parameter values.

```{figure} figures/olson2006_dipole_scaling.avif
:name: fig:dipole-scaling
:width: 600px
:align: center

Dimensionless planetary dipole moment $L_{\mathrm{O}_{\rm dip}}/\mathrm{Ra}_Q^{1/3}$ versus local Rossby number $\mathrm{Ro}_l$. The transition from strongly dipolar (dark shading) to multipolar (light shading) regimes is calibrated against numerical dynamo simulations. The eight planets and Ganymede are placed at their estimated control-parameter values; symbol shading indicates the strength of the constraint. Earth, Jupiter, Saturn, and Ganymede sit in the dipolar regime; Mercury, Uranus, and Neptune lie in or near the multipolar regime, consistent with their tilted, offset, or weak surface fields. Reproduced from {cite:p}`OlsonChristensen2006`, Fig. 7.
```

### Mercury

Mercury possesses a weak but **active** dynamo: its surface field is only about 1% of Earth's. The MESSENGER mission revealed that Mercury's field is strongly offset northward from the planet's centre, suggesting an unusual dynamo geometry. Mercury's liquid outer core shell is thought to be relatively thin (perhaps only a few hundred kilometres), which limits the vigour of convection and the resulting field strength {cite:p}`Anderson2012`.

### Venus

Venus presents a puzzle: it is nearly identical to Earth in size and bulk composition, and should have a liquid iron core, yet it has **no detected magnetic field**. Several explanations have been proposed:

- **Slow rotation:** Venus rotates extremely slowly (243-day period), but numerical dynamo simulations show that slow rotation alone does not prevent dynamo action.
- **No inner core:** If Venus's core is entirely liquid (no solid inner core has nucleated), then compositional convection (the dominant driver of Earth's dynamo) would be absent. Thermal convection alone may be insufficient.
- **Stagnant lid tectonics:** Without plate tectonics ({ref}`Lecture 9 <lecture09>`), the mantle may not extract heat from the core efficiently enough to drive vigorous core convection.

The relative importance of these factors remains debated. Venus's lack of a magnetic field likely reflects a combination of reduced core cooling (due to stagnant lid tectonics insulating the core) and potentially the absence of an inner core {cite:p}`dePaterLissauer2010`.

### Mars

Mars has no global magnetic field today, but the Mars Global Surveyor spacecraft discovered intense **remnant crustal magnetism** in the ancient southern highlands ({numref}`fig:mars-crustal-magnetism`), patches of magnetisation with field strengths up to $\sim$1500 nT measured at $\sim$100–200 km aerobraking altitude, far stronger than crustal magnetisation on Earth {cite:p}`Acuna1999`. These crustal magnetic anomalies are absent in the younger northern lowlands and in large impact basins (Hellas, Argyre, Isidis), indicating that:

1. Mars once had an active dynamo that magnetised the ancient crust.
2. The dynamo shut down between **~4.1 and ~3.7 Gyr ago**: the original basin-demagnetisation analysis of {cite:t}`Acuna1999` placed the cessation around 4.1-3.9 Ga, while more recent low-altitude *MAVEN* data analysed by {cite:t}`Mittelholz2020` push the last detectable dynamo activity to as late as $\sim 3.7$ Ga.
3. The loss of the global magnetic field left Mars's atmosphere unshielded against solar wind erosion, likely contributing to the dramatic atmospheric loss that transformed Mars from a warmer, wetter world to the cold, thin-atmosphere planet we see today (see {ref}`Lecture 10 <lecture10>`).

```{figure} figures/mars_crustal_magnetism.avif
:name: fig:mars-crustal-magnetism
:width: 550px
:align: center

Global map of the radial component $\Delta B_r$ of Mars's crustal magnetic field, compiled from Mars Global Surveyor (MGS) MAG/ER data at $\sim 400$ km mapping-orbit altitude. Red and blue regions indicate strong crustal magnetisation in opposite polarities, concentrated in the ancient southern highlands. The younger northern lowlands and the large impact basins (Hellas, Argyre, Isidis) show little to no magnetisation, indicating the dynamo had ceased before these features formed {cite:p}`Connerney2005`. The original detection of Mars's crustal field is reported in {cite:t}`Acuna1999`. Credit: NASA/Goddard Space Flight Center, public domain.
```

Recent constraints on Mars's interior come from the InSight lander, which deployed the first seismometer on the Martian surface and detected $S$-wave reflections from the core-mantle boundary. Joint inversion of these seismic data with geodetic constraints (mean density, moment of inertia, tidal Love number $k_2$) gives a core radius of $R_{\rm core} = 1830 \pm 40$ km ({numref}`fig:stahler2021-mars-core`), larger than expected from many pre-mission models {cite:p}`Stahler2021`. The implied core density is too low for pure iron, requiring a substantial complement of light elements (S, O, H, C). The large, light core informs models of when and why the Martian dynamo shut down: a core that is too sulfur-rich may never have nucleated a solid inner core, depriving the dynamo of compositional buoyancy.

```{figure} figures/stahler2021_mars_core.avif
:name: fig:stahler2021-mars-core
:width: 550px
:align: center

Joint posterior distribution of Mars's mean core density and core radius from three independent inversions of InSight seismic and geodetic data: a geophysical inversion (blue), a geodynamical inversion (orange), and a mineralogical inversion (yellow). All three converge on a core radius near 1830 km and a mean core density near 6.0 g cm$^{-3}$. Purple bands show iso-composition curves for Fe-S-O-H-C alloys; the data require several wt% of light elements. Reproduced from {cite:t}`Stahler2021`, Fig. 2C.
```

### Jupiter

Jupiter has the **strongest magnetic field** of any planet, roughly 20,000 times Earth's dipole moment. The field is generated by convection in Jupiter's deep interior, where hydrogen is compressed to a metallic state (at pressures above $\sim$100 GPa, hydrogen becomes an electrical conductor). The Juno mission has mapped Jupiter's magnetic field in unprecedented detail, revealing a surprisingly complex and asymmetric field at the surface, with a concentrated magnetic flux patch in the northern hemisphere, the "Great Blue Spot" ({numref}`fig:jupiter-great-blue-spot`) {cite:p}`Connerney2022`.

```{figure} figures/jupiter_great_blue_spot.avif
:name: fig:jupiter-great-blue-spot
:width: 600px
:align: center

Mollweide projection of the radial component of Jupiter's surface magnetic field, derived from the Juno JRM33 model {cite:p}`Connerney2022`. Red marks outward field, blue inward; latitude and longitude grid in System III coordinates. Unlike Earth's field, which is dominated by an axial dipole at the surface, Jupiter's surface field shows pronounced non-dipolar structure, including the intense localised patch of inward flux near the equator (the "Great Blue Spot", deep-blue feature near $0^\circ$ latitude) paired with a strong outward patch immediately to its west. The morphology constrains the depth at which the metallic-hydrogen dynamo operates and indicates that the dynamo is not confined to a thin shell. Credit: NASA/JPL-Caltech/SwRI/J.E.P. Connerney (PIA25040), public domain.
```

### Ganymede

Jupiter's largest moon Ganymede is the only moon in the solar system with its own **intrinsic dynamo**. Its surface field of $\sim$0.7 $\mu$T implies a small but actively convecting liquid iron core. The existence of Ganymede's dynamo is surprising given the moon's small size and is not yet fully understood: it may be sustained by tidal heating or compositional convection from a freezing core {cite:p}`dePaterLissauer2010`.

### Thin-shell dynamos: Mercury and Ganymede contrasted

Mercury and Ganymede present a striking puzzle. Both have sustained dynamos in surprisingly small bodies: Mercury's radius is $2440$ km ($38\%$ of Earth's), and Ganymede's radius is $2634$ km ($41\%$ of Earth's). Yet their surface-field strengths differ by a factor of $\sim 2$ and their internal structures are almost certainly very different. In both cases, the leading hypothesis is a **thin-shell dynamo** operating in a narrow layer of liquid iron alloy that has not yet solidified beneath a growing inner core or between an inner core and a silicate mantle.

Numerical dynamo simulations establish a robust empirical **Christensen-Aubert scaling** between the surface dipole field $B_\mathrm{dip}$, the convective buoyancy flux $F_q$ driving the flow, and the thickness $D$ of the convecting shell {cite:p}`ChristensenAubert2006,OlsonChristensen2006`:

$$
B_\mathrm{dip} \propto \sqrt{\rho_\mathrm{core} \mu_0} \cdot \big( F_q \cdot D \big)^{1/3}
$$ (eq:dynamo-scaling)

where $\rho_\mathrm{core}$ is the mean density of the convecting fluid and $\mu_0$ is the permeability of free space. This scaling is independent of the fluid's rotation rate (provided the flow is rapidly rotating, as it is in every planetary core), and it collapses the output of dozens of three-dimensional numerical dynamo runs onto a single regression line that also passes through Earth, Jupiter, and Saturn. The physical content is that the field strength is set by the rate at which convection generates magnetic energy, which scales with the buoyancy flux and the depth over which that flux is integrated.

The contrast between Mercury and Ganymede follows from applying Eq. {eq}`eq:dynamo-scaling` with very different internal-structure inputs:

| Quantity | **Mercury** | **Ganymede** |
|---|:---:|:---:|
| Planet radius $R_\mathrm{planet}$ | $2440$ km | $2634$ km |
| Core radius $R_\mathrm{core}$ | $\sim 2020$ km {cite:p}`MargotHauck2018` | $\sim 700$ km |
| Liquid-shell thickness $D$ | $\sim 200$–$400$ km (narrow shell above a solidifying inner core) | $\sim 300$ km (liquid iron sandwiched between solid iron inner core and rocky mantle) |
| Buoyancy driver | Latent heat + light-element release from iron snow / inner-core growth | Inner-core growth + tidal-heat modulation |
| Surface dipole $B_\mathrm{dip}$ | $\sim 0.3\ \mu$T | $\sim 0.7\ \mu$T |
| Dynamo regime | Iron-snow / thin liquid shell {cite:p}`Anderson2012` | Convective crystallising core shell {cite:p}`dePaterLissauer2010` |

The key points are: (i) Mercury's dynamo shell is thin in absolute terms because its large core leaves only a shallow convecting layer, whereas Ganymede's dynamo shell is similarly thin but sits in a much smaller absolute core; (ii) both bodies nonetheless satisfy the magnetic-Reynolds criterion ($\mathrm{Rm} \gtrsim 10$) and the scaling of Eq. {eq}`eq:dynamo-scaling`, because the product $F_q \cdot D$ is what matters rather than either factor alone. Geometric considerations magnify the comparison: for a dipole source at the top of the convecting region, the surface field is reduced from the dynamo-region field by $(R_\mathrm{core}/R_\mathrm{planet})^3$, the standard dipole attenuation. For Mercury the ratio is $(2020/2440)^3 \approx 0.57$, so only $\sim 40\%$ of the dynamo-region field strength is lost at the surface. For Ganymede the ratio is $(700/2634)^3 \approx 0.019$, so the surface retains less than $2\%$ of the dynamo-region field. Mercury's observed weaker surface field ($0.3\,\mu$T vs Ganymede's $0.7\,\mu$T) *despite* its much smaller attenuation therefore implies that Mercury's dynamo is **intrinsically much weaker** at source than Ganymede's, i.e. a smaller $F_q \cdot D$ product. This is consistent with the iron-snow scenario for Mercury, in which a thin solidification shell at the bottom of the liquid core releases light elements episodically rather than continuously and drives convection at a more modest rate than Ganymede's steadier compositional buoyancy source.

The geometric attenuation also explains why giant-planet dynamos dominate in absolute field strength. Jupiter's metallic-hydrogen dynamo extends to $\sim 0.85\,R_\mathrm{Jup}$, so surface fields retain $\sim 60\%$ of the dynamo-region strength. Even a modest enhancement of $F_q \cdot D$ from Jupiter's deep, vigorous convection then yields a $20{,}000\,\times$ stronger surface field than Earth's, without requiring Jupiter's convection to be $20{,}000\,\times$ more vigorous.

Venus is the odd one out: despite having a core that is nearly Earth-like by composition and size, it has no detectable dynamo today. The most likely explanation is that Venus's core has not yet begun to crystallise (no inner core) *and* that the stagnant-lid mantle above the core extracts heat too slowly to drive vigorous thermal convection {cite:p}`dePaterLissauer2010`. In the scaling of Eq. {eq}`eq:dynamo-scaling`, both $F_q$ and the convective shell geometry are simultaneously suppressed, and the dynamo cannot sustain itself. Venus is thus the clearest example of a planet whose magnetic state is limited not by core composition but by **mantle dynamics** controlling heat loss from the core.

```{figure} figures/christensen2006_dynamo_scaling.avif
:name: fig:dynamo-scaling
:width: 620px
:align: center

Predicted vs observed magnetic-field strength for numerical dynamo simulations and solar-system bodies, following the scaling law of Eq. {eq}`eq:dynamo-scaling`. The horizontal axis is a non-dimensional combination of convective buoyancy flux, shell thickness, and core density; the vertical axis is the measured (observed) or computed (simulated) dipole field. Numerical simulations (grey crosses) collapse onto a single line over roughly four orders of magnitude; Earth, Jupiter, Saturn, Mercury, and Ganymede (coloured symbols) lie on the same regression within factors of order unity. Venus is omitted because its present-day dynamo is shut off. The universality of this scaling is the central empirical support for the dynamo mechanism being universal across the solar system. Redrawn from {cite:t}`ChristensenAubert2006` and {cite:t}`OlsonChristensen2006`.
```


## Magnetosphere–solar wind interaction

A planetary magnetic field does not exist in isolation: it interacts dynamically with the **solar wind**, the continuous stream of charged particles (mostly protons and electrons) flowing outward from the Sun at speeds of 300–800 km s$^{-1}$, carrying an embedded magnetic field (the interplanetary magnetic field, or IMF) {cite:p}`Kivelson1995`.

### Magnetopause standoff distance

The boundary between the planetary magnetic field and the solar wind is the **magnetopause**. Its distance is determined by pressure balance between the solar wind dynamic pressure and the magnetic pressure of the planet's field:

$$
\frac{1}{2} \rho_{\mathrm{sw}} v_{\mathrm{sw}}^2 = \frac{B_{\mathrm{mp}}^2}{2\mu_0}
$$ (eq:magnetopause-pressure)

where $\rho_{\mathrm{sw}}$ and $v_{\mathrm{sw}}$ are the solar wind density and velocity, and $B_{\mathrm{mp}}$ is the magnetic field strength at the magnetopause. For a dipole field ($B \propto r^{-3}$), this yields a **standoff distance** of approximately:

$$
r_{\mathrm{mp}} \approx 10 \, R_\oplus
$$ (eq:magnetopause-distance)

for Earth under typical solar wind conditions. The dayside pressure-balance geometry, with bow shock, magnetosheath, and compressed dipolar field, is sketched in {numref}`fig:magnetopause-balance`.

```{figure} figures/magnetopause_pressure_balance.avif
:name: fig:magnetopause-balance
:width: 600px
:align: center

Schematic of pressure balance at the dayside magnetopause. The supersonic solar wind (green arrows, arriving from the left) is decelerated at the bow shock (orange dashed curve) and then deflected around the magnetopause (red curve), which compresses Earth's predominantly dipolar field on the dayside and stretches it into a long magnetotail on the nightside. The boundary lies at the radius $r_{\mathrm{mp}}$ where the solar wind ram pressure equals the magnetic pressure of the planetary field (Eq. {eq}`eq:magnetopause-pressure`); for Earth under typical conditions $r_{\mathrm{mp}} \approx 10\,R_\oplus$. Adapted from textbook descriptions in {cite:t}`Kivelson1995`.
```

### Magnetosphere structure

The interaction between the solar wind and the planetary field creates a complex structure {cite:p}`Kivelson1995`:

- **Bow shock:** The supersonic solar wind is decelerated to subsonic speeds at the bow shock, located roughly 3 $R_\oplus$ upstream of the magnetopause. This is analogous to the shock wave in front of a supersonic aircraft.

- **Magnetosheath:** The shocked, heated solar wind plasma flows around the magnetopause in this turbulent region between the bow shock and magnetopause.

- **Magnetotail:** On the night side, the magnetic field is stretched into a long tail extending more than 200 $R_\oplus$ downstream, where magnetic reconnection events release energy and accelerate particles.

- **Plasmasphere:** A torus of cool, dense plasma trapped on closed magnetic field lines in the inner magnetosphere, co-rotating with Earth.

The full structure, including the long magnetotail extending tens of $R_\oplus$ downstream, is shown in {numref}`fig:magnetosphere`.

```{figure} figures/magnetosphere_structure.svg
:name: fig:magnetosphere
:width: 600px
:align: center

Structure of Earth's magnetosphere, showing the bow shock, magnetopause, magnetosheath, magnetotail, and Van Allen radiation belts. The solar wind (arriving from the left) is deflected around the magnetopause, while the magnetic field is compressed on the dayside and stretched into a long tail on the nightside. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

### Auroral processes

When solar wind particles enter the magnetosphere (primarily through reconnection events in the magnetotail), they are channelled along magnetic field lines toward the polar regions. As these energetic particles (mostly electrons) plunge into the upper atmosphere, they collide with atmospheric atoms and molecules, exciting them to emit light. This is the **aurora** (aurora borealis in the north, aurora australis in the south) {cite:p}`Kivelson1995`:

- **Green light** (557.7 nm): Excited atomic oxygen, O, at altitudes of ~100–200 km
- **Red light** (630.0 nm): Excited atomic oxygen at higher altitudes (~200–400 km)
- **Blue/violet light**: Excited molecular nitrogen, $\mathrm{N_2}$, at lower altitudes

Aurorae are observed on other magnetised planets as well ({numref}`fig:aurora`): Jupiter's UV aurorae ({numref}`fig:jupiter-aurora`), powered by its enormous magnetosphere and the volcanic output of Io, are among the most luminous in the solar system.

```{figure} figures/aurora.avif
:name: fig:aurora
:width: 550px
:align: center

The aurora australis (southern lights) photographed from the International Space Station. Charged particles from the solar wind, channelled along Earth's magnetic field lines into the polar regions, excite atmospheric oxygen and nitrogen to produce the characteristic green and red glow. Credit: NASA/ISS Crew Earth Observations, public domain.
```

```{figure} figures/jupiter_uv_aurora.avif
:name: fig:jupiter-aurora
:width: 550px
:align: center

Ultraviolet aurora at Jupiter's north pole, imaged by the Hubble Space Telescope. The bright auroral oval is powered by Jupiter's rapid rotation, by particles from the Io plasma torus, and by interactions with the solar wind, making it the most luminous aurora in the solar system; Jovian aurorae are largely persistent rather than driven by solar wind variability as on Earth. The composite shows the UV aurora overlaid on an optical Hubble image of the planet. Credit: NASA, ESA, J. Nichols (University of Leicester).
```

### Van Allen radiation belts

Earth's magnetosphere traps energetic charged particles in two toroidal regions known as the **Van Allen radiation belts** {cite:p}`dePaterLissauer2010`:

- **Inner belt** (centred at $\sim 1.5 \, R_\oplus$): Primarily energetic protons (10–100 MeV), produced by the decay of neutrons created in cosmic ray collisions with the atmosphere.
- **Outer belt** (centred at $\sim 4$–$5 \, R_\oplus$): Primarily energetic electrons (0.1–10 MeV), injected during geomagnetic storms and accelerated by wave–particle interactions.

The radiation belts ({numref}`fig:van-allen-belts`) pose a hazard to spacecraft electronics and to astronauts. They also demonstrate the double-edged nature of magnetic fields: while the magnetosphere shields the surface from the bulk of the solar wind, it also traps a population of highly energetic particles that would not be present without the field.

```{figure} figures/van_allen_belts.svg
:name: fig:van-allen-belts
:width: 550px
:align: center

Cross-section of Earth's Van Allen radiation belts. The inner belt of energetic protons (10–100 MeV) is centred at $\sim 1.5\,R_\oplus$ and is largely stable; the outer belt of energetic electrons (0.1–10 MeV) is centred at $\sim 4$–$5\,R_\oplus$ and is highly variable, expanding and contracting in response to geomagnetic storms. Both populations are confined to closed magnetic field lines that thread the inner magnetosphere. Credit: Booyabazooka / NASA, public domain (Wikimedia Commons).
```


## Recent advances

NASA's Juno mission has produced the most detailed map of Jupiter's magnetic field to date {cite:p}`Connerney2022`. The data reveal a surprisingly complex field morphology: in the northern hemisphere, the field shows strong non-dipolar features, including a localised patch of reversed polarity (the "Great Blue Spot") that may reflect the dynamics of a deep-seated dynamo operating in the metallic hydrogen layer ({ref}`Lecture 8 <lecture08>`). These measurements provide direct constraints on the depth and nature of convection driving Jupiter's dynamo.

### InSight: no present-day Mars dynamo

NASA's **InSight** lander, operating on the Martian surface from 2018 to 2022, carried a magnetometer that recorded the local crustal field at Elysium Planitia. The measurements showed a static crustal field of $\sim 2000$ nT at the landing site, ten times stronger than satellite-based models had predicted, with time-varying signals of ionospheric origin but no global dynamo field {cite:p}`Johnson2020`. Combined with InSight seismic inferences of a fully liquid but light-element-rich core (core radius $\approx 1830$ km, mean density $\approx 6.0$ g cm$^{-3}$) {cite:p}`Stahler2021`, this supports the scenario that Mars's dynamo shut off early because compositional buoyancy from inner-core growth never began and thermal convection alone could not sustain the dynamo once the initial heat-of-accretion budget was exhausted. The exact age of the dynamo shutdown remains uncertain. The original basin-demagnetisation analysis of {cite:t}`Acuna1999` placed it at $\sim 4.1$ Gyr; subsequent low-altitude *MAVEN* magnetometer data refined the picture to a longer-lived or episodic dynamo lasting until $\sim 3.7$ Gyr {cite:p}`Mittelholz2020` (see {ref}`Lecture 10 <lecture10>` for the full chronology).

### The lunar dynamo paradox

Paleomagnetic measurements of Apollo samples have established that the Moon itself once hosted a core dynamo. The remanent magnetisation of lunar rocks returned by Apollo 15, 16, and 17 implies paleofield strengths of tens of microtesla in the high-field epoch from $\sim 3.85$ to $\sim 3.56$ Ga (mean $\sim 77\,\mu$T), dropping below $\sim 7\,\mu$T by $\sim 3.3$ Ga {cite:p}`Weiss2014`. A microtesla-scale field at a body with only $\sim 400$ km liquid core radius is difficult to generate by purely thermal convection; proposed mechanisms include differential rotation of the core driven by tidal or impact-induced torques, and compositional buoyancy from core crystallisation similar to the scenarios proposed for Mercury and Ganymede ({numref}`fig:dynamo-scaling`).

### The Earth inner-core age debate

Earth's inner core is widely thought to have nucleated sometime in the past $\sim 1$ Gyr. Two independent approaches converge on very different ages. A thermal-evolution argument, pinned to the high thermal conductivity of iron inferred from first-principles calculations {cite:p}`Labrosse2015`, yields an inner-core age of only $\sim 0.5$–$1$ Gyr. Older thermal-evolution estimates based on lower assumed conductivities favoured ages of $\sim 2$–$3$ Gyr, now largely disfavoured. Paleomagnetic records of the strength of Earth's dipole field show a pulse of intensified field $\sim 0.5$–$1.0$ Gyr ago that has been interpreted as the initiation of compositional convection from a nucleating inner core {cite:p}`Nimmo2015`. Together these lines of evidence place inner-core nucleation near the Proterozoic-Phanerozoic boundary, with important implications for Earth's long-term thermal history: before inner-core nucleation the geodynamo was purely thermally driven, and the apparent survival of the field for $\sim 3$ billion years in that regime requires higher core heat flows than the present-day compositional-convection regime demands.

### BepiColombo, JUICE, and Europa Clipper

ESA/JAXA's **BepiColombo** mission has completed multiple Mercury flybys en route to orbital insertion in late $2026$, providing new measurements of Mercury's magnetosphere. Preliminary data confirm Mercury's weak but active dipolar field. Once in orbit, BepiColombo's simultaneous operation of two orbiters (the Mercury Planetary Orbiter and Mio) will allow direct correlation of in-situ magnetospheric measurements with surface and interior constraints {cite:p}`Benkhoff2021`.

ESA's **JUICE** mission, en route to the Jupiter system, will conduct the first detailed investigation of Ganymede's intrinsic magnetic field, the only moon in the solar system known to generate its own dynamo. Understanding how a body as small as Ganymede ($R = 2634$ km) maintains an active dynamo remains an open question in planetary magnetism, with implications for the thermal state and composition of its iron core.

NASA's **Europa Clipper** (launched 2024, arriving at Jupiter in 2030) carries a magnetometer that will precisely measure the induced magnetic signature of Europa's subsurface ocean as it crosses Jupiter's magnetospheric field. This provides a strong constraint on the salinity and thickness of the ocean and, indirectly, on the thermal state of Europa's rocky core ({ref}`Lecture 8 <lecture08>`). While Europa does not have its own dynamo, its induced response to Jupiter's ambient field is one of the cleanest examples of magnetic-field-based remote sensing of a planetary interior; the habitability implications of the ocean it probes are taken up in {ref}`Lecture 14 <lecture14>`.


## Looking ahead to Lecture 5

This lecture ended with a planet that has a core, a mantle, a magnetic field, and a freshly outgassed secondary atmosphere. {ref}`Lecture 5 <lecture05>` picks up that atmosphere and asks what it looks like: how primary, secondary, and tertiary atmospheres differ, how pressure and temperature vary with height under hydrostatic equilibrium, how the greenhouse effect sets the surface temperature, and how atmospheres are lost to space. The magnetic shielding story from this lecture returns there as one control on escape, alongside the thermal escape processes that magnetic fields cannot stop.

## References

```{bibliography}
:filter: docname in docnames
```
