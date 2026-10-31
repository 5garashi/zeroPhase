<!--
  ファイル名 / File: README.md
  概要 / Description: zeroPhase リポジトリの案内 / About this repository
  作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
  作成日 / Created: 2026-10-31
  ライセンス / License: CC BY-ND 4.0(tools/ と .github/workflows/ は MIT)
  SPDX-License-Identifier: CC-BY-ND-4.0
-->
# zeroPhase — 観測限界と未分化の原点 / Observation Limits and the Undifferentiated Origin

バージョン / Version: 1.0.1([改版履歴 / Changelog](CHANGELOG.md))

数式は Markdown の `$…$` / `$$…$$` で記述し、公開ページでは同梱の MathJax 3.2.2 (Apache-2.0、`assets/vendor/mathjax/LICENSE`) で表示します。数式描画のための外部 CDN 通信はありません。
Equations use Markdown math notation and render with the bundled MathJax 3.2.2 (Apache-2.0), without external CDN requests.

数式表示の確認 / Math display checks (2026-10-31): 日英の独立数式13組の一致と版・差分を確認。ブラウザーの目視、200%拡大、小画面、キーボード、読み上げは未確認。
Checked: matching sets of 13 display equations, versions and diffs. Browser appearance, 200% zoom, narrow screens, keyboard use and screen readers remain unverified.

デザイン基準 / Design reference: [5garashi.com設計事務所 / 5garashi.com Design Office — Identity](https://5garashi.github.io/5garashi-identity/), v4.20.0 (確認 / checked: 2026-10-31).

量子測定の限界から宇宙論の極限までをたどり、対象を区別する基準そのものが意味を失う極限を「未分化の第零次相(Zeroth-Order Phase)」と仮称して考える試論です。定量的な予測を示す論文ではなく、思考実験として書いています。

An essay that follows measurement limits from quantum physics to the extremes of cosmology, tentatively naming the limit where the very criteria for telling things apart lose their meaning the "Zeroth-Order Phase". It is a thought experiment, not a paper with quantitative predictions.

**本文を読む / Read the essay**

- [日本語版 / Japanese](https://5garashi.github.io/zeroPhase/zerothOrderPhase.html)
- [English](https://5garashi.github.io/zeroPhase/zerothOrderPhase.en.html)
- ソース / Source: [zerothOrderPhase.md](zerothOrderPhase.md) / [zerothOrderPhase.en.md](zerothOrderPhase.en.md)

## 内容 / Contents

1. 確率的識別限界と標準量子限界 / Probabilistic discrimination and the standard quantum limit
2. 局在限界と時空描像の限界(プランク長、時空の泡、高エネルギー散乱と量子 Fisher 情報) / Localization limits and the limits of the spacetime picture
3. 宇宙論的極限(宇宙マイクロ波背景放射、熱死、共形サイクリック宇宙論) / Indistinguishability at cosmological limits
4. 四つの極限と「未分化の第零次相」の提案 / Four limits and the proposed Zeroth-Order Phase
5. 結論と展望 / Conclusion

## ファイル / Files

| ファイル / File | 内容 / Contents |
| :--- | :--- |
| `zerothOrderPhase.md` / `zerothOrderPhase.en.md` | 日本語版 / English essay |
| `VERSION` | 版の番号(Identity 12-7) / Version number |
| `CHANGELOG.md` | 改版履歴 / Revision history |
| `LICENSE` | 本文のライセンス(CC BY-ND 4.0) / License of the text |
| `tools/check_version.py` | 本文の版が `VERSION` と一致するかを確かめる(Identity から写した MIT のツール) / Checks that the essay's version matches `VERSION` (MIT, copied from the Identity) |
| `.github/workflows/` | 版を上げたときにタグと Release を作る・プルリクエストで版を確かめる(Identity のひな形、MIT) / Tags and releases on version changes, and checks versions on pull requests (Identity templates, MIT) |

## 改版のしかた / How to revise

1. `zerothOrderPhase.md` と `zerothOrderPhase.en.md` を直す。 / Edit the Japanese and English essays.
2. 内容が変わるときは `VERSION` を上げ、`CHANGELOG.md` に節を足し、この README の版の行を直す(Identity 12-7 (10))。 / When the content changes, raise `VERSION`, add a `CHANGELOG.md` section, and update the version line above.
3. `python tools/check_version.py --stamp zerothOrderPhase.md zerothOrderPhase.en.md` で両方の本文に版を書き込み、`python tools/check_version.py` で確かめる。 / Stamp and check both essays.
4. main に push すると、`vX.Y.Z` のタグと GitHub の Release が作られる。 / Pushing to main creates the `vX.Y.Z` tag and a GitHub Release.

## ライセンス / License

本文は [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/deed.ja)(表示 - 改変禁止 4.0 国際)で提供します。出典(5garashi.com設計事務所)を示せば、商用を含めて共有・転載できます。改変したものの配布はできません。`tools/` と `.github/workflows/` は MIT License です(各ファイルのヘッダーによる)。

The text is licensed under [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/). You may share and republish it, including commercially, with attribution to 5garashi.com Design Office; you may not distribute modified versions. Files in `tools/` and `.github/workflows/` are under the MIT License, as stated in their headers.

Copyright © 2026 5garashi.com設計事務所 / 5garashi.com Design Office

---

**作成者 / Author**: 5garashi.com設計事務所 / 5garashi.com Design Office
**最終更新 / Last updated**: 2026-10-31 JST
