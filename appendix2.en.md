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
  Last updated: 2026-11-08 JST
  Version: 2.1.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Appendix 2: Mathematical Notes on Observation Limits and Distinguishability

**Author:** 5garashi.com Design Office

**Version:** <span data-version>2.1.0</span>　**Last updated:** 2026-11-08 JST

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

## 10. An Estimate That Pushes Distant Discrimination to the Limits of Resources

This section estimates how far one can distinguish when the maximum resources available to the observer in principle are substituted into the quantum limit on distinguishing two distant sources of Section 3.1 of the main text. Three principles of this essay are adopted: (1) the observation time has an upper limit $T_{\max}$; (2) the size of the aperture has an upper limit; (3) the precision of a measurement with a single photon is set by its wavelength (energy), and with $N$ photons it improves by up to a factor $\sqrt N$. The apparatus is also a thing in the universe and obeys the same kinds of limits; these are brought in one by one. What follows is an order-of-magnitude estimate for an example with a fixed source and is treated as an estimate of this essay (Section 10.6).

As an example, consider a source with the luminosity of the Sun (lifetime $t_{\mathrm{life}}=10^{10}$ years, emitted wavelength $\lambda_e=500$ nm, number of photons emitted over its life $N_{\mathrm{emit}}\approx3\times10^{62}$), with detection efficiency $\eta=1$. The observed wavelength is $\lambda_{\mathrm{obs}}=(1+z)\lambda_e$. This source is an example for showing orders of magnitude and does not represent a source that actually exists at each epoch. Distances are computed with the same flat ΛCDM (Planck 2018) as in the main text.

### 10.1 The Limit Set by the Number of Photons, and the Upper Limit on Observation Time

The number of photons that arrive during an observation time $T$ is estimated as the number the source emits over its life multiplied by the fraction caught by the aperture and by the fraction that arrives within that time. Because the light of the source is stretched over $(1+z)$ times as long by the time it arrives, the fraction that arrives is $T/[(1+z)\,t_{\mathrm{life}}]$ when $T$ is shorter than $(1+z)\,t_{\mathrm{life}}$. The expression of the main text becomes

$$
\bar N\xi_Q=\frac{\pi^2\eta\,N_{\mathrm{emit}}\,D^4s^2}{256\,\lambda_e^2\,d_M^4}\cdot\frac{T}{(1+z)\,t_{\mathrm{life}}}
$$

and from $\bar N\xi_Q=\ln10$, the smallest separation that can be distinguished is

$$
s_{\mathrm{ph}}=\frac{16\lambda_e d_M^2}{\pi D^2}\sqrt{\frac{\ln10}{\eta N_{\mathrm{emit}}}\cdot\frac{(1+z)\,t_{\mathrm{life}}}{T}}
$$

(when $T$ is longer than $(1+z)\,t_{\mathrm{life}}$, the last ratio is taken as 1).

The upper limit $T_{\max}$ on the observation time is a principle adopted by this essay. As a motivation, it has been argued that in an accelerating universe the total energy and information an observer can recover are finite [14]; this does not, however, directly limit the observation time of a single telescope. With $T_{\max}$ in place, because $(1+z)$ has no upper limit, in the example with a fixed source the photons received from a sufficiently distant (past) source decrease in inverse proportion to $(1+z)$.

### 10.2 The Upper Limit on the Size of the Aperture

If there is no upper limit on the observation time, all the light of the source's life is received ($T\ge(1+z)\,t_{\mathrm{life}}$), and the aperture diameter is enlarged to the radius of the cosmological event horizon set by the cosmological constant, $r_H=c/H_\Lambda\approx5.4$ Gpc ($D=r_H$), then even at the largest distances ($d_M\approx14$ Gpc) $s_{\mathrm{ph}}\approx1.5\times10^{-36}$ m, below the Planck length. An apparatus of that size, however, is torn apart by the expansion of the universe. Under a cosmological constant $\Lambda$, the turnaround radius of a bound structure of mass $M$ has an upper limit

$$
R_{\max}=\left(\frac{3GM}{\Lambda c^2}\right)^{1/3}
$$

