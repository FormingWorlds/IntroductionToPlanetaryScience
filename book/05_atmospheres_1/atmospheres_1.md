(lecture05)=
# Atmospheres I: Composition, Structure, & Energy Balance

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to classify atmospheric types (primary, secondary, tertiary), derive pressure–temperature profiles from hydrostatic equilibrium, explain the greenhouse effect and planetary energy balance, and evaluate atmospheric escape mechanisms.
```

```{seealso}
**Slides:** [Download Lecture 5 (PDF)](../_static/slides/lecture05.pdf)
```

## Atmospheric composition

A planet's atmosphere is the thin gaseous envelope that separates its surface (or cloud tops) from the vacuum of space ({numref}`fig:thin-blue-line`). Atmospheres play an outsized role in determining a planet's surface conditions (temperature, pressure, radiation environment, and chemistry) and are therefore central to questions of habitability. Understanding where atmospheres come from, what they are made of, and how they evolve is one of the core themes of planetary science {cite:p}`Catling2017`.

```{figure} figures/earth_thin_blue_line.avif
:name: fig:thin-blue-line
:width: 600px
:align: center

Earth's atmosphere as a thin blue line on the limb, photographed from the International Space Station during the STS-129 mission (November 2009). The atmosphere contains 99% of its mass below $\sim$30 km altitude (a mere 0.5% of Earth's radius), yet this slender layer controls the surface temperature, shields life from harmful radiation, and mediates the exchange of volatiles between the interior and space. Credit: NASA/ISS Expedition 21 crew, public domain.
```





### Primary atmospheres

**Primary atmospheres** are captured directly from the protoplanetary disk during planet formation. Because the disk is composed predominantly of hydrogen and helium (reflecting the solar composition), primary atmospheres are dominated by $\mathrm{H_2}$ and He, with trace amounts of $\mathrm{CH_4}$, $\mathrm{NH_3}$, $\mathrm{H_2O}$, and noble gases.

Only sufficiently massive bodies (those exceeding roughly $5$–$10 \, \Mearth$) can gravitationally capture and retain large quantities of nebular gas before the disk disperses (within $\sim$3–10 Myr; {ref}`Lecture 2 <lecture02>`). The **gas giants** Jupiter and Saturn are the primary examples: their massive $\mathrm{H_2}$/He envelopes constitute the vast majority of their total mass. The **ice giants** Uranus and Neptune also captured primary atmospheres, but far less gas: their envelopes are only $\sim$10–20% of their total mass, which reflects their slower growth and the disk's dissipation.

Terrestrial planets like Earth, Venus, and Mars were too small to capture much nebular gas. Any primordial hydrogen they did accrete was quickly lost to space (see [atmospheric escape](atm-escape) below). Their present-day atmospheres are therefore **not** primary.

### Secondary atmospheres

**Secondary atmospheres** are produced by **outgassing**: the release of volatiles from the planet's interior through volcanism and magma ocean degassing. As discussed in {ref}`Lecture 4 <lecture04>`, the speciation of outgassed volatiles depends on the **oxygen fugacity** of the magma (an effective partial pressure of $\mathrm{O_2}$ that measures how oxidising or reducing the melt is): oxidising conditions produce $\mathrm{CO_2}$, $\mathrm{H_2O}$, and $\mathrm{N_2}$, while reducing conditions produce $\mathrm{H_2}$, CO, and $\mathrm{N_2}$ {cite:p}`Hirschmann2012`.

The present-day atmospheres of **Venus** ($\mathrm{CO_2}$-dominated) and **Mars** ($\mathrm{CO_2}$-dominated but much thinner) are essentially secondary atmospheres: their compositions reflect volcanic outgassing with relatively modest subsequent modification. Titan's thick $\mathrm{N_2}$ atmosphere also originated from outgassing (likely from the conversion of accreted $\mathrm{NH_3}$).

### Tertiary atmospheres

**Tertiary atmospheres** have been substantially modified from their outgassed composition by surface processes, photochemistry, or biology. Earth is the prime example: its original outgassed atmosphere was likely dominated by $\mathrm{CO_2}$ and $\mathrm{N_2}$ (similar to Venus), but billions of years of biological activity, particularly oxygenic photosynthesis, have transformed it into the $\mathrm{N_2}$/$\mathrm{O_2}$ atmosphere we breathe today. Earth's atmospheric $\mathrm{O_2}$ (21% by volume) is entirely biogenic: it would disappear within a few million years if photosynthesis ceased {cite:p}`Catling2017`.

### Comparative atmospheric properties

The diversity of atmospheres across the solar system is remarkable. The table below compares key properties for five representative bodies:

| Property | Venus | Earth | Mars | Jupiter | Titan |
|----------|:-----:|:-----:|:----:|:-------:|:-----:|
| Surface pressure (bar) | 92 | 1.0 | 0.006 | n/a | 1.5 |
| Surface temperature (K) | 737 | 288 | 215 | n/a | 94 |
| Dominant gas | $\mathrm{CO_2}$ (96.5%) | $\mathrm{N_2}$ (78%) | $\mathrm{CO_2}$ (95%) | $\mathrm{H_2}$ (86%) | $\mathrm{N_2}$ (95%) |
| Secondary gas | $\mathrm{N_2}$ (3.5%) | $\mathrm{O_2}$ (21%) | $\mathrm{N_2}$ (2.7%) | He (14%) | $\mathrm{CH_4}$ (5%) |
| Mean molecular weight $\mu$ | 43.4 | 28.97 | 43.3 | 2.2 | 28.6 |
| Atmosphere type | Secondary | Tertiary | Secondary | Primary | Secondary |

Data from {cite:p}`dePaterLissauer2010` and {cite:p}`NASAFactSheet`. The fractional composition of these five atmospheres is shown in {numref}`fig:composition-bar`; {numref}`fig:venera13-venus` gives a vivid sense of what a 92-bar $\mathrm{CO_2}$ atmosphere looks like at the surface.

```{figure} figures/composition_bar.avif
:name: fig:composition-bar
:width: 100%
:align: center

Atmospheric composition (by volume) for five representative solar system bodies. Venus and Mars are $\mathrm{CO_2}$-dominated secondary atmospheres; Earth's $\mathrm{N_2}$/$\mathrm{O_2}$ mix is biogenically modified (tertiary); Jupiter retains a primary $\mathrm{H_2}$/He envelope; Titan's massive $\mathrm{N_2}$ atmosphere is unusual for such a small body. Numbers rounded to one decimal place. Data from {cite:p}`NASAFactSheet`.
```

```{figure} figures/venera13_venus_surface.avif
:name: fig:venera13-venus
:width: 500px
:align: center

The surface of Venus photographed in colour by the Soviet *Venera 13* lander on 1 March 1982. The image shows flat basaltic rock slabs and soil under an orange sky coloured by the thick $\mathrm{CO_2}$ atmosphere (surface pressure 92 bar, temperature 737 K); the striped bar is a colour calibration target, and the toothed ring is part of the lander. The lander survived for 127 minutes before succumbing to the extreme conditions, a vivid demonstration of how a massive secondary atmosphere transforms a planet's surface environment. Credit: USSR Academy of Sciences / NASA NSSDC, public domain.
```


## Hydrostatic equilibrium

The vertical structure of any atmosphere is governed by the balance between **gravity** pulling gas downward and the **pressure gradient** pushing it upward. This balance, called **hydrostatic equilibrium**, is the most fundamental equation of atmospheric physics.

### Derivation

Consider a thin horizontal slab of atmosphere with cross-sectional area $A$, thickness $\dd z$, and density $\rho(z)$ at height $z$ above the surface. The forces on this slab are:

- **Pressure from below** (pushing up): $P(z) \cdot A$
- **Pressure from above** (pushing down): $P(z + \dd z) \cdot A$
- **Weight** (pulling down): $\rho(z) \, g \, A \, \dd z$

```{figure} figures/hydrostatic_slab.avif
:name: fig:hydrostatic-slab
:width: 100%
:align: center

