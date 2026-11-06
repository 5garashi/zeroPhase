---
title: 付録2：観測限界と識別可能性の数式解説
lang: ja
math: true
appendix: true
translation: /appendix2.en.html
description: 全変動距離、自由波束、SQL型見積もり、プランク尺度、部分トレース、トレース距離、QFIの単調性、非可換座標、エントロピー限界の意味と導出を解説する。
---
<!--
  ファイル名 / File: appendix2.md
  概要 / Description: 観測限界と識別可能性を考える数式の意味・導出・適用条件
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-11-04
  最終更新 / Last updated: 2026-11-06 JST
  版 / Version: 2.0.0
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 付録2：観測限界と識別可能性の数式解説

**著者 / Author:** 5garashi.com設計事務所 / 5garashi.com Design Office

**版:** <span data-version>2.0.0</span>　**更新日:** 2026-11-06 JST

本付録は、本文で用いた観測限界・識別可能性に関する数式の導出と適用条件を整理する。

[本文：観測限界と未分化の原点](zerothOrderPhase.html) / [付録1：論理的背景](appendix1.html)

## 0. 本試論で用いる統計・量子情報指標の一覧

| 指標名 | 数式表記 | 適用領域 | 識別不能の条件 |
|---|---|---|---|
| **全変動距離 (TV Distance)** | $D_{AB} = \frac{1}{2}\int \vert P_A(y)-P_B(y)\vert\,\mathrm{d}y$ | 古典確率密度分布 | $D_{AB} = 0$ |
| **トレース距離 (Trace Distance)** | $T(\rho_A, \rho_B) = \frac{1}{2}\Vert\rho_A - \rho_B\Vert_1$ | 量子状態（密度行列） | $T = 0$ （最適成功確率 $p_{\mathrm{succ}} = 1/2$） |
| **Bures距離** | $D_{\mathrm{Bures}}^2 \approx \frac{1}{4}F_Q(E)(\mathrm{d}E)^2$ | 量子状態のパラメトリック変化 | $F_Q(E) = 0$ （その点で、一次の変化が読み取れない） |

---

## 1. 全変動距離：測定結果の識別度

確率密度 $P_A(y), P_B(y)$ の全変動距離は $0 \le D_{AB} \le 1$ の範囲をとり、$D_{AB}=1$ で完全識別可能、$D_{AB}=0$ で指定した測定における識別不能を表す。特定の測定で $D_{AB}=0$ となっても、別の測定で区別できる場合がある。量子状態としての識別不能は、利用できる測定の全体（付録1 第1.1節の $\mathcal A_O$）を指定して論じる。

## 2. 自由ガウス波束の広がり

質量 $m$ の非相対論的自由粒子で、初期幅 $\sigma_0$、位置と運動量に初期相関のない最小不確定ガウス波束の位置標準偏差 $\Delta x(\tau)$ は次式となる。

$$
\Delta x(\tau)=\sqrt{\sigma_0^2+\left(\frac{\hbar\tau}{2m\sigma_0}\right)^2}
$$

### 導出

1. 初期運動量の標準偏差：$\Delta p = \hbar / (2\sigma_0)$
2. 自由粒子の速度の標準偏差：$\Delta v = \Delta p / m = \hbar / (2m\sigma_0)$
3. 初期相関がないときの分散の和：$\Delta x^2(\tau) = \sigma_0^2 + (\Delta v\, \tau)^2$

初期相関がある場合は共分散の項が加わるため、この式をそのまま用いることはできない。

## 3. SQL型の最小位置幅

時間 $\tau$ について $\sigma_0$ を最適化する（$\frac{\mathrm{d}}{\mathrm{d}\sigma_0}\Delta x^2(\tau) = 0$）。観測者から距離 $d$ 離れた粒子へ、平坦時空で信号を往復させる時間を $\tau = 2d/c$ と置く。

$$
\sigma_0^2 = \frac{\hbar\tau}{2m} \quad\Longrightarrow\quad \Delta x_{\min} = \sqrt{\frac{\hbar\tau}{m}} = \sqrt{\frac{2\hbar d}{mc}}
$$

自由質量の位置を監視する標準量子限界（SQL）は、係数を除いて同じ形（$\sqrt{\hbar\tau/m}$ に比例する形）を持つ [1]。ここで求めたのは、初期相関のない状態族の位置標準偏差の最小値であり、検出器雑音や測定反作用を含めた測距誤差全体ではない。初期に負の位置・運動量相関を持つ収縮状態では、この値を下回れる [2]。

