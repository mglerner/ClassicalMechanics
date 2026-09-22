#!/usr/bin/env python3
"""Write 03-answers.html: one answer sheet per prep pack (PHY 317).

Michael's own copy of the day's answers, laid out to be screenshotted into
the GoodNotes deck (Michael, 2026-09-22: "make sure I have a copy of the
PCCI answers and the in-class problem answers as part of my course prep
packs ... package it up as a PDF I can screenshot").

Everything here is pulled from the plan table in 00-prep-notes.md, so there
is no second copy to drift: the `Check:` lines under each row ARE the
answers, already curated per day. Rows are grouped into PCCI / groupwork /
everything else, using the `Groupwork:` line (playbook 3a).

This is an instructor sheet. It may quote the solutions manual; it is never
posted.

    python make_answer_sheets.py            # all packs
    python make_answer_sheets.py 07 08      # just these

Print to PDF from the browser, or screenshot a section straight into the
deck. One pack = one page, deliberately: the sheet is meant to sit beside
you, not to be read end to end.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

import make_active_learning as M

SOL_DPI = 110          # readable on screen, small enough to screenshot
SOL_GLOB = "*olution*.pdf"   # "solutions" / "Solutions" both match

CSS = """
body { background: #fff; margin: 0; padding: 16px 18px; color: #111;
       font-family: "Iowan Old Style", Palatino, Georgia, serif;
       font-variant-numeric: tabular-nums; }
