---
title: 'Appendix 1: The Logical Background of the Three-Phase Model of Observation Limits'
lang: en
math: true
appendix: true
translation: /appendix1.html
description: Separates existing theory, epistemological definitions, and original hypotheses, defines the effective dimension from the set of observables and the quantum Fisher information matrix, and organizes the relations among the three phases.
---
<!--
  File: appendix1.en.md
  Description: Definitions of the three-phase model, indistinguishability for an observer and the effective dimension, and the logical background (English translation)
  Author: 5garashi.com Design Office
  Created: 2026-11-07
  Last updated: 2026-11-07 JST
  Version: 2.0.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Appendix 1: The Logical Background of the Three-Phase Model of Observation Limits

**Author:** 5garashi.com Design Office

**Version:** <span data-version>2.0.0</span>　**Last updated:** 2026-11-07 JST

This appendix presents the logical framework that organizes distinguishability for an observer by three concepts: the Spacetime-Limit Phase, the Dimension-Reduction Phase, and the Zeroth-Order Phase. It separates the constraints shown by existing theory, epistemological definitions, and original hypotheses, and defines indistinguishability for an observer and the effective dimension in the language of measurement.

[Main text: Observation Limits and the Undifferentiated Origin](zerothOrderPhase.en.html) / [Appendix 2: Mathematical notes](appendix2.en.html) / [Appendix 3: The CCC connection](appendix3.en.html)

## 1. Existing Theory, Epistemological Definitions, and Original Hypotheses

The three-phase model separates proven physical constraints from the definitions and hypotheses introduced by this essay.

| Category | Content | Logical role in this essay |
|---|---|---|
| **Constraints of existing theory** | Uncertainty relations, dispersion of free wave packets, partial traces, monotonicity of the QFI, holographic bounds, and so on | Show the concrete limits on observables and localization under specified physical conditions |
| **Epistemological definition** | Differences that cannot in principle be discriminated by any available observation are not treated as physical distinctions in that observer's description | Sets the convention for what is called a physical distinction or a difference between states |
| **Original hypothesis** | The degrees of freedom, scales, and effective dimension that support discrimination are transformed, and finally the criteria for discrimination themselves are lost | Proposes a connection model from the Spacetime-Limit Phase through the Dimension-Reduction Phase to the Zeroth-Order Phase |

From existing theoretical constraints (for example, the loss of information under a partial trace), "dimensional reduction of spacetime itself" or "the existence of the Zeroth-Order Phase" does not follow automatically. These are additional hypotheses for considering the connection.

### 1.1 Formalizing Distinction for an Observer

Let $\mathcal A_O$ be the set of observables (measurable physical quantities) available to an observer $O$. In algebraic quantum field theory, a theory is built by assigning an algebra of observables to each region of spacetime [1]. This essay borrows that idea and defines $\mathcal A_O$ as "all measurements the observer can use in principle". For two states $\rho,\sigma$,

$$
\rho\sim_O\sigma
\quad\Longleftrightarrow\quad
\operatorname{Tr}(\rho\,a)=\operatorname{Tr}(\sigma\,a)\quad\text{for all } a\in\mathcal A_O
$$

is defined as "indistinguishable for the observer $O$". If the expectation values of all observables in $\mathcal A_O$ are equal, the outcome distributions of all measurements that can be built within $\mathcal A_O$ are also equal. The epistemological position of the introduction amounts to treating two states satisfying this relation as the same physical state.

$\mathcal A_O$ represents the totality of measurements available in principle, not the apparatus at hand. For this reason, a case in which states cannot be distinguished merely because the apparatus is poor is not counted as indistinguishability. Removing unobservable degrees of freedom by a partial trace amounts to taking $\mathcal A_O$ to be the observables of the observable subsystem, and in this case distinction is determined by whether the subsystem density matrices $\rho_{\mathrm{obs}}$ are equal.

## 2. Definitions of the Three-Phase Model and Their Relation to the Main Text

| Phase | Physical and conceptual meaning | What can be defined, and open issues |
|---|---|---|
| **Spacetime-Limit Phase** | The ability to discriminate states decreases while the spacetime framework is maintained | Observables and degrees of discrimination can be defined. Strict indistinguishability ($T=0$) is distinguished from limits approaching it |
| **Dimension-Reduction Phase** | Fewer spacetime directions can be distinguished independently by the observer | The effective dimension $D_{\mathrm{eff}}$ is defined in Section 2.1. Laws for how it decreases in which physical systems are not established |
| **Zeroth-Order Phase** | The criteria of discrimination themselves, such as position, time, and scale, can no longer be applied | An original concept of this essay, not a demonstrated physical phase |

