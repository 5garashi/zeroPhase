---
title: 'Appendix 4: The Quantum Limit on Distinguishing Two Distant Sources and the Effects of Propagation'
lang: en
math: true
appendix: true
translation: /appendix4.html
description: Derives the quantum limit on distinguishing two distant sources of Section 3.1 of the main text, and organizes the upper limits on the observer's resources, whether information is lost during propagation, and the relation between cosmic variance and Fisher information.
---
<!--
  File: appendix4.en.md
  Description: Derivation of the quantum limit on distinguishing two distant sources, and the observer's resource limits and propagation effects (English translation)
  Author: 5garashi.com Design Office
  Created: 2026-11-11
  Last updated: 2026-11-11 JST
  Version: 2.4.0
  License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# Appendix 4: The Quantum Limit on Distinguishing Two Distant Sources and the Effects of Propagation

**Author:** 5garashi.com Design Office

**Version:** <span data-version>2.4.0</span>　**Last updated:** 2026-11-11 JST

This appendix derives the quantum limit on distinguishing two distant sources of [Section 3.1 of the main text](zerothOrderPhase.en.html), and organizes the upper limits on the observer's resources that it presupposes and whether information is lost while light travels. It collects the derivations and conditions on which the main text and the appendices rely.

[Main text: Observation Limits and the Undifferentiated Origin](zerothOrderPhase.en.html) / [Appendix 1: Logical background](appendix1.en.html) / [Appendix 2: Mathematical notes](appendix2.en.html) / [Appendix 3: The CCC connection](appendix3.en.html)

## 1. Three Kinds of Difficulty in Distinguishing

Distant objects are harder to distinguish not only because angles become smaller. This appendix treats the following three kinds separately.

| Kind | Content | Section of this appendix |
|---|---|---|
| Disadvantages the observer's resources can make up for | Angular differences are small and few photons arrive. Larger apertures and longer observation can make up for this, but those resources have upper limits from quantum mechanics and gravity | Sections 2 and 3 |
| Constraints on the side of the universe that cannot be made up for | (a) The universe was opaque when the light was emitted. (b) Only one sky can be observed | [Main text, Section 3.1](zerothOrderPhase.en.html); Section 5 |
| The hypothesis that information is lost while light travels | The proposal that spacetime fluctuations accumulate with distance and reduce the information carried by each photon | Section 4; [Main text, Section 2.1](zerothOrderPhase.en.html) |

All are treated as examples of the Spacetime-Limit Phase, in which distinctions become harder while the spacetime framework is preserved. No transition to the Dimension-Reduction Phase or the Zeroth-Order Phase is derived from the calculations of this appendix.

## 2. Upper Limits on the Observer's Resources

When two positions are distinguished by the mean arrival direction of photons, the distinguishability is expressed by $R=\Delta\theta\sqrt N/\sigma_\theta$ ($\Delta\theta$ is the angular difference, $N$ the number of photons collected, and $\sigma_\theta$ the directional error of a single photon). Receiving a photon through an aperture $D$ confines the transverse position of the photon to a width of about $D$, so by the uncertainty principle $\sigma_\theta\sim\lambda_{\mathrm{obs}}/D$ (the diffraction limit). Because the error of the mean of $N$ photons is $\sigma_\theta/\sqrt N$, the position of a source can be estimated more finely than the diffraction limit. The upper limit on distinguishability is set by the upper limits on the aperture and on the number of photons. This essay adopts the following upper limits under the conditions of the cosmological model, observer, and apparatus configuration it assumes. None of them is by itself a universal theorem that uniquely fixes an upper limit on the aperture or the number of photons; their values depend on those conditions ([Main text, Sections 3.1 and 4.2](zerothOrderPhase.en.html); [Appendix 2, Section 10](appendix2.en.html)).

**(1) Upper limits in principle on the aperture.** The following three cannot be avoided by engineering.

