(lecture06)=
# Atmospheres II: Clouds, Weather, & Climate

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to derive the Clausius-Clapeyron equation and apply it to predict cloud formation conditions, explain atmospheric circulation patterns using the Coriolis effect and geostrophic balance, describe weather phenomena across the solar system, and discuss long-term climate evolution including the faint young Sun paradox and the carbonate-silicate cycle.
```

```{seealso}
**Slides:** [Download Lecture 6 (PDF)](../_static/slides/lecture06.pdf)
```

## Cloud formation

In {ref}`Lecture 5 <lecture05>`, we studied the vertical structure of atmospheres: how pressure and temperature vary with altitude, and how radiation and convection control the energy balance. We now turn to what happens when the air becomes *too cold* to hold all of its vapour: **clouds** form.

### Saturation and condensation

Every gas has a maximum amount of vapour that the surrounding air can hold at a given temperature. This maximum is set by the **saturation vapour pressure** $P_{\mathrm{sat}}(T)$, the partial pressure at which the rate of evaporation from a liquid (or solid) surface equals the rate of condensation back onto it. When the actual partial pressure of a vapour exceeds $P_{\mathrm{sat}}$, the air is **supersaturated** and condensation is thermodynamically favoured {cite:p}`Pierrehumbert2010`.

The key property of $P_{\mathrm{sat}}(T)$ is its strong temperature dependence: it increases roughly exponentially with temperature. A parcel of air that is unsaturated at the warm surface can become saturated simply by cooling (for example, by rising and expanding adiabatically). The temperature at which a parcel first reaches saturation is called the **dew point** (for condensation to liquid) or the **frost point** (for deposition to ice).

The **relative humidity** is defined as the ratio of the actual vapour pressure to the saturation vapour pressure:

$$
\mathrm{RH} = \frac{P_{\mathrm{vapour}}}{P_{\mathrm{sat}}(T)} \times 100\%
$$

When $\mathrm{RH} = 100\%$, the air is saturated; when $\mathrm{RH} > 100\%$, it is supersaturated and condensation can occur. The exponential temperature dependence of $P_\mathrm{sat}$ for the principal condensable species in solar system atmospheres is shown in {numref}`fig:psat-curves`.

```{figure} figures/psat_curves.avif
:name: fig:psat-curves
:width: 600px
:align: center

Saturation vapour pressure $P_{\mathrm{sat}}(T)$ as a function of temperature for the major condensable species in solar system atmospheres: $\mathrm{H_2O}$, $\mathrm{H_2SO_4}$, $\mathrm{NH_3}$, $\mathrm{CH_4}$, and $\mathrm{CO_2}$ (sublimation curve).
The exponential temperature dependence predicted by the Clausius-Clapeyron equation (Eq. {eq}`eq:clausius-clapeyron`) is evident on the logarithmic vertical axis, and the species ordering mirrors the order in which each condenses in its host atmosphere.
Coloured bands at the bottom mark the temperature ranges over which each species condenses: $\mathrm{H_2O}$ on Earth and Mars; $\mathrm{H_2SO_4}$ on Venus; $\mathrm{NH_3}$ on Jupiter and Saturn; $\mathrm{CH_4}$ on Titan, Uranus, and Neptune; and $\mathrm{CO_2}$ on Mars.
Plot generated from thermodynamic data in {cite:p}`Catling2017` and {cite:p}`Pierrehumbert2010`.
```


### Nucleation

Even when air is supersaturated, condensation does not happen instantly. Forming a new droplet requires overcoming an energy barrier: the surface energy of the tiny embryonic droplet. This process is called **nucleation** {cite:p}`Catling2017`.

- **Homogeneous nucleation** (forming droplets from vapour alone, without any pre-existing surface) requires very high supersaturations (RH $\gg$ 100%) and is extremely rare in planetary atmospheres.
- **Heterogeneous nucleation** (condensation onto pre-existing particles called **condensation nuclei**: dust grains, volcanic aerosols, sea salt, soot, cosmic ray ions) occurs at much lower supersaturations (RH $\gtrsim$ 100%) and is the dominant cloud formation mechanism on all planets.

The availability of condensation nuclei therefore controls where and how easily clouds form. On Earth, the oceans and biosphere provide abundant nuclei. On Mars, wind-lofted mineral dust serves the same role. On the giant planets, **photochemical** hazes, aerosol particles formed when ultraviolet sunlight breaks apart atmospheric molecules whose fragments recombine into new compounds, provide nuclei for cloud formation deeper down.

Whether a given nucleus grows into a cloud droplet depends on two competing effects on the equilibrium vapour pressure at the droplet surface. The **Köhler equation** combines them: for a solution droplet of radius $r$, the saturation ratio at which the droplet neither grows nor evaporates is

$$
S(r) \approx 1 + \frac{A}{r} - \frac{B}{r^3},
$$ (eq:kohler)

where $S$ is the vapour pressure over the droplet divided by the saturation vapour pressure over a flat pure-water surface. The **Kelvin (curvature) term** $A/r$ raises the equilibrium vapour pressure over a convex surface, because a molecule on a tightly curved droplet has fewer neighbours to hold it than one on a flat surface. It diverges as $r \to 0$, so the smallest embryos demand the highest supersaturation. Its coefficient is

$$
A = \frac{2\sigma_w}{\rho_w R_v T},
$$

with $\sigma_w$ the surface tension of water, $\rho_w$ the liquid density, $R_v$ the specific gas constant of water vapour, and $T$ the temperature. The **Raoult (solute) term** $-B/r^3$ lowers the vapour pressure, because dissolved solute leaves fewer surface water molecules free to evaporate. The solution concentrates as the droplet shrinks, so this term steepens as $r^{-3}$ and dominates at small radius. Its coefficient is

$$
B = \frac{3\, i\, M_w\, m_s}{4\pi \rho_w M_s},
$$

with $i$ the van 't Hoff factor (the number of dissolved ions per solute formula unit), $m_s$ the solute mass, and $M_w$ and $M_s$ the molar masses of water and the solute. Because the curvature term wins at large radius and the solute term at small radius, $S(r)$ passes through a maximum, the **activation peak** at the critical radius $r_*$. A droplet held below $r_*$ rests in stable equilibrium as a haze particle; once it is pushed past $r_*$, growth becomes self-sustaining and a cloud droplet forms.

The competition between these two terms is captured by the Köhler curves ({numref}`fig:kohler-curves`), which show why heterogeneous nucleation activates at only $\sim$0.04-0.4% supersaturation, while a pure-water droplet would need $\sim$12% even at $r = 10^{-2}\,\mu$m and far more at the nanometre size of a fresh embryo.

```{figure} figures/kohler_curves.avif
:name: fig:kohler-curves
:width: 550px
:align: center

Köhler curves: equilibrium supersaturation $S - 1$ at which a solution droplet of radius $r$ neither grows nor evaporates.
The dashed black curve is the pure-water Kelvin term, $S = 1 + A/r$, which formalises the energy cost of homogeneous nucleation: the equilibrium supersaturation is already $S - 1 \approx 12\%$ at $r = 10^{-2}\,\mu$m and climbs toward $\sim$100% at the nanometre scale of freshly formed embryos, far beyond anything sustained in planetary atmospheres.
The coloured curves show the Köhler form $S = 1 + A/r - B/r^3$ for solution droplets condensed on dry condensation nuclei (CCN) of three solute masses spanning the typical atmospheric range, $m_s = 10^{-16}$, $10^{-15}$, and $10^{-14}$ g {cite:p}`Pruppacher1997`.
The Raoult term $-B/r^3$ pushes the equilibrium curve below the Kelvin curve, so heterogeneous nucleation activates at peak supersaturations of only $\sim$0.04-0.4%, easily reached in adiabatically cooled updraughts.
This is why heterogeneous nucleation dominates on every planet with abundant aerosols.
Adapted from the formulation in {cite:p}`Catling2017`.
```

### The lifting condensation level

As an air parcel rises through the troposphere, it cools at the dry adiabatic lapse rate $\Gamma_d = g/c_p$ (Eq. {eq}`eq:dry-adiabat` from {ref}`Lecture 5 <lecture05>`). Its vapour pressure remains roughly constant (since the mass of vapour is conserved during adiabatic ascent), but $P_{\mathrm{sat}}(T)$ decreases as the temperature drops. At the altitude where the parcel temperature has cooled enough that $P_{\mathrm{vapour}} = P_{\mathrm{sat}}(T)$, condensation begins. This altitude is the **lifting condensation level (LCL)** and marks the cloud base.

Above the LCL, the rising parcel releases **latent heat** as vapour condenses, warming the parcel relative to the dry adiabat. This gives the **moist adiabatic lapse rate**, which is shallower than the dry adiabat ($\sim$9.8 K km$^{-1}$): a representative value in Earth's warm lower troposphere is $\sim$5 K km$^{-1}$, and the observed tropospheric mean of $\sim$6.5 K km$^{-1}$ lies between the two limits ({ref}`Lecture 5 <lecture05>`). The latent heat release also provides buoyancy, driving vigorous convection in moist atmospheres: the mechanism behind thunderstorms, hurricanes, and the towering cumulonimbus clouds on Earth.

```{figure} figures/cumulonimbus_anvil.avif
:name: fig:cumulonimbus-anvil
:width: 560px
:align: center

