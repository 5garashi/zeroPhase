---
title: 'Appendix 3: A Tentative Link Between the CCC Connecting Boundary and the Zeroth-Order Phase'
lang: en
math: true
appendix: true
translation: /appendix3.html
description: Building on the conformal connection of CCC and Penrose's argument that there are no clocks without mass, this appendix regards a uniform boundary on which measurement standards cannot be constructed as the Zeroth-Order Phase and considers the connections among the three phases.
---
<!--
  File: appendix3.en.md
  Description: A proposal connecting the three phases, based on the conformal connection of CCC and the observer's spacetime discrimination (English translation)
  Author: 5garashi.com Design Office
  Created: 2026-11-07
  Last updated: 2026-11-07 JST
  Version: 2.0.1
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Appendix 3: A Tentative Link Between the CCC Connecting Boundary and the Zeroth-Order Phase

**Author:** 5garashi.com Design Office

**Version:** <span data-version>2.0.1</span>　**Last updated:** 2026-11-07 JST

This appendix is a tentative proposal that regards the boundary at which universes are connected in conformal cyclic cosmology (CCC) as **the Zeroth-Order Phase, in which the observer cannot construct spacetime measurement standards**. It borrows from CCC the geometry of the conformal connection and Penrose's argument that "without rest mass, no clock can be built", and extends that argument to all physical quantities available to the observer. This essay does not aim to agree with every claim of CCC; it uses the parts that can be cited as footholds.

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

Even when scales disappear, dimensionless quantities can remain: dimensionless quantities such as angles, causal order, numbers of particles, and electric charge (dimensionless in natural units), and structures invariant under conformal transformations. Information from the previous universe is transmitted through the conformal structure of CCC by such quantities.

For this reason, the loss of dimensionful quantities (Section 3.2) alone does not make the Zeroth-Order Phase; it remains the Dimension-Reduction Phase. The additional hypothesis of this essay is that on the connecting boundary, observational uniformity further leaves no differences the observer can compare even in dimensionless quantities.

| Kind of physical quantity | What follows from Penrose's argument | Additional hypothesis of this essay |
|---|---|---|
| Dimensionful quantities (time, length, energy, and so on) | Lose their numerical values if there is no system with a reference rest mass and no other system that carries a scale is available | Extend the same argument to all dimensionful quantities |
| Dimensionless quantities and conformally invariant structures | Can remain (CCC traces depend on them) | On the connecting boundary, they do not remain as differences the observer can compare |

---

## 4. The Observational Procedure $\mathcal R_O$ That Constructs Spacetime Discrimination

Define $\mathcal R_O$ as the physical procedure that constructs spacetime relations from observational records.

$$
\mathcal R_O: \text{available observational records} \longmapsto \text{relations between events in spacetime (times and distances)}
$$

For example, determining the time and distance of events by combining clock readings with round trips of signals is such a procedure. It means a physical procedure by which the observer confirms distinctions, not the naming of coordinates. That $\mathcal R_O$ becomes unusable in the Zeroth-Order Phase is a hypothesis about every construction procedure based on available records; it does not mean the failure of one clock or apparatus.

| Phase | State of the procedure $\mathcal R_O$ | Rank $d_O$ (constant over a range of the parameters) |
|---|---|---|
| **Spacetime-Limit Phase** | Holds, but distinguishing between particular states is statistically difficult | $d_O=4$ |
| **Dimension-Reduction Phase** | Holds, but fewer directions can be constructed independently | $0<d_O<4$ |
| **Zeroth-Order Phase** | The procedure itself does not hold because of observational uniformity | The decay of sensitivity and the drop of $d_O$ are indicators of the approach. On the boundary itself, it is not required that $F$ be defined |

### 4.1 An Example of Dimensional Reduction by the Quantum Fisher Information Matrix

The definition of Section 2.1 of Appendix 1 is illustrated with a concrete example. Let $q^\mu$ be the spacetime parameters the observer assigns to events and $\lambda$ the parameter expressing the approach to a limit, and let $F_{\mu\nu}(q,\lambda)$ be the quantum Fisher information matrix of the family of states $\rho_O(q,\lambda)$ restricted to the observables $\mathcal A_O$ available to the observer [5, 6]. $F$ represents the upper limit on sensitivity that no measurement in $\mathcal A_O$ can exceed.

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

However, losing all sensitivity does not by itself make the Zeroth-Order Phase, because there are cases in which only the measurement sensitivity is lost while the spacetime standards are preserved outside. The decay of sensitivity and the drop of the rank are indicators of approaching the Zeroth-Order Phase; the Zeroth-Order Phase itself is defined as the procedure $\mathcal R_O$ itself not holding and the states being indistinguishable for the observer. This is because on a boundary where measurement standards do not hold, the parameters $q$ and the matrix $F$ are not necessarily defined.

---

## 5. Connecting the Universes Before and After

