---
title: 観測限界と未分化の原点：量子測定から宇宙論へ至る認識論的思索
lang: ja
math: true
description: 量子測定から宇宙論まで、観測限界と区別不能性を考える試論。
---
<!--
  ファイル名 / File: zerothOrderPhase.md
  概要 / Description: 観測限界と未分化の原点 —— 量子測定から宇宙論へ至る認識論的思索 / Observation limits and the undifferentiated origin
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-10-28
  版 / Version: 1.0.1
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 観測限界と未分化の原点：量子測定から宇宙論へ至る認識論的思索
# Observation Limits and the Undifferentiated Origin: An Epistemological Inquiry from Quantum Measurement to Cosmology

**著者 / Author:** 5garashi.com設計事務所 / 5garashi.com Design Office

**日付 / Date:** 2026年10月28日 / October 28, 2026

---

## 序章：区別不能性という認識論的問い / Introduction: The Epistemological Question of Indistinguishability

遠方の対象を観測するとき、私たちが手にする情報は制限され、その位置や詳細な内部状態を識別することは次第に困難になる。本試論は、一見すると技術的な精度の問題に思える「測定の曖昧さ」を物理的・認識論的な探求の出発点とし、宇宙論の深淵へと至る思考実験（Gedankenexperiment）を展開するものである。

本稿では、次の立場を思索のガイドラインとして採用する。

> **「観測者が利用できるあらゆる観測手段をもってしても原理的に区別できないふたつの状態は、その観測者にとって同一の物理状態として扱う」**

本稿は、量子力学における測定限界のスケール感（第一段階）から出発する。その主題は、対象を区別できなくなることから、区別を支える時空や尺度そのものが成り立たなくなる第二段階へと思索を進めることにある。ミクロな局在の破綻、超高エネルギー散乱、そしてマクロな宇宙の創始と終焉へと視点を広げたとき、私たちはどのような「物理世界の境界」を目にすることになるだろうか。

---

## 1. 確率的識別限界と標準量子限界の描像 / Probabilistic Discrimination and the Standard Quantum Limit

物理状態の「区別しにくさ」を定式化するため、ふたつの状態 A, B から得られる観測結果の確率分布 $P_A(y)$, $P_B(y)$ を考える。両者の分布の重なりを表す古典的な統計指標である全変動距離（Total Variation Distance） $D_{AB}$ は次のように定義される [1]。

$$
D_{AB} = \frac{1}{2}\int \left|P_A(y)-P_B(y)\right|\,\mathrm{d}y,\qquad 0 \le D_{AB} \le 1
$$

$D_{AB} = 1$ は完全な識別可能性を意味し、$D_{AB} = 0$ はその測定では両者を区別できない（分布が完全に重なる）状態を表す [1]。

ここで、観測者から距離 d 離れた位置にある電子の位置を光子などの信号を用いて測定するトイモデルを想定してみよう。信号の往復時間 $\tau = \frac{2d}{c}$ の間に、自由電子の波束（位置と運動量に初期相関のない最小不確定ガウス波束）はシュレーディンガー方程式に従って空間的に拡散する。初期の広がりを $\sigma_0$ とすると、時間 τ 経過後の位置の不確定性（標準偏差） $\Delta x(\tau)$ は次式で与えられる。

$$
\Delta x(\tau) = \sqrt{\sigma_0^2 + \left(\frac{\hbar\tau}{2m\sigma_0}\right)^2}
$$

この式における $\frac{\hbar}{2\sigma_0}$ は、量子状態自身が持つ初期運動量の不確定性（標準偏差） $\Delta p$ に由来するものであり、時間経過とともに空間的な拡散として顕在化する。初期幅 $\sigma_0$ を最適化（$\sigma_0^2 = \frac{\hbar\tau}{2m}$）したときに得られる最小の不確定性スケールは、標準量子限界（SQL）と同等の形をとる [2]。

$$
\Delta x_{\min} \sim \sqrt{\frac{\hbar\tau}{m}} = \sqrt{\frac{2\hbar d}{mc}}
$$

ただし、この標準量子限界は特定の測定条件や相関のない初期波束を前提としたものであり、原理的に絶対破れない下限ではない（例えば、初期に位置と運動量に負の相関を持たせた「収縮状態」等を用いることでSQLを下回る精度を得る手法が知られている） [2]。

