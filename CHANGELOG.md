<!--
  ファイル名 / File: CHANGELOG.md
  概要 / Description: zeroPhase の改版履歴 / Revision history of zeroPhase
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-10-31
  版 / Version: 1.1.1
  ライセンス / License: CC BY-ND 4.0
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# 改版履歴 / Changelog — zeroPhase

版ごとの変更を、新しい版を上に書く(Design Office Identity 12-7 (9))。
Changes by version, newest first (Identity 12-7 (9)).

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

