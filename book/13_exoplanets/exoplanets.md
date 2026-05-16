(lecture13)=
# Lecture 13: Exoplanets, Detection Methods, Demographics & Characterisation

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

Exoplanet science is younger than most of the students taking this course.
The first confirmed planets outside the solar system were announced in 1992 by Aleksander Wolszczan and Dale Frail, who used the radio pulsar **PSR B1257+12** as a precision clock {cite:p}`Wolszczan1992`.
Pulsars are the rapidly spinning, highly magnetised remnants of massive stars that have already gone supernova.
The precision of their pulse arrival times rivals the best atomic clocks, and any unmodelled motion of the pulsar around a system barycentre shows up as a small periodic shift in those arrival times.
The original 1992 *Nature* announcement reported two planets with minimum masses of about $2.8$ and $3.4\,\Mearth$ (assuming coplanar orbits) in $66$ and $98$ day orbits around the pulsar. The subsequent analysis by {cite:t}`Wolszczan1994`, which detected the predicted near-3:2 mutual gravitational perturbation between the two bodies, confirmed these mass estimates (final values $3.4/\sin i\,\Mearth$ and $2.8/\sin i\,\Mearth$, with orbital inclinations greater than 60 degrees) and additionally revealed a much smaller third body of about $0.015\,\Mearth$ (roughly a lunar mass) in a $25.34$-day orbit.
These were not the planets anyone was looking for.
They are the survivors, or perhaps the second-generation products, of a supernova explosion.
They remain a striking reminder that planets can form, or at least exist, in environments that have nothing to do with the textbook picture of star and disk we developed in {ref}`lecture02`.

Three years later Michel Mayor and Didier Queloz used the ELODIE spectrograph at the Observatoire de Haute-Provence to detect a planet around an ordinary main-sequence star, **51 Pegasi b** {cite:p}`MayorQueloz1995`.
This is the discovery for which they shared the 2019 Nobel Prize in Physics.
The planet had roughly half the mass of Jupiter, but the orbital period was a stunning 4.23 days.
A Jupiter-mass body so close to its star contradicted every textbook picture: gas giants were supposed to form beyond the ice line at several AU, where ice could condense and provide raw material for the runaway accretion phase {cite:p}`Pollack1996`.
Either 51 Peg b had formed in situ in a way nobody had imagined, or it had formed at large distance and **migrated inward**.
The migration interpretation won out within a few years and reshaped planet-formation theory; the modern picture of disk-driven Type I and Type II migration was largely a response to the existence of close-in giants like 51 Peg b (recap from {ref}`lecture02`).
A single object, found because it happened to be unusually easy to detect, redirected the entire field.

```{figure} figures/hd209458b_first_transit.avif
:align: center
:name: fig:hd209458b
:width: 70%

The first ground-based detection of a transiting exoplanet, **HD 209458 b**, observed with the STARE photometer over two nights in September 1999. Each successive transit dropped the relative flux of the host star by approximately 1.7 per cent, exactly the depth predicted from the radial velocity mass and an inferred Jupiter-like radius. From {cite:t}`Charbonneau2000`; an independent simultaneous detection was reported by {cite:t}`Henry2000`. After this point exoplanets were no longer abstract Doppler signals: they were physical objects whose sizes could be measured directly.
```

After 1995 the field grew explosively.
Ground-based radial velocity surveys at Lick, Keck, La Silla, and elsewhere expanded the catalogue from one object to a few hundred over the following decade.
The first transit detection of an already-known radial velocity planet, HD 209458 b in 1999, was a watershed: combining transit depth and radial velocity gave the first **bulk density** of an extrasolar world, confirming that hot Jupiters were indeed gas-dominated and not exotic high-density objects {cite:p}`Charbonneau2000,Henry2000` ({numref}`fig:hd209458b`).
The space-based transit era opened with the French-led **CoRoT** mission in 2006 and exploded with NASA's **Kepler** mission in 2009, which monitored about 150,000 stars continuously for four years {cite:p}`Borucki2010`.
The K2 extension (2014--2018), TESS (2018--present), CHEOPS (2019--present), and JWST (2022--present) followed.
By 2026 the **NASA Exoplanet Archive** records more than 6000 confirmed exoplanets in roughly 4000 planetary systems {cite:p}`NASAExoArchive2025`.
Exoplanetary science went from zero confirmed cases to a statistically meaningful population in barely three decades, and the rate of discovery is still accelerating.

### Radial velocity method

The method that found 51 Peg b is conceptually straightforward.
A planet of mass $m_p$ does not orbit a stationary star.
Instead, both the star (mass $M_\star$) and the planet orbit their common centre of mass, the **barycentre**.
The star's orbit around the barycentre is small but not zero, with radius $a_\star = (m_p / M_\star)\,a_p$.
For a Jupiter analogue around a Sun-like star this is about one solar radius; for an Earth analogue it is closer to a hundredth of a solar radius.
The motion of the star can be detected as a periodic shift in the wavelengths of stellar absorption lines via the Doppler effect: when the star is moving towards us its lines blueshift, and when it is moving away they redshift.
The observable is the line-of-sight component of the stellar velocity, and the time series traces a periodic curve from which orbital period $P$, eccentricity $e$, and semi-amplitude $K_\star$ can be extracted.

For a circular orbit and an edge-on geometry the semi-amplitude takes the compact form

$$
K_\star = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{(M_\star + m_p)^{2/3}} \frac{1}{\sqrt{1 - e^2}},
$$

which is derived from Kepler's third law and conservation of momentum (we step through this derivation in the blackboard section below).
Plugging in numbers gives a sense of scale.
A Jupiter analogue around the Sun produces a stellar reflex velocity of about $K_\star \approx 12.5$ m/s.
A Saturn at $9.5$ AU produces about $2.7$ m/s.
An Earth at 1 AU produces about $0.09$ m/s, roughly nine centimetres per second.
A "true Earth twin" lies at the very edge of what current radial velocity instruments can hope to detect even in principle, and well below what is currently achievable around any but the very brightest, quietest stars.

The instrumental sensitivity floor has improved by roughly two orders of magnitude over the past three decades.
ELODIE, the spectrograph that found 51 Peg b, achieved about 10 m/s precision.
HARPS, commissioned at La Silla in 2003, reached about 1 m/s with stabilised optics, evacuated optical paths, and simultaneous wavelength reference {cite:p}`Mayor2003`.
ESPRESSO, installed on the VLT in 2018 and combining four 8-m unit telescopes, has demonstrated photon-noise-limited single-exposure precision at the 10 cm/s level and long-term repeatability of about 0.5 m/s on the quietest standards {cite:p}`Pepe2021`.
That number is no longer limited by photon statistics or by the spectrograph itself.
It is limited by **stellar noise**: the granulation, oscillations, and starspot rotation of the photosphere of the host star itself produce velocity jitter at the 10 cm/s to 1 m/s level even on the quietest, most slowly rotating stars.
Reducing this stellar contribution, by simultaneous activity diagnostics or by very long observing baselines, is now the central technical problem of precision radial velocity work.

The radial velocity method has a fundamental degeneracy.
The Doppler shift gives $K_\star$, and from $K_\star$ we infer $m_p \sin i$, where $i$ is the orbital inclination relative to the line of sight.
For a face-on system $i = 0$ and $\sin i = 0$, so a real planet would produce no signal at all.
For an edge-on system $i = 90^\circ$ and $\sin i = 1$, recovering the true mass.
With radial velocities alone we cannot distinguish a low-mass planet seen edge-on from a more massive planet seen at an inclined orbit.
This is the famous **$m \sin i$ degeneracy**.
It can be broken if we have an independent measurement of the inclination, for instance from a transit (which constrains $\sin i \approx 1$ to within the impact parameter), from astrometry (which gives the inclination directly), or from direct imaging.
The combination of radial velocity with **any** of these methods turns the inferred minimum mass into a true mass.

Radial velocity surveys are biased toward massive planets on relatively short orbits around bright, slowly rotating, magnetically quiet host stars.
A planet that produces only a 10 cm/s signal needs to be observed for many orbital periods at high precision to be detected unambiguously.
A long-period Jupiter analogue requires at least one decade of consistent observing baseline, which is a substantial commitment.
M dwarfs and F dwarfs at the extremes of the spectral type range are harder targets: M dwarfs because they are faint at optical wavelengths and have molecular features that complicate spectral fitting, and F dwarfs because they rotate fast and have few sharp lines.
The strongest yields of pure radial velocity surveys have therefore come around quiet G and K main-sequence stars in the 5 to 10 parsec neighbourhood, where high signal-to-noise spectra can be acquired in a few minutes.

### Transit method

If the orbital plane of an exoplanet system happens to lie close to our line of sight, the planet will periodically pass in front of the stellar disk and block a small fraction of its light.
This is a **transit**.
The geometry is sketched in Figure {numref}`fig:transitgeom`.
The fraction of the stellar disk that is blocked when a planet of radius $R_p$ crosses a star of radius $R_\star$ is, to leading order, just the area ratio of the two disks:

$$
\delta = \frac{\Delta F}{F} = \left(\frac{R_p}{R_\star}\right)^2.
$$

```{figure} figures/transit_geometry.avif
:align: center
:name: fig:transitgeom
:width: 90%

Geometry of a transit. **Left:** the orbit, viewed from above, defines a "shadow band" within which an observer sees transits. The half-angle of the band is $\Theta \approx (R_\star + R_p)/r$, where $r$ is the instantaneous star-planet distance. **Right:** detail of grazing and full transits relative to the stellar limb. The probability that a randomly oriented orbit produces a visible transit scales as $R_\star / a$. From the Winn (2010) review {cite:p}`Winn2010`.
```

For a Jupiter-radius planet around a Sun-radius star, the ratio is $0.1005$, so the depth is $\delta \approx 1.01\%$ (a round "$\sim 1\%$" pedagogical value), easily measurable from the ground with a 1 metre class telescope.
For an Earth-radius planet around the Sun the ratio is $9.16 \times 10^{-3}$, so the depth is only $\delta \approx 8.4 \times 10^{-5}$, about 84 parts per million.
This is well below atmospheric noise and is only achievable from space.
For an Earth-radius planet around an M dwarf with $R_\star \approx 0.15\,\Rsun$, the ratio is much more favourable: $\delta \approx 4 \times 10^{-3}$ or 4000 ppm, accessible even from the ground.
The strong inverse scaling with stellar size is one of the reasons that small planets around M dwarfs (particularly the TRAPPIST-1 system, see below) have dominated the early atmospheric-characterisation era.

A transit is much more than just a depth.
The full light curve, sketched in Figure {numref}`fig:transitlc`, contains four characteristic times: first contact when the planet first touches the stellar limb ($t_\mathrm{I}$), second contact when the planet is fully inside the disk ($t_\mathrm{II}$), third contact when the planet starts to leave the disk ($t_\mathrm{III}$), and fourth contact when it leaves entirely ($t_\mathrm{IV}$).
The duration $T$ between second and third contact, the duration of ingress and egress (between first and second, or third and fourth), and the depth together constrain the impact parameter $b$, the inclination $i$, and (with stellar parameters) the radius $R_\star$.
The shape of the light curve is also distorted by **limb darkening**: the stellar disk is not uniformly bright but is brighter at centre and dimmer at the edge, because lines of sight near the limb intersect cooler upper layers of the photosphere.
Limb-darkened transit fits are now standard, and the residual systematics are typically dominated by the host star itself rather than by the model.

```{figure} figures/transit_lightcurve_schematic.avif
:align: center
:name: fig:transitlc
:width: 75%

Schematic of a transit light curve. The four contact times $t_\mathrm{I}$ through $t_\mathrm{IV}$ define the ingress, total duration, and egress. The depth $\delta = (R_p / R_\star)^2$ gives the planet's radius if the stellar radius is known; the duration and ingress shape constrain the impact parameter $b$ and the orbital geometry. The flat bottom assumes a uniform source; in practice the curved bottom of a real transit reveals limb darkening of the host star. From {cite:t}`Winn2010`.
```