また、距離 d に対する相対誤差の比率 $\frac{\Delta x_{\min}}{d} \propto \frac{1}{\sqrt{d}}$ を評価すると、距離が大きくなるほど相対誤差自体は小さくなる。しかし、このスケール感は「観測という行為において情報がどのように空間的・時間的に広がり、曖昧さを帯びるか」を考える興味深い手がかりを与えてくれる。

---

## 2. 局在限界と時空描像の限界 / Localization Limits and the Limits of the Spacetime Picture

### 2.1 局在限界と時空の量子的揺らぎ
さらに極限を進めると、問題は粒子の位置をどこまで正確に定められるかという問いから、位置や距離を定義する時空そのものがどこまで意味を保てるかという問いへと移っていく。

この問題を考える手がかりとして、量子力学と一般相対論の関係から、局在化の限界を概算してみよう。量子力学の不確定性関係によれば、粒子の位置の不確定さを $\Delta x$ まで小さくしようとすると、運動量の不確定さは概ね

$$
\Delta p \sim \frac{\hbar}{\Delta x}
$$

となる。十分に高エネルギーの領域では、これに対応するエネルギーは

$$
E \sim c\,\Delta p \sim \frac{\hbar c}{\Delta x}
$$

と見積もられる。一方、一般相対論によれば、エネルギー E は、それに対応する重力的な長さの尺度（シュワルツシルト半径）

$$
r_s \sim \frac{2GE}{c^4}
$$

を持つ。ここに先ほどのエネルギーを代入すると、

$$
r_s \sim \frac{2G\hbar}{c^3\Delta x}
$$

となる。局在させようとする領域の大きさ $\Delta x$ が、この重力的な長さの尺度 $r_s$ と同程度になる条件を考えると、

$$
\Delta x \sim r_s \quad\Longrightarrow\quad \Delta x \sim \sqrt{2}\,l_P
$$

という関係が得られる。ここで、

$$
l_P = \sqrt{\frac{\hbar G}{c^3}} \approx 1.6 \times 10^{-35}\,\mathrm{m}
$$

はプランク長である。この概算は、極めて小さな領域を観測しようとするほど大きなエネルギーが必要となり、そのエネルギー自身の重力作用によって、測定しようとする領域の時空が大きく変化し得ることを示唆している [3]。

もちろん、これはプランク長が厳密な最小長さであることを証明するものではない [3]。しかし、プランクスケールでは量子力学と一般相対論の双方を考慮する必要が生じ、時空を連続的で滑らかな幾何学として扱う従来の描像が限界に達する可能性がある。

このような極限における時空の姿を表す概念の一つが、「時空の泡（Spacetime Foam）」である [4]。これは、プランクスケールでは時空の計量や幾何学的構造そのものが量子的な揺らぎを持ち、距離や曲率、さらには時空のトポロジーさえも古典的な意味で固定できなくなる可能性を表す概念である [4]。

ここで区別不能性の問題は、さらに一段深いものとなる。時空の幾何学そのものが明確でなくなり、位置や距離を定義する枠組みそのものが成立しなくなる極限が想定される。

### 2.2 高エネルギー粒子衝突における情報の分散と観測可能性
高エネルギー粒子衝突では、入射粒子のエネルギーが増大するにつれて、多数の粒子生成や複雑な相互作用が生じ、初期状態に関する情報が多様な自由度や粒子間相関へ分散する。実際の観測では全ての生成粒子や相関を完全に測定することは困難であり、観測可能な自由度に限定した部分系の記述が必要となる。

全体系の状態を $\rho(E)$、観測対象となる部分系の状態を

$$
\rho_{\mathrm{obs}}(E) = \operatorname{Tr}_{\mathrm{unobs}}\rho(E)
$$

とする。ここで E は衝突の重心系エネルギー、すなわち $E \equiv \sqrt{s}$ と定義する。また、$\operatorname{Tr}_{\mathrm{unobs}}$ は観測対象外の自由度を部分トレースによって取り除く操作を表す。

このような粗視化は、量子情報幾何学において、観測可能な部分系が保持するパラメータ識別能力に影響を与える。量子Fisher情報（Quantum Fisher Information, QFI） $F_Q(E)$ は、量子状態がパラメータ E の変化をどの程度識別できるかを定量化する指標である [5]。部分系への縮約によって、全体系が保持していた識別能力の一部が失われる可能性がある [5]。

