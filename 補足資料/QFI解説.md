---
title: 補足資料：量子Fisher情報（QFI）から見る高エネルギー衝突における情報散逸と観測可能性
lang: ja
math: true
appendix: true
description: Fisher情報・量子Fisher情報・Bures距離と不確定性関係の関係を導き、高エネルギー衝突でのエネルギー推定の限界を説明する。
---
<!--
  ファイル名 / File: 補足資料/QFI解説.md
  概要 / Description: 量子Fisher情報と不確定性関係、部分トレースによる観測可能性の低下の解説
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-11-05
  最終更新 / Last updated: 2026-11-06 JST
  版 / Version: 2.0.0
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 補足資料：量子Fisher情報（QFI）から見る高エネルギー衝突における情報散逸と観測可能性

**著者 / Author:** 5garashi.com設計事務所 / 5garashi.com Design Office

**版:** <span data-version>2.0.0</span>　**更新日:** 2026-11-06 JST

[本文：観測限界と未分化の原点](../zerothOrderPhase.html) / [付録1：論理的背景](../appendix1.html) / [付録2：数式解説](../appendix2.html)

## 1. はじめに

高エネルギー粒子衝突やブラックホール情報問題では、「情報は本当に失われるのか？」という問題がしばしば現れる。

現代的な理解では、「全体系では情報は失われないが、観測者には失われたように見える」という状況が重要になる。

この現象を定量化する有力な道具が、Fisher情報（FI）、量子Fisher情報（QFI）、Bures距離である。

本稿では、次の内容を順に説明する。

1. Fisher情報とは何か
2. なぜ対数尤度を用いるのか
3. QFIとは何か
4. ハミルトニアンの揺らぎとの関係
5. 不確定性原理との関係
6. 高エネルギー衝突への応用

最終的に、次の結論を導く。

> 情報が観測できない自由度へ散逸し、観測可能部分のQFIが減少すると、観測者は衝突エネルギー $E$ を精密に推定できなくなる。

## 2. Fisher情報とは何か

未知パラメータ $\theta$ を観測データから推定するとき、確率分布 $p(x\mid\theta)$ を考える。

ここで $p(x\mid\theta)$ は、「$\theta$ が与えられたときに観測結果 $x$ が得られる確率」である。記号 $\mid$ は「条件付き（given）」を意味する。

### 2.1 Fisher情報

Fisher情報は

$$
F(\theta) = \sum_x p(x\mid\theta) \left( \frac{\partial}{\partial\theta} \ln p(x\mid\theta) \right)^2
$$

で定義される。

## 3. なぜ対数を取るのか

一見すると

$$
\frac{\partial p(x\mid\theta)} {\partial\theta}
$$

だけで十分に見える。しかし重要なのは「絶対変化量」ではなく「相対変化量」である。

### ケースA

$$
0.5 \rightarrow 0.51
$$

増加率は約2%。

### ケースB

$$
10^{-6} \rightarrow 2\times10^{-6}
$$

増加率は100%。

確率の変化量だけを見るとケースAの方が大きく見える。しかし推定上重要なのは、何％変化したかである。そこで

$$
\frac{\partial}{\partial\theta} \ln p = \frac{1}{p} \frac{\partial p}{\partial\theta}
$$

を用いる。これは確率の相対変化率を表している。

## 4. クラメール・ラオ下限

不偏推定量 $\widehat\theta$ について、Fisher情報から

$$
\operatorname{Var}(\widehat\theta) \ge \frac{1}{F(\theta)}
$$

が導かれる。これはクラメール・ラオ下限と呼ばれ、「どんな不偏推定法を用いても、推定誤差の分散はこれより小さくできない」という意味である。独立に $N$ 回測定するときは、右辺が $1/(NF)$ になる。

Fisher情報が大きいほど推定誤差の下限は小さくなり、推定精度が向上する。

## 5. 量子Fisher情報（QFI）

量子状態 $\rho(\theta)$ が未知パラメータ $\theta$ を含むとする。QFIは、状態が $\theta$ の変化にどれだけ敏感かを表す量であり、可能なすべての測定について最適化したFisher情報に等しい。

純粋状態 $\vert \psi(\theta)\rangle$ では

$$
F_Q = 4 \left( \langle \partial_\theta\psi \vert \partial_\theta\psi \rangle - \vert \langle \psi \vert \partial_\theta\psi \rangle\vert ^2 \right)
$$

となる。

以下では、変換を生む演算子（生成子） $G$ を使って

$$
\vert \psi(\theta)\rangle = e^{-i\theta G} \vert \psi_0\rangle
$$

