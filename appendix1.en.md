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
  Last updated: 2026-11-11 JST
  Version: 2.4.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Appendix 1: The Logical Background of the Three-Phase Model of Observation Limits

**Author:** 5garashi.com Design Office

**Version:** <span data-version>2.4.0</span>　**Last updated:** 2026-11-11 JST

This appendix presents the logical framework that organizes distinguishability for an observer by three concepts: the Spacetime-Limit Phase, the Dimension-Reduction Phase, and the Zeroth-Order Phase. It separates the constraints shown by existing theory, epistemological definitions, and original hypotheses, and defines indistinguishability for an observer and the effective dimension in the language of measurement. Sections 1 and 2 define distinction and the three phases; Section 3 gives kinematic models based on families of states; Section 4 gives dynamical models in which the observer's records relax; Section 5 collects the premises for reading the equations (including the distinction between kinematics and dynamics in general relativity); and Section 6 summarizes open tasks.

[Main text: Observation Limits and the Undifferentiated Origin](zerothOrderPhase.en.html) / [Appendix 2: Mathematical notes](appendix2.en.html) / [Appendix 3: The CCC connection](appendix3.en.html) / [Appendix 4: Distant observation](appendix4.en.html)

## 1. Existing Theory, Epistemological Definitions, and Original Hypotheses

The three-phase model separates proven physical constraints from the definitions and hypotheses introduced by this essay.

| Category | Content | Logical role in this essay |
|---|---|---|
| **Constraints of existing theory** | Uncertainty relations, dispersion of free wave packets, partial traces, monotonicity of the Fisher metric and the QFI [6, 7], holographic bounds, and so on | Show the concrete limits on observables and localization under specified physical conditions |
| **Epistemological definition** | Differences that cannot in principle be discriminated by any available observation are not treated as physical distinctions in that observer's description | Sets the convention for what is called a physical distinction or a difference between states |
| **Original hypothesis** | The degrees of freedom, scales, and effective dimension that support discrimination are transformed, and finally the criteria for discrimination themselves are lost | Proposes a connection model from the Spacetime-Limit Phase through the Dimension-Reduction Phase to the Zeroth-Order Phase |

From existing theoretical constraints (for example, the loss of information under a partial trace), "dimensional reduction of spacetime itself" or "the existence of the Zeroth-Order Phase" does not follow automatically. These are additional hypotheses for considering the connection.

### 1.1 Formalizing Distinction for an Observer

Let $\mathcal A_O$ be the set of observables (measurable physical quantities) available to an observer $O$. In algebraic quantum field theory, a theory is built by assigning an algebra of observables to each region of spacetime [1]. This essay borrows that idea and defines $\mathcal A_O$ as "all measurements that can be performed under the laws of physics and the stated resource constraints of the observer". For two states $\rho,\sigma$,

$$
\rho\sim_O\sigma
\quad\Longleftrightarrow\quad
\operatorname{Tr}(\rho\,a)=\operatorname{Tr}(\sigma\,a)\quad\text{for all } a\in\mathcal A_O
$$

is defined as "indistinguishable for the observer $O$". Here $a$ is an effect operator (an element of a POVM) of an allowed measurement, and $\mathcal A_O$ is a set containing them. If the expectation values of all effect operators of the allowed measurements are equal, the outcome distributions of those measurements are also equal. The set of measurements allowed by resource constraints is in general not an algebra. Moreover, procedures that include interventions in a history cannot be exhausted by the observables at a single time. For this reason, the general definition is given by the outcome distributions of allowed measurements and procedures ([Appendix 3, Section 4](appendix3.en.html)). The epistemological position of the introduction amounts to treating two states satisfying this relation as the same physical state.

For the models of Sections 3 and 4, which use the quantum Fisher information, the observation conditions are specified as follows. There are four premises. (i) A finite-dimensional Hilbert space is considered, and $\mathcal A_O$ is a unital $*$-subalgebra on it (a set of observables closed under sums, products, and Hermitian conjugation). (ii) The allowed measurements are all POVMs whose effect operators belong to $\mathcal A_O$. (iii) $\mathcal E_O$ is a trace-preserving conditional expectation onto $\mathcal A_O$, and the state restricted to that algebra, $\rho_O=\mathcal E_O(\rho)$, is used. (iv) The family of states is differentiable on an open range of the parameters. Then the outcome distributions of the allowed measurements are the same for $\rho$ and $\rho_O$. Moreover, the symmetric logarithmic derivative of $\rho_O$ can be taken inside $\mathcal A_O$ (for non-faithful states it is not unique on the kernel, but the value of the quantum Fisher information does not change), and the measurement by its spectral projections is among the allowed measurements. Therefore, for a single parameter, the quantum Fisher information of $\rho_O$ equals, at each parameter point, the highest sensitivity obtainable from the allowed measurements; for several parameters, the SLD quantum Fisher information matrix is an upper bound, in the positive semidefinite order, on the classical Fisher information matrix of each allowed measurement. However, a single measurement need not reach the whole matrix, and the optimal measurement may change from point to point.

Some examples follow. When restricting to observables invariant under global time translation, the projections $P_\alpha$ onto the eigenspaces of the total energy give $\mathcal E_O(\rho)=\sum_\alpha P_\alpha\rho P_\alpha$, which removes the components between blocks (it is not a projection onto a particular block followed by postselection). When restricting to observables invariant under spatial translation, the eigenspaces of the total momentum are used. Removing the phase coherence in some basis has the same form. When only a subsystem $A$ can be measured, $\mathcal A_O=\mathcal B(\mathcal H_A)\otimes I_B$ and $\mathcal E_O(\rho)=\operatorname{Tr}\nolimits_B(\rho)\otimes I_B/d_B$. The partial trace $\rho_A=\operatorname{Tr}\nolimits_B\rho$ expresses this on the space of subsystem $A$, and the quantum Fisher information is the same for both.

If the quantum Fisher information of the original state is computed without the restriction, differences that the allowed measurements cannot see are also counted. For example, if only measurements in the z basis are allowed and the state is $(\lvert0\rangle+e^{iq}\lvert1\rangle)/\sqrt2$, the outcome distribution of the allowed measurement does not depend on $q$, but the quantum Fisher information of the original state is 1. On the Bloch sphere, $q$ rotates the arrow along the equator, but a measurement in the z basis sees only the height of the arrow and cannot see the rotation. The quantum Fisher information of the original state is the highest sensitivity at each point when measurements that read the phase along the equator can also be used. Restricting, in accordance with the allowed measurement, to the algebra of observables diagonal in the z basis gives $\rho_O=\operatorname{diag}(\tfrac12,\tfrac12)$, which does not depend on $q$; the quantum Fisher information is then 0, in agreement with the allowed measurement being unable to distinguish.

When the allowed POVMs do not coincide with all POVMs in some algebra, as when only the output of a fixed measuring apparatus can be used or only measurements with particular noise or coarse-graining are allowed, the quantum Fisher information is not used; instead the classical Fisher information for that set of measurements is used. For a single parameter, the supremum of that classical Fisher information over the allowed measurements is considered; for several parameters, an optimization with a specified direction or evaluation criterion is considered. The degree of distinction by outcome distributions ($\Delta_O$ in [Appendix 3, Section 4](appendix3.en.html)) can also be used.

$\mathcal A_O$ represents not the apparatus at hand but the totality of measurements that can in principle be performed under the laws of physics and the resource constraints. Indistinguishability caused only by insufficient performance of the apparatus at hand, not included in the stated resource constraints, is not counted as indistinguishability here. Whether states can be distinguished may change with how the resource constraints are chosen. Removing unobservable degrees of freedom by a partial trace amounts to taking $\mathcal A_O$ to be the observables of the observable subsystem, and in this case distinction is determined by whether the subsystem density matrices $\rho_{\mathrm{obs}}$ are equal.

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
| $O$, $\mathcal A_O$ | The observer, and the set of observables the observer can use under the laws of physics and the resource constraints | Section 1.1 |
| $\rho\sim_O\sigma$ | Two states are indistinguishable for the observer $O$ | Section 1.1 |
| $q$, $\lambda$ | The parameters of time and distance that the observer reads with means of observation (not external coordinates), and the parameter expressing the approach to a limit | Section 2.1 (1) |
| $\rho_O(q,\lambda)$ | The observer's state, restricted to $\mathcal A_O$ | Section 2.1 (1) |
| $F$ | The quantum Fisher information matrix | Section 2.1 (2) |
| $K=EFE$, $\kappa_i$ | The matrix made dimensionless by the required resolution, and its eigenvalues | Section 2.1 (3) |
| $N$, $N_{\max}$ | The number of measurements, and its upper limit set by the observer's resources | Section 2.1 (4), [Main text, Section 4.2](zerothOrderPhase.en.html) |
| $D_{\mathrm{eff}}$ | The effective dimension; at finite $N$, an auxiliary indicator of how readable each direction is | Section 2.1 (5) |
| $d_O$ | The rank of $F$, constant over a range of the parameters; used to classify phases | Section 2.1 (6) |
| $P_\mu$, $G_i$ | The generators of spacetime translations (the Hamiltonian for the time direction, the momentum for spatial directions), and the generators along the eigendirections of $K$ | Section 3.1 (1), (3) |

### 2.1 Definition of the Effective Dimension

The effective dimension is defined from the sensitivity of the measurements available to the observer.

