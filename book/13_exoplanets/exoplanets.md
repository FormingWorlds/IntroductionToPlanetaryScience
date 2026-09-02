(lecture13)=
# Exoplanets, Detection Methods, Demographics & Characterisation

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe the main exoplanet detection methods and their observational biases, interpret the period-radius diagram and its key features (radius valley, hot Neptune desert, peas-in-a-pod), apply the transit and radial velocity geometry to derive planetary mass, radius, and bulk density, and evaluate JWST-era atmospheric characterisation results and their implications for habitability and biosignatures.
```

```{seealso}
**Slides:** [Download Lecture 13 (PDF)](../_static/slides/lecture13.pdf)
```

In all the lectures so far we have studied a single planetary system in extraordinary detail.
We know its age, its eight planets, its hundreds of moons, its Kuiper belt, its formation history.
We do not yet know whether any of this is typical.
Lecture 13 finally turns the question outward.
We ask how planets are detected around other stars, what the resulting catalogue looks like, how it can be physically interpreted, and where the solar system sits in that picture.
The lecture follows the same descriptive-first, payoff-at-the-end structure as Lectures 9 to 12: detection methods first (Part 1), then demographics and architectures (Part 2), then atmospheric characterisation, habitability, and the comparative payoff (Part 3).

## Part 1: How we find exoplanets

### Historical context

The first confirmed planets outside the solar system were announced in 1992 by Aleksander Wolszczan and Dale Frail around the radio pulsar PSR B1257+12 {cite:p}`Wolszczan1992`.
A **pulsar** is a rapidly spinning, highly magnetised remnant of a massive star that has undergone a supernova explosion.
Because pulsar pulse arrival times rival atomic clocks in precision, planetary motion around the system **barycentre** (the shared centre of mass) produces periodic shifts in these arrival times.
The system contains two planets with minimum masses of about $3.4$ and $2.8\,\Mearth$ in $66$ and $98$ day orbits, plus a lunar-mass third body ($\sim 0.015\,\Mearth$) in a $25.34$ day orbit {cite:p}`Wolszczan1994`.
These post-supernova planets showed that planetary bodies can exist in environments far removed from the standard star and disk framework of {ref}`Lecture 2 <lecture02>`.

In 1995 Michel Mayor and Didier Queloz used the ELODIE spectrograph to detect 51 Pegasi b, the first confirmed planet orbiting a main-sequence star, earning the 2019 Nobel Prize in Physics {cite:p}`MayorQueloz1995`.
The planet has roughly half the mass of Jupiter on a 4.23-day orbit.
A gas giant so close to its star contradicted standard models where gas giants form beyond the ice line during **runaway accretion** (the rapid intake of surrounding nebular gas by a growing core) {cite:p}`Pollack1996`.
This discovery motivated the **planetary migration** interpretation, which won out over in-situ formation within a few years: planets form at large orbital distances and move inward through disk interactions ({ref}`Lecture 2 <lecture02>`).

```{figure} figures/hd209458b_first_transit.avif
:align: center
:name: fig:hd209458b
:width: 70%

The first ground-based detection of a transiting exoplanet, **HD 209458 b**, observed with the STARE photometer over two nights in September 1999. Each successive transit dropped the relative flux of the host star by approximately 1.7 per cent, exactly the depth predicted from the radial velocity mass and an inferred Jupiter-like radius. From {cite:t}`Charbonneau2000`; an independent simultaneous detection was reported by {cite:t}`Henry2000`. After this point exoplanets were no longer abstract Doppler signals: they were physical objects whose sizes could be measured directly.
```

In 1999 the first transit detection of HD 209458 b combined transit depth and radial velocity to determine the first planetary **bulk density** (total mass divided by volume) ({numref}`fig:hd209458b`).
This confirmed that **hot Jupiters** (Jupiter-mass planets on orbits of only a few days) are gas-dominated bodies rather than high-density objects.
Space-based transit surveys opened with CoRoT in 2006 and expanded with Kepler in 2009, which monitored about 150,000 stars over four years {cite:p}`Borucki2010`.
By 2026 the NASA Exoplanet Archive recorded more than 6000 confirmed exoplanets in more than 4500 planetary systems {cite:p}`NASAExoArchive2025`.

### Radial velocity method

A planet of mass $m_p$ and its host star of mass $M_\star$ orbit their common centre of mass, the **barycentre**.
The star's orbit has radius $a_\star = (m_p / M_\star)\,a_p$, spanning about one solar radius for a Jupiter analogue around a Sun-like star and less than a thousandth of a solar radius for an Earth analogue.
This stellar motion causes periodic Doppler shifts in stellar absorption lines, blueshifting as the star moves toward the observer and redshifting as it moves away.
The resulting line-of-sight velocity time series yields the orbital period $P$, eccentricity $e$, and semi-amplitude $K_\star$, the peak stellar reflex velocity.

For a Keplerian orbit of eccentricity $e$ and inclination $i$ the semi-amplitude takes the compact form

$$
K_\star = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{(M_\star + m_p)^{2/3}} \frac{1}{\sqrt{1 - e^2}},
$$

which is derived from Kepler's third law and conservation of momentum.
Around the Sun, a Jupiter analogue produces $K_\star \approx 12.5$ m/s, Saturn at $9.5$ AU produces $2.7$ m/s, and Earth at 1 AU produces $0.09$ m/s.
A true Earth twin lies at the detection limit of current instruments and well below what is achievable around any but the brightest, quietest stars.

Instrumental precision has improved by two orders of magnitude over three decades, from 10 m/s with ELODIE to 1 m/s with HARPS {cite:p}`Mayor2003` and 10 cm/s with ESPRESSO {cite:p}`Pepe2021`.
Precision is now limited by **stellar noise**, velocity jitter at the 10 cm/s to 1 m/s level caused by granulation, oscillations, and starspots on the host star.
Reducing this stellar jitter through activity diagnostics or long observing baselines is the central technical challenge in precision radial velocity work.

From $K_\star$, radial velocities constrain only $m_p \sin i$, where $i$ is the orbital inclination relative to the line of sight.
A face-on system ($i = 0$, $\sin i = 0$) produces no Doppler signal, while an edge-on system ($i = 90^\circ$, $\sin i = 1$) yields the true mass.
This ambiguity is the **$m \sin i$ degeneracy**, which prevents distinguishing a low-mass edge-on planet from a more massive inclined planet.
The degeneracy is broken when inclination is measured independently from transits (where $\sin i \approx 1$), astrometry, or direct imaging, converting the minimum mass into a true mass.

Radial velocity surveys are biased toward massive planets on short orbits around bright, slowly rotating, magnetically quiet stars.
Detecting small velocity signals requires observing over multiple orbital periods, requiring at least a decade of baseline for long-period Jupiter analogues.
**M dwarfs**, small, cool, low-mass stars, are challenging targets because they are faint at optical wavelengths with complex molecular features, while F dwarfs rotate rapidly with few sharp lines.
Surveys therefore achieve their strongest yields around quiet G and K main-sequence stars in the 5 to 10 parsec neighbourhood.

### Transit method

A **transit** occurs when an exoplanet passes in front of its host star, blocking a fraction of stellar light ({numref}`fig:transitgeom`).
The fractional flux drop for a planet of radius $R_p$ crossing a star of radius $R_\star$ is:

$$
\delta = \frac{\Delta F}{F} = \left(\frac{R_p}{R_\star}\right)^2.
$$

```{figure} figures/transit_geometry.avif
:align: center
:name: fig:transitgeom
:width: 90%

Geometry of a transit. **Left:** the orbit, viewed from above, defines a "shadow band" within which an observer sees transits. The half-angle of the band is $\Theta \approx (R_\star + R_p)/r$, where $r$ is the instantaneous star-planet distance. **Right:** detail of grazing and full transits relative to the stellar limb. The probability that a randomly oriented orbit produces a visible transit scales as $R_\star / a$. From the Winn (2010) review {cite:p}`Winn2010`.
```

For a Jupiter-radius planet around a Sun-like star, the transit depth is $\delta \approx 1\%$, measurable from the ground.
For an Earth-Sun analogue, $\delta \approx 8.4 \times 10^{-5}$ (84 parts per million), achievable only from space.
Around an M dwarf ($R_\star \approx 0.15\,\Rsun$), an Earth-radius planet yields $\delta \approx 4 \times 10^{-3}$ (4000 ppm), favouring M-dwarf systems for characterisation.

Four contact times ($t_\mathrm{I}$ through $t_\mathrm{IV}$) in the light curve ({numref}`fig:transitlc`) constrain the orbital inclination $i$, impact parameter $b$, and planetary radius.
The transit is also shaped by **limb darkening**, where the stellar limb appears dimmer because lines of sight probe cooler upper photospheric layers.

```{figure} figures/transit_lightcurve_schematic.avif
:align: center
:name: fig:transitlc
:width: 75%

Schematic of a transit light curve. The four contact times $t_\mathrm{I}$ through $t_\mathrm{IV}$ define the ingress, total duration, and egress. The depth $\delta = (R_p / R_\star)^2$ gives the planet's radius if the stellar radius is known; the duration and ingress shape constrain the impact parameter $b$ and the orbital geometry. The flat bottom assumes a uniform source; in practice the curved bottom of a real transit reveals limb darkening of the host star. From {cite:t}`Winn2010`.
```

An orbit transits only if aligned within an angle $\Theta \approx R_\star / a$ of our line of sight.
This probability is $\sim 0.005$ (one in 200) for an Earth-Sun analogue and $\sim 0.1$ (ten per cent) for a hot Jupiter at 0.05 AU, biasing detections toward short periods.
Space photometry reaches parts-per-million precision ({numref}`fig:wasp39_jwst`).

```{figure} figures/jwst_transit_lightcurve.avif
:align: center
:name: fig:wasp39_jwst
:width: 90%

