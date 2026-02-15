(lecture06)=
# Lecture 6: Atmospheres II — Clouds, Weather, & Climate

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to derive the Clausius-Clapeyron equation and apply it to predict cloud formation conditions, explain atmospheric circulation patterns using the Coriolis effect and geostrophic balance, describe weather phenomena across the solar system, and discuss long-term climate evolution including the faint young Sun paradox and the carbonate-silicate cycle.
```

## Cloud formation

In {ref}`lecture05`, we studied the vertical structure of atmospheres — how pressure and temperature vary with altitude, and how radiation and convection control the energy balance. We now turn to what happens when the air becomes *too cold* to hold all of its vapour: **clouds** form.

### Saturation and condensation

Every gas has a maximum amount of vapour that the surrounding air can hold at a given temperature. This maximum is set by the **saturation vapour pressure** $P_{\mathrm{sat}}(T)$ — the partial pressure at which the rate of evaporation from a liquid (or solid) surface equals the rate of condensation back onto it. When the actual partial pressure of a vapour exceeds $P_{\mathrm{sat}}$, the air is **supersaturated** and condensation is thermodynamically favoured {cite:p}`Pierrehumbert2010`.

The key property of $P_{\mathrm{sat}}(T)$ is its strong temperature dependence: it increases roughly exponentially with temperature. A parcel of air that is unsaturated at the warm surface can become saturated simply by cooling — for example, by rising and expanding adiabatically. The temperature at which a parcel first reaches saturation is called the **dew point** (for condensation to liquid) or the **frost point** (for deposition to ice).

The **relative humidity** is defined as the ratio of the actual vapour pressure to the saturation vapour pressure:

$$
\mathrm{RH} = \frac{P_{\mathrm{vapour}}}{P_{\mathrm{sat}}(T)} \times 100\%
$$

When $\mathrm{RH} = 100\%$, the air is saturated; when $\mathrm{RH} > 100\%$, it is supersaturated and condensation can occur.

### Nucleation

Even when air is supersaturated, condensation does not happen instantly. Forming a new droplet requires overcoming an energy barrier — the surface energy of the tiny embryonic droplet. This process is called **nucleation** {cite:p}`Catling2017`.

- **Homogeneous nucleation** — forming droplets from vapour alone, without any pre-existing surface — requires very high supersaturations (RH $\gg$ 100%) and is extremely rare in planetary atmospheres.
- **Heterogeneous nucleation** — condensation onto pre-existing particles called **condensation nuclei** (dust grains, volcanic aerosols, sea salt, soot, cosmic ray ions) — occurs at much lower supersaturations (RH $\gtrsim$ 100%) and is the dominant cloud formation mechanism on all planets.

The availability of condensation nuclei therefore controls where and how easily clouds form. On Earth, the oceans and biosphere provide abundant nuclei. On Mars, wind-lofted mineral dust serves the same role. On the giant planets, photochemical hazes produced in the upper atmosphere provide nuclei for cloud formation deeper down.

### The lifting condensation level

As an air parcel rises through the troposphere, it cools at the dry adiabatic lapse rate $\Gamma_d = g/c_p$ (Eq. {eq}`eq:dry-adiabat` from {ref}`lecture05`). Its vapour pressure remains roughly constant (since the mass of vapour is conserved during adiabatic ascent), but $P_{\mathrm{sat}}(T)$ decreases as the temperature drops. At the altitude where the parcel temperature has cooled enough that $P_{\mathrm{vapour}} = P_{\mathrm{sat}}(T)$, condensation begins. This altitude is the **lifting condensation level (LCL)** and marks the cloud base.

Above the LCL, the rising parcel releases **latent heat** as vapour condenses, warming the parcel relative to the dry adiabat. This gives the **moist adiabatic lapse rate**, which is shallower (typically $\sim$5–6 K km$^{-1}$ on Earth) than the dry adiabat ($\sim$9.8 K km$^{-1}$). The latent heat release also provides buoyancy, driving vigorous convection in moist atmospheres — the mechanism behind thunderstorms, hurricanes, and the towering cumulonimbus clouds on Earth.

### Cloud types depend on the condensing species

What condenses depends on what vapour is present and at what temperature. This varies dramatically across the solar system:

- **Earth:** $\mathrm{H_2O}$ clouds (liquid droplets and ice crystals), with cloud base at $\sim$1–2 km
- **Venus:** $\mathrm{H_2SO_4}$ (sulfuric acid) droplets at 48–70 km altitude
- **Mars:** $\mathrm{CO_2}$ ice and $\mathrm{H_2O}$ ice clouds at high altitude
- **Titan:** $\mathrm{CH_4}$ and $\mathrm{C_2H_6}$ (ethane) clouds near the surface
- **Jupiter/Saturn:** Layered $\mathrm{NH_3}$, $\mathrm{NH_4SH}$, and $\mathrm{H_2O}$ clouds at successively deeper levels

The physics of cloud formation is the same in every case — the Clausius-Clapeyron equation governs all of them. The difference is which species condenses and at what temperature.


## Blackboard derivation: The Clausius-Clapeyron equation

```{admonition} Blackboard derivation: The Clausius-Clapeyron equation
:class: tip