The transit geometry imposes a strong selection effect.
A randomly oriented orbit transits only if the orbital plane is within an angle $\Theta \approx R_\star / a$ of our line of sight.
For an Earth-Sun analogue this is $\sim 0.005$, so only one in 200 randomly oriented orbits of a Sun-like star produces a visible Earth transit.
For a hot Jupiter at 0.05 AU the geometric probability rises to $\sim 0.1$, ten per cent.
This very strong bias against long-period and against small-stellar-radius systems is why the transit catalogue is dominated by short-period hot Jupiters and by M-dwarf planets, not because those are intrinsically the most common configuration. Modern transit photometry has pushed precision to the parts-per-million level: {numref}`fig:wasp39_jwst` shows the JWST/NIRSpec G395H broadband and spectroscopic light curves of the hot Saturn WASP-39 b as a representative example.

```{figure} figures/jwst_transit_lightcurve.avif
:align: center
:name: fig:wasp39_jwst
:width: 90%

Modern transit photometry pushed to its current limit. Top: raw broadband transit light curves of the hot Saturn **WASP-39 b** ($0.28\,\Mjup$) observed with JWST NIRSpec G395H detectors NRS1 and NRS2. Middle: spectroscopic light curves at each wavelength. Bottom: photometric precision per spectrophotometric channel, reaching 200--500 ppm per integration. The data quality is now well below the typical signal of an exoplanet atmospheric absorption feature. From {cite:t}`Alderson2023`.
```

The history of transit surveys is essentially a history of expanding field of view, target brightness, and time baseline.
**CoRoT** (2006--2013) was the first dedicated space transit mission and produced about 30 confirmed planets.
**Kepler** (2009--2013) and its **K2** extension (2014--2018) monitored about 150,000 stars in a single field continuously for four years and delivered the first statistically complete sample of small exoplanets {cite:p}`Borucki2010,Fressin2013`.
**TESS** (2018--present) is an all-sky survey designed to find small planets around the brightest, nearest stars where atmospheric follow-up is possible.
**CHEOPS** (2019--present) is a follow-up photometer that obtains high-precision transit light curves of known target systems for refined radius measurements.
**PLATO**, scheduled for launch in 2026, is the next ESA exoplanet mission and is designed specifically to find Earth-sized planets in the habitable zones of bright Sun-like stars over 2--3 year monitoring baselines {cite:p}`Rauer2014`.
Selection biases for these surveys are similar but not identical: Kepler favoured Sun-like stars at moderate distance, TESS favours bright nearby stars across all spectral types, and PLATO will favour bright Sun-like stars where radial-velocity follow-up is feasible.

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

The radial velocity and transit methods are both indirect: they detect the planet's effect on the star.
**Direct imaging** does what the name says.
It spatially separates the photons of the planet from the photons of the star and records them on a different part of a detector.
This is conceptually the simplest detection method but technically by far the hardest, because the contrast between a Sun-like star and a Jupiter-like reflected-light planet at 5 AU is roughly $10^{-9}$ at visible wavelengths and the angular separation is at most a few tenths of an arcsecond.
For an Earth analogue around a Sun-like star at 10 pc, the contrast is closer to $10^{-10}$ and the separation is $0.1$ arcsecond.
These are the parameters of the toughest astronomical observation ever attempted.

The technical solution combines four ingredients.
**Adaptive optics** correct atmospheric turbulence in real time using a deformable mirror driven by a wavefront sensor; the resulting image stays diffraction-limited rather than seeing-limited.
**Coronagraphs**, in their many designs (Lyot, apodised, vortex), suppress the central stellar light inside the focal plane while preserving high transmission off-axis.
**Angular differential imaging** (ADI) and **spectral differential imaging** (SDI) suppress the residual stellar speckle pattern by allowing the planet to rotate or to shift in wavelength while the residual stellar pattern stays fixed; differencing then leaves only the moving planet.
**Long integration times** averaged across many independent realisations of the speckle pattern push the noise floor below the planet flux.
Currently active high-contrast facilities include SPHERE on the VLT, GPI on Gemini, and SCExAO on Subaru on the ground, and the JWST NIRCam and MIRI coronagraphs in space.

```{figure} figures/hr8799_discovery.avif
:align: center
:name: fig:hr8799
:width: 80%

Discovery image of the **HR 8799** planetary system from {cite:t}`Marois2008`. Three of the four giant planets (b, c, d) are visible at projected separations of $24$, $38$, and $68$ AU after subtraction of the stellar PSF using angular differential imaging. The Keck and Gemini AO observations spanned 2004 to 2008. The fourth planet, HR 8799 e (at $\sim 14$ AU), was added by Marois et al.\ in 2010. The four planets have masses of roughly $5$--$10\,\Mjup$ and span orbital separations of $14$--$68$ AU. They are young, hot, self-luminous, and still cooling: this is the regime in which direct imaging works.
```

The current sensitivity of direct imaging is dominated by the planet's brightness.
Young giant planets, $\lesssim 100$ Myr old, are still radiating away the gravitational binding energy of their formation and are luminous in the infrared.
Old planets, like Jupiter, have cooled and emit a thousand times less.
The directly imaged planet population is therefore strongly biased toward young (10--500 Myr), massive ($> 1\,\Mjup$), wide-orbit ($> 10$ AU) giants around nearby stars.
Notable systems include **HR 8799**, with four giant planets around a young A-type star whose age is best estimated at $\sim 60$ Myr (formal range $30$--$160$ Myr) {cite:p}`Marois2008` ({numref}`fig:hr8799`), **$\beta$ Pictoris b/c** orbiting an A6V star embedded in the famous debris disk (system age $\sim 12$–$23$ Myr from successive Beta Pictoris Moving Group calibrations) {cite:p}`Lagrange2010` ({numref}`fig:betapic`), **51 Eridani b**, and the youngest system of all, **PDS 70 b/c**.

```{figure} figures/betapic_imaging.avif
:align: center
:name: fig:betapic
:width: 80%

The first ground-based direct image of $\beta$ Pictoris b, a $\sim 9\pm 3\,\Mjup$ planet (hot-start models) at $\sim 8$--$15$ AU from the central young A-type star. The two epochs (2003 left, 2009 right) show clear orbital motion in the projected sky position, decisively confirming a bound companion rather than a chance alignment. From {cite:t}`Lagrange2010`. The same star hosts an extensively imaged debris disk, an inner planet (b), and a more recently discovered second giant planet (c).
```

PDS 70 deserves a special mention because it is the first system in which a planet was unambiguously detected **inside the gap of a still-present protoplanetary disk** {cite:p}`Keppler2018,Haffert2019`.
The host is a 5 Myr K7 star surrounded by an obvious cleared central cavity, exactly the kind of structure predicted by models of planet-disk interaction (recap from {ref}`lecture02`).
SPHERE at near-infrared wavelengths and MUSE at H$\alpha$ emission both detected a point source inside the gap; this is PDS 70 b.
A second protoplanet, PDS 70 c, was identified in a similar position later.
Both objects are still actively accreting from the surrounding disk gas, as evidenced by the H$\alpha$ emission line that traces accretion shocks.
This is the first case in which a forming planet, its host disk, and the gap it has carved are all visible simultaneously, providing a direct test of the planet-disk-interaction models discussed in {ref}`lecture02` ({numref}`fig:pds70b`, {numref}`fig:pds70bc`, and {numref}`fig:pds70disk`).

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

Multi-epoch H$\alpha$ confirmation of two forming planets in the PDS 70 system, from {cite:t}`Haffert2019`. The strong H$\alpha$ emission of PDS 70 b and the newly discovered PDS 70 c is interpreted as accretion shock luminosity from gas falling onto the planets, providing independent dynamical and accretion-physics evidence for two simultaneously forming protoplanets in the disk gap.
```

```{figure} figures/pds70_disk.avif
:align: center
:name: fig:pds70disk
:width: 65%

