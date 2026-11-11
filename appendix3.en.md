---
title: 'Appendix 3: A Tentative Link Between the CCC Connecting Boundary and the Zeroth-Order Phase'
lang: en
math: true
appendix: true
translation: /appendix3.html
description: Building on the conformal connection of CCC and Penrose's argument that there are no clocks without mass, this appendix regards a uniform boundary on which the observer has no means of observation that distinguish spacetime differences as the Zeroth-Order Phase and considers the connections among the three phases.
---
<!--
  File: appendix3.en.md
  Description: A proposal connecting the three phases, based on the conformal connection of CCC and the observer's spacetime discrimination (English translation)
  Author: 5garashi.com Design Office
  Created: 2026-11-07
  Last updated: 2026-11-11 JST
  Version: 2.4.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Appendix 3: A Tentative Link Between the CCC Connecting Boundary and the Zeroth-Order Phase

**Author:** 5garashi.com Design Office

**Version:** <span data-version>2.4.0</span>　**Last updated:** 2026-11-11 JST

This appendix is a tentative proposal that regards the boundary at which universes are connected in conformal cyclic cosmology (CCC) as **the Zeroth-Order Phase, in which the observer has no means of observation that distinguish spacetime differences**. It borrows from CCC the geometry of the conformal connection and Penrose's argument that "without rest mass, no clock can be built", and extends that argument to all physical quantities available to the observer. This essay does not aim to agree with every claim of CCC; it uses the parts that can be cited as footholds.

[Main text](zerothOrderPhase.en.html) / [Appendix 1: Logical background](appendix1.en.html) / [Appendix 2: Mathematical notes](appendix2.en.html)

---

## 1. The Central Hypothesis: The Connecting Boundary as the Zeroth-Order Phase

> **At the boundary where the future of the previous universe connects to the beginning of the next, spacetime criteria for discrimination cease to hold because of observational uniformity. The state of the observer's description that obtains on this boundary is called the "Zeroth-Order Phase".**

"Observational uniformity" here does not merely mean that density and temperature are the same everywhere. It means that, for the observer, there are no differences from which clocks, rulers, the order of events, or relations between objects can be constructed as standards of discrimination.

Measurement requires objects to compare or changes that can be repeated. A ruler requires comparison of lengths, a clock comparison of changes, and the order of events a relation that distinguishes before and after. In a limit where there are no differences from which these can be constructed, the observer cannot determine "where", "how much", or "when".

---

## 2. The Mathematical Footholds of the CCC Conformal Connection

### 2.1 Separating the Scale Factor

In a homogeneous and isotropic universe, using natural units $c=1$, the metric can be separated by the scale factor $a(\eta)$ and the conformal time $\eta$. It is related to the proper cosmic time $t$ by $\mathrm{d}t=a\,\mathrm{d}\eta$.

$$
ds^2 = a(\eta)^2 \left(-d\eta^2 + d\Sigma_k^2\right) \quad\Longrightarrow\quad d\widetilde{s}^2 = a^{-2}ds^2 = -d\eta^2 + d\Sigma_k^2
$$

This is the basic form for treating $a\to0$ on the initial side and $a\to\infty$ on the future side as conformal boundaries. Actually connecting two universes requires separate consistency conditions for the geometry and matter fields at the boundary [1, 3].

### 2.2 Connecting Through a Common Geometry

The physical metrics $g_{ab}^{-}, g_{ab}^{+}$ of the universes before and after are connected through a common conformal metric $\widetilde{g}_{ab}$ [1].

$$
g^-_{ab} = \Omega_-^2 \widetilde{g}_{ab} \;(\Omega_-\to\infty),\qquad g^+_{ab} = \Omega_+^2 \widetilde{g}_{ab} \;(\Omega_+\to0)
$$

This is a schematic expression of the connection and does not replace the full equations of CCC or the conditions that determine the conformal factor [1, 3]. In 2025, a proposal was made to make the physics of the connection concrete by assuming that the conformal infinity of the previous universe was dominated by gravitational waves [4].

That a common conformal metric $\widetilde{g}_{ab}$ exists mathematically is distinct from an observer on the boundary being able to use it as a ruler. What is adopted from CCC is the method of treating the two sides, whose physical scales differ greatly, with a common conformal geometry. A conformal transformation by itself does not reduce the dimension of spacetime in an ordinary region. For the dimensional reduction of the three phases, the structure of discrimination available to the observer (Section 4) is introduced separately.