- $\sigma_\theta\sim\lambda/D$ holds when the aperture is much smaller than the distance $L$ to the source. As $D$ approaches $L$, the length that ordinary imaging can resolve levels off at about half a wavelength (the Abbe limit). This is a resolution scale of imaging, not a lower limit on the precision with which, in a model in which the number and shape of the sources are known, a separation can be estimated or one source can be told from two (Section 3). In cosmology $L$ is of order $10^{25}$ m, and this limit is not reached.
- A joint measurement that includes phase information from light received at separate apertures requires communication and resources to bring the light to one place or to carry its state by quantum repeaters or similar means, and this is possible only within a causally connected region. In an expanding universe, unbound parts are pulled apart, and depending on its mass and arrangement an apparatus collapses under its own gravity. Measures of the size applied to the aperture are given in [Appendix 2, Sections 10.2 and 10.6 (4)](appendix2.en.html).
- Scattering by the interstellar and intergalactic medium cannot be avoided however large the aperture is made (the same kind of limit as (a) in the main text).

**(2) Upper limits in principle on the number of photons.** The number of photons that can be collected is $N=\Phi_N A T\eta$ ($\Phi_N$ is the number of photons arriving per unit area and unit time, $A\propto D^2$ the collecting area, $T$ the observation time, and $\eta\le1$ the detection efficiency), and each factor has an upper limit. The observation time is limited by the lifetime of the source. In a universe with a future event horizon (such as one that becomes asymptotically de Sitter), depending on the motion of the source and the observer, the total number of photons that can be received is finite even after waiting forever. There are also constraints from quantum mechanics.

- The quantum Fisher information about direction obtained from a single photon received through an aperture $D$ does not exceed about $(2\pi D/\lambda)^2$. Because the light of the source is not a state prepared by the observer, the observer cannot increase the precision by entangling the photons (whether the incoming light carries useful correlations of its own depends on the source; Section 3 treats the photons as independent, as weak thermal light).
- When the light of separate telescopes is combined, a phase-preserving amplifier adds, in the ideal high-gain limit, noise equivalent to at least half the zero-point fluctuations (depending on the convention for counting noise) [1]. Carrying the light by quantum repeaters has been proposed as a way to avoid this [2].
- An apparatus that records the results has, for size $R$ and energy $E$, an upper limit on the information it can store, $I\le2\pi ER/(\hbar c\ln2)$ [3], and an upper limit $2E/(\pi\hbar)$ on the rate at which it can evolve to an orthogonal state ($E$ is the mean energy measured from the ground state) [4]. These are constraints with conditions of applicability, and they do not by themselves fix an upper limit on the number of photons.
- When the universe becomes asymptotically de Sitter, thermal radiation at the horizon temperature becomes a residual noise ((d) in the main text).

**(3) Upper limit on distinguishability.** Because $N$ has an upper limit $N_{\max}$, the distinguishability also has the upper limit

$$
R\ \le\ R_{\max}\sim\Delta\theta\,\frac{2\pi D_{\max}}{\lambda}\sqrt{N_{\max}}
$$

Differences so small that $R_{\max}<1$ cannot be distinguished by that observer under the conditions of this estimate. In the language of this essay, directions in which the eigenvalue $\kappa_i$ of the quantum Fisher information matrix is much smaller than $1/N_{\max}$ cannot be read at the required resolution by locally unbiased estimation, whichever measurement is chosen ([Appendix 1, Section 2.1 (4)](appendix1.en.html); [Main text, Section 4.2](zerothOrderPhase.en.html)). The discrimination of two states a finite distance apart is treated separately, as in Section 3. Systematic errors, and one-time events in which the total number of photons is fixed, cannot be made up for by adding photons, independently of this upper limit.

## 3. Derivation of the Quantum Limit on Distinguishing Two Distant Sources

When the separation of two point sources closer than the diffraction limit is measured by ordinary imaging, the information obtained approaches zero as the separation narrows. Tsang and colleagues showed that if a measurement that sorts the light into spatial modes and counts them is chosen, the information does not decrease even for narrow separations [5]. Whether states can be distinguished depends on the choice of measurement as well. This section derives, in a simple model, the limit that cannot be exceeded even with an ideal quantum measurement. The results rederive existing results [5, 6] from the propagation of light; they do not show a new limit.

