---
title: 'Observation Limits and the Undifferentiated Origin: An Epistemological Inquiry from Quantum Measurement to Cosmology'
lang: en
math: true
description: An exploratory essay distinguishing the inability to discriminate states from the breakdown of the criteria for discrimination, and examining the Zeroth-Order Phase through four limits.
---
<!--
  File: zerothOrderPhase.en.md
  Description: Observation limits and the undifferentiated origin: an English translation of the Japanese essay
  Author: 5garashi.com Design Office
  Created: 2026-10-31
  Last updated: 2026-11-04 JST
  Version: 1.2.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Observation Limits and the Undifferentiated Origin: An Epistemological Inquiry from Quantum Measurement to Cosmology

**Author:** 5garashi.com Design Office

**Version:** <span data-version>1.2.0</span>　**Last updated:** 2026-11-04 JST

---

## Introduction: The Epistemological Question of Indistinguishability

This essay distinguishes two stages: the inability to discriminate objects or states, and the breakdown of the very criteria of position, distance, and time that support discrimination. It tentatively calls the limit of the latter the “undifferentiated Zeroth-Order Phase” and examines it through four limits: the earliest universe, the far future, microscopic localization, and high-energy scattering. The Zeroth-Order Phase is a conceptual proposal in this essay, rather than a known physical state or an experimentally established classification of phases.

The inquiry adopts the following premise:

> **Two states that cannot, even in principle, be distinguished by any observational means available to an observer are treated as the same physical state for that observer.**

This is a definition concerning the physical description accessible to an observer. It does not mean that the states of the total system, independently of that observer, are identical.

Using quantum measurement models and constraints from existing theories as guides, the discussion extends from the inability to discriminate states to the breakdown of the criteria for discrimination. It does not, however, establish that the four limits reach the same state or that the first stage necessarily leads to the second. The following sections distinguish model assumptions, estimates based on existing theories, and this essay’s hypotheses.

---

## 1. Probabilistic Discrimination and the Standard Quantum Limit

To formulate how difficult it is to distinguish physical states, consider the probability distributions $P_A(y)$, $P_B(y)$ of measurement outcomes for two states A and B. A classical statistical measure of their overlap, the total variation distance $D_{AB}$, is defined as follows [1].

$$
D_{AB} = \frac{1}{2}\int \left|P_A(y)-P_B(y)\right|\,\mathrm{d}y,\qquad 0 \le D_{AB} \le 1
$$

$D_{AB} = 1$ means perfect distinguishability, whereas $D_{AB} = 0$ means that the states cannot be distinguished by that measurement: their outcome distributions coincide [1].

For an assumed family of free-electron states, the position width has an SQL-type minimum. Consider a simplified model in which a signal makes a round trip to an electron at a distance d from the observer. During the round-trip time $\tau = \frac{2d}{c}$, the free electron’s wave packet—a minimum-uncertainty Gaussian with no initial position–momentum correlation—spreads spatially according to the Schrödinger equation. If its initial width is $\sigma_0$, the position uncertainty (standard deviation) $\Delta x(\tau)$ after a time τ is

$$
\Delta x(\tau) = \sqrt{\sigma_0^2 + \left(\frac{\hbar\tau}{2m\sigma_0}\right)^2}
$$

The term $\frac{\hbar}{2\sigma_0}$ comes from the initial momentum uncertainty (standard deviation) $\Delta p$ of the quantum state itself, which manifests as spatial spreading over time. Optimizing the initial width $\sigma_0$ by setting $\sigma_0^2 = \frac{\hbar\tau}{2m}$ gives a minimum uncertainty scale of the same form as the standard quantum limit (SQL) [2].

$$
\Delta x_{\min} \sim \sqrt{\frac{\hbar\tau}{m}} = \sqrt{\frac{2\hbar d}{mc}}
$$

This standard quantum limit assumes particular measurement conditions and an initially uncorrelated wave packet. It is not an absolute bound that cannot be surpassed in principle. For example, methods using “contractive states,” with negative initial position–momentum correlations, are known to achieve precision beyond the SQL [2].

The relative uncertainty $\frac{\Delta x_{\min}}{d} \propto \frac{1}{\sqrt{d}}$ actually decreases with increasing distance d. The equation describes the distance dependence of the position standard deviation in the specified model. Wave-packet width alone does not imply state indistinguishability or a transformation of spacetime.

---

## 2. Localization Limits and the Limits of the Spacetime Picture

