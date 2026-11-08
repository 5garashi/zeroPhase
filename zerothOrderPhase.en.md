---
title: 'Observation Limits and the Undifferentiated Origin: An Epistemological Inquiry from Quantum Measurement to Cosmology'
lang: en
math: true
description: An exploratory essay on the limits of discrimination in quantum measurement and cosmology, organized by the Spacetime-Limit Phase, the Dimension-Reduction Phase, and the Zeroth-Order Phase.
---
<!--
  File: zerothOrderPhase.en.md
  Description: Observation limits and the undifferentiated origin: an English translation of the Japanese essay
  Author: 5garashi.com Design Office
  Created: 2026-10-31
  Last updated: 2026-11-08 JST
  Version: 2.2.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Observation Limits and the Undifferentiated Origin: An Epistemological Inquiry from Quantum Measurement to Cosmology

**Author:** 5garashi.com Design Office

**Version:** <span data-version>2.2.0</span>　**Last updated:** 2026-11-08 JST

This is an exploratory essay that has not been peer reviewed. It contains no new experimental or observational data; the numbers are worked examples based on existing theory and published values.

---

## Introduction: The Epistemological Question of Indistinguishability

This essay organizes the limits of an observer's ability to tell objects apart by three concepts: the **Spacetime-Limit Phase, the Dimension-Reduction Phase, and the Zeroth-Order Phase**. It treats as one conceptual sequence the progression from the point at which the ability to discriminate objects reaches its limit, through the transformation of the degrees of freedom and scales that support discrimination, to the point at which distinctions by position, distance, and time no longer hold.

The starting point is the following epistemological position.

> **Two states that cannot, even in principle, be distinguished by any means of observation available to an observer are treated as the same physical state for that observer.**

Even if a mathematical difference remains in the total system, the observer's physical description does not distinguish the two states if the difference appears in none of the measurements available to that observer. This position can be written mathematically using the set $\mathcal A_O$ of observables available to the observer ([Appendix 1, Section 1.1](appendix1.en.html)).

<figure class="essay-figure" style="margin:1.5rem 0">
<svg viewBox="0 0 300 362" role="img" aria-labelledby="fig1-title fig1-desc" style="display:block;width:100%;max-width:360px;height:auto;margin:0 auto;color:inherit" font-size="15">
<title id="fig1-title">Flow of the three-phase model</title>
<desc id="fig1-desc">From top to bottom, three boxes for the Spacetime-Limit Phase, the Dimension-Reduction Phase, and the Zeroth-Order Phase are connected by lines. In the Spacetime-Limit Phase the framework remains and distinctions become harder. As degrees of freedom and scales transform, the Dimension-Reduction Phase follows, in which fewer directions can be independently distinguished. As the effective dimension approaches zero, the Zeroth-Order Phase is reached, where measurement standards cannot be constructed. Beyond it lies the undifferentiated origin.</desc>
<g fill="none" stroke="currentColor" stroke-width="1.5">
<rect x="10" y="10" width="280" height="64" rx="6"/>
<rect x="10" y="124" width="280" height="64" rx="6"/>
<rect x="10" y="238" width="280" height="64" rx="6" stroke-width="3"/>
<line x1="60" y1="74" x2="60" y2="124"/>
<line x1="60" y1="188" x2="60" y2="238"/>
</g>
<g fill="currentColor">
<text x="24" y="36" font-weight="700">Spacetime-Limit Phase</text>
<text x="24" y="60">Framework kept; distinctions harder</text>
<text x="80" y="96">Degrees of freedom and</text>
<text x="80" y="114">scales transform</text>
<text x="24" y="150" font-weight="700">Dimension-Reduction Phase</text>
<text x="24" y="174">Fewer independent directions</text>
<text x="80" y="218">Effective dimension D<tspan baseline-shift="sub" font-size="12">eff</tspan> → 0</text>
<text x="24" y="264" font-weight="700">Zeroth-Order Phase</text>
<text x="24" y="288">Standard R<tspan baseline-shift="sub" font-size="12">O</tspan> cannot be built</text>
<text x="24" y="330">→ Undifferentiated origin</text>
<text x="38" y="350">(CCC connecting boundary)</text>
</g>
</svg>
<figcaption>Figure 1. Flow of the three-phase model. The phases are compared in detail in the following table.</figcaption>
</figure>

| Phase | Framework of position and time | Distinguishable states | Available information structure | Assumed examples |
|---|---|---|---|---|
| **Spacetime-Limit Phase** | Maintained | Limited probabilistically and statistically | The trace distance $T$ approaches 0 | Wave-packet spreading, SQL, partial-trace states |
| **Dimension-Reduction Phase** | Transformed or reduced | Fewer directions can be distinguished independently | The rank $d_O$ of the quantum Fisher information matrix is less than 4 throughout a range of the parameters | Planck-scale spacetime foam, high-energy scattering |
| **Zeroth-Order Phase** | Not applicable (does not hold) | Indistinguishable in principle (undifferentiated) | The procedure $\mathcal R_O$ for constructing spacetime distinctions does not hold | CCC connecting boundary, the Big Bang singularity limit |

The proposal of this essay is a **connection from the Spacetime-Limit Phase through the Dimension-Reduction Phase to the Zeroth-Order Phase**. "Phase" is this essay's name for the state of an observer's description; it does not mean a thermodynamic phase transition or a quantum phase transition in which the character of a ground state changes. A list of the main symbols is given in [Appendix 1, Section 2](appendix1.en.html). A place where such a state holds is called a "region", and in cosmology, where the place is a surface, a "boundary". The detailed logical background and the definition of the effective dimension are developed in [Appendix 1](appendix1.en.html), the derivations and conditions of the equations in [Appendix 2](appendix2.en.html), and the connection to conformal cyclic cosmology (CCC) in [Appendix 3](appendix3.en.html).

---

## 1. The Spacetime-Limit Phase: The Limits of the Ability to Distinguish Objects

In the Spacetime-Limit Phase, objects become harder to distinguish while the spacetime framework in which measurements are made is preserved. How hard it is to distinguish physical states is evaluated by the total variation distance $D_{AB}$, which expresses the difference between the probability distributions $P_A(y), P_B(y)$ of measurement outcomes [1].

$$
D_{AB} = \frac{1}{2}\int \left|P_A(y)-P_B(y)\right|\,\mathrm{d}y,\qquad 0 \le D_{AB} \le 1
$$

$D_{AB} = 1$ means perfect distinguishability, and $D_{AB} = 0$ means that the two cannot be distinguished by that measurement [1].

As an example of a scale of discrimination, consider a model in which a signal makes a round trip to a free particle (mass $m$) at distance $d$ from the observer. During the round-trip time $\tau = 2d/c$, a minimum-uncertainty Gaussian wave packet with no initial correlation between position and momentum spreads in space. Optimizing the initial width gives a minimum position width of the same form as the standard quantum limit (SQL), up to a numerical factor [2].