Force balance on a thin horizontal slab of atmosphere with cross-sectional area $A$, thickness $\dd z$, and density $\rho(z)$. Pressure acting on the lower face pushes the slab up with force $P(z)\,A$ (blue), while pressure on the upper face pushes down with force $P(z+\dd z)\,A$ (blue) and gravity pulls the slab down with its weight $\rho(z)\,g\,A\,\dd z$ (red). Setting the net force to zero and taking the limit $\dd z \to 0$ yields the equation of hydrostatic equilibrium.
```

In equilibrium, the net upward pressure force balances the weight:

$$
P(z) \, A - P(z + \dd z) \, A = \rho(z) \, g \, A \, \dd z
$$

Dividing by $A \, \dd z$ and taking the limit $\dd z \to 0$, in which $[P(z + \dd z) - P(z)]/\dd z$ becomes the derivative $\dv{P}{z}$:

$$
\dv{P}{z} = -\rho \, g
$$ (eq:hydrostatic-equilibrium)

This is the **equation of hydrostatic equilibrium**. The pressure decreases with altitude because each layer must support the weight of everything above it. The minus sign reflects that pressure decreases as height increases.

### The ideal gas law in atmospheric form

To solve Eq. {eq}`eq:hydrostatic-equilibrium`, we need a relation between pressure and density. For an atmosphere behaving as an ideal gas:

$$
P = n \kB T = \frac{\rho \kB T}{\mu \, m_u}
$$ (eq:ideal-gas-atm)

where $n$ is the number density, $\kB = 1.381 \times 10^{-23}$ J K$^{-1}$ is the Boltzmann constant, $T$ is the temperature, $\mu$ is the mean molecular weight (in atomic mass units), and $m_u = 1.661 \times 10^{-27}$ kg is the atomic mass unit.

### The barometric formula

If we assume the atmosphere is **isothermal** (constant $T$) and that $g$ is constant (valid for the lower atmosphere where $z \ll R_{\text{planet}}$), we can substitute the ideal gas law into the hydrostatic equation. From Eq. {eq}`eq:ideal-gas-atm`, $\rho = P \mu m_u / (\kB T)$, so:

$$
\dv{P}{z} = -\frac{P \mu \, m_u \, g}{\kB T}
$$

This is a separable first-order ODE. Integrating from the surface ($z = 0$, $P = P_0$) to height $z$:

$$
P(z) = P_0 \exp\!\left(-\frac{z}{H}\right)
$$ (eq:barometric-formula)

where we have defined the **pressure scale height** $H$:

$$
H = \frac{\kB T}{\mu \, m_u \, g}
$$ (eq:scale-height-preview)

The barometric formula tells us that atmospheric pressure decreases **exponentially** with altitude. Every scale height $H$, the pressure drops by a factor of $e \approx 2.718$. This exponential decay is why atmospheres are thin compared to the size of the planet: for an isothermal column, 99% of the mass lies below $4.6\,H$; in the real atmosphere, colder layers aloft compress this to $\sim$30 km for Earth ({numref}`fig:thin-blue-line`).


## Blackboard derivation: The atmospheric scale height

```{admonition} Blackboard derivation: Atmospheric scale height from hydrostatic equilibrium
:class: tip

**Goal:** Derive the atmospheric scale height $H = \kB T / (\mu \, m_u \, g)$ from hydrostatic equilibrium combined with the ideal gas law, and compute $H$ for Earth, Mars, Venus, Jupiter, and Titan.

**Setup.**

We start from the equation of hydrostatic equilibrium (Eq. {eq}`eq:hydrostatic-equilibrium`) and the ideal gas law (Eq. {eq}`eq:ideal-gas-atm`):

$$
\dv{P}{z} = -\rho \, g \qquad \text{and} \qquad P = \frac{\rho \kB T}{\mu \, m_u}
$$

Our goal is to find the characteristic length scale over which pressure varies: the **scale height**.

**Derivation.**

Rearranging the ideal gas law to express $\rho$ in terms of $P$:

$$
\rho = \frac{P \, \mu \, m_u}{\kB T}
$$

Substituting into the hydrostatic equation:

$$
\dv{P}{z} = -\frac{\mu \, m_u \, g}{\kB T} \, P
$$

This has the form $\dv{P}{z} = -P/H$, where:

$$
\boxed{H = \frac{\kB T}{\mu \, m_u \, g}}
$$ (eq:scale-height)

The scale height has a clear physical interpretation:

- **Higher temperature** $T$ → larger $H$: hotter gas has more thermal energy, so it extends further against gravity.
- **Heavier molecules** (larger $\mu$) → smaller $H$: heavier molecules are harder to loft.
- **Stronger gravity** $g$ → smaller $H$: stronger gravity compresses the atmosphere more.

**Application: scale heights across the solar system.**

We can now compute scale heights for several bodies using their characteristic atmospheric temperatures, compositions, and surface gravities:

| Body | $T$ (K) | $\mu$ | $g$ (m s$^{-2}$) | $H$ (km) |
|------|:-------:|:-----:|:-----------------:|:---------:|
| Venus | 737 | 43.4 | 8.87 | 15.9 |
| Earth | 288 | 28.97 | 9.81 | 8.4 |
| Mars | 215 | 43.3 | 3.72 | 11.1 |
| Jupiter | 165 | 2.2 | 24.8 | 25 |
| Titan | 94 | 28.6 | 1.35 | 20 |

**Worked example for Earth:**

$$
H_\oplus = \frac{1.381 \times 10^{-23} \times 288}{28.97 \times 1.661 \times 10^{-27} \times 9.81} = \frac{3.98 \times 10^{-21}}{4.72 \times 10^{-25}} \approx 8400 \text{ m} \approx 8.4 \text{ km}
$$

This matches our everyday experience: commercial aircraft cruise at $\sim$10–12 km altitude, where the pressure is roughly $0.2$–$0.3$ atm (about 1.2–1.4 scale heights up).

**Note:** Jupiter's scale height is large despite its strong gravity because $\mathrm{H_2}$ has a very low molecular weight ($\mu = 2.2$). Titan's scale height is large because its gravity is weak ($g = 1.35$ m s$^{-2}$): Titan's atmosphere extends to a proportionally much greater height than Earth's, despite being colder.
```


## Vertical structure

Real atmospheres are not isothermal: temperature varies with altitude, creating distinct **layers** characterised by different physical processes. These layers are defined by the sign of the temperature gradient $\dv{T}{z}$.

### Troposphere

The **troposphere** is the lowest layer, heated primarily from below by the surface (which absorbs sunlight and re-emits thermal radiation). Warm air near the surface rises, cool air aloft sinks: this is **convection**, the same process we encountered in planetary interiors ({ref}`Lecture 3 <lecture03>`). Convection keeps the troposphere well-mixed and imposes a characteristic temperature decrease with altitude called the **lapse rate**.

For a parcel of dry air rising adiabatically (without exchanging heat with its surroundings), the temperature decreases at the **dry adiabatic lapse rate**:

$$
\Gamma_d = -\dv{T}{z} = \frac{g}{c_p}
$$ (eq:dry-adiabat)

where $c_p$ is the specific heat capacity at constant pressure. For Earth, $g = 9.81$ m s$^{-2}$ and $c_p \approx 1004$ J kg$^{-1}$ K$^{-1}$ (for dry air), giving $\Gamma_d \approx 9.8$ K km$^{-1}$. The observed average lapse rate ($\sim 6.5$ K km$^{-1}$) is lower because of latent heat released by condensing water vapour, which warms a rising parcel relative to a dry one and so reduces the cooling rate. The lapse rate of a saturated parcel undergoing reversible condensation is the **moist adiabatic lapse rate** ({numref}`fig:dry-moist-adiabat`).

```{figure} figures/dry_moist_adiabat.avif
:name: fig:dry-moist-adiabat
:width: 100%
:align: center

