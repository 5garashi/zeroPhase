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
  最終更新 / Last updated: 2026-11-08 JST
  版 / Version: 2.1.0
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 付録2：観測限界と識別可能性の数式解説

**著者 / Author:** 5garashi.com設計事務所 / 5garashi.com Design Office

**版:** <span data-version>2.1.0</span>　**更新日:** 2026-11-08 JST

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

## 10. 遠方の識別を資源の限界まで押し進めた見積もり

本文 第3.1節の遠方の二光源の量子識別限界に、観測者が原理的に使える最大の資源を代入すると、どこまで見分けられるかを見積もる。次の三つを本試論の原理として置く。(1) 観測時間には上限 $T_{\max}$ がある。(2) 口径の大きさには上限がある。(3) 測定の精度は、測定に使う光子1個では波長（エネルギー）で決まり、$N$ 個の光子を使うと $\sqrt N$ 倍まで良くなる。装置も宇宙の中の物であり、同じ種類の限界に従うことを順に入れていく。以下は、光源を固定した例での桁の見積もりであり、本試論の推定として扱う（第10.6節）。

例として、太陽と同じ光度の光源（寿命 $t_{\mathrm{life}}=10^{10}$ 年、光が出た時の波長 $\lambda_e=500$ nm、一生に出す光子の数 $N_{\mathrm{emit}}\approx3\times10^{62}$）を考え、検出の効率は $\eta=1$ とする。観測する波長は $\lambda_{\mathrm{obs}}=(1+z)\lambda_e$ である。この光源は桁を示すための例であり、各時代に実在する光源を表すものではない。距離は本文と同じ平坦なΛCDM（Planck 2018）で求める。

### 10.1 光子の数で決まる限界と、観測時間の上限

観測時間 $T$ の間に届く光子の数は、光源が一生に出す光子の数に、口径が受ける割合と、その時間に届く割合を掛けたものと見積もる。光源の光は、届くまでに $(1+z)$ 倍の時間に引き延ばされるため、$T$ が $(1+z)\,t_{\mathrm{life}}$ より短いとき、届く割合は $T/[(1+z)\,t_{\mathrm{life}}]$ である。本文の式は

$$
\bar N\xi_Q=\frac{\pi^2\eta\,N_{\mathrm{emit}}\,D^4s^2}{256\,\lambda_e^2\,d_M^4}\cdot\frac{T}{(1+z)\,t_{\mathrm{life}}}
$$

となり、$\bar N\xi_Q=\ln10$ から、見分けられる最小の間隔は

$$
s_{\mathrm{ph}}=\frac{16\lambda_e d_M^2}{\pi D^2}\sqrt{\frac{\ln10}{\eta N_{\mathrm{emit}}}\cdot\frac{(1+z)\,t_{\mathrm{life}}}{T}}
$$

である（$T$ が $(1+z)\,t_{\mathrm{life}}$ より長いときは、最後の比を 1 とする）。

観測時間の上限 $T_{\max}$ は、本試論が置く原理である。動機として、加速膨張する宇宙では、観測者が回収できるエネルギーと情報の総量が有限だとする議論がある [14]。ただし、これは望遠鏡1台の観測時間を直接限るものではない。$T_{\max}$ を置くと、$(1+z)$ には上限がないため、固定した光源の例では、十分に遠い（過去の）光源で、受け取れる光子は $(1+z)$ に反比例して減る。

### 10.2 口径の大きさの上限

観測時間の上限を置かずに光源の一生の光をすべて受け（$T\ge(1+z)\,t_{\mathrm{life}}$）、口径の直径を宇宙定数で決まる事象の地平線の半径 $r_H=c/H_\Lambda\approx5.4$ Gpc まで大きくすると（$D=r_H$）、最も遠い所（$d_M\approx14$ Gpc）でも $s_{\mathrm{ph}}\approx1.5\times10^{-36}$ m となり、プランク長を下回る。しかし、この大きさの装置は宇宙の膨張で引き裂かれる。宇宙定数 $\Lambda$ のもとで、質量 $M$ の束縛された構造の転回半径には上限

$$
R_{\max}=\left(\frac{3GM}{\Lambda c^2}\right)^{1/3}
$$

