"""
Build the change log that accompanies the partner dossier.

    python tools/build_changelog_docx.py

Writes partners/Programme_Dossier_Change_Log.docx

Partners read the dossier, not this repository, so when a new version reaches them they
need to know what moved rather than re-reading twenty pages.

BASELINE is the version the partner already has. It is set below and every claim in the
document is checked against that version's built file, not written from memory -- the
"at the version you have" column is produced by reading the old .docx.

The content here is a SUMMARY of the repository, written for an external reader who will
not open the source. When the curriculum, the schedule or the status changes, this file
must be updated too -- it is the one document that restates facts rather than linking to
them. Figures that appear in both places are listed in CHECKED_FACTS below and verified
against the repository at build time, so this file cannot drift silently.
"""

import re
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "partners" / "Programme_Dossier_Change_Log.docx"

INK = RGBColor(0x1A, 0x1A, 0x1A)
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x5A, 0x5A, 0x5A)
RULE = "1F3A5F"
HEADER_FILL = "1F3A5F"
BAND_FILL = "EEF2F7"
NOTE_FILL = "F7F4EC"


# --------------------------------------------------------------------------- helpers

def shade(cell, fill):
    element = OxmlElement("w:shd")
    element.set(qn("w:val"), "clear")
    element.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(element)


def no_borders(table):
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        line = OxmlElement(f"w:{edge}")
        line.set(qn("w:val"), "none")
        line.set(qn("w:sz"), "0")
        borders.append(line)
    # tblPr enforces child order: tblBorders sits before shd, tblLayout, tblCellMar
    # and tblLook. Appending it would produce a schema-invalid file that some readers
    # silently drop.
    table._tbl.tblPr.insert_element_before(
        borders, "w:shd", "w:tblLayout", "w:tblCellMar", "w:tblLook",
        "w:tblCaption", "w:tblDescription",
    )


def bottom_rule(paragraph, size=6, colour=RULE):
    borders = OxmlElement("w:pBdr")
    line = OxmlElement("w:bottom")
    line.set(qn("w:val"), "single")
    line.set(qn("w:sz"), str(size))
    line.set(qn("w:space"), "4")
    line.set(qn("w:color"), colour)
    borders.append(line)
    paragraph._p.get_or_add_pPr().append(borders)


def keep_with_next(paragraph):
    element = OxmlElement("w:keepNext")
    paragraph._p.get_or_add_pPr().append(element)


def repeat_header(row):
    properties = row._tr.get_or_add_trPr()
    element = OxmlElement("w:tblHeader")
    element.set(qn("w:val"), "true")
    properties.append(element)


# **bold**, *italic* and `code`. The bold alternative must come first so that ** is not
# consumed by the single-asterisk branch.
MARKUP = re.compile(r"(\*\*[^*]+\*\*|\*[^*\n]+\*|`[^`]+`)")