"Phase" is a name for the state of an observer's description; it does not mean a thermodynamic phase transition or a quantum phase transition in which the character of a ground state changes. A place where such a state holds is called a "region", and where the place is a surface, as for CCC in Appendix 3, a "boundary".

The main symbols used in this essay are summarized below.

| Symbol | Meaning | Where defined |
|---|---|---|
| $O$, $\mathcal A_O$ | The observer, and the set of observables the observer can use in principle | Section 1.1 |
| $\rho\sim_O\sigma$ | Two states are indistinguishable for the observer $O$ | Section 1.1 |
| $q$, $\lambda$ | The spacetime parameters the observer assigns to events, and the parameter expressing the approach to a limit | Section 2.1 (1) |
| $\rho_O(q,\lambda)$ | The observer's state, restricted to $\mathcal A_O$ | Section 2.1 (1) |
| $F$ | The quantum Fisher information matrix | Section 2.1 (2) |
| $K=EFE$, $\kappa_i$ | The matrix made dimensionless by the required resolution, and its eigenvalues | Section 2.1 (3) |
| $N$, $N_{\max}$ | The number of measurements, and its upper limit set by the observer's resources | Section 2.1 (4), [Main text, Section 4.2](zerothOrderPhase.en.html) |
| $D_{\mathrm{eff}}$ | The effective dimension; at finite $N$, an auxiliary indicator of how readable each direction is | Section 2.1 (5) |
| $d_O$ | The rank of $F$, constant over a range of the parameters; used to classify phases | Section 2.1 (6) |
| $\mathcal R_O$ | The procedure for assigning times and distances from observational records | [Appendix 3, Section 4](appendix3.en.html) |

### 2.1 Definition of the Effective Dimension

The effective dimension is defined from the sensitivity of the measurements available to the observer.

**(1) Parameters and family of states.** Let $q=(q^0,q^1,q^2,q^3)$ be the spacetime parameters the observer assigns to events, and $\lambda$ the parameter expressing the approach to a limit. $\lambda$ is an index that describes the approach from outside the model, not a clock read by the observer. The family of states $\rho(q,\lambda)$ restricted to $\mathcal A_O$ is the observer's state $\rho_O(q,\lambda)$. The family of states used to determine the phase represents records, such as clocks, rulers, and signals, that the observer can use to construct spacetime relations. This condition separates the case in which an arbitrarily chosen object does not respond to position or time from the case in which the observer cannot in principle construct distinctions of position or time. It is this condition that ties the rank to the ability to discriminate spacetime.

**(2) Quantum Fisher information matrix.** Let $F_{\mu\nu}(q,\lambda)$ be the quantum Fisher information matrix (QFIM) of $\rho_O(q,\lambda)$. For any measurement chosen from $\mathcal A_O$, the classical Fisher information matrix $I$ of that measurement satisfies $I\le F$ (as a matrix inequality) [2, 3]. $F$ represents the upper limit on the sensitivity obtainable by any available measurement.

**(3) Making it dimensionless by the resolution.** Let $\varepsilon_\mu$ be the resolution the observer requires in direction $\mu$, set $E=\operatorname{diag}(\varepsilon_0,\dots,\varepsilon_3)$, and form

$$
K = E\,F\,E
$$

Let the eigenvalues of $K$ be $\kappa_1,\dots,\kappa_4\ (\ge0)$.

**(4) Readable directions.** With $N$ independent measurements, the quantum Cramér–Rao bound makes the covariance of the estimates at least $(NF)^{-1}$ [3]. In the direction of eigenvalue $\kappa_i$, the lower limit on the standard deviation in units of the resolution is $1/\sqrt{N\kappa_i}$. Therefore, if $N\kappa_i\ll1$, that direction cannot be read at the required resolution whichever measurement is chosen. $N\kappa_i\ge1$ is a guide that the required resolution is not excluded by the lower bound of estimation. Whether that resolution is actually reached is examined after the measurement method is specified. Because the aperture, time, energy, and recording capacity available to the observer are finite, $N$ has an upper limit $N_{\max}$, and directions with $N_{\max}\kappa_i\ll1$ cannot in principle be read ([Main text, Section 4.2](zerothOrderPhase.en.html)).

