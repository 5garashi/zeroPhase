---
title: Observation Limits and the Undifferentiated Origin
lang: en
description: An epistemological inquiry into observation limits and indistinguishability, from quantum measurement to cosmology.
---
<!--
  File: zerothOrderPhase.en.md
  Description: An epistemological inquiry into observation limits and the undifferentiated origin, from quantum measurement to cosmology
  Author: 5garashi.com Design Office
  Created: 2026-10-31
  Version: 1.0.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Observation Limits and the Undifferentiated Origin: An Epistemological Inquiry from Quantum Measurement to Cosmology

**Author:** 5garashi.com Design Office

**Date:** October 28, 2026

---

## Introduction: The Epistemological Question of Indistinguishability

When we observe a distant object, the information available to us is limited, and it becomes increasingly difficult to determine its position or distinguish its detailed internal state. This essay takes "measurement ambiguity"—which may at first seem to be a merely technical problem of precision—as the starting point for a physical and epistemological inquiry, and develops a thought experiment (Gedankenexperiment) that reaches into the depths of cosmology.

The following principle will serve as a guide for this inquiry:

> **"Two states that an observer cannot distinguish in principle by any observational means available to them are to be treated as the same physical state for that observer."**

This essay begins with the scale of measurement limits in quantum mechanics (the first stage). Its central theme is to move from the inability to distinguish objects toward a second stage, in which spacetime and scale themselves—the very things that make distinctions possible—cease to hold. As we broaden our view from the breakdown of microscopic localization to ultra-high-energy scattering and the birth and fate of the universe on a cosmic scale, what boundaries of the physical world will we encounter?

## 1. Probabilistic Discrimination and the Standard Quantum Limit

To formalize how difficult it is to distinguish physical states, consider the probability distributions of observational outcomes, P_A(y) and P_B(y), for two states A and B. The total variation distance (Total Variation Distance), a classical statistical measure of the overlap between these distributions, is defined as follows [1]:

D_AB = (1/2) ∫ |P_A(y) - P_B(y)| dy,  0 <= D_AB <= 1

D_AB = 1 means that the states are perfectly distinguishable, while D_AB = 0 means that they cannot be distinguished by that measurement (their distributions overlap completely) [1].

Consider a toy model in which an observer measures the position of an electron located a distance d away, using a signal such as a photon. During the signal's round-trip time τ = 2d/c, a free-electron wave packet—a minimum-uncertainty Gaussian wave packet with no initial position-momentum correlation—spreads in space according to the Schrödinger equation. If its initial width is σ_0, the position uncertainty (standard deviation) Δx(τ) after a time τ is given by:

Δx(τ) = √( σ_0^2 + (ħ τ / (2 m σ_0))^2 )

The term ħ / (2 σ_0) in this expression comes from the initial momentum uncertainty (standard deviation) Δp of the quantum state itself, which manifests over time as spatial spreading. Optimizing the initial width σ_0 (σ_0^2 = ħ τ / 2m) gives a minimum uncertainty scale with the same form as the standard quantum limit (SQL) [2]:

Δx_min ~ √( ħ τ / m ) = √( 2 ħ d / (m c) )

This standard quantum limit, however, assumes specific measurement conditions and an initial wave packet without correlations; it is not an absolute lower bound that cannot be surpassed in principle. For example, techniques are known that achieve precision below the SQL by using "contractive states" with an initial negative correlation between position and momentum [2].

The relative error with respect to distance d, Δx_min / d ∝ 1 / √d, decreases as the distance increases. Nevertheless, this scale offers an interesting clue for considering how information spreads through space and time, and becomes ambiguous, in the act of observation.

## 2. Localization Limits and the Limits of the Spacetime Picture

### 2.1 Localization Limits and Quantum Fluctuations of Spacetime

Pushing the limit further shifts the question from how precisely we can determine a particle's position to how far spacetime itself—the framework that defines position and distance—can retain its meaning.

As a starting point for considering this problem, let us estimate the limit of localization from the relationship between quantum mechanics and general relativity. According to the uncertainty relation in quantum mechanics, if we try to reduce a particle's position uncertainty to Δx, its momentum uncertainty is approximately

Δp ~ ħ / Δx

At sufficiently high energies, the corresponding energy is estimated as

E ~ c Δp ~ (ħ c) / Δx

According to general relativity, energy E has an associated gravitational length scale, the Schwarzschild radius:

r_s ~ (2 G E) / c^4

Substituting the energy estimated above gives:

r_s ~ (2 G ħ) / (c^3 Δx)