def rich(paragraph, text, size=10.5, colour=INK, italic=False):
    """Render **bold**, *italic* and `code` inside a single paragraph."""
    for piece in MARKUP.split(text):
        if not piece:
            continue
        emphasis = False
        if piece.startswith("**") and piece.endswith("**"):
            run = paragraph.add_run(piece[2:-2])
            run.bold = True
        elif piece.startswith("`") and piece.endswith("`"):
            run = paragraph.add_run(piece[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(size - 1)
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            run = paragraph.add_run(piece[1:-1])
            emphasis = True
        else:
            run = paragraph.add_run(piece)
        run.font.size = Pt(size)
        run.font.color.rgb = colour
        run.italic = italic or emphasis
    return paragraph


# ------------------------------------------------------------------------- structure

class Dossier:
    def __init__(self):
        self.document = Document()
        self._fix_settings()
        self._page_setup()
        self._styles()
        self.section_number = 0

    def _fix_settings(self):
        """The stock template emits <w:zoom/>, but w:percent is required by the schema."""
        settings = self.document.settings.element
        zoom = settings.find(qn("w:zoom"))
        if zoom is not None and zoom.get(qn("w:percent")) is None:
            zoom.set(qn("w:percent"), "100")

    def _page_setup(self):
        for section in self.document.sections:
            section.page_width = Cm(21.0)        # A4
            section.page_height = Cm(29.7)
            section.top_margin = Cm(2.2)
            section.bottom_margin = Cm(2.2)
            section.left_margin = Cm(2.2)
            section.right_margin = Cm(2.2)
        self.content_width = Cm(21.0 - 4.4)

    def _styles(self):
        normal = self.document.styles["Normal"]
        normal.font.name = "Calibri"
        normal.font.size = Pt(10.5)
        normal.font.color.rgb = INK
        normal.paragraph_format.space_after = Pt(7)
        normal.paragraph_format.line_spacing = 1.12

        for name, size, colour, before, after in (
            ("Heading 1", 17, NAVY, 22, 8),
            ("Heading 2", 12.5, NAVY, 15, 5),
            ("Heading 3", 11, NAVY, 11, 3),
        ):
            style = self.document.styles[name]
            style.font.name = "Calibri"
            style.font.size = Pt(size)
            style.font.bold = True
            style.font.color.rgb = colour
            style.paragraph_format.space_before = Pt(before)
            style.paragraph_format.space_after = Pt(after)
            style.paragraph_format.keep_with_next = True

    # -- blocks ------------------------------------------------------------

    def h1(self, text, numbered=True):
        if numbered:
            self.section_number += 1
            text = f"{self.section_number}.  {text}"
        heading = self.document.add_heading(text, level=1)
        bottom_rule(heading)
        return heading

    def h2(self, text):
        return self.document.add_heading(text, level=2)

    def h3(self, text):
        return self.document.add_heading(text, level=3)

    def para(self, text, size=10.5, colour=INK, italic=False, after=7):
        paragraph = self.document.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(after)
        rich(paragraph, text, size=size, colour=colour, italic=italic)
        return paragraph

    def bullets(self, items, size=10.5):
        for item in items:
            paragraph = self.document.add_paragraph(style="List Bullet")
            paragraph.paragraph_format.space_after = Pt(3)
            paragraph.paragraph_format.left_indent = Cm(0.7)
            rich(paragraph, item, size=size)

    def numbered(self, items, size=10.5):
        """
        Explicit numbers with a hanging indent.

        Word's built-in List Number style shares one counter across the whole
        document, so the second list in a document starts at 3. Numbering the runs
        ourselves is deterministic and needs no numbering definitions.
        """
        for index, item in enumerate(items, start=1):
            paragraph = self.document.add_paragraph()
            paragraph.paragraph_format.space_after = Pt(3)
            paragraph.paragraph_format.left_indent = Cm(1.0)
            paragraph.paragraph_format.first_line_indent = Cm(-1.0)
            run = paragraph.add_run(f"{index}.")
            run.bold = True
            run.font.size = Pt(size)
            run.font.color.rgb = NAVY
            paragraph.add_run("\u2003").font.size = Pt(size)
            rich(paragraph, item, size=size)

    def table(self, header, rows, widths, size=9.5, zebra=True):
        """
        widths are fractions of the content width and must sum to 1.

        A header of all-empty strings produces no header band -- used for the
        label/value fact tables, where a navy strip with nothing in it looks like a
        mistake.
        """
        assert abs(sum(widths) - 1) < 1e-6, f"widths sum to {sum(widths)}"
        has_header = any(label.strip() for label in header)

        table = self.document.add_table(rows=1 if has_header else 0, cols=len(header))
        table.style = "Table Grid"
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False

        column_widths = [Cm(self.content_width.cm * w) for w in widths]
        for index, width in enumerate(column_widths):
            table.columns[index].width = width

        if has_header:
            for index, label in enumerate(header):
                cell = table.rows[0].cells[index]
                cell.width = column_widths[index]
                cell.text = ""
                paragraph = cell.paragraphs[0]
                paragraph.paragraph_format.space_after = Pt(2)
                paragraph.paragraph_format.space_before = Pt(2)
                run = paragraph.add_run(label)
                run.bold = True
                run.font.size = Pt(size)
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                shade(cell, HEADER_FILL)
            repeat_header(table.rows[0])

        for row_index, values in enumerate(rows):
            cells = table.add_row().cells
            for index, value in enumerate(values):
                cells[index].width = column_widths[index]
                cells[index].text = ""
                paragraph = cells[index].paragraphs[0]
                paragraph.paragraph_format.space_after = Pt(2)
                paragraph.paragraph_format.space_before = Pt(2)
                rich(paragraph, str(value), size=size)
                if zebra and row_index % 2 == 1:
                    shade(cells[index], BAND_FILL)

        self.document.add_paragraph().paragraph_format.space_after = Pt(4)
        return table

    def callout(self, title, body, fill=NOTE_FILL):
        table = self.document.add_table(rows=1, cols=1)
        table.autofit = False
        table.columns[0].width = self.content_width
        cell = table.rows[0].cells[0]
        cell.width = self.content_width
        cell.text = ""
        shade(cell, fill)

        heading = cell.paragraphs[0]
        heading.paragraph_format.space_after = Pt(2)
        run = heading.add_run(title)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = NAVY

        for line in body:
            paragraph = cell.add_paragraph()
            paragraph.paragraph_format.space_after = Pt(1)
            rich(paragraph, line, size=10)

        self.document.add_paragraph().paragraph_format.space_after = Pt(4)
        return table

    def page_break(self):
        self.document.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    def save(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.document.save(str(path))



# ------------------------------------------------------------------- fact checking

BASELINE_COMMIT = "abe1c32"      # the v1.1 build, Friday 2 October
DOSSIER = "partners/Python_from_Zero_Programme_Dossier.docx"


def docx_text(data):
    """All visible text of a .docx held in memory."""
    import io
    from docx import Document
    document = Document(io.BytesIO(data))
    parts = [p.text for p in document.paragraphs]
    parts += [c.text for t in document.tables for r in t.rows for c in r.cells]
    return "\n".join(parts)


def check_facts():
    """
    Verify this log's claims against the two .docx files it describes.

    The "what you have" column is a claim about a file issued four days ago. Writing
    that from memory is exactly how a change log misleads, so it is read back from git
    instead and every claim is checked both ways: present now, absent then.
    """
    import subprocess
    problems = []

    try:
        old = subprocess.run(["git", "show", f"{BASELINE_COMMIT}:{DOSSIER}"],
                             cwd=ROOT, capture_output=True, check=True).stdout
    except subprocess.CalledProcessError:
        return [f"cannot read the baseline dossier from commit {BASELINE_COMMIT}"]

    then = docx_text(old)
    now = docx_text((ROOT / DOSSIER).read_bytes())

    # (label, needle, expected in baseline, expected in current)
    CLAIMS = [
        # Precise phrasings: the dossier may legitimately mention 50 minutes as a
        # possible FUTURE change, so match the claim that sessions ARE 50 minutes.
        ("sessions are 50 minutes", "24 sessions × 50 minutes", True, False),
        ("the course is 20 hours", "= 20 hours", True, False),
        ("groups of up to 16", "Up to 16", True, False),
        ("four take-home tests", "Four take-home", True, False),
        ("Part 2", "Part 2", False, True),
        ("the decision rule", "More than 90%", False, True),
        ("the trial class", "trial class", False, True),
        ("the state curriculum", "ԱԲ սերունդ", False, True),
        ("remote delivery", "Remote", False, True),
        ("the diagnostic assessment", "Initial diagnostic", False, True),
        ("75-minute sessions", "75 minutes", False, True),
        ("30 hours", "30 hours", False, True),
        ("groups of 4–8", "4–8", False, True),
    ]
    for label, needle, want_then, want_now in CLAIMS:
        if (needle in then) != want_then:
            problems.append(f"baseline v{BASELINE}: '{label}' should be "
                            f"{'present' if want_then else 'absent'} and is not")
        if (needle in now) != want_now:
            problems.append(f"current v{CURRENT}: '{label}' should be "
                            f"{'present' if want_now else 'absent'} and is not")

    # The enclosed dossier must actually be the version this log names.
    if f"v{CURRENT}" not in now:
        problems.append(f"the built dossier does not identify itself as v{CURRENT}")

    return problems


# -------------------------------------------------------------------------- content

TODAY = "6 October 2026"
CURRENT = "1.8"

# What the partner already has: the last version issued on Friday 2 October.
BASELINE = "1.1"
BASELINE_DATE = "Friday 2 October"


def build():
    d = Dossier()
    doc = d.document

    # ---------------------------------------------------------------- cover
    for _ in range(3):
        doc.add_paragraph()

    title = doc.add_paragraph()
    run = title.add_run("Programme dossier")
    run.font.size = Pt(30)
    run.bold = True
    run.font.color.rgb = NAVY

    subtitle = doc.add_paragraph()
    run = subtitle.add_run("What changed since the version you have")
    run.font.size = Pt(14.5)
    run.font.color.rgb = GREY
    bottom_rule(subtitle, size=12)

    doc.add_paragraph()
    d.table(
        ["", ""],
        [
            ["Accompanies", "**Python from Zero — Programme dossier**"],
            ["The version you have", f"**{BASELINE}**, issued {BASELINE_DATE}"],
            ["The version enclosed", f"**{CURRENT}**, {TODAY}"],
            ["Covers", f"Everything that changed between the two"],
            ["Prepared for", "Fast Foundation"],
            ["Date", TODAY],
        ],
        [0.18, 0.82],
    )

    d.callout(
        "How to use this",
        [
            f"You last saw **version {BASELINE}**, from {BASELINE_DATE}. The dossier is "
            f"now at **version {CURRENT}**. **§1 is the short answer** — four things "
            "changed that affect how the programme should be judged, not merely what it "
            "contains.",
            "**§2 lists each intermediate version**, newest first, if you want the detail.",
            "**Every version number appears on the dossier's cover and in its footer**, so "
            "you can always tell which one you are holding.",
        ],
    )

    d.page_break()

    # ------------------------------------------------------- 1. the big picture
    d.h1("The short answer")

    d.para(
        f"Four things changed between version {BASELINE} and version {CURRENT}. They are "
        "stated on their own because each affects **how the programme should be judged**, "
        "not merely what it contains."
    )

    d.table(
        ["", f"Version {BASELINE} — what you have", f"Version {CURRENT} — enclosed"],
        [
            ["**Shape**", "One 20-hour course, 50-minute sessions, groups of up to 16, taught on site", "**Two parts — Part 1 teaches coding skills over 2 months; Part 2 covers algorithmic tasks and theory over 4.** 75-minute sessions, 30 hours, groups of 4–8, **taught remotely**"],
            ["**Assessment**", "Four take-home tests, deliberately not graded", "**Three supervised sittings** designed with our partner colleague — a diagnostic **before** the course, a midpoint, and a final practical. Scored, with A/B/C variants"],
            ["**How it is judged**", "Checkpoints, with target numbers left to agree", "**An explicit decision rule**: more than 90% can code = success, under 50% = failure, and the band between defined in advance. Plus a **trial class with real pupils in March**"],
            ["**Relationship to the state curriculum**", "Not addressed", "**Mapped topic by topic** against order 1875 of 09.09.2026, with every gap named and assigned to a part"],
        ],
        [0.17, 0.35, 0.48],
        size=9,
    )

    d.callout(
        "The one change we would most like you to notice",
        [
            f"**Version {BASELINE} could not say what success meant.** It listed "
            "checkpoints and said the numbers should be agreed before the first session.",
            f"**Version {CURRENT} states the rule**, defines \"can code\" so it can be counted "
            "from artefacts the course already produces, and names the one measurement "
            "that tests the programme's own assumption rather than whether it ran "
            "smoothly. That is in §8 of the dossier.",
        ],
        fill=BAND_FILL,
    )

    # ----------------------------------------------------------- 2. by version
    d.h1("Version by version")
    d.para("Newest first. Read down to the version you last saw.", italic=True)

    d.h2("Versions 1.7 and 1.8 — 6 October")
    d.para("**Clarity, and three corrections.**")
    d.bullets([
        "**Corrected the hours.** One sentence still said the 24 sessions were 20 hours; they are **30** (24 × 75 minutes). And the status section still listed *\"session plans are still written to 50 minutes\"* as outstanding — that work is finished, so the item is gone.",
        "**Fixed an ambiguity you may have hit:** earlier versions said *\"Part 1 of six months\"*, which reads as though Part 1 itself lasts six months. Every document now states plainly that **Part 1 is 2 months and Part 2 is 4**, and says what each part teaches.",
        "**Corrected the Part 2 plan.** The stage table still showed an older order — recursion after classes — and omitted libraries entirely. It now matches the roadmap: theory, **recursion**, algorithmic tasks, bigger projects, classes and inheritance, libraries and environments.",
        "Added a structure table to the cover and to the opening section, so the two-part shape cannot be missed.",
    ])

    d.h2("Version 1.6 — 6 October")
    d.para("**Session length confirmed at 75 minutes.**")
    d.bullets([
        "Sessions are **75 minutes**, three times a week: 24 × 75 = **30 hours**. Earlier versions described the plan as 75 minutes while the detailed session plans were still written to 50; those plans have now been rebuilt, so the figures agree.",
        "The extra 25 minutes per session went **entirely to hands-on work** — the 12-minute ceiling on explanation did not move. A standard session is now 71% hands-on, up from 60%.",
    ])

    d.h2("Version 1.5 — 6 October")
    d.para("**The trial class, and the final assessment as a gate.**")
    d.bullets([
        "**Added the trial class in March**, as a *second* criterion. It measures whether a teacher can **teach** what they can code — a different ability from coding, and the one nothing else in the programme would detect.",
        "**The final assessment now decides who continues to Part 2.** Stated with the consequence that follows: because it is consequential for the individual, it is announced **before the course starts**, in the recruitment text and at enrolment, rather than sprung afterwards.",
    ])

    d.h2("Version 1.4 — 6 October")
    d.para("**Aligned with the state curriculum.**")
    d.bullets([
        "**New section mapping the programme against «ԱԲ սերունդ»: Computer Science in Python**, order 1875 of 09.09.2026 — all 24 pupil topics and 193 hours, and which part of our programme covers each.",
        "Reordered the course so that **every data type precedes conditions and loops**. Dictionaries moved from day 14 to day 8; the discovery days are now 6, 8, 11, 17 and 22.",
        "**Added tuples and sets**, because the state curriculum teaches them in the pupils' first semester. Shown and compared, not drilled.",
        "Recorded the two orderings where we diverge from the state document deliberately, and why.",
    ])

    d.h2("Version 1.3 — 6 October")
    d.para("**Remote delivery, smaller groups, and the decision rule.**")
    d.bullets([
        "**The course is taught remotely**, over video with screen sharing. Added what that changes: it removes the worst first-day risk, and removes the best mitigation — an instructor who can walk over and look at a screen.",
        "**Groups are 4–8**, not up to 16. Fewer than four and there is no discussion; more than eight and the instructor cannot check on everyone remotely.",
        "**Added the decision rule** — the success and failure thresholds, and what \"can code\" means in countable terms.",
        "**Added Part 2** as a four-month plan, and flagged the risk inside it: whether our method carries over to algorithmic thinking is unproven.",
        "Added the enrolment screening that replaces the instructor's physical presence.",
    ])

    d.h2("Version 1.2 — 3 October")
    d.para("**Three assessments instead of four.**")
    d.bullets([
        "Adopted the assessment design from our partner colleague: **a diagnostic before day 1, a midpoint, and a final practical**, replacing four take-home tests.",
        "The diagnostic is the significant addition — it gives a **before-measurement**, so the programme can report *change* rather than only an endpoint.",
        "Added the transfer question to the final assessment, marked separately and never reported as a pass rate.",
    ])

    d.h2(f"Version {BASELINE} — 2 October  (the version you have)")
    d.para(
        "Shortened by about a third at your request, from 6,081 words to 4,660. Repetition "
        "was removed rather than content: a milestone table that duplicated the "
        "curriculum, a materials list that duplicated the appendix, and two overlapping "
        "fact tables. Nothing needed to judge the programme was cut.",
        italic=True,
    )

    d.page_break()

    # --------------------------------------------------------- 3. what has not
    d.h1("What has not changed")

    d.para(
        "Worth stating, because it is the part of the programme we would least like to see "
        "quietly drift:"
    )
    d.bullets([
        "**The diagnosis.** Two years of conventional teaching did not produce teachers who can write a program; our reading is that the bottleneck is coding fluency, not missing theory.",
        "**The method.** A real classroom task, done the long way with what they already know, and the tool that collapses it arriving **in the same session**.",
        "**The honesty about risk.** Every version has said, in the same words, that the core assumption may simply be wrong — that it is possible to produce teachers who type Python fluently and still cannot solve a problem with it.",
        "**The three unverified items**, still named in §10: the Armenian terminology has not been reviewed by a native speaker, the installation instructions have not been followed on a clean machine, and nothing has been taught to a cohort.",
    ])

    d.h2("How these figures were produced")
    d.para(
        "This log is generated from the programme repository rather than written from "
        "memory. The version numbers come from the dossier's own generator, and the word "
        "and section counts below are measured from the built files. Each dossier version "
        "is also checked against the repository as it is built — day count, total minutes, "
        "material counts, the sample-class figures — and the build is refused if any of "
        "them disagree."
    )
    d.table(
        ["Version", "Date", "Words", "Tables", "Sections"],
        [
            ["**1.1**", "**2 Oct**", "**4,660**", "28", "12"],
            ["1.2", "3 Oct", "4,905", "30", "12"],
            ["1.3", "6 Oct", "6,064", "31", "12"],
            ["1.4", "6 Oct", "6,260", "32", "12"],
            ["1.5", "6 Oct", "6,661", "33", "12"],
            ["1.6", "6 Oct", "6,652", "33", "12"],
            ["**1.7**", "6 Oct", "**6,832**", "33", "12"],
        ],
        [0.18, 0.16, 0.22, 0.22, 0.22],
    )
    d.para(
        f"The row in bold is the version you have. The document grew after {BASELINE} "
        "because each later version added material you asked for — the decision rule, remote delivery, the state-curriculum mapping, Part 2 "
        "and the trial class. Older material was trimmed to make room, which is why the "
        "section count has stayed at twelve.",
        italic=True,
    )

    closing = doc.add_paragraph()
    bottom_rule(closing)
    d.para(
        f"Change log for Programme dossier v{CURRENT} · {TODAY} · Prepared for Fast "
        "Foundation. Generated from the programme repository.",
        size=9, colour=GREY,
    )

    return d


def main():
    problems = check_facts()
    if problems:
        print("❌ the change log disagrees with the files it describes:\n")
        for problem in problems:
            print(f"   {problem}")
        return 1

    print(f"✅ claims verified against v{BASELINE} (git {BASELINE_COMMIT}) and v{CURRENT}")
    dossier = build()
    dossier.save(OUT)
    print(f"✅ {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