Composite scattered-light image of the PDS 70 protoplanetary disk plus its two embedded planets, from {cite:t}`Haffert2019`. The outer ring is the parent disk, the cleared central cavity is the planet-carved gap, and the two white circles inside the gap mark the positions of PDS 70 b (closer to the star) and PDS 70 c (further out). This is the cleanest direct observational match between a planet-formation theory prediction (a planet inside the gap of a transition disk) and a real system in nature.
```

The direct imaging community took another step in 2023 when the JWST coronagraphs on NIRCam and MIRI delivered the first **mid-infrared spectra** of directly imaged exoplanets, including the wide-orbit objects HIP 65426 b and the planetary-mass companion VHS 1256 b.
Direct imaging is now contributing to the atmospheric-characterisation effort that we will discuss in Part 3, not just to the discovery census.

### Astrometry

The motion of a star around the system barycentre is not only a velocity along the line of sight: it is also a position in the plane of the sky.
**Astrometry** measures the angular reflex motion of the host star against background reference stars.
The expected angular amplitude is

$$
\alpha = \frac{m_p}{M_\star} \cdot \frac{a_p}{d},
$$

where $d$ is the distance to the system.
For a Jupiter analogue around the Sun seen from 10 pc, this is about half a milli-arcsecond.
For a Saturn analogue at the same distance it is about $0.16$ milli-arcseconds.
For an Earth analogue it is $0.3$ micro-arcseconds.
Astrometric exoplanet detection therefore demands microarcsecond precision over years to decades, well beyond what was achievable with ground-based imaging alone for most of the twentieth century.

The space-based mission **Hipparcos** (1989--1993) was the first attempt at systematic astrometry from space and reached about a milli-arcsecond.
This was sufficient to confirm a few stellar binary orbits and to set upper limits on planet masses, but not to actually discover exoplanets.
**Gaia**, launched in 2013, has been performing an all-sky astrometric survey of more than a billion stars at $20$--$50$ microarcsecond precision per epoch and a final precision after the full mission of $\sim 10$ microarcseconds for bright stars.
This is now the precision regime in which Jupiter analogues become accessible.

The Gaia data are released in successive **data releases** (DR).
DR2 (2018) and DR3 (2022) contained five-parameter astrometry (position, parallax, proper motion) for the full sample, plus first orbital fits for unresolved binaries and a small number of substellar companions {cite:p}`GaiaDR3`.
**DR4**, expected in late 2026, will deliver epoch-by-epoch astrometric time series for the full mission. The forecast for the nominal 5-year mission is $\sim 2 \times 10^4$ detectable astrometric exoplanet signatures (predominantly wide-orbit Jupiter analogues around nearby Sun-like stars), with the validated sample after follow-up confirmation likely to be a factor of several smaller {cite:p}`Perryman2014`.
**DR5**, expected late in the decade, will use the full ten years of mission data and is projected to push the sensitivity into the sub-Jovian regime for the closest stars.
The Gaia astrometric exoplanet catalogue will, for the first time, give a relatively unbiased census of long-period gas giants, the regime that radial velocity surveys can only reach with truly heroic decades-long observing programmes.

Astrometry is complementary to radial velocity in the most useful way possible: it directly measures the **inclination** of the orbit, breaking the $m \sin i$ degeneracy without requiring a transit.
A planet that produces both a Gaia astrometric signal and a radial velocity signal yields a true mass, an orbit inclination, and a complete three-dimensional orbital solution.
The combination is particularly powerful for the wide-orbit, Jupiter-analogue regime that is the natural sweet spot for Gaia and the natural blind spot for transit surveys.

### Microlensing

Gravitational lensing offers a fundamentally different detection mechanism.
When a foreground star (the **lens**) passes in front of a more distant background source star, the lens's gravitational field bends the source light around it, briefly amplifying the apparent brightness of the source.
The light curve of this **microlensing event** typically has a characteristic timescale of weeks to months and a smooth peak.
If the lens hosts a planet, the planet's gravity perturbs the lens's geometry and produces a small short-duration spike in the light curve, lasting hours to days, on top of the smoother stellar microlensing event.
The size of the perturbation and its position on the underlying microlensing light curve give the planet's mass and projected separation in units of the Einstein ring radius, which is itself set by the lens mass and the lens-source distance.

Microlensing is sensitive to planets at distances of kiloparsecs, far beyond the reach of any other technique.
It is also sensitive to planets at projected separations of $0.5$--$10$ AU, a regime that maps roughly onto the snow-line distances where giant planets are expected to form.
The microlensing event itself is **one-shot**: the lens-source alignment is unique and never repeats, so there is no possibility of follow-up confirmation in the same way that radial velocity or transit detections allow.
Consequences of this include a higher false-alarm rate in marginal events and the impossibility of subsequent characterisation of the host or the planet.
Active microlensing surveys include OGLE in Chile, MOA in New Zealand, and KMTNet, a three-site network in Chile, South Africa, and Australia that achieves continuous coverage of the Galactic bulge.
The **Nancy Grace Roman Space Telescope**, scheduled for launch in 2027, will conduct a dedicated microlensing survey of the Galactic bulge that is expected to find $\sim 1400$ bound exoplanets at separations of $\sim 0.5$--$10$ AU, with mass sensitivity reaching down to lunar-mass bodies {cite:p}`Penny2019`. A comparable population of free-floating, "rogue" planets unbound from any host is anticipated and will be quantified by follow-up yield analyses.

### Timing methods

When a transiting planet has a non-transiting (or differently transiting) companion in the same system, the gravitational interaction between the two perturbs the transit times of the first one in a periodic way.
These are **transit timing variations** (TTVs), and they were predicted theoretically by {cite:t}`Holman2005` before they were observed.
TTVs encode the masses of the perturber and the perturbed planet, so when both planets in a system transit, TTVs provide a **dynamical mass** measurement that does not require radial velocity follow-up at all.
This is essential for small planets around faint stars, where direct radial velocity measurement is infeasible: for instance, the seven planets of the TRAPPIST-1 system have masses derived almost entirely from TTV analysis (discussed in Part 2 below).
Notable TTV-mass systems include Kepler-11, Kepler-36, and TRAPPIST-1.

A second, older, timing method is **pulsar timing**, the technique that found the very first exoplanets {cite:p}`Wolszczan1992`.
Pulsar timing works by detecting periodic variations in the arrival times of radio pulses from a millisecond pulsar; a planet around the pulsar produces a small periodic shift in the pulse arrival times relative to the constant pulsar spin period.
The technique is extraordinarily sensitive in mass terms, in principle reaching down to lunar-mass bodies, but the sample of millisecond pulsars suitable for the technique is small.

A third timing technique exploits eclipsing binary stars.
A circumbinary planet in orbit around a close binary slightly perturbs the timing of the stellar eclipses and can also produce its own transits across both stars.
The first confirmed circumbinary transiting planet, **Kepler-16 b**, was found this way in 2011 {cite:p}`Doyle2011`, and was nicknamed "Tatooine" after the fictional binary-star planet from Star Wars.

### Detection biases summary

Each of the methods we have just reviewed picks out a different region of (mass, orbital period, host-star type, age) parameter space.
Radial velocity is most sensitive to massive planets on 1--10 year orbits around bright, slowly rotating Sun-like stars.
Transit photometry is most sensitive to short periods (less than $\sim 100$ days), large $R_p / R_\star$ ratios, and bright magnetically quiet stars.
Direct imaging is most sensitive to wide orbits ($> 10$ AU), young massive self-luminous giants, and nearby stars.
Astrometry is most sensitive to wide orbits with orbital periods comparable to the mission baseline, with a sweet spot at the Jupiter-analogue regime around nearby stars.
Microlensing is sensitive to 1--10 AU planets at any host distance but is unrepeatable.
Timing is sensitive to compact multi-planet systems (TTVs) or circumbinary configurations.

The "shape" of the **observed** exoplanet archive, the cloud of points on a period-radius or mass-period plot, reflects the union of these biases at least as much as it reflects the underlying physical distribution.
This is a critical caveat for everything that follows in Part 2: when we say that "most planets are sub-Neptunes" or "hot Jupiters are rare", we are reporting a number that has been **bias-corrected**, not the raw catalogue count.
For Kepler this bias correction is reliable because the survey was designed for it; for almost everything else it is much less certain.

## Part 2: Demographics and architectures

### The Kepler revolution and the TRAPPIST-1 laboratory

Kepler is the mission that turned exoplanet science from a discovery enterprise into a statistical enterprise.
By pointing a single 0.95 m telescope continuously at the same patch of sky in the Cygnus and Lyra constellations for four years and monitoring about 150,000 main-sequence stars at $\sim 30$ ppm photometric precision per six-hour interval, Kepler delivered a sample for which the **detection efficiency** is computable for every target and every transit signal {cite:p}`Borucki2010,Fressin2013`.
This is the prerequisite for inferring **occurrence rates**: how many planets of a given size and orbital period are present per star, regardless of whether they happened to be detected.

The headline result of Kepler is that planets are common.
Combining Kepler with later TESS results, the broad picture is that on average **at least one planet exists per main-sequence star** {cite:p}`Fressin2013,Petigura2018`, and that small planets (radii below 4 Earth radii) are by far the most common kind.
About half of all Sun-like stars host at least one such small planet on an orbit shorter than about 1 AU.
**Hot Jupiters**, by contrast, occur around only 0.5--1\% of Sun-like stars {cite:p}`Fressin2013`: they dominate the early discovery catalogue purely because they are easy to find, not because they are typical.
The fraction of Sun-like stars hosting an Earth-size planet in the habitable zone, known as $\eta_\oplus$, is harder to pin down because Earth-sized planets at 1 AU produce only a few transits over the full Kepler mission and are right at the detection floor.
Recent Kepler-DR25 estimates give central values $\eta_\oplus \sim 0.4$ for the conservative habitable zone (68% credible interval roughly $0.2$--$0.9$), depending on the precise definition of "habitable zone" and "Earth-size" {cite:p}`Bryson2021`.
Whatever the precise number, $\eta_\oplus$ is clearly not small.
Earth-class planets are an ordinary outcome of star formation, not a rare miracle ({numref}`fig:petigura` and {numref}`fig:bryson`).

```{figure} figures/petigura_occurrence.avif
:align: center
:name: fig:petigura
:width: 90%

Kepler-derived planet occurrence rates as a function of orbital period and planet size, from the California-Kepler Survey {cite:p}`Petigura2018`. Small planets are far more common than giants at every period, and the occurrence rate of small planets falls off only slowly toward longer periods. The flattening at the longest periods is partly observational (Kepler had only $\sim 4$ years of baseline), but the overall picture is that the typical Sun-like star hosts at least one small planet inside 1 AU.
```

```{figure} figures/bryson_etaearth.avif
:align: center
:name: fig:bryson
:width: 594px

Marginalised differential occurrence rate of small planets from the Kepler analysis of {cite:t}`Bryson2021`. **Left**: occurrence per unit planetary radius, $\dd N / \dd R$, evaluated at $\Delta R = 0.25\,\Rearth$. **Right**: occurrence per unit instellation flux, $\dd N / \dd I$, evaluated at $\Delta I = 0.18$ (note the inverted x-axis, with low instellation on the right). Dark and light shaded bands are the 68\% and 95\% credible intervals. The observed occurrence rates give central values of $\eta_\oplus \sim 0.4$ for the conservative habitable zone, with 68\% credible intervals of roughly $0.2$--$0.9$ depending on the precise definition of habitable-zone Earth analogue. This is the range typically quoted in mission yield estimates for HWO and LIFE (see Part 3).
```

A particularly important "laboratory" target system is **TRAPPIST-1**, an ultra-cool dwarf at 12 parsecs hosting **seven** transiting Earth-sized planets in a tightly packed inner system, all within 0.06 AU {cite:p}`Gillon2017`.
The system was discovered with the ground-based TRAPPIST-South 60 cm telescope and its successor SPECULOOS, then characterised in detail with Spitzer transit photometry and TTV mass measurements.
The seven planets form a chain of mean-motion resonances, evidence of an early disk-driven migration phase that captured them into orbital lock and stabilised them long enough to survive 4 Gyr of dynamical evolution.
TRAPPIST-1 has become the central reference for several reasons: the planets are small (Earth-sized rather than mini-Neptune-sized), the host star is an M dwarf where atmospheric characterisation is geometrically favourable, several of the planets lie in or near the classical habitable zone, and the system is so geometrically well-aligned that all seven planets transit (a probability of less than $10^{-3}$ for random orientations, which suggests that compact M-dwarf systems are intrinsically very flat) ({numref}`fig:trappist1transits`). The dynamical mass measurements come from transit timing variations rather than from radial velocities, since the host is too faint at optical wavelengths for precision RV work ({numref}`fig:trappist1ttvs`).

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

The single most influential plot in modern exoplanet science is the **period-radius diagram**: orbital period on the horizontal axis (logarithmic), planetary radius on the vertical axis (logarithmic), and a point for every confirmed transiting planet.
On this single plot, several distinct populations are visible as separate clumps or bands.
The largest planets, with $R_p > 10\,\Rearth$, form an upper band of gas giants; among these, the **hot Jupiters** ($P < 10$ days) are a tight clump that dominates short-period detections.
The **warm and cold Jupiters** stretch toward longer periods.
A second well-defined population at $R_p \approx 2$--$4\,\Rearth$ is the **sub-Neptune** or "mini-Neptune" group, which has no analogue in the solar system.
A third population at $R_p \approx 1$--$1.8\,\Rearth$ is the **super-Earth** group: rocky planets larger than Earth but smaller than Neptune.
The **terrestrial analogue** regime, $R_p \lesssim 1.5\,\Rearth$ at periods longer than $\sim 100$ days, is largely unexplored because of detection difficulty: this is exactly the regime PLATO is designed to populate ({numref}`fig:fultonpr`).

```{figure} figures/fulton_period_radius.avif
:align: center
:name: fig:fultonpr
:width: 70%

Period-radius distribution of small Kepler planets after stellar parameter refinement and bias correction, from {cite:t}`Fulton2017`. The colour scale indicates detection completeness. The clear deficit of planets at $R_p \approx 1.8\,\Rearth$ across all orbital periods is the **radius valley** or **Fulton gap**, the central empirical structure that splits the small-planet population into super-Earths and sub-Neptunes.
```

### The radius valley (Fulton gap)

In 2017, Benjamin Fulton and collaborators reanalysed the Kepler small-planet sample using high-resolution Keck/HIRES spectroscopy to refine the stellar radii and therefore the planet radii of the host stars in the **California-Kepler Survey** {cite:p}`Fulton2017`.
With smaller error bars on $R_p$, the period-radius diagram showed a clear, statistically significant **deficit** of planets at $R_p \approx 1.5$--$2\,\Rearth$.
Below the gap is a population of super-Earths peaked at $\sim 1.3\,\Rearth$.
Above the gap is the sub-Neptune population peaked at $\sim 2.4\,\Rearth$.
This bimodality is now known as the **radius valley** or **Fulton gap**, and it has become the defining demographic feature of close-in planet populations ({numref}`fig:fultongap`).

```{figure} figures/fulton_gap.avif
:align: center
:name: fig:fultongap
:width: 80%