Modern transit photometry pushed to its current limit, from Figure 1 of {cite:t}`Alderson2023`. Panel a is the raw, uncorrected broadband transit light curve of the hot Saturn **WASP-39 b** ($0.28\,\Mjup$) observed with the two JWST NIRSpec G395H detectors, NRS1 (purple) and NRS2 (red); normalised flux against time in days. The inset magnifies a drop in flux (grey band) caused by a tilt of a primary-mirror segment, which leaves the two detectors offset from each other for the rest of the observation. Panel b is the same data resolved by wavelength: each column is one spectroscopic light curve, with time on the vertical axis and normalised flux as the colour. The white stripe at $3.72$--$3.82$ $\mu$m is the gap between the two detectors. Panel c is the precision reached in each spectroscopic bin: black points and the left axis are the scatter of the light curve, between about $1100$ ppm near $3.2$ $\mu$m and about $3000$ ppm near $5.1$ $\mu$m, and the two grey dashed curves are one and two times the photon noise. Blue points and the right axis are the resulting precision on the transit depth, about $200$ ppm at the blue end and about $600$ ppm at the red end. The strongest transmission feature of WASP-39 b, the $\mathrm{CO_2}$ band near $4.3$ $\mu$m, is about $1300$ ppm deep ({numref}`fig:wasp39species`), so a single spectroscopic bin now resolves it.
```

Kepler monitored 150,000 stars to deliver the first statistical sample of small exoplanets {cite:p}`Borucki2010`.
TESS surveys bright nearby stars for atmospheric follow-up, while CHEOPS refines planet radii.
PLATO is designed to detect Earth-sized planets in the **habitable zones**, the orbital distances at which a rocky planet could plausibly sustain liquid surface water, of bright Sun-like stars {cite:p}`Rauer2014`.

## Blackboard derivation: Transit depth, radial velocity, and bulk density

````{admonition} Blackboard derivation: Transit depth, radial velocity, and bulk density
:class: tip

This derivation is the central conceptual payoff of the lecture.
Both the transit method and the radial velocity method have an obvious individual limitation: a transit alone gives a radius but not a mass, and a radial velocity alone gives only a minimum mass.
Combining the two breaks the degeneracy, gives both quantities for the same planet, and turns an exoplanet detection into a physical object whose internal composition can be discussed.
We work through this in three steps.

**Step 1: transit depth (~2 min).**
Treat the star as a uniformly bright disk of radius $R_\star$ and the planet as an opaque circular disk of radius $R_p$.
When the planet is fully in front of the star, the area blocked is $\pi R_p^2$ and the area of the star is $\pi R_\star^2$.
The fractional flux drop is therefore the ratio of areas:

$$
\frac{\Delta F}{F} = \frac{\pi R_p^2}{\pi R_\star^2} = \left(\frac{R_p}{R_\star}\right)^2.
$$

The depth is the directly measured observable.
If we know the stellar radius (typically from spectroscopy combined with stellar evolution models, or in the best cases from interferometric angular diameters and parallax distances), we immediately get the planet radius.
Limb darkening, ingress shape, and orbital eccentricity all introduce $\sim$10\% level corrections, but the leading-order picture is just the area ratio.

**Step 2: radial velocity semi-amplitude (~5 min).**
Now we attack the dynamical side.
The two bodies orbit their common centre of mass.
Let $a$ denote the relative (planet-to-star) semi-major axis, and let $a_\star$ and $a_p$ denote the distances of the star and planet from the barycentre, with $a = a_\star + a_p$.
Conservation of momentum at any instant requires

$$
M_\star a_\star = m_p a_p,
$$

so $a_\star = (m_p/(M_\star + m_p))\,a$ and $a_p = (M_\star/(M_\star + m_p))\,a$.
Both bodies move on circles (assuming a circular orbit) around the barycentre with the same orbital period $P$, and the orbital speed of the star is

$$
v_\star = \frac{2\pi a_\star}{P} = \frac{m_p}{M_\star + m_p} \cdot \frac{2\pi a}{P}.
$$

We do not measure $v_\star$ directly: we measure only the line-of-sight projection $v_\star \sin i$, where $i$ is the inclination of the orbit normal to our line of sight.
The maximum line-of-sight reflex velocity is therefore

$$
K_\star = v_\star \sin i = \frac{m_p \sin i}{M_\star + m_p} \cdot \frac{2\pi a}{P}.
$$

To eliminate $a$ in favour of measurable quantities we use Kepler's third law for the **relative** semi-major axis,

$$
a^3 = \frac{G(M_\star + m_p) P^2}{4\pi^2}, \qquad a = \left(\frac{G(M_\star + m_p) P^2}{4\pi^2}\right)^{1/3}.
$$

Substituting into $K_\star$ gives

$$
K_\star = \frac{m_p \sin i}{M_\star + m_p} \cdot \frac{2\pi}{P} \cdot \left(\frac{G(M_\star + m_p) P^2}{4\pi^2}\right)^{1/3} = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{(M_\star + m_p)^{2/3}}.
$$

For the case $m_p \ll M_\star$, which holds for almost all known exoplanets, we can approximate $(M_\star + m_p)^{2/3} \approx M_\star^{2/3}$.
For an eccentric orbit a factor of $1/\sqrt{1 - e^2}$ multiplies the right-hand side.
The full expression in the literature includes that eccentricity factor:

$$
K_\star = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{M_\star^{2/3}} \frac{1}{\sqrt{1 - e^2}}.
$$

Two things should be clear from this expression.
First, $K_\star \propto P^{-1/3}$, so short-period planets give a larger reflex than long-period planets at the same mass.
Second, $K_\star \propto m_p \sin i$, so a radial velocity measurement alone gives only the **minimum** mass $m_p \sin i$, not the true mass $m_p$.

**Step 3: combining the two observables (~3 min).**
Suppose now that the same planet **both transits and produces a measurable radial velocity signal**.
The transit immediately tells us that the orbital plane is nearly edge-on: the impact parameter is small and $\sin i \approx 1$ to better than a few per cent (a non-grazing transit requires $i$ within roughly $R_\star / a$ of $90^\circ$).
This single piece of information collapses the $m_p \sin i$ degeneracy: with $\sin i \approx 1$ the inferred $m_p \sin i$ is the true mass $m_p$.
We now have, for the same object:

- $R_p$ from the transit depth and the stellar radius.
- $m_p$ from the radial velocity semi-amplitude, the orbital period, and the stellar mass.

The bulk density follows immediately from elementary geometry:

$$
\bar{\rho}_p = \frac{m_p}{\frac{4}{3}\pi R_p^3} = \frac{3 m_p}{4\pi R_p^3}.
$$

This is the central observational quantity that turns an abstract exoplanet detection into a physically meaningful object.
A density of about $5.5$ g/cm$^3$ matches an Earth-like silicate-iron rocky composition.
A density of about $1.3$ g/cm$^3$ matches Jupiter and is consistent with a hydrogen-helium envelope around a small dense core.
A density of $0.5$ g/cm$^3$, lower than water, indicates an inflated or low-mass H/He envelope.
A density between rocky and gas, near $2$--$4$ g/cm$^3$, is typical of "sub-Neptunes" and indicates a substantial water-ice or H/He volatile component on top of a rocky core.
Without the joint transit-plus-RV measurement, we cannot tell any of these apart ({numref}`fig:ck17massradius` collects the empirical mass-radius relation across the four major compositional regimes).

```{figure} figures/chenkipping_mass_radius.avif
:align: center
:name: fig:ck17massradius
:width: 90%

Empirical mass-radius relation across the full range of solar-system bodies, exoplanets, brown dwarfs, and stars, from {cite:t}`ChenKipping2017`. The shaded regions mark four distinct compositional regimes: terran ($M \lesssim 2\,\Mearth$, scaling roughly as $R \propto M^{0.28}$), Neptunian ($2\,\Mearth \lesssim M \lesssim 0.4\,\Mjup$, $R \propto M^{0.59}$), Jovian ($0.4\,\Mjup \lesssim M \lesssim 80\,\Mjup$, $R \propto M^{-0.04}$, where electron degeneracy and self-compression flatten the relation), and stellar ($M > 80\,\Mjup$, hydrogen burning sets in). Each break corresponds to a different dominant pressure source. The "Neptunian" segment is the modern compositional location of the sub-Neptune family, the population that has no analogue in the solar system.
```

The pedagogical message is this.
The transit-plus-RV combination is the **single piece of observational machinery** that took exoplanet science from an exotic claim about a few hot Jupiters in 1995 to a quantitative compositional census of thousands of planets by 2020.
Every demographic structure we will discuss in Part 2, including the radius valley and the sub-Neptune family, exists as a discovery only because we can measure both $R_p$ and $m_p$ for the same object.
````

### Direct imaging

**Direct imaging** spatially separates planetary photons from stellar light on a detector.
Contrast reaches $10^{-9}$ for a Jupiter at 5 AU and $10^{-10}$ for an Earth analogue at 10 pc, at angular separations of $0.1$ arcsecond.

**Adaptive optics** correct atmospheric turbulence with deformable mirrors to achieve diffraction-limited resolution.
**Coronagraphs** suppress central starlight, while **angular differential imaging** (ADI) and **spectral differential imaging** (SDI) subtract residual stellar speckles.

```{figure} figures/hr8799_discovery.avif
:align: center
:name: fig:hr8799
:width: 80%

Discovery image of the **HR 8799** planetary system from {cite:t}`Marois2008`. Three of the four giant planets (b, c, d) are visible at projected separations of $24$, $38$, and $68$ AU after subtraction of the stellar PSF (point-spread function, the blurred image of the star itself) using angular differential imaging. The Keck and Gemini AO observations spanned 2004 to 2008. The fourth planet, HR 8799 e (at $\sim 14$ AU), was added by Marois et al.\ in 2010. The four planets have masses of roughly $5$--$10\,\Mjup$ and span orbital separations of $14$--$68$ AU. They are young, hot, self-luminous, and still cooling: this is the regime in which direct imaging works.
```

Because young giant planets ($\lesssim 100$ Myr old) still radiate formation heat, detections are biased toward massive ($> 1\,\Mjup$), wide-orbit ($> 10$ AU) giants.
Key systems include HR 8799 {cite:p}`Marois2008` ({numref}`fig:hr8799`) and $\beta$ Pictoris b {cite:p}`Lagrange2010` ({numref}`fig:betapic`).

```{figure} figures/betapic_imaging.avif
:align: center
:name: fig:betapic
:width: 80%