$$
\Delta x_{\min} \sim \sqrt{\frac{\hbar\tau}{m}} = \sqrt{\frac{2\hbar d}{mc}}
$$

This value is the minimum for the family of states without initial correlation. Contractive states, which have a correlation between position and momentum, can go below it [3]. This essay uses this position width as a scale relevant to distinguishing objects, and examines the ability to discriminate after specifying the states compared and the measurement conditions. The derivation is given in [Appendix 2, Sections 2 and 3](appendix2.en.html).

---

## 2. Toward the Dimension-Reduction Phase: Localization and Observable Degrees of Freedom

### 2.1 Localization Limits and Quantum Fluctuations of Spacetime

Combining the position–momentum uncertainty relation of quantum mechanics with the Schwarzschild radius of general relativity yields the Planck length $l_P$ as a limit of localization [4].

$$
\Delta x \sim r_s \quad\Longrightarrow\quad \Delta x \sim \sqrt{2}\,l_P \qquad \left(l_P = \sqrt{\frac{\hbar G}{c^3}} \approx 1.6 \times 10^{-35}\,\mathrm{m}\right)
$$

The smaller the region one tries to observe, the larger the energy required, and the gravitational effect of that energy can significantly change the spacetime of the region being measured [4]. The picture in which the metric and topology of spacetime fluctuate quantum mechanically at the Planck scale is called "spacetime foam" [5].

At this scale, several approaches to quantum gravity report that the effective dimension itself changes. The spectral dimension, defined from the return probability of a diffusion process, is 4 at large scales and about 2 at short distances [6, 7]. The spectral dimension is defined from a diffusion process and differs in definition from the effective dimension of this essay (Section 4.2). This essay cites the result that the effective dimension depends on the scale probed as a precedent for considering the Dimension-Reduction Phase. Computing the correspondence between the two quantities is a task for future work.

There is also a proposal that quantum fluctuations of spacetime accumulate with distance. When a length $L$ is measured with a clock and a mirror, making the clock heavier suppresses the spreading of its wave packet, but making it too heavy turns the clock itself into a black hole. Combining these two effects, the proposal holds that an uncertainty

$$
\delta L\gtrsim L^{1/3}\,l_P^{2/3}
$$

remains in any measurement of length [20, 21]. Writing more generally $\delta L\sim L^{1-\alpha}l_P^{\alpha}$, $\alpha=2/3$ corresponds to this proposal (the holographic model) and $\alpha=1/2$ to a random summation of small fluctuations (the random-walk model). If phase fluctuations $\Delta\phi\sim2\pi\,\delta L/\lambda$ accumulate while a photon travels a distance $L$, the images of distant point sources become blurred and interference is lost. This is a candidate mechanism, independent of the properties of the early universe, by which the information carried by each photon is lost with the distance traveled. It cancels the improvement in resolution from a larger aperture, and in the extreme case where interference is lost completely, increasing the number of photons cannot restore the distinction. However, because the images of distant quasars are not blurred, X-ray observations give $\alpha\gtrsim0.58$ and gamma-ray observations give $\alpha\gtrsim0.67$ and $\alpha\gtrsim0.72$; the random-walk model is excluded, and the holographic model also appears to be excluded [22]. This conclusion depends on assumptions about how the fluctuations add up. This essay treats the proposal as a hypothesis strongly constrained by observation.

### 2.2 Information Dispersal and Observability in High-Energy Particle Collisions

In high-energy scattering, information about the initial state is dispersed into many produced particles and correlations among them. Let the state of the total system be $\rho(E)$ and the state of the observable subsystem be $\rho_{\mathrm{obs}}(E) = \operatorname{Tr}_{\mathrm{unobs}}\rho(E)$ ($E \equiv \sqrt{s}$ is the center-of-mass energy).

The quantum Fisher information (QFI) expresses how sensitive a state is to a change in a parameter. Operations that discard unobservable degrees of freedom, such as a partial trace, do not increase the QFI [8]. Metrics that do not increase under coarse-graining (stochastic maps in the classical case, CPTP maps in the quantum case) are fixed uniquely, up to a constant factor, as the Fisher metric for probability distributions on a finite sample space [27]; for quantum states they form a family. The QFI in this essay is the one defined by the symmetric logarithmic derivative (SLD), the smallest in that family [28].

$$
F_Q\!\left[\rho_{\mathrm{obs}}\right](E) \;\le\; F_Q\!\left[\rho\right](E)
$$

What is compared here is the total system and the subsystem at the same energy. The observer's degree of discrimination can be expressed locally by the Bures distance [8].

$$
D_{\mathrm{Bures}}\!\left(\rho_{\mathrm{obs}}(E),\rho_{\mathrm{obs}}(E+\mathrm{d}E)\right)^2 \approx \frac{1}{4}F_Q\!\left[\rho_{\mathrm{obs}}\right](E)\,(\mathrm{d}E)^2 + O\!\left((\mathrm{d}E)^3\right)
$$

This essay considers situations in which, at higher energies, information flows into unobservable degrees of freedom and the QFI of the observable part decreases. The derivation of the QFI and its relation to the precision of energy estimation are summarized in the [supplementary note on the QFI (in Japanese)](補足資料/QFI解説.html).

The two-level model of Appendix 2 is a concrete example of the Spacetime-Limit Phase. Even if the two states of the total system are orthogonal, the trace distance of the observed subsystem is $T=\cos\theta$, which vanishes at $\theta=\pi/2$ ([Appendix 2, Sections 6 and 7](appendix2.en.html)). The information remains in correlations, and the spacetime criteria for discrimination are preserved. Probing localization at still higher energies adds the gravitational back-reaction of Section 2.1, and the structure that defines position and distance itself becomes the issue. This essay connects these two questions through the Dimension-Reduction Phase.

---

## 3. Indistinguishability at Cosmological Limits

Observing distant objects means seeing the past universe through the finite speed of light. The observable past is limited by cosmological horizons [9]. This section shows by equations what makes distinctions harder at the two limits of the past and the future. Optical depth and cosmic variance are used as examples of the Spacetime-Limit Phase, in which distinctions become harder while the spacetime standards are preserved. The loss of rest mass and of scale is used as a hypothetical connection from the Dimension-Reduction Phase to the Zeroth-Order Phase.

### 3.1 The Far Past ($t \to 0$)

