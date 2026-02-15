(lecture05)=
# Lecture 5: Atmospheres I — Composition, Structure, & Energy Balance

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to classify atmospheric types (primary, secondary, tertiary), derive pressure–temperature profiles from hydrostatic equilibrium, explain the greenhouse effect and planetary energy balance, and evaluate atmospheric escape mechanisms.
```

## Atmospheric composition

A planet's atmosphere is the thin gaseous envelope that separates its surface (or cloud tops) from the vacuum of space. Atmospheres play an outsized role in determining a planet's surface conditions — temperature, pressure, radiation environment, and chemistry — and are therefore central to questions of habitability. Understanding where atmospheres come from, what they are made of, and how they evolve is one of the core themes of planetary science {cite}`Catling2017`.

```{figure} figures/earth_thin_blue_line.jpg
:name: fig:thin-blue-line
:width: 600px
:align: center

Earth's atmosphere as a thin blue line on the limb, photographed from the International Space Station during the STS-129 mission (November 2009). The atmosphere contains 99% of its mass below $\sim$30 km altitude — a mere 0.5% of Earth's radius — yet this slender layer controls the surface temperature, shields life from harmful radiation, and mediates the exchange of volatiles between the interior and space. Credit: NASA/ISS Expedition 21 crew, public domain.
```

### Primary atmospheres

**Primary atmospheres** are captured directly from the protoplanetary disk during planet formation. Because the disk is composed predominantly of hydrogen and helium (reflecting the solar composition), primary atmospheres are dominated by $\mathrm{H_2}$ and He, with trace amounts of $\mathrm{CH_4}$, $\mathrm{NH_3}$, $\mathrm{H_2O}$, and noble gases.

Only sufficiently massive bodies — those exceeding roughly $5$–$10 \, \Mearth$ — can gravitationally capture and retain significant quantities of nebular gas before the disk disperses (within $\sim$3–10 Myr; {ref}`lecture02`). The **gas giants** Jupiter and Saturn are the primary examples: their massive $\mathrm{H_2}$/He envelopes constitute the vast majority of their total mass. The **ice giants** Uranus and Neptune also captured primary atmospheres, but far less gas — their envelopes are only $\sim$10–20% of their total mass, reflecting their slower growth and the disk's dissipation.

Terrestrial planets like Earth, Venus, and Mars were too small to capture significant nebular gas. Any primordial hydrogen they did accrete was quickly lost to space (see [atmospheric escape](atm-escape) below). Their present-day atmospheres are therefore **not** primary.

### Secondary atmospheres

**Secondary atmospheres** are produced by **outgassing** — the release of volatiles from the planet's interior through volcanism and magma ocean degassing. As discussed in {ref}`lecture04`, the speciation of outgassed volatiles depends on the oxygen fugacity of the magma: oxidising conditions produce $\mathrm{CO_2}$, $\mathrm{H_2O}$, and $\mathrm{N_2}$, while reducing conditions produce $\mathrm{H_2}$, CO, and $\mathrm{N_2}$ {cite}`Hirschmann2012`.

The present-day atmospheres of **Venus** ($\mathrm{CO_2}$-dominated) and **Mars** ($\mathrm{CO_2}$-dominated but much thinner) are essentially secondary atmospheres — their compositions reflect volcanic outgassing with relatively modest subsequent modification. Titan's thick $\mathrm{N_2}$ atmosphere also originated from outgassing (likely from the conversion of accreted $\mathrm{NH_3}$).

### Tertiary atmospheres

**Tertiary atmospheres** have been substantially modified from their outgassed composition by surface processes, photochemistry, or biology. Earth is the prime example: its original outgassed atmosphere was likely dominated by $\mathrm{CO_2}$ and $\mathrm{N_2}$ (similar to Venus), but billions of years of biological activity — particularly oxygenic photosynthesis — have transformed it into the $\mathrm{N_2}$/$\mathrm{O_2}$ atmosphere we breathe today. Earth's atmospheric $\mathrm{O_2}$ (21% by volume) is entirely biogenic: it would disappear within a few million years if photosynthesis ceased {cite}`Catling2017`.

### Comparative atmospheric properties

The diversity of atmospheres across the solar system is remarkable. The table below compares key properties for five representative bodies:

| Property | Venus | Earth | Mars | Jupiter | Titan |
|----------|:-----:|:-----:|:----:|:-------:|:-----:|
| Surface pressure (bar) | 92 | 1.0 | 0.006 | — | 1.5 |
| Surface temperature (K) | 735 | 288 | 210 | — | 94 |
| Dominant gas | $\mathrm{CO_2}$ (96.5%) | $\mathrm{N_2}$ (78%) | $\mathrm{CO_2}$ (95%) | $\mathrm{H_2}$ (86%) | $\mathrm{N_2}$ (95%) |
| Secondary gas | $\mathrm{N_2}$ (3.5%) | $\mathrm{O_2}$ (21%) | $\mathrm{N_2}$ (2.7%) | He (14%) | $\mathrm{CH_4}$ (5%) |
| Mean molecular weight $\mu$ | 43.4 | 28.97 | 43.3 | 2.2 | 28.6 |
| Atmosphere type | Secondary | Tertiary | Secondary | Primary | Secondary |

Data from {cite}`dePaterLissauer2010` and {cite}`NASAFactSheet`.

```{figure} figures/venera13_venus_surface.jpg
:name: fig:venera13-venus
:width: 600px
:align: center