The **radius valley**: the histogram of planet radii in the Kepler sample after stellar parameter refinement, from {cite:t}`Fulton2017`. The deficit at $R_p \approx 1.8\,\Rearth$ is the central empirical signature that splits small planets into a rocky **super-Earth** group at $\sim 1.3\,\Rearth$ (red shaded) and a volatile-rich **sub-Neptune** group at $\sim 2.4\,\Rearth$ (cyan shaded). The smooth curve is a kernel density estimator with the gap clearly resolved.
```

The physical interpretation of the gap is that close-in planets that started life with substantial hydrogen-helium envelopes have been **stripped** of those envelopes by atmospheric escape during the first hundreds of millions of years of their evolution.
A planet with a thin H/He envelope can lose it entirely and end up as a bare rocky core; a planet with a thick envelope keeps it.
The bimodal distribution we see today is the surviving population: the gap is the radius range where the post-stripping outcome is unstable, and any planet that ended in that radius range was either driven below it (becoming a super-Earth) or stayed above it (a sub-Neptune).
Two competing physical mechanisms have been proposed to drive the stripping.

The first is **photoevaporation** {cite:p}`OwenWu2013`.
Young stars emit several orders of magnitude more high-energy XUV (ultraviolet and X-ray) flux than mature stars, particularly during the first $\sim 100$ Myr.
This flux deposits energy in the upper layers of a planet's H/He envelope and drives a thermal hydrodynamic outflow.
The order-of-magnitude rate is set by **energy-limited escape**: a fraction $\epsilon \sim 0.1$ of the absorbed XUV flux is converted into the gravitational work needed to lift gas out of the planet's potential well, giving

$$
\dot{M} \approx \frac{\epsilon \, \pi F_\mathrm{XUV} R_p^3}{G M_p}.
$$

The factor of $R_p^3$ comes from the absorbing cross-section ($\pi R_p^2$) times the inverse of the specific binding energy ($G M_p / R_p$): low-density, low-mass planets are easier to strip than dense, massive ones.
For a young $10\,\Mearth$ sub-Neptune with $R_p \approx 2.5\,\Rearth$ at $0.1$ AU around a Sun-like star in its saturated XUV phase ($F_\mathrm{XUV} \sim 300$ W m$^{-2}$ at 0.1 AU, several orders of magnitude above the present-day value) and $\epsilon = 0.1$, the energy-limited rate is $\dot{M} \sim 10^{8}$ kg s$^{-1}$.
Integrated over the $\sim 100$ Myr that the host star spends in the saturated phase, the cumulative mass loss is $\sim 3 \times 10^{23}$ kg, of order a few per cent of an Earth mass and comparable to the typical primordial $\mathrm{H_2}$/He envelope mass on a $10\,\Mearth$ rocky core.
This is the physical reason why the radius valley sits near $1.8\,\Rearth$: it is the dividing radius below which the early XUV history can plausibly remove the entire primordial envelope and leave a bare rocky core, while planets above the valley retain enough envelope mass to survive.
For a close-in sub-Neptune, the integrated mass loss can therefore be enough to strip the envelope on a timescale of $\sim 100$ Myr.
{cite:t}`OwenWu2013` showed numerically that a Kepler-like population of sub-Neptunes evolved through XUV-driven mass loss reproduces the observed bimodality in planet radius ({numref}`fig:owenvalley` and {numref}`fig:owenmassloss`).

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

The second proposed mechanism is **core-powered mass loss** {cite:p}`Ginzburg2018,Gupta2019`.
A young rocky core retains the energy of its formation as latent and gravitational heat for hundreds of Myr, and the basal heat flux into the bottom of the H/He envelope is enough to drive a slow hydrodynamic outflow even without a strong external XUV input.
The rocky core's own thermal evolution sets the survival probability of any envelope on top of it.
{cite:t}`Ginzburg2018` showed that this mechanism, like photoevaporation, naturally produces a bimodal radius distribution with a gap at $\sim 1.8\,\Rearth$ ({numref}`fig:ginzburg`).

```{figure} figures/ginzburg_corepowered.avif
:align: center
:name: fig:ginzburg
:width: 80%

Core-powered mass loss model from {cite:t}`Ginzburg2018`. The figure shows the predicted radius distribution of small planets when envelope mass loss is driven by the cooling rocky interior rather than by external XUV photons. The distribution is bimodal in the same sense as photoevaporation models, with a gap at $\sim 1.8\,\Rearth$ separating bare rocky cores from sub-Neptunes that retain their envelopes.
```

A key follow-up by Vincent Van Eylen and collaborators used asteroseismic stellar radii (which are more precise than spectroscopic radii) for a sample of transiting Kepler small planets to quantify the **slope** of the radius valley with orbital period {cite:p}`VanEylen2018`.
They found that the valley shifts to smaller radius at longer orbital period, consistent with both photoevaporation and core-powered mass loss models.
The two physical mechanisms predict somewhat different slopes and somewhat different dependences on stellar mass and metallicity; current data are not yet decisive enough to discriminate between them.
The community consensus is that **both** mechanisms operate, that they predict broadly similar valleys, and that the valley itself is now the strongest individual constraint on the close-in evolution of small planets ({numref}`fig:vaneylen` and {numref}`fig:vaneylenmodels`).

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

The implication is straightforward and important.
**Many of the close-in rocky super-Earths in the Kepler sample are not "naturally" rocky planets at all.**
They are the bare cores of former sub-Neptunes whose envelopes were lost during the first hundred million years of system history.
Whether a given super-Earth was born rocky or stripped to rocky is in general impossible to tell from its present-day bulk density alone.
This has consequences for habitability discussions: a stripped sub-Neptune core has experienced a violent atmospheric history and may have very different surface and interior chemistry than a primordially rocky planet.

### The hot Neptune desert

A second well-defined feature of the close-in planet population is the **hot Neptune desert**: a striking deficit of Neptune-mass planets ($M_p \approx 10$--$100\,\Mearth$) at orbital periods shorter than about 5 days.
Hot Jupiters at the same periods are rare but not absent.
Ultra-short-period rocky planets are also rare but not absent.
But hot Neptunes, in the obvious sense of Neptune-sized planets at hot-Jupiter periods, are essentially missing.
{cite:t}`Mazeh2016` quantified the boundaries of the desert in both the period-mass and period-radius planes and showed that the empirical edges follow well-defined power laws ({numref}`fig:neptunedesert`).

```{figure} figures/mazeh_neptune_desert.avif
:align: center
:name: fig:neptunedesert
:width: 90%

The **hot Neptune desert** in the period-mass and period-radius planes from {cite:t}`Mazeh2016`. The shaded triangular region is empirically depleted of Neptune-mass planets. The upper edge follows a tight power law, plausibly set by Roche-lobe overflow on inflated hot Jupiters; the lower edge is more diffuse and has been variously attributed to photoevaporation, in-situ formation, and high-eccentricity migration with tidal circularization. The desert is one of the strongest pieces of evidence for atmospheric mass loss as a major sculptor of close-in planets.
```

The desert is interpreted as the result of two processes acting on a population formed with thick H/He envelopes but with relatively weak gravitational binding.
Photoevaporation strips the envelopes of the lower-mass population (below the desert), turning would-be hot Neptunes into bare hot super-Earths.
Roche-lobe overflow truncates the upper edge: a sufficiently inflated planet on a sufficiently close orbit fills its Roche lobe and loses additional mass through tidal stripping, depleting the heavier population from above.
The hot Neptune desert is therefore a second, independent piece of evidence that **mass loss is the dominant sculptor of close-in planet populations**, and that the planets we see today are not the same planets that formed.

### Planetary system architectures

So far we have discussed individual planets in isolation.
A separate, equally important question is what happens within multi-planet systems.
The Kepler sample contains hundreds of systems with two or more transiting planets, and these allow a statistical study of system architecture.
{cite:t}`Weiss2018` analysed the California-Kepler Survey multi-planet sample and found two striking regularities, summarised by the slogan **"peas in a pod"**: planets within the same multi-planet system tend to have similar sizes (much more similar than two random planets drawn from the full Kepler sample, {numref}`fig:weisspeas`), and they tend to be uniformly spaced in orbital period (in the sense that the period ratios of adjacent pairs in a system are clustered around a single value rather than being randomly distributed, {numref}`fig:weiss_spacing`).

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

The interpretation favoured by Weiss et al. is that compact inner systems form by a **smooth, local process** rather than by stochastic large impacts.
A formation channel dominated by giant impacts and dynamical chaos would tend to produce systems of randomly spaced planets with random sizes.
The observed regularity is more consistent with a slow growth and migration process in which neighbouring planets feel each other's gravity throughout formation and end up with similar sizes and uniform spacing.
This is a remarkable inversion of the lessons drawn from the solar system, where the late stages of terrestrial planet formation are dominated by giant impacts (compare the Earth-Moon system, recap from {ref}`lecture02`).
It may be that the inner solar system is dynamically unusual relative to typical compact systems.

Not every multi-planet system is a peas-in-a-pod arrangement.
Radial-velocity-selected samples, which include many wider, longer-period multi-planet systems, show substantially more architectural diversity than the Kepler transit sample.
There are also dramatic exceptions among Kepler systems themselves, including misaligned multi-planet systems and systems with a giant planet plus a tightly packed inner population.
The peas-in-a-pod result is a statistical statement about typical compact systems, not a universal rule.

A particularly extreme example of a compact system is the TRAPPIST-1 system already discussed above: seven Earth-sized planets in five adjacent mean-motion resonances, all interior to 0.06 AU {cite:p}`Gillon2017`.
The TRAPPIST-1 chain is the longest known resonant chain of any kind and is strong evidence for an early disk-migration phase that captured and locked the planets into resonance before the gas disk dispersed.
Two other notable resonant or near-resonant compact systems are **Kepler-90**, with eight planets, and **TOI-178**, with six planets in an unbroken resonance chain.

### Hot Jupiters and migration

We have seen that hot Jupiters are easy to find but rare in occurrence.
We also said that they cannot have formed in situ at $\sim 0.05$ AU; the temperature there is too high for ice to condense, the disk gas density too low for runaway accretion, and the timescale too short for a giant planet to assemble.
Hot Jupiters must have formed at several AU and migrated inward.
Whatever the migration mechanism, the inner edge of the surviving population is set by tides: at sufficiently small separations the planet would overflow its Roche lobe and be torn apart.
The standard fluid Roche limit is

$$
d_R \approx 2.46\,R_\star \left(\frac{\rho_\star}{\rho_p}\right)^{1/3}.
$$

For a Sun-like host with mean stellar density $\rho_\star \approx 1.4$ g cm$^{-3}$ and a typical hot Jupiter with $\rho_p \approx 1$ g cm$^{-3}$, this gives $d_R \approx 2.46 \times 1.12 \times R_\star \approx 2.7\,R_\star$, or in physical units about $0.013$ AU.
The observed pile-up of hot Jupiters at $\sim 0.04$--$0.05$ AU sits a factor of three to four outside this limit, exactly where tidal circularisation timescales become long enough to preserve the orbit over Gyr but disruption is no longer threatened.
The Roche limit is therefore one of the two physical scales (the other being the host-star tidal dissipation scale) that frame the observed inner edge of the hot-Jupiter distribution and the upper boundary of the hot-Neptune desert discussed above.
There are three competing mechanisms for the inward migration that delivers planets to this region.

**Disk migration** (Type II) is the smoothest of the three.
A giant planet embedded in a still-gaseous disk excites density waves in the disk that exert a net torque back on the planet, and the torque drives the planet inward on a timescale set by the local disk viscosity and gas density (recap from {ref}`lecture02`).
Type II migration is quiescent and predicts low orbital eccentricities and orbits well aligned with the host star spin axis (because the disk and the stellar equator are themselves typically aligned to better than a few degrees).

**High-eccentricity migration** is more violent.
A distant perturber, either a wide stellar binary companion or another giant planet on a misaligned orbit, drives the inner giant onto a high-eccentricity orbit through Kozai-Lidov oscillations: the secular gravitational coupling slowly trades inclination for eccentricity over timescales of $10^{6}$ to $10^{8}$ years.
Once the perihelion of the inner planet's orbit gets close enough to the host star, **tidal dissipation** in the planet rapidly circularises the orbit at a small semi-major axis, leaving a hot Jupiter on a tight roughly circular orbit.
This pathway naturally produces orbits that are misaligned with the stellar spin axis, because Kozai-Lidov oscillations conserve the original misalignment.

**Planet-planet scattering** is the third mechanism.
A multi-giant system that is dynamically unstable can eject one or more giants entirely while leaving survivors on highly eccentric orbits; tidal dissipation again circularises the most extreme of those at short period.
Planet-planet scattering, like high-eccentricity migration, can produce significant misalignments. {numref}`fig:obliquitypathways` sketches the three pathways and the obliquity distributions they leave behind.

```{figure} figures/obliquity_pathways.avif
:align: center
:name: fig:obliquitypathways
:width: 90%