The reasons why distant objects are harder to distinguish fall into two kinds. The first is a limit that follows from quantum measurement and the observer's finite resources; given the same physical laws, it holds regardless of what state the universe was in at any epoch. The observer's resources have the physical upper limits described in Section 4.2, which make the upper limit $N_{\max}$ on the number of measurements a definite value, so this is a limit in principle (the value of the upper limit depends on the physical constants and the cosmological constant). The second consists of constraints whose strength is set by the history of our universe: the universe was opaque when the light was emitted ((a) below), and only one sky can be observed ((b)). (a) and (b) also have a core that does not depend on the history of the universe. The relation between angle and photon number and the limit that follows from resources are shown first, and then (a) and (b) are formulated. The content of this section is explained in question-and-answer form in the [supplementary note on observing distant objects (in Japanese)](補足資料/宇宙論的極限の解説.html).

**The angular difference does not vanish through distance alone.** Merely receiving the light emitted by an object allows one to measure its direction of arrival, spectrum, and brightness. To distinguish two positions A and B, the angular difference in the direction of arrival is enough. Distance is used only when converting the angular difference into an actual size $s$. Cosmological distances are obtained by converting redshift into distance with a cosmological model (here, flat ΛCDM) [17].

In flat, non-expanding space, the angular difference between two positions separated transversely by $s$ is $\Delta\theta\simeq s/d$, which becomes smaller with distance. In an expanding universe, the more distant an object, the closer it was to the observer when it emitted its light. For this reason, the angular difference is determined by the angular diameter distance $d_A$ [17].

$$
\Delta\theta=\frac{s}{d_A(z)},\qquad d_A(z)=\frac{d_M(z)}{1+z},\qquad d_M(z)=c\int_0^{z}\frac{\mathrm{d}z'}{H(z')}
$$

Here $z$ is the redshift, $H(z)$ is the Hubble parameter at that epoch, and $d_M$ is the comoving distance, with space assumed flat. Because $d_M$ remains finite (about 14 Gpc) even as $z\to\infty$, $d_A$ reaches a maximum (about 1.8 Gpc) at $z\approx1.6$ and decreases beyond it (the values are computed from the Planck 2018 cosmological parameters [19]). Objects of the same proper size appear larger beyond a certain distance.

On the other hand, the number of photons arriving per unit area per second from an object that emits $\dot N$ photons per second is

$$
\Phi_N=\frac{\dot N}{4\pi d_M^{2}(1+z)}
$$

which decreases with distance [17]. The factor $(1+z)$ arises because time intervals are stretched by the redshift. Because the energy of each photon also becomes $1/(1+z)$, the energy flux can be written as $L/(4\pi d_L^2)$ using the luminosity distance $d_L=(1+z)d_M$. The number of photons actually counted also depends on the observed waveband. When two positions are distinguished by the mean direction of arrival of photons, the ease of distinction is expressed by the ratio of the angular difference to the standard deviation of the mean, $R=\Delta\theta\sqrt N/\sigma_\theta$ ($N$ is the number of photons and $\sigma_\theta$ is the error in the direction of a single photon). Distance makes distinctions harder not through the angle, but through the number of photons and the directional error $\sigma_\theta\sim\lambda_{\mathrm{obs}}/D$ caused by the wavelength stretched by redshift ($\lambda_{\mathrm{obs}}$ is the observed wavelength and $D$ is the telescope aperture). As long as the source keeps emitting light, a longer observation increases the number of photons and compensates for these effects. However, because the aperture, time, and energy available to the observer are finite, there is an upper limit in principle to what can be compensated (Section 4.2). Systematic errors, such as calibration offsets, do not decrease as the number of photons increases.

The same form of limit remains when deciding whether there is one source or two. This essay calls it the **quantum limit on distinguishing two distant sources**. Compare two sources separated by $s$ with a single source of the same total brightness. Even with the optimal quantum measurement, whether they can be distinguished with $N$ detected photons is governed by $N\xi_Q$ [25]. $\xi_Q$ is the quantum Chernoff exponent per photon; if $N\xi_Q\ll1$ the error probability is close to $1/2$, and if $N\xi_Q\ge\ln10$ it is $5\%$ or less [26]. For a circular aperture of diameter $D$ and a small separation, the expected number $\bar N$ of photons detected when a source of power $P$ is observed for a time $T$ gives

$$
\bar N\xi_Q\propto\frac{PT\,D^4s^2}{d_M^4\,(1+z)}
$$

The constant of proportionality contains the detection efficiency and the emitted wavelength $\lambda_e$; the proportionality holds when sources of the same wavelength are compared with the same efficiency. This is the value for the optimal quantum measurement, proportional to $s^2$. With ordinary imaging the same exponent is proportional to $s^4$ and falls faster as the separation becomes smaller [25].

In this expression, no factor $(1+z)$ remains in the per-photon exponent $\xi_Q$. For the optimal quantum measurement and a small separation, $\xi_Q$ is proportional to the square of the ratio of the angular separation to the wavelength. At large distances the angular diameter distance becomes smaller, so the angular separation widens to $s(1+z)/d_M$; the observed wavelength, however, is also stretched by $(1+z)$, so the two cancel in the ratio and $\xi_Q$ is set by the comoving distance $d_M$ alone. Objects of the same proper size appear larger beyond $z\approx1.6$ (the value for flat ΛCDM), yet each photon does not make them easier to distinguish. The single factor $(1+z)$ in the expression comes from the smaller number of photons that arrive. Assuming a transparent universe, $d_M$ remains finite, so at very large distances $\bar N\xi_Q$ decreases in proportion to $1/(1+z)$. Because the observation time $T$ and the aperture $D$ have the upper limits of Section 4.2, which make $N_{\max}$ a definite value, a lower bound remains on the separation that can be distinguished, even when the observer uses all available resources.

This expression is an upper limit under ideal conditions. It assumes that the separation is well below the diffraction limit; that the hypotheses are limited to two, "one source" and "two sources"; that the two sources are equally bright and mutually incoherent, with the centroid of the light and the total brightness known; that the light is weak thermal light in a narrow waveband, with photon numbers following a Poisson distribution; that there is no background light or detector noise; and that the axis of the optimal measurement that sorts the light into spatial modes (SPADE) is aligned with the center of the sources. When these conditions fail, the value actually obtained is smaller than this upper limit. The attenuation due to the opacity of the universe at the time of emission is added as a factor in (a) below. The derivation and coefficients are given in Section 3.7 of the [supplementary note on observing distant objects (in Japanese)](補足資料/宇宙論的極限の解説.html).

In the round-trip model of Section 1, the wave packet of the object spreads while the signal travels, so the error grows with distance. This is a limit on knowing the "present state". What cosmology asks about is the state at the time the light was emitted. Because light carries the information of that time, the travel time does not blur this information.

Apart from the upper limit on the observer's resources, there are two constraints whose strength is set by the history of our universe. The core of each depends neither on expansion nor on the history of the universe.

The cosmic microwave background (CMB) carries information from the surface of last scattering, about 380,000 years after the beginning of the universe, and its temperature fluctuations are about $10^{-5}$ of the mean [10]. These tiny fluctuations are the "distinguishable structural information" that seeds later galaxies and large-scale structure.