**(1) Model.**

| Condition | Content |
|---|---|
| Sources | Two point sources, mutually incoherent and equally bright, with total power $P$ |
| Light intensity | Weak thermal light with much less than one photon per mode; photons are treated as independent samples |
| Optics | A circular aperture of diameter $D$; ideal, with no background light, dark current, or atmospheric fluctuations; overall efficiency $\eta$ |
| Observation | Wavelength $\lambda$, observation time $T$; the distance $R$ to the sources is known |

**(2) Number of photons received.** In non-expanding space, the expected number of photons from an isotropically emitting source that enter the aperture $A=\pi D^2/4$ is

$$
\bar N=\frac{\eta PAT\lambda}{4\pi R^2hc}=\frac{\eta PTD^2\lambda}{16R^2hc}
$$

**(3) The state of a single photon and its quantum Fisher information.** The state of a single photon is a mixture of the states coming from the two sources.

$$
\rho(\theta)=\frac12\left(\lvert\psi_+\rangle\langle\psi_+\rvert+\lvert\psi_-\rangle\langle\psi_-\rvert\right),\qquad
\lvert\psi_\pm\rangle=e^{\mp ik\theta X/2}\lvert\psi_0\rangle
$$

$\theta$ is the angular separation of the two sources, $k=2\pi/\lambda$, $X$ the transverse position in one direction in the plane of the aperture, and $\lvert\psi_0\rangle$ the state when a single source is at the center. The quantum Fisher information for the separation $\theta$ is $F_Q=k^2\operatorname{Var}(X)$, which is constant, independent of the separation [5]. If the state is uniform within a circle of radius $D/2$, $\operatorname{Var}(X)=D^2/16$ and $F_Q=\pi^2D^2/(4\lambda^2)$. Because the rank of the state changes at $\theta=0$, this value is used for $\theta>0$.

The form of this state follows from the propagation of light from the source to the aperture. The amplitude for light to reach a point of the aperture (transverse position $\boldsymbol\rho$) at distance $R$ from a point of the source (transverse position $\boldsymbol a$) is the sum of the contributions of all paths the light can take (the path integral), and when the light travels close to the optical axis (the paraxial approximation), it becomes the Fresnel propagator.

$$
K(\boldsymbol\rho,\boldsymbol a)\propto\exp\left(\frac{ik\lvert\boldsymbol\rho-\boldsymbol a\rvert^2}{2R}\right)
=\exp\left(\frac{ik\rho^2}{2R}\right)\exp\left(-\frac{ik\,\boldsymbol a\cdot\boldsymbol\rho}{R}\right)\exp\left(\frac{ika^2}{2R}\right)
$$

The first factor multiplies every state in the same form regardless of the position of the source, so it cancels in the overlaps between states. The last factor is a constant phase for each source and does not make the states differ. The difference in source position appears only in the middle factor, that is, in the phase gradient across the aperture (Figure 4). Placing the sources at $\pm s/2$ with $\theta=s/R$, the middle factor becomes $e^{\mp ik\theta X/2}$.