があり [8]、束縛された構造の大きさの目安になる。束縛されていない物は遠ざかるため、集められる質量も、観測者の属する束縛された構造（局所銀河群、太陽の約 $2\times10^{12}$ 倍）に限られる。宇宙定数の限界が、質量と口径に二重に効く。このとき $R_{\max}\approx1.4$ Mpc で、口径の直径を桁の目安として $D=2R_{\max}\approx2.8$ Mpc（$8.7\times10^{22}$ m）とする。転回半径は束縛が破れる境目の大きさであり、安定に保てる大きさはこれより小さい。また、局所銀河群の質量の大半は暗黒物質で、装置には使えない。そのため $D$ は大きめの見積もりであり、実際に達する $s_{\mathrm{ph}}$ は第10.5節の表の値より大きい。この $D$ で、$s_{\mathrm{ph}}$ は距離によって $10^{-33}$〜$10^{-24}$ m 程度となる（第10.5節の表）。

### 10.3 測定の精度は光子の波長で決まる

最適な測定（光を空間のモードに分ける測定）は、測定の軸を光の中心に、見分けたい角度の間隔より細かく合わせる必要がある。軸がずれると、小さい間隔では回折の限界に戻る [9]。

**(1) 光子1個で決まる方向の精度。** 光子が口径に入る横方向の位置は口径の幅の中に限られ、そのばらつきは $\Delta x\lesssim D/2$ である。運動量 $p=h/\lambda_{\mathrm{obs}}$ の光子の到来方向が $\Delta\theta$ ばらつくと、横方向の運動量は $\Delta p_\perp=p\,\Delta\theta$ ばらつく。位置と運動量の不確定性関係 $\Delta x\,\Delta p_\perp\ge\hbar/2$ から、

$$
\Delta\theta\gtrsim\frac{\hbar}{pD}=\frac{\lambda_{\mathrm{obs}}}{2\pi D}
$$

となる。これは回折の限界と同じ形であり、本文 第4.2節の、光子1個から得られる方向の量子Fisher情報が $(2\pi D/\lambda)^2$ を超えないことと一致する。

**(2) 軸は届いた光で合わせる。** 光の中心は、届いた $N$ 個の光子の到来方向の平均から、$\Delta\theta/\sqrt N$ 程度の精度で推定できる（$N$ 個の平均の標準誤差）。この精度で軸を合わせたとき、見分けられる固有の間隔は、軸合わせの精度に角径距離 $d_A$ を掛けた程度であり、$d_A(1+z)=d_M$ を使うと、係数を除いて $s_{\mathrm{ph}}$ と同じ形になる。観測する波長の延び $(1+z)$ と角径距離の縮み $1/(1+z)$ が、本文 第3.1節と同じく打ち消し合う。第10.5節の表では、軸合わせの精度を余裕をみて $\lambda_{\mathrm{obs}}/(D\sqrt N)$ とし、$s_{\mathrm{ph}}$ との比は約 0.5 である。表の値は、同じ光子を軸合わせと識別の両方に使った場合のものである。光子を両者に分けて使えば、どちらの限界も $\sqrt2$ 倍程度になり、軸を間隔より細かく合わせるという前提は、余裕なくぎりぎりで成り立つ。軸合わせの限界は $s_{\mathrm{ph}}$ と同じ桁であり、別の壁にはならない。

**(3) 装置の形の精度。** 装置の形（鏡どうしの位置）を測るにも光子を使い、その精度は (1)・(2) と同じく、測る光子の波長と数で決まる。細かく測るには短い波長、すなわち高いエネルギーが要り、エネルギーを狭い所に集めすぎると重力で崩壊する。そのため、原理の上で下げられる精度の下限はプランク長程度である（第4節の概算と同じ考え方）。(2) と違い、多くの光子で平均してもこの下限は下がらないとする。これは測定の統計の限界ではなく、測るためにエネルギーを集めることによる、局在そのものの下限だからである。実際の誤差は、位置を保つ安定性などで決まり、この下限より大きい。下限まで下げられた場合、装置の形の誤差による軸の向きの誤差は $l_P/D$ 程度、それで決まる間隔は $l_P\,d_A/D$ となる。表のとおり、これは $z\gtrsim3$ では $s_{\mathrm{ph}}$ より十分小さく、近い所（$z\approx0.1$）では同じ桁である。

別の見積もりとして、時計で長さと時間を測るときの量子力学の限界 [10] に装置の重力を組み合わせ、長さ $L$ の測定の誤差を $(l_P^2L)^{1/3}$、時間 $T$ の測定の誤差を $(t_P^2T)^{1/3}$（$t_P=l_P/c$ はプランク時間）とする見積もりがある [11]。これは発見的なものであり、批判と反対の主張がある [12, 13]。この見積もりを軸の向きに当てはめると、誤差が距離と観測時間とともに増え、効く壁が光子の数から装置の物差しと時計に移るが、上の (1)〜(3) はこの見積もりを使わない。