**(a) The record carried by photons fades.** Before the surface of last scattering, the universe was hot and atoms were ionized, so photons were scattered repeatedly by free electrons. If the optical depth along the line of sight is $\tau(z)$, the probability that a photon arrives without being scattered is $e^{-\tau}$. This is expressed by the following model. If scattered photons follow a thermal distribution $Q_0$ and carry no difference between the two states A and B being compared, the distributions of measurement outcomes are

$$
P_{A}(y)=e^{-\tau}Q_{A}(y)+\left(1-e^{-\tau}\right)Q_0(y),\qquad
P_{B}(y)=e^{-\tau}Q_{B}(y)+\left(1-e^{-\tau}\right)Q_0(y)
$$

where $Q_A, Q_B$ are the distributions of photons that arrive unscattered. Because the $Q_0$ term cancels in the difference, the total variation distance of Section 1 satisfies

$$
D_{AB}=e^{-\tau(z)}\,D\!\left(Q_A,Q_B\right)\le e^{-\tau(z)}
$$

where $D(Q_A,Q_B)$ is the total variation distance between $Q_A$ and $Q_B$. This is the cosmological form of the relation $D_{AB}\le p$ that holds when the record conveying the difference appears only with probability $p$. The surface of last scattering ($z\approx1090$) is where $\tau\approx1$ [19]; before it, $\tau\gg1$, and the power to distinguish by photons approaches zero exponentially. On the other hand, the universe after the surface of last scattering is nearly transparent, and the optical depth from there to the present is only $\tau\approx0.054$ [19]. What fades the record carried by photons is not the length of the path, but the opacity of the universe at the time the light was emitted. Because neutrinos and gravitational waves arrive from earlier epochs, this is a case in which distinctions are lost for one kind of observation while the spacetime framework is preserved.

The core of this expression does not depend on the history of the universe. When a signal passes through a channel that replaces it, with probability $1-p$, by a fixed state that carries no difference, the total variation distance between any two states (the trace distance, for quantum states) becomes $p$ times its original value. Even for more general channels, these distances do not increase. What the history of the universe sets is the value $p=e^{-\tau}$, that is, how opaque the universe was when the light was emitted.

This is added to the quantum limit on distinguishing two distant sources through a separate model. Because the Chernoff exponent itself is not multiplied by $p$, the model used here does not use scattered photons and counts only unscattered ones. The number of usable photons is then multiplied by $e^{-\tau}$, so under the same approximation as in Section 3.7 of the supplementary note, the upper bound on the error probability becomes

$$
P_e\le\frac{1}{2}\exp\left(-e^{-\tau}\,\bar N\xi_Q\right)
$$

The factor $e^{-\tau}$ enters the exponent. Distinguishing the epoch with $\tau\gg1$ by light requires multiplying the resources by $e^{\tau}$. Epochs for which $e^{\tau}$ times the resources exceeds the upper limits of Section 4.2 cannot be distinguished by light.

This mechanism works independently of expansion. Photons produced at the center of the Sun are scattered repeatedly and take tens of thousands of years or more to reach the surface, so the center cannot be seen in light and is observed only through neutrinos, which are not scattered. Even in non-expanding space filled with a uniform gas, $\tau=n\sigma d$ for number density $n$ and scattering cross-section $\sigma$, and $D_{AB}\le e^{-n\sigma d}$ decreases exponentially with distance. Because a single event emits a limited number of photons, the number of photons arriving unscattered cannot be increased by observing longer. How much of the difference scattered photons preserve depends on the type of scattering (the polarization of the CMB is produced by scattering). The equation above is a model that ignores this.

**(b) Only one sky can be observed.** An observer can see only one universe, and the statistics of the temperature fluctuations must be estimated from that single realization. Because there are only $2\ell+1$ independent modes for each angular multipole $\ell$, an error independent of instrument performance remains in the power spectrum $C_\ell$ of the fluctuations (cosmic variance) [18]. Cosmic variance is determined not by distance but by the angular scale ($\ell$).

$$
\frac{\Delta C_\ell}{C_\ell}=\sqrt{\frac{2}{2\ell+1}},\qquad
F_{ij}=\sum_{\ell}\frac{2\ell+1}{2}\,\frac{\partial_i C_\ell\,\partial_j C_\ell}{C_\ell^{2}}
$$

$F_{ij}$ is the Fisher information matrix for the cosmological parameters $\theta_i$, with $\partial_i=\partial/\partial\theta_i$. The contribution of each $\ell$ is summed with the cosmic variance $(\Delta C_\ell)^2=2C_\ell^2/(2\ell+1)$ in the denominator. Cosmic variance gives a statistical constraint that cannot be removed by observation time or instrument performance. If the difference in $C_\ell$ between two cosmological models is smaller than the cosmic variance, the two are hard to tell apart from that sky. However, because the two distributions do not coincide, this is not strict indistinguishability but an example of a limit of discrimination that preserves the spacetime standards. This matrix has the same form as the quantum Fisher information matrix that defines the effective dimension in Section 4.2. The factor $(2\ell+1)/2$ plays the role of the number of measurements $N$, and the lower the $\ell$ (the larger the angle), the less information can be read. This limit, too, comes from the observer being able to see only one realization and therefore does not depend on expansion.

The core of this constraint does not depend on the history of the universe either. An observer can see only the inside of their own past light cone. If the fluctuations are Gaussian and the modes statistically independent, the number of independent modes that can be measured there is set by the observable volume and by the smallest scale on which the fluctuations can be read. If that smallest scale has a physical lower limit (such as the upper limits on resources in Section 4.2), the number is finite and limits the ability to discriminate between models that predict the fluctuations statistically. The $2\ell+1$ of the CMB is the concrete form of this limit for a two-dimensional sky. Using three-dimensional distributions increases the number of modes, and non-Gaussian fluctuations change the amount of information that can be read. What the history of the universe sets is which scales of fluctuation remain, and in how much volume. Knowing the map of the one sky itself is not subject to the constraint of cosmic variance.

Thus (a) and (b), which make distinctions in the past harder, do not depend on whether the universe expands. What expansion adds is only that distant objects do not keep appearing smaller with distance. Going still further back, the limit of applicability of the classical description of spacetime becomes the issue [4].