---

## 3. Penrose's Argument and Its Extension to All Physical Quantities

### 3.1 No Clocks Without Rest Mass

Penrose argues that when particles with rest mass disappear in the far future of CCC, clocks that tick off a scale of time can no longer be built [1, 2]. A particle of rest mass $m$ has, from its mass, its own frequency and length.

$$
\nu_m=\frac{mc^2}{h},\qquad \lambda_m=\frac{h}{mc}
$$

No proper time elapses for massless particles (such as photons), and such standards cannot be made with them. For this reason, the scale of the universe itself loses its meaning, and the far future can be conformally identified with the beginning of the next universe; this is CCC's rationale. The additional hypothesis of this essay starts from a restatement of this argument.

### 3.2 Extension to All Dimensionful Physical Quantities

This argument can be extended not only to time but to all dimensionful physical quantities. Using $c$ and $\hbar$, every dimensionful quantity $Q$, such as length, time, energy, and momentum, can be expressed in the dimension of a power of mass $M^k$. To give $Q$ a numerical value, one must choose a reference mass $m_{\mathrm{ref}}$ and form the dimensionless ratio

$$
\frac{Q}{m_{\mathrm{ref}}^{\,k}}\qquad(\text{natural units } c=\hbar=1)
$$

If there is no system with a reference rest mass and no other system that carries a scale is available either, every quantity with $k\ne0$ loses its numerical value. Clocks (time), rulers (length), and the scales of energy, momentum, and temperature cease to hold all at once for the same reason.

What matters here is that it is not enough for a reference scale to exist merely as a constant in the theory; it must be carried by a physical system that works as a clock or a ruler. For example, even if the Planck mass can be formed from the gravitational constant $G$, the observer cannot use it as a scale unless some system ticks it off. This is an application of the position in Section 4.3 of the main text that "even if a mathematical structure remains, it is not a measurement standard unless the observer can use it".

### 3.3 Dimensionless Quantities and Observational Uniformity

Even when scales disappear, dimensionless quantities can remain: angles, causal order, numbers of particles, and electric charge (dimensionless in natural units), and structures invariant under conformal transformations. In CCC, the possibility is discussed that information from the previous universe is transmitted through the conformal connection and leaves traces in the next universe. The carriers of this information are thought to be field data inherited across the boundary, and structures invariant under conformal transformations are candidates. Being dimensionless is not the same as being conformally invariant, and whether numbers of particles or electric charge are preserved across the boundary must be checked individually.

For this reason, the loss of dimensionful quantities (Section 3.2) alone does not determine the Zeroth-Order Phase. Whether a state corresponds to the Dimension-Reduction Phase is likewise not settled until the corresponding family of states is specified and the rank of the quantum Fisher information matrix is computed (Section 4). The additional hypothesis of this essay is that on the connecting boundary, observational uniformity further leaves no differences the observer can compare even in dimensionless quantities.

| Kind of physical quantity | What follows from Penrose's argument | Additional hypothesis of this essay |
|---|---|---|
| Dimensionful quantities (time, length, energy, and so on) | Lose their numerical values if there is no system with a reference rest mass and no other system that carries a scale is available | Extend the same argument to all dimensionful quantities |
| Dimensionless quantities and conformally invariant structures | Can remain (candidates for the carriers of the traces discussed in CCC) | On the connecting boundary, they do not remain as differences the observer can compare |

---

## 4. Means of Observation That Distinguish Spacetime Differences, and the Rank $d_O$

The Zeroth-Order Phase is a state in which the observer has no means of observation that distinguish differences in time, distance, direction, or causal order. The means of observation here are not particular instruments but the whole of the measurements and operations that, within the spacetime region and period under consideration, the laws of physics allow and the observer can perform with the available resources (including the observables $\mathcal A_O$ available to the observer). Cases in which distinctions are merely statistically difficult (the Spacetime-Limit Phase) are not included. The region, period, and memory in which procedures can be carried out are included in the resource constraints, and procedures that store information and read it outside the region or in a later epoch are not counted among the procedures of that region. The Zeroth-Order Phase is therefore a concept fixed by the observer and by the region and period under consideration. By convention, the set of procedures always contains a procedure with a single outcome that records nothing. When the region contains no system that can carry out a readout, the observer $O$ is provisionally posited as the bearer of the procedures physically possible in that region, and the set of procedures consists only of this procedure that records nothing. The resulting $\Delta_O=0$ does not show that the state is uniform; it comes from the absence of any readout procedure.