[8], which serves as a measure of the size of a bound structure. Because unbound matter recedes, the mass that can be gathered is also limited to the bound structure to which the observer belongs (the Local Group, about $2\times10^{12}$ times the mass of the Sun). The limit set by the cosmological constant acts twice, on the mass and on the aperture. Then $R_{\max}\approx1.4$ Mpc, and as an order-of-magnitude measure the aperture diameter is taken as $D=2R_{\max}\approx2.8$ Mpc ($8.7\times10^{22}$ m). The turnaround radius is the size at the edge where binding breaks, so the size that can be held stably is smaller; moreover, most of the mass of the Local Group is dark matter and cannot be used for the apparatus. $D$ is therefore an overestimate, and the $s_{\mathrm{ph}}$ actually reached is larger than the values in the table of Section 10.5. With this $D$, $s_{\mathrm{ph}}$ is of order $10^{-33}$ to $10^{-24}$ m depending on distance (table in Section 10.5).

### 10.3 The Precision of a Measurement Is Set by the Wavelength of the Photons

The optimal measurement (which sorts the light into spatial modes) requires the axis of the measurement to be aligned with the center of the light more finely than the angular separation to be distinguished. When the axis is misaligned, small separations fall back to the diffraction limit [9].

**(1) The precision of direction from a single photon.** The transverse position at which a photon enters the aperture lies within the width of the aperture, with spread $\Delta x\lesssim D/2$. If the direction of arrival of a photon of momentum $p=h/\lambda_{\mathrm{obs}}$ spreads by $\Delta\theta$, its transverse momentum spreads by $\Delta p_\perp=p\,\Delta\theta$. From the uncertainty relation between position and momentum, $\Delta x\,\Delta p_\perp\ge\hbar/2$, the smallest direction uncertainty compatible with a position known to within $D/2$ is

$$
\Delta\theta\gtrsim\frac{\hbar}{pD}=\frac{\lambda_{\mathrm{obs}}}{2\pi D}
$$

This has the same form as the diffraction limit and agrees with the statement in Section 4.2 of the main text that the quantum Fisher information about direction from a single photon does not exceed $(2\pi D/\lambda)^2$.

**(2) The axis is aligned with the received light.** The center of the light can be estimated from the mean direction of arrival of the $N$ photons received, to a precision of about $\Delta\theta/\sqrt N$ (the standard error of a mean of $N$). When the axis is aligned to this precision, the proper separation that can be distinguished is about this precision times the angular diameter distance $d_A$; using $d_A(1+z)=d_M$, it has the same form as $s_{\mathrm{ph}}$ apart from a coefficient. The stretching of the observed wavelength by $(1+z)$ and the shrinking of the angular diameter distance by $1/(1+z)$ cancel, as in Section 3.1 of the main text. In the table of Section 10.5 the alignment precision is taken with a margin as $\lambda_{\mathrm{obs}}/(D\sqrt N)$, and the ratio to $s_{\mathrm{ph}}$ is about 0.5. The values in the table are for the case in which the same photons are used for both alignment and discrimination. If the photons are split between the two, each limit grows by a factor of about $\sqrt2$, and the premise that the axis is aligned more finely than the separation holds only just, without margin. The limit of alignment is of the same order as $s_{\mathrm{ph}}$ and does not form a separate wall.

**(3) The precision of the shape of the apparatus.** Measuring the shape of the apparatus (the positions of its mirrors) also uses photons, and its precision is set, as in (1) and (2), by the wavelength and number of the photons used. Measuring more finely requires a shorter wavelength, that is, a higher energy, and concentrating too much energy in a small region causes gravitational collapse. The lower limit to which this precision can be brought in principle is therefore of the order of the Planck length (the same approach as the rough estimate of Section 4). Unlike (2), this lower limit is taken not to be lowered by averaging over many photons, because it is not a statistical limit of the measurement but a lower limit on localization itself, arising from concentrating energy in order to measure. The actual error is set by things such as the stability with which positions are held, and is larger than this lower limit. If the lower limit is reached, the error in the direction of the axis due to errors in the shape of the apparatus is about $l_P/D$, and the separation it sets is $l_P\,d_A/D$. As the table shows, this is well below $s_{\mathrm{ph}}$ for $z\gtrsim3$, and of the same order nearby ($z\approx0.1$).

As a different estimate, the quantum limits on measuring lengths and times with clocks [10] have been combined with the gravity of the apparatus to give errors of $(l_P^2L)^{1/3}$ in measuring a length $L$ and $(t_P^2T)^{1/3}$ in measuring a time $T$, where $t_P=l_P/c$ is the Planck time [11]. This estimate is heuristic and has been criticized and disputed [12, 13]. Applied to the direction of the axis, it makes the error grow with distance and observation time and moves the wall that matters from the number of photons to the apparatus's reference rulers and clocks; (1) to (3) above do not use this estimate.

