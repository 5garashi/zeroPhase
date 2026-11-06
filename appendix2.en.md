---
title: 'Appendix 2: Mathematical Notes on Observation Limits and Distinguishability'
lang: en
math: true
appendix: true
translation: /appendix2.html
description: Explains the meaning and derivation of the total variation distance, free wave packets, SQL-type estimates, the Planck scale, partial traces, the trace distance, monotonicity of the QFI, noncommutative coordinates, and entropy bounds.
---
<!--
  File: appendix2.en.md
  Description: Meaning, derivation, and conditions of the equations for observation limits and distinguishability (English translation)
  Author: 5garashi.com Design Office
  Created: 2026-11-07
  Last updated: 2026-11-07 JST
  Version: 2.0.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Appendix 2: Mathematical Notes on Observation Limits and Distinguishability

**Author:** 5garashi.com Design Office

**Version:** <span data-version>2.0.0</span>　**Last updated:** 2026-11-07 JST

This appendix organizes the derivations and conditions of the equations on observation limits and distinguishability used in the main text.

[Main text: Observation Limits and the Undifferentiated Origin](zerothOrderPhase.en.html) / [Appendix 1: Logical background](appendix1.en.html)

## 0. Statistical and Quantum-Information Measures Used in This Essay

| Measure | Expression | Domain | Condition of indistinguishability |
|---|---|---|---|
| **Total variation distance (TV distance)** | $D_{AB} = \frac{1}{2}\int \vert P_A(y)-P_B(y)\vert\,\mathrm{d}y$ | Classical probability densities | $D_{AB} = 0$ |
| **Trace distance** | $T(\rho_A, \rho_B) = \frac{1}{2}\Vert\rho_A - \rho_B\Vert_1$ | Quantum states (density matrices) | $T = 0$ (optimal success probability $p_{\mathrm{succ}} = 1/2$) |
| **Bures distance** | $D_{\mathrm{Bures}}^2 \approx \frac{1}{4}F_Q(E)(\mathrm{d}E)^2$ | Parametric changes of quantum states | $F_Q(E) = 0$ (no first-order change can be read at that point) |

---

## 1. Total Variation Distance: The Degree of Discrimination of Measurement Outcomes

The total variation distance between probability densities $P_A(y), P_B(y)$ takes values in $0 \le D_{AB} \le 1$; $D_{AB}=1$ means perfect distinguishability and $D_{AB}=0$ means indistinguishability by the specified measurement. Even if $D_{AB}=0$ for one measurement, the states may be distinguishable by another. Indistinguishability of quantum states is discussed with respect to a specified set of all available measurements ($\mathcal A_O$ in Appendix 1, Section 1.1).

## 2. Spreading of a Free Gaussian Wave Packet

For a nonrelativistic free particle of mass $m$, the position standard deviation $\Delta x(\tau)$ of a minimum-uncertainty Gaussian wave packet with initial width $\sigma_0$ and no initial correlation between position and momentum is

$$
\Delta x(\tau)=\sqrt{\sigma_0^2+\left(\frac{\hbar\tau}{2m\sigma_0}\right)^2}
$$

### Derivation

1. Standard deviation of the initial momentum: $\Delta p = \hbar / (2\sigma_0)$
2. Standard deviation of the velocity of a free particle: $\Delta v = \Delta p / m = \hbar / (2m\sigma_0)$
3. Sum of variances without initial correlation: $\Delta x^2(\tau) = \sigma_0^2 + (\Delta v\, \tau)^2$

If there is an initial correlation, a covariance term is added, so this formula cannot be used as it is.

## 3. SQL-Type Minimum Position Width

Optimize $\sigma_0$ for a given time $\tau$ ($\frac{\mathrm{d}}{\mathrm{d}\sigma_0}\Delta x^2(\tau) = 0$). Let $\tau = 2d/c$ be the time for a signal to make a round trip in flat spacetime to a particle at distance $d$ from the observer.

$$
\sigma_0^2 = \frac{\hbar\tau}{2m} \quad\Longrightarrow\quad \Delta x_{\min} = \sqrt{\frac{\hbar\tau}{m}} = \sqrt{\frac{2\hbar d}{mc}}
$$

The standard quantum limit (SQL) for monitoring the position of a free mass has the same form up to a numerical factor, namely proportional to $\sqrt{\hbar\tau/m}$ [1]. What is obtained here is the minimum position standard deviation for the family of states without initial correlation, not the total ranging error including detector noise and measurement back-action. Contractive states with an initial negative correlation between position and momentum can reach a position width below this value [2].

