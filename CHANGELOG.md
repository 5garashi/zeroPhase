<!--
  ファイル名 / File: CHANGELOG.md
  概要 / Description: zeroPhase の改版履歴 / Revision history of zeroPhase
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-10-31
  版 / Version: 2.2.0
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 改版履歴 / Changelog — zeroPhase

版ごとの変更を、新しい版を上に書く(Design Office Identity 12-7 (9))。
Changes by version, newest first (Identity 12-7 (9)).

## 2.2.0 — 2026-11-08

- 日英の本文の版の行の下と README に、査読を受けていない試論であり、新しい実験・観測のデータは含まないこと、数値は既存の理論と公表値に基づく計算の例であることを書いた。
  Stated below the version line of the Japanese and English essays and in the README that this is an exploratory essay that has not been peer reviewed, that it contains no new experimental or observational data, and that the numbers are worked examples based on existing theory and published values.
- 本文 第2.2節（日英）に、粗視化で増えない計量が古典では定数倍を除いて Fisher 計量に決まり、量子では一つの族を成して SLD の量子 Fisher 情報がその最小であることを加え、文献 [27] Chentsov と [28] Petz を加えた。付録1（日英）では、QFIM を SLD で定めることを明記し、QFI の単調性の出典として同じ2件を加えた。
  Added to Section 2.2 of the essay (Japanese and English) that metrics which do not increase under coarse-graining are, up to a constant factor, the Fisher metric in the classical case and form a family in the quantum case, of which the SLD quantum Fisher information is the smallest, with references [27] Chentsov and [28] Petz. In Appendix 1 (Japanese and English), stated that the QFIM is defined by the SLD and added the same two references for the monotonicity of the QFI.
- 本文 第4.2節と付録1 第2.1節（日英）に、ランク $d_O$ が意味しないことを加えた（自由度の消滅ではないこと、計量の符号を決めないこと、連続的な変化で結ばれない大域的な区別を数えないこと）。
  Added to Section 4.2 of the essay and Section 2.1 of Appendix 1 (Japanese and English) what the rank $d_O$ does not mean: it is not a disappearance of degrees of freedom, it does not fix the signature of the metric, and it does not count global distinctions not connected by continuous changes.
- 足した文の内容と英訳を、別の AI（Copilot）に見てもらい、指摘に対応した（TESTING.md）。
  Had another AI (Copilot) review the content and English translation of the added text, and addressed its comments (TESTING.md).

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