と書ける場合を考える。$\theta$ は変換の量、$G$ は状態をどのように変えるかを定める演算子である。物理的な時間発展では、ハミルトニアン $H$ と換算プランク定数 $\hbar$ を使い、

$$
\vert \psi(t)\rangle = e^{-itH/\hbar} \vert \psi_0\rangle,
\qquad \theta=t,\qquad G=\frac{H}{\hbar}
$$

と対応づける。

## 6. QFIとハミルトニアンの揺らぎ

状態を微分すると

$$
\vert \partial_\theta \psi\rangle = -iG\vert \psi\rangle
$$

である。これをQFIの定義へ代入すると

$$
F_Q^{(\theta)} = 4 \left( \langle G^2\rangle -\langle G\rangle^2 \right) = 4(\Delta G)^2
$$

となる。時間発展（$G=H/\hbar$）では

$$
\boxed{ F_Q^{(t)} = \frac{4(\Delta H)^2}{\hbar^2} }
$$

を得る。ここで $(\Delta H)^2 = \langle H^2\rangle -\langle H\rangle^2$ はエネルギーの分散である。

### 物理的意味

エネルギー固有状態なら $\Delta H=0$ なので $F_Q^{(t)}=0$ となる。時間が経っても全体の位相が変わるだけで、観測結果は変化しない。

逆に、複数のエネルギー状態の重ね合わせでは $\Delta H$ が大きくなり、状態は時間の変化に敏感になる。つまり

$$
\boxed{ \text{エネルギーの揺らぎが大きいほど、時間についてのQFIは大きい} }
$$

のである。

## 7. 不確定性原理との関係

量子クラメール・ラオ下限

$$
\operatorname{Var}(\widehat t) \ge \frac{1}{F_Q^{(t)}}
$$

に $F_Q^{(t)}=4(\Delta H)^2/\hbar^2$ を代入し、両辺の平方根を取ると

$$
\boxed{ \Delta t\, \Delta H \ge \frac{\hbar}{2} },\qquad \Delta t \equiv \sqrt{\operatorname{Var}(\widehat t)}
$$

を得る。これは

$$
\Delta x\,\Delta p \ge \frac{\hbar}{2}
$$

と同じ構造を持つ。ただし、ここでの $\Delta t$ は時間の演算子の揺らぎではなく、状態の変化から経過時間を推定するときの誤差である。時間は、量子状態の変化を記述するパラメータとして扱う。

### 7.1 生成子とネーターの定理との関連

パラメータと生成子の関係は、ネーターの定理とも結び付く。ネーターの定理は、作用が連続的な変換に対して不変であるとき、それに対応する保存量が存在することを示す。例えば、時間並進対称性にはエネルギー保存、空間並進対称性には運動量保存、回転対称性には角運動量保存が対応する。[ネーターの定理の解説](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S1.html)

| 変換 | 変換量 | 量子状態の変換を生む生成子 | 対称性が成立する場合の保存量 |
|---|---|---|---|
| 時間をずらす | 時間 $t$ | $H/\hbar$ | エネルギー |
| 空間の位置をずらす | 変位 $a$ | その方向の運動量 $P/\hbar$ | その方向の運動量 |
| 向きを回転する | 角度 $\phi$ | 回転軸方向の角運動量 $J/\hbar$ | その軸方向の角運動量 |

変換を生成できることだけで、その生成子に対応する量が保存されるとは限らない。ネーターの定理では、作用の対称性が保存則を与える条件となる。