A cumulonimbus cloud spreading into a flat **anvil** (incus) at its top, seen from above the surrounding cloud deck. Latent heat released by condensing water vapour keeps the rising air warmer than its surroundings and drives the convective tower upward. The tower climbs until it reaches the tropopause, where the stable stratosphere above stops the ascent and the cloud spreads sideways into the anvil. The anvil top therefore marks the altitude where convective buoyancy ends.
Credit: Eulenjäger, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), via Wikimedia Commons.
```

### Cloud types depend on the condensing species

What condenses depends on what vapour is present and at what temperature. This varies dramatically across the solar system:

- **Earth:** $\mathrm{H_2O}$ clouds (liquid droplets and ice crystals), with cloud base at $\sim$1–2 km
- **Venus:** $\mathrm{H_2SO_4}$ (sulfuric acid) droplets at 48–70 km altitude
- **Mars:** $\mathrm{CO_2}$ ice and $\mathrm{H_2O}$ ice clouds at high altitude
- **Titan:** $\mathrm{CH_4}$ and $\mathrm{C_2H_6}$ (ethane) clouds near the surface
- **Jupiter/Saturn:** Layered $\mathrm{NH_3}$, $\mathrm{NH_4SH}$, and $\mathrm{H_2O}$ clouds at successively deeper levels

The physics of cloud formation is the same in every case: the Clausius-Clapeyron equation governs all of them. The difference is which species condenses and at what temperature.


## Blackboard derivation: The Clausius-Clapeyron equation

```{admonition} Blackboard derivation: The Clausius-Clapeyron equation
:class: tip

**Goal:** Derive the exponential dependence of saturation vapour pressure on temperature from thermodynamic phase equilibrium, and apply the result to predict cloud condensation conditions across the solar system.

**Setup: phase equilibrium.**

Consider a substance (e.g., water) that exists in two phases: liquid and vapour. Along the **coexistence curve** in the $P$–$T$ diagram (the line separating the liquid and vapour phases; see {numref}`fig:water-phase-diagram`) the two phases are in thermodynamic equilibrium. This means the **Gibbs free energy per unit mass** is equal in both phases:

$$
g_{\ell}(T, P) = g_v(T, P)
$$

where $g_\ell$ and $g_v$ are the specific Gibbs free energies of the liquid and vapour, respectively.

**Derivation.**

If we move along the coexistence curve by an infinitesimal amount ($\dd T$, $\dd P$), the Gibbs free energies must remain equal:

$$
\dd g_\ell = \dd g_v
$$

From thermodynamics, $\dd g = -s \, \dd T + v \, \dd P$, where $s$ is the specific entropy and $v$ is the specific volume. Therefore:

$$
-s_\ell \, \dd T + v_\ell \, \dd P = -s_v \, \dd T + v_v \, \dd P
$$

Rearranging:

$$
(s_v - s_\ell) \, \dd T = (v_v - v_\ell) \, \dd P
$$

$$
\dv{P}{T} = \frac{s_v - s_\ell}{v_v - v_\ell} = \frac{\Delta s}{\Delta v}
$$

At the phase transition, the entropy change is related to the **latent heat of vaporisation** $L_v$ (the energy required to convert one kilogram of liquid to vapour at constant temperature) by $\Delta s = L_v / T$. Therefore:

$$
\dv{P_{\mathrm{sat}}}{T} = \frac{L_v}{T (v_v - v_\ell)}
$$

This is the **exact Clausius-Clapeyron relation**. We now make two approximations:

1. The specific volume of the vapour is much larger than that of the liquid: $v_v \gg v_\ell$, so $v_v - v_\ell \approx v_v$.
2. The vapour behaves as an ideal gas: $v_v = R_v T / P$, where $R_v = R^* / M$ is the specific gas constant ($R^* = 8.314$ J mol$^{-1}$ K$^{-1}$, $M$ is the molar mass of the vapour).

Substituting:

$$
\dv{P_{\mathrm{sat}}}{T} = \frac{L_v \, P_{\mathrm{sat}}}{R_v \, T^2}
$$

This is a separable ODE: $\dd P / P = (L_v / R_v) \, \dd T / T^2$. Integrating from a reference state $(T_{\mathrm{ref}}, P_{\mathrm{ref}})$ to $(T, P_{\mathrm{sat}})$, with $L_v$ treated as constant:

$$
\int_{P_{\mathrm{ref}}}^{P_{\mathrm{sat}}} \frac{\dd P'}{P'} = \frac{L_v}{R_v} \int_{T_{\mathrm{ref}}}^{T} \frac{\dd T'}{T'^2}
$$