<figure class="essay-figure" style="margin:1.5rem 0">
<svg viewBox="0 0 350 255" role="img" aria-labelledby="fig3-title fig3-desc" style="display:block;width:100%;max-width:360px;height:auto;margin:0 auto;color:inherit" font-size="15">
<title id="fig3-title">The universes before and after and the connecting boundary</title>
<desc id="fig3-desc">The upper box is the future side of the previous universe, in the Dimension-Reduction Phase, where scales are lost. The thick horizontal line in the middle is the connecting boundary B, in the Zeroth-Order Phase, where measurement standards do not hold. The lower box is the initial side of the next universe, where measurement standards hold again and traces can be read. The vertical dashed line on the right shows that dimensionless quantities and conformal structure pass across the boundary and are read as CCC traces on the side of the next universe.</desc>
<g fill="none" stroke="currentColor" stroke-width="1.5">
<rect x="10" y="8" width="210" height="80" rx="6"/>
<rect x="10" y="168" width="210" height="80" rx="6"/>
<line x1="10" y1="128" x2="340" y2="128" stroke-width="4"/>
<line x1="234" y1="40" x2="234" y2="196" stroke-dasharray="6 5"/>
</g>
<g fill="currentColor">
<text x="22" y="32" font-weight="700">Previous universe:</text>
<text x="22" y="56">future side; scales lost</text>
<text x="22" y="78">Dimension-Reduction Phase</text>
<text x="10" y="118" font-weight="700">B: Zeroth-Order Phase</text>
<text x="10" y="150">R<tspan baseline-shift="sub" font-size="12">O</tspan> does not hold</text>
<text x="22" y="192" font-weight="700">Next universe:</text>
<text x="22" y="216">initial side; R<tspan baseline-shift="sub" font-size="12">O</tspan> holds</text>
<text x="22" y="238">again; traces readable</text>
<text x="244" y="50">Dimensionless</text>
<text x="244" y="68">quantities and</text>
<text x="244" y="86">conformal</text>
<text x="244" y="104">structure</text>
<text x="244" y="172">Traces</text>
</g>
</svg>
<figcaption>Figure 3. The universes before and after and the connecting boundary. The vertical dashed line represents the dimensionless quantities and conformal structure that pass across the boundary (Section 3.3). They are read as traces on the side of the next universe (Section 6).</figcaption>
</figure>

| Region | Physical meaning in this model |
|---|---|
| **Future side of the previous universe** | The Dimension-Reduction Phase, in which the standards for dimensionful quantities are progressively lost through the exhaustion of free energy and the loss of rest mass |
| **Connecting boundary $\mathcal B$** | The Zeroth-Order Phase, in which the procedure $\mathcal R_O$ does not hold because of observational uniformity |
| **Initial side of the next universe** | The side on which distinguishable differences appear and the measurement standard $\mathcal R_O$ is constructed again |

The central hypothesis can be written as

$$
\text{On }\mathcal B\text{, the procedure } \mathcal R_O \text{ that constructs the observer's spacetime discrimination does not hold}
$$

The common conformal metric is used to describe the boundary from both sides; it is not identified with rulers or clocks that an observer on the boundary could use.

---

## 6. The Status of Directly Observing the Zeroth-Order Phase

If measurement standards do not hold in the Zeroth-Order Phase, reading times or distances inside it and confirming the Zeroth-Order Phase directly is incompatible with this definition. This essay does not require such direct observation.

CCC predicts that traces of the previous universe remain in the CMB, and analyses searching for "Hawking points", originating from the Hawking radiation of supermassive black holes in the previous universe, have been reported [7]. This means that information passes across the boundary, which at first sight conflicts with this essay's hypothesis that "states are indistinguishable on the boundary". This essay positions these traces as follows.

1. What carries the traces is the dimensionless quantities and conformal structure of Section 3.3.
2. What reads them is an observer on the side of the next universe, where the measurement standard $\mathcal R_O$ holds again.
3. On the boundary itself, there is no standard for an observer to read the traces as times, distances, or sizes.

For this reason, observing CCC traces is not a direct measurement inside the Zeroth-Order Phase, but a measurement on the side where standards hold. Finding traces does not contradict the hypothesis of this essay. Excluding direct observation by definition does not prove the existence of the boundary either. The significance of the Zeroth-Order Phase as a hypothesis is examined by what it can explain consistently about both sides of the boundary.

---

## 7. Open Problems

1. Constructing quantitative laws that link the state of matter and gravity to the ability to construct the procedure $\mathcal R_O$
2. The microscopic mechanism by which observational uniformity holds on the connecting boundary and even differences in dimensionless quantities become unusable for the observer
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

[Back to the main text](zerothOrderPhase.en.html) / [Appendix 1](appendix1.en.html) / [Appendix 2](appendix2.en.html)

---

**Author**: 5garashi.com Design Office  
**Last updated**: 2026-11-07 JST