QFIでは、その変換を状態からどれほど精密に読み取れるかを考える。第6節のとおり $F_Q^{(\theta)}=4(\Delta G)^2$ であり、生成子の揺らぎが推定の感度を決める。[QFIと量子推定の解説](https://arxiv.org/abs/1907.08037)

エネルギーが保存されていても、その揺らぎがゼロになるとは限らない。異なるエネルギーの重ね合わせでは、エネルギーの確率分布を保ちながら成分間の相対位相が変わり、経過時間を読み取る手がかりになる。

このように、ネーターの定理は対称性に対応する保存量を、QFIは変換に対する状態の感度を扱う。両者を共通の生成子で整理することで、**対称性・保存量・推定感度のつながり**を理解できる。

## 8. Bures距離とQFI

QFIは量子状態間の距離とも関係する。状態 $\rho(E)$ と $\rho(E+\mathrm{d}E)$ の間のBures距離は

$$
D_{\mathrm{Bures}}^2 \simeq \frac14 F_Q(E)\, (\mathrm{d}E)^2
$$

で与えられる。したがって $F_Q$ は、$E$ の変化によって状態がどれだけ変わるかを測る量である。$F_Q$ が大きい → 状態間の距離が大きい → 識別しやすい、という関係になる。

## 9. 高エネルギー粒子衝突への応用

全体系の状態を $\rho(E)$ とする。ユニタリ発展のもとでは情報は保存される。しかし観測者は全自由度を見られない。そこで観測可能部分を

$$
\rho_{\mathrm{obs}}(E) = \operatorname{Tr}_{\mathrm{unobs}} \rho(E)
$$

と定義する。$\operatorname{Tr}_{\mathrm{unobs}}$ は観測できない自由度を部分トレースしたことを意味する。

部分トレースでは、QFIは増えない。

$$
F_Q\!\left[\rho_{\mathrm{obs}}\right](E) \le F_Q\!\left[\rho\right](E)
$$

比べるのは、同じエネルギーでの全体系と観測可能部分である。

## 10. 情報散逸の本質

高エネルギーになると、追加されたエネルギーの情報は、

- 不可視粒子
- 高次励起状態
- ダークセクター
- ブラックホール内部自由度

などへ流れる可能性がある。その結果、全状態では

$$
\rho(E) \neq \rho(E+\mathrm{d}E)
$$

であっても、観測可能部分では $E$ を変えたときの変化が小さくなる状況が生じる。

ここで注意が要る。$\mathrm{d}E$ をゼロに近づければ、どんな状態でもBures距離はゼロに近づく。QFIを決めるのは距離そのものではなく、距離の2乗と $(\delta E)^2$ の比の極限である。状態の階数が変わらない範囲では、

$$
F_Q\!\left[\rho_{\mathrm{obs}}\right](E)=4\lim_{\delta E\to0}\frac{D_{\mathrm{Bures}}^2\!\left(\rho_{\mathrm{obs}}(E),\rho_{\mathrm{obs}}(E+\delta E)\right)}{(\delta E)^2}
$$

情報が観測できない自由度へ流れ、同じ $\delta E$ に対する観測可能部分の距離が全体系より小さくなると、この比が小さくなる。これが、観測可能部分のQFIが下がるということの意味である。

## 11. エネルギー識別能力の消失

独立に $N$ 回測定し、局所不偏推定など量子クラメール・ラオ下限の成立条件が満たされるとき、

$$
\operatorname{Var}(\widehat E) \ge \frac{1}{N F_Q\!\left[\rho_{\mathrm{obs}}\right](E)}
$$

となる。単一のパラメータでは、適切な測定を選べばこの下限に漸近的に届く。測定回数 $N$ を一定とすると、$F_Q\!\left[\rho_{\mathrm{obs}}\right](E) \rightarrow 0$ なら推定誤差の下限は限りなく大きくなる。

つまり観測者は、観測データから衝突エネルギー $E$ を推定できなくなる。

## 12. 結論

QFIは、パラメータの変化に対して量子状態がどれだけ敏感かを表し、量子クラメール・ラオ下限を通じて推定精度と結び付く。

### 不確定性関係との対応

この関係は、第7節で述べた推定論的な不確定性関係と対応している。純粋状態が $\vert\psi(\theta)\rangle=e^{-i\theta G}\vert\psi_0\rangle$ と変化する場合には $F_Q^{(\theta)}=4(\Delta G)^2$ となり、生成子 $G$ の揺らぎが小さいほど、状態の変化を読み取りにくくなる。

### 衝突エネルギーの推定へのつながり

衝突エネルギーの推定でも、観測可能な状態がエネルギーの違いに反応しにくくなれば、エネルギーについてのQFIが低下し、第11節のとおりエネルギー推定誤差の下限が増大する。

この意味で、不確定性関係とQFIによる推定限界は、**パラメータに対する感度と推定精度の制約**という共通の構造を持つ。エネルギーについてのQFIとハミルトニアンの揺らぎは同じ量ではないが、それぞれが対応するパラメータに対する量子状態の感度に関わり、推定精度を制約するという観点で共通している。

このつながりによって、Fisher情報、QFI、不確定性関係、部分トレースを、観測者が情報をどこまで読み取れるかという共通の問いから理解できる。本試論の三相モデルでは、この読み取りの限界を時空限界相の例とし、時空の方向について同じ考え方を広げたものを有効次元として用いる（[付録1 第2.1節](../appendix1.html)）。

[本文へ戻る](../zerothOrderPhase.html)

---

**作成者 / Author**: 5garashi.com設計事務所 / 5garashi.com Design Office  
**最終更新 / Last updated**: 2026-11-06 JST