**(1) Parameters and family of states.** Let $q=(q^0,q^1,q^2,q^3)$ be the spacetime parameters the observer assigns to events, and $\lambda$ the parameter expressing the approach to a limit. $q$ consists of times and distances that the observer reads with means of observation, not external coordinates. $\lambda$ is an index that describes the approach from outside the model, not a clock read by the observer. The family of states $\rho(q,\lambda)$ restricted to $\mathcal A_O$, that is, the output $\rho_O(q,\lambda)=\mathcal E_O\bigl(\rho(q,\lambda)\bigr)$ of a parameter-independent channel $\mathcal E_O$, is the observer's state (the observation conditions of Section 1.1). $\rho_O$ is taken to be continuously differentiable in $q$, and as smooth as needed where the constant rank theorem of (6) is used. The family of states used to determine the phase represents records, such as clocks, rulers, and signals, that the observer can use to read times and distances. This condition separates the case in which an arbitrarily chosen object does not respond to position or time from the case in which the observer has, in principle, no means of observation that distinguishes positions or times. It is this condition that ties the rank to the ability to discriminate spacetime.

**(2) Quantum Fisher information matrix.** Let $F_{\mu\nu}(q,\lambda)$ be the quantum Fisher information matrix (QFIM) of $\rho_O(q,\lambda)$. Here the QFIM is the one defined by the symmetric logarithmic derivative (SLD). For any measurement chosen from $\mathcal A_O$, the classical Fisher information matrix $I$ of that measurement satisfies $I\le F$ (as a matrix inequality) [2, 3]. $F$ represents the upper limit on the sensitivity obtainable by any available measurement. When the observation conditions are specified by an algebra of observables and its conditional expectation, measurements on $\rho_O$ give the same results as measurements in $\mathcal A_O$, and $F$ expresses the sensitivity of the allowed measurements (Section 1.1). When the allowed measurements do not coincide with all POVMs in some algebra, $F$ remains an upper bound. A direction in which $F$ is 0 also has zero first-order sensitivity for the allowed measurements, but the converse is not guaranteed, and the kernel of $F$ alone cannot fully determine the directions the allowed measurements cannot distinguish. In that case the Fisher information of the allowed measurements or $\Delta_O$ is used (Section 1.1).

**(3) Making it dimensionless by the resolution.** Let $\varepsilon_\mu$ be the resolution the observer requires in direction $\mu$, set $E=\operatorname{diag}(\varepsilon_0,\dots,\varepsilon_3)$, and form

$$
K = E\,F\,E
$$

Let the eigenvalues of $K$ be $\kappa_1,\dots,\kappa_4\ (\ge0)$.

**(4) Readable directions.** With $N$ independent measurements and a locally unbiased estimator, the quantum Cramér–Rao bound makes the covariance of the estimates at least $(NF)^{-1}$ [3]. When $F$ is singular, no locally unbiased estimator exists along the kernel of $F$, so this bound is used restricted to the eigendirections with $\kappa_i>0$. In the direction of eigenvalue $\kappa_i$, the lower limit on the standard deviation in units of the resolution is $1/\sqrt{N\kappa_i}$. Therefore, if $N\kappa_i\ll1$, that direction cannot be read at the required resolution by locally unbiased estimation, whichever measurement is chosen. This bound does not limit the precision of biased estimation or estimation using prior information, and it does not show that two states a finite distance apart cannot be discriminated. The discrimination of states a finite distance apart is treated separately with the trace distance or the error probability of discrimination. $N\kappa_i\ge1$ is a guide that the required resolution is not excluded by the lower bound of estimation. Whether that resolution is actually reached is examined after the measurement method is specified. Because the aperture, time, energy, and recording capacity available to the observer are finite, $N$ has an upper limit $N_{\max}$, and directions with $N_{\max}\kappa_i\ll1$ cannot be read at the required resolution by locally unbiased estimation even with all the observer's resources ([Main text, Section 4.2](zerothOrderPhase.en.html)).

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

**(6) Rank and indistinguishability.** The rank of $F$ expresses the first-order sensitivity at that point. A drop in rank at one point does not imply indistinguishability. For example, in a model in which the mean of the measurement outcome is $q^3$, the Fisher information vanishes at $q=0$, but finitely different $q$ give different distributions.

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
| The Zeroth-Order Phase | There are no means of observation that distinguish differences in time, distance, direction, or causal order (Appendix 3, Section 4), and states are indistinguishable under $\sim_O$. It is not required that $F$ be defined there. The formula by outcome distributions is in Appendix 3, Section 4 |

In the finite-dimensional models of Sections 3 and 4, the number of compared parameters is $m$ ($m\le4$), and within a model $d_O=m$ is associated with the Spacetime-Limit Phase and $d_O<m$ with the Dimension-Reduction Phase. This is an association within the model, not a judgment of the phase over all the observer's means. "Spacetime-Limit Phase" and "Dimension-Reduction Phase" in the sections on models are used in this sense. The rank is used for the judgment when the observation conditions are specified by an algebra of observables and its conditional expectation and $F$ is computed for the restricted state (Section 1.1; (2)). The models of this appendix (projection onto blocks, partial trace) satisfy this condition. When the allowed measurements do not form an algebra, the definition by outcome distributions ([Appendix 3, Section 4](appendix3.en.html)) takes precedence.

The conditions of validity and how to read them are as follows.

- When several parameters are estimated simultaneously and the optimal measurements for different directions are incompatible, the quantum Cramér–Rao bound is not reached [3]. $D_{\mathrm{eff}}$ is an auxiliary indicator that smoothly counts the sensitivity given by the quantum Fisher information; it gives neither an upper nor a lower limit on the number of directions that can be read simultaneously at the required resolution. For example, when $K$ is the identity and $N=1$, in a model that attains the bound the standard deviations in all four directions equal the resolution, yet $D_{\mathrm{eff}}=2$.
- A non-integer $D_{\mathrm{eff}}$ does not express a topological dimension or "how many dimensions the space has". $D_{\mathrm{eff}}=0$ does not mean that a zero-dimensional space was measured.
- A drop in $d_O$ means that directions the observer cannot distinguish have appeared; it does not mean that microscopic degrees of freedom themselves disappear.
- The rank is the number of independently distinguishable directions; it does not fix the distinction between time and space (the signature of the metric).
- When the same observational model is described after a Lorentz transformation, the rank $d_O$ does not change. This does not claim anything about observers in different states of motion who have different resource constraints. A Lorentz transformation changes the parameters of spacetime translations linearly ($U(\Lambda)T(a)U(\Lambda)^\dagger=T(\Lambda a)$). When the state and the set of observables available to the observer are both transformed by $U(\Lambda)$ and the block structure that fixes the available observables (the projections onto the joint eigenspaces of energy and momentum) is preserved by this transformation, the change of parameters $q'=\Lambda q$ turns the QFI matrix into $F'=\Lambda^{-\mathsf T}F\Lambda^{-1}$, and the rank does not change. Because the rank does not change under any invertible linear change of parameters, the substantive content of this item is that Lorentz transformations satisfy that condition. On the other hand, the eigenvalues and $D_{\mathrm{eff}}$ depend on the frame as long as the resolutions $\varepsilon_\mu$ are kept the same (they also change under a change of units). For a wave packet of a particle in 1+1 dimensions, it was checked numerically that the covariance of the translation generators (energy and momentum) transforms according to the transformation formula (difference below $10^{-10}$; this checks the transformation formula and is not a new physical test). For a particle of mass $1$ (momentum distribution normal with center $0.5$ and width $0.8$), the rank stays 2, while $D_{\mathrm{eff}}$ ($\varepsilon=0.1$, $N=100$) changes from $0.855$ to $0.936$ under a transformation of rapidity $0.7$. For a massless particle moving in one direction, the rank is 1 in every frame, and translations along the direction in which the light travels cannot be distinguished (with components in both directions the rank becomes 2). This numerical example concerns an observer with an external reference frame looking at a single particle, a premise different from the other models of this appendix, which use only observables invariant under global translations. This item concerns the frame independence of how the directions of spacetime translations are counted; it is not a model that adds boosts themselves to the compared parameters (Section 6).
- The quantum Fisher information matrix counts distinctions under continuous changes of the parameters. Discrete distinctions that are not connected through the continuous parameters of the family of states being compared (such as topological labels, or the labels of sectors separated by superselection rules) do not appear in the rank. However, quantities that can be treated as continuous parameters, such as the mixing proportions of the sectors, may have their changes reflected in the rank.
- The spectral dimension of quantum gravity is defined from the return probability of a diffusion process, and its definition differs [4, 5]. Results on the spectral dimension are prior results showing that the effective dimension depends on the scale probed, and this essay cites them as a precedent for considering the Dimension-Reduction Phase. Computing the correspondence between the two quantities in concrete systems is a task for future work.

A concrete example (a model with independent Gaussian noise) is given in Section 4.1 of Appendix 3.

### 2.2 Logical Caveats in Connecting the Three Phases

Local indistinguishability, constraints on degrees of freedom, transformation of scale, and decrease of the effective dimension are separate concepts. Even if one holds, the others do not follow automatically. This essay examines the conditions under which they are tied together as the connection of the three phases.

## 3. Kinematic Models: Distinction Seen in Families of States

The models of this section compute the quantum Fisher information matrix and its rank for families of states that line up differences in the prepared states. Time evolution (dynamics) is not treated (Section 4). The number of compared parameters is $m$, and the association with phases within a model follows the convention of Section 2.1. The setting of each model, and what it shows and does not show, are summarized below.

| Section | Compared parameters (number $m$) | Available observables | Operation or process | What it shows | What it does not show |
|---|---|---|---|---|---|
| 3.1 | Spacetime translations (up to 4) | The state of the object (global translations compared from outside) | None (a family of pure states) | For mutually commuting generators the QFI matrix is four times the covariance of the generators, and directions of zero sensitivity are limited to eigenstates; the correspondence between rank reduction and delocalization | A general measure of the depth of superposition; a connection to the Zeroth-Order Phase |
| 3.2 | Time and position, or relative time (1–2) | Specified case by case (with or without an external reference frame) | Adding clocks; destroying phase coherence | Whether a drop in rank comes from the symmetry of the object or from the observer's records can be separated by computing with added records | Four directions; all of the observer's means |
| 3.3 | Relative time (1) | Observables invariant under global time translation | Varying the parameter $\theta$ of the family of states (a hypothetical construction) | A family of states in which the sensitivity decreases continuously and becomes 0 at $\theta=0$; conditions under which a clock cannot be rebuilt | Time evolution; four directions; a connection to the Zeroth-Order Phase |

