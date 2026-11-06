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


def main() -> int:
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