## 4. プランク長：局在と重力反作用の交差

1. 局在に伴う運動量：$\Delta p \sim \hbar / \Delta x$
2. 高エネルギー近似：$E \sim c\Delta p \sim \hbar c / \Delta x$
3. シュワルツシルト半径：$r_s = \frac{2GE}{c^4} \sim \frac{2G\hbar}{c^3\Delta x}$
4. $\Delta x \sim r_s$ より：$\Delta x^2 \sim \frac{2G\hbar}{c^3} = 2 l_P^2 \;\Longrightarrow\; \Delta x \sim \sqrt{2}\, l_P$

係数 $\sqrt2$ はこの概算で採用した関係に由来し、普遍的な最小長さの厳密な係数ではない。プランク時間 $t_P=l_P/c=\sqrt{\hbar G/c^5}$ も、量子重力を考える尺度として位置づける。

---

## 5. 部分トレースとトレース距離

観測できない自由度を除いた部分系 $\rho_{\mathrm{obs}} = \operatorname{Tr}_{\mathrm{unobs}}\rho$ について、二つの状態のトレース距離を

$$
T(\rho_A,\rho_B)=\frac{1}{2}\Vert\rho_A-\rho_B\Vert_1
$$

と定める。$\Vert\cdot\Vert_1$ はトレースノルムで、密度行列の差のようなエルミート行列では固有値の絶対値の和になる。等事前確率で二状態のいずれかを単一試行で識別するとき、利用できる全測定について最適化した成功確率は

$$
p_{\mathrm{succ}} = \frac{1+T}{2}
$$

である [3]。$T=0$ なら最適な成功確率も $1/2$ となり、その部分系では識別できない。

### 5.1 部分トレースとQFIの単調性

観測できない自由度を捨てる操作（部分トレースを含む、物理的に許される写像）では、量子Fisher情報は増えない [4, 5]。

$$
F_Q\!\left[\operatorname{Tr}_{\mathrm{unobs}}\rho(E)\right] \;\le\; F_Q\!\left[\rho(E)\right]
$$

比べるのは同じパラメータ値での全体系と部分系である。本文第2.2節の議論は、この不等式を確かな足場として、エネルギーとともに右辺と左辺の差が広がる状況を考える。

## 6. 二準位系重ね合わせのトイモデル

2つの2準位系において、全体系の純粋状態を以下のように置く。

$$
\vert \Psi_\pm\rangle = \frac{\vert 0\rangle_1\vert 0\rangle_2 \pm \vert 1\rangle_1\vert \chi_\theta\rangle_2}{\sqrt{2}}, \qquad \vert \chi_\theta\rangle_2 = \cos\theta\vert 0\rangle + \sin\theta\vert 1\rangle
$$

## 7. トイモデルにおけるトレース距離の導出

系2を部分トレースした系1の密度行列：

$$
\rho_{1,\pm} = \operatorname{Tr}_2 \vert \Psi_\pm\rangle\langle\Psi_\pm\vert = \frac{1}{2} \begin{pmatrix} 1 & \pm\cos\theta \\ \pm\cos\theta & 1 \end{pmatrix}
$$

密度行列の差：

$$
\rho_{1,+} - \rho_{1,-} = \begin{pmatrix} 0 & \cos\theta \\ \cos\theta & 0 \end{pmatrix}
$$

固有値は $\pm \cos\theta$ であるため、トレース距離は以下となる。

$$
T(\rho_{1,+}, \rho_{1,-}) = \frac{1}{2}\left(\vert \cos\theta\vert  + \vert -\cos\theta\vert \right) = \cos\theta \qquad \left(0 \le \theta \le \frac{\pi}{2}\right)
$$

$\theta \to \pi/2$ において、系1だけを測る観測者にとって $T \to 0$（識別不能）となるが、全体系では $\langle\Psi_+\vert \Psi_-\rangle = 0$ であり完全識別可能である。

---

## 8. 非可換座標・CKN限界・ホログラフィック限界

### 8.1 非可換座標

非可換座標のモデルでは、二つの座標演算子が交換しない関係を仮定する。

$$
[x_i,x_j]=i\theta_{ij}
$$

$[x_i,x_j]=x_ix_j-x_jx_i$ は交換子、$\theta_{ij}$ は非可換性を表すパラメータで、座標を長さとして表すモデルでは長さの二乗の次元を持つ。異なる方向の座標を同時に鋭く定められないため、点や鋭い境界を前提にした古典的な幾何学をそのまま適用できるかを考える手がかりとなる。