[Appendix 2, Section 10](appendix2.en.html) gives an estimate in which the maximum resources available to the observer in principle are substituted into the quantum limit on distinguishing two distant sources. Three principles of this essay are adopted: (1) the observation time has an upper limit; (2) the size of the aperture has an upper limit; (3) the precision of a measurement with a single photon is set by its wavelength (energy), and with $N$ photons it improves by up to a factor $\sqrt N$. When the aperture is limited to the size that can be held together against the expansion of the universe, under the conditions of the table in the appendix (an upper limit on the observation time of $10^{11}$ years as an example, $z\ge0.1$) the limit set by the number of photons remains above the Planck length. The measurement axis can be aligned with the received light; that limit is of the same order as the limit set by the number of photons and does not form a separate wall. In the example with a fixed source, within the range where enough photons arrive, the smallest separation that can be distinguished grows monotonically further into the past: nearby because the comoving distance grows, and far away because the upper limit on the observation time makes the photons received decrease as $1/(1+z)$. Because the comoving distance levels off, the tendency of the smallest separation to grow without bound the further one goes back is a consequence of the upper limit on the observation time (the values at very large $z$ are computational extrapolations). Before the surface of last scattering, the opacity of (a) acts in addition. This is an example consistent with distinctions becoming more ambiguous the further one goes back into the past, and an estimate of this essay based on the three principles above and the example with a fixed source.

### 3.2 The Far-Future Limit ($t \to +\infty$)

Toward the future, scenarios have been presented in which the universe keeps expanding and approaches a heat death (Big Freeze) in which the available free energy is exhausted [11]. Penrose's conformal cyclic cosmology (CCC) holds that in this far future, remaining particles such as electrons lose their rest mass and the universe acquires scale invariance, and it connects this future conformally to the Big Bang of the next universe [12]. On the future side, the following two things cause distinctions to be lost.

**(c) Clocks disappear.** A particle with rest mass $m$ acts as a clock that ticks at its own frequency $\nu_m$ [12]. With metric signature $(-,+,+,+)$ and proper time written $\tau_{\mathrm{prop}}$,

$$
\nu_m=\frac{mc^2}{h}\xrightarrow[m\to0]{}0,\qquad
\mathrm{d}\tau_{\mathrm{prop}}^{2}=-\frac{\mathrm{d}s^2}{c^2}=0\quad(\text{worldline of a massless particle})
$$

When rest mass disappears, clocks with their own frequencies disappear. The worldline of a massless particle is null ($\mathrm{d}s^2=0$), and no proper time elapses along it. Because null curves do not change when the metric is changed as $g\to\Omega^2 g$, no means remains to distinguish scales of time or length. This argument and its extension to all dimensionful physical quantities are given in [Appendix 3, Section 3](appendix3.en.html).

**(d) The reachable range is limited.** In a future dominated by the cosmological constant, the scale factor becomes $a(t)\propto e^{H_\Lambda t}$, and the range from which the observer can receive signals from now on is limited to the inside of the event horizon $r_H=c/H_\Lambda$ [9]. This horizon has a temperature [15].

$$
T_{\mathrm{GH}}=\frac{\hbar H_\Lambda}{2\pi k_B}
$$

Signals from outside the horizon do not arrive. Light from objects approaching the horizon is redshifted exponentially, and its energy eventually becomes smaller than the thermal radiation at this temperature.

| Reason | Equation | What becomes harder or is lost | Phase |
|---|---|---|---|
| (a) The record carried by photons fades | $D_{AB}\le e^{-\tau}$ | Distinction by photons | Spacetime-Limit Phase |
| (b) Only one sky | $\Delta C_\ell/C_\ell=\sqrt{2/(2\ell+1)}$ | Distinction of large-angle statistics | Spacetime-Limit Phase |
| (c) Clocks disappear | $\nu_m=mc^2/h\to0$ | Scales of time and length | From the Dimension-Reduction Phase to the Zeroth-Order Phase |
| (d) The reachable range is limited | $r_H=c/H_\Lambda$, $T_{\mathrm{GH}}$ | Distinctions beyond the horizon | Spacetime-Limit Phase |

In (a), (b), and (d), distinctions become harder while the spacetime framework is preserved. In (c), the scales that support distinctions are themselves lost. A uniform distribution is to be distinguished from a situation in which distinction by position and time itself does not hold. This essay calls the latter the Zeroth-Order Phase.

---

## 4. A Tentative Connection of the Three Phases: From Four Limits to the Zeroth-Order Phase

### 4.1 Comparing the Four Limits

1. **The earliest universe ($t \to 0$):** a region where the classical description of spacetime itself ceases to hold.
2. **The far future of the universe ($t \to +\infty$):** a limit in which, after the heat death, scales of length and time lose their meaning in the CCC picture.
3. **The microscopic localization limit ($\Delta x \to 0$):** a region where the geometric picture of spacetime reaches its limit at the Planck scale.
4. **High-energy scattering ($E = \sqrt{s} \to \infty$):** a region where the limits of resolution due to information dispersal and gravitational back-reaction are at issue.

These differ in physical mechanism and in scale, but all point to a common question: "how far does the boundary for distinguishing something as something hold?" Each limit is an entrance for considering the connection of the three phases from a different side.

| Limit | Clues for the Spacetime-Limit and Dimension-Reduction Phases | Question toward the Zeroth-Order Phase |
|---|---|---|
| The earliest universe | Discrimination of initial structure, and the limit of applicability of the classical description of spacetime | Under what conditions do distinctions by position and time begin to hold? |
| The far future | The decrease of free energy, and the loss of scale in CCC | Can the loss of scale be connected to the failure of spacetime discrimination? |
| The microscopic localization limit | The crossing of the energy needed for localization and gravitational back-reaction; the spectral dimension | How can the transformation of the geometry that supports localization be expressed as a decrease in the effective dimension? |
| High-energy scattering | The decrease of the subsystem QFI, and the gravitational constraint on probing | How can the restriction of degrees of freedom be tied to the transformation of the spacetime criteria for discrimination? |

The four limits need not be the same physical state. This comparison organizes, in the language of the three phases, which distinctions are lost and which remain at each limit. Section 9 of Appendix 2 adds the limit of infinitesimal time division ($\Delta t \to 0$) as an independent line of inquiry and compares five limit regions.

### 4.2 From the Spacetime-Limit Phase to the Dimension-Reduction Phase

In the Spacetime-Limit Phase, one can describe where an object is, when it is measured, and what it is compared with. Within that framework, the states of the object can no longer be distinguished even when all available measurements are used. In the Dimension-Reduction Phase, the framework that supports discrimination itself is transformed, and fewer spacetime directions can be distinguished independently by the observer.

This "number of independently distinguishable directions" is defined, in the language of measurement, by two separate quantities ([Appendix 1, Section 2.1](appendix1.en.html)). The first is the effective dimension $D_{\mathrm{eff}}$. Let $\kappa_i$ ($i=1,\dots,4$) be the eigenvalues of the quantum Fisher information matrix built from the measurements available to the observer, made dimensionless by the required resolution, and let $N$ be the number of measurements. Then

$$
D_{\mathrm{eff}}=\sum_{i=1}^{4}\frac{N\kappa_i}{1+N\kappa_i},\qquad n=4-D_{\mathrm{eff}},\qquad 0\le D_{\mathrm{eff}}\le4
$$