## 4. The Planck Length: The Crossing of Localization and Gravitational Back-Reaction

1. Momentum associated with localization: $\Delta p \sim \hbar / \Delta x$
2. High-energy approximation: $E \sim c\Delta p \sim \hbar c / \Delta x$
3. Schwarzschild radius: $r_s = \frac{2GE}{c^4} \sim \frac{2G\hbar}{c^3\Delta x}$
4. From $\Delta x \sim r_s$: $\Delta x^2 \sim \frac{2G\hbar}{c^3} = 2 l_P^2 \;\Longrightarrow\; \Delta x \sim \sqrt{2}\, l_P$

The factor $\sqrt2$ comes from the relations adopted in this estimate and is not an exact coefficient of a universal minimum length. The Planck time $t_P=l_P/c=\sqrt{\hbar G/c^5}$ is likewise regarded as a scale at which quantum gravity becomes relevant.

---

## 5. Partial Trace and Trace Distance

For the subsystem $\rho_{\mathrm{obs}} = \operatorname{Tr}_{\mathrm{unobs}}\rho$ obtained by removing unobservable degrees of freedom, define the trace distance between two states as

$$
T(\rho_A,\rho_B)=\frac{1}{2}\Vert\rho_A-\rho_B\Vert_1
$$

$\Vert\cdot\Vert_1$ is the trace norm; for a Hermitian matrix such as a difference of density matrices, it is the sum of the absolute values of the eigenvalues. When one of two states with equal prior probabilities is identified in a single trial, the success probability maximized over all available measurements is [3]

$$
p_{\mathrm{succ}} = \frac{1+T}{2}
$$

If $T=0$, the optimal success probability is also $1/2$, and the states cannot be discriminated in that subsystem.

### 5.1 Partial Trace and Monotonicity of the QFI

Operations that discard unobservable degrees of freedom (physically allowed maps, including partial traces) do not increase the quantum Fisher information [4, 5].

$$
F_Q\!\left[\operatorname{Tr}_{\mathrm{unobs}}\rho(E)\right] \;\le\; F_Q\!\left[\rho(E)\right]
$$

What is compared is the total system and the subsystem at the same parameter value. The argument of Section 2.2 of the main text takes this inequality as a firm basis and considers situations in which the gap between the two sides grows with energy.

## 6. A Toy Model of Superposition in a Pair of Two-Level Systems

For two two-level systems, let the pure states of the total system be

$$
\vert \Psi_\pm\rangle = \frac{\vert 0\rangle_1\vert 0\rangle_2 \pm \vert 1\rangle_1\vert \chi_\theta\rangle_2}{\sqrt{2}}, \qquad \vert \chi_\theta\rangle_2 = \cos\theta\vert 0\rangle + \sin\theta\vert 1\rangle
$$

## 7. Derivation of the Trace Distance in the Toy Model

The density matrix of system 1 after tracing out system 2:

$$
\rho_{1,\pm} = \operatorname{Tr}_2 \vert \Psi_\pm\rangle\langle\Psi_\pm\vert = \frac{1}{2} \begin{pmatrix} 1 & \pm\cos\theta \\ \pm\cos\theta & 1 \end{pmatrix}
$$

The difference of the density matrices:

$$
\rho_{1,+} - \rho_{1,-} = \begin{pmatrix} 0 & \cos\theta \\ \cos\theta & 0 \end{pmatrix}
$$

Because the eigenvalues are $\pm \cos\theta$, the trace distance is

$$
T(\rho_{1,+}, \rho_{1,-}) = \frac{1}{2}\left(\vert \cos\theta\vert  + \vert -\cos\theta\vert \right) = \cos\theta \qquad \left(0 \le \theta \le \frac{\pi}{2}\right)
$$

As $\theta \to \pi/2$, $T \to 0$ (indistinguishable) for an observer who measures only system 1, but in the total system $\langle\Psi_+\vert \Psi_-\rangle = 0$, so the states are perfectly distinguishable.

---

## 8. Noncommutative Coordinates, the CKN Bound, and Holographic Bounds

### 8.1 Noncommutative Coordinates

Models of noncommutative coordinates assume that two coordinate operators do not commute.

$$
[x_i,x_j]=i\theta_{ij}
$$

$[x_i,x_j]=x_ix_j-x_jx_i$ is the commutator, and $\theta_{ij}$ is a parameter expressing the noncommutativity; in models that express coordinates as lengths, it has the dimension of length squared. Because coordinates in different directions cannot be fixed sharply at the same time, this gives a clue for considering whether classical geometry, which presupposes points and sharp boundaries, can be applied as it is.