Schematic of the three migration pathways for hot Jupiters and the **stellar obliquities** they produce, from the review of {cite:t}`Albrecht2022`. Disk migration (left) preserves the alignment of the stellar spin and the orbit normal because the disk and the stellar equator are themselves aligned. High-eccentricity migration via Kozai-Lidov coupling to a distant perturber (right) can produce arbitrary misalignments. Planet-planet scattering similarly produces misalignments.
```

The observational discriminant is the **stellar obliquity**, the angle between the stellar rotation axis and the orbit normal of the planet.
Obliquities are measured via the **Rossiter-McLaughlin effect** ({numref}`fig:rmgeom`): as a transiting planet moves across the rotating stellar disk, it occults first the blueshifted (approaching) hemisphere and then the redshifted (receding) hemisphere, producing a small wavelength-dependent distortion in the time-resolved stellar absorption lines that effectively traces out the angle between the orbital and rotational axes projected on the sky.
Two decades of Rossiter-McLaughlin measurements show a mixed picture.
Many hot Jupiters around cool ($T_\mathrm{eff} < 6250$ K) host stars are well aligned, consistent with disk migration.
Many hot Jupiters around hot ($T_\mathrm{eff} > 6250$ K) host stars, by contrast, are heavily misaligned, with sky-projected obliquities spanning the full range from prograde to polar to retrograde {cite:p}`Albrecht2022` ({numref}`fig:obliquitydist`).

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

The current consensus is that **all three migration mechanisms operate**, that their relative contributions depend on host-star spectral type, on system multiplicity, and probably on system age, and that the obliquity distribution is the cleanest empirical handle on which mechanism dominates in any given regime.
A second, complementary line of evidence is that hot Jupiters are typically **lonely**: when companions are searched for via radial velocities or transits, hot Jupiters tend to lack nearby planet companions, in contrast to the compact peas-in-a-pod systems.
This loneliness is consistent with a violent dynamical history that cleared neighbours, and is not consistent with the smooth growth process that produces peas in a pod.

### Super-Earth and sub-Neptune composition

Bulk-density measurements (the joint transit-plus-RV combination) have allowed a compositional census of the small-planet population.
**Super-Earths** below the radius valley generally have densities consistent with rocky compositions, $4$--$8$ g/cm$^3$, similar to Earth and Venus.
**Sub-Neptunes** above the valley have lower densities, typically $1$--$3$ g/cm$^3$, and require some volatile component on top of a rocky core.
The volatile component can be either a thick $\mathrm{H_2}$/He envelope, a thick $\mathrm{H_2O}$ layer ("water world"), or some combination.
At the bulk-density level alone these scenarios are degenerate: the same density can be matched by a variety of internal structures.

A particularly interesting subclass of sub-Neptunes are those whose density is consistent with **water-rich** compositions, $\gtrsim 10$--$20\%$ $\mathrm{H_2O}$ by mass, sometimes called water worlds.
Some authors have proposed that a subset of water-rich sub-Neptunes might host a shallow surface ocean of liquid water under a thick $\mathrm{H_2}$-rich atmosphere, the so-called **hycean** scenario {cite:p}`Madhusudhan2023`.
On a hycean world the high-pressure and low-stellar-flux combination keeps the deep ocean liquid even though the equilibrium temperature is far below 273 K; the $\mathrm{H_2}$ atmosphere provides a strong greenhouse effect.
Hycean worlds have been proposed as a new candidate habitable regime, distinct from the classical rocky habitable-zone planet picture.
The hycean interpretation is contested.
Other authors argue that the same bulk densities can be matched by mini-Neptunes with no surface, and that the atmospheric chemistry expected for true hyceans differs from what is currently observed in the most-studied target K2-18 b (see Part 3) {cite:p}`Wogan2024,Glein2024`.
The hycean question is one of the most active arguments in current exoplanet science.

A second compositional ambiguity, also unresolved, applies to small close-in planets in the ultra-short-period regime.
A planet at a few stellar radii receives so much instellation that distinguishing a thin atmosphere from a bare rock surface is observationally hard.
The same density and radius can match both a "Venus analogue" (thick $\mathrm{CO_2}$ atmosphere, runaway greenhouse) and a stripped bare-rock surface.
Distinguishing them requires spectroscopy, which we discuss in Part 3.

### M dwarf planets

M dwarfs are by far the most abundant stars in the galaxy, accounting for roughly 75\% of all main-sequence stars.
They are also the easiest stars in which to find small habitable-zone planets, for two reasons.
First, the geometric transit probability scales as $R_\star / a$, and the habitable-zone semi-major axis scales as $\sqrt{L_\star}$, so for a given luminosity an M dwarf habitable zone is closer in than a Sun-like one and the transit probability is larger.
Second, the transit depth $(R_p / R_\star)^2$ is much larger for an Earth-sized planet around an M dwarf than around a Sun-like star, so the same SNR is achievable with a smaller telescope and shorter integration.

```{figure} figures/dressing_mdwarf_occurrence.avif
:align: center
:name: fig:dressing
:width: 75%

Cumulative occurrence rate of small planets around M dwarfs as a function of orbital period from the full Kepler sample, from {cite:t}`Dressing2015`. Each curve is a different planet-radius bin from $0.5$--$1\,\Rearth$ (black) to $3$--$4\,\Rearth$ (red). M dwarfs host on average $\sim 2$ small planets per star inside 200 days, and roughly one Earth-size planet per star in or near the habitable zone. M dwarf small-planet occurrence rates exceed those around Sun-like stars by roughly a factor of 2--3.
```

{cite:t}`Dressing2015` used the full Kepler M dwarf sample to estimate that the occurrence rate of small ($R_p < 4\,\Rearth$) planets per M dwarf inside 200 days is roughly $2.5$, compared to $\sim 0.7$ for Sun-like stars.
Roughly $0.16^{+0.17}_{-0.07}$ Earth-size planets lie in the conservative habitable zone of each M dwarf ({numref}`fig:dressing`).
The exoplanet community has therefore made M dwarf habitable-zone Earth analogues a central observational target, despite the substantial concerns discussed below.

The biggest concern for M dwarf habitability is **stellar activity**.
M dwarfs spend a longer fraction of their early life in a high-luminosity pre-main-sequence phase than Sun-like stars do, with surface luminosities up to ten times their main-sequence value for hundreds of Myr.
A planet that ends up in the M dwarf habitable zone will, during this early phase, have been well inside its **runaway-greenhouse boundary** and will have lost much of its initial water inventory.
M dwarfs are also magnetically more active than Sun-like stars and emit much more XUV flux per unit bolometric luminosity.
{cite:t}`LugerBarnes2015` showed that the integrated XUV history of an early M dwarf can drive complete loss of an Earth-equivalent ocean's worth of water on a habitable-zone planet, leaving an oxygen-rich abiotic atmosphere as a false-positive biosignature.
Whether modern habitable-zone M dwarf planets have any atmospheric water at all remains an open empirical question that JWST is now beginning to address (Part 3).

A second concern is **tidal locking**.
The habitable zone of an M dwarf is so close in that the planet's tidal evolution timescale is short compared to the age of the system, so habitable-zone M dwarf planets are typically expected to be in $1{:}1$ spin-orbit resonance with one hemisphere always facing the star.
A tidally locked planet has a permanent dayside and a permanent nightside, and the climate must redistribute heat from one to the other through a thick enough atmosphere or condense the volatiles on the nightside.
Three-dimensional general circulation models of tidally locked M dwarf planets show a richer range of climate states than the older one-dimensional habitable-zone analyses suggested {cite:p}`Yang2013`, including some configurations with strong clouds on the substellar point that extend the inner edge of the habitable zone closer to the star.
The TRAPPIST-1 system is the central laboratory for M dwarf habitability, because the seven planets sample the habitable zone and its bracketing flux regimes simultaneously.

## Part 3: Characterisation, habitability, and the comparative payoff

### Transmission spectroscopy during transit

When a transiting planet has an atmosphere, a small fraction of the stellar light passes through the planet's day-night terminator on its way to the observer.
The atmospheric gases imprint absorption features on the transit depth, making the planet effectively look slightly larger at wavelengths where the atmosphere is opaque and slightly smaller at wavelengths where it is transparent.
The **wavelength-dependent transit depth** is

$$
\delta(\lambda) = \frac{[R_p + n_H H(\lambda)]^2}{R_\star^2},
$$

where $H = \kB T / (\mu m_u g)$ is the atmospheric scale height, $\mu$ is the mean molecular weight in atomic mass units, $m_u$ is the atomic mass unit, $g$ is the surface gravity, and $n_H$ is the number of scale heights probed at wavelength $\lambda$ (typically a few).
A short numerical exercise makes the sensitivity scaling concrete.
For a typical hot Jupiter with dayside-terminator temperature $T \approx 1500$ K, an $\mathrm{H_2}$/He envelope of mean molecular weight $\mu \approx 2.3$, and surface gravity $g \approx 25$ m s$^{-2}$, the scale height is

$$
H = \frac{\kB T}{\mu m_u g} = \frac{(1.38 \times 10^{-23})(1500)}{(2.3)(1.66 \times 10^{-27})(25)} \approx 2 \times 10^{5}\ \mathrm{m},
$$

or roughly $200$ km.
For $R_p \approx 1.2\,\Rjup$ and $R_\star \approx 1\,\Rsun$, the fractional modulation of the transit depth across an $n_H \approx 5$ scale-height absorption line core is

$$
\frac{\Delta\delta}{\delta} \approx \frac{2 n_H H}{R_p} \approx \frac{2 \times 5 \times 2 \times 10^{5}\ \mathrm{m}}{8.6 \times 10^{7}\ \mathrm{m}} \approx 2 \times 10^{-2},
$$

so the absolute change in transit depth is $(\Delta\delta / \delta) \times \delta \approx 2 \times 10^{-2} \times 10^{-2} \approx 2 \times 10^{-4}$, of order a few hundred ppm.
This is exactly the precision regime delivered by JWST NIRSpec, and it explains why hot Jupiters were the first class of exoplanet for which atmospheric characterisation became routine.
For a sub-Neptune the higher mean molecular weight and lower temperature shrink $H$ by an order of magnitude and push the signal to the 10--100 ppm level.
For a rocky terrestrial planet around an M dwarf the signal is below 10 ppm, demanding multi-transit JWST integrations and pushing the noise floor down to its instrumental limit.

The detectable atmospheric species in the optical and near-infrared include sodium, potassium, water vapour, carbon monoxide, carbon dioxide, methane, and a growing list of photochemical and disequilibrium species including $\mathrm{SO_2}$, $\mathrm{H_2S}$, OCS, and HCN.
A complication is **clouds and hazes**: high-altitude condensate or photochemical haze layers can mute or completely flatten transmission spectra by acting as a continuum opacity at all wavelengths.
The strongest evidence that clouds are pervasive in close-in giant atmospheres is the {cite:t}`Sing2016` HST and Spitzer transmission spectral survey of ten hot Jupiters, which arranged the spectra in a continuum from clear (full Na, K, and $\mathrm{H_2O}$ features) to fully cloudy (featureless), with all intermediate states represented ({numref}`fig:sing`; the warm sub-Neptune GJ 1214 b in {numref}`fig:gj1214` is the extreme cloudy case).

```{figure} figures/sing_hotjup_spectra.avif
:align: center
:name: fig:sing
:width: 70%