### 2.1 Localization Limits and Quantum Fluctuations of Spacetime

The Planck scale indicates where quantum theory and gravity need to be considered together. This section relates the question of how tightly a position can be localized to the validity of the spacetime framework used to define position and distance.

As a guide, consider a heuristic estimate of the localization limit obtained by combining quantum mechanics and general relativity. The uncertainty relation implies that reducing a particle’s position uncertainty to $\Delta x$ requires a momentum uncertainty of order

$$
\Delta p \sim \frac{\hbar}{\Delta x}
$$

At sufficiently high energies, the corresponding energy is estimated as

$$
E \sim c\,\Delta p \sim \frac{\hbar c}{\Delta x}
$$

General relativity associates an energy E with a gravitational length scale, the Schwarzschild radius,

$$
r_s \sim \frac{2GE}{c^4}
$$

Substituting the estimated energy gives

$$
r_s \sim \frac{2G\hbar}{c^3\Delta x}
$$

When the size $\Delta x$ of the region to be localized becomes comparable to the gravitational length scale $r_s$, one obtains

$$
\Delta x \sim r_s \quad\Longrightarrow\quad \Delta x \sim \sqrt{2}\,l_P
$$

Here,

$$
l_P = \sqrt{\frac{\hbar G}{c^3}} \approx 1.6 \times 10^{-35}\,\mathrm{m}
$$

is the Planck length. This estimate suggests that probing an increasingly small region requires increasingly large energies, whose own gravitational effects may substantially alter the spacetime of the region being measured [3].

The estimate does not prove that the Planck length is a strict minimum length [3]. At the Planck scale, however, both quantum mechanics and general relativity become relevant, and the conventional picture of spacetime as a smooth, continuous geometry may reach its limit of applicability.

One concept used to describe spacetime in such a regime is “spacetime foam” [4]. It expresses the possibility that the metric and geometrical structure of spacetime fluctuate quantum mechanically at the Planck scale, so that distance, curvature, and even spacetime topology may no longer be fixed in the classical sense [4].

The question of indistinguishability then takes on a further level. One can envisage a limit in which spacetime geometry itself is no longer well defined and the framework for defining position and distance ceases to apply.

### 2.2 Information Dispersal and Observability in High-Energy Particle Collisions

In high-energy particle collisions, increasing incident energy can give rise to the production of many particles and complex interactions, dispersing information about the initial state across many degrees of freedom and interparticle correlations. In practice, it is difficult to measure every produced particle and correlation completely, so a description restricted to observable degrees of freedom is needed.

Let the total system have state $\rho(E)$, and let the observable subsystem have state

$$
\rho_{\mathrm{obs}}(E) = \operatorname{Tr}_{\mathrm{unobs}}\rho(E)
$$

Here E is the center-of-mass collision energy, defined as $E \equiv \sqrt{s}$. The operation $\operatorname{Tr}_{\mathrm{unobs}}$ denotes tracing out degrees of freedom outside the observed subsystem.

Such coarse-graining affects a subsystem’s capacity to discriminate parameters, as described by quantum information geometry. Quantum Fisher information (QFI), $F_Q(E)$, quantifies how sensitively a quantum state can distinguish changes in the parameter E [5]. Reduction to a subsystem may lose some of the discrimination capability retained by the total system [5].

The local distinguishability of energy-dependent quantum states can be expressed using the Bures distance [5]. For a smooth family of quantum states and a sufficiently small energy change dE,

$$
\begin{aligned}
D_{\mathrm{Bures}}\!\left(\rho_{\mathrm{obs}}(E),\rho_{\mathrm{obs}}(E+\mathrm{d}E)\right)^2
&\approx \frac{1}{4}F_Q(E)\,(\mathrm{d}E)^2 + O\!\left((\mathrm{d}E)^3\right)
\end{aligned}
$$

holds [5]. If the observable subsystem’s QFI decreases, its ability to distinguish nearby energy-dependent states also decreases effectively. This corresponds to the first stage.

At still higher energies, the gravitational effects discussed in Section 2.1 constrain the probing process itself. This essay regards that constraint as a possible entry point to the second stage, where the framework for discrimination through position and distance ceases to apply.

---

## 3. Indistinguishability at Cosmological Limits

The earliest universe and the far future are distinct settings in which to examine the validity of the criteria for discrimination. Rather than directly extrapolating equations from microscopic measurement models, this section compares the two settings with their respective cosmological premises made explicit.