<figure class="essay-figure" style="margin:1.5rem 0">
<svg viewBox="0 0 300 215" role="img" aria-labelledby="fig4-title fig4-desc" style="display:block;width:100%;max-width:360px;height:auto;margin:0 auto;color:inherit" font-size="15">
<title id="fig4-title">Two sources and the phase gradient across the aperture</title>
<desc id="fig4-desc">On the left are two point sources separated by s. At distance R to the right is an aperture of diameter D. Thin solid lines run from the upper source to both ends of the aperture, and thin dashed lines from the lower source, showing that light reaches the whole aperture. Further to the right, three lines show the phase across the aperture. The state psi 0 of the central source is a vertical dashed line with no tilt, and the states psi plus and psi minus of the two sources are lines tilted by the same amount in opposite directions.</desc>
<g fill="none" stroke="currentColor">
<path d="M30,105 H290" stroke-width="1" stroke-dasharray="4 4"/>
<path d="M20,85 V125 M16,85 H24 M16,125 H24" stroke-width="1.5"/>
<path d="M40,85 L190,50 M40,85 L190,160" stroke-width="1"/>
<path d="M40,125 L190,50 M40,125 L190,160" stroke-width="1" stroke-dasharray="3 3"/>
<path d="M190,50 V160" stroke-width="5"/>
<path d="M30,188 H190 M30,182 V194 M190,182 V194" stroke-width="1.5"/>
<path d="M250,62 V148" stroke-width="2" stroke-dasharray="5 4"/>
<path d="M232,62 L268,148" stroke-width="3"/>
<path d="M268,62 L232,148" stroke-width="3"/>
</g>
<g fill="currentColor">
<circle cx="40" cy="85" r="5"/>
<circle cx="40" cy="125" r="5"/>
<text x="8" y="110" text-anchor="middle">s</text>
<text x="40" y="70" text-anchor="middle">Sources</text>
<text x="190" y="40" text-anchor="middle">Aperture D</text>
<text x="110" y="208" text-anchor="middle">R</text>
<text x="226" y="56" text-anchor="middle">ψ<tspan baseline-shift="sub" font-size="12">+</tspan></text>
<text x="276" y="56" text-anchor="middle">ψ<tspan baseline-shift="sub" font-size="12">−</tspan></text>
<text x="250" y="170" text-anchor="middle">ψ<tspan baseline-shift="sub" font-size="12">0</tspan></text>
</g>
</svg>
<figcaption>Figure 4. Two sources and the phase across the aperture (distances drawn compressed). The difference in source position appears only in the phase gradient $e^{\mp ik\theta X/2}$ across the aperture. The curvature of the wavefront $e^{ik\rho^2/(2R)}$, common to all sources, cancels in the overlaps between states.</figcaption>
</figure>

**(4) Separating estimation from discrimination.** From the quantum Cramér–Rao bound, the error in estimating the separation is $\sigma_\theta\ge1/\sqrt{\bar NF_Q}=2\lambda/(\pi D\sqrt{\bar N})$. Converted to the actual separation $d=R\theta$,

$$
\sigma_d\ \ge\ \frac{8\lambda R^2}{\pi D^2}\sqrt{\frac{hc}{\eta PT\lambda}}
$$

which is proportional to $R^2$ (one factor of $R$ from converting angle to length, and another from the number of photons decreasing as $R^{-2}$). Keeping the same precision requires extending the observation time in proportion to $R^4$. Distance does not make distinction impossible; it rapidly increases the resources needed. However, what corresponds to "distinction" in this essay is not the estimation of a separation (where it is known that there are two sources and the separation is sought; the quantum Cramér–Rao bound) but the discrimination of one source from two (deciding which state it is; the quantum Chernoff bound).

**(5) The limit on discrimination.** Because the state of a single source $\rho_0=\lvert\psi_0\rangle\langle\psi_0\rvert$ is pure, the quantum Chernoff exponent [7] is determined by the minimum of $Q(t)=\operatorname{Tr}(\rho_0^t\rho^{1-t})=\langle\psi_0\vert\rho^{1-t}\vert\psi_0\rangle$ ($0\le t\le1$). Because the eigenvalues $r$ of $\rho$ satisfy $0\le r\le1$, $r^{1-t}\ge r$, and the minimum is attained as $t\to0$. Computing the overlap for $\lvert\psi_0\rangle$ uniform within a circle of diameter $D$ gives

$$
\xi_Q=-\ln p_0,\qquad p_0=\left[\frac{2J_1(v)}{v}\right]^2,\qquad v=\frac{\pi D\theta}{2\lambda}
$$

($J_1$ is the Bessel function of the first kind of order 1). For small separations $p_0\simeq1-v^2/4$, and

$$
\xi_Q\ \simeq\ \frac{F_Q\theta^2}{4}=\frac{\pi^2D^2\theta^2}{16\lambda^2}
$$