The first ground-based direct image of $\beta$ Pictoris b, a $\sim 9\pm 3\,\Mjup$ planet (hot-start models) at $\sim 9$ AU from the central young A-type star. The two epochs (2003 left, 2009 right) show clear orbital motion in the projected sky position, decisively confirming a bound companion rather than a chance alignment. From {cite:t}`Lagrange2010`. The same star hosts an extensively imaged debris disk and a second giant planet (c), discovered later on a closer orbit at $\sim 2.7$ AU, interior to planet b.
```

PDS 70 contains the first planets detected directly inside the cleared gap of a protoplanetary disk {cite:p}`Keppler2018,Haffert2019`.
Accretion onto PDS 70 b and c produces H$\alpha$ emission from shocks, confirming planet-disk interaction models ({ref}`Lecture 2 <lecture02>`; {numref}`fig:pds70b`, {numref}`fig:pds70bc`, and {numref}`fig:pds70disk`).

```{figure} figures/pds70b_keppler.avif
:align: center
:name: fig:pds70b
:width: 80%

The discovery of **PDS 70 b** in the gap of its protoplanetary disk, from {cite:t}`Keppler2018`. The image shows the SPHERE near-infrared detection of the planet inside the cleared central cavity of the transition disk after PSF subtraction. The host star is masked at the centre. PDS 70 b is the first directly imaged exoplanet caught in the act of forming inside its parent disk.
```

```{figure} figures/pds70bc_haffert.avif
:align: center
:name: fig:pds70bc
:width: 90%

Detection of PDS 70 b and c in three epochs and three wavelength bands, from Figure 2 of {cite:t}`Haffert2019`. All three panels show the same field: offset in right ascension against offset in declination, both in milliarcseconds, with the star at the origin (white star symbol) and the two planets marked by white circles. Each panel has its own colour bar, normalised from 0 to 1. Panel a is the MUSE H$\alpha$ detection map of 20 June 2018, after removal of the direct and scattered starlight; the band just south of PDS 70 b is most likely an artefact of the MUSE image slicer. Panel b is the SPHERE/IRDIS K1-band image of 31 May 2016 after angular differential imaging. Panel c is the NACO L$'$-band image of 1 June 2016, in which PDS 70 c is blended with the disk because the point spread function is broad at that wavelength. The H$\alpha$ emission of PDS 70 b and of the newly discovered PDS 70 c is interpreted as accretion shock luminosity from gas that falls onto the planets, which is evidence that two protoplanets accrete at the same time in the disk gap.
```

```{figure} figures/pds70_disk.avif
:align: center
:name: fig:pds70disk
:width: 65%

Composite scattered-light image of the PDS 70 protoplanetary disk plus its two embedded planets, from {cite:t}`Haffert2019`. The outer ring is the parent disk, the cleared central cavity is the planet-carved gap, and the two white circles inside the gap mark the positions of PDS 70 b (closer to the star) and PDS 70 c (further out). This is the cleanest direct observational match between a planet-formation theory prediction (a planet inside the gap of a transition disk) and a real system in nature.
```

JWST mid-infrared observations of HIP 65426 b and VHS 1256 b extend direct imaging from discovery to atmospheric characterisation.

### Astrometry

**Astrometry** measures the angular reflex motion of the host star against background reference stars.
The expected angular amplitude is

$$
\alpha = \frac{m_p}{M_\star} \cdot \frac{a_p}{d},
$$

where $d$ is the distance to the system.
For a Jupiter analogue around the Sun at 10 pc, this is about half a milli-arcsecond, whereas for an Earth analogue it is $0.3$ micro-arcseconds.
Astrometric exoplanet detection therefore demands microarcsecond precision over years to decades.

The space-based mission Hipparcos (1989 to 1993) reached about a milli-arcsecond, which was sufficient to set upper limits on planet masses but not to discover exoplanets.
Gaia, launched in 2013, performs an all-sky astrometric survey of more than a billion stars with a final precision of $\sim 10$ microarcseconds for bright stars.
This is the precision regime in which Jupiter analogues become accessible.

Early Gaia data releases provided five-parameter astrometry and orbital fits for substellar companions {cite:p}`GaiaDR3`.
DR4 will deliver epoch-by-epoch astrometric time series, with a forecast of $\sim 2 \times 10^4$ detectable exoplanet signatures, although the confirmed sample after follow-up is expected to be several times smaller {cite:p}`Perryman2014`.
DR5 will use the full ten years of mission data to push sensitivity into the sub-Jovian regime, providing an unbiased census of long-period gas giants.

Astrometry is complementary to radial velocity because it directly measures the inclination of the orbit, breaking the $m \sin i$ degeneracy without requiring a transit.
A planet that produces both a Gaia astrometric signal and a radial velocity signal yields a true mass, an orbit inclination, and a complete three-dimensional orbital solution.
The combination is particularly powerful for wide-orbit Jupiter analogues that fall in the blind spot of transit surveys.

### Microlensing

In **gravitational microlensing**, the gravitational field of a foreground star (the **lens**) bends light from a distant background star, briefly magnifying its brightness.
This stellar **microlensing event** produces a smooth light curve lasting weeks to months.
If the lens star hosts a planet, planetary gravity introduces an additional short-duration spike lasting hours to days.
The amplitude and timing of this spike determine the planet's mass and projected separation in units of the **Einstein ring radius**, set by the lens mass and distance.

Microlensing detects planets at distances of kiloparsecs and projected separations of $0.5$ to $10$ AU, mapping onto the snow-line region where giant planets form.
Because the stellar alignment is a unique, one-shot event that never repeats, detections cannot be confirmed by follow-up observations or characterised in the manner of transits or radial velocities.
The Nancy Grace Roman Space Telescope, launched in August 2026, will conduct a dedicated survey of the Galactic bulge expected to discover $\sim 1400$ bound exoplanets down to lunar-mass bodies {cite:p}`Penny2019`.
The mission will also constrain the population of **free-floating planets**, planetary-mass bodies unbound from any host star.

### Timing methods

When a planet has a companion in the same system, gravitational interactions periodically perturb its transit times, producing **transit timing variations** (TTVs) {cite:p}`Holman2005`.
Because TTVs encode the masses of interacting planets, they yield a **dynamical mass** measurement without requiring radial velocity follow-up.
This is essential for small planets around faint stars where radial velocity observations are infeasible, such as the seven planets of the TRAPPIST-1 system.

A second timing approach is **pulsar timing**, the technique that detected the first exoplanets {cite:p}`Wolszczan1992`.
An orbiting planet produces periodic shifts in radio pulse arrival times relative to the millisecond pulsar spin period.
The technique is sensitive down to lunar-mass bodies, but the sample of suitable millisecond pulsars is small.

A third timing technique exploits eclipsing binary stars.
A circumbinary planet orbiting a close binary perturbs the timing of stellar eclipses and can also transit across both stars.
The first confirmed circumbinary transiting planet, Kepler-16 b, was found this way in 2011 {cite:p}`Doyle2011`.

### Detection biases summary

Each detection method introduces a **detection bias**, selecting planets in different regions of parameter space.
Radial velocity is most sensitive to massive planets on short-period orbits (since $K \propto P^{-1/3}$) around bright Sun-like stars.
Transit photometry is most sensitive to short periods (less than $\sim 100$ days) and large $R_p / R_\star$ ratios.
Direct imaging detects young, self-luminous giants on wide orbits ($> 10$ AU).
Astrometry is most sensitive to wide orbits matching the mission baseline.
Microlensing detects planets at 1 to 10 AU at any host distance, but is unrepeatable.
Timing is sensitive to compact multi-planet systems or circumbinary configurations.

The observed exoplanet archive reflects these combined biases rather than the true physical distribution.
Demographic claims in Part 2 therefore require **bias correction**, reporting underlying occurrence rather than raw catalogue counts.
This correction is reliable for Kepler, but much less certain for other surveys.

## Part 2: Demographics and architectures

### The Kepler revolution and the TRAPPIST-1 laboratory

Kepler provided computable detection efficiency to infer **occurrence rates**: how many planets of a given size and period exist per star {cite:p}`Borucki2010`.

On average, at least one planet exists per main-sequence star, with small planets below 4 Earth radii being the most common {cite:p}`Petigura2018`.
**Hot Jupiters** occur around only 0.5% to 1% of Sun-like stars {cite:p}`Fressin2013`.
The habitable-zone Earth-size planet occurrence rate is estimated at $\eta_\oplus \sim 0.4$ ({numref}`fig:petigura` and {numref}`fig:bryson`) {cite:p}`Bryson2021`.

```{figure} figures/petigura_occurrence.avif
:align: center
:name: fig:petigura
:width: 90%

Kepler-derived planet occurrence rates as a function of orbital period and planet size, from the California-Kepler Survey {cite:p}`Petigura2018`. Small planets are far more common than giants at every period, and the occurrence rate of small planets falls off only slowly toward longer periods. The flattening at the longest periods is partly observational (Kepler had only $\sim 4$ years of baseline), but the overall picture is that the typical Sun-like star hosts at least one small planet inside 1 AU.
```

```{figure} figures/bryson_etaearth.avif
:align: center
:name: fig:bryson
:width: 90%