Dry adiabatic lapse rate ($\Gamma_d = g/c_p \approx 9.8$ K km$^{-1}$, dashed) compared with a representative saturated moist adiabat ($\sim 5$ K km$^{-1}$ in the warm lower troposphere, dotted) and the US Standard Atmosphere 1976 reference profile (solid), a defined standard for year-round midlatitude conditions {cite:p}`USStandardAtmosphere1976`. The moist adiabat is shallower than the dry adiabat because condensing water vapour releases latent heat to the rising parcel; the reference profile's tropospheric lapse rate (6.5 K km$^{-1}$, close to the observed midlatitude mean) lies between the two limits. Above the tropopause the adiabats no longer apply: the profile becomes nearly isothermal and then warms in the stratosphere.
```

Earth's troposphere extends from the surface to the **tropopause** at $\sim$12 km altitude (varying from $\sim$8 km at the poles to $\sim$17 km at the equator).

### Stratosphere

Above the tropopause, temperature increases with altitude in the **stratosphere**. On Earth, this temperature inversion is caused by the absorption of solar ultraviolet radiation by the **ozone layer** ($\mathrm{O_3}$), centred at $\sim$25 km altitude. The heating by UV absorption creates a stable, non-convective layer: air parcels displaced upward find themselves cooler and denser than their surroundings and sink back down.

Earth's stratosphere extends to the **stratopause** at $\sim$50 km.

### Mesosphere and thermosphere

Above the stratopause, the **mesosphere** (50–85 km) cools with altitude again as ozone heating diminishes. The **mesopause** at $\sim$85 km is the coldest point in Earth's atmosphere ($\sim$190 K).

Above this, the **thermosphere** (85–600 km) is heated by the absorption of extreme ultraviolet (EUV) radiation and energetic particles. Temperatures rise steeply to $>$1000 K, but the gas is so rarefied that this "temperature" (reflecting the kinetic energy of individual molecules) would not feel hot. The thermosphere merges into the **exosphere**, the outermost region where the mean free path (the average distance a molecule travels between collisions) exceeds the scale height, and molecules on ballistic trajectories can escape to space. The full layered structure of Earth's atmosphere with its named pause levels is shown in {numref}`fig:earth-tz-layers`.

```{figure} figures/earth_tz_layers.avif
:name: fig:earth-tz-layers
:width: 100%
:align: center

Earth's vertical temperature profile from the US Standard Atmosphere 1976, with the four named layers (troposphere, stratosphere, mesosphere, thermosphere) shaded. Pause levels (tropopause $\sim$11 km, stratopause $\sim$50 km, mesopause $\sim$85 km) are marked with dashed grey lines. The sign of $\dv{T}{z}$ flips at each pause, which reflects the transition between dominant heating sources (surface re-radiation in the troposphere, ozone UV absorption in the stratosphere, EUV absorption in the thermosphere). Data: US Standard Atmosphere 1976 {cite:p}`USStandardAtmosphere1976`; plot generated for this course.
```

### Comparative vertical structures

The vertical structure varies dramatically across the solar system {cite:p}`Catling2017`:

- **Venus:** A massive troposphere extends to $\sim$65 km. Above the cloud deck ($\sim$48–70 km), temperature decreases slowly. There is no Earth-like stratospheric temperature inversion because Venus lacks an ozone layer.
- **Mars:** A thin troposphere ($\sim$40 km) directly overlain by a thermosphere. Mars also lacks an appreciable ozone layer and stratospheric inversion.
- **Jupiter:** The troposphere extends deep into the planet (hundreds of kilometres). The stratosphere is heated by $\mathrm{CH_4}$ and hydrocarbon haze absorption. There is no solid surface; pressure increases continuously with depth.
- **Titan:** A thick troposphere ($\sim$40 km), a stratosphere extending up to $\sim$300 km heated by organic haze absorption ({numref}`fig:titan-haze`), and an extended thermosphere reaching $\sim$1400 km, remarkably high for such a small body, which reflects Titan's weak gravity and large scale height. The Huygens-derived T(z) profile is shown in {numref}`fig:titan-tz-hasi`; the canonical Venus T(z) used for comparison is shown in {numref}`fig:venus-tz-vira`.

```{figure} figures/titan_haze_pia06160.avif
:name: fig:titan-haze
:width: 500px
:align: center

Detached haze layers in Titan's upper atmosphere imaged at the limb by the Cassini ISS narrow-angle camera (PIA06160). Multiple distinct layers from $\sim$200 km up to $\sim$500 km altitude are produced by photochemistry of $\mathrm{CH_4}$ in the stratosphere, generating the organic aerosols that give Titan its orange colour and heat the stratosphere by absorbing UV. Credit: NASA/JPL/Space Science Institute, public domain.
```

```{figure} figures/fulchignoni2005_titan_tz.avif
:name: fig:titan-tz-hasi
:width: 100%
:align: center

Titan's atmospheric temperature profile from the *Huygens* Atmospheric Structure Instrument (HASI) descent on 14 January 2005. Solid line: HASI measurements; dashed line: pre-encounter Titan engineering model. Above 160 km, $T$ and $P$ are derived from the measured density via the ideal gas law; below 160 km, $T$ is measured directly by the TEM sensor. Horizontal markers indicate the mesopause (152 K at 490 km), stratopause (186 K at 250 km), and tropopause (70.43 K at 44 km). Wave-like fluctuations above 250 km reflect gravity-wave activity (buoyancy-driven oscillations of displaced air parcels, unrelated to gravitational waves in general relativity) that complements the haze-layer UV absorption (cf. {numref}`fig:titan-haze`). Reproduced from {cite:p}`Fulchignoni2005`, Fig. 2.
```

```{figure} figures/venus_tz_vira.avif
:name: fig:venus-tz-vira
:width: 100%
:align: center

Venus T(z) profile combining Pioneer Venus / VIRA {cite:p}`Seiff1985` lower-atmosphere data with VeRa (Venus Express) radio-occultation results {cite:p}`Tellmann2009`. The profile falls monotonically from the 737 K, 92 bar surface through the cloud deck (48 to 70 km, shaded) to the mesopause near 100 km, with no ozone-driven stratospheric inversion. The near-adiabatic deep troposphere reflects efficient convection in a $\mathrm{CO_2}$-dominated, optically thick atmosphere. Pedagogical fit; not a direct reproduction.
```

A striking unifying observation is that, despite differences of orders of magnitude in surface gravity, composition, and stellar irradiation, the tropopause occurs at a pressure near $0.1$ bar in nearly every thick atmosphere of the solar system ({numref}`fig:tp-profiles`). {cite:t}`Robinson2014` showed that this is a consequence of pressure-dependent infrared transparency: at lower pressures the atmosphere becomes optically thin to thermal radiation, convection ceases, and any UV/shortwave absorber aloft creates a stratospheric inversion; the combination freezes in a near-universal temperature minimum near 0.1 bar.

```{figure} figures/atmosphere_tp_robinson.avif
:name: fig:tp-profiles
:width: 100%
:align: center

Measured vertical temperature profiles of seven solar system atmospheres (Venus, Earth, Titan, Jupiter, Saturn, Uranus, Neptune) plotted against pressure (note the log scale, with low pressures at the top). The tropopause, the temperature minimum separating troposphere from stratosphere, consistently occurs near 0.1 bar in Earth, Titan, and the four giant planets; Venus, which lacks a strong stratospheric inversion, shows only a weak global-mean minimum there {cite:p}`Robinson2014`. The same physics that defines layers in Earth's atmosphere produces comparable structure on the giant planets and Titan. Profiles digitized from {cite:t}`Robinson2014`, Fig. 1, and replotted; the underlying data come from spacecraft radio occultations, infrared spectroscopy, and reference atmosphere compilations.
```


## Radiative transfer basics

While convection dominates energy transport in the troposphere, **radiation** is the primary mechanism by which energy enters and leaves the atmosphere. Understanding how radiation interacts with atmospheric gases is essential for explaining why planets have the temperatures they do.

### Absorption, emission, and scattering

When a beam of radiation passes through an atmosphere, three things can happen:

1. **Absorption:** A gas molecule absorbs a photon, converting radiative energy into internal energy (vibrational, rotational, or electronic excitation). The key atmospheric absorbers are **greenhouse gases**: $\mathrm{CO_2}$, $\mathrm{H_2O}$, $\mathrm{CH_4}$, $\mathrm{O_3}$, and $\mathrm{N_2O}$. These molecules have vibrational and rotational modes that absorb strongly in the infrared, precisely the wavelengths at which warm planetary surfaces emit.

2. **Emission:** By Kirchhoff's law, any gas that absorbs radiation at a given wavelength also emits at that wavelength when it is warm. This thermal emission is the mechanism by which the atmosphere radiates energy to space.

3. **Scattering:** Photons are redirected without being absorbed. Rayleigh scattering by $\mathrm{N_2}$ and $\mathrm{O_2}$ (which goes as $\lambda^{-4}$) explains why the sky is blue and sunsets are red ({numref}`fig:rayleigh-scattering`). Mie scattering by larger particles (aerosols, cloud droplets) is less wavelength-dependent.

```{figure} figures/rayleigh_scattering.avif
:name: fig:rayleigh-scattering
:width: 100%
:align: center