A continuum from clear to cloudy hot Jupiter atmospheres, observed in transmission with HST and Spitzer for ten hot Jupiters and arranged top-to-bottom by decreasing strength of atmospheric features. The clear-atmosphere targets at the top show prominent Na, K, and $\mathrm{H_2O}$ absorption; the cloudy targets at the bottom show flat featureless transmission spectra. From {cite:t}`Sing2016`. The diversity of cloud cover at otherwise similar planet temperatures and gravities is one of the central puzzles of hot Jupiter atmospheric physics.
```

```{figure} figures/gj1214b_clouds.avif
:align: center
:name: fig:gj1214
:width: 80%

Featureless transmission spectrum of the warm sub-Neptune **GJ 1214 b** from {cite:t}`Kreidberg2014`, showing how high-altitude clouds (or hazes) can completely erase atmospheric absorption features even with high-precision HST data. Three model atmospheres (clear $\mathrm{H_2O}$, $\mathrm{CH_4}$, $\mathrm{CO_2}$) are ruled out at high significance. The conclusion is either a high-altitude cloud deck or a high-mean-molecular-weight (water-rich) atmosphere; the two cases are not distinguishable from this measurement alone.
```

### Emission spectroscopy and phase curves

Transmission spectroscopy probes the day-night terminator at low pressure.
A complementary technique is **emission spectroscopy**, which observes the planet's own thermal radiation directly when the planet passes **behind** the star (the **secondary eclipse**) and then reappears.
The drop in flux during secondary eclipse measures the brightness temperature of the planet's dayside.
Continuous monitoring of the planet across its full orbit produces a **phase curve**, which traces the apparent brightness as different parts of the planet rotate into view.
A strong day-night contrast in the phase curve indicates inefficient heat redistribution and therefore a thin or absent atmosphere; a weak contrast indicates strong heat redistribution by an optically thick, dynamically active atmosphere ({numref}`fig:wasp43`).

```{figure} figures/wasp43b_phase_curve.avif
:align: center
:name: fig:wasp43
:width: 90%

JWST MIRI **phase curve** of the hot Jupiter **WASP-43 b**, from {cite:t}`Bell2024`. The top panel is the spectroscopic phase curve as a function of wavelength and orbital phase. The middle panel is the band-integrated white light curve, showing one transit, two secondary eclipses, and the smooth phase modulation of the planet's thermal flux as the dayside rotates in and out of view. The bottom panels are the dayside and nightside emission spectra and best-fit blackbody models. The retrieved nightside temperature is much colder than the dayside, evidence of a strong day-night contrast despite an atmosphere thick enough to imprint clear spectral features on the dayside.
```

A self-consistent transmission plus emission plus phase curve dataset constrains the wavelength-dependent thermal structure, the abundance of major absorbers, the wind circulation pattern, and the cloud distribution simultaneously.
JWST has made this combination routinely accessible for hot Jupiters and is beginning to push it to warm Neptunes and habitable-zone rocky planets.

### JWST era results (2022--2025)

The James Webb Space Telescope began science operations in mid-2022 and has fundamentally reshaped exoplanet atmospheric characterisation in three years.
Below we walk through the most important early results and the active controversies they have generated.

**WASP-39 b** (a $0.28\,\Mjup$ hot Saturn) was the target of the JWST Transiting Exoplanet Early Release Science (ERS) programme.
NIRSpec PRISM and G395H, NIRCam, and NIRISS observations together produced a transmission spectrum spanning $0.5$--$5.5$ $\mu$m with parts-per-million precision, showing **clean and unambiguous detections** of $\mathrm{H_2O}$, CO, $\mathrm{CO_2}$, Na, K, and $\mathrm{SO_2}$, alongside a clear non-detection of $\mathrm{CH_4}$ (3$\sigma$ upper limit $\sim 5$ ppm) that is itself diagnostic of the super-solar metallicity inferred for this atmosphere {cite:p}`Rustamkulov2023,Alderson2023` ({numref}`fig:wasp39prism` and {numref}`fig:wasp39species`).

```{figure} figures/wasp39b_prism_spectrum.avif
:align: center
:name: fig:wasp39prism
:width: 90%

The JWST/NIRSpec PRISM transmission spectrum of **WASP-39 b** from {cite:t}`Rustamkulov2023`. The black points are the JWST data and the model spectra are colour-coded to show the contributions of individual molecules: Na, K, $\mathrm{H_2O}$, CO, $\mathrm{CO_2}$, $\mathrm{SO_2}$, $\mathrm{CH_4}$, and clouds. The features are detected at extreme statistical significance and demonstrate the capability of JWST to extract species-by-species atmospheric composition for transiting planets.
```

The most striking discovery in the WASP-39 b ERS data was the unambiguous detection of **photochemically produced $\mathrm{SO_2}$** {cite:p}`Tsai2023`.
$\mathrm{SO_2}$ is not predicted by any equilibrium chemistry model for a hot Jupiter atmosphere; its abundance in the observed range of $\sim 1$--$10$ ppm requires a non-equilibrium production pathway driven by stellar UV photolysis of $\mathrm{H_2S}$, followed by oxidation of the resulting elemental sulphur to SO and then $\mathrm{SO_2}$.
This is the first **unambiguous detection of disequilibrium photochemistry** in any exoplanet atmosphere, and establishes that photochemical models, calibrated against $\mathrm{SO_2}$ as a tracer, can be used to extract metallicity and C/O ratios from a wider planet sample ({numref}`fig:wasp39so2`).

```{figure} figures/wasp39b_so2_spectrum.avif
:align: center
:name: fig:wasp39so2
:width: 90%

Theoretical transmission spectra of WASP-39 b from photochemical models, compared to JWST data, from {cite:t}`Tsai2023`. The four panels show predictions from four independent photochemistry codes (VULCAN, KINETICS, ARGO, ATMO) all incorporating $\mathrm{SO_2}$ chemistry. All four models predict pronounced $\mathrm{SO_2}$ absorption at $\sim 4\,\mu$m, in agreement with the JWST observation. The detection demonstrates that $\mathrm{SO_2}$ is photochemically generated in the WASP-39 b atmosphere from $\mathrm{H_2S}$ precursors.
```

```{figure} figures/wasp39b_alderson_species.avif
:align: center
:name: fig:wasp39species
:width: 80%

Decomposition of the JWST/NIRSpec G395H transmission spectrum of WASP-39 b into the contributions of individual species, from {cite:t}`Alderson2023`. **Top**: full spectrum with the best-fit model (black) and the contributions of clouds, $\mathrm{CH_4}$, $\mathrm{H_2O}$, $\mathrm{SO_2}$, $\mathrm{CO_2}$, and CO shown as the difference relative to the full model when each species is removed. **Bottom**: isolated $\mathrm{CO_2}$ feature near 4.3 $\mu$m (filled band is the model contribution), detected at $28.5\sigma$. This is by far the strongest detection of any exoplanet absorption feature to date.
```

**TRAPPIST-1 b**, the innermost rocky planet of the TRAPPIST-1 system, was the first habitable-zone-adjacent rocky planet observed by JWST in MIRI thermal emission.
{cite:t}`GreeneTrappist2023` measured the dayside flux at 15 $\mu$m and found it to be consistent with a **bare rock dayside** at the equilibrium temperature, with no evidence for any atmospheric heat redistribution.
The implication is that TRAPPIST-1 b has either no substantial atmosphere or only a very thin one, ruling out thick $\mathrm{CO_2}$ Venus-analogue atmospheres at high statistical significance ({numref}`fig:trappist1beclipse` and {numref}`fig:trappist1bemiss`).

```{figure} figures/trappist1b_eclipse.avif
:align: center
:name: fig:trappist1beclipse
:width: 90%

JWST MIRI 15 $\mu$m secondary eclipse light curve of **TRAPPIST-1 b**, from {cite:t}`GreeneTrappist2023`. The eclipse depth $f_p / f_\star = 861 \pm 99$ ppm corresponds to a dayside brightness temperature of $T_B = 503^{+26}_{-27}$ K, consistent with a bare rock dayside in radiative equilibrium with the stellar flux and no significant heat redistribution. This is the **first** thermal emission detection of an Earth-sized exoplanet.
```

```{figure} figures/trappist1b_emission.avif
:align: center
:name: fig:trappist1bemiss
:width: 90%

The TRAPPIST-1 b dayside emission compared with model atmospheres of different compositions, from {cite:t}`GreeneTrappist2023`. The data are inconsistent with thick $\mathrm{CO_2}$ + $\mathrm{N_2}$ atmospheres and inconsistent with $\mathrm{O_2}$ + $\mathrm{CO_2}$ atmospheres at any plausible mass-loading. They are consistent with a bare-rock dayside (the 503 K blackbody curve, magenta).
```

**TRAPPIST-1 c**, the second-innermost planet, was observed similarly by {cite:t}`Zieba2023` and shows the same behaviour.
A thick Venus-like $\mathrm{CO_2}$ atmosphere is ruled out for TRAPPIST-1 c as well.
The current consensus from these two non-detections is that the inner TRAPPIST-1 planets have either negligible atmospheres or atmospheres so thin that they cannot redistribute heat from the dayside to the nightside.
A thin atmosphere consistent with the data is not yet ruled out, but a thick atmosphere is ({numref}`fig:trappist1c`).

```{figure} figures/trappist1c_grid.avif
:align: center
:name: fig:trappist1c
:width: 90%

Grid of model atmospheric compositions for **TRAPPIST-1 c** compared with the measured 15 $\mu$m secondary eclipse depth, from {cite:t}`Zieba2023`. The colour-coded grid shows expected eclipse depths as a function of $\mathrm{CO_2}$ partial pressure (rows) and total atmospheric thickness (columns). Models with $\geq 0.1$ bar of $\mathrm{CO_2}$ are inconsistent with the data; models with no atmosphere or with very thin atmospheres match. A Venus-analogue thick $\mathrm{CO_2}$ atmosphere on TRAPPIST-1 c is ruled out.
```

A series of additional rocky-planet atmosphere non-detections has accumulated.
**LHS 475 b** {cite:p}`LustigYaeger2023`, **GJ 486 b**, and **GJ 1132 b** all have flat featureless JWST transmission spectra inconsistent with thick low-mean-molecular-weight atmospheres.
The accumulating pattern across small rocky M dwarf planets is therefore that **most do not retain substantial atmospheres**, consistent with the {cite:t}`LugerBarnes2015` prediction that M dwarf XUV history strips early atmospheres efficiently ({numref}`fig:lhs475`).

```{figure} figures/lhs475b_spectrum.avif
:align: center
:name: fig:lhs475
:width: 90%

JWST/NIRSpec G395H transmission spectrum of the rocky exoplanet **LHS 475 b**, an Earth-size M dwarf planet at $\sim 12$ pc, from {cite:t}`LustigYaeger2023`. The data are flat and featureless. Hydrogen-helium-dominated atmospheres are ruled out at high confidence (top panel). A pure $\mathrm{CH_4}$ atmosphere is also ruled out, though a pure $\mathrm{CO_2}$ Venus-like atmosphere is marginally consistent (bottom panel). The result is consistent with no detectable atmosphere on LHS 475 b.
```

**55 Cancri e** is a hot rocky super-Earth on a 17.7 hour orbit around a Sun-like K star at 12.6 pc.
The dayside is so hot ($\sim 2000$ K) that the surface is plausibly molten.
{cite:t}`Hu2024` reported a JWST MIRI thermal emission and phase curve measurement showing a much lower dayside brightness temperature than would be expected from a bare rock surface in equilibrium and a phase curve modulation consistent with the presence of a **secondary CO/$\mathrm{CO_2}$-rich atmosphere** outgassed from the molten surface.
This is the **first tentative atmospheric detection on a rocky world around a Sun-like star** and is currently being scrutinised by the wider community.
The interpretation depends on the precise treatment of the data systematics and on whether the atmosphere is genuinely a stable secondary atmosphere or is an episodically replenished one tied to surface volcanism ({numref}`fig:55cnce`).

```{figure} figures/55cnce_hu_emission.avif
:align: center
:name: fig:55cnce
:width: 90%

