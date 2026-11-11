<!--
  ファイル名 / File: CHANGELOG.md
  概要 / Description: zeroPhase の改版履歴 / Revision history of zeroPhase
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-10-31
  版 / Version: 2.4.2
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 改版履歴 / Changelog — zeroPhase

版ごとの変更を、新しい版を上に書く(Design Office Identity 12-7 (9))。
Changes by version, newest first (Identity 12-7 (9)).

## 2.4.2 — 2026-11-12

- Zenn の紹介記事（`articles/zerophase-observation-limits.md`）を、これまでの連携先のリポジトリ（galois-theory-introduction）から、このリポジトリに移した。Zenn の GitHub 連携で、このリポジトリから同期する。記事には 2.0.2 から 2.4.1 までの更新の節を加え、第零次相の定義を 2.3.0 の定義に、付録の数を4つに改め、補足資料への案内を外した。`articles/` は公開ページ（GitHub Pages）から外した。README のファイルの一覧の付録を1〜4に直した。本文・付録は変えていない。
  Moved the Zenn introduction article (`articles/zerophase-observation-limits.md`) from the previously linked repository (galois-theory-introduction) into this repository, from which Zenn's GitHub integration syncs it. An update section covering versions 2.0.2 to 2.4.1 was added to the article; its definition of the Zeroth-Order Phase was updated to that of 2.3.0, the number of appendices was corrected to four, and the pointer to the supplementary notes was removed. `articles/` is not published on GitHub Pages. The appendix entries in the README file list were corrected to 1 to 4. The essay and appendices are unchanged.

## 2.4.1 — 2026-11-11

- 日英の本文の版の行の下、README、index.md に、Zenodo の DOI（10.5281/zenodo.24134735、すべての版に共通で、最新の版に解決する）を加えた。2.4.0 を Zenodo に登録したことによる。
  Added the Zenodo DOI (10.5281/zenodo.24134735, which is shared by all versions and resolves to the latest version) below the version line of the Japanese and English texts of the essay, and to the README and index.md, following the registration of version 2.4.0 on Zenodo.

## 2.4.0 — 2026-11-11

- 付録4「遠方の二光源の量子識別限界と伝播の影響」（日英）を加えた。補足資料「遠方の観測と区別の難しさ」のうち、本文 第3.1節と付録2 が根拠として使う部分（観測者の資源の上限、遠方の二光源の量子識別限界の導出、伝播の途中で情報が失われるか、宇宙分散と Fisher 情報）を、条件と確かさを明記した試論の形でまとめた。資源の上限は、本試論が採用する宇宙モデル・観測者・装置の構成の条件のもとで置くものとした。
  Added Appendix 4, "The Quantum Limit on Distinguishing Two Distant Sources and the Effects of Propagation" (Japanese and English). It collects, in the form of the essay with conditions and status stated, the parts of the supplementary note on observing distant objects on which Section 3.1 of the essay and Appendix 2 rely: the upper limits on the observer's resources, the derivation of the quantum limit on distinguishing two distant sources, whether information is lost during propagation, and cosmic variance and Fisher information. The upper limits on resources are adopted under the conditions of the cosmological model, observer, and apparatus configuration this essay assumes.