Consider the condition under which the size Δx of the region to be localized becomes comparable to this gravitational length scale r_s:

Δx ~ r_s  =>  Δx ~ √2 l_P

Here,

l_P = √( (ħ G) / c^3 ) ≈ 1.6 * 10^-35 m

is the Planck length. This estimate suggests that the smaller the region we try to observe, the more energy is required—and the gravitational effect of that energy itself may significantly alter the spacetime of the region being measured [3].

Of course, this does not prove that the Planck length is a strict minimum length [3]. It does, however, suggest that at the Planck scale both quantum mechanics and general relativity must be taken into account, and that the conventional picture of spacetime as a continuous, smooth geometry may reach its limits.

One concept used to describe spacetime under such extreme conditions is "spacetime foam" [4]. It describes the possibility that, at the Planck scale, the metric and geometric structure of spacetime itself fluctuate quantum mechanically, so that distance, curvature, and even spacetime topology can no longer be fixed in the classical sense [4].

The problem of indistinguishability thus reaches a deeper level. We can imagine a limit in which the geometry of spacetime itself becomes unclear, and the framework for defining position and distance ceases to hold.

### 2.2 Information Dispersion and Observability in High-Energy Particle Collisions

In high-energy particle collisions, increasing the energy of the incoming particles leads to the production of many particles and complex interactions. Information about the initial state becomes dispersed among diverse degrees of freedom and correlations between particles. In practice, it is difficult to measure every produced particle and every correlation, so we need a description of a subsystem restricted to the observable degrees of freedom.

Let the state of the entire system be ρ(E), and the state of the subsystem being observed be

ρ_obs(E) = Tr_unobs ρ(E)

Here E is the center-of-mass energy of the collision, defined as E ≡ √s. Tr_unobs denotes the operation of removing unobserved degrees of freedom by taking a partial trace.

In quantum information geometry, this kind of coarse-graining affects the parameter-discrimination capability retained by the observable subsystem. Quantum Fisher information (QFI), F_Q(E), quantifies how well a quantum state can distinguish changes in the parameter E [5]. Reducing the state to a subsystem may cause it to lose some of the discrimination capability retained by the full system [5].

The distinguishability of quantum states that depend on energy E can be expressed locally using the Bures distance [5]. For a smooth family of quantum states and a sufficiently small energy change dE,

D_Bures( ρ_obs(E), ρ_obs(E + dE) )^2 ≈ (1/4) F_Q(E) (dE)^2 + O((dE)^3)

holds [5]. If the QFI of the observable subsystem decreases, then the effective distinguishability between nearby energy states in that subsystem also decreases (the first stage).

At still higher energies, the gravitational effects discussed in Section 2.1 constrain the probing process itself. This essay views that as an entry point to the second stage, in which the framework for making distinctions by position and distance ceases to hold.

## 3. Indistinguishability at Cosmological Limits

Let us now shift the motif of "blurred boundaries and dispersed information" seen in microscopic regions and high-energy collisions to the macroscopic scale of cosmology.

### 3.1 The Edge of the Past and the Uniformity of the Very Early Universe

Observing a distant celestial object is equivalent to looking into the past of the universe, because the speed of light is finite. The most distant light we can detect with a telescope, the cosmic microwave background (CMB), carries information from the "recombination era" (the surface of last scattering), about 380,000 years after the universe began [6].

The CMB is remarkably uniform across the sky, at roughly the 10^-5 level [6]. These tiny fluctuations are "distinguishable structural information" that later seeded galaxies and large-scale structures. But if we conduct a thought experiment that traces spacetime further back (t -> 0), then near the singularity the framework for describing classical spacetime itself ceases to hold (the second stage) [3].

### 3.2 The Limit in the Direction of Time (t -> +∞) and the Fate of the Universe

Looking toward the future along the time axis (t -> +∞), scenarios have been proposed in which the universe continues to expand, stars burn out, black holes evaporate, and usable free energy is depleted toward a maximum, leading to heat death (the Big Freeze) [7].

Conformal Cyclic Cosmology (CCC), proposed by Roger Penrose, considers a limit in the distant future in which residual particles such as electrons eventually lose the meaning of rest mass, and the universe acquires scale invariance [8]. In this picture, the scales used to express differences in length and time themselves lose their meaning (the second stage). Conformal and causal structures, however, remain. CCC is a compelling hypothesis: it proposes that the conformal geometric structure of the distant future, after mass and scale have been lost, could connect smoothly to the structure of the beginning of the next universe (the Big Bang singularity) [8].