This definition can be written with the outcome distributions of procedures the observer can perform. In a description outside the model, let $C$ be the set of candidate pairs (pairs of configurations, histories, or processes of events) compared only in their spacetime differences. The two members of a pair agree in all preparation conditions other than the spacetime difference (such as the kind of matter and internal states). Let $\mathfrak P_O$ be the set of measurement and operation procedures that can be carried out within the region and period under consideration, under the laws of physics and the stated resource constraints of the observer, and let $p(\cdot\mid x,\mathsf P)$ be the outcome distribution when procedure $\mathsf P$ is applied to candidate $x$. Then

$$
\text{Zeroth-Order Phase}\iff p(\cdot\mid x,\mathsf P)=p(\cdot\mid x',\mathsf P)\quad\text{for all }(x,x')\in C,\ \mathsf P\in\mathfrak P_O
$$

Configurations, histories, and processes, not only states of events, are compared because a difference in causal order may give the same output state and yet be distinguishable by procedures that include intermediate interventions. The candidates $x$ and the set $C$ are not quantities the observer reads; they are given from outside the model, in the same way as $\lambda$. That the observer cannot distinguish does not imply that there is no distinction in the outside description. In a model in which the spacetime structure itself is not fixed, $C$ cannot be given, and this formula cannot be used.

Summarizing the degree of distinction in one number gives