Rayleigh scattering and the colour of the sky. Panel (a): two sunlight paths to the same observer, with the atmosphere thickness exaggerated for clarity. At noon the beam crosses the atmosphere nearly vertically and loses much less blue light to scattering than at sunset; the scattered blue reaches the eye from every direction, so the sky looks blue. At sunset the beam follows a slant path roughly 40 times longer (the tangent-path estimate $\sqrt{2R/H} \approx 40$ for a scale height of $H \approx 8.5$ km), so most of the blue is scattered out before arrival and the transmitted light is reddened. Panel (b): relative Rayleigh scattering cross-section $\sigma \propto \lambda^{-4}$ across the visible band, normalised to 550 nm; blue light (450 nm) is scattered about 4.4 times more strongly than red light (650 nm). Plot generated for this course.
```

The wavelength dependence of stellar versus planetary emission is the physical basis of the greenhouse effect ({numref}`fig:blackbody-spectrum`): the Sun radiates predominantly in the visible while a $\sim 300$ K planet radiates in the thermal infrared, and atmospheric gases can be opaque at one set of wavelengths while transparent at the other.

```{figure} figures/blackbody_spectrum.svg
:name: fig:blackbody-spectrum
:width: 100%
:align: center

Blackbody radiation curves for objects at several temperatures (representative of stellar and planetary emission). The Sun ($\sim$5800 K) emits primarily at visible wavelengths ($\sim$0.5 $\mu$m), while a planet at $\sim$300 K emits in the thermal infrared ($\sim$10 $\mu$m). This wavelength separation between incoming stellar radiation and outgoing planetary emission is the physical basis of the greenhouse effect: atmospheric gases can be transparent at one set of wavelengths while opaque at the other. Credit: Wikimedia Commons, public domain.
```

### Optical depth

The cumulative effect of absorption along a path through the atmosphere is quantified by the **optical depth** $\tau$:

$$
\tau = \int_0^s \kappa \, \rho \, \dd s'
$$ (eq:optical-depth)

where $\kappa$ is the **mass absorption coefficient** (m$^2$ kg$^{-1}$), $\rho$ is the gas density, and $s$ is the path length. Alternatively, using the number density $n$ and the absorption cross-section $\sigma$: $\tau = \int n \sigma \, \dd s'$.

The optical depth is dimensionless and measures how many "e-folding lengths" of absorption the radiation traverses:

- $\tau \ll 1$: **Optically thin**, most radiation passes through without being absorbed.
- $\tau \gg 1$: **Optically thick**, radiation is strongly absorbed; only photons emitted near the "top" of the absorbing layer escape.

### Beer–Lambert law

For a beam of radiation with initial intensity $I_0$ passing through a medium of optical depth $\tau$:

$$
I = I_0 \, e^{-\tau}
$$ (eq:beer-lambert)

This exponential attenuation law, the **Beer–Lambert law**, shows that intensity decreases by a factor of $e$ for each unit of optical depth traversed.

### The atmospheric photosphere concept

Just as a star has a **photosphere**, the layer from which photons escape to space, a planet's atmosphere has an effective emission level at approximately $\tau \approx 1$ (when looking from space downward at infrared wavelengths). Photons emitted from below this level are likely to be reabsorbed before escaping; photons emitted from above this level escape freely. The temperature at this $\tau \approx 1$ level determines the planet's **effective temperature** as seen from space ({numref}`fig:tau-one`) {cite:p}`Pierrehumbert2010`.

```{figure} figures/tau_one_schematic.avif
:name: fig:tau-one
:width: 100%
:align: center

The atmospheric "photosphere" concept. (a) Beer–Lambert attenuation: the transmitted intensity decreases exponentially with optical depth, $I/I_0 = e^{-\tau}$ (Eq. {eq}`eq:beer-lambert`); the $\tau = 1$ level transmits a fraction $1/e \approx 0.37$ of the incident intensity. (b) An infrared photon emitted from deep in the atmosphere ($\tau \gg 1$) is absorbed before reaching space and re-emitted in a random direction (the short arrows mark possible re-emission directions); only photons emitted from $\tau \lesssim 1$ escape freely. The effective emission level at $\tau \approx 1$ sets the planet's effective temperature as observed from space.
```


## Energy balance and the greenhouse effect

### Planetary energy balance

Every planet reaches a thermal equilibrium in which the rate of **absorbed stellar energy** equals the rate of **emitted thermal radiation**. The stellar flux received at a planet's orbital distance $d$ from its star (luminosity $L_\star$) is:

$$
F_\star = \frac{L_\star}{4\pi d^2}
$$ (eq:stellar-flux)

The planet intercepts this flux over its cross-sectional area $\pi R_p^2$ and reflects a fraction $A$ (the **Bond albedo**). The absorbed power is therefore $(1 - A) \, F_\star \, \pi R_p^2$.

In equilibrium, this absorbed power equals the thermal radiation emitted from the entire surface ($4\pi R_p^2$) at the **effective temperature** $T_{\mathrm{eff}}$ via the Stefan–Boltzmann law ({ref}`Lecture 3 <lecture03>`):

$$
(1 - A) \frac{L_\star}{4\pi d^2} \pi R_p^2 = 4\pi R_p^2 \, \sigma \, T_{\mathrm{eff}}^4
$$

Solving for $T_{\mathrm{eff}}$:

$$
T_{\mathrm{eff}} = \left[\frac{(1-A) \, L_\star}{16 \pi \sigma \, d^2}\right]^{1/4}
$$ (eq:effective-temperature)

The effective temperature is the temperature at which the planet would radiate if it had no atmosphere (or if the atmosphere were completely transparent). It depends only on the stellar luminosity, the orbital distance, and the albedo, not on any atmospheric properties.

For Earth, satellite radiometry has measured the individual flux components of the global energy budget to a few W m$^{-2}$. The leading inventory is from {cite:t}`Trenberth2009` and is shown in {numref}`fig:trenberth`:

```{figure} figures/trenberth_energy_budget.avif
:name: fig:trenberth
:width: 100%
:align: center