### 3.1 The Distant Past and the Uniformity of the Early Universe

Because the speed of light is finite, observing distant celestial objects means observing the universe as it was in the past. The cosmic microwave background (CMB), the earliest light accessible to telescopes, carries information from the epoch when the universe became transparent—the surface of last scattering—about 380,000 years after the Big Bang [6].

The CMB is highly uniform across the sky, with fluctuations of order $10^{-5}$ [6]. These small fluctuations are distinguishable structural information that provided the seeds for later galaxies and large-scale structure. Tracing spacetime further back toward $t \to 0$, however, raises the question of where classical spacetime descriptions cease to apply [3]. Connecting what lies beyond that limit to the Zeroth-Order Phase is this essay’s hypothesis.

### 3.2 The Far-Future Limit ($t \to +\infty$) and the End of the Universe

Looking toward the far future, $t \to +\infty$, cosmological scenarios have been proposed in which expansion continues, stars burn out, black holes evaporate, and the universe approaches heat death, or the Big Freeze, with usable free energy becoming exhausted in the limit [7].

Roger Penrose’s conformal cyclic cosmology (CCC) considers a far-future limit in which remaining particles, such as electrons, ultimately lose the significance of their rest mass and the universe acquires scale invariance [8]. This essay uses that picture as a guide to the second-stage question of how far length and time can continue to serve as standards of scale. Conformal and causal structure nevertheless remain. CCC is a cosmological hypothesis proposing that the conformal geometry of a far future without mass scales can connect smoothly to the structure of the beginning of the next universe, at its Big Bang singularity [8].

---

## 4. Four Limits and the Proposed Undifferentiated Zeroth-Order Phase

### 4.1 Four Limits

The common question across the four limits concerns differences between objects or states and the conditions under which the standards for measuring those differences remain valid. Their physical premises differ.

1. **The earliest universe ($t \to 0$):** A regime near a singularity where classical spacetime descriptions themselves cease to apply.
2. **The far future ($t \to +\infty$):** A limit beyond heat death in which, in the CCC picture, length and time scales themselves lose their meaning.
3. **Microscopic localization ($\Delta x \to 0$):** A regime in which attempts at ever tighter localization encounter the limits of the geometrical spacetime picture at the Planck scale.
4. **High-energy scattering ($E = \sqrt{s} \to \infty$):** A regime that raises questions about many-particle production, information dispersal, and resolution limits imposed by gravitational backreaction.

Although these limits differ in physical mechanism and scale, they raise a common question: how far do the boundaries that allow one thing to be distinguished from another remain valid?

### 4.2 Two Stages of Indistinguishability

This essay distinguishes two stages of indistinguishability.

**In the first stage, an algebra of observables—the collection of observables available to an observer—can still be defined, but distinctions cannot be made within it.** Examples include cases where particle individuality becomes ambiguous or where many-body interactions disperse information across numerous degrees of freedom, making individual states difficult to distinguish.

**In the second stage, the criteria for distinguishing objects, such as position, distance, and time, cease to apply in their conventional sense.** The structure that assigns observables to spacetime regions can no longer be defined in the conventional way, undermining the basis for asking where an object is or how far it is from something else.

**The second stage cannot be described within the conventional framework that assigns observables to spacetime.** An operational approach presupposes a given algebra of observables [13]. The second stage is therefore positioned as a concept indicating the limits of applicability of that approach.

### 4.3 The Tentative Term “Undifferentiated Zeroth-Order Phase”

This essay tentatively calls the limit of the second stage the **undifferentiated Zeroth-Order Phase**: a thought-experiment concept in which not only the individuality of objects but also the criteria and frameworks for distinguishing them lose their meaning.

Connections between the four limits and the second stage are examined as hypotheses of this essay. The following table separates the guidance provided by existing theories from the connections requiring further explanation.

| Limit | Guide to the inquiry | Relation to the Zeroth-Order Phase |
|---|---|---|
| Earliest universe | Limits of applicability of classical spacetime descriptions | Breakdown of the criteria for discrimination beyond those limits is hypothetical |
| Far future | Heat-death scenarios and the reformulation of scales in CCC | Heat death or conformal transformations alone do not imply the Zeroth-Order Phase |
| Microscopic localization | Intersection of quantum theory and gravity at the Planck scale | Connection to a specific spacetime structure remains unresolved |
| High-energy scattering | Information dispersal into subsystems and gravitational backreaction | Connection from local indistinguishability to the breakdown of criteria is hypothetical |