エネルギー E に依存する量子状態の識別可能性は、Bures距離によって局所的に表現できる [5]。滑らかな量子状態族について、十分小さなエネルギー変化 dE に対して、

$$
\begin{aligned}
D_{\mathrm{Bures}}\!\left(\rho_{\mathrm{obs}}(E),\rho_{\mathrm{obs}}(E+\mathrm{d}E)\right)^2
&\approx \frac{1}{4}F_Q(E)\,(\mathrm{d}E)^2 + O\!\left((\mathrm{d}E)^3\right)
\end{aligned}
$$

が成り立つ [5]。観測可能な部分系のQFIが低下する場合には、その部分系における近接したエネルギー状態間の識別可能性も実効的に低下することになる（第一段階）。

さらにエネルギーを上げると、第2.1節で見た重力作用が探査そのものを制約する。本稿では、これを位置や距離による区別の枠組みが成り立たなくなる第二段階への入口と捉える。

---

## 3. 宇宙論的極限における区別不能性のイメージ / Indistinguishability at Cosmological Limits

ミクロな領域や高エネルギー衝突で見られた「境界線の曖昧化・情報の分散」というモチーフを、巨視的な宇宙論的スケールへと転じてみる。

### 3.1 過去の果てと極初期宇宙の一様性
遠方の天体を観測することは、光速の有限性を通じて過去の宇宙の姿を覗き込むことと同義である。私たちが望遠鏡で捉えることのできる最遠の光である「宇宙マイクロ波背景放射（CMB）」は、宇宙誕生から約38万年後の「宇宙の晴れ上がり（最終散乱面）」の情報を伝えている [6]。

CMBは全天で約 $10^{-5}$ という極めて高い均一性を示している [6]。この微小なゆらぎこそが後の銀河や大構造の種となる「識別可能な構造情報」であるが、時空をさらに過去（$t \to 0$）へ遡る思考実験を行うと、特異点近傍では古典的な時空を記述する枠組みそのものが成り立たなくなる（第二段階） [3]。

### 3.2 時間方向の極限 ($t \to +\infty$) と宇宙の終焉
一方、時間軸の未来方向（$t \to +\infty$）へ目を向けると、宇宙は膨張を続け、星の燃え尽きやブラックホールの蒸発を経て、利用可能な有効自由エネルギーが極限まで枯渇した熱死（Big Freeze）へと向かうシナリオが提示されている [7]。

ロジャー・ペンローズ（Roger Penrose）が提唱する共形サイクリック宇宙論（Conformal Cyclic Cosmology: CCC）は、この遠い未来において電子などの残存粒子が最終的に静止質量の意味を失い、宇宙がスケール不変性を獲得する極限を考察している [8]。この描像では、違いを長さや時間で表す尺度そのものが意味を失う（第二段階）。ただし、共形構造や因果構造は残る。CCCは、質量とスケールを失った遠い未来の共形幾何学的構造が、次の宇宙の創始（ビッグバン特異点）の構造と平滑に接続され得るとする、極めて魅力的な仮説である [8]。

---

## 4. 四つの極限と「未分化の第零次相」という提案 / Four Limits and the Proposed "Zeroth-Order Phase"

### 4.1 四つの極限
ここまで論じてきた四つの極限的状況を並べてみよう。

1. **宇宙の最初期 ($t \to 0$):** 特異点近傍において、古典的な時空記述そのものが成り立たなくなる領域。
2. **宇宙の遠い未来 ($t \to +\infty$):** 熱死を経て、CCCの描像では長さや時間の尺度そのものが意味を失う極限。
3. **ミクロな局在限界 ($\Delta x \to 0$):** 位置の局在を突き詰めると、プランクスケールで時空の幾何学的描像の限界に至る領域。
4. **高エネルギー散乱極限 ($E = \sqrt{s} \to \infty$):** 多体生成と情報の分散、および重力反作用による分解能の限界が問われる領域。

これらの極限は、物理的なメカニズムもスケールも異なるが、いずれも「何かを何かとして区別するための境界が、どこまで成立するのか」という共通の問いを浮かび上がらせる。

### 4.2 区別不能性の二つの段階
本稿では、区別不能性に二つの異なる段階を見出す。