## 4. Four Limits and the Proposed "Zeroth-Order Phase"

### 4.1 Four Limits

Let us lay out the four limiting situations discussed so far:

1. **The very early universe (t → 0):** A region near the singularity where the classical description of spacetime itself ceases to hold.
2. **The distant future of the universe (t → +∞):** A limit in which, after heat death, the scales of length and time themselves lose their meaning in the CCC picture.
3. **The microscopic localization limit (Δx → 0):** A region where pushing localization to its limit reaches the boundary of the geometric picture of spacetime at the Planck scale.
4. **The high-energy scattering limit (E = √s → ∞):** A regime in which multiparticle production, information dispersion, and the resolution limit imposed by gravitational back-reaction become relevant.

These limits involve different physical mechanisms and scales, but each raises the same question: how far can the boundaries that allow us to distinguish one thing from another remain valid?

### 4.2 Two Stages of Indistinguishability

This essay identifies two distinct stages of indistinguishability.

**The first is a stage in which the algebra of observables (the set of observables available to an observer) can still be defined, but distinctions cannot be made within its scope.** This includes cases in which the individuality of particles becomes ambiguous, or interactions among many particles disperse information across numerous degrees of freedom, making individual states difficult to identify.

**The second is a stage in which the very criteria for distinguishing objects—such as position, distance, and time—no longer hold in their conventional sense.** The structure that assigns observables to spacetime regions can no longer be defined in the conventional way, and the foundations for determining "where" an object is or "how far" it is from another object begin to falter.

An important point is that **the second stage cannot be described within the conventional framework that assigns observables to spacetime.** An operationalist approach presupposes that an algebra of observables is given [13]; the second stage is therefore positioned as a concept that marks the limits of that approach.

### 4.3 The Tentative Name "Zeroth-Order Phase"

This essay tentatively calls the second-stage limit—where not only the individuality of objects but also the criteria and frameworks for distinguishing them lose their meaning—the **"Zeroth-Order Phase"**, as a concept for this thought experiment.

Each of the four limits may connect to the second stage by a different route:

```text
• [The very early universe (t → 0)]
• [The distant future of the universe (t → +∞)]
• [The microscopic localization limit (Δx → 0)] (Planck scale)
• [The high-energy scattering limit (E → ∞)] (multiparticle dispersion and gravitational back-reaction)
  ↓
[ Zeroth-Order Phase ]
```

These do not represent the same physical state. They are, however, conceptually connected through two questions: "What is being distinguished?" and "By what criteria is it distinguished?"

### 4.4 Existing Connections Between the Micro and the Macro

Existing theories offer several clues about the connection between the micro and the macro.

**(1) The UV/IR connection.** Cohen, Kaplan, and Nelson applied the reasoning that smaller regions require greater energy—and that gravity eventually cannot be ignored—to the relationship between the size L of a region and the ultraviolet cutoff Λ of a field theory [10]:

L^3 Λ^4 <= L M_P^2

The limit on the microscopic side (the ultraviolet) is connected by a single equation to the macroscopic size (the infrared) [10].

**(2) An upper bound on the number of distinguishable states.** The holographic principle (the Bousso bound) suggests that, under suitable conditions, the entropy associated with a region is bounded by the area of its boundary [11]:

S <= A / (4 l_P^2)

This gives an upper bound on the number of states, N <= exp( A / (4 l_P^2) ) [11].

**(3) Entropy of cosmological horizons.** Gibbons and Hawking associated an entropy S = A / (4 l_P^2) with the horizon of de Sitter space [12].

These ideas serve as existing foundations for quantitatively discussing limits on distinguishability [11, 12].

## 5. Conclusion and Outlook: The Significance of the Question

Beginning with simple toy models—the measurement of an electron's position and high-energy scattering—this essay is not a paper presenting rigorous quantitative predictions. It is a thought experiment that reconsiders the physical world through the epistemological framework of "observability" [1, 9].

Of course, the boundary of the observable universe, the existence of event horizons, and the equations of microscopic quantum mechanics cannot simply be extrapolated to the universe as a whole [9]. What is currently unseen (unobservable) must be carefully distinguished from what does not exist in principle or cannot be distinguished [9].

This essay asks not only how far physical objects can be distinguished. It also asks how far the criteria for distinguishing objects can remain valid, and how we might think about a limit in which even those criteria lose their meaning.

"How do boundaries come into being, and how do they disappear?" Continuing to hold on to this question may itself be the purpose of thought experiments at the boundary between theoretical physics and philosophy.

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

**Last updated:** October 31, 2026 JST