The surface of Venus photographed by the Soviet *Venera 13* lander on 1 March 1982. The image shows flat basaltic rocks under an orange sky coloured by the thick $\mathrm{CO_2}$ atmosphere (surface pressure 92 bar, temperature 735 K). The lander survived for 127 minutes before succumbing to the extreme conditions — a vivid demonstration of how a massive secondary atmosphere transforms a planet's surface environment. Credit: USSR Academy of Sciences / NASA NSSDC, public domain.
```


## Hydrostatic equilibrium

The vertical structure of any atmosphere is governed by the balance between **gravity** pulling gas downward and the **pressure gradient** pushing it upward. This balance — **hydrostatic equilibrium** — is the most fundamental equation of atmospheric physics.

### Derivation

Consider a thin horizontal slab of atmosphere with cross-sectional area $A$, thickness $\dd z$, and density $\rho(z)$ at height $z$ above the surface. The forces on this slab are:

- **Pressure from below** (pushing up): $P(z) \cdot A$
- **Pressure from above** (pushing down): $P(z + \dd z) \cdot A$
- **Weight** (pulling down): $\rho(z) \, g \, A \, \dd z$

In equilibrium, the net upward pressure force balances the weight:

$$
P(z) \, A - P(z + \dd z) \, A = \rho(z) \, g \, A \, \dd z
$$

Dividing by $A \, \dd z$ and taking the limit:

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

The barometric formula tells us that atmospheric pressure decreases **exponentially** with altitude. Every scale height $H$, the pressure drops by a factor of $e \approx 2.718$. This exponential decay is why atmospheres are thin compared to the size of the planet — typically, 99% of the atmospheric mass lies below $\sim 5H$.


## Blackboard derivation: The atmospheric scale height

```{admonition} Blackboard derivation: Atmospheric scale height from hydrostatic equilibrium
:class: tip

**Goal:** Derive the atmospheric scale height $H = \kB T / (\mu \, m_u \, g)$ from hydrostatic equilibrium combined with the ideal gas law, and compute $H$ for Earth, Mars, Venus, Jupiter, and Titan.

**Setup.**

We start from the equation of hydrostatic equilibrium (Eq. {eq}`eq:hydrostatic-equilibrium`) and the ideal gas law (Eq. {eq}`eq:ideal-gas-atm`):

$$
\dv{P}{z} = -\rho \, g \qquad \text{and} \qquad P = \frac{\rho \kB T}{\mu \, m_u}
$$

Our goal is to find the characteristic length scale over which pressure varies — the **scale height**.

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
| Venus | 735 | 43.4 | 8.87 | 15.8 |
| Earth | 288 | 28.97 | 9.81 | 8.5 |
| Mars | 210 | 43.3 | 3.72 | 11.1 |
| Jupiter | 165 | 2.2 | 24.8 | 27 |
| Titan | 94 | 28.6 | 1.35 | 21 |

**Worked example for Earth:**

$$
H_\oplus = \frac{1.381 \times 10^{-23} \times 288}{28.97 \times 1.661 \times 10^{-27} \times 9.81} = \frac{3.98 \times 10^{-21}}{4.72 \times 10^{-25}} \approx 8400 \text{ m} \approx 8.4 \text{ km}
$$

This matches our everyday experience: commercial aircraft cruise at $\sim$10–12 km altitude, where the pressure is roughly $0.2$–$0.3$ atm (about 1.2–1.4 scale heights up).