### 8.2 CKN Scaling

The argument of Cohen–Kaplan–Nelson links the size of a region and the ultraviolet cutoff of an effective field theory through a gravitational consistency condition [6].

$$
L^3\Lambda^4\lesssim L M_P^2
$$

Natural units $c=\hbar=1$ are used. $L$ is the characteristic length of the region, $\Lambda$ is the ultraviolet cutoff, and $M_P$ is the Planck mass scale. The left side is the energy obtained by multiplying the energy density $\sim\Lambda^4$ corresponding to the cutoff by the volume $L^3$, and the right side is the mass scale of a black hole of the same size. Because the numerical coefficients depend on conventions such as the definition of the Planck mass, the relation is read as a scaling.

### 8.3 Holographic Entropy Bound

$$
\frac{S}{k_B}\le\frac{A}{4l_P^2}
$$

$S$ is the entropy, $k_B$ is the Boltzmann constant, and $A$ is the area of the relevant boundary surface. The expression $S\le A/(4l_P^2)$ in the main text is a notation that expresses entropy as a dimensionless quantity in units of $k_B$. The covariant entropy bound deals with the entropy on a suitable light sheet attached to a surface of area $A$ [7]. When it is read as a number of states, an equal mixture of $N$ states is counted as $S=k_B\ln N$, giving $N\le\exp[A/(4l_P^2)]$. For a number of bits, the dimensionless entropy is further divided by $\ln2$.

---

## 9. Five Limit Regions and the Three-Phase Model

This comparison adds infinitesimal time division ($\Delta t\to0$) to the four limits of the main text as an independent line of inquiry. Each column is organized according to the three-phase model of Appendix 1, and the column "Connection to the Zeroth-Order Phase" expresses hypotheses of this essay.

| Limit region | Clues for the Spacetime-Limit Phase | Clues for the Dimension-Reduction Phase | Connection to the Zeroth-Order Phase |
|---|---|---|---|
| **Earliest ($t\to0$)** | Measurement of primordial fluctuations | Quantum-gravity effects and transformation of degrees of freedom | Connection beyond the limit of the classical description of spacetime |
| **Far future ($t\to+\infty$)** | Cosmological equilibration | Conformal redescription in CCC | Connection to the failure of scale standards |
| **Localization limit ($\Delta x\to0$)** | Precision of localization and measurement back-action | Noncommutative geometry, spectral dimension | Connection to the limit of the concept of localization |
| **Infinitesimal time ($\Delta t\to0$)** | Quantum Zeno effect (suppression of transitions, not indistinguishability itself) | Transformation of the conditions for measuring time | Connection to the failure of the standards of clocks and temporal order |
| **High energy ($E\to\infty$)** | Trace distance of subsystems, decrease of the QFI | CKN and entropy bounds | Connection to the failure of the criteria for discriminating spacetime and phase space |

## References

1. V. B. Braginsky, F. Ya. Khalili, *Quantum Measurement*, ed. K. S. Thorne (Cambridge University Press, 1992).
2. H. P. Yuen, "Contractive States and the Standard Quantum Limit for Monitoring Free-Mass Positions," Physical Review Letters 51, 719 (1983). [Paper](https://doi.org/10.1103/PhysRevLett.51.719)
3. P. Hayden, K. Milner, M. M. Wilde, "Quantum Interactive Proofs and the Complexity of Separability Testing," Theory of Computing 11 (2015), 201–232. [Paper](https://theoryofcomputing.org/articles/v011a003/)
4. S. L. Braunstein, C. M. Caves, "Statistical distance and the geometry of quantum states," Physical Review Letters 72, 3439 (1994). [Paper](https://doi.org/10.1103/PhysRevLett.72.3439)
5. J. Liu, H. Yuan, X.-M. Lu, X. Wang, "Quantum Fisher information matrix and multiparameter estimation," J. Phys. A: Math. Theor. 53, 023001 (2020). [Paper](https://arxiv.org/abs/1907.08037)
6. A. G. Cohen, D. B. Kaplan, A. E. Nelson, "Effective Field Theory, Black Holes, and the Cosmological Constant" (1999). [Paper](https://arxiv.org/abs/hep-th/9803132)
7. R. Bousso, "A Covariant Entropy Conjecture" (1999). [Paper](https://arxiv.org/abs/hep-th/9905177)

[Back to the main text](zerothOrderPhase.en.html) / [Back to Appendix 1](appendix1.en.html)

---

**Author**: 5garashi.com Design Office  
**Last updated**: 2026-11-07 JST