Earth's globally averaged energy budget in W m$^{-2}$. Of $\sim$340 W m$^{-2}$ incoming shortwave (SW) flux, $\sim$100 W m$^{-2}$ is reflected (Bond albedo $A \approx 0.30$), $\sim$80 W m$^{-2}$ is absorbed by the atmosphere, and $\sim$160 W m$^{-2}$ is absorbed at the surface. The surface re-radiates $\sim$396 W m$^{-2}$ in the longwave (LW), and the atmosphere returns $\sim$333 W m$^{-2}$ as downward back-radiation, the dominant surface heating term. Latent and sensible heat fluxes ($\sim$97 W m$^{-2}$) carry the remainder of the surface energy balance to the atmosphere. At the top of atmosphere, 340 W m$^{-2}$ in matches 100 W m$^{-2}$ reflected plus $\sim$240 W m$^{-2}$ outgoing IR. Schematic adapted from {cite:t}`Trenberth2009`.
```

### Effective vs. actual surface temperatures

The table below compares the effective temperature with the measured surface temperature for several solar system bodies:

| Body | Albedo $A$ | $d$ (AU) | $T_{\mathrm{eff}}$ (K) | $T_{\mathrm{surface}}$ (K) | $\Delta T$ (K) |
|------|:----------:|:--------:|:-----------------------:|:---------------------------:|:---------------:|
| Venus | 0.77 | 0.72 | 227 | 737 | +510 |
| Earth | 0.30 | 1.00 | 255 | 288 | +33 |
| Mars | 0.25 | 1.52 | 210 | 215 | +5 |
| Jupiter | 0.34 | 5.20 | 110 | 165* | +55 |

\*Jupiter's "surface temperature" refers to the 1-bar level.

The discrepancy $\Delta T = T_{\mathrm{surface}} - T_{\mathrm{eff}}$ reveals the strength of the **greenhouse effect**. Venus has a staggering 510 K greenhouse warming, by far the largest in the solar system. Earth's 33 K greenhouse warming, though modest by comparison, is sufficient to keep the oceans liquid. Mars has only a small greenhouse warming ($\sim 5$ K) because its CO$_2$ atmosphere is very thin (surface pressure only 6 mbar) and lacks the water-vapour amplifier that boosts the warming on Earth and Venus. Jupiter's excess temperature is partly due to internal heat left over from formation ({ref}`Lecture 3 <lecture03>`), not solely the greenhouse effect.

### The greenhouse mechanism

The greenhouse effect arises because the atmosphere is **relatively transparent** to incoming shortwave (visible) radiation from the star but **relatively opaque** to outgoing longwave (infrared) radiation from the surface. The mechanism works as follows {cite:p}`Pierrehumbert2010`:

1. Sunlight (visible wavelengths, peak $\sim$0.5 $\mu$m) passes through the atmosphere and heats the surface.
2. The warm surface emits thermal radiation at infrared wavelengths (peak $\sim$10–15 $\mu$m for $T \sim 200$–$300$ K).
3. Greenhouse gases ($\mathrm{CO_2}$, $\mathrm{H_2O}$, $\mathrm{CH_4}$, $\mathrm{O_3}$, etc.) absorb much of this outgoing IR radiation.
4. The absorbing layer re-emits IR radiation in all directions: half upward (toward space), half downward (back toward the surface).
5. The downward emission provides an **additional energy source** for the surface, raising its temperature above $T_{\mathrm{eff}}$.

The atmospheric absorption spectrum that underlies this asymmetry is shown in {numref}`fig:atmospheric-absorption`: $\mathrm{H_2O}$ and $\mathrm{CO_2}$ have strong infrared absorption bands that block outgoing surface radiation, with a relatively transparent "atmospheric window" near 8-13 $\mu$m.

```{figure} figures/atmospheric_transmission.svg
:name: fig:atmospheric-absorption
:width: 100%
:align: center

Atmospheric absorption spectrum of Earth's atmosphere from ultraviolet through infrared wavelengths. The top panel shows the solar radiation spectrum; the bottom panels show absorption by individual gases. Note the strong absorption bands of $\mathrm{H_2O}$ and $\mathrm{CO_2}$ in the infrared, and the "atmospheric window" near 8–13 $\mu$m where the atmosphere is relatively transparent. Credit: Wikimedia Commons, public domain.
```

### One-layer greenhouse model

We can quantify the greenhouse effect with a simple **one-layer model**. Consider an atmosphere represented by a single isothermal layer with **emissivity** $\varepsilon$ at infrared wavelengths (and completely transparent at visible wavelengths). The energy balance has two components:

**Atmospheric layer balance.** The layer absorbs a fraction $\varepsilon$ of the surface emission $\sigma T_s^4$ and emits $\varepsilon \sigma T_a^4$ both upward and downward:

$$
\varepsilon \, \sigma \, T_s^4 = 2 \, \varepsilon \, \sigma \, T_a^4
$$ (eq:atm-balance)

This gives $T_a^4 = T_s^4 / 2$.

**Surface balance.** The surface absorbs the incoming stellar flux plus the downward emission from the atmosphere. In equilibrium:

$$
(1-A) \frac{F_\star}{4} + \varepsilon \, \sigma \, T_a^4 = \sigma \, T_s^4
$$ (eq:surface-balance)

**Top-of-atmosphere balance.** The planet must radiate to space at its effective temperature, so $(1-A) F_\star / 4 = \sigma T_{\mathrm{eff}}^4$. Combining with the atmospheric and surface balance equations:

$$
T_s = T_{\mathrm{eff}} \left(\frac{2}{2 - \varepsilon}\right)^{1/4}
$$ (eq:greenhouse-surface-temp)

When $\varepsilon = 0$ (no greenhouse gases), $T_s = T_{\mathrm{eff}}$: no warming. When $\varepsilon = 1$ (perfect absorber), $T_s = 2^{1/4} \, T_{\mathrm{eff}} \approx 1.19 \, T_{\mathrm{eff}}$, a 19% increase in surface temperature. For Earth, this gives $T_s \approx 1.19 \times 255 \approx 303$ K, a reasonable first estimate, though the real greenhouse effect involves multiple absorbing layers and a more complex radiative transfer calculation. The flux balance is summarised in {numref}`fig:greenhouse-effect`.

```{note}
This one-layer model is deliberately simple. In {ref}`Lecture 9 <lecture09>`, we will extend this treatment to examine the **runaway greenhouse effect**: what happens when the surface temperature rises so high that the outgoing longwave radiation reaches a maximum and can no longer balance the absorbed stellar flux. This is the mechanism that likely transformed Venus from a potentially habitable world into the 737 K inferno we see today.
```

```{figure} figures/greenhouse_one_layer.avif
:name: fig:greenhouse-effect
:width: 100%
:align: center

Energy budget of the one-layer greenhouse model. Stellar shortwave flux $(1-A)F_\star/4$ (yellow) passes unimpeded through the atmosphere and is absorbed at the surface. The surface re-radiates $\sigma T_s^4$ in the infrared (red); a fraction $(1-\varepsilon)$ is transmitted directly to space, while a fraction $\varepsilon$ is absorbed in the atmospheric layer. The layer re-emits $\varepsilon\,\sigma T_a^4$ both upward (to space) and downward (back to the surface). The downward emission is the additional energy source that raises $T_s$ above the no-atmosphere effective temperature $T_\mathrm{eff}$. Schematic following the one-layer derivation in {cite:t}`Pierrehumbert2010`.
```


(atm-escape)=
## Atmospheric escape

An atmosphere is not permanent. Over geological time, gas molecules can be lost to space through several physical mechanisms. The balance between outgassing supply and escape loss determines a planet's atmospheric mass and composition over its history {cite:p}`Lammer2008`.

The dominant escape regime for a given planet-species pair depends on two quantities: the **Jeans escape parameter** $\lambda_J$ (the ratio of gravitational binding energy to thermal energy at the exobase, the altitude above which the atmosphere becomes collisionless) and the incident **EUV flux** from the host star (which heats the upper atmosphere and drives bulk outflow). Low $\lambda_J$ or high EUV flux pushes the system into hydrodynamic outflow, a bulk, wind-like escape of the entire upper atmosphere; high $\lambda_J$ with low EUV flux corresponds to the retention regime in which escape is negligible on Gyr timescales. Thermal escape is not the only loss channel: the stellar wind and a planetary magnetic field enable or suppress several additional escape processes, summarised in {numref}`fig:escape-overview`.

```{figure} figures/escape_processes_gronoff2020.avif
:name: fig:escape-overview
:width: 100%
:align: center

Overview of the main atmospheric escape processes and the conditions under which each operates. The central column lists the processes that act on both magnetised and unmagnetised planets, powered mainly by the stellar EUV flux: thermal escape (Jeans and hydrodynamic), photochemical escape, and bulk ion escape. On unmagnetised planets such as Venus and Mars (left), the stellar wind interacts directly with the upper atmosphere and drives sputtering, ion pickup, and charge exchange. On magnetised planets such as Earth (right), the magnetic field deflects the stellar wind but channels ions into ionospheric outflow along open field lines and permits charge exchange of magnetospherically trapped ions. Each process operates either near the exobase, the altitude above which the atmosphere becomes collisionless, or in the extended region above it. Reproduced from {cite:t}`Gronoff2020`, Fig. 2.
```

### Thermal (Jeans) escape

The most fundamental escape mechanism is **Jeans escape**, which arises from the thermal velocity distribution of gas molecules. In a gas at temperature $T$, molecules have a range of speeds described by the Maxwell–Boltzmann distribution. The mean thermal speed is $v_{\mathrm{th}} \sim \sqrt{\kB T / m}$, where $m$ is the molecular mass. Most molecules are far too slow to escape, but the tail of the distribution extends to arbitrarily high speeds, and some molecules in this high-velocity tail exceed the escape speed.

The **exobase** ({numref}`fig:exobase`) is the altitude at which the mean free path $\ell = 1/(n \sigma)$, with $\sigma$ an effective collision cross-section, equals the pressure scale height $H$. Below this level, collisions dominate and the gas behaves as a fluid; above it, collisions are rare enough that molecules travel on ballistic trajectories, and those with $v > v_\mathrm{esc}$ escape to space without further interaction. For Earth, the exobase sits near 500 km altitude; for Mars, closer to 200 km.

```{figure} figures/exobase_definition.avif
:name: fig:exobase
:width: 100%
:align: center

