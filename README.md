<!--
  ファイル名 / File: README.md
  概要 / Description: zeroPhase リポジトリの案内 / About this repository
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-10-31
  版 / Version: 2.4.2
  ライセンス / License: CC BY-ND 4.0(tools/ と .github/workflows/ は MIT)
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# zeroPhase — 観測限界と未分化の原点 / Observation Limits and the Undifferentiated Origin

バージョン / Version: 2.4.2([改版履歴 / Changelog](CHANGELOG.md))

DOI: [10.5281/zenodo.24134735](https://doi.org/10.5281/zenodo.24134735)(Zenodo。すべての版に共通で、最新の版に解決する / shared by all versions, resolves to the latest version)

数式は Markdown の `$…$` / `$$…$$` で記述し、公開ページでは同梱の MathJax 3.2.2 (Apache-2.0、`assets/vendor/mathjax/LICENSE`) で表示します。数式描画のための外部 CDN 通信はありません。
Equations use Markdown math notation and render with the bundled MathJax 3.2.2 (Apache-2.0), without external CDN requests.

適用基準: [Design Office Identity](https://5garashi.github.io/5garashi-identity/) 4.26.0（2026-11-11確認）。確認方法は[品質確認規定](https://5garashi.github.io/5garashi-quality/) 1.3.0の文書・Web表示の項目を参照。[確認方法と結果](TESTING.md)に実施範囲と未実施項目を記録する。全項目の適合確認を宣言するものではない。

2.0.0では、日本語本文・付録1〜3を改稿し、英語本文を訳し直して、付録1〜3の英語版を加えた。補足資料2つは日本語のみで公開する。本文の表示先はGitHub Pagesの公開ページを指定する（Identity 8-9 (9)）。

In 2.0.0, the Japanese essay and Appendices 1–3 were revised, the English essay was retranslated, and English editions of Appendices 1–3 were added. The two supplementary notes are published in Japanese only.

観測者が対象を区別できる限界を、時空限界相・次元縮減相・第零次相の三つの概念で整理する試論です。量子測定の限界から宇宙論の極限までをたどり、位置・距離・時間による区別そのものが成り立たなくなる状態を「未分化の第零次相(Zeroth-Order Phase)」と仮称して考えます。定量的な予測を示す論文ではなく、思考実験として書いています。

An essay that organizes the limits of an observer's ability to tell things apart by three concepts: the Spacetime-Limit Phase, the Dimension-Reduction Phase, and the Zeroth-Order Phase. It follows measurement limits from quantum physics to the extremes of cosmology, and tentatively calls the state in which distinctions by position, distance, and time no longer hold the "Zeroth-Order Phase". It is a thought experiment, not a paper with quantitative predictions.

査読を受けていない試論であり、新しい実験・観測のデータは含まない。数値は、既存の理論と公表値に基づく計算の例である。
An exploratory essay that has not been peer reviewed. It contains no new experimental or observational data; the numbers are worked examples based on existing theory and published values.

**本文を読む / Read the essay**

- [日本語版 / Japanese](https://5garashi.github.io/zeroPhase/zerothOrderPhase.html)
- [English](https://5garashi.github.io/zeroPhase/zerothOrderPhase.en.html)
- ソース / Source: [zerothOrderPhase.md](zerothOrderPhase.md) / [zerothOrderPhase.en.md](zerothOrderPhase.en.md)

## 内容 / Contents

1. 時空限界相：対象を区別する能力の限界 / The Spacetime-Limit Phase
2. 次元縮減相への接続：局在と観測可能な自由度 / Toward the Dimension-Reduction Phase
3. 第零次相への問い：宇宙論的極限における区別不能性 / Questions toward the Zeroth-Order Phase: indistinguishability at cosmological limits
4. 三相をつなぐ試論：四つの極限から第零次相へ / From four limits to the Zeroth-Order Phase
5. 結論と展望 / Conclusion and outlook
6. 本試論の主張の確かさについて / On the status of the claims

## 付録 / Appendices

| 付録 / Appendix | 日本語 / Japanese | English |
| :--- | :--- | :--- |
| 1. 三相モデルの論理的背景 / Logical background of the three-phase model | [appendix1](https://5garashi.github.io/zeroPhase/appendix1.html) | [appendix1.en](https://5garashi.github.io/zeroPhase/appendix1.en.html) |
| 2. 観測限界と識別可能性の数式解説 / Mathematical notes | [appendix2](https://5garashi.github.io/zeroPhase/appendix2.html) | [appendix2.en](https://5garashi.github.io/zeroPhase/appendix2.en.html) |
| 3. CCCの接続境界と第零次相 / The CCC connecting boundary and the Zeroth-Order Phase | [appendix3](https://5garashi.github.io/zeroPhase/appendix3.html) | [appendix3.en](https://5garashi.github.io/zeroPhase/appendix3.en.html) |
| 4. 遠方の二光源の量子識別限界と伝播の影響 / Distinguishing two distant sources and the effects of propagation | [appendix4](https://5garashi.github.io/zeroPhase/appendix4.html) | [appendix4.en](https://5garashi.github.io/zeroPhase/appendix4.en.html) |

## ファイル / Files

| ファイル / File | 内容 / Contents |
| :--- | :--- |
| `zerothOrderPhase.md` / `zerothOrderPhase.en.md` | 本文の日本語版 / English essay |
| `appendix1.md`〜`appendix4.md` / `appendix1.en.md`〜`appendix4.en.md` | 付録の日本語版 / English appendices |
| `補足資料/` | 補足資料（日本語） / Supplementary notes (Japanese) |
| `articles/` | Zenn の紹介記事（日本語。Zenn の GitHub 連携で同期する。公開ページには含めない。MIT） / Zenn introduction article (Japanese; synced through Zenn's GitHub integration; not part of the published pages; MIT) |
| `VERSION` | 版の番号(Identity 12-7) / Version number |
| `CHANGELOG.md` | 改版履歴 / Revision history |
| `TESTING.md` | 確認方法と結果 / Verification method and results |
| `LICENSE` | 本文のライセンス(CC BY-ND 4.0) / License of the text |
| `tools/check_math.py` | 文中数式（`$…$`）に、Markdown として処理されて壊れる書き方がないかを確かめる(MIT) / Finds inline math that the Markdown converter would break (MIT) |
| `tools/check_version.py` | 本文の版が `VERSION` と一致するかを確かめる(Identity から写した MIT のツール) / Checks that the essay's version matches `VERSION` (MIT, copied from the Identity) |
| `.github/workflows/` | 版を上げたときにタグと Release を作る・プルリクエストで版を確かめる(Identity のひな形、MIT) / Tags and releases on version changes, and checks versions on pull requests (Identity templates, MIT) |

## 改版のしかた / How to revise

1. 日本語の本文と付録を改訂し、英語版の章・段落・数式・引用と意味を合わせる。 / Revise the Japanese essay and appendices, and align the English sections, paragraphs, equations, citations, and meaning.
2. 内容が変わるときは `VERSION` を上げ、`CHANGELOG.md` に節を足し、この README の版の行を直す(Identity 12-7 (10))。 / When the content changes, raise `VERSION`, add a `CHANGELOG.md` section, and update the version line above.
3. `python tools/check_version.py --stamp <改訂したファイル>` で今回改訂した文書に版を書き込み、`python tools/check_version.py` で確かめる。改訂しない文書のヘッダーには、最後に改訂した版を残す。 / Stamp the revised files with `--stamp` and check with `python tools/check_version.py`.
4. main に push すると、`vX.Y.Z` のタグと GitHub の Release が作られる。 / Pushing to main creates the `vX.Y.Z` tag and a GitHub Release.

## AI 支援の開示 / Disclosure of AI assistance

本文の執筆と改稿、英語版の訳、図の作成、確認作業に、生成 AI（Claude・Codex・GitHub Copilot など）を使いました。英語版の見直しには、別の AI を使っています。内容の判断と責任は、5garashi.com設計事務所が負います。

Generative AI tools (Claude, Codex, GitHub Copilot, and others) were used to draft and revise the text, translate it into English, create the figures, and carry out checks. The English translation was reviewed by an AI other than the one that translated it. 5garashi.com Design Office made the judgments on the content and is responsible for it.

## ライセンス / License

本文は [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/deed.ja)(表示 - 改変禁止 4.0 国際)で提供します。出典(5garashi.com設計事務所)を示せば、商用を含めて共有・転載できます。改変したものの配布はできません。`tools/`・`.github/workflows/`・`articles/` は MIT License です(各ファイルのヘッダーによる)。

The text is licensed under [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/). You may share and republish it, including commercially, with attribution to 5garashi.com Design Office; you may not distribute modified versions. Files in `tools/`, `.github/workflows/` and `articles/` are under the MIT License, as stated in their headers.

Copyright © 2026 5garashi.com設計事務所 / 5garashi.com Design Office

---

**作成者 / Author**: 5garashi.com設計事務所 / 5garashi.com Design Office  
**最終更新 / Last updated**: 2026-11-08 JST