Marginalised differential occurrence rate of small planets from the Kepler analysis of {cite:t}`Bryson2021`. **Left**: occurrence per unit planetary radius, $\dd N / \dd R$, evaluated at $\Delta R = 0.25\,\Rearth$. **Right**: occurrence per unit instellation flux (the stellar radiative flux received at the planet's orbit), $\dd N / \dd I$, evaluated at $\Delta I = 0.18$ (note the inverted x-axis, with low instellation on the right). Dark and light shaded bands are the 68\% and 95\% credible intervals. The observed occurrence rates give central values of $\eta_\oplus \sim 0.4$ for the conservative habitable zone, with 68\% credible intervals of roughly $0.2$--$0.9$ depending on the precise definition of habitable-zone Earth analogue. This is the range typically quoted in mission yield estimates for HWO and LIFE (see Part 3).
```

The **TRAPPIST-1** system hosts seven transiting Earth-sized planets within 0.06 AU of an ultra-cool dwarf {cite:p}`Gillon2017`.
The planets form a chain of **mean-motion resonances**, orbital periods locked near ratios of small integers, consistent with capture during an early disk-migration phase.
All seven planets transit ({numref}`fig:trappist1transits`), a configuration with probability below $10^{-3}$ for random orientations, which suggests that compact M-dwarf systems are intrinsically very flat; the transits allow their masses to be measured from transit timing variations ({numref}`fig:trappist1ttvs`).

```{figure} figures/trappist1_transits.avif
:align: center
:name: fig:trappist1transits
:width: 80%

Transit light curves of the seven **TRAPPIST-1** planets from {cite:t}`Gillon2017`, observed with Spitzer at $4.5\,\mu$m and ground-based facilities. The seven planets are labelled b through h in order of increasing orbital distance. The successive transit depths trace the planet sizes; all seven are Earth-sized to within a factor of $\sim 1.5$. The overall flatness of the system geometry is remarkable: the probability that all seven planets transit if the orbits were randomly oriented is less than $10^{-3}$.
```

```{figure} figures/trappist1_ttvs.avif
:align: center
:name: fig:trappist1ttvs
:width: 80%

Transit timing variations (TTVs) of **TRAPPIST-1 e** as a representative panel from the seven-planet TTV dataset of {cite:t}`Gillon2017`. Black points are observed deviations from a constant-period transit ephemeris; the red curve is the best-fit dynamical model that includes gravitational coupling to the other six planets. The TTV amplitude reaches tens of minutes and is coherent over hundreds of days. Inverting the joint seven-planet TTV signal yields **dynamical masses** for all the planets without any radial velocity follow-up; this is essential because TRAPPIST-1 is too faint at optical wavelengths for high-precision radial velocity measurements.
```

### The period-radius diagram

The **period-radius diagram** plots orbital period against planetary radius for confirmed transiting planets ({numref}`fig:fultonpr`).
Gas giants ($R_p > 10\,\Rearth$) include short-period **hot Jupiters** ($P < 10$ days).
Small planets split into **sub-Neptunes** ($R_p \approx 2$ to $4\,\Rearth$), which have no solar system analogue, and rocky **super-Earths** ($R_p \approx 1$ to $1.8\,\Rearth$).
The **terrestrial analogue** regime ($R_p \lesssim 1.5\,\Rearth$ at periods longer than $\sim 100$ days) remains largely unexplored.

```{figure} figures/fulton_period_radius.avif
:align: center
:name: fig:fultonpr
:width: 70%

Period-radius distribution of small Kepler planets after stellar parameter refinement and bias correction, from {cite:t}`Fulton2017`. The colour scale indicates detection completeness. The clear deficit of planets at $R_p \approx 1.8\,\Rearth$ across all orbital periods is the **radius valley** or **Fulton gap**, the central empirical structure that splits the small-planet population into super-Earths and sub-Neptunes.
```

### The radius valley (Fulton gap)

The **radius valley** (or **Fulton gap**) is a deficit of small exoplanets at $R_p \approx 1.5$ to $2\,\Rearth$ that separates rocky super-Earths from volatile-rich sub-Neptunes ({numref}`fig:fultongap`) {cite:p}`Fulton2017`.
Below the valley, super-Earths peak near $1.3\,\Rearth$, while sub-Neptunes above the valley peak near $2.4\,\Rearth$.

```{figure} figures/fulton_gap.avif
:align: center
:name: fig:fultongap
:width: 80%

The **radius valley**: the histogram of planet radii in the Kepler sample after stellar parameter refinement, from {cite:t}`Fulton2017`. The deficit at $R_p \approx 1.8\,\Rearth$ is the central empirical signature that splits small planets into a rocky **super-Earth** group at $\sim 1.3\,\Rearth$ (red shaded) and a volatile-rich **sub-Neptune** group at $\sim 2.4\,\Rearth$ (cyan shaded). The smooth curve is a kernel density estimator with the gap clearly resolved.
```

The valley is produced when close-in planets with thin hydrogen-helium envelopes lose their gas via atmospheric escape to become bare rocky cores.
Two physical mechanisms can drive this envelope stripping during the first hundreds of millions of years.

The first mechanism is **photoevaporation**, where stellar XUV (ultraviolet and X-ray) radiation heats the upper envelope to drive hydrodynamic escape {cite:p}`OwenWu2013`.
In **energy-limited escape**, a fraction $\epsilon \sim 0.1$ of the absorbed XUV flux converts into the gravitational work needed to lift gas out of the potential well:

$$
\dot{M} \approx \frac{\epsilon \, \pi F_\mathrm{XUV} R_p^3}{G M_p}.
$$

The $R_p^3$ scaling indicates that low-density, low-mass planets are stripped most easily.
For a $10\,\Mearth$ sub-Neptune with $R_p \approx 2.5\,\Rearth$ at $0.1$ AU, an initial saturated flux of $F_\mathrm{XUV} \sim 300$ W m$^{-2}$ yields a mass-loss rate of $\dot{M} \sim 10^{8}$ kg s$^{-1}$.
Integrated over the $\sim 100$ Myr saturated phase, this removes $\sim 3 \times 10^{23}$ kg, stripping the envelope to produce the bimodal radius valley ({numref}`fig:owenvalley` and {numref}`fig:owenmassloss`).

```{figure} figures/owen_evaporation_valley.avif
:align: center
:name: fig:owenvalley
:width: 70%

Photoevaporation theory prediction of the radius valley from {cite:t}`OwenWu2013`. The figure shows a model planet population evolved through XUV-driven envelope stripping, projected onto a planet mass versus planet radius plane. Planets with envelopes survive above $\sim 2\,\Rearth$; planets that lose their envelopes settle as bare rocky cores below $\sim 1.8\,\Rearth$. The intermediate regime is depopulated, producing the observed valley.
```

```{figure} figures/owen_xuv_massloss.avif
:align: center
:name: fig:owenmassloss
:width: 90%

Photoevaporation-driven evolution of a young sub-Neptune in the {cite:t}`OwenWu2013` model. **Top**: planetary radius as a function of time since disc clearing, for two host XUV histories (line styles) and two starting orbital separations. **Bottom**: planet mass over the same evolution. The thin vertical line marks the end of the saturated XUV phase at $\sim 100$ Myr. After this time the radius and mass plateau; planets that have lost their envelopes by then settle as bare rocky cores below the radius valley.
```

The second mechanism is **core-powered mass loss**, where the cooling luminosity and primordial heat of the rocky core drive envelope outflow {cite:p}`Ginzburg2018`.
Heat released from the cooling interior over hundreds of Myr powers hydrodynamic escape without requiring external XUV flux, naturally reproducing the gap at $\sim 1.8\,\Rearth$ ({numref}`fig:ginzburg`).

```{figure} figures/ginzburg_corepowered.avif
:align: center
:name: fig:ginzburg
:width: 80%

Core-powered mass loss model from {cite:t}`Ginzburg2018`. The figure shows the predicted radius distribution of small planets when envelope mass loss is driven by the cooling rocky interior rather than by external XUV photons. The distribution is bimodal in the same sense as photoevaporation models, with a gap at $\sim 1.8\,\Rearth$ separating bare rocky cores from sub-Neptunes that retain their envelopes.
```

Precise **asteroseismic** stellar radii, derived from stellar oscillation frequencies, show that the radius valley shifts to smaller radii at longer orbital periods {cite:p}`VanEylen2018`.
This negative slope is consistent with both photoevaporation and core-powered mass loss, although current data cannot yet distinguish between the two mechanisms ({numref}`fig:vaneylen` and {numref}`fig:vaneylenmodels`).

```{figure} figures/vaneylen_radius_valley.avif
:align: center
:name: fig:vaneylen
:width: 90%

Slope of the **radius valley** with orbital period, from the asteroseismic Kepler subsample of {cite:t}`VanEylen2018`. The grey band marks the empirical valley boundary, which descends to smaller radii at longer periods. Brown points are super-Earths (below the valley) and blue points are sub-Neptunes (above). The slope is consistent with the predictions of both photoevaporation and core-powered mass loss; current data do not yet discriminate between the two.
```

```{figure} figures/vaneylen_models.avif
:align: center
:name: fig:vaneylenmodels
:width: 70%

Model predictions for the slope of the radius valley with orbital period, overlaid on the {cite:t}`VanEylen2018` data. The black curves are different theoretical predictions; both photoevaporation and core-powered mass loss predict broadly compatible slopes, and the data alone cannot decisively prefer one over the other.
```

Because stripping removes primordial envelopes, many close-in super-Earths are remnant cores rather than primordially rocky planets, although for any single planet the two origins cannot be told apart from bulk density alone.
This transition affects habitability discussions, as stripped cores experience extensive atmospheric loss that can alter their surface and interior chemistry.

### The hot Neptune desert

The **hot Neptune desert** is a deficit of Neptune-mass planets ($M_p \approx 10$ to $100\,\Mearth$) at orbital periods shorter than 5 days.
While hot Jupiters and rocky planets occur at these periods, {cite:t}`Mazeh2016` showed that hot Neptunes are absent ({numref}`fig:neptunedesert`).

```{figure} figures/mazeh_neptune_desert.avif
:align: center
:name: fig:neptunedesert
:width: 90%

The **hot Neptune desert** in the period-mass and period-radius planes from {cite:t}`Mazeh2016`. The shaded triangular region is empirically depleted of Neptune-mass planets. The upper edge follows a tight power law, plausibly set by Roche-lobe overflow on inflated hot Jupiters; the lower edge is more diffuse and has been variously attributed to photoevaporation, in-situ formation, and high-eccentricity migration with tidal circularization. The desert is one of the strongest pieces of evidence for atmospheric mass loss as a major sculptor of close-in planets.
```

Photoevaporation strips envelopes from lower-mass planets below the desert, leaving bare super-Earths.
At the upper edge, inflated planets fill their **Roche lobe**, the region where gas stays gravitationally bound to the planet rather than the star, losing mass through tidal stripping.
The desert is therefore a second, independent piece of evidence that atmospheric mass loss sculpts close-in planets after formation.

### Planetary system architectures

Multi-planet systems observed by Kepler enable statistical studies of planetary architecture.
{cite:t}`Weiss2018` identified a **peas in a pod** architecture, in which planets within the same system share similar sizes ({numref}`fig:weisspeas`) and regular orbital period spacing ({numref}`fig:weiss_spacing`).

```{figure} figures/weiss_peas_in_pod.avif
:align: center
:name: fig:weisspeas
:width: 75%

The **peas in a pod** correlation from {cite:t}`Weiss2018`: the radius of an inner Kepler multi-planet $R_i$ versus the radius of its immediately outer neighbour $R_{i+1}$. The clear positive correlation along the diagonal means that within a system the planets tend to be the same size as each other, far more so than randomly drawn pairs of planets from the Kepler sample. The Pearson correlation coefficient is 0.65 and the null-hypothesis probability is $p < 10^{-7}$.
```

```{figure} figures/weiss_spacing.avif
:align: center
:name: fig:weiss_spacing
:width: 75%

Period-ratio correlation in Kepler multi-planet systems, from {cite:t}`Weiss2018`. Each point is a triple of consecutive transiting planets in the same system: the horizontal axis is the period ratio of the inner pair ($P_{j+1}/P_j$) and the vertical axis is the period ratio of the next pair out ($P_{j+2}/P_{j+1}$). The clustering along the diagonal (Pearson $R = 0.46$, $p < 10^{-5}$) means that within a system, neighbouring period ratios are similar, supporting the view that compact inner systems form by a smooth, local process rather than by stochastic large impacts.
```

This regularity indicates that compact inner systems form through smooth growth and disk migration rather than stochastic giant impacts.
In contrast, terrestrial planet assembly in the solar system was dominated by giant impacts ({ref}`Lecture 2 <lecture02>`), suggesting the inner solar system may be dynamically unusual.

This pattern is a statistical trend for compact systems rather than a universal rule.
Radial-velocity samples of wider systems and exceptional Kepler architectures exhibit greater diversity.

Resonant chains provide direct evidence that early disk migration locked planets into place before gas dispersal.
For example, TRAPPIST-1 contains seven Earth-sized planets in mean-motion resonances within 0.06 AU {cite:p}`Gillon2017`.
Other notable compact multi-planet systems include Kepler-90 with eight planets and TOI-178 with six planets in a resonant chain.

### Hot Jupiters and migration

Hot Jupiters cannot form in situ at $\sim 0.05$ AU because local disk temperatures prevent ice condensation and solid mass is insufficient to assemble a $\sim 10\,\Mearth$ core before gas disperses.
They must form at several AU and migrate inward.
The inner edge of the surviving population is set by the **fluid Roche limit**, the orbital separation where stellar tides tear a planet apart:

$$
d_R \approx 2.46\,R_\star \left(\frac{\rho_\star}{\rho_p}\right)^{1/3}.
$$

For a Sun-like star ($\rho_\star \approx 1.4$ g cm$^{-3}$) and a hot Jupiter ($\rho_p \approx 1$ g cm$^{-3}$), this limit gives $d_R \approx 2.7\,R_\star \approx 0.013$ AU.
The observed pile-up of hot Jupiters at $\sim 0.04$ to $0.05$ AU sits a factor of three to four outside this limit, where orbits survive over Gyr timescales without tidal disruption.
Three competing mechanisms can drive inward migration.

In **disk migration** (Type II), a giant planet embedded in a gaseous disk excites density waves whose net torque drives inward migration ({ref}`Lecture 2 <lecture02>`).
This quiescent mechanism preserves low orbital eccentricities and leaves orbits aligned with the stellar equator.

In **high-eccentricity migration**, a distant companion or planet excites Kozai-Lidov oscillations that trade inclination for eccentricity over $10^{6}$ to $10^{8}$ years.
When perihelion approaches the star, **tidal dissipation** circularises the orbit at small separation while freezing in large orbital misalignments.

In **planet-planet scattering**, dynamical instabilities in multi-giant systems eject planets and leave survivors on eccentric orbits circularised by tides.
Like high-eccentricity migration, scattering produces large misalignments ({numref}`fig:obliquitypathways`).

```{figure} figures/obliquity_pathways.avif
:align: center
:name: fig:obliquitypathways
:width: 90%

Schematic of the three migration pathways for hot Jupiters and the **stellar obliquities** they produce, from the review of {cite:t}`Albrecht2022`. Disk migration (left) preserves the alignment of the stellar spin and the orbit normal because the disk and the stellar equator are themselves aligned. High-eccentricity migration via Kozai-Lidov coupling to a distant perturber (right) can produce arbitrary misalignments. Planet-planet scattering similarly produces misalignments.
```

These pathways are distinguished observationally by the **stellar obliquity**, the angle between the stellar rotation axis and the planetary orbit normal.
Obliquities are measured via the **Rossiter-McLaughlin effect** ({numref}`fig:rmgeom`), where a transiting planet sequentially occults the blueshifted and redshifted stellar hemispheres to reveal the sky-projected spin-orbit angle.
Hot Jupiters around cool stars ($T_\mathrm{eff} < 6250$ K) are mostly well aligned, reflecting disk migration or tidal realignment in convective envelopes.
Hot Jupiters around hot stars ($T_\mathrm{eff} > 6250$ K) show wide misalignments spanning prograde to retrograde orbits {cite:p}`Albrecht2022` ({numref}`fig:obliquitydist`).

```{figure} figures/rossiter_mclaughlin.avif
:align: center
:name: fig:rmgeom
:width: 80%

Geometry of the **Rossiter-McLaughlin effect**, from the {cite:t}`Triaud2018` review chapter. As a transiting planet moves across the rotating stellar disk along its chord (impact parameter $b$), it sequentially occults the approaching (blueshifted, blue) hemisphere and the receding (redshifted, red) hemisphere. The resulting time-resolved distortion in the stellar absorption-line profile traces the angle $\lambda$ between the projected stellar spin axis and the orbital angular momentum vector on the sky.
```

```{figure} figures/obliquity_distribution.avif
:align: center
:name: fig:obliquitydist
:width: 90%

Projected stellar obliquity $\lambda$ as a function of scaled orbital separation $a/R_\star$ for the hot Jupiter sample, from {cite:t}`Albrecht2022`. The stacked panels split the sample by host-star spectral type bin. Tight orbits around cool stars cluster near zero obliquity, consistent with tidal realignment of initially misaligned orbits over Gyr timescales. The wider scatter at larger $a/R_\star$ and around hotter hosts indicates that the **primordial** obliquity distribution was wide, supporting an important role for high-eccentricity migration in the hot Jupiter population. The inset shows the solar system planets for reference.
```

All three migration mechanisms operate, with their relative contributions depending on host-star type, multiplicity, and system age.
Hot Jupiters typically lack nearby planetary companions.
This loneliness supports violent dynamical histories that cleared neighbouring planets rather than smooth in situ formation.

### Super-Earth and sub-Neptune composition

Bulk-density measurements combining transit and radial-velocity data enable a compositional census of small planets.
**Super-Earths** below the radius valley have rocky compositions with densities of $4$ to $8$ g/cm$^3$, similar to Earth and Venus.
**Sub-Neptunes** above the valley have lower densities, typically $1$ to $3$ g/cm$^3$, requiring a volatile envelope of $\mathrm{H_2}$/He or $\mathrm{H_2O}$ over a rocky core.
Bulk density alone is degenerate: multiple internal structures can match the same bulk density.

Sub-Neptunes with $\gtrsim 10$ to $20\%$ $\mathrm{H_2O}$ by mass are candidate water worlds.
In the proposed **hycean** scenario, a planet hosts a shallow liquid water ocean beneath a thick $\mathrm{H_2}$-rich atmosphere {cite:p}`Madhusudhan2021`.
The strong $\mathrm{H_2}$ greenhouse effect can keep the ocean liquid at equilibrium temperatures below 273 K, extending the candidate habitable region.
This interpretation is contested: observations of K2-18 b may reflect mini-Neptunes without a surface, or an $\mathrm{H_2}$ envelope over a deep **magma ocean** {cite:p}`Shorttle2024`.

A second compositional ambiguity applies to small close-in planets in the ultra-short-period regime at a few stellar radii.
Under high instellation, the same density and radius can match either a bare-rock surface or a Venus analogue with a thick $\mathrm{CO_2}$ atmosphere in a runaway greenhouse.
Distinguishing them requires spectroscopy (see Part 3).

### M dwarf planets

M dwarfs account for roughly 75\% of main-sequence stars and are the easiest targets for discovering small habitable-zone planets.
Because the habitable-zone semi-major axis scales as $\sqrt{L_\star}$, closer orbits around low-luminosity M dwarfs increase the geometric transit probability $R_\star / a$.
The transit depth $(R_p / R_\star)^2$ for an Earth-sized planet is also much larger than around a Sun-like star.

```{figure} figures/dressing_mdwarf_occurrence.avif
:align: center
:name: fig:dressing
:width: 75%

Cumulative occurrence rate of small planets around M dwarfs as a function of orbital period from the full Kepler sample, from {cite:t}`Dressing2015`. Each curve is a different planet-radius bin from $0.5$--$1\,\Rearth$ (black) to $3$--$4\,\Rearth$ (red). M dwarfs host on average $\sim 2$ small planets per star inside 200 days, and roughly one Earth-size planet per star in or near the habitable zone. M dwarf small-planet occurrence rates exceed those around Sun-like stars by roughly a factor of 2--3.
```

Kepler occurrence rates indicate roughly $2.5$ small planets ($R_p < 4\,\Rearth$) per M dwarf inside 200 days, with $0.16^{+0.17}_{-0.07}$ Earth-size planets in the conservative habitable zone ({numref}`fig:dressing`) {cite:p}`Dressing2015`.
These occurrence rates make M dwarf habitable-zone planets central observational targets.

The main challenge for habitability is **stellar activity**, the elevated magnetic and high-energy emission of the host star.
M dwarfs spend hundreds of Myr in an early phase with luminosities up to ten times their main-sequence values.
Habitable-zone planets sit inside their **runaway-greenhouse boundary** during this phase, causing severe water loss.
High XUV flux can strip an Earth-equivalent ocean of water, leaving an abiotic oxygen atmosphere as a false-positive **biosignature** (a chemical sign mimicking life) {cite:p}`LugerBarnes2015`.
Whether modern M dwarf habitable-zone planets retain water remains an open question under study by JWST.

A second challenge is **tidal locking**, the synchronization of rotation and orbit into a $1{:}1$ spin-orbit resonance.
Close-in orbits produce permanent daysides and nightsides, requiring atmospheric heat transport to prevent volatile collapse on the nightside.
Three-dimensional climate models show that substellar clouds can stabilize climates and extend the habitable zone closer to the star {cite:p}`Yang2013`.
The seven planets of TRAPPIST-1 are a primary laboratory to study these climate regimes.

## Part 3: Characterisation, habitability, and the comparative payoff

### Transmission spectroscopy during transit

During transit, atmospheric absorption along the terminator sets the **wavelength-dependent transit depth**:

$$
\delta(\lambda) = \frac{[R_p + n_H H(\lambda)]^2}{R_\star^2},
$$

where $H = \kB T / (\mu m_u g)$ is the atmospheric **scale height** (the density e-folding scale).
For a hot Jupiter ($T \approx 1500$ K, $\mu \approx 2.3$, $g \approx 25$ m s$^{-2}$):

$$
H = \frac{\kB T}{\mu m_u g} = \frac{(1.38 \times 10^{-23})(1500)}{(2.3)(1.66 \times 10^{-27})(25)} \approx 2 \times 10^{5}\ \mathrm{m},
$$

With $R_p \approx 1.2\,\Rjup$, $R_\star \approx 1\,\Rsun$, and $n_H \approx 5$:

$$
\frac{\Delta\delta}{\delta} \approx \frac{2 n_H H}{R_p} \approx \frac{2 \times 5 \times 2 \times 10^{5}\ \mathrm{m}}{8.6 \times 10^{7}\ \mathrm{m}} \approx 2 \times 10^{-2},
$$

The absolute depth change $(\Delta\delta / \delta) \times \delta \approx 2 \times 10^{-4}$ (a few hundred ppm) is detectable with JWST.
Sub-Neptunes reach 10 to 100 ppm, while terrestrial planets around M dwarfs fall below 10 ppm.

High-altitude **clouds and hazes** flatten transmission spectra via continuum opacity.
Hot Jupiter spectra span a continuum from clear to cloudy ({cite:t}`Sing2016`, {numref}`fig:sing`; {numref}`fig:gj1214`).

```{figure} figures/sing_hotjup_spectra.avif
:align: center
:name: fig:sing
:width: 70%

Transmission spectra of ten hot Jupiters observed with HST and Spitzer, from Figure 1 of {cite:t}`Sing2016`. The horizontal axis is wavelength from $0.3$ to $5$ $\mu$m on a logarithmic scale. The vertical axis is the relative altitude $z(\lambda)/H_{\rm eq}$ in units of the equilibrium scale height, with the ten spectra offset from each other. Points with error bars are the measurements: the horizontal bar is the width of the wavelength bin and the vertical bar is the $1\sigma$ uncertainty. The solid coloured line through each set of points is a fitted atmospheric model. The order from top to bottom is by increasing $\Delta Z_{\rm UB-LM}$, the altitude difference between the blue-optical and the mid-infrared; a large value means the optical radius is high relative to the mid-infrared, which is the signature of a scattering haze or cloud. The dotted vertical lines mark the Na and K resonance lines near $0.59$ and $0.77$ $\mu$m, and the bracket near $1.4$ $\mu$m marks the $\mathrm{H_2O}$ band. WASP-17 b at the top has the most negative $\Delta Z_{\rm UB-LM}$ and shows Na and $\mathrm{H_2O}$ absorption; WASP-6 b at the bottom has the largest value and is aerosol-dominated, with a smooth slope across the optical. The diversity of cloud cover at otherwise similar planet temperatures and gravities is one of the central questions of hot Jupiter atmospheric physics.
```

```{figure} figures/gj1214b_clouds.avif
:align: center
:name: fig:gj1214
:width: 80%

Featureless transmission spectrum of the warm sub-Neptune **GJ 1214 b** from {cite:t}`Kreidberg2014`, showing how high-altitude clouds (or hazes) can completely erase atmospheric absorption features even with high-precision HST data. Three cloud-free model atmospheres ($\mathrm{H_2O}$, $\mathrm{CH_4}$, $\mathrm{CO_2}$) are ruled out at high significance, including the high-mean-molecular-weight (water-rich) case, so the flat spectrum requires an optically thick cloud or haze layer at high altitude.
```

### Emission spectroscopy and phase curves

**Emission spectroscopy** observes planetary thermal radiation during **secondary eclipse**, when the planet passes behind the star.
The flux drop yields the dayside **brightness temperature**, the equivalent blackbody temperature.
A **phase curve** tracks orbital brightness, where day-night contrast reveals heat redistribution efficiency ({numref}`fig:wasp43`).

```{figure} figures/wasp43b_phase_curve.avif
:align: center
:name: fig:wasp43
:width: 90%

JWST MIRI **phase curve** of the hot Jupiter **WASP-43 b**, from {cite:t}`Bell2024`. The top panel is the spectroscopic phase curve as a function of wavelength and orbital phase. The middle panel is the band-integrated white light curve, showing one transit, two secondary eclipses, and the smooth phase modulation of the planet's thermal flux as the dayside rotates in and out of view. The bottom panels are the dayside and nightside emission spectra and best-fit blackbody models. The retrieved nightside temperature is much colder than the dayside, evidence of a strong day-night contrast despite an atmosphere thick enough to imprint clear spectral features on the dayside.
```

Combining transmission, emission, and phase curves constrains atmospheric thermal structure, composition, and circulation.

### JWST era results (2022--2025)

The James Webb Space Telescope has transformed exoplanet atmospheric characterisation since mid-2022.
Transmission spectroscopy of the hot Saturn WASP-39 b revealed $\mathrm{H_2O}$, $\mathrm{CO_2}$, Na, and CO, while the absence of $\mathrm{CH_4}$ indicates super-solar metallicity {cite:p}`Rustamkulov2023,Alderson2023` ({numref}`fig:wasp39prism`, {numref}`fig:wasp39species`).

```{figure} figures/wasp39b_prism_spectrum.avif
:align: center
:name: fig:wasp39prism
:width: 90%

The JWST/NIRSpec PRISM transmission spectrum of **WASP-39 b**, from Figure 4 of {cite:t}`Rustamkulov2023`. The horizontal axis is wavelength from $0.5$ to $5.5$ $\mu$m and the vertical axis is transit depth in per cent. Black points with $1\sigma$ error bars are the measured transit depths and the grey line is the best-fitting model from the PICASO 3.0 grid. Each shaded colour is the opacity contribution of one species to that model, in the legend order Na, K, $\mathrm{H_2O}$, $\mathrm{H_2S}$, $\mathrm{CO_2}$, $\mathrm{CH_4}$, CO, $\mathrm{SO_2}$, and clouds. A shaded band is a model contribution, not by itself a detection: the data support $\mathrm{H_2O}$ ($33\sigma$, the four bands between $1$ and $2.2$ $\mu$m), $\mathrm{CO_2}$ ($28\sigma$, the tall violet band at $4.3$ $\mu$m), the grey cloud deck ($21\sigma$, the flat grey floor), Na ($19\sigma$, the narrow yellow feature at $0.58$ $\mu$m), and CO ($7\sigma$, near $4.7$ $\mu$m), while the K, $\mathrm{H_2S}$, and $\mathrm{CH_4}$ contributions in the model are not favoured by the data. The detector saturates to varying degrees between $0.8$ and $1.9$ $\mu$m.
```

The detection of $4$ $\mu$m absorption from $\mathrm{SO_2}$ is the first identification of a **photochemical product**, a molecule generated by stellar irradiation rather than thermochemical equilibrium, in an exoplanet atmosphere {cite:p}`Tsai2023` ({numref}`fig:wasp39so2`).
The signal is modest in each instrument ($2.7\sigma$ to $4.8\sigma$), and the case rests on two instruments seeing the same feature and on four photochemistry codes reproducing it.
Its formation requires ultraviolet photolysis of $\mathrm{H_2S}$ followed by oxidation of sulfur to SO and $\mathrm{SO_2}$.

```{figure} figures/wasp39b_so2_spectrum.avif
:align: center
:name: fig:wasp39so2
:width: 90%

Terminator-averaged theoretical transmission spectra of WASP-39 b from photochemical models, from Figure 3 of {cite:t}`Tsai2023`. Every panel plots transit depth in per cent against wavelength in $\mu$m, and each panel shows the same four photochemistry codes, VULCAN (blue), KINETICS (orange), ARGO (green), and ATMO (red). The panels differ by wavelength range and by the data they are compared against. Panel a is the NIRSpec PRISM measurement (grey points), panel b the NIRSpec G395H measurement, and panel c the existing HST and VLT/FORS2 optical data, where the dashed blue curve is the same VULCAN model run without sulfur species and shows how much of the near-ultraviolet opacity the sulfur chemistry supplies. Panel d is a prediction rather than a comparison: the MIRI range from $5$ to $15$ $\mu$m, with the grey curve the VULCAN model with $\mathrm{SO_2}$ removed, so the separation between grey and coloured is the $\mathrm{SO_2}$ contribution. All four codes reproduce the strength and the shape of the $4.05$ $\mu$m $\mathrm{SO_2}$ feature, and all predict stronger $\mathrm{SO_2}$ bands near $7.5$ and $8.7$ $\mu$m that MIRI can reach.
```

```{figure} figures/wasp39b_alderson_species.avif
:align: center
:name: fig:wasp39species
:width: 80%

Contribution of individual opacity sources to the JWST/NIRSpec G395H transmission spectrum of WASP-39 b, from Figure 4 of {cite:t}`Alderson2023`. Panel a is the full spectrum. Grey points with error bars are the measurement, the black curve is the best-fitting model with an injected $\mathrm{SO_2}$ volume mixing ratio of $10^{-5.6}$, and each coloured curve is that same model with one opacity source removed: cloud, $\mathrm{CH_4}$, $\mathrm{H_2O}$, $\mathrm{SO_2}$, $\mathrm{CO_2}$, or CO. The left axis is transit depth in per cent and the right axis is the same quantity in planetary scale heights; the horizontal axis is wavelength in $\mu$m. The wavelength range where a coloured curve separates from the black one is the range in which that species absorbs. Panel d is the $\mathrm{CO_2}$ band near 4.3 $\mu$m on its own: black points are the measurement and the shaded orange region is the difference that the $\mathrm{CO_2}$ opacity makes to the model. The band is detected at $28.5\sigma$, above the $21.5\sigma$ of $\mathrm{H_2O}$ and the $4.8\sigma$ of $\mathrm{SO_2}$ in the same spectrum.
```

For TRAPPIST-1 b, 15 $\mu$m thermal emission is consistent with a **bare rock dayside** or a very thin atmosphere, an airless surface in radiative equilibrium with no atmospheric heat redistribution {cite:p}`Greene2023` ({numref}`fig:trappist1beclipse`, {numref}`fig:trappist1bemiss`).
This measurement rules out a thick $\mathrm{CO_2}$ atmosphere.

```{figure} figures/trappist1b_eclipse.avif
:align: center
:name: fig:trappist1beclipse
:width: 90%

JWST MIRI 15 $\mu$m secondary eclipse light curve of **TRAPPIST-1 b**, from {cite:t}`Greene2023`. The eclipse depth $f_p / f_\star = 861 \pm 99$ ppm corresponds to a dayside brightness temperature of $T_B = 503^{+26}_{-27}$ K, consistent with a bare rock dayside in radiative equilibrium with the stellar flux and no significant heat redistribution. This is the **first** thermal emission detection of an Earth-sized exoplanet.
```

```{figure} figures/trappist1b_emission.avif
:align: center
:name: fig:trappist1bemiss
:width: 90%

The TRAPPIST-1 b dayside emission compared with model atmospheres of different compositions, from {cite:t}`Greene2023`. The data are inconsistent with thick $\mathrm{CO_2}$ + $\mathrm{N_2}$ atmospheres and inconsistent with $\mathrm{O_2}$ + $\mathrm{CO_2}$ atmospheres at any plausible mass-loading. They are consistent with a bare-rock dayside (the 503 K blackbody curve, magenta).
```

Observations of TRAPPIST-1 c by {cite:t}`Zieba2023` similarly rule out a thick $\mathrm{CO_2}$ envelope ({numref}`fig:trappist1c`).
TRAPPIST-1 b and c therefore lack thick atmospheres capable of redistributing heat, although a thin atmosphere on c is not yet ruled out.

```{figure} figures/trappist1c_grid.avif
:align: center
:name: fig:trappist1c
:width: 90%

Grid of model atmospheric compositions for **TRAPPIST-1 c** compared with the measured 15 $\mu$m secondary eclipse depth, from {cite:t}`Zieba2023`. The colour-coded grid shows expected eclipse depths as a function of $\mathrm{CO_2}$ partial pressure (rows) and total atmospheric thickness (columns). Models with $\geq 0.1$ bar of $\mathrm{CO_2}$ are inconsistent with the data; models with no atmosphere or with very thin atmospheres match. A Venus-analogue thick $\mathrm{CO_2}$ atmosphere on TRAPPIST-1 c is ruled out.
```

Flat transmission spectra for LHS 475 b {cite:p}`LustigYaeger2023` and GJ 1132 b further indicate that small rocky M dwarf planets generally lose their atmospheres to early stellar activity ({numref}`fig:lhs475`).
A tentative water signal on GJ 486 b remains ambiguous due to stellar starspots {cite:p}`Moran2023`.

```{figure} figures/lhs475b_spectrum.avif
:align: center
:name: fig:lhs475
:width: 90%

JWST/NIRSpec G395H transmission spectrum of the rocky exoplanet **LHS 475 b**, an Earth-size M dwarf planet at $\sim 12$ pc, from {cite:t}`LustigYaeger2023`. The data are flat and featureless. Hydrogen-helium-dominated atmospheres are ruled out at high confidence (top panel). A pure $\mathrm{CH_4}$ atmosphere is also ruled out, though a pure $\mathrm{CO_2}$ Venus-like atmosphere is marginally consistent (bottom panel). The result is consistent with no detectable atmosphere on LHS 475 b.
```

Secondary eclipse observations of the hot rocky super-Earth 55 Cancri e by {cite:t}`Hu2024` show a dayside cooler than expected for bare rock ({numref}`fig:55cnce`).
This provides tentative evidence for a **secondary atmosphere**, a volatile envelope outgassed from a molten surface.

```{figure} figures/55cnce_hu_emission.avif
:align: center
:name: fig:55cnce
:width: 90%

JWST/NIRCam plus MIRI thermal emission spectrum of **55 Cancri e** from {cite:t}`Hu2024`. Black points are the binned JWST data; coloured curves are atmospheric models (grey blackbody, $\mathrm{CO_2}$+$\mathrm{N_2}$ purple, $\mathrm{CO_2}$+CO red, CO-only gold). The data fall below the bare-rock blackbody at most wavelengths and favour atmospheric models with non-negligible CO and $\mathrm{CO_2}$. A companion retrieval (not shown) constrains the volatile mixing ratios but is sensitive to the assumed background gas, so the conclusion of a secondary atmosphere is currently tentative but suggestive.
```

JWST observations of the ultra-short-period rocky planet TOI-561 b show only marginal evidence for a thin atmosphere or surface signal.

The habitable-zone sub-Neptune K2-18 b exhibits $\mathrm{CH_4}$ and $\mathrm{CO_2}$ alongside a marginal $2\sigma$ detection of **dimethyl sulfide** (DMS), a volatile produced on Earth by marine phytoplankton, with the significance dropping further under alternative retrieval assumptions {cite:p}`Madhusudhan2023` ({numref}`fig:k218b`).
This was initially interpreted as evidence for a **hycean world**, a sub-Neptune with a hydrogen-rich atmosphere overlying a liquid-water ocean.

```{figure} figures/k218b_spectrum.avif
:align: center
:name: fig:k218b
:width: 90%

JWST transmission spectrum of **K2-18 b** from {cite:t}`Madhusudhan2023`, combining NIRISS SOSS and NIRSpec G395H data. The black points are the data and the colour-coded model spectrum shows contributions from $\mathrm{CH_4}$, $\mathrm{CO_2}$, and tentatively dimethyl sulfide (DMS). The $\mathrm{CH_4}$ and $\mathrm{CO_2}$ detections are robust; the DMS feature is at the edge of the JWST sensitivity floor and is heavily dependent on the retrieval assumptions. The interpretation is contested.
```

Subsequent reanalyses disputed the DMS detection, showing the data are also consistent with an uninhabitable mini-Neptune {cite:p}`Wogan2024`, with an interior too hot to hold a liquid water ocean {cite:p}`Glein2024`, or with an atmosphere overlying a **magma ocean**, a molten interior that depletes $\mathrm{NH_3}$ by dissolving nitrogen {cite:p}`Shorttle2024`.
Like past debates over Martian methane and Venusian phosphine ({ref}`Lecture 6 <lecture06>`), K2-18 b illustrates how tentative biosignature claims undergo community scrutiny and revision.

JWST has also expanded **direct imaging**, the spatial separation of planetary light from stellar glare, to obtain mid-infrared spectra of self-luminous giant planets.

### The habitable zone revisited

The **classical habitable zone** is the range of stellar fluxes where a rocky planet can maintain liquid surface water ({ref}`Lecture 9 <lecture09>`).
{cite:t}`Kasting1993` identified two boundaries using a one-dimensional radiative-convective model.
The **inner edge** is set by the **runaway greenhouse limit**: rising water vapour caps outgoing longwave radiation at $280$ to $310$ W/m$^2$, evaporating the ocean.
For a Sun-like star, this occurs at $\sim 1.06$ times Earth's flux ($\sim 0.97$ AU), with the conservative moist greenhouse limit at $\sim 0.99$ AU.
The **outer edge** is set by the **maximum $\mathrm{CO_2}$ greenhouse**, where $\mathrm{CO_2}$ condenses into ice clouds and greenhouse warming saturates.

```{figure} figures/kopparapu_hz.avif
:align: center
:name: fig:kopparapu
:width: 80%

The **classical habitable zone** as a function of stellar effective temperature and effective stellar flux, from {cite:t}`Kopparapu2013`. The green-shaded region is the habitable zone bounded on the inside by the moist greenhouse limit and on the outside by the maximum $\mathrm{CO_2}$ greenhouse limit. Symbols mark known potentially habitable exoplanets including GJ 581 d/g, GJ 667C c, Kepler-22 b, Tau Ceti e/f, and the solar system planets Earth, Venus, and Mars. The "Recent Venus" and "Early Mars" empirical limits are shown by the dotted boundaries.
```

{cite:t}`Kopparapu2013` updated these 1D boundaries across stellar effective temperatures, including M dwarfs ({numref}`fig:kopparapu`).
Two important caveats apply to these classical estimates.

First, evolutionary history matters rather than snapshot conditions alone.
A planet in the habitable zone today may have suffered early runaway greenhouse desiccation ({ref}`Lecture 9 <lecture09>`).
M dwarf planets spend hundreds of Myr in runaway greenhouse conditions during the pre-main-sequence phase, potentially losing their water inventory {cite:p}`LugerBarnes2015`.
Habitability is therefore a trajectory through climate space rather than a static present-day line.

Second, one-dimensional calculations neglect three-dimensional circulation and cloud feedbacks.
General circulation models show that cloud feedbacks shift boundaries by 5 to 20% depending on rotation rate, atmospheric composition, and surface albedo {cite:p}`Way2016,Turbet2021`.
For tidally locked M dwarf planets, substellar clouds extend the inner edge to fluxes well above the 1D moist greenhouse limit.
The classical habitable zone is thus a first-order screening tool rather than a precise boundary.

### Biosignature gases and the challenge of false positives

Atmospheric biosignatures are classically identified through **disequilibrium gas combinations**, mixtures of reactive gases that cannot persist without continuous biological replenishment.
On modern Earth, the coexistence of $\mathrm{O_2}$ ($\sim 21\%$) and $\mathrm{CH_4}$ ($\sim 1.8$ ppm) is the canonical example, because both react photochemically within decades and require continuous biological production.
On early Earth before the Great Oxidation Event around 2.4 Ga, analogous combinations included $\mathrm{CH_4}$ + $\mathrm{N_2O}$ or $\mathrm{CH_4}$ + $\mathrm{CO_2}$ in a low-$\mathrm{O_2}$ atmosphere.
Classical biosignature gases include $\mathrm{O_2}$, $\mathrm{O_3}$, $\mathrm{CH_4}$, and $\mathrm{N_2O}$, though a single gas in isolation almost never constitutes a biosignature.

The central challenge in biosignature detection is **false positives**, abiotic processes that mimic biological gas signatures.
{cite:t}`Wordsworth2014` showed that water vapour photolysis followed by hydrogen escape can build up substantial abiotic $\mathrm{O_2}$ on dry planets around M dwarfs.
Likewise, $\mathrm{CO_2}$ photolysis in dry atmospheres produces abiotic $\mathrm{O_2}$ by splitting $\mathrm{CO_2}$ into CO and O, driven by stellar XUV irradiation.
Abiotic $\mathrm{CH_4}$ can similarly arise from volcanic outgassing, hydrothermal serpentinisation reactions, and impact shocks ({ref}`Lecture 10 <lecture10>`).

Biosignature identification is fundamentally an **inverse problem**, where an observed atmospheric composition must be tested against every plausible abiotic mechanism.
A biological interpretation is convincing only if all known abiotic pathways are demonstrably insufficient.
The debate over DMS on K2-18 b illustrates this difficulty: the absence of an abiotic source on Earth does not rule out unknown abiotic production pathways under exoplanet conditions.

### Comparative payoff: the solar system in the exoplanet landscape

Whether the solar system is typical has been an open question since {ref}`Lecture 1 <lecture01>`.
If "typical" means the most common configuration in the bias-corrected exoplanet archive, the answer is no.
The most common stars are M dwarfs rather than G dwarfs like the Sun.
The most common planet class is the **sub-Neptune** ($2$ to $3\,\Rearth$), which the solar system lacks between Earth ($1\,\Rearth$) and Neptune ($3.88\,\Rearth$).
Inner exoplanet systems often form compact **peas-in-a-pod** configurations ($\sim 5$ to $8$ similarly sized planets within $\sim 0.2$ AU), whereas the solar system has four irregularly spaced terrestrial planets out to $1.5$ AU.
The solar system also lacks hot Jupiters or hot Neptunes, and its giant planets occupy wide ($\geq 5$ AU), nearly circular orbits rather than eccentric paths.

However, the observed archive is shaped by detection biases that work against finding solar system analogues.
A Jupiter analogue at $5$ AU produces a radial velocity signal of $\sim 12$ m/s with a 12-year period, requiring more than a decade to detect (fewer than a hundred are known).
Saturn analogues at $9.5$ AU and Earth analogues at 1 AU around Sun-like stars sit at the edge of current sensitivity.
Whether the solar system is truly rare or merely undersampled in parameter space remains an open question.

Over the next decade, Gaia DR4 and DR5 astrometry of long-period giant planets and PLATO photometry of Earth analogues around Sun-like stars should resolve this question.
The full discussion will return in {ref}`Lecture 14 <lecture14>`.

### Frontier missions, part 1: surveys and atmospheres (2026--2035)

Upcoming exoplanet missions scheduled for launch in 2026 to 2030 focus on survey photometry, microlensing, and atmospheric spectroscopy of extended target samples.

**PLATO** (PLAnetary Transits and Oscillations of stars) is an ESA mission scheduled for launch in January 2027 {cite:p}`Rauer2014`.
Using 26 cameras as a multi-aperture photometric array, PLATO will monitor bright Sun-like stars over 2 to 3 year baselines to detect Earth analogues in the habitable zones of G dwarfs.
These bright targets enable radial velocity follow-up for mass measurements, while asteroseismic measurements of stellar oscillations provide precise host star radii and ages to constrain planet radii.

**Ariel** (Atmospheric Remote-sensing Infrared Exoplanet Large-survey) is an ESA mission scheduled for launch in 2029 {cite:p}`Tinetti2018`.
Ariel will survey approximately 1000 exoplanet atmospheres using transmission and emission spectroscopy at $1.25$ to $7.8\,\mu$m and optical photometry at $0.5$ to $1.2\,\mu$m.
Unlike JWST, which observes few targets in depth, Ariel provides a statistical census of atmospheric composition from hot Jupiters to warm sub-Neptunes at moderate depth.

**The Nancy Grace Roman Space Telescope** is a NASA flagship launched in August 2026 with a 2.4 m mirror and a $100\times$ larger field of view than HST.
Its Galactic bulge microlensing survey will deliver $\sim 1400$ bound exoplanets at separations of $\sim 0.5$ to $10$ AU down to lunar masses {cite:p}`Penny2019`, alongside free-floating rogue planets.
Its coronagraph instrument will demonstrate direct imaging technology for precursor HWO-class observations, achieving contrasts of $10^{-8}$ to $10^{-9}$ on bright nearby stars at visible wavelengths.

### Frontier missions, part 2: direct imaging of Earth analogues (2030s--2040s)

The **Habitable Worlds Observatory** (HWO) is a planned $\sim 6$ m NASA flagship space telescope targeted for launch in the 2040s {cite:p}`NAS2021`.
Using a coronagraph or external starshade to achieve contrasts of $10^{-10}$ at sub-arcsecond separations from nearby Sun-like stars, HWO will directly image and obtain spectra of approximately $25$ Earth analogues to search for atmospheric biosignatures.

The **Large Interferometer For Exoplanets** (LIFE) is a proposed European mission designed to detect thermal emission from terrestrial exoplanets {cite:p}`Quanz2022`.
LIFE is a mid-infrared **nulling interferometer**, a system of four collector spacecraft feeding a central beam combiner to suppress starlight by destructive interference in the $4$ to $18\,\mu$m range.
By observing thermal emission rather than reflected starlight, LIFE targets key absorption features of $\mathrm{CO_2}$, $\mathrm{O_3}$, $\mathrm{H_2O}$, $\mathrm{CH_4}$, and $\mathrm{N_2O}$ under favourable contrast conditions ({numref}`fig:lifeyield`).

```{figure} figures/life_yield.avif
:align: center
:name: fig:lifeyield
:width: 80%

Sensitivity of the predicted **LIFE** detection yield to the wavelength range of the mid-infrared nulling interferometer, from {cite:t}`Quanz2022`. Each panel shows the *change* in detectable planets per category (rocky habitable-zone, exo-Earth candidates, rocky+super-Earth, sub-Neptune, sub-Jovian), split by hot/warm/cold instellation, relative to the LIFE baseline configuration. **Top**: extending the band to $3$--$20\,\mu$m adds modest numbers of detections across most categories. **Bottom**: restricting the band to $6$--$17\,\mu$m removes a comparable number, with the rocky+super-Earth bin most affected. The headline absolute-yield prediction (not shown) of the same Scenario 2 calculation is that LIFE detects of order tens of rocky planets in the conservative habitable zones of nearby host stars; M dwarfs dominate the yield because they are nearby and abundant, while FGK dwarfs contribute the more solar-system-like targets.
```

Ground-based **Extremely Large Telescopes** (ELTs) are observatories designed to combine high-contrast imaging with high-resolution near-infrared spectroscopy.
The ELT class will complement HWO and LIFE by resolving habitable-zone planets around the closest M dwarfs, such as Proxima Centauri b.

Collectively, these missions push the field from **statistical demography** (population surveys of detected planets) toward the individual atmospheric characterisation of Earth analogues.

### Open questions for the next lecture

A central open question is what constitutes a convincing detection of life on another world.
It is debated whether a single biosignature gas, gas abundance ratios, seasonal cycles, or photosynthetic surface features are sufficient.
The answer depends on how much we trust atmospheric models and catalogues of false positives.
While planned missions use different definitions of convincing, none is universally agreed upon.
{ref}`Lecture 14 <lecture14>` addresses how to move from a candidate biosignature to detecting life.

## Summary

- Exoplanet science went from the first confirmed detection in 1992 to more than 6000 confirmed planets by 2026, a complete observational revolution in three decades.
- **Each detection method has a distinct bias**, and the observed planet population reflects the union of those biases as much as it reflects the underlying distribution. Radial velocity finds short-period giants around bright quiet stars; transits find short-period and large $R_p / R_\star$ systems; direct imaging finds wide-orbit young hot giants; astrometry will find Jupiter analogues; microlensing finds 1--10 AU planets at kpc distances.
- The combined transit-plus-radial-velocity measurement breaks the $m \sin i$ degeneracy and gives bulk densities, the central observational quantity that turns exoplanet detections into physical objects with measurable composition.
- **Kepler showed that planets are common.** Most main-sequence stars host at least one planet, and the small-planet population dominates by number. Hot Jupiters occur around only $\sim 1\%$ of Sun-like stars.
- The **radius valley** at $\sim 1.8\,\Rearth$ is the defining empirical feature of small-planet demographics. It points to atmospheric mass loss (photoevaporation and core-powered) as a universal sculptor of the close-in planet population, and means that many of today's super-Earths are the bare cores of former sub-Neptunes.
- The **hot Neptune desert**, the **peas-in-a-pod** correlation, and the **TRAPPIST-1** resonant chain are the other three central architectural results that any planet formation theory must explain.
- **JWST has moved exoplanet atmospheric characterisation from a promise to a routine capability.** WASP-39 b $\mathrm{SO_2}$ is the first photochemical product identified in an exoplanet atmosphere. TRAPPIST-1 b/c rule out thick $\mathrm{CO_2}$ atmospheres on close-in M dwarf rocky planets. 55 Cancri e and TOI-561 b are tentative detections of secondary atmospheres on rocky planets around Sun-like and metal-poor hosts. K2-18 b is the textbook case study in how biosignature claims are tested and revised.
- **The solar system is not obviously typical**: it lacks sub-Neptunes, lacks compact inner-system architecture, lacks hot giants, and has wide low-eccentricity outer giants. Whether it is rare or simply undersampled is the central observational question of the next decade.
- **Habitability is a history-dependent trajectory**, not a snapshot line on the HR diagram, and biosignature detection is an inverse problem with unavoidable false-positive challenges.
- The 2026--2040 mission queue (PLATO, Ariel, Roman, HWO, LIFE, ELTs) will push the field from statistical demography to individual characterisation of potentially habitable worlds. The forward question of what constitutes convincing life detection is taken up in {ref}`Lecture 14 <lecture14>`.

## References

```{bibliography}
:filter: docname in docnames
```