JWST/NIRCam plus MIRI thermal emission spectrum of **55 Cancri e** from {cite:t}`Hu2024`. Black points are the binned JWST data; coloured curves are atmospheric models (grey blackbody, $\mathrm{CO_2}$+$\mathrm{N_2}$ purple, $\mathrm{CO_2}$+CO red, CO-only gold). The data fall below the bare-rock blackbody at most wavelengths and favour atmospheric models with non-negligible CO and $\mathrm{CO_2}$. A companion retrieval (not shown) constrains the volatile mixing ratios but is sensitive to the assumed background gas, so the conclusion of a secondary atmosphere is currently tentative but suggestive.
```

**TOI-561 b** is an ultra-short-period rocky planet around a metal-poor thick-disk K star, particularly interesting because the host star formation history is older than the average exoplanet host and the bulk-density measurement places the planet near the rocky end of the small-planet spectrum.
JWST observations have produced **tentative evidence for a thin atmosphere or surface composition signal** on TOI-561 b, with current data quality at the marginal detection level.
This is a useful case study in how challenging it is to claim atmospheric detections on small rocky planets even with JWST.

**K2-18 b** is the case study that has drawn the most attention, and the most controversy.
It is a sub-Neptune of $2.6\,\Rearth$ and $8.6\,\Mearth$ in the habitable zone of an M3 host star.
{cite:t}`Madhusudhan2023` reported a JWST NIRISS plus NIRSpec transmission spectrum showing detections of $\mathrm{CH_4}$ and $\mathrm{CO_2}$, and a marginal detection of **dimethyl sulphide** ($\mathrm{(CH_3)_2 S}$, DMS) at the $\sim 2\sigma$ level (significance dropping further when retrieval-pipeline detector offsets are allowed to float).
On Earth, DMS is produced almost exclusively by marine phytoplankton, with no significant abiotic sources known.
The Madhusudhan et al.\ team interpreted the detection as a tentative biosignature consistent with the **hycean** scenario discussed earlier: a sub-Neptune with a deep $\mathrm{H_2}$ atmosphere overlying a planet-wide liquid-water ocean at the base ({numref}`fig:k218b`).

```{figure} figures/k218b_spectrum.avif
:align: center
:name: fig:k218b
:width: 90%

JWST transmission spectrum of **K2-18 b** from {cite:t}`Madhusudhan2023`, combining NIRISS SOSS and NIRSpec G395H data. The black points are the data and the colour-coded model spectrum shows contributions from $\mathrm{CH_4}$, $\mathrm{CO_2}$, and tentatively dimethyl sulphide (DMS). The $\mathrm{CH_4}$ and $\mathrm{CO_2}$ detections are robust; the DMS feature is at the edge of the JWST sensitivity floor and is heavily dependent on the retrieval assumptions. The interpretation is contested.
```

The community response was swift and largely sceptical.
Several independent groups reanalysed the same data with different retrieval frameworks and could not reproduce the DMS detection at significant levels {cite:p}`Wogan2024`.
Others argued that the spectral feature attributed to DMS could be explained by other molecules or by instrument systematics, or that the line-by-line cross sections used in the retrievals are not yet accurate enough at the relevant wavelengths.
{cite:t}`Glein2024` argued from a geochemical standpoint that the K2-18 b interior is unlikely to support a habitable liquid water ocean at the base, based on temperature and pressure constraints.
{cite:t}`Wogan2024` argued that the entire spectrum is consistent with a non-habitable mini-Neptune with no surface, no DMS, and a different chemical interpretation.
The debate remains open as of early 2026.

The pedagogical value of K2-18 b is independent of the specific outcome.
**Whatever the final consensus on DMS turns out to be, K2-18 b is the textbook example of how a tentative biosignature claim is tested, challenged, and revised in real time.**
The same general pattern, of a single team's tentative detection followed by community reanalysis, has played out many times in the history of biosignature claims (the historical Mars methane debate, the Venus phosphine controversy from {ref}`lecture06`, the ALH84001 nano-fossil claim).
The K2-18 b discussion has been faster, more transparent, and better documented than any of those previous cases, and it sets a useful template for how the much louder claims of the next decade should be evaluated.

A separate strand of JWST atmospheric work has come from the **direct imaging** instruments on NIRCam and MIRI.
The first JWST mid-infrared spectra of directly imaged exoplanets were obtained for the wide-orbit planet HIP 65426 b and the planetary-mass companion VHS 1256 b in 2023.
These spectra provide the first direct atmospheric retrievals of self-luminous giant planets at wavelengths where ground-based facilities are dominated by atmospheric absorption.

### The habitable zone revisited

Lecture 9 (Earth and Venus) introduced the **classical habitable zone** as the range of stellar fluxes for which a rocky planet can plausibly maintain liquid surface water.
The classical formulation goes back to {cite:t}`Kasting1993`, who used a one-dimensional radiative-convective climate model to identify two boundaries.
The **inner edge** is set by the **Simpson-Nakajima runaway greenhouse limit**: as the planet warms, the atmospheric water vapour content rises following the Clausius-Clapeyron relation, the outgoing longwave radiation reaches a maximum, and any further increase in absorbed flux drives the planet into a runaway state in which the entire ocean evaporates.
The numerical value of the limiting outgoing longwave radiation is about $280$--$310$ W/m$^2$, depending on details, and it implies that an Earth-twin climate cannot be sustained at solar fluxes much above $\sim 1.06$ times the Earth value, corresponding to a critical orbital distance of $\sim 0.97$ AU around a Sun-like star (the runaway greenhouse limit; the more conservative moist greenhouse limit lies just inside Earth's orbit at $\sim 0.99$ AU; recap from {ref}`lecture09`).
The **outer edge** is set by the **maximum $\mathrm{CO_2}$ greenhouse**: as a planet at large stellar distance accumulates more $\mathrm{CO_2}$ to compensate for the lower flux, eventually the increased atmospheric $\mathrm{CO_2}$ starts to condense out as ice clouds and the greenhouse effect saturates, leaving the planet too cold for surface water regardless of the atmospheric inventory.

```{figure} figures/kopparapu_hz.avif
:align: center
:name: fig:kopparapu
:width: 80%