**Note:** Jupiter's scale height is large despite its strong gravity because $\mathrm{H_2}$ has a very low molecular weight ($\mu = 2.2$). Titan's scale height is large because its gravity is weak ($g = 1.35$ m s$^{-2}$) — Titan's atmosphere extends to a proportionally much greater height than Earth's, despite being colder.
```


## Vertical structure

Real atmospheres are not isothermal — temperature varies with altitude, creating distinct **layers** characterised by different physical processes. These layers are defined by the sign of the temperature gradient $\dv{T}{z}$.

### Troposphere

The **troposphere** is the lowest layer, heated primarily from below by the surface (which absorbs sunlight and re-emits thermal radiation). Warm air near the surface rises, cool air aloft sinks — this is **convection**, the same process we encountered in planetary interiors ({ref}`lecture03`). Convection keeps the troposphere well-mixed and imposes a characteristic temperature decrease with altitude called the **lapse rate**.

For a parcel of dry air rising adiabatically (without exchanging heat with its surroundings), the temperature decreases at the **dry adiabatic lapse rate**:

$$
\Gamma_d = -\dv{T}{z} = \frac{g}{c_p}
$$ (eq:dry-adiabat)

where $c_p$ is the specific heat capacity at constant pressure. For Earth, $g = 9.81$ m s$^{-2}$ and $c_p \approx 1004$ J kg$^{-1}$ K$^{-1}$ (for dry air), giving $\Gamma_d \approx 9.8$ K km$^{-1}$. The observed average lapse rate ($\sim 6.5$ K km$^{-1}$) is lower because of latent heat released by condensing water vapour — the **moist adiabatic lapse rate**.

Earth's troposphere extends from the surface to the **tropopause** at $\sim$12 km altitude (varying from $\sim$8 km at the poles to $\sim$17 km at the equator).

### Stratosphere

Above the tropopause, temperature increases with altitude in the **stratosphere**. On Earth, this temperature inversion is caused by the absorption of solar ultraviolet radiation by the **ozone layer** ($\mathrm{O_3}$), centred at $\sim$25 km altitude. The heating by UV absorption creates a stable, non-convective layer — air parcels displaced upward find themselves cooler and denser than their surroundings and sink back down.

Earth's stratosphere extends to the **stratopause** at $\sim$50 km.

### Mesosphere and thermosphere

Above the stratopause, the **mesosphere** (50–85 km) cools with altitude again as ozone heating diminishes. The **mesopause** at $\sim$85 km is the coldest point in Earth's atmosphere ($\sim$190 K).

Above this, the **thermosphere** (85–600 km) is heated by the absorption of extreme ultraviolet (EUV) radiation and energetic particles. Temperatures rise steeply to $>$1000 K, but the gas is so rarefied that this "temperature" (reflecting the kinetic energy of individual molecules) would not feel hot. The thermosphere merges into the **exosphere** — the outermost region where the mean free path exceeds the scale height, and molecules on ballistic trajectories can escape to space.

### Comparative vertical structures

The vertical structure varies dramatically across the solar system {cite}`Catling2017`:

- **Venus:** A massive troposphere extends to $\sim$65 km. Above the cloud deck ($\sim$48–70 km), temperature decreases slowly. There is no Earth-like stratospheric temperature inversion because Venus lacks an ozone layer.
- **Mars:** A thin troposphere ($\sim$40 km) directly overlain by a thermosphere. Mars also lacks a significant ozone layer and stratospheric inversion.
- **Jupiter:** The troposphere extends deep into the planet (hundreds of kilometres). The stratosphere is heated by $\mathrm{CH_4}$ and hydrocarbon haze absorption. There is no solid surface — pressure increases continuously with depth.
- **Titan:** A thick troposphere ($\sim$40 km), a stratosphere heated by organic haze absorption (up to $\sim$300 km), and an extended thermosphere reaching $\sim$1500 km — remarkably high for such a small body, reflecting Titan's weak gravity and large scale height.

```{figure} figures/atmosphere_layers.svg
:name: fig:atmosphere-layers
:width: 350px
:align: center