**Goal:** Derive the exponential dependence of saturation vapour pressure on temperature from thermodynamic phase equilibrium, and apply the result to predict cloud condensation conditions across the solar system.

**Setup: phase equilibrium.**

Consider a substance (e.g., water) that exists in two phases: liquid and vapour. Along the **coexistence curve** in the $P$–$T$ diagram — the line separating the liquid and vapour phases — the two phases are in thermodynamic equilibrium. This means the **Gibbs free energy per unit mass** is equal in both phases:

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
$$ (eq:clausius-clapeyron-diff)

This is a separable ODE: $\dd P / P = (L_v / R_v) \, \dd T / T^2$. Integrating from a reference state $(T_{\mathrm{ref}}, P_{\mathrm{ref}})$ to $(T, P_{\mathrm{sat}})$, and assuming $L_v$ is approximately constant:

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
P_{\mathrm{sat}} = 611 \exp\!\left[-5400\left(\frac{1}{293} - \frac{1}{273}\right)\right] = 611 \exp(1.35) \approx 611 \times 3.86 \approx 2360 \text{ Pa} \approx 2.4 \text{ kPa}
$$

The measured value is 2.3 kPa — excellent agreement. The small discrepancy arises because $L_v$ decreases slightly with temperature (from $2.50 \times 10^6$ J kg$^{-1}$ at 0°C to $2.26 \times 10^6$ J kg$^{-1}$ at 100°C), which we neglected by treating $L_v$ as constant.

**Application: condensing species across the solar system.**

The Clausius-Clapeyron equation applies to *any* vapour-to-liquid (or vapour-to-solid) transition. The following table lists the key condensing species in solar system atmospheres and their thermodynamic properties:

| Species | $L_v$ (kJ kg$^{-1}$) | $R_v$ (J kg$^{-1}$ K$^{-1}$) | $L_v/R_v$ (K) | $T_{\mathrm{cond}}$ (K)$^*$ | Where it condenses |
|---------|:-----:|:-----:|:-----:|:-----:|------|
| $\mathrm{H_2O}$ | 2500 | 462 | 5400 | 200–280 | Earth, Mars |
| $\mathrm{H_2SO_4}$ | 540 | 85 | 6400 | 340–380 | Venus |
| $\mathrm{NH_3}$ | 1370 | 488 | 2800 | 130–150 | Jupiter, Saturn |
| $\mathrm{CH_4}$ | 510 | 519 | 980 | 80–90 | Titan, Uranus, Neptune |
| $\mathrm{CO_2}$ | 571$^\dagger$ | 189 | 3020 | 145–175 | Mars |

$^*$Approximate condensation temperature at the pressure levels found in each planet's atmosphere.
$^\dagger$Latent heat of sublimation (solid $\leftrightarrow$ vapour).

Data from {cite:p}`Catling2017` and {cite:p}`dePaterLissauer2010`.

The large $L_v/R_v$ ratio for $\mathrm{H_2SO_4}$ explains why Venus's sulfuric acid clouds occupy a relatively narrow altitude range — the exponential sensitivity confines condensation to a thin temperature band. Conversely, $\mathrm{CH_4}$ has a low $L_v/R_v$, meaning its saturation curve is flatter and methane clouds on Titan can extend over a wider altitude range.
```


## Clouds across the solar system

Every planet and moon with a substantial atmosphere has clouds — but the condensing species and the cloud structure vary enormously. Here we survey the major cloud systems in our solar system {cite:p}`SanchezLavega2011`.

### Venus: sulfuric acid clouds

Venus is permanently shrouded in thick clouds that completely obscure the surface at visible wavelengths. These clouds are composed of $\mathrm{H_2SO_4}$ (sulfuric acid) droplets and extend from $\sim$48 km to $\sim$70 km altitude, spanning a temperature range of roughly 350–230 K {cite:p}`Catling2017`.

The sulfuric acid is produced by **photochemistry** in the upper atmosphere:

$$
\mathrm{SO_2} + \mathrm{H_2O} \xrightarrow{h\nu} \mathrm{H_2SO_4}
$$

where $\mathrm{SO_2}$ is supplied by volcanic outgassing. Below the main cloud deck lies a diffuse sub-cloud haze extending down to $\sim$30 km. An unidentified **UV absorber** in the upper clouds absorbs roughly half the solar UV flux and creates the distinctive banded patterns visible in ultraviolet images.

```{figure} figures/venus_uv_clouds.avif
:name: fig:venus-uv-clouds
:width: 400px
:align: center