These limits do not signify the same physical state. They are nevertheless conceptually related through two questions: what is being distinguished, and what provides the basis for that distinction?

### 4.4 Existing Links Between Microscopic and Macroscopic Scales

Gravitational constraints on energy and entropy provide guides for relating microscopic and macroscopic scales. The following relations do not, however, directly establish the Zeroth-Order Phase or a reduction in dimensionality.

**(1) The ultraviolet–infrared relation.** Cohen, Kaplan, and Nelson applied the reasoning that probing smaller regions requires higher energies and makes gravity significant to the relation between a region’s size L and a field theory’s ultraviolet cutoff Λ [10].

$$
L^3\Lambda^4 \le L M_P^2
$$

The microscopic (ultraviolet) limit and the macroscopic (infrared) size are thus related by a single expression [10].

**(2) An upper bound on the number of distinguishable states.** The holographic principle, as discussed in Bousso’s entropy bounds, suggests that under appropriate conditions the entropy associated with a region is constrained by its boundary area [11].

$$
S \le \frac{A}{4l_P^2}
$$

This yields a bound on the number of states, $N \le \exp\!\left(\frac{A}{4l_P^2}\right)$ [11].

**(3) Cosmological horizon entropy.** Gibbons and Hawking associated the horizon of de Sitter space with an entropy $S = \frac{A}{4l_P^2}$ [12].

These results provide existing foundations for quantitative discussion of the limits of distinguishability [11, 12].

---

## 5. Conclusion and Outlook

This essay proposes distinguishing limits on the ability to discriminate objects or states from limits on the applicability of the criteria for discrimination, and considering the limit of the latter as the undifferentiated Zeroth-Order Phase. It compares electron position measurement, high-energy scattering, the earliest universe, and the far future through this common question.

Measurement and gravitational constraints from existing theories provide guides for considering the proposal. The essay does not establish that the four limits reach the same physical state, or that information dispersal necessarily leads to the breakdown of spacetime or scale.

A next step is to specify the measurements available to an observer and a measure of distinguishability, and to model the conditions connecting the first stage to the second. This requires distinguishing what is currently unobservable, what cannot be distinguished by specified observations, and what lacks definable criteria for discrimination [9, 13].

---

## References

1. IBM Quantum Learning, "Quantum state discrimination and tomography". (Information-theoretic formulation of state distinguishability)
2. H. P. Yuen, "Contractive States and the Standard Quantum Limit for Monitoring Free-Mass Positions", Phys. Rev. Lett. 51(9), 719-722 (1983).
3. S. Hossenfelder, "Minimal Length Scale Scenarios for Quantum Gravity", Living Rev. Relativ. 16, 2 (2013).
4. S. Carlip, "Spacetime foam: a review", Rep. Prog. Phys. 86(6), 066001 (2023).
5. S. L. Braunstein and C. M. Caves, "Statistical distance and the geometry of quantum states", Phys. Rev. Lett. 72, 3439 (1994); J. Liu, H. Yuan, X. M. Lu, and X. Wang, "Quantum Fisher information matrix and multiparameter estimation", J. Phys. A: Math. Theor. 53, 023001 (2020).
6. NASA Imagine the Universe!, "Inflation in the Universe". (Educational resource on CMB cosmic horizon and inflation theory)
7. NASA Science, "Expand our Knowledge of Dark Energy". (Cosmological scenarios on dark energy and heat death)
8. R. Penrose, "On the Gravitization of Quantum Mechanics 2: Conformal Cyclic Cosmology", Foundations of Physics 44(8), 873-890 (2014).
9. T. M. Davis and C. H. Lineweaver, "Expanding Confusion: Common Misconceptions of Cosmological Horizons and the Superluminal Expansion of the Universe", Publications of the Astronomical Society of Australia 21(1), 97-109 (2004).
10. A. G. Cohen, D. B. Kaplan, and A. E. Nelson, "Effective field theory, black holes, and the cosmological constant", Phys. Rev. Lett. 82, 4971 (1999).
11. R. Bousso, "The holographic principle", Rev. Mod. Phys. 74, 825 (2002).
12. G. W. Gibbons and S. W. Hawking, "Cosmological event horizons, thermodynamics, and particle creation", Phys. Rev. D 15, 2738 (1977).
13. R. Haag, *Local Quantum Physics* (Springer, 2nd ed., 1996).


---

**Author:** 5garashi.com Design Office  
**Last updated:** 2026-11-04 JST