Vertical temperature profile of Earth's atmosphere, showing the four principal layers (troposphere, stratosphere, mesosphere, thermosphere) defined by the sign of the temperature gradient. The tropopause, stratopause, and mesopause mark the boundaries between layers. Credit: Wikimedia Commons, public domain.
```


## Radiative transfer basics

While convection dominates energy transport in the troposphere, **radiation** is the primary mechanism by which energy enters and leaves the atmosphere. Understanding how radiation interacts with atmospheric gases is essential for explaining why planets have the temperatures they do.

### Absorption, emission, and scattering

When a beam of radiation passes through an atmosphere, three things can happen:

1. **Absorption:** A gas molecule absorbs a photon, converting radiative energy into internal energy (vibrational, rotational, or electronic excitation). The key atmospheric absorbers are **greenhouse gases**: $\mathrm{CO_2}$, $\mathrm{H_2O}$, $\mathrm{CH_4}$, $\mathrm{O_3}$, and $\mathrm{N_2O}$. These molecules have vibrational and rotational modes that absorb strongly in the infrared — precisely the wavelengths at which warm planetary surfaces emit.

2. **Emission:** By Kirchhoff's law, any gas that absorbs radiation at a given wavelength also emits at that wavelength when it is warm. This thermal emission is the mechanism by which the atmosphere radiates energy to space.

3. **Scattering:** Photons are redirected without being absorbed. Rayleigh scattering by $\mathrm{N_2}$ and $\mathrm{O_2}$ (which goes as $\lambda^{-4}$) explains why the sky is blue and sunsets are red. Mie scattering by larger particles (aerosols, cloud droplets) is less wavelength-dependent.

```{figure} figures/blackbody_spectrum.svg
:name: fig:blackbody-spectrum
:width: 550px
:align: center

Blackbody radiation curves for objects at several temperatures (representative of stellar and planetary emission). The Sun ($\sim$5800 K) emits primarily at visible wavelengths ($\sim$0.5 $\mu$m), while a planet at $\sim$300 K emits in the thermal infrared ($\sim$10 $\mu$m). This wavelength separation between incoming stellar radiation and outgoing planetary emission is the physical basis of the greenhouse effect — atmospheric gases can be transparent at one set of wavelengths while opaque at the other. Credit: Wikimedia Commons, public domain.
```

### Optical depth

The cumulative effect of absorption along a path through the atmosphere is quantified by the **optical depth** $\tau$:

$$
\tau = \int_0^s \kappa \, \rho \, \dd s'
$$ (eq:optical-depth)

where $\kappa$ is the **mass absorption coefficient** (m$^2$ kg$^{-1}$), $\rho$ is the gas density, and $s$ is the path length. Alternatively, using the number density $n$ and the absorption cross-section $\sigma$: $\tau = \int n \sigma \, \dd s'$.

The optical depth is dimensionless and measures how many "e-folding lengths" of absorption the radiation traverses:

- $\tau \ll 1$: **Optically thin** — most radiation passes through without being absorbed.
- $\tau \gg 1$: **Optically thick** — radiation is strongly absorbed; only photons emitted near the "top" of the absorbing layer escape.

### Beer–Lambert law

For a beam of radiation with initial intensity $I_0$ passing through a medium of optical depth $\tau$:

$$
I = I_0 \, e^{-\tau}
$$ (eq:beer-lambert)

This exponential attenuation law — the **Beer–Lambert law** — shows that intensity decreases by a factor of $e$ for each unit of optical depth traversed.

### The atmospheric photosphere concept

Just as a star has a **photosphere** — the layer from which photons escape to space — a planet's atmosphere has an effective emission level at approximately $\tau \approx 1$ (when looking from space downward at infrared wavelengths). Photons emitted from below this level are likely to be reabsorbed before escaping; photons emitted from above this level escape freely. The temperature at this $\tau \approx 1$ level determines the planet's **effective temperature** as seen from space {cite}`Pierrehumbert2010`.


## Energy balance and the greenhouse effect

### Planetary energy balance

Every planet reaches a thermal equilibrium in which the rate of **absorbed stellar energy** equals the rate of **emitted thermal radiation**. The stellar flux received at a planet's orbital distance $d$ from its star (luminosity $L_\star$) is:

$$
F_\star = \frac{L_\star}{4\pi d^2}
$$ (eq:stellar-flux)

The planet intercepts this flux over its cross-sectional area $\pi R_p^2$ and reflects a fraction $A$ (the **Bond albedo**). The absorbed power is therefore $(1 - A) \, F_\star \, \pi R_p^2$.

In equilibrium, this absorbed power equals the thermal radiation emitted from the entire surface ($4\pi R_p^2$) at the **effective temperature** $T_{\mathrm{eff}}$ via the Stefan–Boltzmann law ({ref}`lecture03`):

$$
(1 - A) \frac{L_\star}{4\pi d^2} \pi R_p^2 = 4\pi R_p^2 \, \sigma \, T_{\mathrm{eff}}^4
$$

Solving for $T_{\mathrm{eff}}$:

$$
T_{\mathrm{eff}} = \left[\frac{(1-A) \, L_\star}{16 \pi \sigma \, d^2}\right]^{1/4}
$$ (eq:effective-temperature)

The effective temperature is the temperature at which the planet would radiate if it had no atmosphere (or if the atmosphere were completely transparent). It depends only on the stellar luminosity, the orbital distance, and the albedo — not on any atmospheric properties.

### Effective vs. actual surface temperatures

The table below compares the effective temperature with the measured surface temperature for several solar system bodies:

| Body | Albedo $A$ | $d$ (AU) | $T_{\mathrm{eff}}$ (K) | $T_{\mathrm{surface}}$ (K) | $\Delta T$ (K) |
|------|:----------:|:--------:|:-----------------------:|:---------------------------:|:---------------:|
| Venus | 0.77 | 0.72 | 227 | 735 | +508 |
| Earth | 0.30 | 1.00 | 255 | 288 | +33 |
| Mars | 0.25 | 1.52 | 210 | 210 | ~0 |
| Jupiter | 0.34 | 5.20 | 110 | 165* | +55 |

\*Jupiter's "surface temperature" refers to the 1-bar level.

The discrepancy $\Delta T = T_{\mathrm{surface}} - T_{\mathrm{eff}}$ reveals the strength of the **greenhouse effect**. Venus has a staggering 508 K greenhouse warming — by far the largest in the solar system. Earth's 33 K greenhouse warming, though modest by comparison, is sufficient to keep the oceans liquid. Mars has essentially no greenhouse warming because its atmosphere is too thin (surface pressure only 6 mbar). Jupiter's excess temperature is partly due to internal heat left over from formation ({ref}`lecture03`), not solely the greenhouse effect.

### The greenhouse mechanism

The greenhouse effect arises because the atmosphere is **relatively transparent** to incoming shortwave (visible) radiation from the star but **relatively opaque** to outgoing longwave (infrared) radiation from the surface. The mechanism works as follows {cite}`Pierrehumbert2010`:

1. Sunlight (visible wavelengths, peak $\sim$0.5 $\mu$m) passes through the atmosphere and heats the surface.
2. The warm surface emits thermal radiation at infrared wavelengths (peak $\sim$10–15 $\mu$m for $T \sim 200$–$300$ K).
3. Greenhouse gases ($\mathrm{CO_2}$, $\mathrm{H_2O}$, $\mathrm{CH_4}$, $\mathrm{O_3}$, etc.) absorb much of this outgoing IR radiation.
4. The absorbing layer re-emits IR radiation in all directions — half upward (toward space), half downward (back toward the surface).
5. The downward emission provides an **additional energy source** for the surface, raising its temperature above $T_{\mathrm{eff}}$.

```{figure} figures/atmospheric_transmission.svg
:name: fig:atmospheric-absorption
:width: 600px
:align: center