### 10.4 波長の効果

同じエネルギーなら、波長が短いほど光子1個あたりの見分けやすさが良くなり（$\xi_Q\propto\lambda_e^{-2}$）、光子の数は減る（$\bar N\propto\lambda_e$）。差し引きで、$s_{\mathrm{ph}}$ は $\sqrt{\lambda_e}$ に比例して小さくなる。ただし、波長が原子核の大きさ（約 $10^{-15}$ m）より短いと、物質で光を集めたり空間のモードに分けたりする装置を作れない。また、口径の各部分の光を合わせるには、装置の形の誤差が波長より十分小さい必要がある。短い波長で限界を下げるには、装置の形もそれだけ細かく知る必要があり、その下限は第10.3節 (3) のとおりプランク長程度である。

### 10.5 距離との関係

局所銀河群の大きさの口径で、観測時間の上限を例として $T_{\max}=10^{11}$ 年とした値を示す。本文 (a) の不透明さは含めていない。$z=10^{6}$ と $10^{12}$ の行は、その時代に光源が存在しない計算上の外挿であり、傾向を示すためのものである（どの行でも、届く光子の数は $10^{40}$ を超え、統計の扱いは成り立つ）。表のどの行でも $s_{\mathrm{ph}}$ は $\lambda_e d_M/D$（近い所で約 0.1 mm、最も遠い所で約 2 mm）より十分小さく、本文の式の前提である、間隔が回折の限界より十分小さいことは成り立つ。

| 赤方偏移 $z$ | $s_{\mathrm{ph}}$（光子の数） | 軸を光で合わせる限界 | 装置の形（プランク長）で決まる間隔 |
|---|---|---|---|
| 0.1 | $5.3\times10^{-33}$ m | $2.7\times10^{-33}$ m | $2.3\times10^{-33}$ m |
| 3 | $1.2\times10^{-30}$ m | $6.2\times10^{-31}$ m | $9.4\times10^{-33}$ m |
| 1090 | $5.7\times10^{-29}$ m | $2.9\times10^{-29}$ m | $7.3\times10^{-35}$ m |
| $10^{6}$ | $1.8\times10^{-27}$ m | $9.2\times10^{-28}$ m | $8.2\times10^{-38}$ m |
| $10^{12}$ | $1.8\times10^{-24}$ m | $9.2\times10^{-25}$ m | $8.2\times10^{-44}$ m |

この表から、固定した光源の例について、次のことが言える。

1. 効く限界は、光子の数で決まる $s_{\mathrm{ph}}$ である。軸合わせの限界はそれと同じ桁で、装置の形の限界は $z\gtrsim3$ では十分小さい。
2. $s_{\mathrm{ph}}$ は距離とともに単調に大きくなる。近い範囲では共動距離 $d_M$ が大きくなるためであり、$(1+z)\,t_{\mathrm{life}}$ が $T_{\max}$ を超える所から先では、受け取れる光子が $(1+z)$ に反比例して減るためである。$d_M$ は約 14 Gpc で頭打ちになるため、$z\to\infty$ で $s_{\mathrm{ph}}$ が限りなく大きくなるのは、$T_{\max}$ による $\sqrt{1+z}$ の項による。
3. 最終散乱面より前では、本文 (a) の不透明さにより、使える光子が $e^{-\tau}$ 倍になり、$s_{\mathrm{ph}}$ はさらに $e^{\tau/2}$ 倍になる。

したがって、観測時間と口径に上限があり、測定の精度が光子の波長と数で決まるという本試論の原理のもとでは、固定した光源の例で計算した範囲において、見分けられる最小の間隔は遠い過去ほど単調に大きくなり、$T_{\max}$ の帰結として、さかのぼるほど限りなく大きくなる傾向を持つ。過去へさかのぼるほど区別が曖昧になることと整合的な一例である。光源の波長や出す光子の数が時代によって変われば、値は変わる（第10.4節）。

### 10.6 確かさ