Venus imaged by the *Mariner 10* spacecraft in February 1974, using a false-colour composite of orange and ultraviolet filters to reveal the banded cloud structure driven by atmospheric super-rotation. The $\mathrm{H_2SO_4}$ cloud deck extends from $\sim$48 to $\sim$70 km altitude and completely obscures the surface. Credit: NASA/JPL-Caltech, public domain.
```

### Mars: dust and ice clouds

Mars's thin atmosphere ($\sim$6 mbar surface pressure) supports two types of clouds:

- **$\mathrm{CO_2}$ ice clouds** form at high altitudes ($\sim$50–100 km) where temperatures drop below the frost point of $\mathrm{CO_2}$ ($\sim$148 K at 6 mbar). These are thin, wispy clouds, sometimes called "mesospheric" clouds.
- **$\mathrm{H_2O}$ ice clouds** form at lower altitudes ($\sim$10–30 km), particularly over the Tharsis volcanic region and in the aphelion cloud belt near the equator during northern summer.

**Mineral dust** plays a central role in Martian atmospheric physics: wind-lofted dust particles serve as condensation nuclei for ice clouds, and dust itself is a powerful radiative agent — absorbing solar radiation and heating the atmosphere, which can trigger positive feedback loops leading to global dust storms (see [weather and storms](weather-storms) below).

### Titan: methane rain

Saturn's moon Titan hosts the only known active **hydrological cycle** beyond Earth — but with $\mathrm{CH_4}$ (methane) playing the role of water. Titan's surface temperature ($\sim$94 K) and pressure ($\sim$1.5 bar) place it near the triple point of methane, enabling liquid methane on the surface (lakes and seas), methane clouds in the troposphere, and methane rain {cite:p}`dePaterLissauer2010`.

Titan's clouds are mostly $\mathrm{CH_4}$ (condensing at $\sim$8–30 km altitude) with some $\mathrm{C_2H_6}$ (ethane). Unlike Earth's water cycle, which is driven by solar evaporation, Titan's methane cycle is sluggish — rainfall is infrequent but intense when it occurs, creating transient rivers and channels carved into the icy surface. The Cassini–Huygens mission observed clouds forming preferentially at Titan's south pole (then in summer), with seasonal shifts as Titan orbits Saturn.

### Giant planets: layered cloud structure

The hydrogen-dominated atmospheres of Jupiter and Saturn host a **vertically layered** cloud structure, predicted by the Clausius-Clapeyron equation applied to each condensing species at the temperature and pressure where it reaches saturation {cite:p}`Showman2020`:

1. **$\mathrm{NH_3}$ ice** (topmost layer): condensing at $T \sim 130$–150 K, $P \sim 0.5$–1 bar. These are the clouds we see in visible light — the white and coloured bands of Jupiter.
2. **$\mathrm{NH_4SH}$** (ammonium hydrosulfide): condensing at $T \sim 200$–240 K, $P \sim 2$–3 bar. Formed by the reaction $\mathrm{NH_3} + \mathrm{H_2S} \to \mathrm{NH_4SH}$.
3. **$\mathrm{H_2O}$ ice and liquid** (deepest layer): condensing at $T \sim 270$–300 K, $P \sim 5$–7 bar. These deep water clouds are difficult to observe directly but are thought to play a critical role in powering Jupiter's weather through latent heat release.

```{figure} figures/jupiter_cloud_layers.avif
:name: fig:jupiter-cloud-layers
:width: 450px
:align: center

Temperature–pressure profile of Jupiter's atmosphere, showing the three main cloud layers: ammonia ($\mathrm{NH_3}$) ice at the top ($\sim$1 bar), ammonium hydrosulfide ($\mathrm{NH_4SH}$) in the middle ($\sim$2–3 bar), and water ($\mathrm{H_2O}$) at the deepest level ($\sim$5–7 bar). The tropopause at $\sim$50 km and the stratosphere–thermosphere boundary at $\sim$320 km are marked. Each cloud layer forms where the local temperature crosses the saturation curve for that species. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

The ice giants **Uranus** and **Neptune** have a different cloud hierarchy reflecting their colder temperatures and distinct compositions: $\mathrm{CH_4}$ ice forms the uppermost visible cloud layer ($T \sim 80$ K), with $\mathrm{H_2S}$ below it, and deeper $\mathrm{NH_4SH}$ and $\mathrm{H_2O}$ layers.


## Atmospheric dynamics

Atmospheres are not static — they are vast heat engines driven by uneven heating. The equator receives more solar energy per unit area than the poles, creating a temperature gradient that drives global-scale circulation patterns. How the atmosphere redistributes this heat depends on the planet's rotation rate, size, and atmospheric properties {cite:p}`SanchezLavega2011`.

### The Hadley cell