Atmospheric absorption spectrum of Earth's atmosphere from ultraviolet through infrared wavelengths. The top panel shows the solar radiation spectrum; the bottom panels show absorption by individual gases. Note the strong absorption bands of $\mathrm{H_2O}$ and $\mathrm{CO_2}$ in the infrared, and the "atmospheric window" near 8–13 $\mu$m where the atmosphere is relatively transparent. Credit: Wikimedia Commons, public domain.
```

### One-layer greenhouse model

We can quantify the greenhouse effect with a simple **one-layer model**. Consider an atmosphere represented by a single isothermal layer with **emissivity** $\varepsilon$ at infrared wavelengths (and completely transparent at visible wavelengths). The energy balance has two components:

**Atmospheric layer balance** — The layer absorbs a fraction $\varepsilon$ of the surface emission $\sigma T_s^4$ and emits $\varepsilon \sigma T_a^4$ both upward and downward:

$$
\varepsilon \, \sigma \, T_s^4 = 2 \, \varepsilon \, \sigma \, T_a^4
$$ (eq:atm-balance)

This gives $T_a^4 = T_s^4 / 2$.

**Surface balance** — The surface absorbs the incoming stellar flux plus the downward emission from the atmosphere. In equilibrium:

$$
(1-A) \frac{F_\star}{4} + \varepsilon \, \sigma \, T_a^4 = \sigma \, T_s^4
$$ (eq:surface-balance)

**Top-of-atmosphere balance** — The planet must radiate to space at its effective temperature, so $(1-A) F_\star / 4 = \sigma T_{\mathrm{eff}}^4$. Combining with the atmospheric and surface balance equations:

$$
T_s = T_{\mathrm{eff}} \left(\frac{2}{2 - \varepsilon}\right)^{1/4}
$$ (eq:greenhouse-surface-temp)

When $\varepsilon = 0$ (no greenhouse gases), $T_s = T_{\mathrm{eff}}$ — no warming. When $\varepsilon = 1$ (perfect absorber), $T_s = 2^{1/4} \, T_{\mathrm{eff}} \approx 1.19 \, T_{\mathrm{eff}}$ — a 19% increase in surface temperature. For Earth, this gives $T_s \approx 1.19 \times 255 \approx 303$ K — a reasonable first estimate, though the real greenhouse effect involves multiple absorbing layers and a more complex radiative transfer calculation.

```{note}
This one-layer model is deliberately simple. In {ref}`lecture06`, we will extend this treatment to examine the **runaway greenhouse effect** — what happens when the surface temperature rises so high that the outgoing longwave radiation reaches a maximum and can no longer balance the absorbed stellar flux. This is the mechanism that likely transformed Venus from a potentially habitable world into the 735 K inferno we see today.
```

```{figure} figures/greenhouse_effect.svg
:name: fig:greenhouse-effect
:width: 500px
:align: center