The **classical habitable zone** as a function of stellar effective temperature and effective stellar flux, from {cite:t}`Kopparapu2013`. The green-shaded region is the habitable zone bounded on the inside by the moist greenhouse limit and on the outside by the maximum $\mathrm{CO_2}$ greenhouse limit. Symbols mark known potentially habitable exoplanets including GJ 581 d/g, GJ 667C c, Kepler-22 b, Tau Ceti e/f, and the solar system planets Earth, Venus, and Mars. The "Recent Venus" and "Early Mars" empirical limits are shown by the dotted boundaries.
```

{cite:t}`Kopparapu2013` updated the classical Kasting calculation with modern radiative transfer and provided habitable-zone boundaries for stars with a wide range of effective temperatures, including M dwarfs.
The Kopparapu boundaries are the standard input to most recent occurrence rate estimates of habitable-zone planets (the $\eta_\oplus$ discussion above) ({numref}`fig:kopparapu`).
Two important caveats apply to the classical habitable zone.

First, **history matters**, not just snapshot conditions.
A planet currently inside the formal habitable zone is not necessarily habitable if its early evolution drove it through a runaway greenhouse phase that desiccated it (the Venus alternative discussed in {ref}`lecture09`).
A planet currently inside the formal habitable zone of an M dwarf has spent hundreds of Myr inside the runaway greenhouse boundary during the host's pre-main-sequence high-luminosity phase {cite:p}`LugerBarnes2015`, and may have lost its initial water inventory entirely.
The habitable zone is not a line that a planet either lies inside or outside at the present epoch.
It is a **trajectory** through climate-evolution space that the planet has followed since formation.

Second, the one-dimensional Kasting/Kopparapu boundaries are computed under simplifying assumptions about atmospheric circulation and clouds.
Modern three-dimensional general circulation models (GCMs) {cite:p}`Yang2013,Way2016,Turbet2021` include realistic three-dimensional cloud feedbacks, and they show that the actual habitable-zone boundaries can shift by 5--20\% depending on rotation rate, atmospheric composition, and surface albedo.
For tidally locked M dwarf planets, GCMs predict a substellar cloud feedback that can extend the inner edge significantly, allowing surface liquid water at instellation fluxes well above the 1D moist greenhouse limit.
The classical habitable zone is therefore best treated as a useful first-order screening tool, not as a precise boundary.

### Biosignature gases and the challenge of false positives

If a habitable-zone exoplanet does have a thick enough atmosphere to be characterised, what would constitute a convincing detection of life?
The classical answer is that life produces **disequilibrium gas combinations** that cannot be sustained without continuous biological replenishment.
On Earth, the simultaneous presence of substantial $\mathrm{O_2}$ ($\sim 21\%$ of the atmosphere) and $\mathrm{CH_4}$ ($\sim 1.8$ ppm) is the canonical example: $\mathrm{O_2}$ and $\mathrm{CH_4}$ react with each other photochemically in a few decades, so their joint presence in the modern atmosphere requires both gases to be replenished by living systems ($\mathrm{O_2}$ by oxygenic photosynthesis, $\mathrm{CH_4}$ by methanogenesis and biomass-mediated processes).
On the early Earth, before the Great Oxidation Event around 2.4 Ga, the analogous disequilibrium combination would have been $\mathrm{CH_4}$ + $\mathrm{N_2O}$ or $\mathrm{CH_4}$ + $\mathrm{CO_2}$ in a low-$\mathrm{O_2}$ atmosphere.

The catalogue of "classical biosignature gases" therefore includes $\mathrm{O_2}$, $\mathrm{O_3}$ (which is photochemically derived from $\mathrm{O_2}$ and easier to detect spectroscopically at some wavelengths), $\mathrm{CH_4}$, $\mathrm{N_2O}$, and a longer list of organosulphur and organohalogen compounds.
A single gas, in isolation, almost never constitutes a biosignature: the question is whether the combination of detected gases is consistent with any plausible abiotic source.

The big problem with biosignature detection is **false positives**.
An astonishing number of abiotic processes can produce $\mathrm{O_2}$ and $\mathrm{O_3}$ in planetary atmospheres without any life involved.
{cite:t}`Wordsworth2014` showed that water vapour photolysis followed by hydrogen escape can build up substantial abiotic $\mathrm{O_2}$ on dry planets, particularly during the early evolution of M dwarf habitable-zone planets.
$\mathrm{CO_2}$ photolysis in a dry $\mathrm{CO_2}$-rich atmosphere can produce comparable amounts of $\mathrm{O_2}$ via splitting of $\mathrm{CO_2}$ into CO and O.
Both of these abiotic $\mathrm{O_2}$ pathways are common consequences of M dwarf XUV history, and they specifically contaminate the most accessible class of habitable-zone targets.
Methane is also a non-trivial false positive: volcanic outgassing, serpentinisation reactions in hydrothermal systems, and impact-driven shocks can all release abiotic $\mathrm{CH_4}$ in measurable quantities (recap from {ref}`lecture10` Mars methane discussion).

The community consensus is that biosignature detection is fundamentally an **inverse problem**: a given combination of gases must be tested against all plausible abiotic explanations, and the biosignature interpretation is only convincing if the abiotic pathways are demonstrably insufficient.
This is much harder than it sounds, because the catalogue of plausible abiotic pathways is constantly being extended by new theoretical and experimental work.
A false positive that nobody has thought of cannot be ruled out until somebody thinks of it.
The DMS-on-K2-18 b debate is a useful microcosm: the original biosignature claim rested on the argument that DMS has no significant abiotic source on Earth, but "no significant abiotic source on Earth" is a much weaker statement than "no significant abiotic source anywhere", and the skeptical literature has already proposed several possible abiotic DMS production pathways under exoplanet conditions.

### Comparative payoff: the solar system in the exoplanet landscape

We can now ask the question that has been waiting since {ref}`lecture01`: **is the solar system typical?**

The answer depends on what we mean by "typical".
If "typical" means "the most common configuration in the bias-corrected exoplanet archive", then the answer is unambiguously **no**.
The most common host star in the galaxy is an M dwarf, not a G dwarf like the Sun.
The most common planet class around any host is the sub-Neptune at $2$--$3\,\Rearth$, which the solar system completely lacks (there is nothing between Earth at $1\,\Rearth$ and Neptune at $3.88\,\Rearth$).
The most common inner-system architecture is the compact peas-in-a-pod of $\sim 5$--$8$ similarly sized planets within $\sim 0.2$ AU; the solar system has four irregularly spaced terrestrial planets out to $1.5$ AU.
The solar system also lacks any hot Jupiter or hot Neptune, and its giant planets are on wide ($\geq 5$ AU), nearly circular, low-inclination orbits, rather than the dynamically hot, eccentric orbits typical of radial-velocity-discovered giant planet systems.

In every individual respect, the solar system sits in a sparsely populated corner of the observed exoplanet parameter space.

But "typical" can also mean "drawn from the underlying physical distribution", which is a different question.
The observed exoplanet archive is the union of detection biases discussed in Part 1, and many of those biases work strongly against finding solar-system analogues.
A Jupiter analogue at $5$ AU produces a radial velocity signal of only $\sim 12$ m/s with a 12-year period, which requires more than a decade of consistent observing to detect; fewer than a hundred such planets are currently known.
A Saturn analogue at $9.5$ AU is even harder.
An Earth analogue at 1 AU around a Sun-like star is at the very edge of detectability for any current technique.
The corner of parameter space in which the solar system sits is also the corner that current surveys are least sensitive to.
Whether the solar system is genuinely **rare** or simply lives in an **undersampled** region of parameter space is therefore an open question that the next decade of observations will answer.

The honest answer in 2026 is: the solar system is **not obviously typical**, but it is also not yet known to be rare.
The two main lines of evidence that should resolve the question over the next decade are (a) Gaia DR4 and DR5 astrometry of long-period giant planets around nearby stars, which will populate the Jupiter analogue regime, and (b) PLATO photometry of true Earth analogues around bright Sun-like stars, which will close the inner-system gap.
The full discussion will return in {ref}`lecture14`.

### Frontier missions, part 1: transits and atmospheres (2026--2035)

The exoplanet mission queue for the next decade is dense.
The first cluster of missions, scheduled for launches in 2026--2030, is focused on transit photometry and atmospheric spectroscopy of an extended sample of known and new targets.
All dates quoted below are planning targets as of early 2026 and are commonly revised by months to years over the course of mission development.

**PLATO** (PLAnetary Transits and Oscillations of stars) is an ESA medium-class mission scheduled for launch at the end of 2026 {cite:p}`Rauer2014`.
PLATO carries 24 small telescopes operating as a single multi-aperture photometric array and is designed for high-precision photometry of a large sample of bright Sun-like stars over 2--3 year monitoring baselines.
The primary goal is the detection of true Earth analogues in the habitable zones of G dwarfs, complementing Kepler by observing brighter targets that are accessible to radial velocity follow-up for mass measurement.
PLATO is also designed to provide stellar oscillation (asteroseismic) measurements of the host stars themselves, which gives much more precise stellar radii and ages than spectroscopy alone, propagating directly into much more precise planet radii.

**Ariel** (Atmospheric Remote-sensing Infrared Exoplanet Large-survey) is an ESA medium-class mission scheduled for launch in 2029 {cite:p}`Tinetti2018`.
Ariel will conduct a dedicated transmission and emission spectroscopic survey of approximately 1000 exoplanet atmospheres at $1.25$--$7.8\,\mu$m, with simultaneous narrow-band optical photometry at $0.5$--$1.2\,\mu$m.
Unlike JWST, which observes a small number of targets in great depth, Ariel will observe a large number of targets at moderate depth, generating a statistical census of atmospheric composition as a function of planet size, equilibrium temperature, host star properties, and orbital parameters.
The Ariel sample will span the full hot Jupiter through warm sub-Neptune range and is the first dedicated atmospheric statistics mission.

**The Nancy Grace Roman Space Telescope** is a NASA flagship scheduled for launch in 2027.
Roman is primarily a wide-field survey instrument with a 2.4 m mirror equal in diameter to HST but with a $100\times$ larger field of view.
Two of its core programmes are exoplanet related.
The microlensing survey in the Galactic bulge will, as discussed in Part 1, deliver $\sim 1400$ bound exoplanets at separations of $\sim 0.5$--$10$ AU with sensitivity down to lunar masses {cite:p}`Penny2019`, plus a comparable but separately analysed sample of free-floating rogue planets.
The coronagraph instrument will be a technology demonstration for the precursor of HWO-class direct imaging, achieving contrasts at the $10^{-8}$--$10^{-9}$ level on a small number of bright nearby stars at near-infrared wavelengths.

### Frontier missions, part 2: direct imaging of Earth analogues (2030s--2040s)

The second cluster of missions, on a longer timeline, is focused on the direct detection and atmospheric characterisation of habitable-zone Earth analogues themselves.

**Habitable Worlds Observatory** (HWO) is the top-priority NASA flagship mission of the 2020 US Decadal Survey {cite:p}`NAS2021`.
HWO is currently in concept development and is targeted for a launch in the 2040s.
The baseline design is a $\sim 6$ m space telescope with a state-of-the-art coronagraph (or external starshade) capable of achieving contrasts of $10^{-10}$ at sub-arcsecond separations from nearby Sun-like stars.
The science goal is to directly image and obtain spectra of approximately $25$ Earth-analogue exoplanets around the closest Sun-like stars at visible and near-infrared wavelengths, and to search them for atmospheric biosignatures.
HWO is the most ambitious exoplanet mission ever proposed and is the long-term successor to HST and JWST in the optical and near-infrared.

**LIFE** (Large Interferometer For Exoplanets) is a European mission concept led by Sascha Quanz and collaborators, currently in study phase {cite:p}`Quanz2022`.
LIFE is a mid-infrared **nulling interferometer**: four free-flying spacecraft configured as an interferometer in the $4$--$18\,\mu$m range, with the central stellar light suppressed by destructive interference (nulling) so that the much fainter planetary thermal emission can be detected.
The science goal is complementary to HWO: rather than detecting Earth analogues in reflected starlight, LIFE detects their thermal emission and characterises their atmospheres at the wavelengths where $\mathrm{CO_2}$, $\mathrm{O_3}$, $\mathrm{H_2O}$, $\mathrm{CH_4}$, and $\mathrm{N_2O}$ have their strongest absorption features.
The mid-infrared regime is particularly well suited to biosignature gas detection because the temperature and absorption-feature contrasts are favourable ({numref}`fig:lifeyield` shows how the predicted habitable-zone yield depends on the choice of wavelength range).

```{figure} figures/life_yield.avif
:align: center
:name: fig:lifeyield
:width: 80%

Sensitivity of the predicted **LIFE** detection yield to the wavelength range of the mid-infrared nulling interferometer, from {cite:t}`Quanz2022`. Each panel shows the *change* in detectable planets per category (rocky habitable-zone, exo-Earth candidates, rocky+super-Earth, sub-Neptune, sub-Jovian), split by hot/warm/cold instellation, relative to the LIFE baseline configuration. **Top**: extending the band to $3$--$20\,\mu$m adds modest numbers of detections across most categories. **Bottom**: restricting the band to $6$--$17\,\mu$m removes a comparable number, with the rocky+super-Earth bin most affected. The headline absolute-yield prediction (not shown) of the same Scenario 2 calculation is that LIFE detects of order tens of rocky planets in the conservative habitable zones of nearby host stars; M dwarfs dominate the yield because they are nearby and abundant, while FGK dwarfs contribute the more solar-system-like targets.
```

**Extremely Large Telescopes** (ELTs) are the third pillar of the next-decade exoplanet effort and are ground-based.
The European ELT (39 m primary, first light expected 2028) on Cerro Armazones in Chile, the Giant Magellan Telescope (24.5 m, expected first light early 2030s) on Las Campanas, and the Thirty Meter Telescope (30 m, currently in delayed status) are designed to combine high-contrast imaging with high-resolution spectroscopy at near-infrared wavelengths.
The ELT class will complement HWO and LIFE in the spatially resolved high-resolution regime, particularly for the closest M dwarf habitable-zone planets like Proxima Centauri b, where the angular separation is large enough to be resolved.

Collectively, these missions push the field from **statistical demography** (where we are today, with thousands of detected planets and a few dozen well-characterised atmospheres) toward **individual characterisation of potentially habitable worlds** (where we want to be in 20 years, with full atmospheric retrievals on a curated sample of Earth analogues).

### Open questions for the next lecture

The biggest open question of the lecture is one we cannot yet answer: **what would constitute a convincing detection of life on another world?**
Would a single biosignature gas be enough?
A specific combination of gases at specific abundance ratios?
Temporal variability (seasonal cycles) on a habitable-zone target?
Unambiguous spectral evidence of vegetation or photosynthetic surface features?
The answer depends on how much we trust our catalogue of false positives and how much we trust our atmospheric models.
Each of the missions listed above is designed against a specific definition of "convincing", but none of those definitions is universally agreed upon.
The forward question for {ref}`lecture14` is exactly this: how do we move from "we have a candidate biosignature" to "we have detected life", and what would the post-detection scientific landscape look like?

## Summary

- Exoplanet science went from zero confirmed detections in 1991 to more than 6000 confirmed planets in 2025, a complete observational revolution in three decades.
- **Each detection method has a distinct bias**, and the observed planet population reflects the union of those biases as much as it reflects the underlying distribution. Radial velocity finds short-period giants around bright quiet stars; transits find short-period and large $R_p / R_\star$ systems; direct imaging finds wide-orbit young hot giants; astrometry will find Jupiter analogues; microlensing finds 1--10 AU planets at kpc distances.
- The combined transit-plus-radial-velocity measurement breaks the $m \sin i$ degeneracy and gives bulk densities, the central observational quantity that turns exoplanet detections into physical objects with measurable composition.
- **Kepler showed that planets are common.** Most main-sequence stars host at least one planet, and the small-planet population dominates by number. Hot Jupiters occur around only $\sim 1\%$ of Sun-like stars.
- The **radius valley** at $\sim 1.8\,\Rearth$ is the defining empirical feature of small-planet demographics. It points to atmospheric mass loss (photoevaporation and core-powered) as a universal sculptor of the close-in planet population, and means that many of today's super-Earths are the bare cores of former sub-Neptunes.
- The **hot Neptune desert**, the **peas-in-a-pod** correlation, and the **TRAPPIST-1** resonant chain are the other three central architectural results that any planet formation theory must explain.
- **JWST has moved exoplanet atmospheric characterisation from a promise to a routine capability.** WASP-39 b $\mathrm{SO_2}$ is the first unambiguous detection of disequilibrium photochemistry. TRAPPIST-1 b/c rule out thick $\mathrm{CO_2}$ atmospheres on close-in M dwarf rocky planets. 55 Cancri e and TOI-561 b are tentative detections of secondary atmospheres on rocky planets around Sun-like and metal-poor hosts. K2-18 b is the textbook case study in how biosignature claims are tested and revised.
- **The solar system is not obviously typical**: it lacks sub-Neptunes, lacks compact inner-system architecture, lacks hot giants, and has wide low-eccentricity outer giants. Whether it is genuinely rare or just lives in an undersampled corner of parameter space is the central observational question of the next decade.
- **Habitability is a history-dependent trajectory**, not a snapshot line on the HR diagram, and biosignature detection is an inverse problem with unavoidable false-positive challenges.
- The 2026--2040 mission queue (PLATO, Ariel, Roman, HWO, LIFE, ELTs) will push the field from statistical demography to individual characterisation of potentially habitable worlds. The forward question of what constitutes convincing life detection is taken up in {ref}`lecture14`.

## References

```{bibliography}
:filter: docname in docnames
```