### 10.4 The Effect of Wavelength

At fixed energy, a shorter wavelength makes each photon more informative ($\xi_Q\propto\lambda_e^{-2}$) and reduces the number of photons ($\bar N\propto\lambda_e$). On balance, $s_{\mathrm{ph}}$ decreases in proportion to $\sqrt{\lambda_e}$. When the wavelength is shorter than the size of an atomic nucleus (about $10^{-15}$ m), however, no apparatus made of matter can collect the light or sort it into spatial modes. In addition, combining the light from all parts of the aperture requires the error in the shape of the apparatus to be well below the wavelength. Lowering the limit with a shorter wavelength therefore requires knowing the shape of the apparatus correspondingly more finely, and the lower limit on that is of the order of the Planck length, as in Section 10.3 (3).

### 10.5 Dependence on Distance

The table gives values for an aperture of the size of the Local Group, with the upper limit on the observation time taken, as an example, as $T_{\max}=10^{11}$ years. The opacity of (a) in the main text is not included. The rows for $z=10^{6}$ and $10^{12}$ are computational extrapolations to epochs at which the source does not exist, given to show the trend (in every row the number of photons received exceeds $10^{40}$, so the statistical treatment holds). In every row, $s_{\mathrm{ph}}$ is far below $\lambda_e d_M/D$ (about 0.1 mm nearby and about 2 mm at the largest distances), so the assumption of the expression in the main text, that the separation is well below the diffraction limit, holds.

| Redshift $z$ | $s_{\mathrm{ph}}$ (number of photons) | Limit of aligning the axis with the light | Separation set by the shape of the apparatus (Planck length) |
|---|---|---|---|
| 0.1 | $5.3\times10^{-33}$ m | $2.7\times10^{-33}$ m | $2.3\times10^{-33}$ m |
| 3 | $1.2\times10^{-30}$ m | $6.2\times10^{-31}$ m | $9.4\times10^{-33}$ m |
| 1090 | $5.7\times10^{-29}$ m | $2.9\times10^{-29}$ m | $7.3\times10^{-35}$ m |
| $10^{6}$ | $1.8\times10^{-27}$ m | $9.2\times10^{-28}$ m | $8.2\times10^{-38}$ m |
| $10^{12}$ | $1.8\times10^{-24}$ m | $9.2\times10^{-25}$ m | $8.2\times10^{-44}$ m |

From this table, the following can be said for the example with a fixed source.

1. The limit that matters is $s_{\mathrm{ph}}$, set by the number of photons. The limit of alignment is of the same order, and the limit from the shape of the apparatus is well below it for $z\gtrsim3$.
2. $s_{\mathrm{ph}}$ grows monotonically with distance: nearby because the comoving distance $d_M$ grows, and beyond the point where $(1+z)\,t_{\mathrm{life}}$ exceeds $T_{\max}$ because the photons received decrease in inverse proportion to $(1+z)$. Because $d_M$ levels off at about 14 Gpc, the unbounded growth of $s_{\mathrm{ph}}$ as $z\to\infty$ comes from the $\sqrt{1+z}$ term due to $T_{\max}$.
3. Before the surface of last scattering, the opacity of (a) in the main text multiplies the usable photons by $e^{-\tau}$ and $s_{\mathrm{ph}}$ by a further $e^{\tau/2}$.

Therefore, under this essay's principles that the observation time and the aperture have upper limits and that the precision of a measurement is set by the wavelength and number of the photons, within the range computed for the example with a fixed source, the smallest separation that can be distinguished grows monotonically further into the past and, as a consequence of $T_{\max}$, tends to grow without bound the further one goes back. This is an example consistent with distinctions becoming more ambiguous the further one goes back into the past. If the wavelength of the source or the number of photons it emits changes with epoch, the values change (Section 10.4).

### 10.6 Status