**(5) Effective dimension.** Counting the contribution of each direction smoothly, define

$$
D_{\mathrm{eff}}(q,\lambda;N,\varepsilon)=\sum_{i=1}^{4}\frac{N\kappa_i}{1+N\kappa_i},
\qquad
n=4-D_{\mathrm{eff}}
$$

| Property | Content |
|---|---|
| Range | $0\le D_{\mathrm{eff}}\le4$. Each term is close to 1 for $N\kappa_i\gg1$ and close to $N\kappa_i$ for $N\kappa_i\ll1$ |
| Continuity | As the sensitivity $\kappa_i$ decreases, $D_{\mathrm{eff}}$ decreases continuously |
| Limit of many measurements | As $N\to\infty$, every direction with $\kappa_i>0$ contributes 1, and $D_{\mathrm{eff}}\to\operatorname{rank}F$. The relation between rank and indistinguishability is described in (6) |

**(6) Rank and indistinguishability.** The rank of $F$ expresses the first-order sensitivity at that point. A drop in rank at one point does not imply indistinguishability. For example, in a model in which the mean of the measurement outcome is $q^3$ (q cubed), the Fisher information vanishes at $q=0$, but finitely different $q$ give different distributions.

On the other hand, suppose that $Fv=0$ holds for some direction $v$ throughout a range $U$ of the parameters. If the rank of the density matrices does not change in $U$, the Bures distance does not exceed the length of a curve measured with the metric $F/4$. Taking a curve $\gamma$ in $U$ that connects $q$ and $q'$ along $v$, its length is zero, so