### 3.1 Reading in Models of Pure States: Correspondence with Superposition

In models of pure states that satisfy certain conditions, zero sensitivity in a spatial direction corresponds, in the position basis, to a superposition spread over the whole of that direction. This section gives the conditions and limitations under which this correspondence holds. Tying this correspondence to the connection of the three phases, in particular to the approach to the Zeroth-Order Phase, is an additional hypothesis of this essay ([Main text, Section 6](zerothOrderPhase.en.html)).

**(1) Conditions and formula.** Fix $\lambda$ of Section 2.1 (1), and let the observer's state be the pure state $\rho_O(q)=\lvert\psi(q)\rangle\langle\psi(q)\rvert$. The spacetime parameters enter through unitary translations $\lvert\psi(q)\rangle=\exp\left(-i\sum_{\mu}q^\mu P_\mu\right)\lvert\psi\rangle$ generated by $P_\mu$ (the Hamiltonian for the time direction and the momentum for spatial directions; $\hbar=1$). The generators are self-adjoint and strongly commuting (their spectral measures commute), the state belongs to the domains of the required products, and the second moments of the generators are finite. Then the quantum Fisher information matrix is four times the covariance of the generators [3].

$$
F_{\mu\nu}=4\left(\langle P_\mu P_\nu\rangle-\langle P_\mu\rangle\langle P_\nu\rangle\right)
$$

Because the right-hand side does not depend on $q$, the rank is constant over the whole parameter space. When the generators do not commute (for example, when rotations are included), this form does not hold in general, and the matrix is expressed by the symmetrized covariance of the local generators at each point [3].

**(2) Directions of zero sensitivity and eigenstates.** For a real vector $v$, with $P_v=\sum_\mu v^\mu P_\mu$,

$$
v^{\mathsf T}Fv=4\operatorname{Var}(P_v)=4\left\lVert\left(P_v-\langle P_v\rangle\right)\psi\right\rVert^2
$$

Because $F$ is positive semidefinite, $Fv=0$ holds only when the state is an eigenstate of $P_v$. Translations in the direction $v$ then change only the global phase of the state, so states connected along $v$ cannot be distinguished (Section 2.1 (6)).

In a spatial direction, an eigenstate of momentum, seen in the position basis, is a plane wave whose amplitude has the same magnitude at all positions in that direction and whose phase changes in proportion to position; it is a superposition over the whole of that direction. Whether a state is a superposition depends on the basis, and this superposition in the position basis is the same as the momentum having a single definite value. Conversely, a uniform probability density in position does not by itself make an eigenstate of momentum. For example, in a box of period $2\pi$, $\psi(x)=e^{ia\sin x}/\sqrt{2\pi}$ ($a\ne0$) has a uniform probability density, but $P\psi=a\cos x\,\psi$, and the QFI for spatial translation is $2a^2>0$. For spatial translations on the usual $L^2(\mathbb R)$, eigenstates of momentum cannot be normalized. Therefore, in this model, $Fv=0$ holds strictly in a spatial direction only when that direction is closed, or as a limit.

**(3) Separating decreased sensitivity from rank reduction.** Let $u_i$ be the normalized eigenvectors of $K=EFE$ and $G_i=\sum_\mu\varepsilon_\mu u_i^\mu P_\mu$; then $\kappa_i=4\operatorname{Var}(G_i)$. Because the eigenvectors may mix time and space directions, the following argument about the spread in position is limited to spatial directions for which a conjugate position can be defined.

With $N$ and $E$ fixed, when the momentum variance in some spatial direction decreases, the uncertainty relation $\Delta x\ge1/(2\Delta p)$ makes the lower limit on the spread in position in that direction grow. As an example in which the spread actually grows, a minimum-uncertainty Gaussian state has $\Delta x=1/(2\Delta p)$, so decreasing the momentum variance directly increases the spread in position. However, a decrease of $D_{\mathrm{eff}}$ does not mean a decrease of each eigenvalue, and $D_{\mathrm{eff}}$ also changes when $N$ or $E$ is changed. The value of $D_{\mathrm{eff}}$ itself is therefore not taken as a measure of the depth of superposition.

| Stage | Reading in the model of pure states | Phase (table in Section 2.1) |
|---|---|---|
| With $N$ and $E$ fixed, the momentum variance in some spatial direction decreases | The lower limit on the spread in position in that direction grows | The rank does not drop unless the variance becomes zero; the state can belong to the Spacetime-Limit Phase |
| $d_O$ drops by one | In one direction, the state becomes an eigenstate of the generator; in a spatial direction, a superposition over the whole of that direction (as a limit in an unbounded direction; normalizable examples are closed directions such as a box with periodic boundaries, (2)) | Dimension-Reduction Phase |
| $d_O=0$ | Within the family of states of this model, a simultaneous eigenstate of all four generators; translations in any direction change only the global phase | The extreme case of the Dimension-Reduction Phase. $d_O=0$ alone does not define the Zeroth-Order Phase; whether it is the Zeroth-Order Phase is decided by whether there are means of observation that distinguish spacetime differences (this section, (6) and (7)) |