| Content | Kind |
|---|---|
| Applying the expression of the main text (the first part of the expression in Section 10.1); the dependence on wavelength in Section 10.4 | Application of existing expressions |
| The upper limit on the turnaround radius [8], the return to the diffraction limit under misalignment [9], the uncertainty relation between position and momentum and the diffraction limit, the standard error of a mean of $N$ | Existing results |
| Bringing in the arriving fraction $T/[(1+z)\,t_{\mathrm{life}}]$; the derivations of Section 10.3 (1) to (3) | Rough estimates of this essay |
| That the mass that can be gathered is limited to the bound structure to which the observer belongs | Consequence of existing results |
| That the observation time and the size of the aperture have upper limits, and that precision is set by the wavelength and number of the photons | Principles adopted by this essay (for the observation time, motivated by [14]) |
| That the lower limit on the precision of the shape of the apparatus is of the order of the Planck length | Rough estimate of this essay (the same approach as Section 4); the actual error is larger |
| The $(l_P^2L)^{1/3}$-type estimate [11] | Heuristic estimate; it has been criticized and disputed [12, 13]. Not used for the conclusion of this section |
| The numbers | Orders of magnitude. When the aperture is large compared with the distance to the source, as in the first example of Section 10.2, the assumptions of the expression in the main text (small angles and so on) fail |
| The conclusion of Section 10.5 | Estimate of this essay (based on the three principles above and the example with a fixed source) |

## References

1. V. B. Braginsky, F. Ya. Khalili, *Quantum Measurement*, ed. K. S. Thorne (Cambridge University Press, 1992).
2. H. P. Yuen, "Contractive States and the Standard Quantum Limit for Monitoring Free-Mass Positions," Physical Review Letters 51, 719 (1983). [Paper](https://doi.org/10.1103/PhysRevLett.51.719)
3. P. Hayden, K. Milner, M. M. Wilde, "Quantum Interactive Proofs and the Complexity of Separability Testing," Theory of Computing 11 (2015), 201–232. [Paper](https://theoryofcomputing.org/articles/v011a003/)
4. S. L. Braunstein, C. M. Caves, "Statistical distance and the geometry of quantum states," Physical Review Letters 72, 3439 (1994). [Paper](https://doi.org/10.1103/PhysRevLett.72.3439)
5. J. Liu, H. Yuan, X.-M. Lu, X. Wang, "Quantum Fisher information matrix and multiparameter estimation," J. Phys. A: Math. Theor. 53, 023001 (2020). [Paper](https://arxiv.org/abs/1907.08037)
6. A. G. Cohen, D. B. Kaplan, A. E. Nelson, "Effective Field Theory, Black Holes, and the Cosmological Constant" (1999). [Paper](https://arxiv.org/abs/hep-th/9803132)
7. R. Bousso, "A Covariant Entropy Conjecture" (1999). [Paper](https://arxiv.org/abs/hep-th/9905177)
8. V. Pavlidou, T. N. Tomaras, "Where the world stands still: turnaround as a strong test of ΛCDM cosmology," JCAP (2014). [Paper](https://arxiv.org/abs/1310.1920)
9. J. O. de Almeida, J. Kołodyński, C. Hirche, M. Lewenstein, M. Skotiniotis, "Discrimination and estimation of incoherent sources under misalignment," Physical Review A 103, 022406 (2021). [Paper](https://arxiv.org/abs/2003.01166)
10. H. Salecker, E. P. Wigner, "Quantum Limitations of the Measurement of Space-Time Distances," Physical Review 109, 571 (1958). [Paper](https://doi.org/10.1103/PhysRev.109.571)
11. Y. J. Ng, H. van Dam, "Measuring the Foaminess of Space-Time with Gravity-Wave Interferometers" (1999). [Paper](https://arxiv.org/abs/gr-qc/9906003)
12. L. Diósi, B. Lukács, "Critique of proposed limit to space–time measurement, based on Wigner's clocks and mirrors" (1995). [Paper](https://arxiv.org/abs/quant-ph/9501001)
13. J. C. Baez, S. J. Olson, "Uncertainty in measurements of distance," Classical and Quantum Gravity 19, L121 (2002). [Paper](https://arxiv.org/abs/gr-qc/0201030)
14. L. M. Krauss, G. D. Starkman, "Life, the Universe, and Nothing: Life and Death in an Ever-Expanding Universe" (1999). [Paper](https://arxiv.org/abs/astro-ph/9902189)

[Back to the main text](zerothOrderPhase.en.html) / [Back to Appendix 1](appendix1.en.html)

---

**Author**: 5garashi.com Design Office  
**Last updated**: 2026-11-08 JST