$$
\Delta_O=\sup_{(x,x')\in C}\ \sup_{\mathsf P\in\mathfrak P_O}\ \frac12\sum_k\bigl\lvert p(k\mid x,\mathsf P)-p(k\mid x',\mathsf P)\bigr\rvert
$$

The sum on the right is the total variation distance between the two outcome distributions ($k$ is the outcome of the procedure; for continuous outcomes the sum is replaced by an integral), and $\sup$ is the supremum over all pairs and all procedures. The value for a fixed pair, that is, the supremum over procedures only, is written $\delta_O(x,x')$, the degree of distinction for that pair; $\Delta_O$ is the supremum of $\delta_O$ over all pairs. If the supremum is 0, every difference is 0, so the formula above can be written

$$
\text{Zeroth-Order Phase}\iff\Delta_O=0
$$

If a pair remains whose degree of distinction is small but not 0, then $\Delta_O>0$ and it is not the Zeroth-Order Phase. $\Delta_O$ separates the Zeroth-Order Phase from the rest; it does not express the degree of the Spacetime-Limit Phase. Even in the Spacetime-Limit Phase, $\Delta_O$ is large if some pair can be distinguished completely. The degree of a phase is expressed by $d_O$ and $D_{\mathrm{eff}}$. Because these formulas use no derivatives, they can be used even when $F$ is not defined.

When the outcome distributions are represented by density operators $\rho_O(q)$ on a common state space, differentiable in $q$, and the usual SLD quantum Fisher information matrix is defined, the formula above becomes $\rho_O(q)\sim_O\rho_O(q')$ (Appendix 1, Section 1.1). Further, in the finite-dimensional framework of Appendix 1, Section 1.1, when the observation conditions are specified by an algebra of observables and a trace-preserving conditional expectation and the state restricted to that algebra is used, $\rho_O(q)$ is constant, and $F=0$, $D_{\mathrm{eff}}=0$ for every $N$ (by the definition in Appendix 1, Section 2.1 (5)), and $d_O=0$ over the whole range. No assumption on the rank of the state is needed. If the quantum Fisher information of the original state is computed without the restriction, this conclusion fails. For example, if only measurements in the z basis are allowed and the state is $(\lvert0\rangle+e^{iq}\lvert1\rangle)/\sqrt2$, the outcome distribution of the allowed measurement does not depend on $q$, but the quantum Fisher information of the original state is 1. After restriction to the algebra of observables diagonal in the z basis, the quantum Fisher information is also 0 (see the example and its interpretation in Appendix 1, Section 1.1). When the allowed measurements do not form an algebra, the definition by outcome distributions takes precedence. The converse does not hold. For example, if a discrete spacetime difference (such as two orders) is represented by a label $s\in\lbrace0,1\rbrace$ and the state is $\rho(q,s)=\lvert s\rangle\langle s\rvert$, then $F$ with respect to $q$ is 0 everywhere, but if the observer can use a measurement in this basis, $s=0$ and $s=1$ can be distinguished.

These formulas restate the definition and derive no new physics. They cannot be computed until the contents of $C$ and $\mathfrak P_O$ are specified for each model, and the judgment of the phase depends on how the resource constraints are chosen.

For example, determining the time and distance of events by combining clock readings with round trips of signals is one means of observation that distinguishes differences in time and distance. The absence of means of observation in the Zeroth-Order Phase is a hypothesis about every measurement and operation available to the observer; it does not mean the failure of a single clock or apparatus.

| Phase | Means of observation that distinguish spacetime differences | Rank $d_O$ (for a specified family of states, over a range of the parameters; a guide) |
|---|---|---|
| **Spacetime-Limit Phase** | Present in every direction (distinction may be statistically difficult) | $d_O=4$ |
| **Dimension-Reduction Phase** | Absent in some directions | $d_O<4$ ($d_O=0$ is the extreme case; $d_O=0$ alone does not define the Zeroth-Order Phase) |
| **Zeroth-Order Phase** | Absent in every direction, because of observational uniformity | The decay of sensitivity and the drop of $d_O$ are indicators of approaching this phase. On the boundary itself, it is not required that $F$ be defined |

$d_O$ and the Zeroth-Order Phase are different kinds of concepts. $d_O$ is fixed for each combination of a specified family of states and $\mathcal A_O$, and is the number of directions that can be distinguished to first order (Section 4.1); it is an indicator representing only part of the means of observation. Even if $d_O=0$ for some family of states, the state is not the Zeroth-Order Phase if the observer can distinguish by other means of observation. If an external spacetime standard remains and the observer can in principle become correlated with it, the state is not the Zeroth-Order Phase. This is a sufficient condition for not being the Zeroth-Order Phase, not a necessary one: even without the possibility in principle of correlating with an external reference frame, the relative time between clocks may be distinguishable ([Appendix 1, Section 3.2](appendix1.en.html), case B). Even if $d_O=0$ for all means of observation of the observer, this alone does not define the Zeroth-Order Phase, because $d_O$ counts only the first-order sensitivity with respect to the compared parameters $q$ in the range for which the rank is specified, and does not count discrete distinctions not represented by $q$, causal order, or distinctions of states outside that range (in another connected component). If the range where the rank is 0 is a connected open region and the derivative of the map to states vanishes in all directions, even distant states within it cannot be distinguished (Appendix 1, Section 2.1 (6)). Conversely, in the Zeroth-Order Phase, if $F$ of the state restricted according to the observation conditions can be defined, $d_O=0$ for all means of observation. If $F$ cannot be defined, the question of $d_O$ does not arise. Taking the decrease of $d_O$ as an indicator of approaching the Zeroth-Order Phase is a hypothesis of this essay, and its grounds remain an open problem.

### 4.1 An Example of Dimensional Reduction by the Quantum Fisher Information Matrix

The definition of Section 2.1 of Appendix 1 is illustrated with a concrete example. Let $q^\mu$ be the parameters of time and distance that the observer reads by means of observation (not external coordinates) and $\lambda$ the parameter expressing the approach to a limit, and let $F_{\mu\nu}(q,\lambda)$ be the quantum Fisher information matrix of the family of states $\rho_O(q,\lambda)$ restricted to the observables $\mathcal A_O$ available to the observer [5, 6]. $F$ represents the upper limit on sensitivity that no measurement in $\mathcal A_O$ can exceed.

The number of independent spacetime parameters that can be discriminated as first-order changes is expressed by the rank of the matrix.

$$
d_O(q,\lambda) = \operatorname{rank} F(q,\lambda)
$$

If the rank is constant throughout a range of $q$, states along the lost directions are strictly indistinguishable for the observer (Appendix 1, Section 2.1 (6)). The effective dimension $D_{\mathrm{eff}}$ at a finite number of measurements $N$ and resolution $\varepsilon$ is an auxiliary indicator of how well each direction can be read, and it approaches $d_O$ as $N\to\infty$.

As an example, consider a model in which four independent dimensionless parameters are read through Gaussian noise of unit variance.

$$
y^\mu=b_\mu(\lambda)\,q^\mu+\epsilon^\mu,
\qquad \epsilon^\mu\sim\mathcal N(0,1)
$$

Assume that this distribution is what the best available measurement gives. If the noises are mutually independent, the information matrix is diagonal, and the effective dimension at resolution $\varepsilon$ is as follows.

$$
F=\operatorname{diag}(b_0^2,b_1^2,b_2^2,b_3^2),
\qquad
D_{\mathrm{eff}}=\sum_{\mu=0}^{3}\frac{N\varepsilon^2 b_\mu^2}{1+N\varepsilon^2 b_\mu^2}
$$

The contribution of each direction, $N\varepsilon^2 b_\mu^2/(1+N\varepsilon^2 b_\mu^2)$, changes with the sensitivity $N\varepsilon^2 b_\mu^2$ as follows.

| Sensitivity $N\varepsilon^2 b_\mu^2$ | Contribution | Reading of that direction |
|---|---|---|
| $100$ | $0.99$ | The required resolution is not excluded by the estimation lower bound |
| $1$ | $0.5$ | The boundary at which the lower bound equals the required resolution |
| $0.01$ | $0.0099$ | Almost unreadable |
| $0$ | $0$ | Unreadable in principle (the rank drops) |

For example, if the sensitivities of the four directions are $100, 100, 1, 0.01$, then $D_{\mathrm{eff}}\approx0.99+0.99+0.5+0.01=2.49$. Under these measurement conditions, the directions contribute about 2.49 directions' worth in total. Because none of the four $b_\mu$ is zero, the rank is 4, and the phase is the Spacetime-Limit Phase. As $b_\mu$ approaches zero, the contribution of that direction decreases continuously. In this model $b_\mu$ does not depend on $q$, so when $b_\mu=0$, changes in that direction no longer appear in the measurement results over the whole range of $q$. The rank drops and states along that direction become strictly indistinguishable, so the Dimension-Reduction Phase is entered. As all $b_\mu$ approach zero, $D_{\mathrm{eff}}$ under fixed measurement conditions approaches zero. The rank drops where the corresponding $b_\mu$ actually becomes zero. For example, if $b_\mu(\lambda)=e^{-\lambda}$, the rank remains 4 for finite $\lambda$, and only the sensitivity is lost smoothly.

However, losing all sensitivity does not by itself make the Zeroth-Order Phase, because there are cases in which only the measurement sensitivity is lost while the spacetime standards are preserved outside. The decay of sensitivity and the drop of the rank are indicators of approaching the Zeroth-Order Phase; the Zeroth-Order Phase itself is defined as the observer having no means of observation that distinguish spacetime differences and the states being indistinguishable for the observer (Section 4), because on a boundary where measurement standards do not hold, the parameters $q$ and the matrix $F$ are not necessarily defined.

### 4.2 The Degree of Distinction in a Setting Modeled on the Far Future of CCC: A Toy Model by Kind of Pair

The degree of distinction $\Delta_O$ of Section 4 is computed for each kind of compared pair in a small model modeled on the far future of CCC. As a premise, there are no massive particles, and the observer has no standard (clock or ruler) that carries scales of length or time. Even with only massless fields, other scales or quantum numbers might take the place of a standard; this is a premise, not a conclusion. Under this premise, the observer's procedures are limited to operations covariant under dilation (a change of scale) and measurements invariant under a global dilation, and the outcome distributions of states differing by a global dilation do not change. This is the same form of restriction as case B of [Appendix 1, Section 3.2](appendix1.en.html) for the procedures of an observer without an external clock.

In conformal field theory, dilations are generated by the dilation generator $D$ (the correspondence between its eigenvalues and the scaling dimensions of operators depends on settings such as the choice of quantization). This section is a two-level toy model that formally mimics the action of the dilation group; it does not reproduce the eigenvalue structure of $D$ or the global correspondence between scale ratios and phases (the phase in the model is periodic, whereas a ratio of scales has no period). The model has two subsystems, each with a two-level generator $h\lvert1\rangle\langle1\rvert$ (a two-level system whose generator has eigenvalues $0$ and $h$). The model formally reinterprets the time translation of the clock model of Appendix 1, Section 3.2 as a dilation and does not address the difference in physical meaning between dilation and time translation. Both subsystems are in $\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2$, and the results depend on this choice of state. The values below are the degree of distinction for a pair, $\delta_O^{(1)}$, with procedures limited to one measurement on one copy (the trace distance between the two states after restriction to measurements invariant under a global dilation); they are a lower bound on the general $\delta_O$, not a computation of $\Delta_O$ itself. We set $h=1$ and denote the amount of dilation by $s$.

**(1) Pairs that differ only in scale.** Pairs whose two members differ by a global dilation give the same outcome distributions under measurements invariant under a global dilation, and the degree of distinction is 0 (also 0 numerically for $s=0.5,\ 1,\ \pi$). This is the constraint of the form corresponding to Penrose's "no clocks without rest mass" (Section 3.1), expressed in this model; the model does not contain rest mass itself and assumes the absence of a scale standard as a premise. By contrast, pairs in which only one subsystem is dilated, that is, pairs differing in the relative scale of the subsystems, can be distinguished. After the restriction, what remains dependent on $s$ is only the relative phase of the state $(\lvert01\rangle+e^{-ihs}\lvert10\rangle)/\sqrt2$ in the block of weight $1/2$, and the degree of distinction is $\frac12\lvert\sin(hs/2)\rvert$ ($0.5$ at $s=\pi$; $\lvert\sin(hs/2)\rvert$ before the restriction). In terms of the quantum Fisher information as well, the direction of global dilation gives 0 and the direction of relative scale gives $h^2/2$. This is an example of relative differences between subsystems remaining even when scale is lost (Section 3.3).

**(2) Pairs of order-dependent processes.** Suppose two changes A and B act, in mutually noncommuting ways, on a degree of freedom unaffected by dilation (for example, the polarization of light; dilation does not change polarization). Then, for a suitable initial state, the state of that degree of freedom can differ between the process in which B follows A and the process in which A follows B. In the example in which the initial state is a pure polarization in the $+z$ direction and it is rotated by $90^\circ$ about the x and z axes ($e^{-i\pi\sigma_x/4}$ and $e^{-i\pi\sigma_z/4}$), the Bloch vectors of the two states are orthogonal and the degree of distinction is $1/\sqrt2\approx0.71$. With the channel $\mathcal D_p(\rho)=(1-p)\rho+pI/2$ that destroys polarization, the degree of distinction is $(1-p)/\sqrt2$ (about $0.35$ at $p=1/2$), and 0 when the polarization is lost completely.

This is an example of distinguishing two processes whose order is given from the start; it is not a computation of causal order in spacetime itself. The two are related through the commutativity of local operations: local operations at spacelike-separated events commute, and the result depends on the order only when the events are causally connected. Because conformal transformations preserve light cones, the causal structure of spacetime remains even without a scale standard. However, the continuation of the causal structure across the CCC connecting boundary is an assumption of CCC, and the conformal factor becomes singular on the boundary. Moreover, the preservation of the causal structure of spacetime is a separate matter from whether the observer can distinguish it from records.

**(3) What this model shows.** In this model, the loss of scale alone makes the degree of distinction 0 only for pairs that differ only in global scale; pairs differing in relative scale and pairs of order-dependent processes can be distinguished. Therefore the central hypothesis that the CCC connecting boundary is the Zeroth-Order Phase (Section 1) needs, in addition to the loss of scale, conditions such as the following.

- (A) Uniformity of state: the state of the degrees of freedom the observer compares is the same for every pair of differing configurations. This is the case in which even traces of relative scale and order become uniform in those degrees of freedom.
- (B) Absence of readout means: even if the degrees of freedom that carry the difference in configuration (the state of the field) remain, there is no interaction that transfers it to the observer's outcome distributions and no system that carries out a readout (a bound structure acting as a detector or recording device).

Because the degree of distinction is fixed by both the pairs and the procedures, these two are extreme cases, and there are intermediate cases in which only some pairs become uniform. Nor do they exclude other possibilities, such as the definition of the boundary itself being undetermined.

(A) and (B) are not mutually exclusive. Even if the state of the degrees of freedom the observer compares is uniform, if differences remain in unusable degrees of freedom or correlations, they may be readable later ([Appendix 1, Section 3.2](appendix1.en.html), case C). Traces arising from the difference between candidates can be said not to cross the boundary only when the state including all degrees of freedom and correlations passing across the boundary is the same for the candidates and the subsequent evolution does not depend on the candidates. Section 6 took dimensionless quantities and conformal structure to pass across the boundary as traces, read by observers in the next universe. What is compatible with this is the case in which the observer on the boundary cannot distinguish in the compared degrees of freedom (uniformity in the sense of (A), or (B)), while differences remain in the degrees of freedom passing across the boundary as a whole. In (B), degrees of freedom that carry differences, such as the polarization of (2), remain in the field, and conserved dimensionless quantities such as electric charge may also remain, but on the boundary there are no means to read them and transfer them to outcome distributions, so the degree of distinction is 0. If an observer with readout means appears later, the difference can be read. That is, the difference cannot be distinguished by procedures limited to the region and period of the boundary, but can be distinguished by procedures that extend to the next universe (by the way the region and period are specified in Section 4). Since Section 1 says that differences do not exist "for the observer", Section 6 is compatible if "observational uniformity" is read as follows: at least one of (A) uniformity of state or (B) absence of means holds, while differences remain in the degrees of freedom passing across the boundary as a whole.

(B) has two weaknesses. One is that if interacting massless particles (such as charged particles that have lost their mass) remain, a system that carries out a readout might be built, and (B) could fail. This is the greatest weakness of (B) and the core of open problem 2 in Section 7. The other is that, because the conclusion rests on "the absence of means", the hypothesis becomes hard to refute unless the absence of means is shown physically. A physical explanation is needed of why there is no system that carries out a readout on the boundary.

**(4) What this model does not show.**

- It is a two-level, finite-dimensional toy model, not a field-theory calculation. The results depend on the choice of the initial state of the subsystems ($\lvert+\rangle$).
- Conformal transformations other than dilation (special conformal transformations), the state of fields on an expanding universe, and the change of scale on the CCC boundary itself are not treated.
- Dissipation at the boundary, the change to mixed states, and the observer being part of the system are not treated.
- The degree of distinction is the one-measurement value $\delta_O^{(1)}$. When procedures that use many copies of the same state are included, the degree of distinction grows for pairs for which it is nonzero, and stays 0 for pairs for which it is 0.
- (2) distinguishes processes with a given order; it does not compute causal order from the structure of spacetime.

---

## 5. Connecting the Universes Before and After

<figure class="essay-figure" style="margin:1.5rem 0">
<svg viewBox="0 0 350 255" role="img" aria-labelledby="fig3-title fig3-desc" style="display:block;width:100%;max-width:360px;height:auto;margin:0 auto;color:inherit" font-size="15">
<title id="fig3-title">The universes before and after and the connecting boundary</title>
<desc id="fig3-desc">The upper box is the future side of the previous universe, where scales are lost; the connection hypothesis associates it with the Dimension-Reduction Phase. The thick horizontal line in the middle is the connecting boundary B, in the Zeroth-Order Phase, where spacetime differences cannot be distinguished. The lower box is the initial side of the next universe, where means of distinction exist again and traces can be read. The vertical dashed line on the right shows schematically the possibility that field data assumed to be inherited across the boundary pass across it and are read as CCC traces on the side of the next universe.</desc>
<g fill="none" stroke="currentColor" stroke-width="1.5">
<rect x="10" y="8" width="210" height="80" rx="6"/>
<rect x="10" y="168" width="210" height="80" rx="6"/>
<line x1="10" y1="128" x2="340" y2="128" stroke-width="4"/>
<line x1="234" y1="40" x2="234" y2="196" stroke-dasharray="6 5"/>
</g>
<g fill="currentColor">
<text x="22" y="32" font-weight="700">Previous universe:</text>
<text x="22" y="56">future side; scales lost</text>
<text x="22" y="78">Dim.-Reduction (hypothesis)</text>
<text x="10" y="118" font-weight="700">B: Zeroth-Order Phase</text>
<text x="10" y="150">Spacetime not distinguishable</text>
<text x="22" y="192" font-weight="700">Next universe:</text>
<text x="22" y="216">initial side; means exist</text>
<text x="22" y="238">again; traces readable</text>
<text x="244" y="50">Dimensionless</text>
<text x="244" y="68">quantities and</text>
<text x="244" y="86">conformal</text>
<text x="244" y="104">structure</text>
<text x="244" y="172">Traces</text>
</g>
</svg>
<figcaption>Figure 3. The universes before and after and the connecting boundary. The vertical dashed line represents schematically the possibility that field data assumed to be inherited across the boundary (such as structures invariant under conformal transformations; Section 3.3) are transmitted. They are read as traces on the side of the next universe (Section 6). Treating the future side as the Dimension-Reduction Phase is an association made by the connection hypothesis, not a judgment from the loss of scale alone (Section 3.3).</figcaption>
</figure>

| Region | Physical meaning in this model |
|---|---|
| **Future side of the previous universe** | The side on which the standards for dimensionful quantities are progressively lost through the exhaustion of free energy and the loss of rest mass. The connection hypothesis associates it with the Dimension-Reduction Phase (not judged from the loss of scale alone; Section 3.3). For the time direction, a model in which clocks relax to thermal equilibrium is given in [Appendix 1, Section 4.1](appendix1.en.html) |
| **Connecting boundary $\mathcal B$** | The Zeroth-Order Phase, in which, because of observational uniformity, the observer has no means of observation that distinguish spacetime differences (central hypothesis) |
| **Initial side of the next universe** | The side on which distinguishable differences appear and means of observation that distinguish spacetime differences exist again in principle |

The central hypothesis can be written as

$$
\text{On }\mathcal B\text{, the observer has no means of observation that distinguish spacetime differences}
$$

The common conformal metric is used to describe the boundary from both sides; it is not identified with rulers or clocks that an observer on the boundary could use.

---

## 6. The Status of Directly Observing the Zeroth-Order Phase

If measurement standards do not hold in the Zeroth-Order Phase, reading times or distances inside it and confirming the Zeroth-Order Phase directly is incompatible with this definition. This essay does not require such direct observation.

CCC predicts that traces of the previous universe remain in the CMB, and analyses searching for "Hawking points", originating from the Hawking radiation of supermassive black holes in the previous universe, have been reported [7]. Under the assumptions of CCC, this means that information passes across the boundary, which at first sight conflicts with this essay's hypothesis that "states are indistinguishable on the boundary". This essay positions these traces as follows.

1. What is taken to carry the traces is field data assumed to be inherited across the boundary, and structures invariant under conformal transformations are candidates (Section 3.3).
2. What reads them is an observer on the side of the next universe, where means of observation that distinguish spacetime differences exist again.
3. On the boundary itself, there is no standard for an observer to read the traces as times, distances, or sizes.

For this reason, observing CCC traces is not a direct measurement inside the Zeroth-Order Phase, but a measurement on the side where standards hold. Finding traces does not contradict the hypothesis of this essay. Excluding direct observation by definition does not prove the existence of the boundary either. The significance of the Zeroth-Order Phase as a hypothesis is examined by what it can explain consistently about both sides of the boundary.

---

## 7. Open Problems

1. Constructing quantitative laws that link the state of matter and gravity to the presence or absence of means of observation that distinguish spacetime differences
2. The microscopic mechanism by which observational uniformity holds on the connecting boundary and even differences in dimensionless quantities become unusable for the observer. In the toy model of Section 4.2, the loss of scale alone leaves distinctions of relative scale and of order-dependent processes. What is compatible with the traces of Section 6 is the case in which differences remain in the degrees of freedom passing across the boundary as a whole even though the degrees of freedom the observer compares are uniform, or the case in which the observer has no means to read the differences (Section 4.2 (3)). One of the central questions is whether it can be said that there are no readout means when interacting massless particles remain
3. Formulating the "emergence of differences" from the Zeroth-Order Phase to the next universe

---

## References

1. R. Penrose, "On the Gravitization of Quantum Mechanics 2: Conformal Cyclic Cosmology," Foundations of Physics 44, 873–890 (2014). [Paper](https://doi.org/10.1007/s10701-013-9763-z)
2. R. Penrose, *Cycles of Time: An Extraordinary New View of the Universe* (The Bodley Head, 2010).
3. C. Stevens, O. Markwell, "Toward fixing a framework for conformal cyclic cosmology" (2022). [Paper](https://arxiv.org/abs/2212.06914)
4. K. A. Meissner, R. Penrose, "The Physics of Conformal Cyclic Cosmology" (2025). [Paper](https://arxiv.org/abs/2503.24263)
5. S. L. Braunstein, C. M. Caves, "Statistical distance and the geometry of quantum states," Physical Review Letters 72, 3439 (1994). [Paper](https://doi.org/10.1103/PhysRevLett.72.3439)
6. J. Liu, H. Yuan, X.-M. Lu, X. Wang, "Quantum Fisher information matrix and multiparameter estimation," J. Phys. A: Math. Theor. 53, 023001 (2020). [Paper](https://arxiv.org/abs/1907.08037)
7. D. An, K. A. Meissner, P. Nurowski, R. Penrose, "Apparent evidence for Hawking points in the CMB Sky," Monthly Notices of the Royal Astronomical Society 495, 3403–3408 (2020). [Paper](https://doi.org/10.1093/mnras/staa1343)

[Back to the main text](zerothOrderPhase.en.html) / [Appendix 1](appendix1.en.html) / [Appendix 2](appendix2.en.html) / [Appendix 4](appendix4.en.html)

---

**Author**: 5garashi.com Design Office  
**Last updated**: 2026-11-11 JST
