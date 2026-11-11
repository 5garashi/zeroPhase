"""
ファイル名 / File: tools/check_math.py
概要 / Description: 公開する Markdown の文中数式($…$)に、kramdown が数式として扱わずに書き換えてしまう書き方がないかを確かめる
                    / Finds inline math ($…$) that kramdown rewrites before MathJax sees it
作成者 / Author: 5garashi.com設計事務所 / 5garashi.com Design Office
作成日 / Created: 2026-11-07
ライセンス / License: MIT
SPDX-License-Identifier: MIT

使い方 / Usage:
    python tools/check_math.py            # 公開する Markdown をすべて確かめる / check every published Markdown file
    python tools/check_math.py --self-test  # 過去の不具合の例集で、検査そのものを確かめる / test the checker on past defects

背景 / Background:
    kramdown は $$…$$ だけを数式として扱い、$…$ の中は普通の文として処理する。
    そのため、次の書き方は MathJax に届く前に壊れる(1.3.1 と 2.0.0 の公開後に見つかった不具合)。
    kramdown treats only $$…$$ as math; text inside $…$ is processed as ordinary Markdown.

確かめること / Checks (inline math only):
    (1) 縦棒 | : 段落が表として解釈される。\\vert を使う / a bar turns the paragraph into a table; use \\vert
    (2) ]( : リンクとして解釈される / parsed as a link
    (3) バックスラッシュの後の記号(\\! \\{ \\} \\[ \\] \\| \\_ \\# など): エスケープとして処理され、バックスラッシュが消える
        / backslash escapes are consumed by kramdown
    (4) 単語の途中でない _ が一つの段落の文中数式に2つ以上: 強調として解釈される。g_{ab}^{-} のように、文字の直後に置く
        / two or more non-intraword underscores in one paragraph become emphasis
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_PREFIXES = ("local/", "old/", "backupDoc/", ".git/", "_", "assets/", "tools/", ".github/")
SKIP_FILES = {"README.md", "CHANGELOG.md", "TESTING.md", "LICENSE.md"}
ESCAPE_RE = re.compile(r"\\[!{}\[\]()#+\-.:|_*`]")
NONWORD_UNDERSCORE_RE = re.compile(r"(?<![A-Za-z0-9])_")


def paragraphs(text: str):
    """独立数式とコードを除き、空行で区切った段落を、開始行の番号とともに返す"""
    text = re.sub(r"^---\n.*?\n---\n", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    for pattern in (r"```.*?```", r"\$\$.*?\$\$", r"<svg.*?</svg>"):
        text = re.sub(pattern, lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    start = 1
    for block in text.split("\n\n"):
        yield start, block
        start += block.count("\n") + 2


def check(path: pathlib.Path):
    problems = []
    for line_no, block in paragraphs(path.read_text(encoding="utf-8")):
        maths = re.findall(r"(?<!\\)\$([^$\n]+)\$", block)
        if not maths:
            continue
        underscores = 0
        for m in maths:
            if "|" in m:
                problems.append((line_no, "縦棒 / bar", m))
            if "](" in m:
                problems.append((line_no, "リンクの形 / link syntax", m))
            esc = ESCAPE_RE.findall(m)
            if esc:
                problems.append((line_no, "エスケープ / escape " + " ".join(sorted(set(esc))), m))
            underscores += len(NONWORD_UNDERSCORE_RE.findall(m))
        if underscores >= 2:
            problems.append((line_no, f"強調になる _ が{underscores}個 / underscores", " / ".join(maths)[:80]))
    return problems


# 過去に公開ページで崩れた書き方(must_fail)と、直した書き方・崩れないと確かめた書き方(must_pass)の例集
# Corpus of past defects (must_fail) and their fixes or verified-safe forms (must_pass)
CORPUS = {
    "must_fail": [
        # 1.3.1 付録2: 縦棒が表として解釈された / bars parsed as a table
        "ケット $|0\\rangle$ と $|1\\rangle$ を考える。",
        # 2.0.0 付録3: 添字が強調として解釈された / subscripts parsed as emphasis
        "物理的計量 $g^-_{ab}, g^+_{ab}$ は、共通の共形計量 $\\widetilde{g}_{ab}$ を介して",
        # 2.0.0 本文 4.4: \! が消えて ! (階乗)になった / \\! became a factorial sign
        "状態の数は $N \\le \\exp\\!\\left(A/4l_P^2\\right)$ と読める。",
        # 2.0.0 QFI解説: ]( がリンクとして解釈された / ]( parsed as a link
        "$F_Q\\!\\left[\\rho_{\\mathrm{obs}}\\right](E) \\rightarrow 0$ なら",
    ],
    "must_pass": [
        "ケット $\\vert0\\rangle$ と $\\vert1\\rangle$ を考える。",
        "物理的計量 $g_{ab}^{-}, g_{ab}^{+}$ は、共通の共形計量 $\\widetilde{g}_{ab}$ を介して",
        "状態の数は $N \\le \\exp\\left(A/4l_P^2\\right)$ と読める。",
        "$F_Q[\\rho_{\\mathrm{obs}}]\\,(E) \\rightarrow 0$ なら",
        # 段落に一つだけの _ と、]( にならない括弧は崩れないことを公開ページで確かめた
        "部分系 $\\rho_{\\mathrm{obs}} = \\operatorname{Tr}_{\\mathrm{unobs}}\\rho$ について",
        "$N\\le\\exp[A/(4l_P^2)]$ と表す。",
        # 2.4.0 付録1: 同じ段落で }_ が2回になるのを \nolimits で避けた書き方。公開ページで崩れないことを確かめた
        "$\\mathcal E_O(\\rho)=\\operatorname{Tr}\\nolimits_B(\\rho)\\otimes I_B/d_B$ である。部分トレース $\\rho_A=\\operatorname{Tr}\\nolimits_B\\rho$ は",
    ],
}


def self_test() -> int:
    import tempfile
    failures = 0
    with tempfile.TemporaryDirectory() as d:
        for kind, samples in CORPUS.items():
            for s in samples:
                p = pathlib.Path(d) / "sample.md"
                p.write_text(s + "\n", encoding="utf-8")
                found = bool(check(p))
                ok = found if kind == "must_fail" else not found
                if not ok:
                    failures += 1
                    print(f"自己試験の失敗 / self-test failed ({kind}): {s}")
    total = sum(len(v) for v in CORPUS.values())
    print(f"self-test: {total - failures}/{total} passed")
    return 1 if failures else 0


def main() -> int:
    if "--self-test" in sys.argv[1:]:
        return self_test()
    files = []
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(SKIP_PREFIXES) or p.name in SKIP_FILES:
            continue
        files.append((rel, p))
    bad = 0
    for rel, p in files:
        for line_no, kind, snippet in check(p):
            bad += 1
            print(f"{rel}:{line_no}: {kind}: {snippet[:80]}")
    print(f"{len(files)} files, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