Schematic of the greenhouse effect. Incoming solar radiation (shortwave, yellow) passes through the atmosphere to heat the surface. The surface emits infrared radiation (longwave, red), which is partially absorbed by greenhouse gases. The atmosphere re-emits this energy both upward (to space) and downward (back to the surface), raising the surface temperature above what it would be without an atmosphere. Credit: Wikimedia Commons, public domain.
```


(atm-escape)=
## Atmospheric escape

An atmosphere is not permanent. Over geological time, gas molecules can be lost to space through several physical mechanisms. The balance between outgassing supply and escape loss determines a planet's atmospheric mass and composition over its history {cite}`Lammer2008`.

### Thermal (Jeans) escape

The most fundamental escape mechanism is **Jeans escape**, which arises from the thermal velocity distribution of gas molecules. In a gas at temperature $T$, molecules have a range of speeds described by the Maxwell–Boltzmann distribution. The mean thermal speed is $v_{\mathrm{th}} \sim \sqrt{\kB T / m}$, where $m$ is the molecular mass. Most molecules are far too slow to escape, but the tail of the distribution extends to arbitrarily high speeds — and some molecules in this high-velocity tail exceed the escape speed.

The key parameter governing Jeans escape is the **Jeans escape parameter** $\lambda_J$, defined at the exobase (the altitude where the mean free path equals the scale height):

$$
\lambda_J = \frac{G M_p \, m}{\kB T_{\mathrm{exo}} \, r_{\mathrm{exo}}} = \frac{v_{\mathrm{esc}}^2}{v_{\mathrm{th}}^2}
$$ (eq:jeans-parameter)

where $M_p$ is the planet's mass, $m$ is the molecular mass, $T_{\mathrm{exo}}$ is the exobase temperature, $r_{\mathrm{exo}}$ is the exobase radius, $v_{\mathrm{esc}} = \sqrt{2GM_p/r_{\mathrm{exo}}}$ is the escape speed, and $v_{\mathrm{th}} = \sqrt{2\kB T_{\mathrm{exo}}/m}$ is the most probable thermal speed.

The Jeans escape parameter is the ratio of gravitational binding energy to thermal energy for a molecule at the exobase. When $\lambda_J \gg 1$, very few molecules have enough energy to escape — escape is slow. When $\lambda_J \lesssim 2$–3, a significant fraction of molecules can escape, and the atmosphere erodes rapidly.

The **Jeans escape flux** (number of molecules escaping per unit area per unit time from the exobase) is:

$$
\Phi_J = \frac{n_{\mathrm{exo}} \, v_{\mathrm{th}}}{2\sqrt{\pi}} \, (1 + \lambda_J) \, e^{-\lambda_J}
$$ (eq:jeans-flux)

where $n_{\mathrm{exo}}$ is the number density at the exobase. The exponential factor $e^{-\lambda_J}$ shows that escape is extremely sensitive to $\lambda_J$: a small change in temperature, gravity, or molecular mass can change the escape rate by orders of magnitude.

The following table illustrates $\lambda_J$ for several atmospheric species on Earth and Mars, assuming exobase temperatures of 1000 K (Earth) and 300 K (Mars):

| Species | $m$ (u) | $\lambda_J$ (Earth) | $\lambda_J$ (Mars) |
|---------|:-------:|:--------------------:|:-------------------:|
| H | 1 | 7.5 | 5.4 |
| $\mathrm{H_2}$ | 2 | 15 | 11 |
| He | 4 | 30 | 22 |
| $\mathrm{N_2}$ | 28 | 210 | 150 |
| $\mathrm{CO_2}$ | 44 | 330 | 240 |

For heavy species like $\mathrm{N_2}$ and $\mathrm{CO_2}$, $\lambda_J$ is so large that Jeans escape is negligible on both planets. For atomic hydrogen, $\lambda_J$ is moderate, leading to significant escape — this is why both Earth and Mars lose hydrogen to space. We will revisit this derivation in full detail (starting from the Maxwell–Boltzmann distribution) in {ref}`lecture10`.

### Hydrodynamic escape

When the energy input to the upper atmosphere is very large — for example, from intense **extreme ultraviolet (EUV)** radiation from a young, active star — the escape can transition from the slow, molecule-by-molecule Jeans process to a bulk **hydrodynamic outflow** in which the entire upper atmosphere flows outward like a wind. This is analogous to the solar wind but driven by stellar heating rather than the star's own thermal energy {cite}`Hunten1987`.

Hydrodynamic escape is most important during a planet's first few hundred million years, when the host star's EUV luminosity is 10–100 times higher than at present. It can strip hydrogen-rich primary atmospheres from planets up to several Earth masses, and is the leading explanation for the observed **radius valley** in the exoplanet population — the deficit of planets with radii between $\sim$1.5 and $2 \, \Rearth$ ({ref}`lecture13`). During hydrodynamic escape, the outflowing hydrogen can also **drag along heavier species** (such as He, C, N, O), leading to more extensive atmospheric loss than Jeans escape alone would produce {cite}`Hunten1987`.

### Non-thermal escape mechanisms

Several processes can eject atmospheric particles to space without relying on thermal energy {cite}`Lammer2008`:

- **Sputtering:** Energetic ions from the solar wind or magnetospheric plasma impact the upper atmosphere and transfer enough momentum to eject atmospheric molecules. This is significant for Mars, which lacks a global magnetic field to deflect the solar wind.

- **Photochemical escape:** Solar UV radiation dissociates molecules (e.g., $\mathrm{H_2O} \to$ H + OH), producing fast atoms with enough energy to escape. This is an important loss channel for hydrogen from Venus and Mars.

- **Ion pickup:** Atmospheric atoms ionised by solar UV or charge exchange are picked up by the solar wind magnetic field and swept away from the planet. This process is particularly effective at unmagnetised planets like Mars and Venus.

- **Impact erosion:** Large asteroid or comet impacts can eject significant fractions of a planet's atmosphere. The efficiency depends on the impactor size relative to the atmospheric scale height — very large impacts can blow off a substantial atmospheric mass in a single event.

The MAVEN mission at Mars has measured the present-day atmospheric escape rates and demonstrated that solar wind stripping is the dominant loss mechanism for Mars's remaining atmosphere, with a current loss rate of $\sim$100 g s$^{-1}$ for $\mathrm{O}^+$ ions {cite}`Jakosky2018`.

```{figure} figures/mars_atmosphere.jpg
:name: fig:mars-atmosphere
:width: 550px
:align: center