$1-p_0$ is the probability that a single photon leaves the state of the central source, and is proportional to $\theta^2$. A projective measurement that separates the light into the fundamental mode and the rest attains the exponent $-\ln p_0$ [6], and for small separations $-\ln p_0\simeq1-p_0$. In ordinary imaging, which looks only at the intensity distribution, the distinguishability is proportional to $\theta^4$.

When one source is to be told from two with equal prior probabilities and the number of detected photons $N_{\mathrm{det}}$ is fixed, the minimum error probability lies in the range

$$
\frac{1-\sqrt{1-e^{-N_{\mathrm{det}}\xi_Q}}}{2}\ \le\ P_e\ \le\ \frac12e^{-N_{\mathrm{det}}\xi_Q}
$$

The right side follows from the quantum Chernoff bound [7], and the left side from the lower bound by the fidelity. If $N_{\mathrm{det}}\xi_Q\ll1$, then $P_e\approx1/2$ and the two cannot be distinguished; if $N_{\mathrm{det}}\xi_Q\ge\ln10\approx2.3$, then $P_e\le0.05$. When the photons are spread over many independent modes and the mean photon number per mode is sufficiently small, the number of detected photons can be approximated by a Poisson distribution, and averaging gives $\frac12\exp[-\bar N(1-e^{-\xi_Q})]$ for the upper side. For small $\xi_Q$ this is nearly the same as $\frac12e^{-\bar N\xi_Q}$. Because the function on the left side is convex, the lower bound with $N_{\mathrm{det}}$ replaced by $\bar N$ also holds. The treatment of the limit in which fewer than one photon arrives on average is given in [Appendix 2, Section 10.6 (2)](appendix2.en.html).

**(6) The cosmological case.** In an expanding universe, the number of photons becomes $\bar N\propto1/[d_M^2(1+z)]$, the angular separation $\theta=s/d_A$ ($d_A=d_M/(1+z)$), and the observed wavelength $\lambda_{\mathrm{obs}}=(1+z)\lambda_e$ ($s$ is the proper separation at the time of emission, $\lambda_e$ the emitted wavelength, and $d_M$ the comoving distance). The source's wavelength band is taken to be narrow, and its emission is taken not to change during the observation. Because $d_A\lambda_{\mathrm{obs}}=d_M\lambda_e$, the two effects of redshift cancel, and

$$
\bar N=\frac{\eta PTD^2\lambda_e}{16hc\,d_M^2(1+z)},\qquad
\bar N\xi_Q\simeq\frac{\pi^2\eta PTD^4s^2}{256\,hc\,\lambda_e\,d_M^4(1+z)}
$$

This is the coefficient of the proportionality $\bar N\xi_Q\propto PTD^4s^2/[d_M^4(1+z)]$ in Section 3.1 of the main text. Because $d_M$ levels off at about 14 Gpc, at very large distances $\bar N\xi_Q$ decreases in proportion to $1/(1+z)$. In a model that uses only unscattered photons, the optical depth $\tau$ multiplies $\bar N\xi_Q$ by $e^{-\tau}$ ((a) in Section 3.1 of the main text). If scattered light mixes in as a background, the situation can become worse. On the other hand, scattered light can also carry information (as with the polarization of the CMB), and a general limit including scattered light is not determined by this formula alone.

**(7) Correspondence with the three phases.** What this calculation shows is the limit of the Spacetime-Limit Phase, in which, with the spacetime framework preserved, states cannot be distinguished with finite resources. Like $\kappa_i$ in [Appendix 1, Section 2.1](appendix1.en.html), $\xi_Q\simeq F_Q\theta^2/4$ corresponds to the product of the information obtained from a single photon and the square of the required resolution, and $N_{\max}\xi_Q\ll1$ is a concrete example of $N_{\max}\kappa_i\ll1$ in Section 4.2 of the main text. However, $\xi_Q$ is an exponent for discriminating two particular states, while $\kappa_i$ is a dimensionless eigenvalue of the quantum Fisher information matrix; in general they are not equal.

## 4. Is the Information of a Single Photon Lost During Propagation?