**(4) The time direction.** Eigenstates of the generator of the time direction are energy eigenstates, stationary states that change only by a global phase with respect to time as an external parameter. Some energy eigenstates, such as bound states, can be normalized. For a Hamiltonian bounded below, there is no self-adjoint time operator satisfying a global canonical conjugate relation that shifts the energy by an arbitrary real amount (Pauli's argument). Self-adjoint operators representing clock readings in general are not excluded, but for this reason time does not necessarily have an operator basis in the same sense as position (Section 5.1), and the "superposition in the position basis" of spatial directions does not carry over directly to the time direction. Clock readings are treated as measurements of a clock (such as time observables represented as POVMs). Reading it as a superposition of clock readings requires a concrete model that specifies the clock as a quantum system, the interactions, the correlations of the total state, and so on.

In the canonical formulation of quantum gravity, states satisfying the Hamiltonian constraint $\hat H\Psi=0$ (the Wheeler–DeWitt equation) are written in a form that does not depend on an external time (the problem of time) [8]. This constraint plays a different role from the ordinary Hamiltonian that generates evolution in an external time, and its physical inner product and normalization are not trivial either. It is therefore not used as an example of the family of states or the QFI of (1). Page and Wootters gave a model in which a total state invariant under external time is compatible with relational change conditioned on a clock [9]. This essay cites it as an analogy for the idea that, even if distinctions are lost with respect to time as an external parameter, distinctions of time can be reconstructed from the records of a clock. The correspondence with $d_O$ is an untested analogy made by this essay. States in which distinctions of time can be constructed by a relational description are not included in the Zeroth-Order Phase ([Main text, Section 4.3](zerothOrderPhase.en.html)).

**(5) Relation to mixed states.** Distinctions are not lost only when the amplitude of a pure state spreads. Under a parameter-independent partial trace, the QFI does not increase and may decrease (Section 5.3; the two-level system of Appendix 2). Mixed states can also have off-diagonal components in the position basis, so the question is not an either-or between "superposition or mixture". What all cases have in common is that, when the rank of the state is constant, the observer's state stops changing under translations in the direction $v$ ($\partial_v\rho_O=0$, Section 2.1 (6)). The spreading of the amplitude of pure states alone cannot explain the whole of the loss of distinctions.

**(6) Relation to the Zeroth-Order Phase.** The correspondence of this section is a correspondence with spatial delocalization in a particular model of pure states. The degeneracy of the QFI is not a general measure of the depth of superposition, and it derives neither the Zeroth-Order Phase nor the loss of meaning of the position basis. There are models that are invariant under translations but in which the position basis and the geometric description remain. This essay does not define the Zeroth-Order Phase as a state of complete superposition, but by the absence of means of observation that distinguish spacetime differences (the table in Section 2.1). The view that "the Zeroth-Order Phase lies beyond the limit of superposition in all directions" and the view that "the position basis loses its meaning in that limit" are each additional hypotheses of this essay. The relation between this limit and the state this essay calls "undifferentiated" is a subject of examination under these hypotheses.

**(7) The rank is not the dimension of spacetime itself.** In the model of (1), when the state is a superposition $\lvert\psi\rangle=\sum_j c_j\lvert p_j\rangle$ of simultaneous eigenstates $\lvert p_j\rangle$ of the four generators (with $p_j$ the vector of eigenvalues), $F$ is four times the covariance of $p_j$ with weights $\lvert c_j\rvert^2$, and its rank equals the dimension of the affine space spanned by the $p_j$ with $c_j\ne0$. For example, for a free particle in a box with periodic boundaries, the standing wave $\psi\propto\cos(\mathbf k\cdot\mathbf x)$, an equal-weight superposition of states with momenta $\pm\mathbf k$, has equal energies for the two states, so

$$
F_{\mu\nu}=\Delta_\mu\Delta_\nu,\qquad \Delta=(0,\,2\mathbf k)
$$

and the rank is 1. Translations in the time direction and in the two spatial directions perpendicular to $\mathbf k$ change only the global phase. Even though spacetime remains four-dimensional, only one direction can be distinguished in this state. What lowers the rank is that the state does not change under the chosen translations, not symmetry in general. An isotropic Gaussian wave packet $\psi\propto\exp\left(-\lvert\mathbf x-\mathbf x_0\rvert^2/(4\sigma^2)\right)$ is symmetric under rotations about its center, but the state changes under translation in any direction, so $F=\sigma^{-2}I_3$ for the three spatial directions and the rank is 3. The simplest example is a uniform state. A uniform state normalized in a box with periodic boundaries (an eigenstate with zero momentum and zero energy) changes only by a global phase under translations in any direction, so $F=0$ and the rank is 0. Spacetime is still four-dimensional.

Thus the rank counts the directions that can be distinguished under the chosen translations in the chosen family of states; it is not the dimension of spacetime itself. A low rank for the state of a single object shows only that the object does not respond to translations in some direction. This is why the phase is determined with families of states that represent records the observer can use to read times and distances (Section 2.1 (1)). An example that computes, in a finite-dimensional model, whether the rank recovers when records are added is given in Section 3.2. Even if the standing wave above has rank 1, if the observer can distinguish the remaining directions with other records, $d_O$ for that observer is not 1, and the state is not placed in the Dimension-Reduction Phase. Even if a uniform state has rank 0, it is not the Zeroth-Order Phase if the observer can assign times and distances with other records ([Main text, Section 4.3](zerothOrderPhase.en.html)).

### 3.2 A Model That Specifies the Observer's Records: Does the Rank Recover When Records Are Added?

Section 2.1 (1) specified that the phase is determined with families of states that represent records the observer can use to read times and distances. This section computes, in a finite-dimensional model that specifies the usable and unusable degrees of freedom, the reference frames, the allowed operations, and the compared parameters, whether the rank recovers when records are added. The conclusions are limited to the records and operations allowed in this model. Saying anything about all of the observer's means requires separate grounds that the model exhausts those means. We set $\hbar=1$.

| Item | How it is specified in this model |
|---|---|
| Object S | A particle on a ring with periodic boundaries, in the standing wave $\psi_S=(\lvert k\rangle+\lvert{-k}\rangle)/\sqrt2$, an equal-weight superposition of the momentum eigenstates $\lvert\pm k\rangle$. The Hamiltonian is $H_S=P^2/2$ |
| Clock | A qubit with Hamiltonian $H_C=\omega\lvert1\rangle\langle1\rvert$ ($\lvert0\rangle$ is the ground state and $\lvert1\rangle$ the excited state; this differs from $\omega\sigma_z/2$ only by a constant and does not change the results), initially in $\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2$ |
| Parameters | Time translation (generated by the sum $H$ of the Hamiltonians of all systems) and spatial translation (generated by $P$). In cases B and C, the relative time between clocks is also used |
| Available observables $\mathcal A_O$ and unusable degrees of freedom | Specified case by case |

**Case A: symmetry of the object.** If $\mathcal A_O$ is limited to the observables of S, the two states forming $\psi_S$ have equal energies (Section 3.1 (7)), so $F=\operatorname{diag}(0,\,4k^2)$ for time translation $t$ and spatial translation $x$, and the rank is 1. Adding one clock and taking $\mathcal A_O$ to be all observables of S and the clock, the state $\psi_S\otimes\lvert+\rangle$ gives

$$
F=\operatorname{diag}\!\left(\omega^2,\ 4k^2\right)
$$

and the rank recovers to 2. The zero sensitivity in the time direction came from the object S being stationary, and it can be distinguished once the record of a clock is added. For this observer, the state is not in the Dimension-Reduction Phase.

**Case B: no external reference frame.** Suppose the observer has no correlation with an external clock and can use only observables invariant under global time translation $e^{-itH}$. The absence of a shared reference frame restricts the available operations and acts like a superselection rule [10]. Then every observable $a$ in $\mathcal A_O$ commutes with $H$, and $\operatorname{Tr}(\rho(t)\,a)=\operatorname{Tr}(\rho\,a)$, so $F_{tt}=0$ for any state. However many clocks are added within this model, as long as they move together under the global translation, the direction $t$ does not recover.

This setting assumes neither that the total state is an energy eigenstate nor that it satisfies a constraint $\hat H\Psi=0$. It is a restriction of operations due to having no external reference frame, and amounts to using the state averaged over global time translations (its block-diagonal part with respect to the eigenspaces of the total energy) [10]. The case in which the total state lies in a single eigenspace of the total energy is the original setting of Page and Wootters [9]; there is then a single block, and the information about relative time lies only within that eigenspace. In models approximated by a single constraint, there is a formal analogy with a Page–Wootters-type constraint on the whole. However, the whole set of local constraints of general relativity (the Hamiltonian and momentum constraints at each point) is not identified with an eigenspace of the total energy of an ordinary quantum system (there are also problems of the physical inner product and of continuous spectra; Section 5.5). The example below is a case in which the initial state spans several blocks.

Still, $t$ is not a parameter assigned from records the observer can read. What the observer can assign is the relative time between records. Take two clocks ($C_1$, $C_2$, both in $\lvert+\rangle$) and the family of states in which only $C_1$ is advanced by time $\tau$. The restriction to observables invariant under global translation becomes the projection onto blocks by total excitation number. The information about $\tau$ remains in the block with one excitation (weight $1/2$), and the pure state $(\lvert01\rangle+e^{-i\omega\tau}\lvert10\rangle)/\sqrt2$ in it has QFI $\omega^2$. Hence

$$
F_{\tau\tau}=\frac{\omega^2}{2}
$$

and half of the value with an external reference frame ($\omega^2$) remains. The relative time can be distinguished (this corresponds to the relational encoding of [10]). Therefore, rank 0 with respect to an external parameter does not mean that the observer cannot construct distinctions of time. The phase is determined with parameters the observer assigns from records (here $\tau$). This is also a finite-dimensional computed example of the Page–Wootters analogy of Section 3.1 (4).

**Case C: relative records are lost to unusable degrees of freedom.** In case B, suppose $C_1$ interacts with an environment E, and E is outside $\mathcal A_O$. Removing E by a partial trace lowers the phase coherence of $C_1$ (the length of the Bloch vector in the equatorial plane) to $r$ ($0\le r\le1$). The state in the block with one excitation becomes a qubit whose Bloch vector of length $r$ rotates by the angle $\omega\tau$, and

$$
F_{\tau\tau}=\frac{r^2\omega^2}{2}
$$

While $r>0$, the sensitivity only weakens and the rank stays 1, corresponding to the Spacetime-Limit Phase, in which the compared states become harder to distinguish. The rank becomes 0 only when $r=0$. For $0\le r<1$ the rank of the density matrix (the state rank) is constant at 4; what changes at $r=0$ is not the state rank but the rank of the QFI.

Whether the direction $\tau$ recovers at $r=0$ depends on the order of operations and on what the observer can use. Here the order is: (1) prepare the clocks; (2) write the time difference $\tau$ into $C_1$; (3) $C_1$ interacts with E and completely loses phase coherence; (4) afterwards, add a clock in a state independent of $\tau$ and measure with observables invariant under global translation. In this order, both the state of $C_1$ and the state of the added clock are independent of $\tau$, so the direction $\tau$ does not recover. On the other hand, if before (3) an operation that exchanges the states of $C_1$ and a clock $C_3$ with the same Hamiltonian (SWAP, which commutes with the total Hamiltonian and needs no external reference frame) is allowed, the information about $\tau$ moves to $C_3$, and $F_{\tau\tau}=\omega^2/2$ remains even after $C_1$ loses phase coherence. Moreover, even when the state of $C_1$ alone no longer depends on $\tau$, the information about $\tau$ can remain in the correlations between $C_1$ and E. For example, when the dephasing occurs as

$$
\lvert\Psi(\tau)\rangle=\frac{\lvert0\rangle\lvert e_0\rangle+e^{-i\omega\tau}\lvert1\rangle\lvert e_1\rangle}{\sqrt2},\qquad \langle e_0\vert e_1\rangle=0
$$

(with $\lvert e_0\rangle$, $\lvert e_1\rangle$ states of E), neither $C_1$ alone nor E alone depends on $\tau$, but the phase remains in the joint state. Therefore, in this case, the direction can be said not to recover only under the order above and the premise that neither E nor the joint system of $C_1$ and E is included in $\mathcal A_O$. It has not been shown that no observer can recover it.

| Case | Does the rank recover when records are added? | Reading in this model |
|---|---|---|
| A | Yes (rank 2 with a clock added) | Due to the symmetry of the object; not the Dimension-Reduction Phase |
| B | The external $t$ does not recover; the relative time $\tau$ can be distinguished | $t$ is not a parameter the observer assigns. Distinctions of time can be constructed relatively, so it is not the Zeroth-Order Phase |
| C | For $r>0$ the rank has not dropped. At $r=0$, adding a clock independent of $\tau$ after the loss of phase coherence does not recover it (it may recover if operations that move the information to another clock before the loss, or the joint system with E, can be used) | $r>0$ is the Spacetime-Limit Phase; $r=0$ is a reduction of the direction $\tau$ within the order and $\mathcal A_O$ specified in this model |

This model shows three things. (i) Whether a drop in rank comes from the symmetry of the object or from the structure of the observer's records can be separated by computing with added records. (ii) Zero sensitivity to an external parameter and zero sensitivity to a relative parameter the observer assigns are different. (iii) A reduction on the observer's side occurs in this model when the information of the relative records is completely lost from the records the observer can use, under the specified order and $\mathcal A_O$; before that, there is only decreased sensitivity (the Spacetime-Limit Phase). It is a model of the time direction only, and shows neither the reduction of four directions nor the loss of all means of observation that distinguish spacetime differences.

### 3.3 A Kinematic Model of the Connection Through Superposition of Records (Hypothesis)

[Main text, Section 4.3](zerothOrderPhase.en.html) took as an additional hypothesis of this essay that the Zeroth-Order Phase lies beyond the limit where superposition extends over all independent spacetime directions. This section gives a kinematic model that applies this hypothesis not to an object but to the state of the observer's records (clocks and rulers). One can build a model in which varying the state of the records with an approach parameter lowers the sensitivity to relative shifts until it vanishes in some direction. In the example with two clocks, this process can be computed concretely. However, that the records cannot be rebuilt by allowed operations (outside the conditions of (3)), the extension to four directions, the loss of all means of observation that distinguish spacetime differences, and the correspondence with CCC remain as tasks to be shown separately. This section does not derive a connection to the Zeroth-Order Phase.

**(1) Example with two clocks.** As in case B of Section 3.2, there is no external reference frame, and the available observables are those invariant under global time translation. Put clocks $C_1$ and $C_2$ in the same state $\cos\theta\lvert0\rangle+\sin\theta\lvert1\rangle$ ($0\le\theta\le\pi/4$), and advance only $C_1$ by time $\tau$. $\theta$ corresponds to the approach parameter $\lambda$ of Section 2.1 (1). As $\theta\to0$, each clock approaches an energy eigenstate, that is, a stopped clock whose reading is completely spread. Restricting to the blocks by total excitation number, the information about $\tau$ remains in the block with one excitation (weight $2\cos^2\theta\sin^2\theta$), and

$$
F_{\tau\tau}(\theta)=\frac{\omega^2}{2}\sin^2 2\theta
$$

At $\theta=\pi/4$ this returns to $\omega^2/2$ of Section 3.2; as $\theta$ decreases the sensitivity decreases continuously, and at $\theta=0$ it is exactly 0. Because the restriction to the available observables is a parameter-independent operation and does not increase the QFI [6, 7], the bound $F_{\tau\tau}\le4\operatorname{Var}(H_{C_1})=\omega^2\sin^2 2\theta$ also holds.

**(2) Meaning of the family of states.** Changing $\theta$ changes the prepared state of the records; it is not time evolution. What this family of states shows is that changing the prepared state removes the sensitivity to relative shifts applied afterwards. It does not show a process in which existing information about a time difference disappears. Because unitary changes independent of $\tau$ preserve the inner products of states and the QFI, losing the information in the records requires something like the interaction with unusable degrees of freedom of case C of Section 3.2. At the endpoint of this family of states, the dependence on the specified relative shift is gone. The physical process leading to that endpoint, and where the information of earlier records goes, are not treated in this model. An example that computes the relaxation of clocks to thermal equilibrium as time evolution is given in Section 4.1.

**(3) Conditions under which a clock cannot be rebuilt at the endpoint.** That each record is an eigenstate does not by itself mean that a clock cannot be rebuilt. If clocks of the same frequency are put in $\lvert1\rangle\lvert0\rangle$, both are energy eigenstates, but an operation that conserves the total energy can change the state to $(\lvert10\rangle+\lvert01\rangle)/\sqrt2$. This operation commutes with the total Hamiltonian and needs no external reference frame. Advancing $C_1$ by $\tau$ afterwards gives $F_{\tau\tau}=\omega^2$, and a clock has been rebuilt. This is because $\lvert10\rangle$ and $\lvert01\rangle$ have equal energies and the eigenspace of the total Hamiltonian is degenerate.

In this model, a clock can be said not to be rebuildable under the following two conditions.

1. The total state of the records and of the auxiliary systems used for operations lies in a nondegenerate eigenspace of the total Hamiltonian (for example, as with $\lvert00\rangle$ at $\theta=0$, everything including the auxiliary systems is in the ground state, and the total ground state is nondegenerate).
2. The allowed operations are limited to unitaries commuting with the total Hamiltonian (energy-conserving operations) and discarding auxiliary systems, with no external energy source or reference frame. If general channels covariant under time translation are allowed, states such as $(\lvert10\rangle+\lvert01\rangle)/\sqrt2$ can be newly prepared, and this conclusion fails (Section 4.1 (3)).

Then the allowed operations keep the state within the same one-dimensional eigenspace, so the state changes only by a global phase. Because the Hamiltonian of each clock also commutes with the total Hamiltonian, this state is also an eigenstate for each clock, and whatever relative shift is applied, the state is exactly the same even for finite shifts. This is a conclusion within the records, auxiliary systems, and operations specified in this model, and does not show that all of the observer's means have been exhausted (Section 3.2).

**(4) Extension to four directions (a hypothetical construction).** The following table is the construction one would want to realize when extending to four directions; it is not a computed result.

| Stage of approach | State of the observer's records (assumed) | Phase (table in Section 2.1) |
|---|---|---|
| Beginning | The QFI matrix for relative shifts is positive definite, and its eigenvalues decrease | Spacetime-Limit Phase |
| Sensitivity exactly zero in some direction | The state of the records becomes an eigenstate of the generator of that direction | Dimension-Reduction Phase |
| Sensitivity zero in all directions, and the conditions of (3) are satisfied | The whole of the records and auxiliary systems lies in a nondegenerate eigenspace | Within this model, there is no material for constructing spacetime relations from records (a candidate for the Zeroth-Order Phase) |

Even if the variance in each direction is positive, the rank is not 4 if changes by different generators amount to the same change of the state. The condition of the first row was therefore taken to be that the QFI matrix is positive definite. If the stages at which the sensitivity becomes exactly zero differ from direction to direction, the Dimension-Reduction Phase is passed through in steps; but if all sensitivities vanish only simultaneously in the limit, the rank stays 4 throughout. Which happens depends on how the model is set up, and it cannot be derived that the Dimension-Reduction Phase is necessarily passed through. An example in which clocks and rulers relax thermally and only the effective dimension decreases in steps while the rank stays 4 is given in Section 4.2. In spatial directions that extend without bound, eigenstates of momentum cannot be normalized, so zero sensitivity in that direction appears only as a limit (Section 3.1 (2)).

**(5) On CCC.** That a theory is conformally invariant does not mean that individual states are eigenstates of the dilation generator. The dilation generator is different from the generators of the four translations of (4), and the loss of scale cannot be counted as a drop of rank in one direction of the four-direction QFI matrix. Moreover, even if the QFI with respect to a chosen continuous parameter is zero, discrete distinctions, causal order, and procedures using other records may remain (Section 2.1). For this reason, conditions for judging that there are no means of observation that distinguish spacetime differences on the CCC connecting boundary cannot be built from the models of this section. What can be written is only a direction for examination: to study distinguishability for relative records invariant under conformal transformations, for a specified family of states and observation conditions ([Appendix 3](appendix3.en.html)). A toy model that follows this direction and computes the degree of distinction for pairs of global scale, pairs of relative scale, and pairs of order-dependent processes is given in Appendix 3, Section 4.2.

## 4. Dynamical Models: Processes in Which Records Relax

The models of this section compute, as time evolution, processes in which the observer's records (clocks and rulers) interact with an environment and relax. They are examples of processes leading to the endpoints of the families of states of Section 3. Every model assumes an independent environment for each record, weak coupling, and a Markovian approximation, and the environment is not included in the observables available to the observer (Section 4.1 (5)). The number of compared parameters is $m$, and the association with phases within a model follows the convention of Section 2.1. The relaxation time $t$ is a time outside the model; its reading in general relativity is given in Section 5.5.

| Section | Compared parameters (number $m$) | Available observables | Process | What it shows | What it does not show |
|---|---|---|---|---|---|
| 4.1 | Relative time (1) | Observables invariant under global time translation | Relaxation to thermal equilibrium | The sensitivity does not become 0 at finite times; in thermal equilibrium at a common temperature, a clock cannot be rebuilt by thermal operations | Loss of distinction in the time direction in general; the arrow of time; spatial directions |
| 4.2 | Relative time and three positions (4) | Observables invariant under global time and spatial translations | Relaxation by an assumed generator (with rates differing by direction; a mathematical example including values outside the conditions of the approximation) | The rank stays 4 at finite times, and only $D_{\mathrm{eff}}$ under fixed measurement conditions decreases in steps | The distinction between time and space (because the rulers are two-level) |
| 4.3 | Relative time and position (2) | Observables invariant under total energy and momentum | Loss of phase coherence in the energy or the momentum basis | With multilevel rulers the two directions become independent; an example in which only the time direction is lost in the limit | Relativistic dispersion relations; three-dimensional space; boosts |

### 4.1 Records Relaxing to Thermal Equilibrium: An Example of Dynamics in the Time Direction

The family of states of Section 3.3 lined up differences in the prepared states; it was not time evolution. This section computes, as time evolution in the same model of two clocks, the process in which the clocks exchange heat with an environment and approach thermal equilibrium. There is no external reference frame, and the available observables are the same as in case B of Section 3.2. We set $\hbar=k_B=1$.

**(1) Model.** Each clock is weakly coupled to its own independent environment at temperature $T$. The clocks do not interact with each other. The environment is not included in the observables available to the observer. The change of the clock states is described by the standard Markovian master equation for thermal relaxation (the Lindblad equation). The level populations approach their equilibrium values at the rate $\Gamma_1=\gamma(2\bar n+1)$, and the phase coherence between the two levels is lost at the rate $\Gamma_2=\Gamma_1/2$, where $\gamma$ is the coupling strength and $\bar n=1/(e^{\omega/T}-1)$ is the mean excitation number of the environment. Weak coupling and the secular approximation (valid for $\gamma\ll\omega$) are assumed, and the frequency shift due to the environment is absorbed into $\omega$. Under these conditions, the change commutes with the time translation of each clock, and it does not matter whether the relaxation or the advance of a clock by $\tau$ comes first. When the two clocks couple to a common environment (collective dissipation), the change does not commute with the translation of one clock alone, and the formulas below cannot be used. The relaxation time $t$ is a parameter describing the change of state from outside the model; like $\lambda$ of Section 2.1 (1), it is not a clock the observer reads.

**(2) How the sensitivity decreases.** If only $C_1$ relaxes and $C_2$ stays in $\lvert+\rangle$,

$$
F_{\tau\tau}(t)=\frac{\omega^2}{2}\,e^{-2\Gamma_2 t}
$$

This is case C of Section 3.2 with $r$ replaced by $e^{-\Gamma_2 t}$, and it does not depend on the change of populations. When both clocks relax, with the population of the upper level $p(t)=p_{\mathrm{eq}}+(\tfrac12-p_{\mathrm{eq}})e^{-\Gamma_1 t}$ ($p_{\mathrm{eq}}=\bar n/(2\bar n+1)$),

$$
F_{\tau\tau}(t)=\frac{\omega^2\,e^{-4\Gamma_2 t}}{8\,p(t)\bigl(1-p(t)\bigr)}
$$

Both formulas agreed with the QFI obtained by direct time integration of the master equation ($\omega=0.7$, $\gamma=0.4$, $\bar n=0$ and $0.5$, $t=1,3,10$). These numbers confirm the agreement between the analytic formulas and numerical integration under the assumed generator; they do not confirm the validity of the approximation. With these values $\gamma\ll\omega$ is not well satisfied, and applying the model to a physical system requires the relaxation rates $\Gamma_1$, $\Gamma_2$ to be much smaller than $\omega$. In both cases, $F_{\tau\tau}>0$ at finite times. The sensitivity weakens exponentially and becomes 0 only in the limit $t\to\infty$. This is an example of a path in which the sensitivity is lost smoothly rather than becoming exactly zero (the table in Section 2.1), and at finite times the classification of phases places it in the Spacetime-Limit Phase. However, even with $F_{\tau\tau}>0$, if the observer's resources are finite, the states may in practice be indistinguishable (Section 2.1 (4)).

**(3) In thermal equilibrium, a clock cannot be rebuilt.** At the endpoint of the relaxation, all systems available to the observer (the clocks) are in thermal equilibrium at the same temperature, and the state is a function of the total Hamiltonian $H$, $\rho\propto e^{-H/T}$. Because the clocks do not interact, the state of each clock is also a function of its own Hamiltonian, and the state does not change under global time translation or under the time translation of a single clock. Therefore, pairs obtained by applying the specified relative time translation or a global time translation to this clock state have equal outcome distributions, and the degree of distinction (Appendix 3, Section 4) for these pairs is 0. This does not show $\Delta_O=0$ for the time direction in general. Even in thermal equilibrium, two-time correlations and responses are not trivial, and depending on the range of procedures that allow interventions and records, time differences may be accessible.

Moreover, a state being a function of $H$ is equivalent to its being unchanged by every unitary commuting with $H$ (because it is proportional to the identity within each eigenspace of $H$). If the allowed operations are limited to energy-conserving unitaries together with adding auxiliary systems in thermal equilibrium at the same temperature and later discarding them, with no external energy source or reference frame, a clock cannot be rebuilt. This range of operations corresponds to the one used in the theory that treats states out of thermal equilibrium as resources (thermal operations) [11]. If general channels covariant under time translation are allowed, eigenstates of the total Hamiltonian such as $(\lvert10\rangle+\lvert01\rangle)/\sqrt2$ can be newly prepared, and this conclusion fails. If the clocks interact with each other, the global thermal state no longer commutes with the Hamiltonian of each clock, and sensitivity to the translation of a single clock may remain. Condition 1 of Section 3.3 (3) (a nondegenerate eigenspace) is a special case of this "state that is a function of the total Hamiltonian". In the example of $\lvert10\rangle$ in Section 3.3 (3), a clock could be rebuilt because the state was not proportional to the identity within the degenerate eigenspace.

The situation differs when the temperatures differ. When two clocks of equal frequency are in thermal equilibrium at different temperatures (inverse temperatures $1$ and $3$, $\omega=0.7$), the populations of the degenerate $\lvert01\rangle$ and $\lvert10\rangle$ are unequal, so an energy-conserving operation that exchanges them halfway yields a clock with $F_{\tau\tau}\approx0.066$. At equal temperatures, neither that operation nor 20 randomly chosen energy-conserving unitaries changed the state (numerical computation). What acts as the resource for making a clock in this model is the imbalance of populations within a degenerate eigenspace, of which a temperature difference is one example. For two clocks without auxiliary systems, if the frequencies differ there is no degeneracy, and even with different temperatures a clock cannot be made by energy-conserving unitaries. It is known that asymmetry (coherence) with respect to time translation is not determined by free energy alone [12], and the result here is not regarded as a general correspondence with free energy.

**(4) Relation to Appendix 3.** [Appendix 3](appendix3.en.html) took the future side of the previous universe to be the side on which free energy is exhausted and the standards for dimensionful quantities are progressively lost. This model is a small example of that side, restricted to the time direction. During relaxation, the sensitivity of existing clocks weakens but is not 0. In the limit in which all systems available to the observer reach thermal equilibrium at the same temperature, the degree of distinction for the pairs of time translations encoded in the clock states becomes 0, and within the operations of (3) no new clock can be made either. While states out of thermal equilibrium remain, new clocks may be made. The correspondence with the "exhaustion of free energy" of Appendix 3 is an analogy, and what this model shows extends only to the conclusion for the case in which thermal equilibrium at a common temperature is reached.

**(5) What this model does not show.**

- The Markovian master equation is an approximation that assumes a large environment, weak coupling, the secular approximation ($\gamma\ll\omega$), and an independent environment for each clock. In a finite closed system, the state may eventually return close to the initial state, so exact thermal equilibrium appears only as a limit.
- The environment is not included in the observables available to the observer. The change of the clocks and environment together is unitary, and the information about $\tau$ may remain in the correlations between the clocks and the environment (case C of Section 3.2). If the environment can also be used, the conclusion may change.
- The relaxation time $t$ is a time outside the model, a description at a different level from the setting in which the observer has no external reference frame.
- What becomes 0 is invariance under time translation. The distinction of the direction of time (past and future) is a separate question; the value of the QFI alone does not fix the thermodynamic arrow of time. This is a separate question from whether the states for $\tau$ and $-\tau$ can be distinguished. Under thermal relaxation, the entropy of the system does not necessarily increase monotonically (for example, relaxation at zero temperature from a pure state to the pure ground state). Monotone quantities include, under suitable conditions, the decrease of the relative entropy to the thermal state. This model does not discuss the connection with the arrow of time.
- Only the time direction is treated; spatial directions and causal order are not. Whether distinctions of causal order remain in thermal equilibrium must be examined separately.
- The temperature of the environment is taken as constant. Whether the universe reaches thermal equilibrium at a single temperature while expanding, and how to treat the temperature of cosmological horizons, are not treated in this model.

### 4.2 Extension to Four Relative Shifts: A Model in Which Clocks and Rulers Relax

The model of Section 4.1 is extended to three spatial directions. In addition to two clocks, two rulers are placed in each spatial direction. A ruler is a distinguishable particle on a periodic boundary of length $L$ in that direction, put in the state $\lvert+\rangle$, an equal-weight superposition of the two states with momenta $0$ and $k=2\pi n/L$ ($n$ an integer; kinetic energy $k^2/2m$). Positional shifts have period $L/n$. The compared parameters are the relative shifts that move only the first record of each pair: the time $\tau$ (generated by the Hamiltonian of the first clock) and the positions $\xi_x,\xi_y,\xi_z$ in each direction (generated by the momentum of the first ruler). The four generators commute with each other. Because the rulers are truncated to two levels, the kinetic energy of a ruler is proportional to its momentum, and time and spatial translations of a ruler cannot be distinguished. What this model counts is therefore the independent relative shifts of four records (one clock and three rulers); it does not test the distinction between time and space or the relation between energy and momentum. An example that distinguishes time shifts and position shifts with multilevel rulers is given in Section 4.3. The same result would be obtained with four clocks. There is no external reference frame, and the available observables are those invariant under both global time translation and global spatial translations (the projection onto blocks for each combination of the total energy and the total momentum in each direction).

Each record undergoes the same thermal relaxation as in Section 4.1 (temperature $0$, $\omega=0.7$, $k=m=1$), with the rate $\Gamma_2$ at which phase coherence is lost varied by direction (time $0.02$, x $0.1$, y $0.5$, z $2.5$; the population relaxation rate is $2\Gamma_2$). For the rulers, losing phase coherence in the momentum basis loses positional information. Each ruler is coupled to an independent environment that can take up momentum. This assumption is needed because in an isolated system the total momentum is conserved, and the thermal state depends not only on energy but also on momentum. The ratios of the rates between directions were chosen arbitrarily, and the values in the table and the way $D_{\mathrm{eff}}$ decreases depend on this choice. The conclusion about the rank does not depend on the choice of rates. The level spacing of the rulers is $k^2/2m=0.5$, and the rate in the z direction ($\Gamma_2=2.5$, $\Gamma_1=5$) is much larger, far outside the conditions of weak coupling and the secular approximation. This section is therefore to be read not as an example of physical weak-coupling thermal relaxation but as a mathematical example of an assumed Lindblad-type generator (GKSL form).

**(1) Results.** Computing the 4×4 QFI matrix numerically for the state of eight qubits (256 dimensions), each component agreed with the formula of Section 4.1 (with $\omega$ replaced by $k$ for the rulers). Because the state is a product and the blocks separate by the excitation number of each pair, the matrix is diagonal by structure. At temperature $0$, each component reduces to $g^2p/\bigl(2(1-p)\bigr)$ ($p=\frac12e^{-2\Gamma_2t}$, with $g$ equal to $\omega$ or $k$). The effective dimension $D_{\mathrm{eff}}$ under fixed measurement conditions was computed with the resolution chosen for each direction so that initially $N\kappa_i$ is $100$ in every direction; the values of $D_{\mathrm{eff}}$ depend on this choice of resolution. The small values in the table are from the analytic formula.

| Time $t$ | $F_{\tau\tau}$ | $F_{xx}$ | $F_{yy}$ | $F_{zz}$ | $D_{\mathrm{eff}}$ |
|---|---|---|---|---|---|
| $0$ | $0.245$ | $0.5$ | $0.5$ | $0.5$ | $3.96$ |
| $1$ | $0.227$ | $0.347$ | $0.113$ | $0.0017$ | $3.19$ |
| $3$ | $0.195$ | $0.189$ | $0.013$ | $7.7\times10^{-8}$ | $2.68$ |
| $10$ | $0.124$ | $0.036$ | $1.1\times10^{-5}$ | $4.8\times10^{-23}$ | $1.86$ |
| $30$ | $0.043$ | $6.2\times10^{-4}$ | $2.3\times10^{-14}$ | $1.8\times10^{-66}$ | $1.06$ |
| $100$ | $0.0023$ | $5.2\times10^{-10}$ | $9.3\times10^{-45}$ | about $10^{-218}$ | $0.48$ |

**(2) How to read it.**

- At finite times, all four components are positive and the rank stays 4. In terms of the classification of phases, the state remains in the Spacetime-Limit Phase, and the rank drops exactly only in the limit $t\to\infty$. In that limit the rank drops from 4 to 0 at once, without passing through intermediate values. However, components such as $F_{zz}\approx10^{-218}$ cannot be read in practice.
- On the other hand, $D_{\mathrm{eff}}$ under fixed measurement conditions loses contributions starting from the direction that relaxes fastest (through $t=30$; at $t=100$ the contribution of the clock has also dropped to about $0.48$), decreasing from $3.96$ to $0.48$. Seen under fixed measurement conditions, it looks like a dimensional reduction in which directions are lost one by one, but the rank has not dropped. This is an example, in time evolution, of the difference in Section 2.1 between $D_{\mathrm{eff}}$ (readability under those measurement conditions) and the rank $d_O$ (strict distinction).
- In this model, because the four components are all strictly positive at finite times (the formula of Section 4.1), the rank does not drop at finite times and the Dimension-Reduction Phase is not passed through. This conclusion does not follow merely from the state being analytic in time. When the rates change with time, or in non-Markovian or other models, the rank may drop at finite times. Examples in which the rank in some direction drops exactly at a finite time include processes that completely destroy the phase coherence in that direction in a finite time (such as projective measurements by the environment) and records that carry no distinction in that direction from the start. This is a concrete example of "it cannot be derived that the Dimension-Reduction Phase is necessarily passed through" in Section 3.3 (4).

**(3) Endpoint.** At the endpoint at temperature $0$, all records are in their ground states (clocks in the lower level, rulers with momentum $0$), the state does not change under any time or spatial translation, and the QFI matrix is 0 (also 0 numerically). This is a conclusion for the pairs of relative shifts encoded in the records (Section 4.1 (3)). Even in thermal equilibrium at positive temperature, the state of the rulers is diagonal in the momentum basis and does not change under spatial translation. Under the assumption that each ruler couples to an environment that takes up momentum, the total state is a function of the total Hamiltonian. Therefore, with the set of operations consisting of unitaries that conserve total energy and momentum and auxiliary systems at the same temperature, neither clocks nor rulers can be rebuilt, for the same reason as in Section 4.1 (3). If auxiliary systems out of thermal equilibrium or temperature differences are available, clocks or rulers may be made.

**(4) What this model does not show.**

- Lorentz transformations (boosts) are not treated, because they do not commute with the generators of translations.
- Treating the relaxation of the rulers as loss of phase coherence in the momentum basis is an assumption. In continuous space, many environments destroy phase coherence in the direction of measuring position, in which case the positional record is rather preserved. The two-level truncation of this model has no position basis and cannot represent that case.
- That the thermal state does not change under spatial translation corresponds to the uniformity of a gas in thermal equilibrium, but only for independent, noninteracting particles. In an interacting gas, even if the one-particle density is uniform, information remains in the distribution of relative positions of particles (the radial distribution function).
- The records in each direction are two-level, and independent environments and rates were assumed for each direction.
- The limitations of Section 4.1 (5) (that $t$ is a time outside the model, the range of the approximation, that the environment is not usable, the arrow of time, causal order, the expanding universe) apply here as well.

### 4.3 Multilevel Rulers: A Model That Distinguishes Time Shifts from Position Shifts

With the two-level rulers of Section 4.2, time and spatial translations of a ruler could not be distinguished. This section shows that with multilevel rulers, time shifts and position shifts can be distinguished as two independent directions by rulers alone, and gives a process in which only one of the directions is lost. The model is nonrelativistic (kinetic energy $p^2/2m$), and does not treat the distinction between timelike and spacelike directions (the signature of the metric) or the extension to relativistic dispersion relations.

**(1) Model.** Two rulers (distinguishable particles on a one-dimensional periodic boundary) are placed, with no clocks. Each ruler has five levels with momenta $p\in\lbrace-2k,-k,0,k,2k\rbrace$ and kinetic energy $p^2/2m$ ($k=m=1$). Both are put in the equal-weight superposition of the five momentum states. The compared parameters are the relative time $\tau$ that moves only the first ruler (generated by the kinetic energy of the first ruler) and the relative position $\xi$ (generated by the momentum of the first ruler). There is no external reference frame, and the available observables are given by the projection onto blocks for each combination of the total energy and the total momentum (25 dimensions).

**(2) Distinguishing time and space.** Computing the 2×2 QFI matrix for different numbers of levels gives the following.

| Momenta of the ruler | Components of the QFI matrix | Rank |
|---|---|---|
| $0,\ k$ (two levels) | $F_{\tau\tau}=0.125$, $F_{\xi\xi}=0.5$, $F_{\tau\xi}=0.25$ | 1 |
| $-k,\ 0,\ k$ (three levels) | $F_{\tau\tau}=0.111$, $F_{\xi\xi}=1.333$, off-diagonal 0 | 2 |
| $-2k,\dots,2k$ (five levels) | $F_{\tau\tau}=1.4$, $F_{\xi\xi}=4$, off-diagonal 0 | 2 |

With two levels, there are only two values of momentum, so the energy can always be written as a linear function of momentum, and the rank is 1. This comes from the truncation to two levels, not from a property of the dispersion relation. The indistinguishable direction is the one in which the position shift and time shift are related by $\xi=-(k/2m)\tau$, that is, the direction in which the phase of the ruler does not change. For the levels chosen here, the rank is 2 when there are three or more values of momentum. In general, the rank is 2 if the ratio of the energy difference to the momentum difference is not constant over the pairs of states that can be compared within the blocks. In this model the two directions are independent because the relation between energy and momentum (the dispersion relation $p^2/2m$) is curved.

**(3) A process in which only one of the directions is lost.** The phase coherence of the first ruler is destroyed by two kinds of environments (Lindblad type, at a rate proportional to the square of the difference of the eigenvalues of the operator $L$ representing the dephasing, with proportionality coefficient $0.2$).

| Time $t$ | $F_{\tau\tau}$ ($L$ = energy) | $F_{\xi\xi}$ ($L$ = energy) | $F_{\tau\tau}$ ($L$ = momentum) | $F_{\xi\xi}$ ($L$ = momentum) |
|---|---|---|---|---|
| $0$ | $1.4$ | $4$ | $1.4$ | $4$ |
| $1$ | $0.785$ | $3.06$ | $0.675$ | $0.984$ |
| $3$ | $0.279$ | $2.21$ | $0.279$ | $0.269$ |
| $10$ | $0.032$ | $1.72$ | $0.054$ | $0.044$ |
| $30$ | $0.0089$ | $1.64$ | $0.00099$ | $0.00079$ |
| $\infty$ | $0$ | $1.6$ | $0$ | $0$ |

The off-diagonal components are 0 in both cases because the state and the levels are symmetric under $\pm p$; in general they need not be 0. An environment that destroys phase coherence in the energy basis randomly rotates the generator of the compared parameter $\tau$ itself (the rate at which time advances fluctuates), so it is to be expected by construction that the information about $\tau$ is lost. The same holds for $\xi$ in the momentum-basis case. This table is an example showing which direction remains when fluctuations of the compared parameter itself are introduced. In an environment that destroys phase coherence in the energy basis, only the phases between states of different energies are lost, and the phases between $+p$ and $-p$ (equal energies) remain. At the endpoint only the time direction becomes 0, the spatial direction remains, and the rank is 1. What remains at the endpoint is a superposition of pairs in which the two rulers are entangled with momenta $\pm a$ and $\mp a$, a component resembling a standing wave (Section 3.1 (7)) in the relative motion. In an environment that destroys phase coherence in the momentum basis, both directions become 0 at the endpoint.

At finite times, the rank stays 2 in both cases (as in Section 4.2), and it drops only at the endpoint. What appears at finite times is the decrease of $D_{\mathrm{eff}}$ under fixed measurement conditions. When phase coherence is lost in the energy basis and the resolution is chosen so that initially $N\kappa_i$ is $100$ in each direction, $D_{\mathrm{eff}}$ is $1.98,\ 1.97,\ 1.93,\ 1.68,\ 1.37,\ 0.98$ at $t=0,1,3,10,30$ and at the endpoint. The endpoint is a state in which, with the two directions distinguished, only the time direction has been lost, and it corresponds to the Dimension-Reduction Phase as a limit. Under the definition of this appendix, which requires the rank to be constant over a range for a phase, it can be called a phase only as an idealization of this limit.

**(4) What this model does not show.** Space is one-dimensional, far from the claim about four directions. Because the momenta are truncated to five levels on a lattice, invariance under boosts cannot be tested within the model. Only one state and one proportionality coefficient ($0.2$) were computed. The concrete environment that destroys phase coherence in the energy basis is not identified. The environment is not included in the observables available to the observer (Section 4.1 (5)). Accelerated observers are not treated. For Lorentz transformations, see the item on how to read Section 2.1.

## 5. Premises for Reading the Equations and Physical Concepts

### 5.1 Treatment of Time and Energy

In standard quantum mechanics, time is treated as an external parameter. The position–momentum relation and the time–energy relation are not treated as having the same operator structure. The time–energy relation is used as an estimation limit, namely how precisely elapsed time can be estimated from a change of state ([Appendix 2, Section 5.2](appendix2.en.html)), and no universal minimum time is derived from it.

### 5.2 Treatment of the Planck Scale

The Planck length and the Planck time are the natural scales at which quantum theory and gravity must be considered together. The argument comparing the energy needed for localization with the gravitational radius is used as a heuristic estimate, not as a proof of a minimum length.

### 5.3 Treatment of Partial Traces and Toy Models

A partial trace is an operation that removes an unobservable subsystem from the observational description; it does not physically erase the information of the total system. In the two-level model of Appendix 2 ($0\le\theta\le\pi/2$), the trace distance of the subsystem is $T=\cos\theta$ and approaches zero as $\theta\to\pi/2$, while the two states of the total system remain orthogonal. What this model directly shows is local indistinguishability in the Spacetime-Limit Phase, not dimensional reduction.

### 5.4 Extension to Five Limit Regions

Adding infinitesimal time division ($\Delta t\to0$) to the four limits of the main text as an independent line of inquiry allows five limit regions to be compared. The suppression of state transitions by the quantum Zeno effect is distinguished from indistinguishability of states. The correspondence between each region and the three phases is given in Section 9 of Appendix 2.

### 5.5 Kinematics and Dynamics in General Relativity

The distinction between Section 3 (kinematics) and Section 4 (dynamics) rests on a view in a fixed background spacetime that uses a time $t$ outside the model. In general relativity, too, structures such as the configuration space and phase space can be distinguished from constraints and equations of motion, and the distinction between kinematics and dynamics does not disappear. However, the way this appendix divides them, which presupposes a fixed background and an external time, needs reexamination. The spacetime metric, which in special relativity was a given stage, becomes a field that changes through interaction with matter (the Einstein equations) and an object of dynamics. Correspondingly, the theory is invariant under diffeomorphisms (transformations corresponding to changes of coordinates), and in the classical canonical formulation the Hamiltonian constraint and the momentum constraint appear at each point. In the spatially closed case there is no boundary term, the canonical Hamiltonian is a sum of constraints, and time evolution is the same as a gauge transformation by diffeomorphisms. Upon quantization, the constraints become conditions on states (such as the Wheeler–DeWitt equation $\hat H\Psi=0$; Section 3.1 (4)), but their treatment has open problems such as the physical inner product. In the asymptotically flat case, a boundary term (the ADM energy) that generates time translation at infinity remains, but local reparametrizations of time are still gauge transformations. That the metric is an object of dynamics and that time evolution becomes a gauge transformation are both related to the structure of a theory without a background spacetime, but the metric being an object of dynamics cannot be derived from diffeomorphism invariance alone. In this setting, physical change is expressed not as change with respect to an external time but as a relation between one system and others (partial and complete observables [13]; the conditional states of Page and Wootters [9]). The Page–Wootters construction presupposes an ideal clock, and that presupposition itself has open problems.

From this viewpoint, it is more consistent to replace $t$ in Section 4 by the reading of another clock available to the observer, and the relaxation process is reread as a relation among records, namely the sequence of states of the records for each reading of that clock. The use of the relative time rather than an external time in case B of Section 3.2 follows this reading. However, using the external $t$ as a local approximation in a fixed background is legitimate, and the calculations of this appendix rely on that approximation. When $t$ is replaced by a clock reading, the clock itself fluctuates through interaction with its environment, so its reading need not be a good time variable, and the interaction between the clock and the system can also disturb the change of the system. This must be treated in a separate model.

In settings that combine quantum theory with these ideas, the effect in which a clock follows a superposition of paths with different proper times and the interference is weakened by the clock's record has been discussed [15]. There is also a framework of quantum correlations that does not presuppose a definite causal order [14]; the latter is a formal framework, not derived from quantum gravity itself. In such settings, models that treat clocks, geometry, and interactions as one may become necessary. However, these studies alone do not show that the distinction between kinematics and dynamics cannot be kept. The hypothesis of Section 3.3 (placing the Zeroth-Order Phase beyond the superposition of the observer's records) may connect with these settings in that the records of clocks become superpositions of different rates of time. That, however, is a direction for examination, not something shown in this appendix. The calculations of the models in this appendix are made under a fixed background and a time outside the model.

