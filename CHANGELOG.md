<!--
  ファイル名 / File: CHANGELOG.md
  概要 / Description: zeroPhase の改版履歴 / Revision history of zeroPhase
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-10-31
  版 / Version: 2.0.1
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 改版履歴 / Changelog — zeroPhase

版ごとの変更を、新しい版を上に書く(Design Office Identity 12-7 (9))。
Changes by version, newest first (Identity 12-7 (9)).

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