The exobase as the altitude where the mean free path $\ell$ (blue) equals the pressure scale height $H$ (red dashed) in Earth's upper atmosphere. Below the crossing (blue shading) the atmosphere is collisional (thermosphere); above it (orange shading) the atmosphere is effectively collisionless (exosphere) and ballistic trajectories carry individual molecules to escape. The crossing altitude is approximately 450 to 500 km for present-day Earth, depending on solar activity and exobase temperature. Plot generated for this course using the US Standard Atmosphere 1976 {cite:p}`USStandardAtmosphere1976` + MSIS-86 number density and an effective cross-section $\sigma = 10^{-18}\ \mathrm{m}^2$.
```

The key parameter governing Jeans escape is the **Jeans escape parameter** $\lambda_J$, defined at the exobase:

$$
\lambda_J = \frac{G M_p \, m}{\kB T_{\mathrm{exo}} \, r_{\mathrm{exo}}} = \frac{v_{\mathrm{esc}}^2}{v_{\mathrm{th}}^2}
$$ (eq:jeans-parameter)

where $M_p$ is the planet's mass, $m$ is the molecular mass, $T_{\mathrm{exo}}$ is the exobase temperature, $r_{\mathrm{exo}}$ is the exobase radius, $v_{\mathrm{esc}} = \sqrt{2GM_p/r_{\mathrm{exo}}}$ is the escape speed, and $v_{\mathrm{th}} = \sqrt{2\kB T_{\mathrm{exo}}/m}$ is the most probable thermal speed.

The Jeans escape parameter is the ratio of gravitational binding energy to thermal energy for a molecule at the exobase. When $\lambda_J \gg 1$, very few molecules have enough energy to escape and escape is slow. When $\lambda_J \lesssim 2$–3, a substantial fraction of molecules can escape, and the atmosphere erodes rapidly.

The **Jeans escape flux** (number of molecules escaping per unit area per unit time from the exobase) is:

$$
\Phi_J = \frac{n_{\mathrm{exo}} \, v_{\mathrm{th}}}{2\sqrt{\pi}} \, (1 + \lambda_J) \, e^{-\lambda_J}
$$ (eq:jeans-flux)

where $n_{\mathrm{exo}}$ is the number density at the exobase. The exponential factor $e^{-\lambda_J}$ shows that escape is extremely sensitive to $\lambda_J$: a small change in temperature, gravity, or molecular mass can change the escape rate by orders of magnitude.

```{figure} figures/maxwell_boltzmann_jeans.avif
:name: fig:mb-jeans
:width: 100%
:align: center

Maxwell–Boltzmann speed distribution for atomic hydrogen at the exobase temperatures of Earth ($T_\mathrm{exo} = 1000$ K, blue) and Mars ($T_\mathrm{exo} = 270$ K, red). Dashed vertical lines mark the escape velocity $v_\mathrm{esc}$ at the exobase of each planet ($\sim$10.6 km s$^{-1}$ and $\sim$4.9 km s$^{-1}$ respectively). Only molecules in the high-speed tail above $v_\mathrm{esc}$ (shaded) contribute to Jeans escape; the exponential dependence of the tail area on $\lambda_J = v_\mathrm{esc}^2 / v_\mathrm{th}^2$ explains why escape rates vary by orders of magnitude across species and bodies.
```

The following table illustrates $\lambda_J$ for several atmospheric species on Earth and Mars, evaluated at the exobase: $T_\mathrm{exo} = 1000$ K and $r_\mathrm{exo} = R_\oplus + 500$ km for Earth, $T_\mathrm{exo} = 270$ K and $r_\mathrm{exo} = R_M + 200$ km for Mars.

| Species | $m$ (u) | $\lambda_J$ (Earth) | $\lambda_J$ (Mars) |
|---------|:-------:|:--------------------:|:-------------------:|
| H | 1 | 7.0 | 5.3 |
| $\mathrm{H_2}$ | 2 | 14 | 11 |
| He | 4 | 28 | 22 |
| $\mathrm{N_2}$ | 28 | 200 | 150 |
| $\mathrm{CO_2}$ | 44 | 310 | 230 |

For heavy species like $\mathrm{N_2}$ and $\mathrm{CO_2}$, $\lambda_J$ is so large that Jeans escape is negligible on both planets. For atomic hydrogen, $\lambda_J$ is moderate, leading to measurable escape: this is why both Earth and Mars lose hydrogen to space ({numref}`fig:mb-jeans`). Earth's exobase temperature is not fixed at 1000 K: it varies from $\sim$600 K at solar minimum to $\sim$1500 K at solar maximum, which modulates the escape flux of the lightest species by orders of magnitude. We will revisit this derivation in full detail (starting from the Maxwell–Boltzmann distribution) in {ref}`Lecture 10 <lecture10>`.

### Hydrodynamic escape

When the energy input to the upper atmosphere is very large (for example, from intense **extreme ultraviolet (EUV)** radiation from a young, active star), the escape can transition from the slow, molecule-by-molecule Jeans process to a bulk **hydrodynamic outflow** in which the entire upper atmosphere flows outward like a wind. This is analogous to the solar wind but driven by stellar heating rather than the star's own thermal energy {cite:p}`Hunten1987`. {numref}`fig:hydro-outflow` shows the structure of such an outflow from a 3D radiation-hydrodynamic simulation of a hot Jupiter: gas streams off the irradiated day side, flows around the terminator, and becomes progressively ionised as it accelerates away from the planet.

```{figure} figures/hot_jupiter_outflow_tripathi2015.avif
:name: fig:hydro-outflow
:width: 80%
:align: center

Velocity field (arrows) and neutral hydrogen fraction (colour scale) of an EUV-driven hydrodynamic outflow from a hot Jupiter (radius $2.14\ \Rjup$, mass $0.53\ \Mjup$), from the 3D radiation-hydrodynamic simulations of {cite:t}`Tripathi2015`. Axes are in units of the planetary radius $R_p$; the star is to the left. The heated gas accelerates outward from the bound atmosphere (dark red, neutral) and flows around the terminator into a partially neutral wake that flares out on the night side (right). The shear between the day-side wind and the night-side gas produces the Kelvin-Helmholtz rolls visible near $x \approx 1\,R_p$; away from the planet the outflow is almost fully ionised (light shading). Reproduced from {cite:t}`Owen2019`, Fig. 2.
```

Hydrodynamic outflows of this kind are observed directly. Ultraviolet transit spectroscopy has detected extended envelopes of escaping atomic hydrogen around the hot Jupiter HD 209458 b {cite:p}`VidalMadjar2003` and the warm Neptune GJ 436 b {cite:p}`Ehrenreich2015`, and near-infrared spectroscopy has revealed escaping helium around the warm super-Neptune WASP-107 b {cite:p}`Spake2018`.

Hydrodynamic escape is most important during a planet's first few hundred million years, when the host star's EUV luminosity is 10–100 times higher than at present. It can strip hydrogen-rich primary atmospheres from planets up to several Earth masses, and is the leading explanation for the observed **radius valley** in the exoplanet population ({numref}`fig:owen-radius-valley`), the deficit of planets with radii between $\sim$1.5 and $2 \, \Rearth$ ({ref}`Lecture 13 <lecture13>`). During hydrodynamic escape, the outflowing hydrogen can also **drag along heavier species** (such as He, C, N, O), leading to more extensive atmospheric loss than Jeans escape alone would produce {cite:p}`Hunten1987`.

```{figure} figures/radius_valley_owen2019.avif
:name: fig:owen-radius-valley
:width: 100%
:align: center