h1 { font-size: 19px; margin: 0 0 2px 0; font-weight: normal; }
h1 .when { font-size: 14px; font-style: italic; color: #666; margin-left: 10px; }
h2 { font-size: 12px; letter-spacing: .12em; text-transform: uppercase;
     color: #6b6b6b; margin: 16px 0 6px 0; font-weight: normal;
     border-bottom: 1px solid #ccc; padding-bottom: 3px; }
.prob { margin: 0 0 9px 0; break-inside: avoid; }
.num { font-weight: bold; font-size: 15px; }
.num .when { font-weight: normal; font-style: italic; color: #777;
             font-size: 12.5px; margin-left: 6px; }
.task { font-size: 13.5px; color: #333; margin: 1px 0 2px 0; }
ul { margin: 0; padding-left: 17px; }
li { font-size: 14.5px; line-height: 1.4; }
.none { font-size: 13.5px; color: #777; font-style: italic; }
.sol { margin: 0 0 20px 0; break-inside: avoid; }
.sol img { width: 100%; border: 1px solid #ccc; display: block; }
.sol .cap { font-size: 12.5px; color: #666; font-style: italic;
            margin: 0 0 3px 0; }
.warn { background: #fff3cd; border: 1px solid #e0cd8a; padding: 7px 10px;
        font-size: 13px; margin: 14px 0 0 0; }
footer { margin-top: 18px; font-size: 11.5px; color: #777; font-style: italic;
         border-top: 1px solid #ccc; padding-top: 5px; }
@media print { body { padding: 0; } h2 { break-after: avoid; } }
"""

SKIP_AS_TASK = ("Check:", "Read back:", "Next:", "Check ")


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def segments(text):
    return [s.strip() for s in text.split("<br>") if s.strip()]


def row_entries(rows):
    """[(problem-or-None, when, task_line, [check lines])] for rows that have answers."""
    out = []
    for a, b, m, mode, _src, text in rows:
        segs = segments(text)
        checks = [s for s in segs if s.startswith("Check")]
        if not checks:
            continue
        body = [s for s in segs if not s.startswith(SKIP_AS_TASK)]
        # the problem number can sit in any non-Check line, not just the
        # first: plenty of rows open with a "We're about to find ..." frame.
        probs = [q for s in body for q in re.findall(r"\b(\d+\.\d+)\b", s)]
        task = next((s for s in body if re.search(r"\b\d+\.\d+\b", s)),
                    body[0] if body else "")
        out.append((probs[0] if probs else None, M.clock(a), task, checks))
    return out


def render(n, date, topic, rows, groupwork, pcci, sols):
    ent = row_entries(rows)
    gw, other, pcci_ent = [], [], []
    for prob, when, task, checks in ent:
        if pcci and ("PCCI" in task):
            pcci_ent.append((prob, when, task, checks))
        elif prob and prob in groupwork:
            gw.append((prob, when, task, checks))
        else:
            other.append((prob, when, task, checks))

    o = [f"<!doctype html><meta charset=utf-8>",
         f"<title>PHY 317 answers -- class {n:02d}</title><style>{CSS}</style>",
         f"<h1>Class {n:02d} answers<span class=when>{date} &middot; "
         f"{esc(topic)}</span></h1>"]

    def block(title, items):
        o.append(f"<h2>{title}</h2>")
        if not items:
            o.append('<p class=none>none</p>')
            return
        for prob, when, task, checks in items:
            label = prob or "&mdash;"
            o.append(f'<div class=prob><div class=num>{label}'
                     f'<span class=when>{when}</span></div>')
            if task and task != prob:
                o.append(f'<div class=task>{esc(task)}</div>')
            o.append("<ul>" + "".join(f"<li>{esc(c)}</li>" for c in checks)
                     + "</ul></div>")

    block(f"PCCI {esc(pcci) if pcci else ''}".strip(), pcci_ent)
    block("Groupwork " + (", ".join(groupwork) if groupwork else ""), gw)
    block("Everything else with an answer", other)

    o.append("<h2>Worked solutions</h2>")
    if sols:
        o.append('<p class=warn><b>Instructor copy.</b> These pages are '
                 'solutions-manual excerpts. Do not post them and do not '
                 'project them.</p>')
        for src, cap in sols:
            o.append(f'<div class=sol><p class=cap>{esc(cap)}</p>'
                     f'<img src="{esc(src)}" alt="{esc(cap)}"></div>')
    else:
        o.append('<p class=none>no solution PDF in this pack</p>')
    o.append("<footer>Instructor copy. Generated by make_answer_sheets.py from "
             "the plan table in 00-prep-notes.md -- edit the plan, not this "
             "file. Not for posting.</footer>")
    return "\n".join(o)


def solution_pages(pack_dir):
    """Render every page of the pack's ISM solution PDFs; return [(png, caption)].

    The ISM excerpts are image-only scans with no text layer, so there is
    nothing to parse: each page carries several problems and is shown whole,
    captioned by file and page. That is what makes this sheet a WORKED
    solution set rather than a list of answers.
    """
    if not shutil.which("pdftoppm"):
        return []
    out_dir = pack_dir / "03-answers-files"
    pages = []
    for pdf in sorted(pack_dir.glob(SOL_GLOB)):
        stem = re.sub(r"[^A-Za-z0-9]+", "-", pdf.stem).strip("-").lower()[:48]
        out_dir.mkdir(exist_ok=True)
        subprocess.run(["pdftoppm", "-png", "-r", str(SOL_DPI),
                        str(pdf), str(out_dir / stem)],
                       check=True, capture_output=True)
        for png in sorted(out_dir.glob(stem + "-*.png")):
            n = re.search(r"-(\d+)\.png$", png.name)
            pages.append((f"03-answers-files/{png.name}",
                          f"{pdf.name}, page {int(n.group(1)) if n else '?'}"))
    return pages


def pcci_number(rows):
    for _a, _b, _m, _mode, _src, text in rows:
        m = re.search(r"PCCI (\d+\.\d+)", text)
        if m:
            return m.group(1)
    return ""


def main(only=None):
    wrote = 0
    for n, date, path in M.pack_files():
        if only and f"{n:02d}" not in only:
            continue
        lines = path.read_text().split("\n")
        rows = M.plan_rows(lines, path)
        if not rows:
            continue
        gw = M.groupwork(lines) or []
        sols = solution_pages(path.parent)
        html = render(n, date, M.topic(lines, path), rows, gw,
                      pcci_number(rows), sols)
        out = path.parent / "03-answers.html"
        out.write_text(html)
        wrote += 1
    print(f"wrote {wrote} answer sheets (03-answers.html)")


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