A direction that can be read well contributes nearly 1, and one that cannot be read contributes nearly 0, so $D_{\mathrm{eff}}$ decreases continuously as sensitivity decays (Figure 2). For finite $N$, $D_{\mathrm{eff}}<4$ even for an ordinary four-dimensional measurement. For this reason, $D_{\mathrm{eff}}$ at finite $N$ is used as an auxiliary indicator of how well each direction can be read under those measurement conditions, and not to classify phases.

The second is the rank $d_O$ of the matrix, constant over a range of the parameters. The states used here represent records, such as clocks, rulers, and signals, that the observer can use to construct spacetime relations. This separates the case in which an arbitrarily chosen object merely does not respond to position or time from the case in which the observer cannot construct the distinction in principle. As the number of measurements increases without bound, $D_{\mathrm{eff}}$ approaches the rank. States along a direction in which the sensitivity is zero throughout a range of the parameters (the kernel of the matrix) are strictly indistinguishable for the observer ([Appendix 1, Section 2.1 (6)](appendix1.en.html)). A drop in rank at a single point does not qualify. The case in which pairs of states become harder to distinguish while $d_O=4$ is the Spacetime-Limit Phase, and $d_O<4$ is the Dimension-Reduction Phase. A drop in $d_O$ is a loss of distinctions for the observer, not a disappearance of degrees of freedom. The rank counts the directions in parameter space along which states can be distinguished under continuous changes of the parameters; it counts neither the signature of the metric nor global distinctions ([Appendix 1, Section 2.1](appendix1.en.html)).

The decay of sensitivity and the drop in rank play different roles. The eigenvalues, and $D_{\mathrm{eff}}$ under fixed measurement conditions, express how much the sensitivity has weakened; a drop in rank expresses that an independent direction has been lost. In a process in which sensitivity is lost smoothly, the rank need not drop in steps. Both are indicators of approaching the Zeroth-Order Phase.

The number of measurements $N$ has a fundamental upper limit set by the resources available to the observer. The quantum Fisher information about direction obtained from a single photon received through an aperture $D$ does not exceed about $(2\pi D/\lambda)^2$. Because the light received is not a state prepared by the observer, precision cannot be increased by entangling the photons. The aperture is limited by the causally connected region and by the gravity of the apparatus itself, and the observation time by the lifetime of the source and the event horizon. The apparatus that records the results also has, for size $R$ and energy $E$, an upper limit on the information it can store, $I\le2\pi ER/(\hbar c\ln2)$ [23], and an upper limit on the rate at which it can change state, $2E/(\pi\hbar)$ [24]. Finiteness of resources alone does not fix a limit, because every finite value has a larger one. Because of these physical upper limits, $N$ has a definite upper limit $N_{\max}$, and directions with $N_{\max}\kappa_i\ll1$ cannot be read even in principle, whichever measurement is chosen ([Appendix 1, Section 2.1 (4)](appendix1.en.html)). For the quantum limit on distinguishing two distant sources in Section 3.1, this corresponds to $N_{\max}\xi_Q\ll1$. In this optical model, $\xi_Q\simeq F_Q\theta^2/4$ for a small angular separation $\theta$. Like $\kappa_i$, it corresponds to the product of the information obtained from one photon and the square of the required resolution. However, $\xi_Q$ is an exponent for discriminating two particular states, while $\kappa_i$ is a dimensionless eigenvalue of the quantum Fisher information matrix; their definitions differ, and in general they are not equal. The difficulty of distinction in the Spacetime-Limit Phase thus becomes a limit in principle, due not to instrument performance but to the observer having only finite resources. Because the rank $d_O$ is defined in the limit in which $N$ increases without bound, this upper limit does not change the classification of phases. The upper limit on records is also tied to the area law of entropy in Section 4.4.

<figure class="essay-figure" style="margin:1.5rem 0">
<svg viewBox="0 0 300 316" role="img" aria-labelledby="fig2-title fig2-desc" style="display:block;width:100%;max-width:360px;height:auto;margin:0 auto;color:inherit" font-size="15">
<title id="fig2-title">Example of a continuous decrease of the effective dimension</title>
<desc id="fig2-desc">The horizontal axis is the approach to the limit, and the vertical axis is the effective dimension at a finite number of measurements, with ticks from 0 to 4. The curve is near 4 at the left end, decreases continuously to the right, and is near 0 at the right end. At point A on the curve nearly four directions can be read, at point B about two directions can be read, and at point C the effective dimension is nearly 0, approaching the Zeroth-Order Phase.</desc>
<text x="10" y="16" fill="currentColor">D<tspan baseline-shift="sub" font-size="12">eff</tspan></text>
<g transform="translate(0,16)">
<g fill="none" stroke="currentColor">
<path d="M50,20 L50,180 L285,180" stroke-width="1.5"/>
<path d="M45,20 H50 M45,60 H50 M45,100 H50 M45,140 H50 M45,180 H50" stroke-width="1.5"/>
<path d="M50,21 L59,22 L68,24 L77,27 L86,31 L95,37 L104,44 L113,52 L122,61 L131,71 L140,80 L149,90 L158,100 L168,110 L177,120 L186,129 L195,139 L204,148 L213,156 L222,163 L231,169 L240,173 L249,176 L258,178 L267,179 L276,179 L285,180" stroke-width="3"/>
</g>
<g fill="currentColor">
<circle cx="61" cy="23" r="5"/>
<circle cx="158" cy="100" r="5"/>
<circle cx="274" cy="179" r="5"/>
<text x="64" y="44" font-weight="700">A</text>
<text x="166" y="96" font-weight="700">B</text>
<text x="262" y="166" font-weight="700">C</text>
<text x="36" y="25" text-anchor="end">4</text>
<text x="36" y="105" text-anchor="end">2</text>
<text x="36" y="185" text-anchor="end">0</text>
<text x="285" y="204" text-anchor="end">Approach to the limit →</text>
<text x="10" y="236">A  Nearly 4 directions readable</text>
<text x="10" y="260">B  About 2 directions readable</text>
<text x="10" y="284">C  Toward Zeroth-Order (D<tspan baseline-shift="sub" font-size="12">eff</tspan> → 0)</text>
</g>
</g>
</svg>
<figcaption>Figure 2. Continuous decrease of the effective dimension at a finite number of measurements (example). Drawn assuming that the sensitivities $N\kappa_i$ of the four directions fall below 1 at different points as the limit is approached. The curve shows how well each direction can be read; phases are classified by the rank $d_O$.</figcaption>
</figure>

### 4.3 The Undifferentiated Zeroth-Order Phase

