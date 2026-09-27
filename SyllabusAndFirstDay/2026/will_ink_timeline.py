#!/usr/bin/env python3
"""Will Raven's F2025 PHY 317 classes, as delivered, from the ink timestamps
in his PowerPoint decks.

Every pen stroke Will made on a slide during class is stored in the .pptx as
InkML with a wall-clock timestamp. Grouping the strokes by date gives each
class day; ordering the slides by first stroke gives what he did and when;
the gap between his last content stroke and the end of the period is the
problem-solving tail he left the students. This is the "Will as delivered"
record that pass 1 of the class-plan recipe copies (ClassPlanPlaybook.md).

Input:  private/WillF2025/GoogleDrive/PHY317/ChN/Chapter N.pptx  (N = 1..12)
Output: private/F2026PrepPacks/_shared/will-ink-timeline.md

Class periods, F2025 (his Ch 1 slide 1): Mon 3:05-4:20 PM, Wed/Fri 2:45-4:00
PM, Eastern time. Timestamps in the InkML are UTC; converted with zoneinfo so
the November classes (after the DST change) come out right.

Terms used in the output:
  content stroke  a stroke on a slide that received >= MIN_TRACES strokes that
                  day (a slide with fewer is a "mark": a circled problem number
                  on a roadmap, a pointer, a stray)
  last content    the end of the main cluster of content strokes: strokes are
                  chained while gaps are <= CLUSTER_GAP; a late isolated burst
                  (e.g. a roadmap handoff 15 minutes after the lecture ended)
                  does not extend it
  tail            class end minus last content

Strokes more than WINDOW_SLOP outside the class period (prep ink that morning,
a fix on Sunday) are set aside and listed under "out-of-class ink", so they
never stretch a day's content block. Exam days and days he did not ink do not
appear, so the row number is NOT his meeting number; map to our packs by
chapter and slide, as the packs already do.
"""
import datetime as dt
import re
import sys
import zipfile
from collections import defaultdict
from pathlib import Path
from zoneinfo import ZoneInfo

HOME = Path.home()
DRIVE = HOME / "coding/courses/ClassicalMechanics/private/WillF2025/GoogleDrive/PHY317"
OUT = HOME / "coding/courses/ClassicalMechanics/private/F2026PrepPacks/_shared/will-ink-timeline.md"
TZ = ZoneInfo("America/New_York")
MIN_TRACES = 10          # fewer strokes on a slide in a day = a mark, not content
CLUSTER_GAP = 15 * 60    # seconds; a longer silence ends the content cluster
MIN_DAY_TRACES = 20      # fewer strokes in a day = not a class (prep, a stray)
WINDOW_SLOP = dt.timedelta(minutes=15)   # ink this far outside the period still counts as class
PERIOD = dt.timedelta(minutes=75)
START = {0: dt.time(15, 5)}          # Monday
START_DEFAULT = dt.time(14, 45)      # Wed / Fri
OUR_FIRST_CLASS = dt.date(2026, 9, 9)


def slide_texts(z, slide_path):
    xml = z.read(slide_path).decode("utf8", "replace")
    parts = re.findall(r"<a:t>([^<]*)</a:t>", xml)
    text = " ".join(p.strip() for p in parts if p.strip())
    text = re.sub(r"\s+", " ", text)
    return text[:70]


def deck(path):
    """Yield (slide_no, title, [local timestamps]) for every slide of a deck."""
    z = zipfile.ZipFile(path)
    names = set(z.namelist())
    pres = z.read("ppt/presentation.xml").decode()
    rels = z.read("ppt/_rels/presentation.xml.rels").decode()
    rid2t = {}
    for m in re.finditer(r"<Relationship [^>]*>", rels):
        s = m.group(0)
        rid2t[re.search(r'Id="([^"]+)"', s).group(1)] = re.search(r'Target="([^"]+)"', s).group(1)
    order = re.findall(r'<p:sldId [^>]*r:id="(rId\d+)"', pres)
    for n, r in enumerate(order, 1):
        t = "ppt/" + rid2t[r]
        rp = t.replace("slides/", "slides/_rels/") + ".rels"
        rr = z.read(rp).decode() if rp in names else ""
        inks = ["ppt/" + x.replace("../", "") for x in re.findall(r'Target="(\.\./ink/[^"]+)"', rr)]
        times = []
        for ink in inks:
            x = z.read(ink).decode("utf8", "replace")
            ctx = {}
            for m in re.finditer(r'<inkml:context xml:id="([^"]+)".*?timeString="([^"]+)"', x, re.S):
                ts = dt.datetime.fromisoformat(m.group(2).replace("Z", "+00:00"))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=dt.timezone.utc)
                ctx[m.group(1)] = ts
            for m in re.finditer(r"<inkml:trace ([^>]*)>", x):
                a = m.group(1)
                c = re.search(r'contextRef="#([^"]+)"', a).group(1)
                o = re.search(r'timeOffset="([^"]+)"', a)
                o = float(o.group(1)) if o else 0.0
                times.append((ctx[c] + dt.timedelta(milliseconds=o)).astimezone(TZ))
        yield n, slide_texts(z, t), times


def class_window(day):
    start = dt.datetime.combine(day, START.get(day.weekday(), START_DEFAULT), TZ)
    return start, start + PERIOD