### 8.2 CKNスケーリング

Cohen–Kaplan–Nelson の議論は、領域の大きさと有効場理論の紫外カットオフを、重力的な整合条件で結ぶ [6]。

$$
L^3\Lambda^4\lesssim L M_P^2
$$

自然単位系 $c=\hbar=1$ を用いる。$L$ は領域の代表長さ、$\Lambda$ は紫外カットオフ、$M_P$ はプランク質量の尺度である。左辺はカットオフに対応するエネルギー密度 $\sim\Lambda^4$ を体積 $L^3$ に掛けたエネルギー、右辺は同じ大きさのブラックホールの質量の尺度を表す。係数はプランク質量の規約などに依存するため、スケーリングとして読む。

### 8.3 ホログラフィックなエントロピー限界

$$
\frac{S}{k_B}\le\frac{A}{4l_P^2}
$$

$S$ はエントロピー、$k_B$ はボルツマン定数、$A$ は関係する境界面の面積である。本文の $S\le A/(4l_P^2)$ は、エントロピーを $k_B$ を単位として無次元で表す記法である。共変エントロピー限界は、面積 $A$ の面に付随する適切なライトシート上のエントロピーを扱う [7]。状態数として読むときは、$N$ 個の状態の等確率混合について $S=k_B\ln N$ と数え、$N\le\exp[A/(4l_P^2)]$ と表す。ビット数なら、無次元エントロピーをさらに $\ln2$ で割る。

---

## 9. 五つの極限領域と三相モデルの対応

本文の四つの極限に、極小時間分割（$\Delta t\to0$）を独立した検討方向として加えた比較である。各列は付録1の三相モデルに基づく整理であり、「第零次相との接続」の列は本試論の仮説を表す。

| 極限領域 | 時空限界相を考える手がかり | 次元縮減相を考える手がかり | 第零次相との接続 |
|---|---|---|---|
| **最初期（$t\to0$）** | 初期揺らぎの測定 | 量子重力効果と自由度の変容 | 古典的時空記述の限界より先への接続 |
| **遠い未来（$t\to+\infty$）** | 宇宙論的な平衡化 | CCCの共形的な再記述 | 尺度基準の不成立への接続 |
| **局在限界（$\Delta x\to0$）** | 局在の精度と測定反作用 | 非可換幾何学、スペクトル次元 | 局在の概念の限界への接続 |
| **極小時間（$\Delta t\to0$）** | 量子ゼノン効果（遷移の抑制であり、識別不能そのものではない） | 時間測定条件の変容 | 時計や時間順序の基準の不成立への接続 |
| **高エネルギー（$E\to\infty$）** | 部分系のトレース距離、QFIの低下 | CKN・エントロピー限界 | 時空や相空間の識別基準の不成立への接続 |

## 参考文献

1. V. B. Braginsky, F. Ya. Khalili, *Quantum Measurement*, ed. K. S. Thorne (Cambridge University Press, 1992).
2. H. P. Yuen, "Contractive States and the Standard Quantum Limit for Monitoring Free-Mass Positions," Physical Review Letters 51, 719 (1983). [論文](https://doi.org/10.1103/PhysRevLett.51.719)
3. P. Hayden, K. Milner, M. M. Wilde, "Quantum Interactive Proofs and the Complexity of Separability Testing," Theory of Computing 11 (2015), 201–232. [論文](https://theoryofcomputing.org/articles/v011a003/)
4. S. L. Braunstein, C. M. Caves, "Statistical distance and the geometry of quantum states," Physical Review Letters 72, 3439 (1994). [論文](https://doi.org/10.1103/PhysRevLett.72.3439)
5. J. Liu, H. Yuan, X.-M. Lu, X. Wang, "Quantum Fisher information matrix and multiparameter estimation," J. Phys. A: Math. Theor. 53, 023001 (2020). [論文](https://arxiv.org/abs/1907.08037)
6. A. G. Cohen, D. B. Kaplan, A. E. Nelson, "Effective Field Theory, Black Holes, and the Cosmological Constant" (1999). [論文](https://arxiv.org/abs/hep-th/9803132)
7. R. Bousso, "A Covariant Entropy Conjecture" (1999). [論文](https://arxiv.org/abs/hep-th/9905177)

[本文へ戻る](zerothOrderPhase.html) / [付録1へ戻る](appendix1.html)

---

**作成者 / Author**: 5garashi.com設計事務所 / 5garashi.com Design Office  
**最終更新 / Last updated**: 2026-11-06 JST