**The Zeroth-Order Phase is a state in which the conventional criteria of discrimination by position, distance, and time can no longer be applied by the observer.** The independently distinguishable spacetime directions are lost, the procedure $\mathcal R_O$ for assigning times and distances from observational records does not hold, and states are indistinguishable for the observer ($\sim_O$). It is not required that the quantum Fisher information matrix be defined there. Not only can differences between objects not be measured, but the framework that supports "where", "how much", and "when" itself loses its meaning. In this sense it is called "undifferentiated".

This essay holds that the path to this state passes through the Dimension-Reduction Phase, in which independent directions are progressively lost. This connection is a hypothesis of this essay, organized in Section 6.

Even if geometric structure remains in a mathematical or conceptual description, it is the Zeroth-Order Phase for an observer if the observer cannot construct measurement standards of position, distance, and time by any available means.

Conversely, states in which information is merely hidden in correlations, states in which the observer can use conformal or causal structure as measurement standards, and states in which spacetime distinctions can be constructed by relational descriptions are not included in the Zeroth-Order Phase. These are states in which the structure of discrimination is preserved, and they are placed in the Spacetime-Limit Phase or the Dimension-Reduction Phase.

### 4.4 Existing Footholds Linking the Microscopic and the Macroscopic

Gravitational constraints on energy and entropy give an upper limit on the number of degrees of freedom that can be discriminated, and provide footholds for considering the connection of the three phases quantitatively.

| Relation | What it limits | Position in the three phases |
|---|---|---|
| CKN scaling [13] | The number of field modes that can be resolved independently in a region | A clue to reading the transition from the Spacetime-Limit Phase to the Dimension-Reduction Phase |
| Covariant entropy bound [14] | The number of distinguishable states (determined by area) | The upper limit on information is set by area rather than volume; a clue to reading the Dimension-Reduction Phase |
| de Sitter entropy [15] | The number of states an observer in an accelerating universe can distinguish | A future-side clue toward the Zeroth-Order Phase, in which the total amount of distinction closes to a finite value in the far future |

**(1) The relation between ultraviolet and infrared (CKN scaling).** Cohen, Kaplan, and Nelson applied the argument that probing a smaller region requires more energy, so that gravity can no longer be ignored, to the size $L$ of a region and the ultraviolet cutoff $\Lambda$ of a field theory [13].

$$
L^3\Lambda^4 \lesssim L M_P^2
$$

Natural units $c=\hbar=1$ are used here, and $M_P$ denotes the Planck mass scale. Gravity puts an upper limit on the number of field modes that can be resolved independently in a region. As resolution is increased in the Spacetime-Limit Phase, at some point the number of independent degrees of freedom stops increasing. This essay reads this point as the transition from the Spacetime-Limit Phase to the Dimension-Reduction Phase.

**(2) The upper limit on the number of distinguishable states (covariant entropy bound).** Bousso's covariant entropy bound limits the entropy on a light sheet attached to a surface of area $A$ [14]. Entropy is expressed as a dimensionless quantity in units of $k_B$.

$$
S \le \frac{A}{4l_P^2}
$$

If an equal mixture of $N$ allowed states is counted as $S=\ln N$ and the same bound can be applied to that mixture, the number of distinguishable states can be read as $N \le \exp\left(A/4l_P^2\right)$. That the number of states is determined by area rather than volume is a precedent for the way information is counted changing with scale. However, this is an upper limit on the amount of information and differs from the effective dimension of this essay (a quantity based on the sensitivity of observed states). This essay takes it as a clue to reading the Dimension-Reduction Phase, and computing the correspondence between the two quantities is left for future work.

**(3) The entropy of the cosmological horizon.** Gibbons and Hawking associated an entropy $S = A/4l_P^2$ with the horizon of de Sitter space [15]. The number of states an observer in a universe that keeps accelerating can distinguish is bounded to a finite value by the area of the horizon. This is a foothold showing that, in the far-future limit ($t\to+\infty$), the total amount of distinction available to the observer closes to a finite value, and it is a future-side clue toward the Zeroth-Order Phase.

---

## 5. Conclusion and Outlook

This essay has organized the limits of discrimination for an observer into three phases: the Spacetime-Limit Phase, the Dimension-Reduction Phase, and the Zeroth-Order Phase. Building on the physical constraints given by existing theories, it has defined the effective dimension and the rank from the observables available to the observer and the quantum Fisher information matrix, and presented the skeleton of a model that connects to the Zeroth-Order Phase through the Dimension-Reduction Phase.

The next task is to specify, for concrete physical systems, the set of observables $\mathcal A_O$ and the families of states to be compared, and to compute the relations among the degree of discrimination, scale, and effective dimension [8, 16]. Computing the correspondence between the spectral dimension or the area law of entropy and the effective dimension of this essay is also part of this task.

---

## 6. On the Status of the Claims of This Essay

To keep the argument clear, caveats in the main text have been kept to a minimum. The kinds of claims are summarized here.

| Kind | Content in this essay | How to read it |
|---|---|---|
| **Results of existing theory** | Definitions and properties of the total variation distance, the trace distance, and the QFI; that the QFI does not increase under a partial trace; wave-packet spreading and SQL-type estimates; the estimate of the Planck length; numerical results on the spectral dimension; the diffraction limit and the standard quantum limit; the quantum Chernoff bound for discriminating two point sources; that the total variation distance and the trace distance decrease through a channel that replaces the signal by a state carrying no difference (the data-processing inequality); that for Gaussian fluctuations the number of independent modes is set by the observable volume and the smallest scale; the Bekenstein bound and the Margolus–Levitin bound; the proposal that spacetime fluctuations accumulate with distance and its observational constraints; the angular diameter distance, the luminosity distance, and the optical depth; that the center of the Sun cannot be seen in light; cosmic variance; the event horizon and the Gibbons–Hawking temperature; CKN scaling; the covariant entropy bound; de Sitter entropy; the conformal connection of CCC | They hold under the conditions of the cited sources. The derivation of the Planck length is an estimate, not a proof of a minimum length. The distances and values of $d_A$ in Section 3.1 assume conversion of redshift to distance with flat ΛCDM; $D_{AB}\le e^{-\tau}$ assumes that scattered photons carry no difference; the formula for cosmic variance assumes Gaussian fluctuations over the full sky. The quantum limit on distinguishing two distant sources is an upper limit under ideal conditions, such as the absence of background light, and actual values are lower. $P_e\le\frac{1}{2}\exp(-e^{-\tau}\bar N\xi_Q)$ is an application within a model that does not use scattered photons. The strength of (a) and (b) (the value of $\tau$, and the CMB being a two-dimensional sky) rests on observed values for our universe. Optical depth and cosmic variance make distinctions harder; they do not give strict indistinguishability. The accumulation of spacetime fluctuations with distance is an existing hypothesis, and its simple forms are nearly excluded by observation. CCC is a cosmological model still under study |
| **Definitions of this essay** | The epistemological position of the introduction; the effective dimension $D_{\mathrm{eff}}$ and the rank $d_O$; the naming of the three phases; the procedure $\mathcal R_O$ | Being definitions, they are evaluated not by truth but by whether they help describe physics |
| **Hypotheses of this essay** | That the three phases form one connection; that the QFI of the observable part decreases at high energy; reading CKN, entropy bounds, and the spectral dimension as clues to the Dimension-Reduction Phase; assigning the four reasons of Section 3 to the three phases as in the table; reading, in Section 3.1, the quantum limit on distinguishing two distant sources as a limit in principle due to the upper limits on resources, and separating (a) and (b) into their core and the strength set by the history of the universe; the estimate of Appendix 2, Section 10 (that, when the observation time and the aperture have upper limits and the precision of a measurement is set by the wavelength and number of the photons, the smallest distinguishable separation grows monotonically further into the past in the example with a fixed source); that the CCC connecting boundary and the Big Bang singularity limit correspond to the Zeroth-Order Phase (including the "assumed examples" in the table of the introduction) | Even if the hypotheses fail, the organization of discrimination limits in Sections 1 and 2 remains as results of existing theory |