def main():
    days = defaultdict(list)          # date -> [(t, ch, slide, title)]
    for ch in range(1, 13):
        path = DRIVE / f"Ch{ch}" / f"Chapter {ch}.pptx"
        if not path.exists():
            continue
        for n, title, times in deck(path):
            for t in times:
                days[t.date()].append((t, ch, n, title))

    out = ["# Will Raven F2025: classes as delivered, from slide ink timestamps", "",
           f"GENERATED by `SyllabusAndFirstDay/2026/will_ink_timeline.py`; do not edit. "
           f"Source: `WillF2025/GoogleDrive/PHY317/ChN/Chapter N.pptx`, InkML timestamps, Eastern time.",
           "",
           "How to read it: `content` = start of class to his last content stroke, i.e. the front-of-room "
           "block; `tail` = what was left of the 75 minutes, which his roadmap slides handed to problem-solving "
           "time. A slide with fewer than %d strokes in a day is a mark (a circled problem number), listed but "
           "not counted as content. Minutes per slide are first stroke to last stroke on that slide that day; "
           "slides overlap when he flipped back." % MIN_TRACES,
           "", "## Class days", "",
           "| # | Will's date | Class | First ink | Last content | Content min | Tail min | Slides in ink order (chapter.slide: minutes) |",
           "| - | ----------- | ----- | --------- | ------------ | ----------- | -------- | -------------------------------------------- |"]
    detail = ["", "## Per-slide detail", ""]
    k = 0
    stray = []
    outside = []
    for day in sorted(days):
        start, end = class_window(day)
        allL = sorted(days[day])
        L = [x for x in allL if start - WINDOW_SLOP <= x[0] <= end + WINDOW_SLOP]
        off = [x for x in allL if x not in L]
        if off:
            outside.append((day, len(off), sorted({(c, n) for _, c, n, _ in off}),
                            min(x[0] for x in off), max(x[0] for x in off)))
        if len(L) < MIN_DAY_TRACES:
            stray.append((day, len(L), sorted({(c, n) for _, c, n, _ in L})))
            continue
        k += 1
        per = defaultdict(list)
        titles = {}
        for t, c, n, title in L:
            per[(c, n)].append(t)
            titles[(c, n)] = title
        content_slides = {s for s, ts in per.items() if len(ts) >= MIN_TRACES}
        content = sorted(t for t, c, n, _ in L if (c, n) in content_slides)
        if not content:
            content = sorted(t for t, *_ in L)
        cluster_end = content[0]
        for t in content[1:]:
            if (t - cluster_end).total_seconds() > CLUSTER_GAP:
                break
            cluster_end = t
        first = L[0][0]
        cmin = (cluster_end - start).total_seconds() / 60
        tail = (end - cluster_end).total_seconds() / 60
        order = sorted(per, key=lambda s: min(per[s]))
        seq = ", ".join(
            f"{c}.{n}: {(max(per[(c, n)]) - min(per[(c, n)])).total_seconds() / 60:.0f}"
            + ("" if (c, n) in content_slides else " (mark)")
            for c, n in order)
        out.append(f"| {k} | {day:%a %b %d %Y} | {start:%H:%M}-{end:%H:%M} | {first:%H:%M} | "
                   f"{cluster_end:%H:%M} | {cmin:.0f} | {tail:.0f} | {seq} |")
        detail += [f"### {k}. {day:%A %B %d, %Y} ({start:%H:%M}-{end:%H:%M})", "",
                   "| Slide | First | Last | Strokes | Min | Title |",
                   "| ----- | ----- | ---- | ------- | --- | ----- |"]
        for c, n in order:
            ts = per[(c, n)]
            mark = "" if (c, n) in content_slides else " (mark)"
            detail.append(f"| {c}.{n}{mark} | {min(ts):%H:%M} | {max(ts):%H:%M} | {len(ts)} | "
                          f"{(max(ts) - min(ts)).total_seconds() / 60:.0f} | {titles[(c, n)]} |")
        detail.append("")
    if stray:
        out += ["", "Days with fewer than %d strokes inside the class window (prep or strays, not classes): " % MIN_DAY_TRACES
                + "; ".join(f"{d:%a %b %d} ({n} strokes on {s})" for d, n, s in stray)]
    if outside:
        out += ["", "Out-of-class ink, set aside: "
                + "; ".join(f"{d:%a %b %d} {a:%H:%M}-{b:%H:%M} ({n} strokes on {s})" for d, n, s, a, b in outside)]
    tails = []
    for line in out:
        m = re.match(r"\| \d+ \| .*? \| \d\d:\d\d-\d\d:\d\d \| \d\d:\d\d \| \d\d:\d\d \| (-?\d+) \| (-?\d+) \|", line)
        if m:
            tails.append((int(m.group(1)), int(m.group(2))))
    if tails:
        cs = sorted(c for c, _ in tails)
        ts = sorted(t for _, t in tails)
        out += ["", f"Across {len(tails)} class days: content median {cs[len(cs) // 2]} min "
                f"(range {cs[0]}-{cs[-1]}), tail median {ts[len(ts) // 2]} min (range {ts[0]}-{ts[-1]})."]
    OUT.write_text("\n".join(out + detail) + "\n")
    print(f"wrote {OUT} ({k} class days, {len(stray)} stray days)")


if __name__ == "__main__":
    sys.exit(main())