$$
D_{\mathrm{Bures}}\!\left(\rho_O(q),\rho_O(q')\right)\le\frac12\int_{\gamma}\sqrt{\dot q^{\mathsf T}F\,\dot q}\;\mathrm{d}s=0
\quad\Longrightarrow\quad
\rho_O(q)\sim_O\rho_O(q')
$$

For the same reason, when the tangent vector of a curve lies in the kernel of $F$ at every point (a curve tangent to the kernel), the states at its two ends cannot be distinguished.

Write $d_O$ for the rank that is constant over the range $U$. If the rank of the density matrices is constant, $Fv=0$ is the same as $\partial_v\rho_O=0$, and the rank of the map $q\mapsto\rho_O(q)$ is also constant at $d_O$. By the constant rank theorem, the set of points at which the states are equal locally forms a smooth set of dimension $4-d_O$. Therefore, in a region of constant rank, states on a curve tangent to the kernel are strictly indistinguishable in the sense of Section 1.1, and locally there are $4-d_O$ such indistinguishable degrees of freedom. The indistinguishable directions are not necessarily along fixed coordinate axes. For example, if the state depends only on $q_1^2+q_2^2$, the indistinguishable direction is tangent to a circle and changes from place to place.

To determine the three phases, the following quantities are used with separate roles.

| Quantity | Role |
|---|---|
| $D_{\mathrm{eff}}$ at finite $N$ | An auxiliary indicator of how well each direction can be read under those measurement conditions. It does not determine the phase |
| The rank $d_O$, constant over the range $U$ | If the trace distance or total variation distance of the pairs of states compared becomes small while $d_O=4$, the phase is the Spacetime-Limit Phase. If $d_O<4$, it is the Dimension-Reduction Phase, and $\sim_O$ holds strictly along the lost directions |
| Decay of the eigenvalues, and $D_{\mathrm{eff}}\to0$ under fixed measurement conditions | An indicator that the sensitivity is weakening and the Zeroth-Order Phase is being approached. In a process in which sensitivity is lost smoothly, the rank need not drop in steps |
| A drop in the rank $d_O$ | An independent direction has been lost. It occurs where the corresponding sensitivity actually vanishes throughout a range of the parameters |
| The Zeroth-Order Phase | The procedure $\mathcal R_O$ does not hold (Appendix 3, Section 4), and states are indistinguishable under $\sim_O$. It is not required that $F$ be defined there |

The conditions of validity and how to read them are as follows.

- When several parameters are estimated simultaneously and the optimal measurements for different directions are incompatible, the quantum Cramér–Rao bound is not reached [3]. In that case $D_{\mathrm{eff}}$ gives an upper limit on the number of readable directions.
- A non-integer $D_{\mathrm{eff}}$ does not express a topological dimension or "how many dimensions the space has". $D_{\mathrm{eff}}=0$ does not mean that a zero-dimensional space was measured.
- The spectral dimension of quantum gravity is defined from the return probability of a diffusion process, and its definition differs [4, 5]. Results on the spectral dimension are prior results showing that the effective dimension depends on the scale probed, and this essay cites them as a precedent for considering the Dimension-Reduction Phase. Computing the correspondence between the two quantities in concrete systems is a task for future work.

A concrete example (a model with independent Gaussian noise) is given in Section 4.1 of Appendix 3.

### 2.2 Logical Caveats in Connecting the Three Phases

Local indistinguishability, constraints on degrees of freedom, transformation of scale, and decrease of the effective dimension are separate concepts. Even if one holds, the others do not follow automatically. This essay examines the conditions under which they are tied together as the connection of the three phases.

## 3. Premises for Reading the Equations and Physical Concepts

### 3.1 Treatment of Time and Energy

In standard quantum mechanics, time is treated as an external parameter. The position–momentum relation and the time–energy relation are not treated as having the same operator structure. The time–energy relation is used as an estimation limit, namely how precisely elapsed time can be estimated from a change of state ([supplementary note on the QFI (in Japanese)](補足資料/QFI解説.html)), and no universal minimum time is derived from it.

### 3.2 Treatment of the Planck Scale

The Planck length and the Planck time are the natural scales at which quantum theory and gravity must be considered together. The argument comparing the energy needed for localization with the gravitational radius is used as a heuristic estimate, not as a proof of a minimum length.

### 3.3 Treatment of Partial Traces and Toy Models

A partial trace is an operation that removes an unobservable subsystem from the observational description; it does not physically erase the information of the total system. In the two-level model of Appendix 2 ($0\le\theta\le\pi/2$), the trace distance of the subsystem is $T=\cos\theta$ and approaches zero as $\theta\to\pi/2$, while the two states of the total system remain orthogonal. What this model directly shows is local indistinguishability in the Spacetime-Limit Phase, not dimensional reduction.

### 3.4 Extension to Five Limit Regions

Adding infinitesimal time division ($\Delta t\to0$) to the four limits of the main text as an independent line of inquiry allows five limit regions to be compared. The suppression of state transitions by the quantum Zeno effect is distinguished from indistinguishability of states. The correspondence between each region and the three phases is given in Section 9 of Appendix 2.

## 4. Tasks Toward Modeling

To develop the three phases into a physical model, the following must be specified for concrete physical systems.

1. The set of observables $\mathcal A_O$ available to the observer, and the family of states $\rho(q,\lambda)$ to be compared.
2. The required resolutions $\varepsilon_\mu$, and the behavior of the eigenvalues $\kappa_i(\lambda)$ of the quantum Fisher information matrix under them.
3. Under what conditions the decrease of $D_{\mathrm{eff}}$ and the failure of the procedure $\mathcal R_O$ are tied together.

## References

1. R. Haag, *Local Quantum Physics* (Springer, 2nd ed., 1996).
2. S. L. Braunstein, C. M. Caves, "Statistical distance and the geometry of quantum states", Phys. Rev. Lett. 72, 3439 (1994).
3. J. Liu, H. Yuan, X.-M. Lu, X. Wang, "Quantum Fisher information matrix and multiparameter estimation", J. Phys. A: Math. Theor. 53, 023001 (2020). [Paper](https://arxiv.org/abs/1907.08037)
4. S. Carlip, "Dimension and dimensional reduction in quantum gravity", Class. Quantum Grav. 34, 193001 (2017). [Paper](https://arxiv.org/abs/1705.05417)
5. J. Ambjørn, J. Jurkiewicz, R. Loll, "Spectral dimension of the universe is scale dependent", Phys. Rev. Lett. 95, 171301 (2005). [Paper](https://arxiv.org/abs/hep-th/0505113)

[Back to the main text](zerothOrderPhase.en.html) / [Go to Appendix 2](appendix2.en.html)

---

**Author**: 5garashi.com Design Office  
**Last updated**: 2026-11-07 JST