$\bar N\xi_Q$ in Section 3 decreases with distance, but in this model, with angle, wavelength, and aperture fixed, distance acts only through the number of arriving photons and the angular separation; $\xi_Q$ per photon is set only by the angle and $D/\lambda$ and does not depend on the length of the path the light has traveled. The observation time needed increases rapidly, but within the upper limits on resources it can be made up for. In general, a known, lossless propagation that does not depend on the compared parameters preserves the quantum Fisher information of the whole propagating field. On the other hand, the same conclusion does not hold directly for observable states restricted to a finite aperture or conditioned on detection (the discrimination exponent of Section 3 for a fixed physical separation changes with distance). What this section asks is whether there are mechanisms by which the information of the propagating light itself is lost while it travels.

**(1) The Fresnel zone.** In the path integral, the paths within a tube of radius $r_F=\sqrt{\lambda L}$ around the straight line (the Fresnel zone) contribute mainly, and this tube widens with distance $L$. If the aperture has an upper limit $D_{\max}$, the length that can be distinguished on the source side is about $\lambda L/D_{\max}$, coarsening in proportion to distance. This, however, is a disadvantage of angle and photon number, as in Section 3; it does not mean that the information of a single photon is lost along the way.

**(2) Dispersion in a medium.** Consider distinguishing two photons emitted from the same place with a time difference $\delta t$ by their arrival times (deciding whether a photon was emitted earlier or later). In vacuum, in non-dispersive propagation in the same spatial mode, a long travel time alone does not broaden the temporal waveform. With plasma along the way, lower-frequency light is delayed more. In cold, dilute plasma over a range in which cosmic expansion can be neglected, light of frequency $\nu$ is delayed, in proportion to the electron column density along the line of sight $\mathrm{DM}=\int_0^Ln_e(s)\,\mathrm{d}s$, by

$$
\Delta t_{\mathrm{DM}}(\nu)\simeq4.15\ \mathrm{ms}\times\frac{\mathrm{DM}}{\mathrm{pc\,cm^{-3}}}\left(\frac{\nu}{\mathrm{GHz}}\right)^{-2}
$$

[8]. For a narrow-band wave packet with central frequency $\nu_0$ and frequency standard deviation $\sigma_\nu$, $\sigma_{\mathrm{disp}}\simeq2\,\Delta t_{\mathrm{DM}}(\nu_0)\,\sigma_\nu/\nu_0$ is added to the width of the arrival times. If time and frequency are uncorrelated at emission, the medium does not change between the two emissions, absorption, scattering, and higher-order dispersion are neglected, and the dispersion is not compensated, the normal approximation gives

$$
\sigma_t^2=\sigma_0^2+\sigma_{\mathrm{disp}}^2+\sigma_{\mathrm{det}}^2,\qquad
P_e=1-\Phi\!\left(\frac{\delta t}{2\sigma_t}\right)
$$

($\sigma_0$ is the time width at emission, $\sigma_{\mathrm{det}}$ the timing error of the detector, and $P_e$ the minimum error probability of [Appendix 2, Section 1.1](appendix2.en.html)). Assuming $\mathrm{DM}=30\ \mathrm{pc\,cm^{-3}}$ and $\sigma_\nu/\nu_0=1\%$, radio waves at 1 GHz are delayed by about 124 ms with an added width of about 2.5 ms, and visible light at 500 nm is delayed by about 0.35 ps with an added width of about 7 fs (these are not measured values for a particular object). The time width and the frequency width are related by the Fourier relation ($\sigma_0\sigma_\nu\ge1/4\pi$) and cannot be chosen independently. Because the amount of electrons differs from one line of sight to another, it cannot be said that the situation worsens monotonically with distance alone, and at cosmological distances the calculation must be redone including the redshift along the way. When there is a scattering tail, the normal distribution is not assumed, and $P_e=\frac12\int\min\lbrace p(t),p(t-\delta t)\rbrace\,\mathrm{d}t$ is computed from the distribution of arrival times $p(t)$.