Population synthesis of close-in exoplanets that have undergone EUV-driven hydrodynamic atmospheric escape. *Left*: planet radius vs orbital separation after 10 Gyr of evolution, for cores with masses 6.5–15 $\Mearth$ (different colours indicate different core masses; the published axis label reads "Seperation" [sic] in the original figure). The "evaporation desert" at small separations and large radii is empty because all H/He envelopes have been stripped, and the "evaporation valley" appears as a thin gap near $1.5\!-\!2\,\Rearth$. *Right*: planet radius vs incident bolometric flux ($F_\oplus$, in units of Earth's), colour-coded by retained atmospheric mass fraction (% H/He). Greyscale shading shows the predicted population density. Reproduced from {cite:t}`Owen2019`, Fig. 3 (left panel originally from {cite:t}`OwenWu2013`; right panel from {cite:t}`LopezFortney2013`).
```

The observational counterpart was established by {cite:t}`Fulton2017`, who measured the planet radius distribution for short-period exoplanets in the California-Kepler Survey (CKS) and found a clear bimodality ({numref}`fig:fulton-radius-valley`):

```{figure} figures/fulton2017_radius_valley.avif
:name: fig:fulton-radius-valley
:width: 100%
:align: center

Observed radius distribution of short-period ($P < 100$ days) small planets from the California-Kepler Survey {cite:p}`Fulton2017`. Two distinct populations appear: a super-Earth peak near $1.3\ \Rearth$ (likely stripped rocky cores) and a sub-Neptune peak near $2.4\ \Rearth$ (cores with retained H/He envelopes of a few percent by mass). The gap between them near $1.8\ \Rearth$ is the observational signature of the radius valley predicted by photoevaporation models (cf. {numref}`fig:owen-radius-valley`). Completeness-corrected histogram reproduced from {cite:t}`Fulton2017`, Fig. 7 (top panel); the light grey region below $1.14\ \Rearth$ suffers from low completeness, and the population labels are added here.
```

### Non-thermal escape mechanisms

Several processes can eject atmospheric particles to space without relying on thermal energy {cite:p}`Lammer2008`:

- **Sputtering:** Energetic ions from the solar wind or magnetospheric plasma impact the upper atmosphere and transfer enough momentum to eject atmospheric molecules. This is significant for Mars, which lacks a global magnetic field to deflect the solar wind.

- **Photochemical escape:** Solar UV radiation dissociates molecules (e.g., $\mathrm{H_2O} \to$ H + OH), producing fast atoms with enough energy to escape. This is an important loss channel for hydrogen from Venus and Mars.

- **Ion pickup:** Atmospheric atoms ionised by solar UV or charge exchange are picked up by the solar wind magnetic field and swept away from the planet. This process is particularly effective at unmagnetised planets like Mars and Venus.

- **Impact erosion:** Large asteroid or comet impacts can eject a large fraction of a planet's atmosphere. The efficiency depends on the impactor size relative to the atmospheric scale height: very large impacts can blow off a substantial atmospheric mass in a single event.

The MAVEN mission at Mars has measured the present-day total atmospheric escape rate at $\sim 2$–$3$ kg s$^{-1}$ for H and O combined, with H escape varying seasonally by nearly an order of magnitude, integrated across photochemical, thermal, and solar-wind-driven channels {cite:p}`Jakosky2018`. MAVEN's elliptical science orbit ({numref}`fig:maven-science-orbit`) samples the thermosphere/exobase at periapsis and the ionised tail at apoapsis; the resulting picture of ion escape is shown in {numref}`fig:maven-ion-plume`, and the partitioning of oxygen loss across photochemical, ion, and sputtering channels is summarised in {numref}`fig:maven-o-loss-channels`. The thin atmosphere that remains today is photographed on the limb in {numref}`fig:mars-atmosphere`.

```{figure} figures/maven_science_orbit.avif
:name: fig:maven-science-orbit
:width: 650px
:align: center

MAVEN's science orbit around Mars, showing how the spacecraft transitioned from the highly elliptical Mars-orbit insertion trajectory (outermost path) through an intermediate ellipse to its final science orbit with a periapsis near $\sim$150 km altitude and an apoapsis of $\sim$6200 km. The low-altitude periapsis passes sample the thermosphere and exobase region where most species-specific escape occurs, while the higher apoapsis samples the ionised tail and pickup-ion environment downstream of Mars relative to the solar wind. The combination enables simultaneous in-situ and remote-sensing characterisation of the atmospheric-escape pathways summarised above. Credit: NASA's Scientific Visualization Studio (SVS ID 4190), public domain.
```

```{figure} figures/maven_ion_plume.avif
:name: fig:maven-ion-plume
:width: 100%
:align: center

NASA Scientific Visualization Studio rendering of the ion plume escaping from Mars, based on MAVEN data. The most energetic ions (red) are accelerated in a plume above the planet, while the bulk of escaping ions (green) are lost along the tail region behind Mars relative to the solar wind. Unmagnetised Mars is particularly vulnerable to this class of solar-wind-driven escape because the solar wind reaches deep into the upper atmosphere rather than being deflected by a global dipole field. Credit: NASA's Scientific Visualization Studio (SVS ID 4370), PI Bruce Jakosky, public domain.
```

```{figure} figures/maven_o_loss_channels.avif
:name: fig:maven-o-loss-channels
:width: 100%
:align: center

Present-day oxygen loss rates from Mars decomposed into escape channels, after {cite:t}`Jakosky2018` Fig. 6. Horizontal bars indicate the loss rate (log$_{10}$ s$^{-1}$) for O ion escape, photochemical escape, and sputtering, plus the combined total. Photochemical escape dominates the oxygen budget today; sputtering is sub-dominant at present solar activity but was likely comparable or larger in the young, EUV-active Sun epoch. The three channels sum to the total at the top of the panel and, together with hydrogen escape, give the $\sim 2$–$3$ kg s$^{-1}$ figure quoted in the text. Redrawn from {cite:t}`Jakosky2018`.
```

```{figure} figures/mars_atmosphere.avif
:name: fig:mars-atmosphere
:width: 550px
:align: center

The thin Martian atmosphere visible as a blue haze on the limb, photographed by NASA's *Viking 1* orbiter in 1976. With a surface pressure of only 6 mbar ($\sim$0.6% of Earth's), Mars's atmosphere is too thin to sustain liquid water or provide significant greenhouse warming today. Geological evidence for ancient rivers, lakes, and possibly an ocean indicates that Mars once had a much thicker atmosphere, most of which has been lost to space over the past $\sim$4 billion years through solar wind stripping and other escape processes. Credit: NASA/JPL, public domain.
```


## Atmospheric retention

Whether a planet retains its atmosphere over billions of years depends on the competition between escape processes and atmospheric sources (outgassing, volatile delivery). The outcome is controlled primarily by two parameters: the planet's **escape velocity** and the **thermal velocity** of atmospheric molecules.

### The escape velocity–temperature diagram

The classic tool for assessing atmospheric retention is a plot of escape velocity versus surface (or exosphere) temperature. Each atmospheric species occupies a characteristic region based on its thermal velocity $v_{\mathrm{th}} = \sqrt{2\kB T / m}$. The rule of thumb for long-term retention is {cite:p}`dePaterLissauer2010`:

$$
v_{\mathrm{esc}} \gtrsim 6 \, v_{\mathrm{th}}
$$

A planet retains a given gas species if its escape velocity exceeds roughly 6 times the thermal velocity of that species (corresponding to $\lambda_J \gtrsim 36$, which keeps Jeans escape negligible over billions of years).

### Solar system trends

Applying this criterion reveals a clear pattern across the solar system:

- **Gas giants** (Jupiter, Saturn): With escape velocities of 60 and 36 km s$^{-1}$ respectively, and moderate exosphere temperatures, they retain **all species**, including the lightest ($\mathrm{H_2}$, He). This is why they still possess their primary atmospheres.

- **Earth and Venus**: Escape velocities of $\sim$11 km s$^{-1}$ are sufficient to retain heavy molecules ($\mathrm{N_2}$, $\mathrm{O_2}$, $\mathrm{CO_2}$, $\mathrm{H_2O}$) but not atomic hydrogen. Earth and Venus lose H to space, which contributes to long-term water loss (via photodissociation of $\mathrm{H_2O}$ followed by H escape).

- **Mars**: With $v_{\mathrm{esc}} = 5.0$ km s$^{-1}$ and an exosphere temperature of $\sim$270 K, Mars is marginal for retaining even heavy species like $\mathrm{CO_2}$. While Jeans escape of $\mathrm{CO_2}$ is negligible, non-thermal processes (sputtering, ion pickup) have eroded most of Mars's original atmosphere over 4 billion years {cite:p}`Jakosky2018`.

- **Titan**: Despite its low escape velocity (2.6 km s$^{-1}$), Titan retains a thick $\mathrm{N_2}$ atmosphere because it is extremely **cold** ($T_{\mathrm{exo}} \approx 150$ K). Low temperature means low thermal velocities, and the Jeans parameter remains large.

- **Moon and Mercury**: With escape velocities of 2.4 and 4.3 km s$^{-1}$ and high dayside temperatures ($>$400 K), these bodies cannot retain any significant atmosphere. Mercury has only a tenuous **exosphere** (a collisionless atmosphere with surface pressure $\sim 10^{-15}$ bar).

The classic graphical summary of these competing constraints is the escape-velocity-vs-temperature diagram ({numref}`fig:escape-velocity-temperature`).

### Atmospheric evolution over time

Atmospheric retention is not simply a present-day snapshot: it evolves over a planet's lifetime {cite:p}`Lammer2008`:

- **Young stars are UV-bright:** Stars on the main sequence emit 10–100 times more EUV radiation in their first few hundred million years. This drives intense hydrodynamic escape that can strip primary atmospheres from low-mass planets.

- **Magnetic field loss:** A planet that loses its global magnetic field (like Mars $\sim$4 Gyr ago; {ref}`Lecture 4 <lecture04>`) becomes exposed to solar wind sputtering and ion pickup, accelerating atmospheric loss.

- **Outgassing replenishment:** Ongoing volcanism can replenish atmospheric gases. Earth's atmosphere is maintained in part by the continuous volcanic outgassing of $\mathrm{CO_2}$, $\mathrm{H_2O}$, and $\mathrm{SO_2}$. A planet with active tectonics (and thus active volcanism) has a better chance of maintaining its atmosphere.

- **Atmospheric chemistry:** Photochemical reactions can transform atmospheric species. For example, solar UV dissociates $\mathrm{H_2O}$ into H and O; the hydrogen escapes while the oxygen may be incorporated into surface rocks. This irreversible loss of hydrogen is the leading hypothesis for how Venus lost its primordial water inventory.

We will examine the long-term atmospheric evolution of specific planets in detail: Venus's runaway greenhouse and water loss ({ref}`Lecture 9 <lecture09>`), Mars's atmospheric collapse and escape ({ref}`Lecture 10 <lecture10>`), and the atmospheric characterisation of exoplanets ({ref}`Lecture 13 <lecture13>`). Clouds, weather, and climate feedbacks are the focus of {ref}`Lecture 6 <lecture06>`; the runaway greenhouse limit itself is derived in {ref}`Lecture 9 <lecture09>`.

```{figure} figures/escape_velocity_temperature.svg
:name: fig:escape-velocity-temperature
:width: 100%
:align: center