The left-hand integral gives $\ln(P_{\mathrm{sat}}/P_{\mathrm{ref}})$. The right-hand integral gives $\left[-1/T'\right]_{T_{\mathrm{ref}}}^{T} = -(1/T - 1/T_{\mathrm{ref}})$. Therefore:

$$
\ln \frac{P_{\mathrm{sat}}}{P_{\mathrm{ref}}} = -\frac{L_v}{R_v}\left(\frac{1}{T} - \frac{1}{T_{\mathrm{ref}}}\right)
$$

Exponentiating both sides:

$$
\boxed{P_{\mathrm{sat}}(T) = P_{\mathrm{ref}} \exp\!\left[-\frac{L_v}{R_v}\left(\frac{1}{T} - \frac{1}{T_{\mathrm{ref}}}\right)\right]}
$$ (eq:clausius-clapeyron)

This is the **Clausius-Clapeyron equation**. The saturation vapour pressure depends **exponentially** on temperature through the ratio $L_v / R_v$, which has units of temperature and characterises the sensitivity of the phase transition.

**Worked example: water on Earth.**

For water vapour:
- $L_v = 2.50 \times 10^6$ J kg$^{-1}$ (latent heat of vaporisation at 0°C)
- $M = 0.018$ kg mol$^{-1}$, so $R_v = 8.314 / 0.018 = 462$ J kg$^{-1}$ K$^{-1}$
- Reference point: the triple point of water, $T_{\mathrm{ref}} = 273$ K, $P_{\mathrm{ref}} = 611$ Pa

The characteristic temperature scale is $L_v / R_v = 2.50 \times 10^6 / 462 \approx 5400$ K. This large value (compared to typical atmospheric temperatures) is why $P_{\mathrm{sat}}$ changes so rapidly with temperature.

At $T = 293$ K (20°C):

$$
\begin{aligned}
P_{\mathrm{sat}} &= 611 \exp\!\left[-5400\left(\frac{1}{293} - \frac{1}{273}\right)\right] \\
&= 611 \exp(1.35) \approx 611 \times 3.86 \approx 2360 \text{ Pa} \approx 2.4 \text{ kPa}
\end{aligned}
$$

The measured value is 2.3 kPa (excellent agreement). The small discrepancy arises because $L_v$ decreases slightly with temperature (from $2.50 \times 10^6$ J kg$^{-1}$ at 0°C to $2.26 \times 10^6$ J kg$^{-1}$ at 100°C), which we neglected by treating $L_v$ as constant.

**Application: condensing species across the solar system.**

The Clausius-Clapeyron equation applies to *any* vapour-to-liquid (or vapour-to-solid) transition. The following table lists the key condensing species in solar system atmospheres and their thermodynamic properties:

| Species | $L_v$<br>(kJ kg$^{-1}$) | $R_v$<br>(J kg$^{-1}$ K$^{-1}$) | $L_v/R_v$<br>(K) | $T_{\mathrm{cond}}$<br>(K)$^*$ | Where it condenses |
|---------|:-----:|:-----:|:-----:|:-----:|------|
| $\mathrm{H_2O}$ | 2500 | 462 | 5400 | 200–280 | Earth, Mars |
| $\mathrm{H_2SO_4}$ | 540 | 85 | 6400 | 230–360 | Venus |
| $\mathrm{NH_3}$ | 1370 | 488 | 2800 | 130–150 | Jupiter, Saturn |
| $\mathrm{CH_4}$ | 510 | 519 | 980 | 80–90 | Titan, Uranus, Neptune |
| $\mathrm{CO_2}$ | 571$^\dagger$ | 189 | 3020 | 100–150 | Mars |

$^*$Approximate condensation temperature at the pressure levels found in each planet's atmosphere.
$^\dagger$Latent heat of sublimation (solid $\leftrightarrow$ vapour).

Data from {cite:p}`Catling2017` and {cite:p}`dePaterLissauer2010`.

The large $L_v/R_v$ ratio for $\mathrm{H_2SO_4}$ makes its saturation curve extremely steep, so the crossing from vapour to droplets happens over a small temperature interval: Venus's cloud base near 48 km is sharply defined, and droplets that settle below it evaporate quickly. Conversely, $\mathrm{CH_4}$ has a low $L_v/R_v$: its flat saturation curve keeps methane on Titan close to saturation through much of the troposphere, so clouds can form over a wide range of altitudes.
```

```{figure} figures/water_phase_diagram.avif
:name: fig:water-phase-diagram
:width: 600px
:align: center

Phase diagram of water in $P$-$T$ space.
The liquid-vapour coexistence curve (blue) is the integrated Clausius-Clapeyron relation (Eq. {eq}`eq:clausius-clapeyron`); the solid-vapour (sublimation) curve (cyan) is the analogous Clausius-Clapeyron relation with the latent heat of sublimation; and the solid-liquid curve (black) has the anomalously negative slope characteristic of water (ice less dense than liquid).
Because the integrated relation assumes a constant $L_v$, the blue curve is drawn with an effective $L_v = 2.29 \times 10^6$ J kg$^{-1}$, the single value that makes it pass through both the triple point and the critical point; the worked example above instead uses the 0°C value $L_v = 2.50 \times 10^6$ J kg$^{-1}$ over a much narrower temperature range.
The black curve is the melting curve of ice Ih only, and it stops where that field ends near 0.2 GPa; at higher pressure the slope reverses and denser ice phases take over, which the figure does not show.
The triple point (273.16 K, 611.7 Pa) defines the unique state at which all three phases coexist.
The critical point (647 K, 22.1 MPa) marks the end of the liquid-vapour distinction.
Earth's surface (288 K, 1 bar) sits well within the liquid-vapour stability field, which is why liquid water is the dominant condensable on the planet.
The blackboard derivation in this lecture integrates the Clausius-Clapeyron equation along the blue curve.
```


## Clouds across the solar system

Every planet and moon with a substantial atmosphere has clouds, but the condensing species and the cloud structure vary enormously. Here we survey the major cloud systems in our solar system {cite:p}`SanchezLavega2011`.

### Venus: sulfuric acid clouds

Venus is permanently shrouded in thick clouds that completely obscure the surface at visible wavelengths. These clouds are composed of $\mathrm{H_2SO_4}$ (sulfuric acid) droplets and extend from $\sim$48 km to $\sim$70 km altitude, spanning a temperature range of roughly 360–230 K between cloud base and cloud top {cite:p}`Catling2017`.

The cloud deck completely obscures the surface in visible light ({numref}`fig:venus-uv-clouds`); UV imaging reveals the banded pattern produced by **super-rotation**, the clouds circling the planet far faster than the solid surface rotates beneath them. The sulfuric acid is produced by **photochemistry** in the upper atmosphere:

$$
\mathrm{SO_2} + \mathrm{O} \longrightarrow \mathrm{SO_3}, \qquad \mathrm{SO_3} + \mathrm{H_2O} \longrightarrow \mathrm{H_2SO_4}
$$

where the atomic oxygen comes from ultraviolet photolysis of $\mathrm{CO_2}$ high in the atmosphere, and the $\mathrm{SO_2}$ is supplied by volcanic outgassing. Below the main cloud deck lies a diffuse sub-cloud haze extending down to $\sim$31 km. An unidentified **UV absorber** in the upper clouds absorbs roughly half the solar UV flux and creates the distinctive banded patterns visible in ultraviolet images. Venus's vertical thermal structure with cloud-deck and sub-cloud-haze altitude bands is shown in {numref}`fig:venus-tz`.

```{figure} figures/venus_uv_clouds.avif
:name: fig:venus-uv-clouds
:figwidth: 100%
:width: 100%
:align: center

Venus imaged by the *Mariner 10* spacecraft in February 1974, using a false-colour composite of orange and ultraviolet filters to reveal the banded cloud structure driven by atmospheric super-rotation. The $\mathrm{H_2SO_4}$ cloud deck extends from $\sim$48 to $\sim$70 km altitude and completely obscures the surface. Credit: NASA/JPL-Caltech, public domain.
```

```{figure} figures/venus_tz_profile.avif
:name: fig:venus-tz
:width: 480px
:align: center

Venus thermal structure from the surface (737 K, 92 bar) to 100 km altitude, based on the *Venus International Reference Atmosphere* and the *Venus Express* radio-science experiment {cite:p}`Tellmann2009`.
The $\mathrm{H_2SO_4}$ cloud deck (yellow band, 48-70 km) sits where the temperature traverses $\sim$230-360 K between cloud top and cloud base, within the thermodynamic stability field of concentrated sulfuric acid droplets; the sub-cloud haze (peach band, 31-48 km) lies just below.
The cold collar inversion layer near 62-65 km altitude, prominent in the VeRa retrievals at high latitudes ($\sim$65-75°), sits where the temperature inversion shapes the upper boundary of the cloud system.
```

### Mars: dust and ice clouds

Mars's thin atmosphere ($\sim$6 mbar surface pressure) supports two types of clouds:

- **$\mathrm{CO_2}$ ice clouds** form at high altitudes ($\sim$50–100 km) where temperatures drop below the local $\mathrm{CO_2}$ frost point ($\sim$148 K at the 6 mbar surface pressure, near 100 K at mesospheric pressures). These are thin, wispy clouds, sometimes called "mesospheric" clouds.
- **$\mathrm{H_2O}$ ice clouds** form at lower altitudes ($\sim$10–30 km), particularly over the Tharsis volcanic region and in the aphelion cloud belt near the equator during northern summer.

**Mineral dust** plays a central role in Martian atmospheric physics: wind-lofted dust particles serve as condensation nuclei for ice clouds, and dust itself is a powerful radiative agent, absorbing solar radiation and heating the atmosphere, which can trigger positive feedback loops leading to global dust storms (see [weather and storms](weather-storms) below).

```{figure} figures/mars_water_ice_clouds.avif
:name: fig:mars-water-ice-clouds
:figwidth: 100%
:width: 100%
:align: center

Water-ice clouds over the Tharsis region of Mars near dawn, viewed along the limb from orbit. The dark peak breaking through the bright cloud canopy (left of centre) is the summit of the shield volcano **Arsia Mons**. These are the $\mathrm{H_2O}$ ice clouds described above. They form when air cools as it rises over the high volcanic terrain, and again near the equator when the seasonal aphelion cloud belt develops. The panorama was recorded by the THEMIS instrument on NASA's *Mars Odyssey* orbiter on 2 May 2025.
Credit: NASA/JPL-Caltech/ASU, public domain.
```

### Titan: methane rain

Saturn's moon Titan hosts the only known active **hydrological cycle** beyond Earth, but with $\mathrm{CH_4}$ (methane) playing the role of water. Titan's surface temperature ($\sim$94 K) and pressure ($\sim$1.5 bar) place it near the triple point of methane, enabling liquid methane on the surface (lakes and seas), methane clouds in the troposphere, and methane rain {cite:p}`dePaterLissauer2010`.

Titan's clouds are mostly $\mathrm{CH_4}$ (condensing at $\sim$8–30 km altitude) with some $\mathrm{C_2H_6}$ (ethane). Unlike Earth's water cycle, which is driven by solar evaporation, Titan's methane cycle is sluggish: rainfall is infrequent but intense when it occurs, creating transient rivers and channels carved into the icy surface ({numref}`fig:titan-lakes`, {numref}`fig:titan-clouds`). The Cassini-Huygens mission observed clouds forming preferentially at Titan's south pole (then in summer), with seasonal shifts as Titan orbits Saturn.

```{figure} figures/titan_lakes.avif
:name: fig:titan-lakes
:width: 550px
:align: center

Titan's north polar lake district imaged by the *Cassini* RADAR instrument. The first detection {cite:p}`Stofan2007` resolved more than 75 radar-dark lake-like patches poleward of $\sim$70°N latitude, ranging from 3 to over 70 km across; subsequent Cassini RADAR coverage of the high-latitude seas mapped the three largest *maria*: *Kraken Mare*, *Ligeia Mare*, and *Punga Mare*, each hundreds of kilometres across, here interpreted as standing bodies of liquid methane and ethane.
Together with the methane-cloud observations and inferred rainfall, these lakes constitute the visible surface end of the only active hydrocarbon hydrological cycle in the solar system.
Credit: NASA/JPL-Caltech/ASI/USGS, public domain.
```

```{figure} figures/titan_clouds.avif
:name: fig:titan-clouds
:width: 480px
:align: center

Methane-ethane clouds at Titan's mid-southern latitudes captured by the *Cassini* Imaging Science Subsystem in the 938 nm methane window.
The bright streaks near the limb are tropospheric clouds organised along the local zonal (east-west) wind, which shows that Titan supports an active condensation cycle of the same Clausius-Clapeyron physics described in this lecture, but with $\mathrm{CH_4}$ replacing $\mathrm{H_2O}$ at $T \approx 90$ K.
Credit: NASA/JPL-Caltech/Space Science Institute, public domain.
```

### Giant planets: layered cloud structure

The hydrogen-dominated atmospheres of Jupiter and Saturn host a **vertically layered** cloud structure, predicted by the Clausius-Clapeyron equation applied to each condensing species at the temperature and pressure where it reaches saturation {cite:p}`dePaterLissauer2010`:

1. **$\mathrm{NH_3}$ ice** (topmost layer): condensing at $T \sim 130$–150 K, $P \sim 0.5$–1 bar. These are the clouds we see in visible light: the white and coloured bands of Jupiter.
2. **$\mathrm{NH_4SH}$** (ammonium hydrosulfide): condensing at $T \sim 200$–240 K, $P \sim 2$–3 bar. Formed by the reaction $\mathrm{NH_3} + \mathrm{H_2S} \to \mathrm{NH_4SH}$.
3. **$\mathrm{H_2O}$ ice and liquid** (deepest layer): condensing at $T \sim 270$–300 K, $P \sim 5$–7 bar. These deep water clouds are difficult to observe directly but are thought to play a critical role in powering Jupiter's weather through latent heat release.

The vertical layering of these three cloud decks is sketched in {numref}`fig:jupiter-cloud-layers`; the visible cloud-band morphology is shown in the full-disk Hubble portrait in {numref}`fig:jupiter-global-map`.

```{figure} figures/jupiter_cloud_layers.avif
:name: fig:jupiter-cloud-layers
:figwidth: 100%
:width: 100%
:align: center

Temperature–pressure profile of Jupiter's atmosphere, showing the three main cloud layers: ammonia ($\mathrm{NH_3}$) ice at the top ($\sim$1 bar), ammonium hydrosulfide ($\mathrm{NH_4SH}$) in the middle ($\sim$2–3 bar), and water ($\mathrm{H_2O}$) at the deepest level ($\sim$5–7 bar). The **tropopause**, the boundary where temperature stops falling with altitude and convective mixing gives way to a stably stratified layer above, sits at $\sim$50 km, and the stratosphere–thermosphere boundary at $\sim$320 km is marked as well. Each cloud layer forms where the local temperature crosses the saturation curve for that species. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

```{figure} figures/jupiter_global_map.avif
:name: fig:jupiter-global-map
:width: 480px
:align: center

Full-disk portrait of Jupiter from the Hubble Space Telescope, observed on 4 September 2021 as part of the Outer Planets Atmospheres Legacy (OPAL) programme.
The banded structure is clear: light *zones* (rising air topped by high $\mathrm{NH_3}$-ice clouds) alternate with dark *belts* (sinking air that exposes the deeper $\mathrm{NH_4SH}$ layer).
The Great Red Spot appears at $\sim$22°S, just south of the dark South Equatorial Belt.
These narrow latitudinal contrasts trace the alternating zonal-jet system that long-term Hubble programmes have monitored for over a decade {cite:p}`Wong2020`; the jets extend to $\sim \pm 60^\circ$ and are summarised quantitatively in {numref}`fig:jupiter-zonal-winds`.
Credit: NASA, ESA, A. Simon (GSFC), M. H. Wong (UC Berkeley), and the OPAL team; ESA/Hubble, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```

The ice giants **Uranus** and **Neptune** have a different cloud hierarchy reflecting their colder temperatures and distinct compositions: $\mathrm{CH_4}$ ice forms the uppermost visible cloud layer ($T \sim 80$ K), with $\mathrm{H_2S}$ below it, and deeper $\mathrm{NH_4SH}$ and $\mathrm{H_2O}$ layers.


## Atmospheric dynamics

Atmospheres are not static: they are vast heat engines driven by uneven heating. The equator receives more solar energy per unit area than the poles, creating a temperature gradient that drives global-scale circulation patterns. How the atmosphere redistributes this heat depends on the planet's rotation rate, size, and atmospheric properties {cite:p}`SanchezLavega2011`.

### The Hadley cell

The simplest atmospheric circulation pattern, first described by George Hadley in 1735, works as follows:

1. Intense solar heating at the equator warms the surface and the air above it.
2. Warm, buoyant air **rises** at the equator, creating a low-pressure zone (the *Intertropical Convergence Zone*, ITCZ).
3. At altitude, the air flows **poleward** (toward higher latitudes).
4. As it moves poleward, it cools radiatively, becomes denser, and **sinks** at $\sim$30° latitude (the subtropics), creating high-pressure zones (where Earth's great deserts are located).
5. At the surface, air flows back toward the equator to replace the rising air: these return flows are the **trade winds**.

This loop is the **Hadley cell** ({numref}`fig:hadley-cells`). It is the dominant circulation pattern in the tropics on Earth and the primary mechanism for transporting heat from the equator toward the poles. The full three-cell structure (Hadley + Ferrel + polar) per hemisphere is captured by the zonal-mean (averaged around each latitude circle) meridional (north-south) streamfunction in {numref}`fig:hadley-observed`.

```{figure} figures/hadley_cells.svg
:name: fig:hadley-cells
:width: 500px
:align: center

Schematic of Earth's atmospheric circulation, showing the three-cell structure in each hemisphere: the Hadley cell (equator to $\sim$30°), the Ferrel cell ($\sim$30° to $\sim$60°, labelled "mid-latitude cell" here), and the polar cell ($\sim$60° to the pole). The northeasterly and southeasterly trade winds and the westerlies are labelled as the surface expression of these cells, together with the intertropical convergence zone at the equator and the subtropical high-pressure belt. The Coriolis effect deflects the winds to the right in the Northern Hemisphere and to the left in the Southern Hemisphere. Credit: Wikimedia Commons, public domain.
```

```{figure} figures/hadley_observed.avif
:name: fig:hadley-observed
:width: 600px
:align: center

Idealised zonal-mean meridional streamfunction of Earth's troposphere, plotted as latitude versus altitude.
Solid blue contours mark clockwise overturning in this latitude-altitude view, the sense of the Northern-Hemisphere Hadley cell (rising at the equator, poleward aloft, sinking near 30°); dashed red contours mark counter-clockwise overturning, arrows on the two Hadley cells show the flow direction, and the dashed black line indicates the tropopause.
The two thermally direct Hadley cells flank the equator from the surface to $\sim$15 km, the indirect Ferrel cells lie between $\sim$30° and $\sim$60° in each hemisphere, and the weak polar cells sit poleward of $\sim$60°.
The cell structure follows the {cite:t}`Held1980` axisymmetric theory of nearly inviscid atmospheres.
```

### The Coriolis effect

On a rotating planet, air that moves in a straight line (as seen from an inertial frame) appears to be **deflected** as seen from the rotating surface. This apparent deflection is the **Coriolis effect**: moving air is deflected to the *right* in the Northern Hemisphere and to the *left* in the Southern Hemisphere.

The magnitude of the Coriolis acceleration depends on the planet's angular rotation rate $\Omega$ and the latitude $\phi$ through the **Coriolis parameter**:

$$
f = 2\Omega \sin\phi
$$

For Earth, $\Omega = 7.29 \times 10^{-5}$ rad s$^{-1}$ (sidereal rotation rate). At mid-latitudes ($\phi = 45°$), $f \approx 1.03 \times 10^{-4}$ s$^{-1}$. At the equator ($\phi = 0°$), $f = 0$: the Coriolis effect vanishes. The kinematic origin of the deflection is shown in {numref}`fig:coriolis`.

```{figure} figures/coriolis_effect.avif
:name: fig:coriolis
:width: 560px
:align: center

Geometric origin of the Coriolis deflection, viewed from above the rotating planet's north pole (centre), with the equator at the rim.
A projectile launched from the pole has no eastward velocity, so on a non-rotating planet it would travel straight to its target (dashed line).
Because the planet turns east under the flight with angular velocity $\Omega$, the track over the ground curves to the right of the direction of travel in the Northern Hemisphere (red curve) and lands to the right of the target.
Launching from the pole isolates the effect: the aim is a straight radial line, and the deflection comes entirely from the ground rotating beneath the flight.
The strength of the deflection is set by the Coriolis parameter $f = 2 \Omega \sin \phi$: it vanishes at the equator and is strongest at the poles, and in the Southern Hemisphere the deflection is mirrored to the left.
The deflection angle shown is exaggerated for clarity.
```

### The Rossby number

Whether rotation significantly influences a particular atmospheric flow depends on the **Rossby number**, which compares the inertial acceleration to the Coriolis acceleration:

$$
\mathrm{Ro} = \frac{U}{f L}
$$

where $U$ is the characteristic wind speed and $L$ is the characteristic horizontal length scale of the flow.

- $\mathrm{Ro} \ll 1$: Rotation dominates; the flow is strongly influenced by the Coriolis effect. This applies to large-scale atmospheric and oceanic circulation on Earth (e.g., $U \sim 10$ m s$^{-1}$, $L \sim 1000$ km $\Rightarrow \mathrm{Ro} \sim 0.1$).
- $\mathrm{Ro} \gg 1$: Rotation is unimportant; the flow is governed by pressure gradients and friction. This applies to small-scale phenomena like tornadoes and dust devils.

### Circulation cells and rotation rate

The number of circulation cells depends critically on the planet's rotation rate {cite:p}`dePaterLissauer2010`:

- **Slowly rotating planets** (Venus, Titan): A single Hadley cell extends from equator to pole in each hemisphere. Venus has one giant Hadley cell per hemisphere despite being nearly the same size as Earth, because its slow rotation (243-day period) gives very small Coriolis forces ($\mathrm{Ro} \gg 1$ for large-scale flows).
- **Moderately rotating planets** (Earth): The Hadley cell extends to $\sim$30° latitude, where the Coriolis deflection becomes strong enough to break the cell. Two additional cells form at higher latitudes: the **Ferrel cell** (mid-latitudes, driven indirectly by the Hadley and polar cells) and the **polar cell**. Earth has three cells per hemisphere.
- **Rapidly rotating planets** (Jupiter, Saturn): Many alternating cells form, producing the characteristic **banded structure** of alternating light zones (rising air, high clouds) and dark belts (sinking air, deeper cloud exposure). Jupiter and Saturn each show many alternating jets per hemisphere, extending to roughly $\pm 60^\circ$ latitude.

The transition between regimes is governed by the ratio of the planet's rotation timescale to the advective timescale across the planet. When rotation is fast compared to the time for air to flow from equator to pole, the flow breaks up into multiple cells.


## Geostrophic balance and jet streams

### Geostrophic balance

At large scales (low Rossby number), the atmosphere reaches a steady state in which the **Coriolis force** balances the **pressure gradient force**. This balance is called **geostrophic balance** and is the dominant force balance for large-scale weather systems on Earth and the banded circulations of the giant planets {cite:p}`Pierrehumbert2010`.

In vector form, geostrophic balance reads:

$$
f \hat{k} \times \mathbf{v}_g = -\frac{1}{\rho} \nabla P
$$ (eq:geostrophic-balance)

where $\hat{k}$ is the unit vector pointing upward (along the rotation axis), $\mathbf{v}_g$ is the geostrophic wind, $\rho$ is the air density, and $\nabla P$ is the horizontal pressure gradient.

The key consequence is that the **geostrophic wind blows parallel to isobars** (lines of constant pressure), not from high to low pressure as one might naively expect. In the Northern Hemisphere, the wind blows with low pressure to its left; in the Southern Hemisphere, low pressure is to the right. This is why large-scale weather systems (cyclones and anticyclones) rotate around pressure centres rather than flowing directly toward them.

The vector force balance, with the wind blowing parallel to isobars rather than down the pressure gradient, is shown in {numref}`fig:geostrophic-balance`. In scalar form, the geostrophic wind components are:

$$
u_g = -\frac{1}{f\rho} \pdv{P}{y}, \qquad v_g = \frac{1}{f\rho} \pdv{P}{x}
$$

where $x$ and $y$ are the eastward and northward directions, respectively.

```{figure} figures/geostrophic_balance.avif
:name: fig:geostrophic-balance
:width: 480px
:align: center

Geostrophic balance between the horizontal pressure-gradient force ($-\nabla P / \rho$, blue arrow) and the Coriolis force ($-f \hat{k} \times \mathbf{v}_g$, red arrow), giving a wind $\mathbf{v}_g$ that blows parallel to the isobars rather than down the pressure gradient. In the Northern Hemisphere the balanced wind keeps low pressure to its left. This is the dominant balance for large-scale flow on Earth and the giant planets ({numref}`fig:jupiter-zonal-winds`) where the Rossby number is small.
```

### Jet streams

**Jet streams** are narrow bands of fast-moving air ($\sim$30–70 m s$^{-1}$ on Earth) that form at the boundaries between circulation cells, where horizontal temperature gradients are strongest. Their existence is a direct consequence of the **thermal wind relation**, which connects vertical wind shear to horizontal temperature gradients:

$$
\pdv{\mathbf{v}_g}{z} \propto \hat{k} \times \nabla T
$$

Where the temperature gradient between the warm tropics and the cold poles is steepest (at $\sim$30° and $\sim$60° latitude on Earth), the wind speed increases with altitude, producing the subtropical and polar jet streams. These jet streams steer weather systems across the planet and are critical for understanding weather patterns ({numref}`fig:earth-jet-stream`).

```{figure} figures/earth_jet_stream.avif
:name: fig:earth-jet-stream
:width: 600px
:align: center

An Earth-from-orbit astronaut photograph showing long cirrus filaments streaked across the limb above a dark sea and coastline.
Such aligned cirrus bands trace the upper-tropospheric jet core at $\sim$200-250 hPa, where horizontal temperature gradients drive thermal-wind shear of order 30-70 m s$^{-1}$; weather systems are steered along the layer in which these filaments form.
Credit: NASA astronaut photograph, Johnson Space Center, public domain.
```

### Giant planet banding

On Jupiter and Saturn, the same physics operates on a grander scale. The alternating light and dark bands (the **zones** and **belts**) correspond to regions of rising and sinking air with alternating wind directions. Between adjacent bands, strong **zonal jets** (east-west winds) reach peak speeds of $\sim$180 m s$^{-1}$ on Jupiter and $\sim$400 m s$^{-1}$ on Saturn. The jets ({numref}`fig:jupiter-zonal-winds`) are remarkably stable over decades of observation and extend deep into the planetary interior, as revealed by Juno's gravity measurements {cite:p}`Kaspi2018`.

```{figure} figures/jupiter_zonal_winds.avif
:name: fig:jupiter-zonal-winds
:width: 420px
:align: center

Jupiter's cloud-top zonal wind profile $u(\phi)$, schematic representation of the HST composite (1995-2000) of {cite:t}`GarciaMelendo2001`.
A ladder of narrow prograde (eastward, blue) and retrograde (westward, red) jets is stacked from the broad equatorial superrotating jet at the centre out to $\sim$60° latitude (the schematic resolves only the principal jets to keep the figure legible).
The jets coincide with the boundaries between bright zones and dark belts visible in {numref}`fig:jupiter-global-map`, and Juno gravity measurements yield a best-fit e-folding decay depth (the depth over which the jet strength falls by a factor of $1/e$) of $\sim$1800 km, with the full uncertainty range spanning $\sim$1000-3000 km into the molecular envelope {cite:p}`Kaspi2018`.
```


(weather-storms)=
## Weather and storms across the solar system

Planets and moons exhibit a stunning variety of weather phenomena, from gentle breezes to apocalyptic storms. Here we survey the highlights.

### Mars: dust storms and seasonal cycles

Mars experiences dramatic weather driven by its thin atmosphere and strong seasonal forcing. Two phenomena stand out {cite:p}`Catling2017`:

- **Dust storms:** Local dust storms are common, lofting mineral particles to $\sim$10–30 km altitude. Occasionally, these storms grow to engulf the entire planet in a **global dust storm** ({numref}`fig:mars-dust-storm`), reducing surface visibility to near zero for weeks. The most recent global dust storms occurred in 2018 and 2007. The feedback mechanism is straightforward: dust absorbs solar radiation $\Rightarrow$ heats the atmosphere $\Rightarrow$ drives stronger winds $\Rightarrow$ lofts more dust, a positive feedback loop.

- **Seasonal $\mathrm{CO_2}$ cycle:** Mars's polar caps contain solid $\mathrm{CO_2}$ (dry ice). During winter at a given hemisphere, atmospheric $\mathrm{CO_2}$ freezes onto that polar cap; during summer, it sublimes back into the atmosphere. This exchange involves $\sim$25–30% of the total atmospheric mass: global mean surface pressure swings from $\sim$7 mbar in southern spring and summer, when the massive southern $\mathrm{CO_2}$ cap sublimates, to $\sim$5 mbar in southern winter, when the cap refreezes, a phenomenon with no analogue on Earth.

```{figure} figures/mars_dust_storm.avif
:name: fig:mars-dust-storm
:width: 550px
:align: center

Mars before and during the 2018 global dust storm, as imaged by the Mars Reconnaissance Orbiter. The left panel shows clear atmospheric conditions with surface features visible; the right panel shows the planet almost completely obscured by wind-lofted mineral dust. The storm ultimately ended the *Opportunity* rover's 15-year mission by blocking sunlight to its solar panels. Credit: NASA/JPL-Caltech/MSSS, public domain.
```

### Venus: super-rotation

Venus presents one of the great puzzles of atmospheric dynamics: its atmosphere's rotation period of $\sim$4 days is $\sim$60 times shorter than the planet's 243-day solid-body rotation (angular-velocity ratio), with cloud-top winds reaching $\sim$100 m s$^{-1}$ while the solid surface rotates retrograde. This phenomenon is called **atmospheric super-rotation** {cite:p}`SanchezLavega2011`.

Super-rotation requires a mechanism to transport angular momentum from the slowly rotating surface *upward and equatorward*, against the usual sense of friction, which should slow the atmosphere down to match the surface. The leading explanation involves a combination of **thermal tides** (driven by solar heating of the cloud layer) and **planetary-scale waves** that pump angular momentum toward the equator. Despite decades of study, the detailed mechanism remains an active area of research. The latitude-dependent zonal and meridional wind structure mapped by Venus Express VIRTIS is shown in {numref}`fig:venus-zonal-winds`.

```{figure} figures/sanchezlavega2008_venus_winds.avif
:name: fig:venus-zonal-winds
:width: 380px
:align: center

Averaged zonal (top) and meridional (bottom) wind profiles in Venus's southern hemisphere at cloud level (April 2006-June 2007), as a function of latitude. Cloud tracers were measured at three wavelengths probing different altitudes: ultraviolet (380 nm, upper cloud $\sim 66$ km, day; blue), near-infrared (980 nm, upper cloud $\sim 61$ km, day; violet), and infrared (1.74 µm, lower cloud $\sim 47$ km, night; red). Zonal winds at low latitudes reach $\sim 105$ m s$^{-1}$ at the cloud tops but only $\sim 60$-$70$ m s$^{-1}$ at the cloud base; meridional winds are poleward at the cloud tops with peak $\sim 10$ m s$^{-1}$. The cloud-top winds are $\sim 60$ times faster than the planet's solid-body rotation, a state known as atmospheric super-rotation. Reproduced from {cite:p}`SanchezLavega2008`, Fig. 2.
```

### Jupiter: the Great Red Spot

Jupiter's **Great Red Spot (GRS)** is the largest and longest-lived storm in the solar system ({numref}`fig:jupiter-grs`): an anticyclonic vortex larger than Earth, with winds reaching $\sim$120 m s$^{-1}$ at its periphery. The first telescopic sightings, attributed to Robert Hooke in 1664 and Giovanni Cassini around 1665, may or may not be the same feature; uninterrupted observations date from 1830.

```{figure} figures/jupiter_great_red_spot.avif
:name: fig:jupiter-grs
:width: 500px
:align: center

Jupiter's Great Red Spot and surrounding turbulent atmosphere, imaged by NASA's *Juno* spacecraft during a close flyby. The Great Red Spot is an anticyclonic storm larger than Earth that has persisted for centuries. The surrounding vortices and chaotic cloud patterns reveal the intense turbulence of Jupiter's upper troposphere. Credit: NASA/JPL-Caltech/SwRI/MSSS, public domain.
```

The GRS sits between two zonal jets with opposite directions, which confine and sustain it. Its longevity is remarkable: on Earth, the largest hurricanes dissipate within days once they lose their energy source (warm ocean water). The GRS is sustained by absorbing smaller vortices and by latent heat released from $\mathrm{H_2O}$ condensation deep in the atmosphere. However, the GRS has been slowly shrinking over the past century, and its long-term fate remains uncertain {cite:p}`dePaterLissauer2010`. Jupiter's poles host a different organising principle: a stable octagonal cluster of cyclones around the north pole ({numref}`fig:juno-polar-cyclones`).

```{figure} figures/juno_polar_cyclones.avif
:name: fig:juno-polar-cyclones
:width: 480px
:align: center

Polar cyclone cluster at Jupiter's north pole imaged by the JIRAM infrared spectrometer on NASA's *Juno* spacecraft.
A central cyclone is encircled by eight smaller cyclones in a stable octagonal arrangement, which shows that Jupiter's atmospheric dynamics produce coherent polygonal vortex patterns analogous to Saturn's hexagonal jet ({numref}`fig:saturn-hexagon`).
The cyclones have remained in this configuration over multiple Juno **perijoves** (the spacecraft's closest approaches to Jupiter on each orbit) spanning several years, far longer than any Earth analogue.
At the south pole, a pentagonal cluster of five circumpolar cyclones remained remarkably stable through perijove 18 (February 2019) {cite:p}`Adriani2020`; a sixth cyclone briefly joined the southern pentagon in late 2019 but dissipated within about two months without merging, leaving the pentagonal arrangement intact {cite:p}`Mura2021`.
Adapted from {cite:t}`Adriani2018`.
Credit: NASA/JPL-Caltech/SwRI/ASI/INAF/JIRAM, public domain.
```

### Saturn: the hexagonal jet stream

Saturn's north pole hosts one of the most geometrically striking features in the solar system: a persistent **hexagonal jet stream** ({numref}`fig:saturn-hexagon`) encircling the pole at $\sim$78°N latitude, first seen in the Voyager flyby images of 1980-81 and extensively imaged by Cassini.

```{figure} figures/saturn_hexagon.avif
:name: fig:saturn-hexagon
:width: 480px
:align: center

Saturn's hexagonal jet stream encircling the north pole at $\sim$78°N, imaged by NASA's *Cassini* spacecraft in November 2012.
The hexagonal pattern is interpreted as a stable Rossby wave with six-fold symmetry, sustained by the prograde polar jet at its boundary.
The hexagon spans $\sim$30,000 km across, larger than Earth's diameter, and has persisted since its discovery in the *Voyager 1* and *2* flyby images of 1980-81.
Credit: NASA/JPL-Caltech/SSI/Hampton University, public domain.
```

The hexagonal shape is explained as a stable **Rossby wave**, a large-scale atmospheric wave whose restoring force is the variation of the Coriolis parameter with latitude. When the jet stream speed and width satisfy certain resonance conditions, the wave locks into a pattern with a specific number of sides. Laboratory experiments with rotating fluids have reproduced hexagonal and other polygonal patterns under analogous conditions.

Saturn also experiences periodic **Great White Storms** roughly every 30 years (most recently in 2010), which are massive convective outbursts that encircle the planet within weeks: the Saturnian equivalent of a planet-wide thunderstorm.

### Neptune: extreme weather on a cold world

Despite receiving only $\sim$1/900th of Earth's solar flux, Neptune has the **fastest winds** in the solar system, with its retrograde equatorial jet reaching $\sim$580 m s$^{-1}$ ($\sim$2100 km h$^{-1}$). The Voyager 2 flyby in 1989 revealed a **Great Dark Spot** similar to Jupiter's GRS ({numref}`fig:neptune-dark-spot`), though subsequent Hubble observations showed it had vanished while new ones had formed, suggesting Neptune's storms are more transient than Jupiter's.

```{figure} figures/neptune_great_dark_spot.avif
:name: fig:neptune-dark-spot
:width: 400px
:align: center

Neptune's *Great Dark Spot* (centre-left, with bright "scooter" cloud feature below) and *Dark Spot 2* (lower right), imaged by *Voyager 2* in August 1989.
The Great Dark Spot was a high-pressure anticyclone roughly the size of Earth. The adjacent zonal flow (Neptune's equatorial retrograde jet reaches $\sim 580$ m s$^{-1}$, the fastest winds measured in the solar system) helped confine and transport the storm.
Hubble follow-up imaging just a few years later showed that the original Great Dark Spot had dissipated and new dark spots had appeared elsewhere on the planet, which shows that Neptune's storms are far more transient than Jupiter's GRS.
Credit: NASA/JPL-Caltech, public domain.
```

Neptune's vigorous weather is powered primarily by **internal heat**: Neptune radiates $\sim$2.6 times more energy than it receives from the Sun, driven by slow gravitational contraction and possibly differentiation in the interior ({ref}`Lecture 3 <lecture03>`). This internal heat source drives convection and storms even in the near-absence of solar heating.


## Climate evolution and the faint young Sun

On timescales of billions of years, a planet's climate is not constant: it evolves in response to changes in the host star's luminosity, the atmospheric composition, and geological processes. The most celebrated example of this long-term evolution is the **faint young Sun paradox** {cite:p}`Feulner2012`.

### Solar luminosity evolution

The Sun, like all main-sequence stars, has been gradually brightening as hydrogen is converted to helium in the core. The increasing mean molecular weight requires higher core temperatures to maintain pressure support, which increases the nuclear reaction rate and hence the luminosity. A standard solar evolution model gives {cite:p}`Gough1981,Catling2017`:

$$
\frac{L(t)}{\Lsun} \approx \left[1 + \frac{2}{5}\left(1 - \frac{t}{t_\odot}\right)\right]^{-1}
$$ (eq:solar-luminosity-evolution)

where $t$ is the time since the Sun's formation and $t_\odot \approx 4.57$ Gyr is the present age of the Sun. At formation ($t = 0$):

$$
\frac{L(0)}{\Lsun} = \frac{1}{1.4} \approx 0.71
$$

The early Sun was **$\sim$30% less luminous** than today. Even 4 Gyr ago (when the first evidence for life on Earth appears), the Sun was still $\sim$25% fainter ({numref}`fig:solar-luminosity`).

```{figure} figures/feulner2012_solar_luminosity.avif
:name: fig:solar-luminosity
:width: 700px
:align: center

Evolution of solar luminosity over the four geologic eons (Hadean, Archean, Proterozoic, Phanerozoic; labelled bands at top), normalised to the present-day value. The standard-solar-model curve from Bahcall et al. (2001) (solid line) and the analytic approximation by {cite:t}`Gough1981` (dashed line, Eq. {eq}`eq:solar-luminosity-evolution`) agree to better than $\sim 0.1\%$ over the past 4 Gyr. At $t = 0$ (left edge, $\sim 4.5$ Gyr ago) the Sun was about $30\%$ less luminous than today; the Archean climate problem of maintaining liquid surface water under this faint young Sun is the *faint young Sun paradox*. Reproduced from {cite:p}`Feulner2012`, Fig. 1.
```

### The paradox

A 30% reduction in solar luminosity would reduce Earth's effective temperature from 255 K to:

$$
T_{\mathrm{eff}} = 255 \times (0.71)^{1/4} \approx 234 \text{ K}
$$

Combined with a greenhouse effect similar to today's, this would yield a surface temperature well below freezing: the entire ocean should have been **frozen solid**. Yet geological evidence tells a strikingly different story:

- **Zircon crystals** from 4.4 Ga show oxygen isotope ratios ($\delta^{18}\mathrm{O}$) consistent with liquid water interacting with rock at the surface.
- **Pillow basalts** (lava cooled underwater) and **sedimentary rocks** (requiring liquid water for transport and deposition) date back to at least 3.8 Ga.
- **Stromatolites** (microbial mat fossils) at 3.5 Ga and possible carbon isotope signatures of life at 3.8 Ga imply liquid water and conditions warm enough for biology.

This contradiction, a faint Sun that should have frozen the Earth versus geological evidence for liquid water, is the **faint young Sun paradox**, first articulated by {cite:t}`SaganMullen1972`.

### Possible solutions

Several mechanisms have been proposed to resolve the paradox {cite:p}`Feulner2012`:

- **Enhanced $\mathrm{CO_2}$ greenhouse:** If the early atmosphere contained 10–1000 times more $\mathrm{CO_2}$ than today (plausible: with less continental area exposed to weathering on the early Earth, the carbonate-silicate thermostat of the next section settles at a higher $\mathrm{CO_2}$ level), the enhanced greenhouse warming could compensate for the weaker Sun.
- **Methane greenhouse:** Biogenic $\mathrm{CH_4}$ from early methanogens could have provided additional greenhouse warming. $\mathrm{CH_4}$ is a potent greenhouse gas, and in an anoxic (oxygen-free) early atmosphere, it would have had a much longer lifetime than today.
- **$\mathrm{N_2}$ pressure broadening:** A thicker $\mathrm{N_2}$ atmosphere (2–3 times present levels) would enhance greenhouse warming through pressure broadening of $\mathrm{CO_2}$ and $\mathrm{H_2O}$ absorption lines.
- **Lower albedo:** Without continents (less land area in the Archean) and potentially fewer clouds, the early Earth may have reflected less sunlight, absorbing more energy despite the lower luminosity.

The most likely resolution is a combination of elevated $\mathrm{CO_2}$ and $\mathrm{CH_4}$ concentrations, regulated by the carbonate-silicate cycle (next section).

### The Mars climate puzzle

Mars poses an even more extreme version of the same problem. At 1.52 AU, Mars receives less than half of Earth's solar flux, and with the faint young Sun, the situation is even worse. Yet Mars shows compelling geological evidence for warm, wet conditions during the **Noachian** period ($>$3.7 Ga): extensive valley networks carved by flowing water ({numref}`fig:mars-valleys`), clay minerals formed by aqueous weathering, and sedimentary deposits in ancient lake basins (including Jezero crater, where the Perseverance rover is currently exploring) {cite:p}`Wordsworth2016`.

```{figure} figures/mars_valley_networks.avif
:name: fig:mars-valleys
:width: 600px
:align: center

Perspective view of an ancient valley network in the Noachian highlands of Mars, derived from the *Mars Express* High Resolution Stereo Camera (HRSC) digital terrain model.
The dendritic, river-like channel pattern requires sustained surface runoff and is incompatible with the present-day Mars climate, where mean surface temperature is $\sim$215 K and surface pressure is below the triple point of water.
Such networks are among the strongest geological constraints on the warm-wet Noachian climate problem discussed by {cite:t}`Wordsworth2016`.
Credit: ESA / DLR / FU Berlin (G. Neukum), CC BY-SA 3.0 IGO.
```

A dense $\mathrm{CO_2}$ atmosphere alone struggles to explain warm conditions on early Mars: $\mathrm{CO_2}$ condenses into ice clouds at the high pressures required, which can actually *cool* the planet by increasing the albedo. Reducing greenhouse gases ($\mathrm{H_2}$, $\mathrm{CH_4}$) produced by volcanism and water-rock reactions have been proposed as additional warming agents. The early Mars climate remains one of the major unsolved problems in planetary science.

### Climate feedbacks

The stability of a planet's climate depends on **feedback mechanisms**, processes where a change in temperature triggers secondary effects that either amplify (positive feedback) or counteract (negative feedback) the original change:

- **Ice-albedo feedback** (positive): If the planet cools, ice and snow expand $\Rightarrow$ the surface becomes more reflective (higher albedo) $\Rightarrow$ less sunlight is absorbed $\Rightarrow$ further cooling. Pushed far enough, this feedback can lock a planet into a globally frozen **snowball state**, as may have happened on Earth during the Neoproterozoic. The energy balance behind this behaviour is set out below.

- **Water vapour feedback** (positive): If the planet warms, more water evaporates $\Rightarrow$ $\mathrm{H_2O}$ is a strong greenhouse gas $\Rightarrow$ enhanced warming $\Rightarrow$ more evaporation. This feedback is the largest positive feedback in Earth's climate system: without any feedbacks, doubling $\mathrm{CO_2}$ would warm Earth by only $\sim$1.2 K, while the IPCC AR6 best estimate of the equilibrium warming, with the water vapour, lapse-rate, cloud, and albedo feedbacks included, is $\sim 3$ K {cite:p}`IPCC2021`. If it runs away (as may have happened on Venus), it leads to the **runaway greenhouse effect**, where the oceans completely evaporate (discussed in detail in {ref}`Lecture 9 <lecture09>`).

- **Cloud feedback** (complex): Low-altitude clouds reflect sunlight (cooling), while high-altitude cirrus clouds trap infrared radiation (warming). The net cloud feedback is the largest source of uncertainty in Earth climate models and is one of the key unknowns for exoplanet climate predictions ({ref}`Lecture 13 <lecture13>`).

#### Snowball Earth and climate bistability

The ice-albedo feedback is the clearest case of how a single feedback can give a planet more than one stable climate. Taken to its extreme it produces a **snowball Earth**, a state in which ice and snow cover almost the whole surface, from the poles to the equator ({numref}`fig:snowball-earth`). The evidence is geological: glacial deposits laid down at tropical latitudes show that Earth entered such states around 717 and 635 Ma {cite:p}`Hoffman1998,Hoffman2017`.

```{figure} figures/snowball_earth.avif
:name: fig:snowball-earth
:width: 560px
:align: center

Artist's impression of a fully ice-covered "snowball" Earth, with the continents buried under ice and only faint outlines showing through. A bright frozen surface reflects most of the incoming sunlight, which is what makes the snowball state so stable.
Credit: Oleg Kuznetsov (3depix.com), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```

A planet's surface temperature settles where the sunlight it absorbs equals the thermal radiation it emits to space. {numref}`fig:snowball-bistability` plots both terms against surface temperature $T$, and the two behave very differently. The emitted radiation (red) follows the grey-body law $\varepsilon \sigma T^4$ and rises smoothly and steeply with temperature, because a warmer surface always radiates more. The absorbed sunlight (blue) is $(1 - \alpha(T))\,S/4$, where $S$ is the stellar flux and $\alpha(T)$ the planetary albedo, so its temperature dependence enters only through the albedo. That albedo is not fixed: a frozen surface is bright ($\alpha \approx 0.6$), an ice-free surface dark ($\alpha \approx 0.3$). As the planet warms through the freezing range and its ice retreats, the albedo falls, so the blue curve climbs steeply across a narrow band of temperature and is nearly flat on either side of it.

```{figure} figures/snowball_bistability.avif
:name: fig:snowball-bistability
:width: 580px
:align: center

Energy-balance illustration of the ice-albedo feedback and snowball bistability.
The red curve is the outgoing longwave radiation $\varepsilon \sigma T^4$ with a fixed grey emissivity $\varepsilon = 0.62$ (a constant greenhouse), and the blue curve is the absorbed solar flux $(1 - \alpha(T))\,S/4$ with a temperature-dependent albedo that drops from $\sim$0.6 (ice-covered) to $\sim$0.3 (ice-free) across the freezing region.
Three energy-balance equilibria exist: a stable cold *snowball* state (left intersection), an unstable deglaciation threshold (middle), and a stable warm state (right).
Pushing the system across the unstable middle point triggers a runaway transition.
The snowball events of the Neoproterozoic ($\sim$717 and $\sim$635 Ma) are interpreted as global excursions of this bifurcation diagram {cite:p}`Hoffman1998,Hoffman2017`.
```

Wherever the two curves cross, absorbed and emitted power balance, so each crossing is an equilibrium. For the values shown they cross three times. Their stability follows from a simple slope test. At the cold ($\sim$250 K) and warm ($\sim$287 K) crossings the radiation curve is the steeper of the two, so a small warming radiates away more energy than it gains and the planet slides back to the crossing; a small cooling is undone the same way. Both are **stable** climates. The middle crossing ($\sim$267 K) is different: there the absorbed-sunlight curve is steeper, so a small warming absorbs more than it emits and the planet keeps warming, while a small cooling runs away downward. This state is an **unstable** deglaciation threshold, and no planet can rest on it.

Two stable climates for the same stellar flux is a **bistability**. Which one a planet occupies then depends on its history, not on the sunlight alone. Cool a warm world past the middle threshold, by a fall in greenhouse gases or in stellar flux, and it drops onto the snowball branch; climbing back out means crossing the threshold again from the cold side. Escape is hard. The bright frozen surface reflects most of the incoming sunlight, so only a large greenhouse forcing can lift the blue curve far enough to erase the cold crossing. On Earth that forcing builds up as volcanic $\mathrm{CO_2}$ accumulates in an atmosphere where the ice cover has shut down the silicate weathering that normally removes it, the negative feedback described in the next section.


## The carbonate-silicate cycle

Earth has maintained liquid water at its surface for at least 4.4 billion years despite a 30% increase in solar luminosity. This remarkable stability requires a powerful **negative feedback** mechanism: the **carbonate-silicate cycle**, first described by {cite:p}`Walker1981`.

### The Urey reaction

The cycle is built on the chemical weathering of silicate rocks by atmospheric $\mathrm{CO_2}$ dissolved in rainwater. The overall reaction (simplified) is:

$$
\mathrm{CaSiO_3} + \mathrm{CO_2} + \mathrm{H_2O} \longrightarrow \mathrm{CaCO_3} + \mathrm{SiO_2} + \mathrm{H_2O}
$$

This is sometimes called the **Urey reaction**. In words: carbon dioxide from the atmosphere dissolves in rainwater to form a weak acid, which reacts with silicate minerals in surface rocks. The products (calcium carbonate, $\mathrm{CaCO_3}$, limestone; and silica, $\mathrm{SiO_2}$) are transported by rivers to the ocean, where the carbonate precipitates, that is, comes out of solution as solid grains (biologically, as the shells and skeletons of marine organisms, or abiotically), and is deposited on the ocean floor as sedimentary rock.

The net effect is to **draw $\mathrm{CO_2}$ out of the atmosphere** and lock it into carbonate rocks. This is the long-term carbon *sink*.

### Volcanic outgassing: the carbon source

The cycle is closed by **plate tectonics**. Carbonate-bearing ocean floor is subducted into the mantle, where high temperatures and pressures decompose the carbonates, releasing $\mathrm{CO_2}$. This $\mathrm{CO_2}$ is returned to the atmosphere through **volcanic outgassing**, the long-term carbon *source*.

### The negative feedback

The weathering rate depends strongly on temperature through an **Arrhenius-type dependence**: chemical reactions proceed faster at higher temperatures. Additionally, a warmer climate produces more rainfall (more water evaporates from the oceans), which further accelerates weathering. This creates a powerful **negative feedback loop** {cite:p}`Walker1981`:

1. **If the planet warms** (e.g., due to increasing solar luminosity or volcanic outgassing): more rainfall + faster chemical reactions → **weathering rate increases** → more $\mathrm{CO_2}$ is drawn out of the atmosphere → greenhouse weakens → planet **cools back down**.

2. **If the planet cools** (e.g., due to reduced volcanic activity or orbital changes): less rainfall + slower reactions → **weathering rate decreases** → $\mathrm{CO_2}$ from volcanism accumulates in the atmosphere → greenhouse strengthens → planet **warms back up**.

This thermostat operates on geological timescales of $\sim 10^5$-$10^6$ yr, long by human standards but short compared to geological time. It is the primary reason Earth has maintained habitable surface temperatures for over 4 billion years despite the 30% increase in solar luminosity. The geologic cycle as a whole is summarised in {numref}`fig:carbonate-silicate-cycle`, and the modern plate-tectonic version of the cycle from {cite:p}`Foley2024` is shown in {numref}`fig:walker-loop`.

```{figure} figures/carbonate_silicate_cycle.avif
:name: fig:carbonate-silicate-cycle
:width: 500px
:align: center

The carbonate-silicate cycle, Earth's long-term climate thermostat. **Top:** The geologic cycle: atmospheric $\mathrm{CO_2}$ dissolves in rainwater and weathers silicate rocks, producing carbonates that are transported to the ocean and deposited as sediments. Subduction and volcanism return the $\mathrm{CO_2}$ to the atmosphere, closing the cycle. **Bottom:** The feedback loops: surface temperature, rainfall, silicate weathering rate, atmospheric $\mathrm{CO_2}$, and the greenhouse effect are linked in a negative feedback that stabilises the climate over geological timescales. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```

```{figure} figures/foley2024_carbonate_silicate.avif
:name: fig:walker-loop
:width: 700px
:align: center

Schematic diagram of the carbonate-silicate cycle as it operates on the modern-day, plate-tectonic Earth. CO$_2$ released from the mantle by arc, ridge, and plume volcanism enters the atmosphere; silicate weathering and carbonate precipitation transfer carbon from the atmosphere to the crust; hydrothermal alteration of seafloor basalts (seafloor weathering) is a secondary sink; subduction returns carbon to the mantle. Negative feedback: higher temperature accelerates weathering, drains atmospheric CO$_2$, cools the climate. The loop fails on Venus (no liquid water) and on Mars (no active subduction), as discussed below. Reproduced from {cite:p}`Foley2024`, Fig. 6.
```

### Venus and Mars: failed thermostats

The carbonate-silicate cycle requires two essential ingredients: **liquid water** (to dissolve $\mathrm{CO_2}$ and weather rocks) and **active volcanism** (to recycle carbon). Without either, the thermostat fails:

- **Venus:** Once Venus lost its surface water (likely through the runaway greenhouse and subsequent hydrogen escape to space), silicate weathering ceased. Without a carbon sink, volcanic $\mathrm{CO_2}$ accumulated in the atmosphere to the present 92 bar: a catastrophic demonstration of what happens when the thermostat breaks. We will explore Venus's climate history in detail in {ref}`Lecture 9 <lecture09>`.

- **Mars:** Mars's interior cooled and volcanism largely ceased by the end of the Hesperian ($\sim$3 Ga). Without a volcanic $\mathrm{CO_2}$ source, the remaining atmospheric $\mathrm{CO_2}$ was gradually drawn down by weathering and possibly lost to space, leaving the thin 6 mbar atmosphere we see today. We will discuss Mars's atmospheric evolution in {ref}`Lecture 10 <lecture10>`.

The requirement for both liquid water and active volcanism to maintain the carbonate-silicate cycle has profound implications for **planetary habitability**: a planet needs both the right temperature and the right geological activity to sustain that temperature over billions of years. This theme will return in {ref}`Lecture 14 <lecture14>` when we discuss the habitability of exoplanets.


## Recent advances

In 2020, a team reported a tentative detection of phosphine ($\mathrm{PH_3}$) in the cloud decks of Venus using millimetre-wavelength spectroscopy {cite:p}`Greaves2021`, sparking intense debate about possible biological or unknown chemical sources. Independent reanalyses contested the detection, showing among other things that mesospheric $\mathrm{SO_2}$ can reproduce the observed spectral feature, and it remains controversial {cite:p}`Lincowski2021`. Regardless of the outcome, the episode highlighted how little we understand about Venus's atmospheric chemistry and motivated renewed interest in Venus exploration. ESA's **EnVision** orbiter and NASA's **DAVINCI** probe (both selected for launch in the early 2030s) will provide new measurements of Venus's atmospheric composition and surface-atmosphere interactions.

NASA's **Dragonfly** mission, a nuclear-powered rotorcraft scheduled for launch in 2028, will explore Titan's surface and lower atmosphere in unprecedented detail. Dragonfly will sample the organic-rich dunes and investigate the products of Titan's atmospheric photochemistry at the surface, testing whether the combination of complex organics and transient liquid water (from impact melts or **cryovolcanism**, the eruption of water or other volatiles rather than molten rock) could drive **prebiotic chemistry**, reactions that build the organic precursors of life, without life being present ({ref}`Lecture 14 <lecture14>`).

Updated three-dimensional climate models for early Mars continue to challenge the "warm and wet" hypothesis, suggesting that episodic warming from impacts, volcanism, or atmospheric $\mathrm{H_2}$ greenhouse effects may be needed to explain the geological evidence for liquid water on early Mars ({ref}`Lecture 10 <lecture10>`). The interplay between atmospheric composition, climate feedbacks, and surface geology remains an active area of research.


## Looking ahead to Lecture 7

The last three lectures treated planets from the top down: energy budgets, vertical structure, and now clouds, winds, and climate. {ref}`Lecture 7 <lecture07>` moves to the solid surfaces these atmospheres act upon. Impact cratering provides the clocks by which planetary surfaces are dated, volcanism and tectonics resurface them from within, and erosion and weathering, driven by the winds, rain, and chemistry of this lecture, rework them from above. The climate history written into Mars's valley networks returns there as a geological record to be read.


## References

```{bibliography}
:filter: docname in docnames
```