- 付録2 に第5.2節（量子Fisher情報と生成子の揺らぎ、推定としての時間とエネルギーの関係、生成子とネーターの定理の違い）と第5.3節（観測可能部分のQFIとエネルギーの推定）を日英で加えた。補足資料「QFI解説」のうち、本文 第2.2節と付録1 第5.1節が根拠として使う部分である。
  Added to Appendix 2 (Japanese and English) Section 5.2 (the quantum Fisher information and the fluctuation of the generator, the time–energy relation as estimation, and the difference between generators and Noether's theorem) and Section 5.3 (the QFI of the observable part and the estimation of energy), the parts of the supplementary note on the QFI on which Section 2.2 of the essay and Section 5.1 of Appendix 1 rely.
- 本文と付録1〜4（日英）、index.md、README の一覧から、補足資料2つへの参照を外した。補足資料そのものは変えずに残した。
  Removed references to the two supplementary notes from the essay and Appendices 1–4 (Japanese and English) and from the lists in index.md and the README. The supplementary notes themselves are kept unchanged.
- 本文 第3.1節（日英）を直した。光学的厚さを含む誤り確率の上限を、近似によらない $\frac12\exp[-e^{-\tau}\bar N(1-e^{-\xi_Q})]$ とし、$\xi_Q\ll1$ での近似を後に書いた（第6節の表も）。宇宙分散の式の条件（全天、統計的に等方的でガウス的、雑音なし）と、多数の多重極を合わせる効果を書いた。太陽の中心はニュートリノでだけ観測されるとした言い過ぎを直した。付録2 第5.1節に、QFI が増えないのは推定するパラメータによらない操作であることを書いた。
  Revised Section 3.1 of the essay (Japanese and English). The upper bound on the error probability including optical depth is now the non-approximate $\frac12\exp[-e^{-\tau}\bar N(1-e^{-\xi_Q})]$, with the approximation for $\xi_Q\ll1$ given afterwards (also in the table of Section 6). The conditions of the cosmic-variance formula (full sky, statistically isotropic and Gaussian, no noise) and the effect of combining many multipoles are stated. The overstatement that the center of the Sun is observed only through neutrinos was corrected. Section 5.1 of Appendix 2 now states that the QFI does not increase under operations that do not depend on the estimated parameter.
- 取り込みの内容を別の AI（Codex）に、英訳を別の AI（Copilot）に見てもらい、指摘に対応した（TESTING.md）。
  Another AI (Codex) reviewed the integrated content and another AI (Copilot) the English translation, and their comments were addressed (TESTING.md).

## 2.3.0 — 2026-11-11

- 第零次相の定義を改めた。記号 $\mathcal R_O$（観測手続き）を廃し、第零次相を「時刻・距離・方向・因果の順序の違いを区別する観測手段が、観測者にない状態」と定義した。観測手段は、考えている領域と期間の中で、物理法則が許し、観測者の使える資源で行える測定と操作の全体とした。付録3 第4節に、この定義を観測者が行える手順の結果の分布の一致として式で書き、区別の度合い $\Delta_O$（組ごとは $\delta_O$）を定めた。ランク $d_O$ と第零次相が種類の違う概念であり、$d_O=0$ は第零次相の十分条件でないことを書いた。本文・付録・補足資料の言い方と図をそろえた。
  Revised the definition of the Zeroth-Order Phase. The symbol $\mathcal R_O$ (the observational procedure) was removed, and the Zeroth-Order Phase is now defined as a state in which the observer has no means of observation that distinguish differences in time, distance, direction, or causal order. The means of observation are the whole of the measurements and operations that, within the region and period under consideration, the laws of physics allow and the observer can perform with the available resources. Section 4 of Appendix 3 writes this definition as a formula, the equality of the outcome distributions of procedures the observer can perform, and defines the degree of distinction $\Delta_O$ (and $\delta_O$ for each pair). It states that the rank $d_O$ and the Zeroth-Order Phase are different kinds of concepts and that $d_O=0$ is not a sufficient condition for the Zeroth-Order Phase. The wording and figures of the essay, appendices, and supplementary notes were aligned.
- 付録1 第1.1節に観測条件を定めた。許される測定を観測量の代数で表し、状態をその代数へ制限（条件つき期待値）してから量子Fisher情報を計算する。制限しないと QFI が0にならない例（z 基底の測定だけが許される場合）とその解釈を載せ、代数にならない場合は許される測定の Fisher 情報か $\Delta_O$ を使うとした。
  Section 1.1 of Appendix 1 now specifies observation conditions: the allowed measurements are represented by an algebra of observables, and the quantum Fisher information is computed after restricting the state to that algebra (a conditional expectation). An example in which the QFI does not vanish without the restriction (only z-basis measurements allowed) is given with its interpretation; when the allowed measurements do not form an algebra, the Fisher information of the allowed measurements or $\Delta_O$ is used.
- 付録1 を組み直し、第3節（運動学の模型）と第4節（動力学の模型）を新しく置いて、それぞれの初めに模型の設定と、示すこと・示さないことの一覧を置いた。数式を読む際の前提を第5節、課題を第6節とした。
  Reorganized Appendix 1 with new Section 3 (kinematic models) and Section 4 (dynamical models), each opening with a table of the models' settings and what they show and do not show. The premises for reading the equations are now Section 5 and the open tasks Section 6.
- 付録1 第3節に三つの模型を加えた。3.1：条件を満たす純粋状態では、ランクの低下が位置の基底での重ね合わせに対応し（互いに可換な生成子で QFI 行列が生成子の共分散の4倍）、ランクは時空の次元そのものではない（定在波でランク1、ガウス波束でランク3、一様な状態でランク0）。3.2：記録を加えるとランクが戻るかを有限次元の模型で計算し、対象の対称性による場合と観測者の記録の情報が失われる場合を分けた。3.3：観測者の記録の状態を接近のパラメータで変える運動学的な模型を、本試論の仮説として示した（接続を導くものではない）。
  Added three models to Section 3 of Appendix 1. 3.1: for pure states satisfying certain conditions, a drop in rank corresponds to superposition in the position basis (the QFI matrix is four times the covariance of mutually commuting generators), and the rank is not the dimension of spacetime itself (rank 1 for a standing wave, 3 for a Gaussian wave packet, 0 for a uniform state). 3.2: a finite-dimensional model computes whether the rank recovers when records are added, separating the symmetry of the object from the loss of information from the observer's records. 3.3: a kinematic model that varies the state of the observer's records with an approach parameter is given as a hypothesis of this essay (it does not derive the connection).
- 付録1 第4節に三つの動力学の模型を加えた。4.1：時計が熱平衡へ緩和すると、相対的な時刻の感度は有限の時間では0にならず、同じ温度の熱平衡では熱的な操作で時計を作り直せない（作る資源は縮退した準位の占有の偏りで、温度差はその一例）。4.2：時計と二準位の物差しの模型で、ランクは有限の時間で4のまま、固定した測定条件での有効次元だけが段階的に下がる（四つの独立な相対的なずれを数えるもので、時間と空間の区別は確かめていない）。4.3：物差しを多準位にすると時刻のずれと位置のずれが独立な二方向として区別され、極限で時刻の方向だけが失われる例がある。
  Added three dynamical models to Section 4 of Appendix 1. 4.1: when clocks relax to thermal equilibrium, the sensitivity to relative time does not vanish at finite times, and at a common temperature a clock cannot be rebuilt by thermal operations (the resource is the population imbalance within a degenerate eigenspace, of which a temperature difference is one example). 4.2: in a model of clocks and two-level rulers, the rank stays 4 at finite times while only the effective dimension under fixed measurement conditions decreases in steps (it counts four independent relative shifts and does not test the distinction between time and space). 4.3: with multilevel rulers, time shifts and position shifts are distinguished as two independent directions, and there is an example in which only the time direction is lost in the limit.
- 付録1 第2.1節に、同じ観測の模型をローレンツ変換で移して記述するときランクは変わらず、有効次元は座標系によることを書いた。第5.5節に、一般相対性理論でも運動学と動力学の区別はなくならないが、固定した背景と外部の時間を前提とする本付録の分け方には再検討が要ることを書いた。第3.1節 (4) にパウリの議論の条件を、第3.2節の場合 B にその設定の前提を書いた。
  Section 2.1 of Appendix 1 now states that the rank does not change when the same observational model is described after a Lorentz transformation, while the effective dimension depends on the frame. Section 5.5 states that general relativity does not remove the distinction between kinematics and dynamics, but that this appendix's division, which presupposes a fixed background and an external time, needs reexamination. Section 3.1 (4) gives the conditions of Pauli's argument, and case B of Section 3.2 its premises.
- 付録3 に第4.2節を加え、CCC の遠い未来を想定したおもちゃの模型で、組の種類ごとの区別の度合いを計算した。尺度の喪失だけでは全体の尺度の組しか区別できなくならず、相対的な尺度と順序に依存する過程の区別は残る。接続境界を第零次相とするには状態の一様性か読み取る手段の不在が要り、境界を越える自由度全体には違いが残る場合に第6節の痕跡と両立することと、その弱点を書いた。付録3 第3.3節・第6節で、CCC の情報の伝わり方を「論じられている可能性」と書き改めた。
  Added Section 4.2 to Appendix 3: a toy model modeled on the far future of CCC computes the degree of distinction for each kind of pair. The loss of scale alone removes only distinctions of global scale; distinctions of relative scale and of order-dependent processes remain. Treating the connecting boundary as the Zeroth-Order Phase requires uniformity of state or the absence of readout means, which is compatible with the traces of Section 6 when differences remain in the degrees of freedom crossing the boundary as a whole; its weaknesses are stated. Sections 3.3 and 6 of Appendix 3 now describe the transmission of information in CCC as a possibility that is discussed.
- 本文 第1節と付録2 第1.1節に、同じ幅の正規分布で識別度が中心の間隔と幅の比で決まる例を加えた。本文 第3.1節の「届くまでの時間は情報をぼかさない」を同じ空間モードの非分散伝播に限り、補足資料「遠方の観測と区別の難しさ」に第4.5節（媒質による分散は、既知で損失がなければ補償できる）を加えた。
  Added to Section 1 of the essay and Section 1.1 of Appendix 2 an example in which, for normal distributions of the same width, the degree of discrimination is set by the ratio of the separation of the centers to the width. Section 3.1 of the essay now limits "travel time does not blur the information" to non-dispersive propagation in the same spatial mode, and Section 4.5 was added to the supplementary note on observing distant objects (dispersion in a medium can be compensated if it is known and lossless).
- 付録2 に第10.6節「計算の有効範囲」を加え、遠い過去の極限では見分けられる最小の間隔が限りなく大きくなるのではなく、識別に使える検出がまれになり誤り率が $\frac12e^{-\bar N}$ を下回らないとした。転回半径を口径に当てはめることは本試論の前提とした。本文 第3.1節・第6節を合わせた。
  Added Section 10.6, "Range of validity of the calculation", to Appendix 2: in the limit of the distant past, the smallest distinguishable separation does not grow without bound; instead detections usable for discrimination become rare and the error probability does not fall below $\frac12e^{-\bar N}$. Applying the turnaround radius to the aperture is stated as a premise of this essay. Sections 3.1 and 6 of the essay were aligned.
- 量子クラメール・ラオ下限を使う所に局所不偏な推定の条件を書き、$D_{\mathrm{eff}}$ を読み取れる方向の数の上限とする説明を取り消した。付録3 第4節の表の次元縮減相を $d_O<4$ とし、尺度の喪失だけでは次元縮減相とも判定できないとした。補足資料「遠方の観測と区別の難しさ」第3.3節の波長の半分の限界を、通常の結像の分解の尺度に限った。
  Added the condition of locally unbiased estimation wherever the quantum Cramér–Rao bound is used, and withdrew the description of $D_{\mathrm{eff}}$ as an upper limit on the number of readable directions. The Dimension-Reduction Phase in the table of Section 4 of Appendix 3 is now $d_O<4$, and the loss of scale alone is not taken to determine even the Dimension-Reduction Phase. The half-wavelength limit in Section 3.3 of the supplementary note on observing distant objects is limited to the resolution scale of ordinary imaging.
- 本文 第3節の見出しを「第零次相への問い：宇宙論的極限における区別不能性」とした。本文の図1に「区別の度合い $\Delta_O\to0$」を加え、本文 第4.2節・第4.3節の模型の説明は付録を指す短い文にした。
  Retitled Section 3 of the essay "Questions Toward the Zeroth-Order Phase: Indistinguishability at Cosmological Limits". Figure 1 of the essay now shows "degree of distinction $\Delta_O\to0$", and the descriptions of the models in Sections 4.2 and 4.3 of the essay were shortened to sentences that point to the appendices.
- 英語版の本文と付録1〜3を、日本語の改訂に合わせて訳した。追加と変更の内容と英訳は、別の AI（Codex、Copilot）に見てもらい、指摘に対応した（TESTING.md）。
  Translated the English essay and Appendices 1–3 to match the revised Japanese. The added and changed content and the English translation were reviewed by other AIs (Codex, Copilot), and their comments were addressed (TESTING.md).

## 2.2.0 — 2026-11-08

- 日英の本文の版の行の下と README に、査読を受けていない試論であり、新しい実験・観測のデータは含まないこと、数値は既存の理論と公表値に基づく計算の例であることを書いた。
  Stated below the version line of the Japanese and English essays and in the README that this is an exploratory essay that has not been peer reviewed, that it contains no new experimental or observational data, and that the numbers are worked examples based on existing theory and published values.
- 本文 第2.2節（日英）に、粗視化で増えない計量が古典では定数倍を除いて Fisher 計量に決まり、量子では一つの族を成して SLD の量子 Fisher 情報がその最小であることを加え、文献 [27] Chentsov と [28] Petz を加えた。付録1（日英）では、QFIM を SLD で定めることを明記し、QFI の単調性の出典として同じ2件を加えた。
  Added to Section 2.2 of the essay (Japanese and English) that metrics which do not increase under coarse-graining are, up to a constant factor, the Fisher metric in the classical case and form a family in the quantum case, of which the SLD quantum Fisher information is the smallest, with references [27] Chentsov and [28] Petz. In Appendix 1 (Japanese and English), stated that the QFIM is defined by the SLD and added the same two references for the monotonicity of the QFI.
- 本文 第4.2節と付録1 第2.1節（日英）に、ランク $d_O$ が意味しないことを加えた（自由度の消滅ではないこと、計量の符号を決めないこと、連続的な変化で結ばれない大域的な区別を数えないこと）。
  Added to Section 4.2 of the essay and Section 2.1 of Appendix 1 (Japanese and English) what the rank $d_O$ does not mean: it is not a disappearance of degrees of freedom, it does not fix the signature of the metric, and it does not count global distinctions not connected by continuous changes.
- 足した文の内容と英訳を、別の AI（Copilot）に見てもらい、公開の前に内容を別の AI（Codex）にも見てもらって、指摘に対応した。これにあわせて、本文 第2.2節の QFI が増えない操作をパラメータによらないものに限り、第4.2節の区別できない状態の書き方（核に入る向きの曲線に沿って結ぶ）を正確にした（TESTING.md）。
  Had another AI (Copilot) review the content and English translation of the added text, and another AI (Codex) review the content before publication, and addressed their comments. Accordingly, Section 2.2 now limits the operations that do not increase the QFI to parameter-independent ones, and Section 4.2 states more precisely which states are indistinguishable (those joined by a curve whose tangent lies in the kernel) (TESTING.md).

## 2.1.0 — 2026-11-08

- 本文 第3.1節（日英）を、遠方を区別する難しさの二つの種類に分けて書き直した。一つは量子測定と観測者の有限の資源から出る原理的な限界で、光源が一つか二つかの識別の式を「遠方の二光源の量子識別限界」と名づけ、光子1個あたりの指数から $(1+z)$ が打ち消すこと、理想的な条件での上限であることと、その前提を書いた。もう一つは私たちの宇宙の歴史が強さを決める制約で、(a) 光学的厚さには宇宙の歴史によらない芯（データ処理不等式）と、散乱されなかった光子だけを使うモデルでの誤り確率の上限（$e^{-\tau}$ が指数の中に入る）を、(b) 宇宙分散には、ガウス的なゆらぎでのモードの数の芯を加えた。
  Rewrote Section 3.1 of the essay (Japanese and English) to separate two kinds of difficulty in distinguishing distant objects. The first is a limit in principle from quantum measurement and the observer's finite resources: the expression for distinguishing one source from two is named the "quantum limit on distinguishing two distant sources", with the cancellation of $(1+z)$ in the per-photon exponent and the ideal conditions under which it is an upper limit. The second consists of constraints whose strength is set by the history of our universe: (a) optical depth now has a core independent of that history (the data-processing inequality) and an upper bound on the error probability in a model that uses only unscattered photons ($e^{-\tau}$ enters the exponent), and (b) cosmic variance has a core in the number of modes for Gaussian fluctuations.
- 第4.2節（日英）に、資源が有限であるだけでは限界が決まらず、物理の上限があるため測定回数の上限 $N_{\max}$ が決まった値になることを加えた。第6節の確かさの表を合わせた。
  Added to Section 4.2 (Japanese and English) that finite resources alone do not fix a limit, and that the physical upper limits make the upper limit $N_{\max}$ on the number of measurements a definite value. Updated the table in Section 6 to match.
- 付録2（日英）に第10節「遠方の識別を資源の限界まで押し進めた見積もり」を加えた。本試論の原理として、(1) 観測時間には上限がある、(2) 口径の大きさには上限がある、(3) 測定の精度は光子1個では波長（エネルギー）で決まり、$N$ 個で $\sqrt N$ 倍まで良くなる、の三つを置き、遠方の二光源の量子識別限界に原理的な最大の資源を代入した。口径は宇宙の膨張に逆らって保てる大きさ（転回半径の2倍）に限り、測定の軸は届いた光で合わせ（位置と運動量の不確定性関係から、光子1個の方向の精度は $\lambda_{\mathrm{obs}}/(2\pi D)$ 程度）、装置の形の精度の下限はプランク長程度とした。固定した光源の例で、計算した範囲では、見分けられる最小の間隔が遠い過去ほど単調に大きくなり、さかのぼるほど限りなく大きくなる傾向が観測時間の上限の帰結であることを、本試論の推定として示した。本文 第3.1節の終わりに要約を加え、参考文献を7件加えた。
  Added Section 10, "An Estimate That Pushes Distant Discrimination to the Limits of Resources", to Appendix 2 (Japanese and English). Adopting three principles of this essay, (1) the observation time has an upper limit, (2) the size of the aperture has an upper limit, and (3) the precision of a measurement with a single photon is set by its wavelength (energy) and improves by up to a factor $\sqrt N$ with $N$ photons, it substitutes the maximum resources in principle into the quantum limit on distinguishing two distant sources. The aperture is limited to the size that can be held together against the expansion of the universe (twice the turnaround radius), the measurement axis is aligned with the received light (from the uncertainty relation between position and momentum, the precision of direction from a single photon is about $\lambda_{\mathrm{obs}}/(2\pi D)$), and the lower limit on the precision of the shape of the apparatus is taken to be of the order of the Planck length. As an estimate of this essay, it shows that, within the range computed for the example with a fixed source, the smallest distinguishable separation grows monotonically further into the past, and that its tendency to grow without bound the further one goes back is a consequence of the upper limit on the observation time. A summary was added at the end of Section 3.1 of the essay, and seven references were added.
- 補足資料「遠方の観測と区別の難しさ」第3.7節に、遠方の二光源の量子識別限界を光の伝わり方から導き直す説明を加えた。光源から開口への振幅（経路積分の近軸近似であるフレネルの伝搬核）から、光源の位置の違いが開口を横切る位相の傾きだけに現れること、円形の開口での状態の重なり $2J_1(v)/v$、量子チェルノフ指数の最小が端で取られる理由、指数が間隔の2乗に比例する理由を示し、図4・図5を加えた。既存の結果の導き直しであり、限界の式と結論は変えていない。
  Added to Section 3.7 of the supplementary note on Section 3 (Japanese only) an explanation that rederives the quantum limit on distinguishing two distant sources from the propagation of light. From the amplitude from a source to the aperture (the Fresnel propagation kernel, the paraxial approximation of the path integral), it shows that the difference in source position appears only as a tilt of the phase across the aperture, the overlap $2J_1(v)/v$ of the states on a circular aperture, why the quantum Chernoff exponent takes its minimum at the end point, and why the exponent is proportional to the square of the separation, with Figures 4 and 5. It rederives existing results and changes neither the expression for the limit nor the conclusions.
- 内容の妥当性と英訳を、別の AI（Copilot）に4回見てもらい、指摘に対応した。補足資料への追記の案は、別の AI（Codex）に見てもらい、指摘に対応した（TESTING.md）。適用する Design Office Identity を 4.26.0 に改めた。
  Had another AI (Copilot) review the validity of the content and the English translation four times, and addressed its comments; had another AI (Codex) review the proposal for the addition to the supplementary note, and addressed its comments (TESTING.md). Updated the applied Design Office Identity to 4.26.0.

## 2.0.3 — 2026-11-08

- 日英の本文の参考文献の前と README に「AI 支援の開示」の節を加え、執筆・改稿・英訳・図の作成・確認に生成 AI を使ったことと、内容の判断と責任が 5garashi.com設計事務所にあることを示した。日本語の文は Zenn の記事と同じ。論旨と数式は変えていない。
  Added a "Disclosure of AI Assistance" section before the references in the Japanese and English essays and in the README, stating that generative AI was used for drafting, revision, translation, figures, and checks, and that 5garashi.com Design Office made the judgments on the content and is responsible for it. The Japanese text matches the Zenn article. The argument and the equations are unchanged.

## 2.0.2 — 2026-11-07

- 各ページに Open Graph のタグ（og:title・og:description・og:url・og:image・og:locale）と twitter:card を加えた。URL を X・LinkedIn などに貼ったとき、タイトル・説明・画像が出るようにした。本文の内容は変えていない。共有用の画像は `assets/ogp/zeroPhase-ogp.png`（1200×630）。
  Added Open Graph tags (og:title, og:description, og:url, og:image, og:locale) and twitter:card to every page, so that a title, description, and image appear when a URL is shared on X, LinkedIn, and other services. The essay content is unchanged. The sharing image is `assets/ogp/zeroPhase-ogp.png` (1200×630).
- 適用する Design Office Identity の版を 4.23.0 から 4.25.0 に改めた（README・TESTING.md）。4.24.0 と 4.25.0 の変更のうち、本文の書き方に関係する GitHub 対応の記法（8-9 (10)）は、既存の検査 `tools/check_math.py` で確かめた。
  Updated the applied Design Office Identity version from 4.23.0 to 4.25.0 (README and TESTING.md). For the changes in 4.24.0 and 4.25.0, the notation rule for GitHub (8-9 (10)) that bears on the essay's writing was checked with the existing `tools/check_math.py`.

## 2.0.1 — 2026-11-07

- 公開後に、文中数式（`$…$`）の5か所が Markdown として処理され、正しく描画されていないことを確認して直した。付録3（日英）の計量の添字が強調として解釈される箇所、本文 第4.4節（日英）の `\!` が消えて階乗の記号として表示される箇所、補足資料の縦棒が表として、括弧がリンクとして解釈される箇所。数学的内容は変更していない。
  Fixed five inline math expressions that kramdown processed as Markdown after publication: subscripts parsed as emphasis in Appendix 3, a `\!` that turned into a factorial sign in Section 4.4 of the essay, and a bar and brackets in the supplementary notes parsed as a table and a link. The mathematical content is unchanged.
- 同じ不具合を見つける `tools/check_math.py` を加えた。
  Added `tools/check_math.py` to detect such expressions.

## 2.0.0 — 2026-11-07

- 有効次元を、観測者が利用できる測定の量子Fisher情報行列の固有値から定義し直した。測定回数と分解能のもとで連続的に変わり、測定回数を限りなく増やすと行列のランクに一致する。付録1・付録3の二つの定義を一つにまとめた。有限回数の有効次元は各方向をどれだけ読み取れるかの補助指標とし、三相の区分は、ある範囲で一定のランクで行う。ある範囲の全体で感度がゼロの方向では、状態が厳密に区別できないことを示した。
  Redefined the effective dimension from the eigenvalues of the quantum Fisher information matrix of the measurements available to the observer. It varies continuously with the number of measurements and the resolution, and reduces to the matrix rank in the limit of unlimited measurements, unifying the definitions in Appendices 1 and 3. The finite-measurement effective dimension is an auxiliary indicator; the three phases are classified by the rank over a region, and directions with zero sensitivity over a whole region are shown to be strictly indistinguishable.
- 観測者にとっての区別を、観測量の集まり（代数的場の量子論の考え方）で定義した。付録1に主な記号の表を加えた。
  Defined indistinguishability for an observer through the set of available observables, following algebraic quantum field theory, and added a table of the main symbols to Appendix 1.
- 付録3に、ペンローズの「静止質量がなければ時計がない」という議論を、次元を持つすべての物理量へ広げる節と、CCCの痕跡（ホーキング点）と第零次相の関係を説明する節を加えた。
  Appendix 3 extends Penrose's argument that there are no clocks without rest mass to all dimensionful quantities, and explains how the predicted CCC traces (Hawking points) relate to the Zeroth-Order Phase.
- 本文 第3節に、宇宙論の極限で区別が難しくなる理由と失われる理由を数式で加えた（角径距離、光子の数の流れ、光学的厚さによる全変動距離の上限、宇宙分散、静止質量と時計、事象の地平線とその温度）。光源が一つか二つかの識別を量子チェルノフ指数で表し、観測者の資源（口径・時間・エネルギー・記録の容量）に原理的な上限があることを第4.2節に加えた。
  Section 3 of the essay now shows by equations why distinctions become harder or are lost in the cosmological limits, expresses one-versus-two source discrimination by the quantum Chernoff exponent, and Section 4.2 adds the upper limits in principle on the observer's resources.
- 本文 第2.1節に、スペクトル次元の結果を次元縮減相を考える先行例として加え、距離とともに積み重なる時空の揺らぎの説とその観測による制限を加えた。CKNスケーリング・エントロピー限界と三相の関係を説明し、主張の確かさを本文の末尾の一つの節にまとめた。
  Section 2.1 cites spectral-dimension results as precedents and adds the proposal that spacetime fluctuations accumulate with distance, with its observational constraints. The essay explains the relation of CKN scaling and entropy bounds to the three phases and gathers the status of its claims in one closing section.
- 本文を短くし、三相の概念遷移図と比較表を序章に加えた。図3つと表を加えた。
  Shortened the essay and added figures and tables, including a transition diagram and comparison table of the three phases.
- 補足資料「QFI解説」と「遠方の観測と区別の難しさ（第3節の解説）」を加えた（日本語）。
  Added two supplementary notes in Japanese: on the QFI, and a question-and-answer guide to Section 3.
- 英語本文を2.0.0の内容で訳し直し、付録1〜3の英語版を新しく作った。付録のページに、本文と対応する言語の版へのリンクを付けた。
  Retranslated the English essay from the 2.0.0 Japanese text and added English editions of Appendices 1–3. Appendix pages now link to the essay and to their counterpart in the other language.
- 誤記を修正した（簡体字の混入、成功確率の記号、表の中のノルム記号、未定義の距離 d、付録の節番号の参照）。SQLの文献を Braginsky–Khalili とし、Yuen の論文を収縮状態の文献として引き直した。
  Corrected typos and notation, defined the distance d, fixed appendix section references, and cited Braginsky–Khalili for the SQL and Yuen for contractive states.
- 1.5.0（未公開）の付録3の追加を含む。
  Includes the addition of Appendix 3 from the unpublished 1.5.0.

## 1.5.0 — 2026-11-05（未公開 / not published）

この版はタグと Release を作らず、内容は 2.0.0 に含めて公開した。
This version was not tagged or released; its content was published as part of 2.0.0.

- 付録3を追加。CCCの接続境界を、時空的測定基準を構成できない第零次相と捉える仮説を整理した。
- 共形接続、観測上の一様性、時空的識別の構成、Fisher情報による縮減の例を説明した。CCCの既存の主張と本試論の追加仮説を分けた。
- 日本語本文とREADMEに付録3へのリンクを追加した。英語本文は変更していない。

## 1.4.0 — 2026-11-05

- 日本語本文を、時空限界相・次元縮減相・第零次相の接続を中心とする試論へ改稿した。第零次相を従来の時空的識別の限界と定義し、情報が相関に隠れる状態、共形・因果構造が残る状態、関係的記述で区別できる状態を対象外とした。
- 数式の詳しい条件は付録へ委ね、本文の留保の反復を減らした。QFIの比較対象、CKNの単位系、状態数を読む前提を明記した。
- 付録1の本文との関係を更新した。付録2と英語本文は改訂していない。
- 原稿の確認結果と、公開表示・外部レビューの未実施範囲はTESTING.mdに記録する。

## 1.3.1 — 2026-11-04

- 公開後に、付録2の文中数式の縦棒が表の区切りに解釈される箇所を確認。縦棒をLaTeXの `\vert` に変更し、ケット・内積・密度行列の説明を修正した。数学的内容は変更していない。
  Replaced literal vertical bars in Appendix 2’s math with LaTeX `\vert` so Kramdown does not interpret the surrounding prose as tables. The mathematical content is unchanged.

## 1.3.0 — 2026-11-04

- 元の付録1・2を、日本語の独立文書「観測限界を整理する三相モデルの論理的背景」「観測限界と識別可能性の数式解説」として整理・公開した。
  Published the former appendices as two standalone Japanese documents on the logical background of the three-phase model and the meaning and derivation of the equations.
- 三相・五つの極限領域を、本文の二段階・四つの極限を補う考察として位置づけた。付録2では元の10項目の数式と比較表を保持し、仮定・導出・適用条件を補足した。
  Positioned the three-phase model and five limits as supplementary considerations, retaining the original ten mathematical topics and comparison table with clarified assumptions and scope.
- 日本語本文・READMEから付録へ、付録どうしと本文へリンクを追加した。付録のヘッダーは「本文へ」とし、存在しない英語版への切り替えと誤認させない表示にした。
  Added navigation between the Japanese essay and the appendices; appendix headers link back to the essay rather than implying an English counterpart.
- 本文の論旨と既存の独立数式13組は変更していない。英語本文の原稿は改訂していない。
  The essay’s argument and its thirteen display equations are unchanged; the English source is unchanged.

## 1.2.0 — 2026-11-04

- 現行の日本語本文に対応する英語版を作成。序章・全5章・比較表・参考文献を揃え、二段階・四つの極限、仮説の限定を保持した。
  Updated the English edition to match the current Japanese essay, including the introduction, five sections, comparison table, and references, preserving the two stages, four limits, and qualifications of the hypotheses.
- 日本語ページから翻訳予定の告知、表示実装の説明、確認記録へのリンクを削除。公開本文は読者向けの内容と版・著者・更新日の情報に整理した。
  Removed the translation-status notice, rendering implementation notes, and verification-record links from the Japanese essay page, retaining reader-facing content and edition metadata.
- 日本語版・英語版の数式と引用番号を照合。README・VERSION・確認記録を更新した。
  Checked equations and citation numbers across both editions and updated README, VERSION, and verification records.

## 1.1.1 — 2026-11-04

- 公開後のChrome確認で、新しい本文と古いCSSが組み合わさるキャッシュ残存を確認。CSSのURLにビルド時刻を付け、更新した配色が読み込まれるようにした。
- 確認結果は TESTING.md に記録する。本文の内容と数式は1.1.0から変更していない。

## 1.1.0 — 2026-11-04

- 日本語本文のタイトルを1つにし、見出しを日本語へ統一。目的・版・更新日・表示先を冒頭に示した。
- 序章と各節の要点を先に置き、既存理論の説明と本稿の接続仮説を区別。二段階・四つの極限の構成と既存の独立数式13組は維持した。
- 第4.3節の整形済みテキスト図を比較表へ変更した。
- Identity 4.22.0に合わせ、文書面の無彩色、本文の太さ、印刷時の白背景、強制カラーと狭い画面の表示を整えた。
- 本文・README・本履歴のヘッダーと版、末尾の署名を整理。確認方法と実施範囲は TESTING.md に記録する。
- 英語本文は改訂していない。日本語版に、英語版が旧版であることを表示する。英訳は後日まとめて行う。
- 日本語だけで改訂する指定を本版に適用し、新しい英語本文や英語の改訂説明は追加しない。正式名称とヘッダー・署名の項目名はIdentityの書式を維持する。

## 1.0.1 — 2026-10-31

- 日英本文の分数・根号・積分・添え字・累乗を LaTeX 数式記法に変更。数学的内容は変更していない。
  Format fractions, roots, integrals, subscripts and powers as LaTeX math in both essays, preserving their mathematical content.
- MathJax 3.2.2 (Apache-2.0) を同梱し、GitHub Pages で数式を描画する。長い独立数式は枠内で横スクロールできる。
  Bundle MathJax 3.2.2 (Apache-2.0) for GitHub Pages, with horizontal scrolling for long display equations.

## 1.0.0 — 2026-10-31

最初の公開版。下書きの第20稿を、版 1.0.0 として公開した。
First public version: the 20th draft, published as version 1.0.0.

- 本文 `electron_cosmology_report.md`(旧名 `electron_cosmology_report_V20.md`)を公開した。版は VERSION とヘッダーで示すため、ファイル名から下書きの番号を外した(Identity 8-5、12-7 (5))。
  Published the essay `electron_cosmology_report.md` (formerly `electron_cosmology_report_V20.md`); the draft number was dropped from the file name because the version lives in VERSION and the header.
- Design Office Identity 4.20.0 を当てはめた:ファイルヘッダー(9-3)、著者の公式表記(8-6)、末尾の署名(9-5)。
  Applied Design Office Identity 4.20.0: file header (9-3), official author name (8-6), and closing signature (9-5).
- GitHub での表示を直した:4.3 の図の行が1行に連結されないよう整形済みテキストにし、「未分化の第零次相」の太字が表示されるよう括弧の内側に移し、末尾に残っていた閉じていない「````」を削除した。本文の内容は変えていない。
  Fixed display on GitHub: the diagram in 4.3 is now preformatted text so its lines stay separate, the bold "Zeroth-Order Phase" moved inside the brackets so it renders, and a stray unclosed "````" at the end was removed. The content is unchanged.