## 6. Tasks Toward Modeling

To develop the three phases into a physical model, the following must be specified for concrete physical systems.

1. The set of observables $\mathcal A_O$ available to the observer, and the family of states $\rho(q,\lambda)$ to be compared. A finite-dimensional example for the time direction alone is given in Section 3.2, and an example of four independent relative shifts with clocks and rulers (without testing the distinction between time and space) in Section 4.2. A model that treats all of the observer's means of observation is a task for future work.
2. The required resolutions $\varepsilon_\mu$, and the behavior of the eigenvalues $\kappa_i(\lambda)$ of the matrix $K=EFE$ made dimensionless by them.
3. Under what conditions the decrease of $D_{\mathrm{eff}}$ and the loss of means of observation that distinguish spacetime differences are tied together. A kinematic model that varies the state of the records with an approach parameter (time direction only) is given in Section 3.3; an example of clocks relaxing to thermal equilibrium (time direction only) in Section 4.1; an example of four relative shifts with relaxing clocks and rulers in Section 4.2; and an example that distinguishes time shifts from position shifts with multilevel rulers and loses only the time direction in the limit in Section 4.3. Physical processes in cosmological settings, and showing that there are no means of observation that distinguish even when the allowed operations are exhausted, are tasks for future work.
4. A model that adds boosts themselves to the compared parameters and treats them relationally from the observer's records. That the rank does not depend on the frame was shown in Section 2.1, but the Lorentz group (its connected component) is a connected, noncompact simple Lie group and has no nontrivial finite-dimensional unitary representations (finite-dimensional representations such as vectors and spinors exist but are not unitary). For this reason it does not fit the finite-dimensional models of this appendix. A treatment with quantum reference frames is a candidate.