**第一は、観測量の代数（観測者が利用できる観測量の集まり）は定義できるが、その範囲では区別がつかなくなる段階である。** 粒子の個体性が曖昧になったり、多体相互作用によって情報が多数の自由度へ分散し、個々の状態を識別しにくくなったりする場合がこれに当たる。

**第二は、位置・距離・時間など、対象を区別する基準そのものが、従来の意味では成り立たなくなる段階である。** 観測量を時空領域に割り当てる構造が従来の意味では定義できなくなり、対象が「どこにあるのか」「何からどれほど離れているのか」を判断する基盤そのものが揺らぐ。

ここで重要な点として、**第二段階は従来の時空に観測量を割り当てる枠組みの内部では記述できない。** 操作的立場は観測量の代数が与えられていることを前提としているため [13]、第二段階はこの立場の適用限界を示す概念として位置づけられる。

### 4.3 「未分化の第零次相」という仮称
本稿では、対象の個別性だけでなく、それを区別するための基準や枠組みまでもが意味を失っていく第二段階の極限を、思考実験上の概念として「**未分化の第零次相（Zeroth-Order Phase）**」と仮称する。

四つの極限は、それぞれ異なる経路を通じて第二段階へ接続し得る。

```text
・【宇宙の最初期 (t → 0)】
・【宇宙の遠い未来 (t → +∞)】
・【ミクロ局在限界 (Δx → 0)】 (プランクスケール)
・【高エネルギー散乱極限 (E → ∞)】 (多体分散・重力反作用)
  ↓
[ 未分化の第零次相 (Zeroth-Order Phase) ]
```

これらは同一の物理状態を意味するものではない。しかし、「何が区別されるのか」、そして「何をもって区別するのか」という二つの問いを通じて、概念的につながっている。

### 4.4 ミクロとマクロを結ぶ既存の足場
ミクロとマクロの結びつきについては、既存の理論にいくつか手がかりが存在する。

**(1) 紫外と赤外の関係。** 小さな領域を調べるほど大きなエネルギーが必要となり、重力が無視できなくなるという論法を領域の大きさ L と場の理論の紫外カットオフ Λ の関係に適用したのが Cohen, Kaplan, Nelson の議論である [10]。

$$
L^3\Lambda^4 \le L M_P^2
$$

ミクロな側の限界（紫外）が、マクロな側の大きさ（赤外）と一つの式で結ばれている [10]。

**(2) 区別できる状態の数の上限。** ホログラフィック原理（Bousso の限界）は、適切な条件のもとで領域に対応するエントロピーが境界面積によって制限されることを示唆する [11]。

$$
S \le \frac{A}{4l_P^2}
$$

状態数の上限として $N \le \exp\!\left(\frac{A}{4l_P^2}\right)$ が導かれる [11]。

**(3) 宇宙論的地平線のエントロピー。** ド・ジッター空間の地平線には、Gibbons と Hawking によって $S = \frac{A}{4l_P^2}$ というエントロピーが対応づけられている [12]。

これらは、区別可能性の限界を定量的に議論するための既存の足場として位置づけられるものである [11, 12]。

---

## 5. 結論と展望：存在意義としての問い / Conclusion: The Inquiry as a Purpose

電子の位置測定や高エネルギー散乱という素朴なトイモデルから始まった本稿の試みは、厳密な定量予測を提示する論文ではなく、「観測可能性」という認識論的枠組みを通じて物理世界を眺め直す思考実験である [1, 9]。

もちろん、観測可能宇宙の境界や事象地平線の存在、あるいはミクロな量子力学の数式を、そのまま宇宙全体へ単純外挿することはできない [9]。現在見えないこと（観測不可能性）と、原理的に状態が存在しないことや区別がつかないことは厳密に区別されるべきである [9]。

本試論が問いかけるのは、物理的な対象がどこまで区別できるかという問題だけではない。対象を区別するための基準そのものは、どこまで成立し得るのか。そして、その基準さえ意味を失う極限を、私たちはどのように考えることができるのか、という問題である。

「境界線はいかにして生まれ、いかにして消失するのか」——この問いを抱え続けること自体が、理論物理学と哲学の境界領域における思考実験の存在意義であると言えるだろう。

---

## 参考文献 / References

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

**作成者 / Author**: 5garashi.com設計事務所 / 5garashi.com Design Office
**最終更新 / Last updated**: 2026-10-31 JST