The thin Martian atmosphere visible as a blue haze on the limb, photographed by NASA's *Viking 1* orbiter in 1976. With a surface pressure of only 6 mbar ($\sim$0.6% of Earth's), Mars's atmosphere is too thin to sustain liquid water or provide significant greenhouse warming today. Geological evidence for ancient rivers, lakes, and possibly an ocean indicates that Mars once had a much thicker atmosphere, most of which has been lost to space over the past $\sim$4 billion years through solar wind stripping and other escape processes. Credit: NASA/JPL, public domain.
```


## Atmospheric retention

Whether a planet retains its atmosphere over billions of years depends on the competition between escape processes and atmospheric sources (outgassing, volatile delivery). The outcome is controlled primarily by two parameters: the planet's **escape velocity** and the **thermal velocity** of atmospheric molecules.

### The escape velocity–temperature diagram

The classic tool for assessing atmospheric retention is a plot of escape velocity versus surface (or exosphere) temperature. Each atmospheric species occupies a characteristic region based on its thermal velocity $v_{\mathrm{th}} = \sqrt{2\kB T / m}$. The rule of thumb for long-term retention is {cite}`dePaterLissauer2010`:

$$
v_{\mathrm{esc}} \gtrsim 6 \, v_{\mathrm{th}}
$$

A planet retains a given gas species if its escape velocity exceeds roughly 6 times the thermal velocity of that species (corresponding to $\lambda_J \gtrsim 18$, ensuring negligible Jeans escape over billions of years).

### Solar system trends

Applying this criterion reveals a clear pattern across the solar system:

- **Gas giants** (Jupiter, Saturn): With escape velocities of 60 and 36 km s$^{-1}$ respectively, and moderate exosphere temperatures, they retain **all species** — including the lightest ($\mathrm{H_2}$, He). This is why they still possess their primary atmospheres.

- **Earth and Venus**: Escape velocities of $\sim$11 km s$^{-1}$ are sufficient to retain heavy molecules ($\mathrm{N_2}$, $\mathrm{O_2}$, $\mathrm{CO_2}$, $\mathrm{H_2O}$) but not atomic hydrogen. Earth and Venus lose H to space, which contributes to long-term water loss (via photodissociation of $\mathrm{H_2O}$ followed by H escape).

- **Mars**: With $v_{\mathrm{esc}} = 5.0$ km s$^{-1}$ and an exosphere temperature of $\sim$300 K, Mars is marginal for retaining even heavy species like $\mathrm{CO_2}$. While Jeans escape of $\mathrm{CO_2}$ is negligible, non-thermal processes (sputtering, ion pickup) have eroded most of Mars's original atmosphere over 4 billion years {cite}`Jakosky2018`.

- **Titan**: Despite its low escape velocity (2.6 km s$^{-1}$), Titan retains a thick $\mathrm{N_2}$ atmosphere because it is extremely **cold** ($T_{\mathrm{exo}} \approx 150$ K). Low temperature means low thermal velocities, and the Jeans parameter remains large.

- **Moon and Mercury**: With escape velocities of 2.4 and 4.3 km s$^{-1}$ and high dayside temperatures ($>$400 K), these bodies cannot retain any significant atmosphere. Mercury has only a tenuous **exosphere** (a collisionless atmosphere with surface pressure $\sim 10^{-15}$ bar).

### Atmospheric evolution over time

Atmospheric retention is not simply a present-day snapshot — it evolves over a planet's lifetime {cite}`Lammer2008`:

- **Young stars are UV-bright:** Stars on the main sequence emit 10–100 times more EUV radiation in their first few hundred million years. This drives intense hydrodynamic escape that can strip primary atmospheres from low-mass planets.

- **Magnetic field loss:** A planet that loses its global magnetic field (like Mars $\sim$4 Gyr ago; {ref}`lecture04`) becomes exposed to solar wind sputtering and ion pickup, accelerating atmospheric loss.

- **Outgassing replenishment:** Ongoing volcanism can replenish atmospheric gases. Earth's atmosphere is maintained in part by the continuous volcanic outgassing of $\mathrm{CO_2}$, $\mathrm{H_2O}$, and $\mathrm{SO_2}$. A planet with active tectonics (and thus active volcanism) has a better chance of maintaining its atmosphere.

- **Atmospheric chemistry:** Photochemical reactions can transform atmospheric species. For example, solar UV dissociates $\mathrm{H_2O}$ into H and O; the hydrogen escapes while the oxygen may be incorporated into surface rocks. This irreversible loss of hydrogen is the leading hypothesis for how Venus lost its primordial water inventory.

We will examine the long-term atmospheric evolution of specific planets in detail: Venus's runaway greenhouse and water loss ({ref}`lecture09`), Mars's atmospheric collapse and escape ({ref}`lecture10`), and the atmospheric characterisation of exoplanets ({ref}`lecture13`). The runaway greenhouse effect and climate feedbacks will be the central topics of {ref}`lecture06`.

```{figure} figures/escape_velocity_temperature.svg
:name: fig:escape-velocity-temperature
:width: 550px
:align: center

Escape velocity versus surface temperature for solar system bodies. Diagonal lines indicate the thermal velocity of different gas species (scaled by a factor of 6 for long-term retention). Bodies above and to the left of a species line can retain that gas; bodies below and to the right cannot. The gas giants retain everything; Earth and Venus retain heavy species but lose H; Mars and Titan are marginal; the Moon and Mercury retain essentially nothing. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```


## References

```{bibliography}
:filter: docname in docnames
```