When only arrival times are measured, the Fisher information about the emission time is $1/\sigma_t^2$, which decreases as dispersion broadens the width. On the other hand, a known, lossless and noiseless dispersion that does not depend on the compared emission times is a unitary change that alters the phase at each frequency. Because parameter-independent unitary changes do not change the quantum Fisher information, the quantum Fisher information about the emission time is the same as before the dispersion. Indeed, radio pulsar observations use processing that removes the dispersion from the data (coherent dedispersion) [8]. This conclusion has the following conditions.

1. Only known, lossless, noiseless unitary dispersion that does not depend on the compared emission times can be compensated. Information carried off by scattering, absorption, or undetected light does not return even if DM is known.
2. If frequency resolution or dispersion compensation is among the means available to the observer ([Appendix 1, Section 1.1](appendix1.en.html)), "hard to distinguish by arrival times alone" cannot be called "indistinguishable by every means".
3. A finite time width has positive sensitivity to the central time. Broadening of the width alone does not show a drop in the rank of the quantum Fisher information matrix or the loss of means of observation that distinguish spacetime differences.
4. Dispersion differs from the "replacement by a state carrying no difference" caused by scattering. DM cannot be substituted for $\tau$ in $D_{AB}\le e^{-\tau}$ of the main text.

Under cosmic expansion alone, both the time difference between the two emissions and the width of the wave packet are stretched by a factor $(1+z)$, so when the timing error of the detector is negligible, the ratio $\delta t/\sigma_t$ does not change. Time dilation alone cannot be the basis for difficulty of distinction in the time direction.

**(3) Spacetime fluctuations.** There is a proposal that quantum fluctuations of spacetime accumulate with the distance light travels ([Main text, Section 2.1](zerothOrderPhase.en.html)). Their effect depends on the spatial and temporal correlations of the phase disturbance. A phase common to all photons is not observable, while a disturbance with short correlation across the aperture broadens the point image (in that case, enlarging the aperture does not improve the resolution). In discriminating two hypotheses for which independent samples can be obtained, as long as the two states after propagation differ and $\xi_Q>0$, increasing the number of samples lowers the error probability. What cannot be made up for by adding samples is the case in which the two states after propagation coincide, which is different from interference disappearing. Resource limits and correlations between samples are treated separately. Observations of the blurring of the images of distant quasars strongly constrain simple models of fluctuations that accumulate with distance (the models in Section 2.1 of the main text).

**(4) Comparison of mechanisms.**

| Mechanism | Disadvantage with distance | Is the information of a single photon lost along the way? | Can it be made up for? |
|---|---|---|---|
| Angular diffraction limit (Section 2) | With the emitted wavelength and aperture fixed, the angular scale $\lambda_{\mathrm{obs}}/D$ grows with redshift; the length scale on the source side $\lambda_ed_M/D$ coarsens until $d_M$ levels off | No | By photon number, up to the resource limits |
| Discrimination of two point sources (Section 3) | The disadvantage grows because $\bar N\xi_Q\propto1/[d_M^4(1+z)]$ decreases | Not lost for the whole propagating field (start of Section 4) | By photon number and aperture, up to the resource limits |
| Fresnel zone ((1)) | The length resolution on the source side coarsens | No | By photon number, up to the resource limits |
| Dispersion in a medium ((2)) | The width of the arrival times grows with DM (depending on the line of sight) | Harder to distinguish by arrival times alone, but the quantum Fisher information does not change | A known, lossless dispersion can be compensated in principle |
| Spacetime fluctuations ((3)) | Grows (depending on the model) | Can be lost (if the proposal is correct; depending on the model) | Depends on the correlations of the phase disturbance and on whether the two states after propagation coincide |

## 5. Cosmic Variance and Fisher Information

The cosmic variance $\Delta C_\ell/C_\ell=\sqrt{2/(2\ell+1)}$ of (b) in Section 3.1 of the main text is the formula for full-sky observation of statistically isotropic, Gaussian fluctuations without noise. It is determined not by distance but by the angular scale (the multipole $\ell$), and its cause is that only one sky can be observed [9]. Cosmic variance and the Fisher information matrix for reading the cosmological parameters $\theta_i$ are different quantities; the latter is built with the former in the denominator.