---

## Appendices

- [Appendix 1: The Logical Background of the Three-Phase Model of Observation Limits](appendix1.en.html)
- [Appendix 2: Mathematical Notes on Observation Limits and Distinguishability](appendix2.en.html)
- [Appendix 3: A Tentative Link Between the CCC Connecting Boundary and the Zeroth-Order Phase](appendix3.en.html)
- [Supplementary note: Information dispersal and observability from the quantum Fisher information (QFI) (in Japanese)](補足資料/QFI解説.html)
- [Supplementary note: Observing distant objects and the difficulty of distinction (a guide to Section 3) (in Japanese)](補足資料/宇宙論的極限の解説.html)

---

## Disclosure of AI Assistance

Generative AI tools (Claude, Codex, GitHub Copilot, and others) were used to draft and revise the text, translate it into English, create the figures, and carry out checks. The English translation was reviewed by an AI other than the one that translated it. 5garashi.com Design Office made the judgments on the content and is responsible for it.

---

## References

1. IBM Quantum Learning, "Quantum state discrimination and tomography".
2. V. B. Braginsky and F. Ya. Khalili, *Quantum Measurement*, ed. K. S. Thorne (Cambridge University Press, 1992).
3. H. P. Yuen, "Contractive States and the Standard Quantum Limit for Monitoring Free-Mass Positions", Phys. Rev. Lett. 51(9), 719-722 (1983).
4. S. Hossenfelder, "Minimal Length Scale Scenarios for Quantum Gravity", Living Rev. Relativ. 16, 2 (2013).
5. S. Carlip, "Spacetime foam: a review", Rep. Prog. Phys. 86(6), 066001 (2023).
6. S. Carlip, "Dimension and dimensional reduction in quantum gravity", Class. Quantum Grav. 34, 193001 (2017), arXiv:1705.05417.
7. J. Ambjørn, J. Jurkiewicz, and R. Loll, "Spectral dimension of the universe is scale dependent", Phys. Rev. Lett. 95, 171301 (2005).
8. S. L. Braunstein and C. M. Caves, "Statistical distance and the geometry of quantum states", Phys. Rev. Lett. 72, 3439 (1994); J. Liu, H. Yuan, X.-M. Lu, and X. Wang, "Quantum Fisher information matrix and multiparameter estimation", J. Phys. A: Math. Theor. 53, 023001 (2020).
9. T. M. Davis and C. H. Lineweaver, "Expanding Confusion: Common Misconceptions of Cosmological Horizons and the Superluminal Expansion of the Universe", Publ. Astron. Soc. Aust. 21(1), 97-109 (2004).
10. NASA Imagine the Universe!, "Inflation in the Universe".
11. NASA Science, "Expand our Knowledge of Dark Energy".
12. R. Penrose, "On the Gravitization of Quantum Mechanics 2: Conformal Cyclic Cosmology", Foundations of Physics 44(8), 873-890 (2014).
13. A. G. Cohen, D. B. Kaplan, and A. E. Nelson, "Effective field theory, black holes, and the cosmological constant", Phys. Rev. Lett. 82, 4971 (1999).
14. R. Bousso, "The holographic principle", Rev. Mod. Phys. 74, 825 (2002).
15. G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation", Phys. Rev. D 15, 2738 (1977).
16. R. Haag, *Local Quantum Physics* (Springer, 2nd ed., 1996).
17. D. W. Hogg, "Distance measures in cosmology", arXiv:astro-ph/9905116 (1999).
18. L. Knox, "Determination of inflationary observables by cosmic microwave background anisotropy experiments", Phys. Rev. D 52, 4307-4318 (1995).
19. Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters", Astron. Astrophys. 641, A6 (2020).
20. F. Károlyházy, "Gravitation and quantum mechanics of macroscopic objects", Il Nuovo Cimento A 42, 390-402 (1966).
21. Y. J. Ng and H. van Dam, "Limit to space-time measurement", Mod. Phys. Lett. A 9, 335-340 (1994).
22. E. S. Perlman, S. A. Rappaport, W. A. Christiansen, Y. J. Ng, J. DeVore, and D. Pooley, "New Constraints on Quantum Gravity from X-Ray and Gamma-Ray Observations", Astrophys. J. 805, 10 (2015), arXiv:1411.7262.
23. J. D. Bekenstein, "Universal upper bound on the entropy-to-energy ratio for bounded systems", Phys. Rev. D 23, 287-298 (1981).
24. N. Margolus and L. B. Levitin, "The maximum speed of dynamical evolution", Physica D 120, 188-195 (1998), arXiv:quant-ph/9710043.
25. X.-M. Lu, H. Krovi, R. Nair, S. Guha, and J. H. Shapiro, "Quantum-optimal detection of one-versus-two incoherent optical sources with arbitrary separation", npj Quantum Inf. 4, 64 (2018), arXiv:1802.02300.
26. K. M. R. Audenaert, J. Calsamiglia, R. Muñoz-Tapia, E. Bagan, Ll. Masanes, A. Acín, and F. Verstraete, "Discriminating States: The Quantum Chernoff Bound", Phys. Rev. Lett. 98, 160501 (2007).
27. N. N. Chentsov, *Statistical Decision Rules and Optimal Inference*, Translations of Mathematical Monographs 53 (American Mathematical Society, 1982); Russian original: Nauka, Moscow, 1972.
28. D. Petz, "Monotone metrics on matrix spaces", Linear Algebra Appl. 244, 81-96 (1996). [Paper](https://doi.org/10.1016/0024-3795(94)00211-8)

---

**Author**: 5garashi.com Design Office  
**Last updated**: 2026-11-08 JST