| 内容 | 種類 |
|---|---|
| 本文の式の当てはめ（第10.1節の式の前半）、第10.4節の波長による増減 | 既存の式の当てはめ |
| 転回半径の上限 [8]、軸のずれで回折の限界に戻ること [9]、位置と運動量の不確定性関係と回折の限界、$N$ 個の平均の標準誤差 | 既存の結果 |
| 届く割合 $T/[(1+z)\,t_{\mathrm{life}}]$ の取り込み、第10.3節 (1)〜(3) の導き方 | 本試論の概算 |
| 集められる質量が観測者の属する束縛された構造に限られること | 既存の結果からの帰結 |
| 観測時間に上限があること、口径の大きさに上限があること、精度が光子の波長と数で決まること | 本試論が置く原理（観測時間については [14] を動機とする） |
| 装置の形の精度の下限がプランク長程度であること | 本試論の概算（第4節と同じ考え方）。実際の誤差はこれより大きい |
| $(l_P^2L)^{1/3}$ 型の見積もり [11] | 発見的な見積もり。批判と反対の主張がある [12, 13]。本節の結論には使わない |
| 数値 | 桁の目安。第10.2節の最初の例のように口径が光源までの距離と比べて大きい場合は、本文の式の前提（小さい角度など）が崩れている |
| 第10.5節の結論 | 本試論の推定（上の三つの原理と、固定した光源の例による） |

## 参考文献

1. V. B. Braginsky, F. Ya. Khalili, *Quantum Measurement*, ed. K. S. Thorne (Cambridge University Press, 1992).
2. H. P. Yuen, "Contractive States and the Standard Quantum Limit for Monitoring Free-Mass Positions," Physical Review Letters 51, 719 (1983). [論文](https://doi.org/10.1103/PhysRevLett.51.719)
3. P. Hayden, K. Milner, M. M. Wilde, "Quantum Interactive Proofs and the Complexity of Separability Testing," Theory of Computing 11 (2015), 201–232. [論文](https://theoryofcomputing.org/articles/v011a003/)
4. S. L. Braunstein, C. M. Caves, "Statistical distance and the geometry of quantum states," Physical Review Letters 72, 3439 (1994). [論文](https://doi.org/10.1103/PhysRevLett.72.3439)
5. J. Liu, H. Yuan, X.-M. Lu, X. Wang, "Quantum Fisher information matrix and multiparameter estimation," J. Phys. A: Math. Theor. 53, 023001 (2020). [論文](https://arxiv.org/abs/1907.08037)
6. A. G. Cohen, D. B. Kaplan, A. E. Nelson, "Effective Field Theory, Black Holes, and the Cosmological Constant" (1999). [論文](https://arxiv.org/abs/hep-th/9803132)
7. R. Bousso, "A Covariant Entropy Conjecture" (1999). [論文](https://arxiv.org/abs/hep-th/9905177)
8. V. Pavlidou, T. N. Tomaras, "Where the world stands still: turnaround as a strong test of ΛCDM cosmology," JCAP (2014). [論文](https://arxiv.org/abs/1310.1920)
9. J. O. de Almeida, J. Kołodyński, C. Hirche, M. Lewenstein, M. Skotiniotis, "Discrimination and estimation of incoherent sources under misalignment," Physical Review A 103, 022406 (2021). [論文](https://arxiv.org/abs/2003.01166)
10. H. Salecker, E. P. Wigner, "Quantum Limitations of the Measurement of Space-Time Distances," Physical Review 109, 571 (1958). [論文](https://doi.org/10.1103/PhysRev.109.571)
11. Y. J. Ng, H. van Dam, "Measuring the Foaminess of Space-Time with Gravity-Wave Interferometers" (1999). [論文](https://arxiv.org/abs/gr-qc/9906003)
12. L. Diósi, B. Lukács, "Critique of proposed limit to space–time measurement, based on Wigner's clocks and mirrors" (1995). [論文](https://arxiv.org/abs/quant-ph/9501001)
13. J. C. Baez, S. J. Olson, "Uncertainty in measurements of distance," Classical and Quantum Gravity 19, L121 (2002). [論文](https://arxiv.org/abs/gr-qc/0201030)
14. L. M. Krauss, G. D. Starkman, "Life, the Universe, and Nothing: Life and Death in an Ever-Expanding Universe" (1999). [論文](https://arxiv.org/abs/astro-ph/9902189)

[本文へ戻る](zerothOrderPhase.html) / [付録1へ戻る](appendix1.html)

---

**作成者 / Author**: 5garashi.com設計事務所 / 5garashi.com Design Office  
**最終更新 / Last updated**: 2026-11-08 JST