$$
F_{ij}=\sum_\ell\frac{\partial_iC_\ell\,\partial_jC_\ell}{(\Delta C_\ell)^2},\qquad (\Delta C_\ell)^2=\frac{2C_\ell^2}{2\ell+1}
$$

For the same parameter sensitivity, an $\ell$ with larger variance has a smaller weight in $F$. Considering a single multipole, if the difference in $C_\ell$ between two cosmological models is smaller than the cosmic variance, that multipole alone hardly distinguishes them. The power to distinguish with all modes combined is set by the shape of the difference and the covariance, and combining many $\ell$ can make the models distinguishable. Because the distributions of the two models do not coincide, this is not strict indistinguishability. The main text treats it as an example in which distinctions become harder while the spacetime standards are preserved (the Spacetime-Limit Phase).

## 6. Status

| Content | Kind |
|---|---|
| The diffraction limit, the quantum Cramér–Rao bound, the quantum Chernoff bound and the lower bound by the fidelity, amplifier noise, the Bekenstein bound, the Margolus–Levitin bound, the dispersion delay in plasma, cosmic variance | Existing results [1–9] (each with its conditions of applicability) |
| Adopting upper limits on resources (Section 2) | A premise under the conditions of the cosmological model, observer, and apparatus configuration this essay assumes |
| The state of two point sources and its quantum Fisher information; the exponent of the optimal measurement (Section 3 (3), (5)) | Existing results [5, 6] rederived from the propagation of light |
| The cosmological substitution (Section 3 (6)) and the comparison in the table (Section 4 (4)) | Estimates under ideal conditions |
| The upper limit $R_{\max}$ on distinguishability and the correspondence with the three phases (Section 2 (3), Section 3 (7)) | Estimates and readings of this essay |
| The proposal that spacetime fluctuations accumulate (Section 4 (3)) | An existing hypothesis. The effect depends on the model of the phase disturbance. Simple accumulation models are strongly constrained by observation |

## References

1. C. M. Caves, "Quantum limits on noise in linear amplifiers," *Phys. Rev. D* **26**, 1817–1839 (1982).
2. D. Gottesman, T. Jennewein, S. Croke, "Longer-baseline telescopes using quantum repeaters," *Phys. Rev. Lett.* **109**, 070503 (2012).
3. J. D. Bekenstein, "Universal upper bound on the entropy-to-energy ratio for bounded systems," *Phys. Rev. D* **23**, 287–298 (1981).
4. N. Margolus, L. B. Levitin, "The maximum speed of dynamical evolution," *Physica D* **120**, 188–195 (1998).
5. M. Tsang, R. Nair, X.-M. Lu, "Quantum theory of superresolution for two incoherent optical point sources," *Phys. Rev. X* **6**, 031033 (2016).
6. X.-M. Lu, H. Krovi, R. Nair, S. Guha, J. H. Shapiro, "Quantum-optimal detection of one-versus-two incoherent optical sources with arbitrary separation," *npj Quantum Inf.* **4**, 64 (2018).
7. K. M. R. Audenaert, J. Calsamiglia, R. Muñoz-Tapia, E. Bagan, Ll. Masanes, A. Acín, F. Verstraete, "Discriminating states: the quantum Chernoff bound," *Phys. Rev. Lett.* **98**, 160501 (2007).
8. *Essential Radio Astronomy*, Chapter 6 "Pulsars," Section 6.2 "Pulsars and the Interstellar Medium," NRAO, <https://www.cv.nrao.edu/~sransom/web/Ch6.html> (Eqs. (6.45) and (6.46)).
9. L. Knox, "Determination of inflationary observables by cosmic microwave background anisotropy experiments," *Phys. Rev. D* **52**, 4307–4318 (1995).

[Back to the main text](zerothOrderPhase.en.html) / [Back to Appendix 3](appendix3.en.html)

---

**Author**: 5garashi.com Design Office  
**Last updated**: 2026-11-11 JST