Escape velocity versus surface temperature for solar system bodies. Diagonal lines indicate the thermal velocity of different gas species (scaled by a factor of 6 for long-term retention). Bodies above and to the left of a species line can retain that gas; bodies below and to the right cannot. The gas giants retain everything; Earth and Venus retain heavy species but lose H; Mars and Titan are marginal; the Moon and Mercury retain essentially nothing. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```


## Recent advances

The James Webb Space Telescope (JWST) has opened a new era in exoplanet atmospheric characterisation. Thermal emission measurements of TRAPPIST-1 b, an Earth-sized planet orbiting an M dwarf, indicate a dayside temperature consistent with bare rock and no significant atmosphere ({numref}`fig:greene-trappist`) {cite:p}`Greene2023`. Similar results for TRAPPIST-1 c {cite:p}`Zieba2023` suggest that the innermost rocky planets around active M dwarfs may be stripped of their atmospheres by intense stellar irradiation, consistent with theoretical predictions of enhanced atmospheric escape around low-mass stars {cite:p}`Wordsworth2022`.

A central reason M-dwarf planets are so vulnerable to escape is that late-type stars remain in the high-activity **saturated regime** (a phase in which a star's X-ray and EUV output holds at a roughly constant fraction of its bolometric luminosity, independent of its declining rotation rate) for much longer than Sun-like stars, exposing their close-in planets to intense **XUV** (combined X-ray and extreme-ultraviolet) irradiation for $\gtrsim 1$ Gyr after formation. The mass-dependence of this XUV evolution is shown in {numref}`fig:xuv-evolution`:

```{figure} figures/johnstone2021_xuv_evolution.avif
:name: fig:xuv-evolution
:width: 100%
:align: center

Evolutionary tracks for stellar X-ray luminosity for slow, medium, and fast rotators (three coloured lines per panel) for a Sun-like star (1.0 $M_\odot$, top) and a mid-M dwarf (0.25 $M_\odot$, bottom). Shaded bands give one standard deviation around the mean track. Lower-mass stars remain in the saturated regime $L_X / L_\mathrm{bol} \sim 10^{-3}$ for far longer than Sun-like stars: $\sim 100$ Myr for $1.0\,M_\odot$, $\gtrsim 1$ Gyr for $0.25\,M_\odot$. Close-in rocky planets around late-M stars (e.g. the TRAPPIST-1 system) therefore experience prolonged high-XUV irradiation that drives sustained atmospheric escape. Reproduced from {cite:p}`Johnstone2021`, Fig. 11 (two of the four stellar-mass panels shown).
```

```{figure} figures/trappist1b_jwst_greene2023.avif
:name: fig:greene-trappist
:width: 100%
:align: center

JWST/MIRI 15 $\mu$m thermal emission measurement of TRAPPIST-1 b (black point with error bars labelled "Measured F1500W") compared with predicted spectra. The measured dayside flux matches a bare-rock blackbody at $T_B = 503$ K (blue curve), close to the 508 K blackbody predicted for zero heat redistribution and no atmosphere (green curve), and is significantly above the 400 K isotropic-redistribution blackbody (orange) that would be expected for an efficient atmospheric heat engine. The second black point ("Expected F1280W") marks the flux the bare-rock fit predicts in the neighbouring 12.8 $\mu$m band. Thick atmospheres (e.g. 93 bar $\mathrm{CO_2}$, cyan; 10 bar $\mathrm{O_2}/\mathrm{CO_2}$, magenta) absorb in the 15 $\mu$m band and would suppress the observed flux by a factor of two or more, inconsistent with the data. The result is best explained by little-to-no redistribution from a thin or absent atmosphere on the dayside of TRAPPIST-1 b. Figure from {cite:t}`Greene2023`.
```

For solar system bodies, the MAVEN mission at Mars has quantified present-day atmospheric loss rates for multiple species, establishing that ion escape driven by the solar wind dominates over Jeans escape for most atmospheric constituents {cite:p}`Jakosky2018`. Integrated over Mars's history, these loss rates can account for the removal of a substantial fraction of Mars's early atmosphere, though the total amount of $\mathrm{CO_2}$ lost to space versus sequestered in surface carbonates and the polar caps remains debated ({ref}`Lecture 10 <lecture10>`). Thermal escape of carbon under the strong EUV flux of the young Sun may in addition have prevented a dense $\mathrm{CO_2}$ atmosphere from persisting through Mars's first few hundred million years {cite:p}`Tian2009`.

These results reflect a central theme of atmospheric science: a planet's ability to retain its atmosphere depends not only on its mass and temperature (the Jeans escape criterion derived in this lecture) but also on the intensity of stellar radiation, the presence or absence of a global magnetic field ({ref}`Lecture 4 <lecture04>`), and the planet's geological activity.


## Looking ahead to Lecture 6

This lecture treated an atmosphere as a static column: its composition, its vertical structure, and the energy budget that sets its temperature. {ref}`Lecture 6 <lecture06>` sets that column in motion. Condensation turns vapour into clouds wherever the saturation curve is crossed, planetary rotation organises the resulting flows into circulation cells and jets, and the feedbacks between temperature, ice, and radiation decide between stable climates and runaway states. The hydrostatic and radiative results assembled here return in every one of those pieces.

## References

```{bibliography}
:filter: docname in docnames
```