The simplest atmospheric circulation pattern, first described by George Hadley in 1735, works as follows:

1. Intense solar heating at the equator warms the surface and the air above it.
2. Warm, buoyant air **rises** at the equator, creating a low-pressure zone (the *Intertropical Convergence Zone*, ITCZ).
3. At altitude, the air flows **poleward** (toward higher latitudes).
4. As it moves poleward, it cools radiatively, becomes denser, and **sinks** at $\sim$30° latitude (the subtropics), creating high-pressure zones (where Earth's great deserts are located).
5. At the surface, air flows back toward the equator to replace the rising air — these return flows are the **trade winds**.

This loop is the **Hadley cell**. It is the dominant circulation pattern in the tropics on Earth and the primary mechanism for transporting heat from the equator toward the poles.

```{figure} figures/hadley_cells.svg
:name: fig:hadley-cells
:width: 500px
:align: center

Schematic of Earth's atmospheric circulation, showing the three-cell structure in each hemisphere: the Hadley cell (equator to $\sim$30°), the Ferrel cell ($\sim$30° to $\sim$60°), and the polar cell ($\sim$60° to the pole). The trade winds, westerlies, and polar easterlies are the surface manifestations of these circulation cells. The Coriolis effect deflects the winds to the right in the Northern Hemisphere and to the left in the Southern Hemisphere. Credit: Wikimedia Commons, public domain.
```

### The Coriolis effect

On a rotating planet, air that moves in a straight line (as seen from an inertial frame) appears to be **deflected** as seen from the rotating surface. This apparent deflection is the **Coriolis effect**: moving air is deflected to the *right* in the Northern Hemisphere and to the *left* in the Southern Hemisphere.

The magnitude of the Coriolis acceleration depends on the planet's angular rotation rate $\Omega$ and the latitude $\phi$ through the **Coriolis parameter**:

$$
f = 2\Omega \sin\phi
$$ (eq:coriolis-parameter)

For Earth, $\Omega = 7.27 \times 10^{-5}$ rad s$^{-1}$. At mid-latitudes ($\phi = 45°$), $f \approx 1.03 \times 10^{-4}$ s$^{-1}$. At the equator ($\phi = 0°$), $f = 0$ — the Coriolis effect vanishes.

### The Rossby number

Whether rotation significantly influences a particular atmospheric flow depends on the **Rossby number**, which compares the inertial acceleration to the Coriolis acceleration:

$$
\mathrm{Ro} = \frac{U}{f L}
$$ (eq:rossby-number)

where $U$ is the characteristic wind speed and $L$ is the characteristic horizontal length scale of the flow.

- $\mathrm{Ro} \ll 1$: Rotation dominates — the flow is strongly influenced by the Coriolis effect. This applies to large-scale atmospheric and oceanic circulation on Earth (e.g., $U \sim 10$ m s$^{-1}$, $L \sim 1000$ km → $\mathrm{Ro} \sim 0.1$).
- $\mathrm{Ro} \gg 1$: Rotation is unimportant — the flow is governed by pressure gradients and friction. This applies to small-scale phenomena like tornadoes and dust devils.

### Circulation cells and rotation rate

The number of circulation cells depends critically on the planet's rotation rate {cite:p}`Showman2020`:

- **Slowly rotating planets** (Venus, Titan): A single Hadley cell extends from equator to pole in each hemisphere. Venus has one giant Hadley cell per hemisphere despite being nearly the same size as Earth, because its slow rotation (243-day period) gives very small Coriolis forces ($\mathrm{Ro} \gg 1$ for large-scale flows).
- **Moderately rotating planets** (Earth): The Hadley cell extends to $\sim$30° latitude, where the Coriolis deflection becomes strong enough to break the cell. Two additional cells form at higher latitudes: the **Ferrel cell** (mid-latitudes, driven indirectly by the Hadley and polar cells) and the **polar cell**. Earth has three cells per hemisphere.
- **Rapidly rotating planets** (Jupiter, Saturn): Many alternating cells form, producing the characteristic **banded structure** of alternating light zones (rising air, high clouds) and dark belts (sinking air, deeper cloud exposure). Jupiter has $\sim$15 alternating jet streams per hemisphere.

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

In scalar form, the geostrophic wind components are:

$$
u_g = -\frac{1}{f\rho} \pdv{P}{y}, \qquad v_g = \frac{1}{f\rho} \pdv{P}{x}
$$

where $x$ and $y$ are the eastward and northward directions, respectively.

### Jet streams

**Jet streams** are narrow bands of fast-moving air ($\sim$30–70 m s$^{-1}$ on Earth) that form at the boundaries between circulation cells, where horizontal temperature gradients are strongest. Their existence is a direct consequence of the **thermal wind relation**, which connects vertical wind shear to horizontal temperature gradients:

$$
\pdv{\mathbf{v}_g}{z} \propto \hat{k} \times \nabla T
$$

Where the temperature gradient between the warm tropics and the cold poles is steepest (at $\sim$30° and $\sim$60° latitude on Earth), the wind speed increases with altitude, producing the subtropical and polar jet streams. These jet streams steer weather systems across the planet and are critical for understanding weather patterns.

### Giant planet banding

On Jupiter and Saturn, the same physics operates on a grander scale. The alternating light and dark bands — **zones** and **belts** — correspond to regions of rising and sinking air with alternating wind directions. Between adjacent bands, strong **zonal jets** (east–west winds) reach speeds of $\sim$150 m s$^{-1}$ on Jupiter and $\sim$400 m s$^{-1}$ on Saturn. The jets are remarkably stable over decades of observation and extend deep into the planetary interior, as revealed by Juno's gravity measurements {cite:p}`Showman2020`.


(weather-storms)=
## Weather and storms across the solar system

Planets and moons exhibit a stunning variety of weather phenomena, from gentle breezes to apocalyptic storms. Here we survey the highlights.

### Mars: dust storms and seasonal cycles

Mars experiences dramatic weather driven by its thin atmosphere and strong seasonal forcing. Two phenomena stand out {cite:p}`Catling2017`:

- **Dust storms:** Local dust storms are common, lofting mineral particles to $\sim$10–30 km altitude. Occasionally, these storms grow to engulf the entire planet in a **global dust storm**, reducing surface visibility to near zero for weeks. The most recent global dust storms occurred in 2018 and 2007. The feedback mechanism is straightforward: dust absorbs solar radiation → heats the atmosphere → drives stronger winds → lofts more dust — a positive feedback loop.

- **Seasonal $\mathrm{CO_2}$ cycle:** Mars's polar caps contain solid $\mathrm{CO_2}$ (dry ice). During winter, atmospheric $\mathrm{CO_2}$ freezes onto the polar cap; during summer, it sublimes back into the atmosphere. This exchange involves $\sim$25–30% of the total atmospheric mass, causing surface pressure to swing from $\sim$5 mbar (summer pole) to $\sim$7 mbar (winter pole) — a phenomenon with no analogue on Earth.

```{figure} figures/mars_dust_storm.avif
:name: fig:mars-dust-storm
:width: 550px
:align: center

Mars before and during the 2018 global dust storm, as imaged by the Mars Reconnaissance Orbiter. The left panel shows clear atmospheric conditions with surface features visible; the right panel shows the planet almost completely obscured by wind-lofted mineral dust. The storm ultimately ended the *Opportunity* rover's 15-year mission by blocking sunlight to its solar panels. Credit: NASA/JPL-Caltech/MSSS, public domain.
```

### Venus: super-rotation

Venus presents one of the great puzzles of atmospheric dynamics: its atmosphere **rotates 60 times faster** than the planet itself at cloud level. While Venus's surface rotates once every 243 Earth days (retrograde), the cloud-top winds circle the planet in just $\sim$4 days, reaching speeds of $\sim$100 m s$^{-1}$. This phenomenon is called **atmospheric super-rotation** {cite:p}`SanchezLavega2011`.

Super-rotation requires a mechanism to transport angular momentum from the slowly rotating surface *upward and equatorward* — against the usual sense of friction, which should slow the atmosphere down to match the surface. The leading explanation involves a combination of **thermal tides** (driven by solar heating of the cloud layer) and **planetary-scale waves** that pump angular momentum toward the equator. Despite decades of study, the detailed mechanism remains an active area of research.

### Jupiter: the Great Red Spot

Jupiter's **Great Red Spot (GRS)** is the largest and longest-lived storm in the solar system — an anticyclonic vortex larger than Earth, with winds reaching $\sim$120 m s$^{-1}$ at its periphery. It has been observed continuously for over 350 years (first recorded by Robert Hooke in 1664, though continuous observations date from 1830).

```{figure} figures/jupiter_great_red_spot.avif
:name: fig:jupiter-grs
:width: 500px
:align: center

Jupiter's Great Red Spot and surrounding turbulent atmosphere, imaged by NASA's *Juno* spacecraft during a close flyby. The Great Red Spot is an anticyclonic storm larger than Earth that has persisted for centuries. The surrounding vortices and chaotic cloud patterns reveal the intense turbulence of Jupiter's upper troposphere. Credit: NASA/JPL-Caltech/SwRI/MSSS, public domain.
```

The GRS sits between two zonal jets with opposite directions, which confine and sustain it. Its longevity is remarkable — on Earth, the largest hurricanes dissipate within days once they lose their energy source (warm ocean water). The GRS is sustained by absorbing smaller vortices and by latent heat released from $\mathrm{H_2O}$ condensation deep in the atmosphere. However, the GRS has been slowly shrinking over the past century, and its long-term fate remains uncertain {cite:p}`Showman2020`.

### Saturn: the hexagonal jet stream

Saturn's north pole hosts one of the most geometrically striking features in the solar system: a persistent **hexagonal jet stream** encircling the pole at $\sim$78°N latitude, first discovered by Voyager in 1981 and extensively imaged by Cassini.

```{figure} figures/saturn_hexagon.avif
:name: fig:saturn-hexagon
:width: 400px
:align: center

Saturn's hexagonal jet stream at the north pole, imaged by NASA's *Cassini* spacecraft in 2013. The hexagonal pattern is a stable Rossby wave with six-fold symmetry, maintained by the interaction between the polar jet stream and the surrounding atmosphere. The hexagon has a diameter of $\sim$30,000 km — larger than Earth's diameter. Credit: NASA/JPL-Caltech/SSI, public domain.
```

The hexagonal shape is explained as a stable **Rossby wave** — a large-scale atmospheric wave whose restoring force is the variation of the Coriolis parameter with latitude. When the jet stream speed and width satisfy certain resonance conditions, the wave locks into a pattern with a specific number of sides. Laboratory experiments with rotating fluids have reproduced hexagonal and other polygonal patterns under analogous conditions.

Saturn also experiences periodic **Great White Storms** roughly every 30 years (most recently in 2010), which are massive convective outbursts that encircle the planet within weeks — the Saturnian equivalent of a planet-wide thunderstorm.

### Neptune: extreme weather on a cold world

Despite receiving only $\sim$1/900th of Earth's solar flux, Neptune has the **fastest winds** in the solar system, reaching $\sim$580 m s$^{-1}$ ($\sim$2100 km h$^{-1}$). The Voyager 2 flyby in 1989 revealed a **Great Dark Spot** similar to Jupiter's GRS, though subsequent Hubble observations showed it had vanished — and new ones had formed, suggesting Neptune's storms are more transient than Jupiter's.

Neptune's vigorous weather is powered primarily by **internal heat**: Neptune radiates $\sim$2.6 times more energy than it receives from the Sun, driven by slow gravitational contraction and possibly differentiation in the interior ({ref}`lecture03`). This internal heat source drives convection and storms even in the near-absence of solar heating.


## Climate evolution and the faint young Sun

On timescales of billions of years, a planet's climate is not constant — it evolves in response to changes in the host star's luminosity, the atmospheric composition, and geological processes. The most celebrated example of this long-term evolution is the **faint young Sun paradox** {cite:p}`Feulner2012`.

### Solar luminosity evolution

The Sun, like all main-sequence stars, has been gradually brightening as hydrogen is converted to helium in the core. The increasing mean molecular weight requires higher core temperatures to maintain pressure support, which increases the nuclear reaction rate and hence the luminosity. A standard solar evolution model gives {cite:p}`Catling2017`:

$$
\frac{L(t)}{\Lsun} \approx \left[1 + \frac{2}{5}\left(1 - \frac{t}{t_\odot}\right)\right]^{-1}
$$ (eq:solar-luminosity-evolution)

where $t$ is the time since the Sun's formation and $t_\odot \approx 4.57$ Gyr is the present age of the Sun. At formation ($t = 0$):

$$
\frac{L(0)}{\Lsun} = \frac{1}{1.4} \approx 0.71
$$

The early Sun was **$\sim$30% less luminous** than today. Even 4 Gyr ago (when the first evidence for life on Earth appears), the Sun was still $\sim$25% fainter.

### The paradox

A 30% reduction in solar luminosity would reduce Earth's effective temperature from 255 K to:

$$
T_{\mathrm{eff}} = 255 \times (0.71)^{1/4} \approx 234 \text{ K}
$$

Combined with a greenhouse effect similar to today's, this would yield a surface temperature well below freezing — the entire ocean should have been **frozen solid**. Yet geological evidence tells a strikingly different story:

- **Zircon crystals** from 4.4 Ga show oxygen isotope ratios ($\delta^{18}\mathrm{O}$) consistent with liquid water interacting with rock at the surface.
- **Pillow basalts** (lava cooled underwater) and **sedimentary rocks** (requiring liquid water for transport and deposition) date back to at least 3.8 Ga.
- **Stromatolites** (microbial mat fossils) at 3.5 Ga and possible carbon isotope signatures of life at 3.8 Ga imply not just liquid water, but conditions warm enough for biology.

This contradiction — a faint Sun that should have frozen the Earth, versus geological evidence for liquid water — is the **faint young Sun paradox**, first articulated by Sagan & Mullen (1972).

### Possible solutions

Several mechanisms have been proposed to resolve the paradox {cite:p}`Feulner2012`:

- **Enhanced $\mathrm{CO_2}$ greenhouse:** If the early atmosphere contained 10–1000 times more $\mathrm{CO_2}$ than today (plausible, given that the carbonate-silicate cycle was less efficient before the emergence of land plants), the enhanced greenhouse warming could compensate for the weaker Sun.
- **Methane greenhouse:** Biogenic $\mathrm{CH_4}$ from early methanogens could have provided additional greenhouse warming. $\mathrm{CH_4}$ is a potent greenhouse gas, and in an anoxic (oxygen-free) early atmosphere, it would have had a much longer lifetime than today.
- **$\mathrm{N_2}$ pressure broadening:** A thicker $\mathrm{N_2}$ atmosphere (2–3 times present levels) would enhance greenhouse warming through pressure broadening of $\mathrm{CO_2}$ and $\mathrm{H_2O}$ absorption lines.
- **Lower albedo:** Without continents (less land area in the Archean) and potentially fewer clouds, the early Earth may have reflected less sunlight, absorbing more energy despite the lower luminosity.

The most likely resolution is a combination of elevated $\mathrm{CO_2}$ and $\mathrm{CH_4}$ concentrations, regulated by the carbonate-silicate cycle (next section).

### The Mars climate puzzle

Mars poses an even more extreme version of the same problem. At 1.52 AU, Mars receives less than half of Earth's solar flux — and with the faint young Sun, the situation is even worse. Yet Mars shows compelling geological evidence for warm, wet conditions during the **Noachian** period ($>$3.7 Ga): extensive valley networks carved by flowing water, clay minerals formed by aqueous weathering, and sedimentary deposits in ancient lake basins (including Jezero crater, where the Perseverance rover is currently exploring) {cite:p}`Wordsworth2022`.

A dense $\mathrm{CO_2}$ atmosphere alone struggles to explain warm conditions on early Mars — $\mathrm{CO_2}$ condenses into ice clouds at the high pressures required, which can actually *cool* the planet by increasing the albedo. Reducing greenhouse gases ($\mathrm{H_2}$, $\mathrm{CH_4}$) produced by volcanism and water-rock reactions have been proposed as additional warming agents. The early Mars climate remains one of the major unsolved problems in planetary science.

### Climate feedbacks

The stability of a planet's climate depends on **feedback mechanisms** — processes where a change in temperature triggers secondary effects that either amplify (positive feedback) or counteract (negative feedback) the original change:

- **Ice-albedo feedback** (positive): If the planet cools, ice sheets expand → the surface becomes more reflective (higher albedo) → less sunlight is absorbed → further cooling. This feedback can drive a planet into a **snowball state** if triggered strongly enough (as may have happened on Earth during the Neoproterozoic, $\sim$700 Ma).

- **Water vapour feedback** (positive): If the planet warms, more water evaporates → $\mathrm{H_2O}$ is a strong greenhouse gas → enhanced warming → more evaporation. This feedback approximately doubles the warming from $\mathrm{CO_2}$ alone on present-day Earth. If it runs away — which may have happened on Venus — it leads to the **runaway greenhouse effect**, where the oceans completely evaporate (discussed in detail in {ref}`lecture09`).

- **Cloud feedback** (complex): Low-altitude clouds reflect sunlight (cooling), while high-altitude cirrus clouds trap infrared radiation (warming). The net cloud feedback is the largest source of uncertainty in Earth climate models and is one of the key unknowns for exoplanet climate predictions ({ref}`lecture13`).


## The carbonate-silicate cycle

Earth has maintained liquid water at its surface for at least 4.4 billion years despite a 30% increase in solar luminosity. This remarkable stability requires a powerful **negative feedback** mechanism: the **carbonate-silicate cycle**, first described by {cite:p}`Walker1981`.

### The Urey reaction

The cycle is built on the chemical weathering of silicate rocks by atmospheric $\mathrm{CO_2}$ dissolved in rainwater. The overall reaction (simplified) is:

$$
\mathrm{CaSiO_3} + \mathrm{CO_2} + \mathrm{H_2O} \longrightarrow \mathrm{CaCO_3} + \mathrm{SiO_2} + \mathrm{H_2O}
$$

This is sometimes called the **Urey reaction**. In words: carbon dioxide from the atmosphere dissolves in rainwater to form a weak acid, which reacts with silicate minerals in surface rocks. The products — calcium carbonate ($\mathrm{CaCO_3}$, limestone) and silica ($\mathrm{SiO_2}$) — are transported by rivers to the ocean, where the carbonate precipitates (biologically or abiotically) and is deposited on the ocean floor as sedimentary rock.

The net effect is to **draw $\mathrm{CO_2}$ out of the atmosphere** and lock it into carbonate rocks. This is the long-term carbon *sink*.

### Volcanic outgassing: the carbon source

The cycle is closed by **plate tectonics**. Carbonate-bearing ocean floor is subducted into the mantle, where high temperatures and pressures decompose the carbonates, releasing $\mathrm{CO_2}$. This $\mathrm{CO_2}$ is returned to the atmosphere through **volcanic outgassing** — the long-term carbon *source*.

### The negative feedback

The weathering rate depends strongly on temperature through an **Arrhenius-type dependence**: chemical reactions proceed faster at higher temperatures. Additionally, a warmer climate produces more rainfall (more water evaporates from the oceans), which further accelerates weathering. This creates a powerful **negative feedback loop** {cite:p}`Walker1981`:

1. **If the planet warms** (e.g., due to increasing solar luminosity or volcanic outgassing): more rainfall + faster chemical reactions → **weathering rate increases** → more $\mathrm{CO_2}$ is drawn out of the atmosphere → greenhouse weakens → planet **cools back down**.

2. **If the planet cools** (e.g., due to reduced volcanic activity or orbital changes): less rainfall + slower reactions → **weathering rate decreases** → $\mathrm{CO_2}$ from volcanism accumulates in the atmosphere → greenhouse strengthens → planet **warms back up**.

This thermostat operates on a timescale of $\sim$0.5 Myr — long by human standards, but short compared to geological time. It is the primary reason Earth has maintained habitable surface temperatures for over 4 billion years despite the 30% increase in solar luminosity.

```{figure} figures/carbonate_silicate_cycle.avif
:name: fig:carbonate-silicate-cycle
:width: 500px
:align: center

The carbonate-silicate cycle — Earth's long-term climate thermostat. **Top:** The geologic cycle: atmospheric $\mathrm{CO_2}$ dissolves in rainwater and weathers silicate rocks, producing carbonates that are transported to the ocean and deposited as sediments. Subduction and volcanism return the $\mathrm{CO_2}$ to the atmosphere, closing the cycle. **Bottom:** The feedback loops: surface temperature, rainfall, silicate weathering rate, atmospheric $\mathrm{CO_2}$, and the greenhouse effect are linked in a negative feedback that stabilises the climate over geological timescales. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```

### Venus and Mars: failed thermostats

The carbonate-silicate cycle requires two essential ingredients: **liquid water** (to dissolve $\mathrm{CO_2}$ and weather rocks) and **active volcanism** (to recycle carbon). Without either, the thermostat fails:

- **Venus:** Once Venus lost its surface water (likely through the runaway greenhouse and subsequent hydrogen escape to space), silicate weathering ceased. Without a carbon sink, volcanic $\mathrm{CO_2}$ accumulated in the atmosphere to the present 92 bar — a catastrophic demonstration of what happens when the thermostat breaks. We will explore Venus's climate history in detail in {ref}`lecture09`.

- **Mars:** Mars's interior cooled and volcanism largely ceased by the end of the Hesperian ($\sim$3 Ga). Without a volcanic $\mathrm{CO_2}$ source, the remaining atmospheric $\mathrm{CO_2}$ was gradually drawn down by weathering and possibly lost to space, leaving the thin 6 mbar atmosphere we see today. We will discuss Mars's atmospheric evolution in {ref}`lecture10`.

The requirement for both liquid water and active volcanism to maintain the carbonate-silicate cycle has profound implications for **planetary habitability**: a planet needs not just the right temperature, but also the right geological activity to sustain that temperature over billions of years. This theme will return in {ref}`lecture14` when we discuss the habitability of exoplanets.


## Recent advances

In 2020, a team reported a tentative detection of phosphine ($\mathrm{PH_3}$) in the cloud decks of Venus using submillimetre spectroscopy, sparking intense debate about possible biological or unknown chemical sources. Subsequent reanalyses by independent groups found that the original signal was significantly weaker than first claimed, and the detection remains controversial. Regardless of the outcome, the episode highlighted how little we understand about Venus's atmospheric chemistry and motivated renewed interest in Venus exploration. ESA's **EnVision** orbiter and NASA's **DAVINCI** probe — both selected for launch in the early 2030s — will provide new measurements of Venus's atmospheric composition and surface–atmosphere interactions.

NASA's **Dragonfly** mission, a nuclear-powered rotorcraft scheduled for launch in 2028, will explore Titan's surface and lower atmosphere in unprecedented detail. Dragonfly will sample the organic-rich dunes and investigate the products of Titan's atmospheric photochemistry at the surface — testing whether the combination of complex organics and transient liquid water (from impact melts or cryovolcanism) could drive prebiotic chemistry ({ref}`lecture14`).

Updated three-dimensional climate models for early Mars continue to challenge the "warm and wet" hypothesis, suggesting that episodic warming from impacts, volcanism, or atmospheric $\mathrm{H_2}$ greenhouse effects may be needed to explain the geological evidence for liquid water on early Mars ({ref}`lecture10`). The interplay between atmospheric composition, climate feedbacks, and surface geology remains an active area of research.


## References

```{bibliography}
:filter: docname in docnames
```