## References

1. R. Haag, *Local Quantum Physics* (Springer, 2nd ed., 1996).
2. S. L. Braunstein, C. M. Caves, "Statistical distance and the geometry of quantum states", Phys. Rev. Lett. 72, 3439 (1994).
3. J. Liu, H. Yuan, X.-M. Lu, X. Wang, "Quantum Fisher information matrix and multiparameter estimation", J. Phys. A: Math. Theor. 53, 023001 (2020). [Paper](https://arxiv.org/abs/1907.08037)
4. S. Carlip, "Dimension and dimensional reduction in quantum gravity", Class. Quantum Grav. 34, 193001 (2017). [Paper](https://arxiv.org/abs/1705.05417)
5. J. Ambjørn, J. Jurkiewicz, R. Loll, "Spectral dimension of the universe is scale dependent", Phys. Rev. Lett. 95, 171301 (2005). [Paper](https://arxiv.org/abs/hep-th/0505113)
6. N. N. Chentsov, *Statistical Decision Rules and Optimal Inference*, Translations of Mathematical Monographs 53 (American Mathematical Society, 1982); Russian original: Nauka, Moscow, 1972.
7. D. Petz, "Monotone metrics on matrix spaces", Linear Algebra Appl. 244, 81-96 (1996). [Paper](https://doi.org/10.1016/0024-3795(94)00211-8)
8. B. S. DeWitt, "Quantum Theory of Gravity. I. The Canonical Theory", Phys. Rev. 160, 1113-1148 (1967).
9. D. N. Page, W. K. Wootters, "Evolution without evolution: Dynamics described by stationary observables", Phys. Rev. D 27, 2885-2892 (1983).
10. S. D. Bartlett, T. Rudolph, R. W. Spekkens, "Reference frames, superselection rules, and quantum information", Rev. Mod. Phys. 79, 555 (2007). [Paper](https://arxiv.org/abs/quant-ph/0610030)
11. F. G. S. L. Brandão, M. Horodecki, J. Oppenheim, J. M. Renes, R. W. Spekkens, "Resource Theory of Quantum States Out of Thermal Equilibrium", Phys. Rev. Lett. 111, 250404 (2013). [Paper](https://arxiv.org/abs/1111.3882)
12. M. Lostaglio, D. Jennings, T. Rudolph, "Description of quantum coherence in thermodynamic processes requires constraints beyond free energy", Nat. Commun. 6, 6383 (2015). [Paper](https://arxiv.org/abs/1405.2188)
13. C. Rovelli, "Partial observables", Phys. Rev. D 65, 124013 (2002). [Paper](https://arxiv.org/abs/gr-qc/0110035)
14. O. Oreshkov, F. Costa, Č. Brukner, "Quantum correlations with no causal order", Nat. Commun. 3, 1092 (2012). [Paper](https://arxiv.org/abs/1105.4464)
15. M. Zych, F. Costa, I. Pikovski, Č. Brukner, "Quantum interferometric visibility as a witness of general relativistic proper time", Nat. Commun. 2, 505 (2011). [Paper](https://arxiv.org/abs/1105.4531)

[Back to the main text](zerothOrderPhase.en.html) / [Go to Appendix 2](appendix2.en.html)

---

**Author**: 5garashi.com Design Office  
**Last updated**: 2026-11-11 JST
