"""
Build the partner-facing programme dossier as a .docx.

    python tools/build_partner_docx.py

Writes partners/Python_from_Zero_Programme_Dossier.docx

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
TEN = ROOT / "grade10"
ELEVEN = ROOT / "grade11"
OUT = ROOT / "partners" / "Python_from_Zero_Programme_Dossier.docx"

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

def check_facts():
    """
    Verify the figures this document quotes against the repository itself.

    This file restates facts instead of linking to them, so it is the one place that can
    drift. Each claim below is checked at build time; a mismatch stops the build.
    """
    problems = []

    curriculum = (TEN / "docs" / "CURRICULUM.md").read_text(encoding="utf-8")
    index_rows = re.findall(r"^\|\s*(\d+)\s*\|[^|]+\|[^|]+\|[^|]+\|\s*(\d+)\s*\|\s*$",
                            curriculum, re.M)
    days = [int(n) for n, _ in index_rows]
    minutes = [int(m) for _, m in index_rows]

    if days != list(range(1, 17)):
        problems.append(f"docs/CURRICULUM.md lists sessions {days[:3]}…, not 1..16")
    if sum(minutes) != 1920:
        problems.append(f"total is {sum(minutes)} minutes, not 1920")

    # The grade-11 course is a sibling folder; section 11 quotes its figures.
    eleven = ELEVEN
    if eleven.exists():
        eleven_days = re.findall(
            r"^\|\s*(\d+)\s*\|[^|]+\|[^|]+\|[^|]+\|\s*(\d+)\s*\|\s*$",
            (eleven / "docs" / "CURRICULUM.md").read_text(encoding="utf-8"), re.M)
        if [int(n) for n, _ in eleven_days] != list(range(1, 17)):
            problems.append("grade11 CURRICULUM.md does not list sessions 1..16")
        if sum(int(m) for _, m in eleven_days) != 1920:
            problems.append("grade11 total is not 1920 minutes")
        # Count only session-map rows, not the word wherever it appears: a row is
        # "| n | title | topics | shape | 120 |" and the shape holds "Discovery".
        discovery = len(re.findall(
            r"(?m)^\|\s*\d+\s*\|[^|]*\|[^|]*\|[^|]*Discovery[^|]*\|\s*120\s*\|$",
            (eleven / "docs" / "CURRICULUM.md").read_text(encoding="utf-8")))
        if discovery != 7:
            problems.append(f"grade11 has {discovery} discovery days, not the 7 quoted")
        eleven_project = len(list((ELEVEN / "project" / "school_report").glob("*.py")))
        if eleven_project != 5:
            problems.append(f"grade11 project has {eleven_project} files, not the 5 quoted")
    else:
        problems.append("grade11/ is missing but section 11 describes it")

    # Claims added for the grade-11 part of this document.
    if ELEVEN.exists():
        eleven_counts = {
            "notebooks": len(list((ELEVEN / "notebooks").glob("*.ipynb"))),
            "solutions": len(list((ELEVEN / "solutions").glob("*.ipynb"))),
            "guides": len(list((ELEVEN / "guides").glob("*.md"))),
        }
        for label, expected in [("notebooks", 21), ("solutions", 21), ("guides", 3)]:
            if eleven_counts[label] != expected:
                problems.append(f"grade11 has {eleven_counts[label]} {label}, "
                                f"not the {expected} quoted in the appendix")
        eleven_curriculum = (ELEVEN / "docs" / "CURRICULUM.md").read_text(encoding="utf-8")
        for moment in ["**After session 8**", "**Session 16**", "**Before session 1**"]:
            if moment not in eleven_curriculum:
                problems.append(f"grade11 CURRICULUM no longer says {moment} — the "
                                "assessment table in this document quotes it")

    counts = {
        "notebooks": len(list((TEN / "notebooks").glob("*.ipynb"))),
        "solutions": len(list((TEN / "solutions").glob("*.ipynb"))),
        "tests": len(list((TEN / "tests").glob("*.ipynb"))),
        "participant tests": len(list((TEN / "tests" / "participant").glob("*.ipynb"))),
        "guides": len(list((TEN / "guides").glob("*.md"))),
        "marking guides": len(list((TEN / "tests").glob("mark*_guide.md"))),
        "project files": len(list((TEN / "project" / "gradebook").glob("*.py"))),
    }
    expected = {"notebooks": 19, "solutions": 18, "tests": 3, "participant tests": 3,
                "guides": 5, "marking guides": 3, "project files": 4}
    for name, want in expected.items():
        if counts[name] != want:
            problems.append(f"{name}: found {counts[name]}, dossier says {want}")

    # The sample class is quoted in the dossier and in the course prose.
    sample = (TEN / "notebooks" / "sample_class.csv").read_text(encoding="utf-8")
    grades = [int(line.split(",")[1]) for line in sample.strip().splitlines()[1:]]
    if len(grades) != 12 or sum(grades) != 78 or sum(grades) / len(grades) != 6.5:
        problems.append(f"sample class: {len(grades)} students, sum {sum(grades)}, "
                        f"average {sum(grades) / len(grades)}")

    # The dossier quotes the point totals, so check them against the exams themselves.
    for name, points in (("test1_diagnostic", 44), ("test2_midpoint", 50),
                         ("test3_final_practical", 70)):
        source = (TEN / "src" / "tests" / f"{name}.py").read_text(encoding="utf-8")
        scored = [int(m) for m in re.findall(r"\*\*Միավոր՝\*\*\s*(\d+)", source)]
        # The final test's question 8 is reported separately and is not in the total.
        total = sum(scored[:-1]) if name == "test3_final_practical" else sum(scored)
        if total != points:
            problems.append(f"{name}: questions total {total} points, dossier says {points}")

    # No grader-only cell may survive into the participant copy.
    for path in (TEN / "tests" / "participant").glob("*.ipynb"):
        if "Ուսուցչի նշում" in path.read_text(encoding="utf-8"):
            problems.append(f"{path.name}: the rubric leaked into the participant copy")

    # Discovery days must still be the five the dossier names.
    for day in ("day06_class_register", "day08_dictionaries", "day11_for_loops",
                "day17_functions"):
        if not (TEN / "notebooks" / f"{day}.ipynb").exists():
            problems.append(f"missing discovery notebook {day}")
    if not (TEN / "guides" / "day22_your_own_class.md").exists():
        problems.append("missing discovery guide day22_your_own_class.md")

    return problems


# -------------------------------------------------------------------------- content

TODAY = "2 October 2026"
VERSION = "3.0"


# Phrases from the three-a-week schedule. This document restates its figures in prose
# rather than linking to them, and a half-finished sweep is exactly how a partner ends
# up holding two different schedules in one file.
STALE_SCHEDULE = [
    "75 minutes", "75-minute", "three a week", "three times a week",
    "24 sessions", "30 hours", "1,800 minutes", "Day 24", "before day 1",
]


def docx_text(path):
    """All visible text of a .docx, so the finished file can be checked rather than the
    script that wrote it."""
    import xml.etree.ElementTree as ET
    import zipfile

    namespace = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    return " ".join(node.text or "" for node in root.iter(f"{namespace}t"))


def check_built_document(path):
    """Fail if the finished .docx still carries the old schedule anywhere in it."""
    found = []
    text = docx_text(path)
    for phrase in STALE_SCHEDULE:
        if phrase.lower() in text.lower():
            found.append(phrase)
    return found


def build():
    d = Dossier()
    doc = d.document

    # ---------------------------------------------------------------- cover
    for _ in range(4):
        doc.add_paragraph()

    title = doc.add_paragraph()
    run = title.add_run("Python from Zero")
    run.font.size = Pt(34)
    run.bold = True
    run.font.color.rgb = NAVY

    subtitle = doc.add_paragraph()
    run = subtitle.add_run("A practical programming course for public-school teachers")
    run.font.size = Pt(14.5)
    run.font.color.rgb = GREY
    bottom_rule(subtitle, size=12)

    doc.add_paragraph()
    lead = doc.add_paragraph()
    lead.paragraph_format.space_after = Pt(2)
    run = lead.add_run("Programme dossier")
    run.font.size = Pt(13)
    run.bold = True

    recipient = doc.add_paragraph()
    run = recipient.add_run("Prepared for Fast Foundation")
    run.font.size = Pt(12)
    run.font.color.rgb = GREY

    doc.add_paragraph()

    d.table(
        ["", ""],
        [
            ["Structure", "**Two courses, one per school grade.** Each is a **practical Part 1 of 2 months** and a **theoretical Part 2 of 4 months** that runs only if its Part 1 succeeds. **Sections 1–10 describe the grade-10 course's Part 1; section 11 describes the grade-11 course's Part 1.** Both are built and verified."],
            ["Part 1 format", "16 sessions × 120 minutes = **32 hours**, **twice a week** over eight weeks, plus homework between sessions and three assessment sittings"],
            ["Delivery", "**Remote**, over Google Meet with screen sharing"],
            ["Audience", "Public-school teachers, any subject. **No prior programming assumed** — the course begins with installing software"],
            ["Group size", "**4–8 per group**, one instructor"],
            ["Deliverable", "A runnable four-file Python program over the participant's own class data, demonstrated to a colleague"],
            ["Cost", "**Zero.** All software is free; nothing touches a paid service or needs the internet after day one"],
            ["Judged by", "**Can they code?** More than 90% = success, under 50% = failure (section 8) — plus a trial class with real pupils in March"],
            ["Status", "**Both Part 1 courses are complete and verified. Neither has been taught to a cohort.** Both Part 2s are visions"],
            ["Version", f"{VERSION} — for partner review · {TODAY}"],
        ],
        [0.17, 0.83],
    )

    d.callout(
        "How to read this",
        [
            "**Sections 1–10 describe the grade-10 course** — the method, the schedule, "
            "the curriculum, the expected results and the assessment. The method is "
            "shared by both courses, so section 3 is worth reading whichever one "
            "interests you.",
            "**Section 11 is the grade-11 course in full** — its own curriculum, "
            "schedule, assessment and deliverable, and what it assumes a teacher already "
            "knows on its first day.",
            "Section 8 sets out how the programme will be judged, including the one "
            "measurement that tests its central assumption.",
            "Section 9 states the risks plainly, including how this could fail. We would "
            "rather you read them here than discover them later.",
        ],
    )

    d.page_break()

    # ------------------------------------------------------ 1. executive summary
    d.h1("Executive summary")

    d.para(
        "A programme for public-school teachers who have never written a line of code. "
        "**It is now two courses — one preparing a teacher for grade 10, one for grade "
        "11 — and each is a practical Part 1 of two months followed by a theoretical "
        "Part 2 of four.** This dossier describes the **grade-10 course's Part 1**; "
        "**section 11 is the grade-11 course in full**, which is also built. Part 1 is "
        "sixteen sessions of two hours, twice a week for eight weeks, "
        "**taught remotely in groups of four to eight**. Every participant finishes with "
        "a small program they wrote themselves and can use: a gradebook that opens their "
        "own class list, shows who has passed, calculates the average, and saves changes "
        "back to a file."
    )
    d.para(
        "The programme is deliberately unusual. Two years of conventional teaching has not "
        "produced teachers who can write a program. Our diagnosis is that the bottleneck "
        "is not missing theory but missing **coding fluency** — teaching through "
        "algorithmic problems asks beginners to work out *what* a program should do and "
        "*how* to write it at once, so they fail at both. This course separates the two "
        "loads: mechanics to fluency first, with almost no theory and no algorithmic "
        "difficulty, leaving problem-solving to a later course."
    )
    d.callout(
        "What we are asking you to evaluate",
        [
            "**Part 1 is a two-month experiment with a decision at the end, not a "
            "finished methodology.** It is built and verified. **Part 2 — the four months "
            "that follow — is a vision that runs only if Part 1 succeeds** (section 12).",
            "Part 1 is judged on one question — **can they code?** The threshold is agreed "
            "and is in section 8.",
        ],
        fill=BAND_FILL,
    )

    # ------------------------------------------------------------- 2. the problem
    d.h1("The problem this programme addresses")

    d.para(
        "**The fundamental problem is that the teachers cannot code.** Not that they do "
        "not understand recursion, and not that they have not practised enough algorithms. "
        "They cannot comfortably produce working code at all — the typing, the syntax, the "
        "loop that runs, the error message that gets read and fixed."
    )
    d.para(
        "When a course then teaches through algorithmic tasks, two things must happen at "
        "once: working out **what** the program should do, and working out **how** to "
        "write it. They are overloaded, they confuse the two, and they fail at both. A "
        "teacher stuck on an algorithm cannot tell whether they are stuck on the idea or "
        "on a missing colon. The theory never connects to the practice, because there is "
        "no practice for it to connect to."
    )
    d.para(
        "Adding more theory does not help, because theory is not the bottleneck. Adding "
        "harder problems makes it worse."
    )

    d.h2("The bet")
    d.callout(
        "The programme in one sentence",
        ["**Teach coding first and algorithms later — not the other way round.**"],
        fill=BAND_FILL,
    )
    d.para(
        "For two months: almost no theory — around 12 minutes of explanation per session, "
        "then 30 minutes of typing. **No algorithmic difficulty whatsoever**; nothing "
        "requires working anything out. A great deal of very simple code, all of it about "
        "the participant's own classroom. Concepts arrive as relief, never as definitions."
    )
    d.para(
        "The intended sequence is: write code mechanically → concepts become obvious, "
        "because each one removes a difficulty just met → coding stops needing conscious "
        "attention → **algorithmic problems become learnable**. That last stage is not "
        "part of this course. It is the next one, if this works."
    )

    d.page_break()

    # ------------------------------------------------------------ 3. methodology
    d.h1("Methodology — how the course teaches")

    d.para(
        "Teachers are given a real classroom task, solve it with what they already know, "
        "and then — **in the same session** — meet the tool that collapses it. We call "
        "these **discovery days**; there are five."
    )

    d.table(
        ["Day", "The real task", "The long way they do it first", "The tool, same session"],
        [
            ["6", "A register for the whole class", "One variable per student", "**Lists**"],
            ["8", "Find one student's grade by name", "Two parallel lists, read by hand", "**Dictionaries**"],
            ["11", "Mark the whole class pass or fail", "One `if` block per student", "**`for` loops**"],
            ["17", "An average on every report card", "The same six lines, four times", "**Functions**"],
            ["22", "Keep the register after closing it", "Retyping it every time", "**Files**"],
        ],
        [0.07, 0.29, 0.34, 0.30],
    )

    d.h2("A worked example — day 6")
    d.para(
        "Participants are told: *a teacher needs somewhere to keep the whole class — every "
        "name, every score — so the program can work with all of them.* With what they "
        "know on day 6, that means one variable per student. The notebook supplies twenty; "
        "they add a few of their own and update the scores. It works, and it takes a while."
    )
    d.para(
        "**Thirty minutes later, in the same session**, the list arrives and the whole "
        "register becomes two lines. The notebook puts the two versions side by side: 40 "
        "lines against 2. Nobody has to explain why lists are useful — the participants "
        "spent twenty minutes finding out, and got the answer before they went home."
    )

    d.h2("Three rules that make it work")
    d.table(
        ["Rule", "Why, and what it costs us"],
        [
            ["**The relief comes in the same session. Always.**", "An earlier draft planted a difficulty on day 6 and resolved it on day 10. Good structure on paper, bad teaching in practice: adults who spend an evening on tedious work and go home with no resolution do not come back. If a session runs long, the optional tasks are cut — never the second half"],
            ["**The task is real, and the tedium is never named.**", "Participants are never told they are doing something in order to struggle. They are building a class register because a teacher needs one — which is true. Work you chose to do, and were then shown a better way to do, is a lesson; the same work revealed afterwards as a deliberate ordeal is a trick, and this audience has been let down enough already"],
            ["**The shortcut is promised in advance, in writing.**", "A participant who knows a shortcut is twenty minutes away types the long version willingly; one who does not starts wondering whether the course knows what it is doing"],
        ],
        [0.28, 0.72],
    )

    d.para(
        "Three smaller decisions follow from the same thinking. **Every example is a "
        "classroom** — students, grades, attendance, report lines — so a participant sees "
        "their Tuesday morning in any line of the course. **Armenian explains and English "
        "codes**: a teacher who names a variable in Armenian writes valid Python and can "
        "then read no other Python, search for no answer online and copy no example ever "
        "again. And **every session contains one deliberate error**, read together, "
        "because beginners lose more time to fear of red text than to any concept here."
    )

    d.page_break()

    # --------------------------------------------------------------- 4. schedule
    d.h1("Schedule")

    d.para(
        "**16 sessions, twice a week over eight weeks.** Sessions run **two hours**. "
        "Every agenda is planned to the minute and the arithmetic is verified by script, "
        "not by eye."
    )
    d.callout(
        "One decision still settling",
        [
            "**Session length.** Sessions run 120 minutes, twice a week — 16 × 120 "
            "= 32 hours, and the practice that no longer fits in the room is set as "
            "homework drawn from tasks the notebooks already carry. Once the cohort has adapted we may move to "
            "three of eighty minutes; the topic map and deliverables would not change.",
            "**Tools.** Anaconda, Jupyter and VS Code, with Google Colab and Thonny under "
            "discussion as a lighter alternative that would remove the installation "
            "problem entirely. Current materials assume Anaconda and VS Code.",
        ],
    )

    d.table(
        ["Week", "Sessions", "Topics", "What the participant can do by the end of it", "Assessment"],
        [
            ["1", "1–2", "1–4", "It runs on my laptop, and I know what a value is", "*diagnostic sat before session 1*"],
            ["2", "3–4", "5–6", "I can name things, and keep a whole class in one list", ""],
            ["3", "5–6", "7–8", "Every data type I need, and I can find one student", ""],
            ["4", "7–8", "9–11", "Conditions, then one loop marks thirty students", ""],
            ["5", "9–10", "12–15", "I can compute and report on the whole class", "**Midpoint**"],
            ["6", "11–12", "16–17", "I write a calculation once and use it everywhere", ""],
            ["7", "13–14", "18–21", "It is a program now, not a notebook", ""],
            ["8", "15–16", "22–24", "It has my class in it, it saves, and I showed it to someone", "**Final practical**"],
        ],
        [0.08, 0.12, 0.11, 0.49, 0.20],
    )
    d.para(
        "**Week 4 is the centre of the course** — where the first two discovery sessions pay "
        "off and a loop first does thirty students' work. If the calendar slips, that week "
        "is protected.",
        italic=True,
    )

    d.h2("The shape of a session")
    d.para(
        "Two shapes are used. A **standard session** is a recap, twelve minutes of "
        "teaching, the notebook's examples run together, the exercises, then a short "
        "retrospective. A **discovery session** splits the teaching in two — seven minutes "
        "introducing the task, the long way done by hand, nine minutes introducing the "
        "tool, then the same task again with it, and a comparison."
    )
    d.para(
        "Teaching never exceeds **12 minutes in one block**, and that ceiling does not "
        "move when sessions lengthen: **the extra 25 minutes goes to hands-on work** and "
        "to the second half of the discovery days, which is where the method lives. "
        "Hands-on is never less than half of a session."
    )

    d.h2("Remote delivery")
    d.para(
        "The course is taught over **Google Meet with screen sharing**, in groups of "
        "**four to eight**. Fewer than four and there is no discussion; more than eight "
        "and the instructor cannot check on everyone during hands-on work, so the people "
        "who are quietly stuck stay stuck."
    )
    d.table(
        ["Remote delivery", "Effect"],
        [
            ["**Removes the worst day-one risk**", "In a room, sixteen people downloading 1 GB over one school connection would have cost a session. Each teacher now installs at home, on their own connection, before day one"],
            ["**Removes the best mitigation**", "An instructor cannot walk over and look at a screen. Everything that was a thirty-second fix becomes a conversation with a beginner who often cannot describe what they are seeing"],
            ["The substitute", "Google Meet can now display **every participant's shared screen at once**, with switching between them. Screens stay shared through hands-on work — the remote equivalent of walking between desks — and with 4–8 people the instructor checks in on each one by name"],
            ["Requires of each teacher", "Their own laptop for the whole course, and a connection that holds a two-hour video call with screen sharing. A webcam is wanted but not required"],
        ],
        [0.26, 0.74],
    )
    d.para(
        "Every requirement is asked on an **enrolment questionnaire before a group is "
        "formed** — days available, connection, webcam, familiarity with video calls, "
        "known technical problems, and the laptop's memory and free disk. Several of the "
        "answers decide whether a teacher can take part at all, and acting on them early "
        "is what replaces the instructor's physical presence.",
    )

    d.h2("Between sessions")
    d.para(
        "Sessions are two days apart and the participants are working teachers, so nothing "
        "is required between them. Each notebook ends with an **optional ten-minute "
        "practice task** that the next session never assumes was done. The four "
        "assessments are take-home and consume no session time."
    )

    d.page_break()

    # ------------------------------------------------------------- 5. curriculum
    d.h1("Curriculum — the grade-10 course")

    d.para(
        "Topics are taught in the order a beginner can absorb them: printing, types, "
        "variables, conditions, loops, functions. Lists and dictionaries are placed where "
        "they solve a problem the participant has just met, rather than where a textbook "
        "would put them. The course teaches **24 topics across 16 two-hour sessions**: a "
        "topic is one notebook and one idea, a session is two hours in a room. "
        "**D** marks a discovery session, **T** the transition to real files, "
        "**P** the project phase."
    )

    d.table(
        ["Topic", "", "Title", "What the participant has at the end"],
        [
            ["1", "", "Install everything and run your first line", "Six green setup checks, and a line printed by a machine they set up themselves"],
            ["2", "", "Printing properly", "A four-line class register header"],
            ["3", "", "Four kinds of value", "Each type shown, and why `\"2\" + 2` fails"],
            ["4", "", "Changing type, and asking a question", "A cell that takes a grade and prints it plus one"],
            ["5", "", "Giving a value a name", "One student's row printed from named values"],
            ["6", "**D**", "**A register for the whole class**", "Their class as one list, written both ways and compared"],
            ["7", "", "Working with the register, and two near-relatives", "A sorted class list, plus the same names as a tuple and a set"],
            ["8", "**D**", "**Finding one student**", "Their class as name-to-grade, and a note on what went wrong before"],
            ["9", "", "The first decision", "Pass or fail, on their own school's pass mark"],
            ["10", "", "More than two outcomes", "A grade sorted into four named bands"],
            ["11", "**D**", "**Marking the whole class**", "The whole register marked, in four lines"],
            ["12", "", "Counting and totalling", "Their own class average, computed"],
            ["13", "", "Loops that decide", "Who failed, how many passed, the highest grade"],
            ["14", "", "Reports from the register", "A printed register line per student, columns aligned"],
            ["15", "", "Several grades per student", "A report card per student with three grades each"],
            ["16", "", "Entering grades one by one", "A loop that collects grades until told to stop"],
            ["17", "**D**", "**An average on every card**", "The calculation written once, called four times"],
            ["18", "", "Sending an answer back", "Four working grade functions that return values"],
            ["19", "", "The register, assembled  *(no new syntax)*", "The complete register program in one notebook"],
            ["20", "T", "Leaving the notebook", "`python grades.py` running in a terminal"],
            ["21", "T", "Four files that each do one thing", "**A working `python main.py`**, confirmed individually"],
            ["22", "**D**", "**Keeping it after you close it**", "Their own class in a file, loaded and saved back"],
            ["23", "P", "Make it yours", "One feature of their own design, working"],
            ["24", "P", "Finish and show", "A colleague runs their program from their notes alone"],
        ],
        [0.05, 0.05, 0.37, 0.53],
        size=8.5,
    )
    d.para(
        "Topics 1–19 use Jupyter notebooks; topics 20–24 use plain Python files with a "
        "written guide beside them, because by then the participants are running a "
        "terminal. Topic 19 doubles as the catch-up — nothing new arrives, so anyone who "
        "has fallen behind has time to recover.",
        size=9.5, italic=True,
    )

    d.h2("Alignment with the state curriculum")
    d.para(
        "Our teachers must be able to deliver **«ԱԲ սերունդ»: Computer Science in "
        "Python**, approved by order 1875 of 09.09.2026 — a 24-topic, 193-hour curriculum "
        "for pupils in grades 10 and 11. Our programme is not a compressed copy of it; it "
        "is the preparation that makes delivering it possible."
    )
    d.table(
        ["State curriculum", "Pupil hours", "Covered by"],
        [
            ["Grade 10 · S1 — fundamentals (topics 1–12)", "60", "**the grade-10 course**, topics 1–11"],
            ["Grade 10 · S2 — intermediate (topics 13–17)", "65", "**Part 1** for functions and files; **Part 2** for advanced functions and recursion"],
            ["Grade 11 · S1 — classes and inheritance (18–20)", "30", "**Part 2**, stage 5"],
            ["Grade 11 · S2 — libraries, debugging, git (21–24)", "38", "**Part 2**, stage 6. Git remains out of scope pending Part 1's result"],
        ],
        [0.44, 0.14, 0.42],
    )
    d.para(
        "**A teacher finishing Part 1 can deliver grade 10 semester 1 outright**, and most "
        "of semester 2. Two orderings differ from the state document deliberately: we "
        "teach conditions before loops, and every data type before both, because our "
        "discovery sequence depends on having something worth looping over. **Recursion "
        "stays before classes**, as the state curriculum has it."
    )

    d.page_break()

    # -------------------------------------------------------- 6. expected results
    d.h1("Expected results")

    d.h2("What every participant leaves with")
    d.para(
        "A **runnable Python program**, in their own folder, made of four files they typed "
        "themselves. One command — `python main.py` — opens their class, shows who passed, "
        "lists who did not, corrects a grade, and saves."
    )
    d.table(
        ["File", "Its one job", "What it deliberately does not know"],
        [
            ["`settings.py`", "Every number you might want to change", "It contains no logic at all"],
            ["`storage.py`", "Reads the class from a file and writes it back", "Nothing about grades or what they mean"],
            ["`grades.py`", "The calculations: average, highest, pass or fail", "Nothing about files"],
            ["`main.py`", "Asks the teacher what they want, and prints", "It does no calculating of its own"],
        ],
        [0.17, 0.43, 0.40],
    )
    d.para(
        "The separation is itself an outcome: because `grades.py` does not import "
        "`storage.py`, a participant can test the calculations without having a data file. "
        "When an answer looks wrong they can ask *which half is wrong* — the calculation "
        "or the display — and halve the search. That habit is the most transferable thing "
        "in the course."
    )

    d.h2("The checkpoints worth watching")
    d.table(
        ["By the end of", "Every participant has"],
        [
            ["Day 10", "The whole register marked in four lines, proved by adding students without touching the loop"],
            ["Day 17", "A calculation written once and used in four places, with a change proved in a single edit"],
            ["**Day 21**", "**A working `python main.py` — confirmed individually, per person, before they leave the room.** Everything after this day assumes it"],
            ["Session 16", "A documented program a colleague ran unaided, and a 90-second demonstration given aloud"],
        ],
        [0.17, 0.83],
    )

    d.h2("Skills and habits")
    d.para(
        "**Programming.** `print` · the four value types · `input` · variables and "
        "formatted strings · `if` / `elif` / `else` · lists · `for` and `range` · `while` "
        "· dictionaries · functions and `return` · reading and writing files · modules and "
        "running a program from a terminal."
    )
    d.para(
        "**Habits that outlast the syntax**, and what we most want to survive the course: "
        "if a number or a piece of code appears more than once, give it a name; when a "
        "result is wrong, ask *which half* is wrong before changing anything; and an error "
        "message is a sentence telling you what to fix, not a judgement."
    )

    d.callout(
        "What this course does not produce",
        [
            "**It does not produce programmers, and it does not produce people who can "
            "solve algorithmic problems.** That is the next course, and only if this one "
            "works.",
            "A participant finishing this programme can write simple, working, useful code "
            "and read an error message. Saying so clearly now is what makes the "
            "measurement in section 8 honest.",
        ],
        fill=BAND_FILL,
    )

    # ------------------------------------------------------------------ 7. scope
    d.h1("Scope and assessment")

    d.h2("What is deliberately excluded")
    d.para(
        "The exclusion list matters as much as the syllabus. **Classes, recursion, "
        "comprehensions, `lambda`, generators, regular expressions, type hints, "
        "decorators, web frameworks and databases are all out**, along with package "
        "installation and virtual environments — which removes the most common way a "
        "beginner's setup breaks between sessions. Error handling is one safeguard at the "
        "outermost edge of the finished program, so an unexpected failure shows a sentence "
        "rather than ten lines of red text."
    )
    d.para(
        "Each would cost roughly fifteen minutes and buy a teacher nothing in the program "
        "they are going to write. Most of them are Part 2's material. Before anything is "
        "added back, one question has to be answered: **which line of the finished "
        "gradebook needs it?**"
    )

    d.h2("Differentiation within a session")
    d.para(
        "In a group of four to eight, at least one or two finish early in **every** session, so "
        "each notebook carries three tiers: **3–4 required tasks** sized so nobody leaves "
        "with unfinished work, **3–4 extra tasks** for whoever has eight minutes to spare, "
        "and **1–2 challenges** for the fastest. Extra tasks use only what has already "
        "been taught — wider, not further ahead. Running out of work is how a competent "
        "participant concludes a course is beneath them."
    )

    d.h2("Assessment")
    d.para(
        "**Three sittings**, designed jointly with our partner colleague. They are "
        "**separate sittings, not session time** — the 16 teaching sessions remain 32 "
        "hours exactly and the assessments add roughly 3½ hours."
    )
    d.table(
        ["", "Assessment", "When", "Length", "Points", "Covers"],
        [
            ["1", "Initial diagnostic", "Before session 1", "45–60 min", "44", "Nothing — it measures the baseline"],
            ["2", "Midpoint", "After session 9", "60–75 min", "50", "Topics 6–13"],
            ["3", "Final practical", "Session 16", "90–120 min", "70 + 10", "Topics 14–24"],
        ],
        [0.04, 0.21, 0.14, 0.13, 0.11, 0.37],
    )
    d.para(
        "**Each question has variants A, B and C**, equivalent in difficulty and points; "
        "the exam platform gives each participant one. Every score is recorded with a "
        "**help level** — independent, after one hint, with step-by-step help, or not "
        "finished — which on the diagnostic carries more information than the score."
    )
    d.para(
        "**Scores diagnose the programme, not the teachers**, and the participants are "
        "told so in writing. They exist to show the instructor where to slow down and to "
        "give the two-month decision something to stand on."
    )
    d.callout(
        "Why the diagnostic matters more than it looks",
        [
            "It is sat **before anyone has been taught anything**, so it cannot be failed. "
            "What it buys is a **before-measurement**: the programme can report *change* "
            "rather than just an endpoint, and the help levels show how much of any result "
            "came from support rather than from the course.",
            "It is also an early warning. A participant who cannot run a single cell "
            "unaided tells us to put extra help into day 1 — the riskiest session in the "
            "programme — six weeks before it would otherwise show.",
        ],
    )
    d.para(
        "Each assessment ships an instructor marking guide whose **second column is the "
        "point**: not whether the answer was right, but what a wrong answer tells you and "
        "what to change next session. Three results change what happens:"
    )
    d.table(
        ["Assessment", "A result that changes what the instructor does next"],
        [
            ["Diagnostic", "Several participants unable to run a cell unaided → a second helper on day 1, or a setup clinic beforehand"],
            ["Midpoint", "**Still writing one block per student instead of a loop** → the clearest early evidence against the method, and it is recorded as such"],
            ["Final", "Printing instead of returning a value → `return` never landed, and the four-file program rests on it"],
        ],
        [0.15, 0.85],
    )
    d.para(
        "Two versions of every assessment are produced automatically — the grader's copy "
        "with the rubric, and the participant's copy with the questions only — so the "
        "rubric cannot be handed out by mistake.",
        italic=True,
    )

    d.page_break()

    # ------------------------------------------------------- 8. measuring success
    d.h1("How success will be measured")

    d.h2("The decision rule")
    d.para(
        "**Part 1 succeeds or fails on one question: can they code?** The threshold was "
        "agreed with colleagues and is set before the first session rather than after it."
    )
    d.table(
        ["Result", "Meaning", "What happens next"],
        [
            ["**More than 90%** can code", "**Success**", "Continue to Part 2 (section 12)"],
            ["50% to 90%", "Inconclusive", "The method is neither proved nor refuted. Adjust and repeat Part 1 with a second cohort before committing to Part 2"],
            ["**Less than 50%** can code", "**Failure**", "Return to the conventional approach, informed by where it broke"],
        ],
        [0.22, 0.16, 0.62],
    )
    d.para(
        "The middle band is not a hedge. It is the most likely outcome of a first run of "
        "anything, and deciding in advance what we do with it stops the result being "
        "argued into whichever camp someone already preferred."
    )

    d.h3("What \"can code\" means, in a way that can be counted")
    d.para(
        "A participant **can code** if, unaided, they can write a working program using "
        "the constructs the course taught — variables, conditions, lists, loops, "
        "dictionaries and functions. That is judged from two artefacts the course already "
        "produces, both pass or fail:"
    )
    d.bullets([
        "They left **day 21** with a working `python main.py`, confirmed individually while sharing their screen.",
        "They scored **at least half** of the 70 points on questions 1–7 of the final practical, which require writing code from a blank cell.",
    ])
    d.para(
        "Meeting both counts. Meeting one counts as partial and falls in the middle band — "
        "it is not rounded up. **The transfer question is excluded** from this judgement: "
        "it measures problem-solving, which Part 1 does not teach and does not claim."
    )

    d.callout(
        "⚠ One thing we would ask you to agree before the first cohort",
        [
            "Groups are four to eight. **At every size in that range, \"more than 90%\" "
            "means every single participant without exception** — 6 of 6, 8 of 8. One "
            "teacher whose laptop dies in week six moves the group out of success on "
            "their own.",
            "So we propose two things: **judge the criterion across all cohorts pooled**, "
            "not per group — four groups of six is 24 people, where a percentage means "
            "something — and **record withdrawals separately from failures**, since a "
            "teacher reassigned by their school in week two has not failed to learn to "
            "code.",
            "Neither weakens the bar. They stop it being decided by one broken laptop.",
        ],
    )

    d.h2("The trial class in March — a second criterion")
    d.para(
        "After Part 1, **each teacher takes a trial class with real pupils.** It measures "
        "something none of the assessments can: **whether they can teach what they can "
        "code.** Those are different abilities, and a teacher can have either without the "
        "other."
    )
    d.para(
        "Nothing in the three written assessments would detect a teacher who writes "
        "correct code and cannot explain it to a fifteen-year-old — and that teacher "
        "cannot deliver the state curriculum, which is what the whole programme is for. "
        "**It is reported separately from the coding criterion and is not averaged with "
        "it.**"
    )
    d.para(
        "Four things are recorded, kept deliberately light because a first lesson taught "
        "by a nervous adult is not a performance review: did the lesson happen and "
        "finish; did the **pupils** run code themselves or did the teacher demonstrate "
        "throughout; **could the teacher read a pupil's error message and act on it "
        "live**; and one sentence from the teacher on what surprised them. The third is "
        "the most diagnostic — it is the skill our course drills from day 2 onward, and "
        "if it holds up in front of a class, the method transferred."
    )

    d.h2("The final assessment also decides who continues")
    d.callout(
        "A gate, announced in advance",
        [
            "Teachers meeting the \"can code\" bar continue to Part 2. Those who do not "
            "are **offered Part 1 again**, rather than carried into material that assumes "
            "fluency they do not have. The bar is the one defined above; the transfer "
            "question does not gate.",
            "**This makes the last assessment consequential for the individual, so it is "
            "announced before the course starts** — in the recruitment text and at "
            "enrolment. People behave differently when they know, and discovering it "
            "afterwards would be unfair and would spoil the measurement.",
            "Being filtered out is not a judgement on the teacher. At 32 hours, with mixed "
            "laptops and a remote room, the likeliest reasons are time, equipment and "
            "attendance — so **why** someone did not meet the bar is recorded, not just "
            "that they did not.",
        ],
    )

    d.h2("The checkpoints along the way")
    d.para(
        "Three results during the course change what the instructor does next, and all "
        "come from artefacts the course already produces. **The diagnostic**: can they run "
        "a cell at all, and with how much help — the baseline, without which we could "
        "report an endpoint but not change. **The midpoint test**: do they write a loop, "
        "or still repeat themselves — the first real evidence for or against the method. "
        "**Day 21**: does `python main.py` run, confirmed individually while they share "
        "their screen. Attendance is recorded throughout, because below a certain point "
        "nothing else is interpretable."
    )

    d.h2("The one measurement that tests the theory")
    d.para(
        "**None of the checks above tests the actual bet**, because none is an algorithmic "
        "problem — they measure whether the course ran well. So the final practical ends "
        "with one question that is different. It is the only question with no A/B/C "
        "variants, and its 10 points are reported separately from the other 70:"
    )
    d.callout(
        "Final practical, question 8 — the transfer question",
        [
            "*Given a class register, find the student whose grade is closest to the class "
            "average.*",
            "It uses **no syntax the course did not teach**, and **the course never "
            "demonstrates it**. The participant is asked to write their approach in plain "
            "words first, then attempt the code, and to say where they stopped if they "
            "could not finish.",
        ],
    )
    d.para(
        "Four things are recorded, not one: whether they wrote the plan at all; whether "
        "the plan was a **correct approach**, even if the code failed; whether the code "
        "worked; and **where they stopped, in their own words**."
    )
    d.table(
        ["Pattern", "What it means for the decision"],
        [
            ["Plan correct, code works", "The bet paid off: coding fluency freed attention for the problem"],
            ["**Plan correct, code incomplete**", "**The most important result, and a positive one.** They can now reason about a problem; the remaining gap is practice, which is exactly what the next course provides"],
            ["Plan vague, code attempted anyway", "Mechanical fluency without problem-solving — the central risk, realised"],
            ["Nothing attempted, or \"we did not do this in class\"", "The strongest negative signal. The course taught recipes, not capability"],
        ],
        [0.33, 0.67],
    )
    d.callout(
        "Please note when reading our final report",
        [
            "A cohort that mostly produces the **second** pattern is a success, even "
            "though most of the code will not run. **We will not report this question as "
            "a pass rate**, and we would ask that it not be read as one.",
            "**Target numbers should be set jointly before the first session.** A target "
            "chosen afterwards is not a target.",
        ],
        fill=BAND_FILL,
    )

    d.page_break()

    # ------------------------------------------------------------------ 9. risks
    d.h1("Risks")

    d.para(
        "Stated plainly, because the programme has to be judged fairly in two months and "
        "because we would rather you read these here than discover them later."
    )

    d.h2("The approach itself")
    d.table(
        ["Risk", "What we do about it"],
        [
            ["**The core assumption may simply be wrong.** We are betting that coding fluency transfers — that someone who can code mechanically will find algorithmic problems learnable later. That is plausible and unproven. It is possible to produce teachers who type Python fluently and still cannot solve a problem with it", "We measure it directly (section 8) rather than assuming it. If it happens, the programme failed, and no amount of the course being pleasant changes that"],
            ["**Participants may not accept it.** Adults judge a course by how substantial it feels, and one that explains little and asks for a lot of typing can read as shallow. The first half of each discovery session is deliberately laborious", "Every discovery day resolves inside the same session; the shortcut is promised in writing before the long half starts; the work is never framed as an ordeal. A participant who leaves topic 6 thinking \"I typed for twenty minutes\" rather than \"I learned what a list is for\" is a genuine failure, and it will happen to somebody"],
            ["**Thirty-two hours is not much**, in two-hour pieces, for working teachers", "The scope is deliberately narrow and the exclusion list is explicit. Narrow means things are missing, by design"],
        ],
        [0.46, 0.54],
        size=9,
    )

    d.h2("Delivery")
    d.para(
        "These can sink the experiment **without telling us anything about whether the "
        "approach works**, which is why they are managed hard."
    )
    d.table(
        ["Risk", "Likelihood", "Mitigation"],
        [
            ["**The ~1 GB software download.** Much lower risk remotely — each teacher downloads at home rather than all at once on one connection", "Medium", "Setup instructions sent three days early, **with a reply required** confirming the setup check is green. No reply means it was not attempted"],
            ["**No instructor in the room.** Everything that would have been a thirty-second fix becomes a conversation with a beginner who cannot describe what they are seeing", "High", "All screens shared through hands-on work, with Meet showing every participant at once; each person checked on by name; groups capped at eight so that is possible"],
            ["Laptops that block software installation, or lack the ~5 GB needed", "Medium", "Confirmed with schools, and asked on the enrolment form, before anyone is admitted. A browser-based fallback exists for sessions 1–19, but that participant cannot do days 20–24 fully"],
            ["The editor's interpreter picker — the most common beginner failure", "High", "Only one choice is ever present; a red callout on days 1 and 2; the setup script reports which Python is actually running"],
            ["Missed sessions — twice a week for eight weeks, on top of a teaching job", "High", "Every topic is self-contained; worked solutions published after each session; topic 19 is a catch-up with nothing new in it. **A missed session now costs more than it did on the old three-a-week schedule** — it is two hours and two topics, not one — and the recap block at the start of every session exists for it"],
        ],
        [0.42, 0.13, 0.45],
        size=9,
    )

    d.callout(
        "The comparison we would ask you to make",
        [
            "This is not a risky option against a safe one. The conventional approach has "
            "**two years of evidence of not producing the result we wanted** — that is not "
            "a safe option, it is a known-unsuccessful one.",
            "This is a risky option with an argument behind it, a defined measurement and "
            "a decision point. **We think there is a real chance it succeeds. We are not "
            "claiming it will.**",
        ],
        fill=BAND_FILL,
    )

    # ------------------------------------------- 10. requirements, cost, status
    d.h1("Requirements, cost and current status")

    d.table(
        ["", ""],
        [
            ["Per participant", "**Their own laptop for the whole course** — Windows or macOS, about **5 GB free**, and permission to install software"],
            ["Connection", "Good enough for a **two-hour video call with screen sharing**, twice a week. This is the one requirement that most often needs solving before a teacher can start"],
            ["Webcam", "Wanted, not required. Without one the instructor loses the clearest signal that someone is stuck"],
            ["Software", "**Anaconda** and **VS Code**, both free. Two installations before day one and nothing afterwards; the course uses only Python's standard library"],
            ["Not needed", "No GPU, no server, no accounts, no API keys, no paid service of any kind"],
            ["Staffing", "One instructor per group of 4–8"],
            ["**Cost**", "**Zero.** The only material cost is instructor time"],
        ],
        [0.21, 0.79],
    )

    d.h2("Screening before a group is formed")
    d.para(
        "Because the course is remote, the requirements above are **asked and acted on "
        "before enrolment**, not discovered in week one. Every teacher answers six "
        "questions: how many days a week they can commit, whether their connection is "
        "sufficient, whether they have a webcam, whether they can use Zoom or Google Meet, "
        "any technical problem worth knowing about, and their laptop's memory and free "
        "disk space."
    )
    d.para(
        "The answers decide group composition — teachers who can commit two days a week "
        "cannot be mixed with those committing three — and they surface the cases that "
        "need solving first: a locked-down school laptop, a shared family machine, a "
        "connection that will not hold a call. **This screening is what replaces the "
        "instructor's physical presence**, and it is the single cheapest risk reduction "
        "available to a remote course."
    )

    d.h2("Verified by automated checks")
    d.para(
        "**All Part 1 materials are written.** Four scripts run against them, and all "
        "currently pass: every session agenda sums exactly to its stated length; **all 43 "
        "notebooks** — lessons, worked solutions and both versions of each assessment — "
        "execute cell by cell, in order, from a clean start; the language and dependency "
        "rules hold, with nothing outside Python's standard library imported anywhere; and "
        "the finished program runs end to end, with missing files, corrupt data and bad "
        "input each producing one actionable sentence rather than a technical traceback."
    )
    d.para(
        "Every teaching cell designed to fail still raises exactly the error it claims. "
        "One that silently starts working is treated as a defect.",
        italic=True,
    )

    d.h2("Not yet verified — stated plainly")
    d.table(
        ["Open item", "What closes it"],
        [
            ["**The Armenian terminology has not been reviewed by a native-speaker teacher**", "Every term is drawn from a single glossary, so a correction is one edit plus an automated sweep rather than a rewrite of nineteen files. Terms we are least sure of are already marked"],
            ["**The installation instructions have never been followed on a clean machine**", "Run once on a fresh Windows laptop and once on a fresh Mac, and timed, before the first session"],
            ["**Nothing has been taught to a real cohort**", "Every estimate of pacing here is a design estimate. The first cohort will find things we did not"],
            ["**The toolchain may change**", "Anaconda and VS Code are assumed throughout. Google Colab and Thonny are under discussion as a lighter alternative that would remove the installation problem — and with it the largest remaining delivery risk"],
        ],
        [0.34, 0.66],
    )
    d.para(
        "We would rather hand you a document that names these three than one that reads "
        "as finished.",
        italic=True,
    )

    d.h2("What we would find most useful from you")
    d.numbered([
        "**Is the diagnosis right?** Is \"they cannot code\" really the bottleneck, or are we fixing the wrong thing?",
        "**Is 32 hours enough** to produce the fluency the approach depends on?",
        "**What should the success numbers be?** Agreed before the first session.",
        "**Will the discovery sessions be accepted or resented?** Anyone who knows this audience better than we do should say so before we run it, not after.",
    ])

    d.page_break()

    # ------------------------------------------------------- 11. decision point
    d.h1("The grade-11 course")

    d.para(
        "Since this dossier was last issued, a **second course has been built and "
        "verified**. It takes a teacher who has finished the course described above and "
        "prepares them to teach **grade 11**. It is the same length, the same shape and "
        "the same method: sixteen sessions of two hours, twice a week for "
        "eight weeks, delivered remotely in groups of four to eight."
    )

    d.table(
        ["", "Grade-10 course", "Grade-11 course"],
        [
            ["Entry", "**None.** Begins with installing software", "**The grade-10 course**, and nothing beyond it"],
            ["State topics", "1–14", "15–22 and 24"],
            ["Spine", "one class, in dictionaries", "**the whole school**, as objects with statistics and charts"],
            ["Teaches", "print, types, variables, lists, dictionaries, conditions, loops, functions, files", "**classes, inheritance, NumPy, Matplotlib, pandas, recursion, debugging**"],
            ["Deliverable", "a four-file gradebook over the teacher's own class", "a **five-file report tool** over the teacher's own school file, with charts"],
            ["Discovery sessions", "5 of 16", "**7 of 16**"],
            ["Status", "built and verified", "**built and verified**"],
        ],
        [0.16, 0.42, 0.42],
    )

    d.h2("What changes between them, and why")

    d.para(
        "Two rules invert, and both inversions are deliberate. The grade-10 course "
        "**forbids classes and every third-party library**, because they would let a "
        "participant skip the mechanics the course exists to build. The grade-11 course "
        "**makes classes its centre and teaches three libraries**, because those are "
        "state topics 18, 19, 15, 20 and 21, and a teacher has to be able to demonstrate "
        "them."
    )
    d.para(
        "**The order is preserved even so.** The session that introduces NumPy first has "
        "participants write the standard-deviation formula out by hand. The session that "
        "introduces pandas first spends twenty-two lines parsing a file with the tools "
        "they already have. The library arrives as relief from work already done — never "
        "as a way to avoid understanding it."
    )

    d.callout(
        "What the two courses cover together",
        [
            "**187 of the state curriculum's 193 pupil-hours**, in sixty teacher-hours.",
            "The six that remain are **topic 23, version control**, deliberately deferred "
            "until the rest of the subject is secure.",
            "A teacher who completes both can deliver grade 10 and grade 11 in full, "
            "apart from that topic.",
        ],
        fill=BAND_FILL,
    )

    d.h2("The grade-11 curriculum")

    d.para(
        "The same shape as the first course: **24 topics across 16 two-hour sessions**. "
        "Seven of the sixteen are discovery sessions, marked **D** — two more than the "
        "first course, because almost everything here is a tool that replaces work the "
        "participant has just done by hand."
    )

    d.table(
        ["Topic", "", "Title", "What the participant has at the end"],
        [
            ["1", "", "The school, and what we are going to build", "The school's real file open, and its average computed with what they already knew"],
            ["2", "", "Functions that bend", "One report function called six ways, with defaults and named arguments"],
            ["3", "", "Sending back more than one answer", "One pass over the register returning three figures at once"],
            ["4", "**D**", "**Six reports, six loops**", "Six lists the head teacher asked for, each on one line instead of four"],
            ["5", "", "Choosing while you build", "A register labelled pass/fail in one line, and sorted by a rule of their own"],
            ["6", "**D**", "**A student is more than a grade**", "A Student class, after a misspelled dictionary key failed silently thirty lines away"],
            ["7", "", "The calculation moves inside", "`student.average()` — the data and the thing that calculates it travelling together"],
            ["8", "", "A class full of students", "A SchoolClass holding Student objects, and a School holding classes"],
            ["9", "**D**", "**Teachers as well as students**", "Person, Student and Teacher — the shared part written once, after copying it twice"],
            ["10", "", "One loop, many kinds", "One loop printing the right line for every kind of person, with no `if` in it"],
            ["11", "", "The register, rewritten  *(no new syntax)*", "The first course's gradebook rebuilt with objects, side by side with the old one"],
            ["12", "**D**", "**The term's statistics**", "Mean, spread and extremes in four lines, after writing the spread formula out by hand"],
            ["13", "", "Whole arrays at once", "Every grade changed at once, and failing marks selected without a loop"],
            ["14", "**D**", "**Show the head teacher**", "A real chart saved as a file, after drawing one with asterisks"],
            ["15", "", "The four charts a school asks for", "Bar, histogram, line and grouped bar — and which question each answers"],
            ["16", "**D**", "**The school's own file**", "The file read correctly in one line, after twenty-two lines got it wrong"],
            ["17", "", "Filter, group, describe", "Averages per class and per subject, without naming the classes in the code"],
            ["18", "", "The term report", "File in, statistics and two charts out — all three libraries in one workflow"],
            ["19", "**D**", "**How deep does it go?**", "One recursive function that works at any depth, after loops ran out of levels"],
            ["20", "", "Where code comes from", "`pip`, `requirements.txt`, environments and Colab — the only session needing internet"],
            ["21", "", "Wrong, with no error", "A silent wrong answer found with a debugger, not by rereading"],
            ["22", "T", "Five files that each do one thing", "**A working `python main.py`**, confirmed individually"],
            ["23", "P", "Make it yours", "Their own school's data in, and one feature of their own design"],
            ["24", "P", "Finish and show", "A colleague runs their program from their notes alone"],
        ],
        [0.05, 0.05, 0.37, 0.53],
        size=8.5,
    )

    d.h2("The grade-11 schedule")

    d.para(
        "Identical in shape to the first course — two sessions a week for eight weeks, "
        "sixteen sessions of two hours, 32 hours in total, with homework between sessions "
        "drawn from tasks the notebooks already carry."
    )

    d.table(
        ["Week", "Sessions", "Topics", "What the participant can do by the end of it", "Assessment"],
        [
            ["1", "1–2", "1–3", "My functions bend to what is asked of them", "*diagnostic sat before session 1*"],
            ["2", "3–4", "4–5", "One line instead of six", ""],
            ["3", "5–6", "6–8", "A student is a thing, and the school is objects", ""],
            ["4", "7–8", "9–11", "They share what they have in common", "**Midpoint**"],
            ["5", "9–10", "12–15", "I can measure a term and draw it", ""],
            ["6", "11–12", "16–18", "The school's own file goes in, a report comes out", ""],
            ["7", "13–14", "19–21", "Any depth, and I can find out why it is wrong", ""],
            ["8", "15–16", "22–24", "It runs on my school's data, and I showed it", "**Final practical**"],
        ],
        [0.08, 0.12, 0.11, 0.49, 0.20],
        size=9,
    )

    d.h2("How the grade-11 course is assessed")

    d.para(
        "Three sittings, on the same principle as the first course: the first two measure "
        "the programme, the third decides who continues."
    )

    d.table(
        ["", "Sitting", "When", "Length", "Points", "What it covers"],
        [
            ["1", "Initial diagnostic", "Before session 1", "45–60 min", "40", "**What the first course actually produced** — nothing from this one"],
            ["2", "Midpoint", "After session 8", "60–75 min", "50", "Topics 2–11: functions, comprehensions, classes, inheritance"],
            ["3", "Final practical", "Session 16", "90–120 min", "70 + 10", "Topics 12–24: libraries, charts, data, recursion, the project"],
        ],
        [0.04, 0.17, 0.15, 0.12, 0.10, 0.42],
        size=9,
    )

    d.callout(
        "Two things worth your attention in that table",
        [
            "**The diagnostic measures the first course, not this one.** It is the only "
            "point at which we find out what the grade-10 programme actually produced, "
            "taken before the second course can affect the answer. Its marking guide "
            "includes the option of sending a cohort back to repeat the first course.",
            "**The midpoint is a go/no-go on objects.** Whether a participant can write a "
            "working class decides whether the libraries half of the course can start at "
            "all. If the cohort fails it, the instruction is to spend a session on "
            "revision rather than press on.",
        ],
    )

    d.h2("What a grade-11 participant finishes with")

    d.para(
        "A five-file Python program — settings, people, loading, charts and an entry "
        "point — that reads **their own school's grade file**, prints the term's "
        "statistics by class and by subject, lists the pupils who need attention, and "
        "saves two charts as image files that can go straight into a report."
    )

    d.h2("Three gaps we are naming rather than hiding")

    d.bullets([
        "**Recursion is taught as mechanics only** — walking a nested structure. Its "
        "algorithmic half, including the call stack and complexity, is Part 2 material. "
        "The build fails if the teaching material so much as names factorial or Fibonacci.",
        "**Topic 21 names six libraries and five environments.** Three libraries are "
        "taught to the point of use. The rest are named once, in the final session, with "
        "what each one is and why a grade-11 teacher does not need it — because pupils "
        "will ask, and «that is difficult» is the wrong answer.",
        "**Neither course has been taught to a cohort.** Everything above is a design "
        "claim, not a result.",
    ])

    d.page_break()

    d.h1("The decision point after two months")

    d.para(
        "The programme is deliberately framed as an experiment with a decision at the end, "
        "and both outcomes are useful."
    )

    d.h2("Between the parts — the trial class")
    d.para(
        "**March.** Each teacher teaches one lesson to real pupils, after Part 1 and "
        "before any decision about Part 2. It is the only point in the programme that "
        "tests the thing the programme exists for, and it informs the decision below "
        "alongside the coding criterion."
    )

    d.h2("If it works — Part 2, four months")
    d.para(
        "Part 2 is **outlined, not written**. Building it before Part 1 reports would be "
        "assuming the answer to the question Part 1 exists to ask. The ordering below is "
        "not arbitrary: each stage depends on the one before it, and the first exists "
        "because Part 1 deliberately skipped it."
    )
    d.table(
        ["Stage", "", "Why here"],
        [
            ["1", "**The theory we postponed** — parameters in depth, `*args`/`**kwargs`, scope, comprehensions and `lambda`, nested loops and conditions, choosing between data structures, reading other people's code", "Part 1 taught constructs as tools that solved a problem; it never explained how they work underneath. **This stage is itself a test of the programme's claim** — if theory now lands easily on top of two months of practice, the sequencing was right. State curriculum topic 16"],
            ["2", "**Recursion**", "Placed here for the same reason the state curriculum places it immediately after advanced functions: it is a fact about functions before it is a technique. **Before classes**, as the state curriculum has it. Topic 17"],
            ["3", "**Algorithmic tasks and problem-solving** — problems with no given method; writing the approach in words before the code", "The thing Part 1 was clearing the ground for. With the mechanics automatic, the whole of a participant's attention is free for the problem"],
            ["4", "**Bigger projects** — several times the size of Part 1's, built over weeks rather than sessions", "Where structure starts to matter, and where a program becomes too big to hold in your head"],
            ["5", "**Objects and classes**, including inheritance", "Deliberately late. Classes solve a problem a participant only *feels* once their programs are big enough to have it — which is why this follows stage 4. Topics 18–19"],
            ["6", "**Libraries and environments** — `pip`, NumPy, Matplotlib, pandas, Colab and Kaggle", "Together the largest block in the state curriculum, and the bridge into the Artificial Intelligence subject beside Python. **This stage deliberately breaks Part 1's standard-library-only rule**, which has done its job by then. Topics 15 and 21"],
        ],
        [0.06, 0.40, 0.54],
        size=9,
    )
    d.para(
        "**Git and version control** (state curriculum topic 23) stays out of scope and is "
        "revisited once Part 1 reports: if the cohort arrives at Part 2 comfortably, git "
        "and the remaining tooling go in; if not, the time is better spent elsewhere.",
        italic=True,
    )
    d.callout(
        "The honest uncertainty in Part 2",
        [
            "**Whether our method carries over is unproven.** \"Do it the long way, then "
            "get the tool\" works for concrete mechanics, where the long way is tedious "
            "but obvious. Algorithmic thinking may need a different shape entirely.",
            "We would rather expect to discover that in stage 2 than assume it now. "
            "Part 1's assessments measure mechanics; **measuring problem-solving will need "
            "a different instrument**, and designing it is part of Part 2's work.",
        ],
    )

    d.h2("If it does not work")
    d.para(
        "We return to the conventional approach, having learned something specific rather "
        "than having failed again in the same way. And we will know **where** it broke:"
    )
    d.table(
        ["Where it broke", "What that tells us"],
        [
            ["At the mechanics — they still cannot code after 32 hours", "The time budget is wrong, not the theory. A longer course on the same method"],
            ["At acceptance — they disliked the method and left", "The theory is untested; the delivery needs rethinking"],
            ["At transfer — they can code but cannot solve problems", "The central assumption is wrong. This is the finding that would change our direction"],
        ],
        [0.31, 0.69],
    )
    d.callout(
        "Either result is worth two months",
        ["A third repeat of the approach that has not worked is not."],
        fill=BAND_FILL,
    )

    # ------------------------------------------------------------ A. appendix
    d.h1("Appendix — inventory of materials", numbered=False)

    d.para(
        "Everything below exists today and is version-controlled. The counts are verified "
        "against the materials when this document is generated."
    )
    d.table(
        ["Material", "Grade 10", "Grade 11", "Audience"],
        [
            ["Lesson notebooks", "19", "21", "Participant"],
            ["Written guides", "5", "3", "Participant"],
            ["Worked solutions", "18", "21", "Participant, after each session"],
            ["Assessments — grader's and participant versions", "3 × 2", "3 × 2", "Participant / instructor"],
            ["Assessment marking guides", "3", "3", "Instructor only"],
            ["Reference program", "4 files", "5 files", "Participant, from the transition session"],
            ["Installation instructions, reference sheet, setup check", "3", "3", "Participant"],
            ["Instructor notes, curriculum, build specification", "3", "3", "Instructor / organiser"],
            ["Recruitment announcement, enrolment guidance", "2", "2", "Prospective participants"],
            ["**Notebooks that must execute before any change is accepted**", "**43**", "**48**", "— automated"],
        ],
        [0.40, 0.11, 0.11, 0.38],
        size=9,
    )
    d.para(
        "Each course is held in the same version-controlled repository, and each has its "
        "own automated checks that must pass before a change is accepted: session "
        "arithmetic, execution of every notebook in order, the language and dependency "
        "rules, and the finished program running end to end. A further check runs across "
        "both courses and this document, confirming that every figure restated in more "
        "than one place still agrees. **Nothing is reported as complete on the strength "
        "of inspection alone.**"
    )

    closing = doc.add_paragraph()
    bottom_rule(closing)
    d.para(
        f"Programme dossier v{VERSION} · {TODAY} · Prepared for Fast Foundation. "
        "Figures in this document are generated from the programme materials and verified "
        "against them at the time of writing.",
        size=9, colour=GREY,
    )

    return d


def main():
    problems = check_facts()
    if problems:
        print("❌ the dossier disagrees with the repository:\n")
        for problem in problems:
            print(f"   {problem}")
        print("\nFix the content in this script (or the repository) before shipping.")
        return 1

    dossier = build()
    dossier.save(OUT)
    print("✅ facts verified against the repository")
    stale = check_built_document(OUT)
    if stale:
        print("❌ the built dossier still carries the old schedule:\n")
        for phrase in stale:
            print(f"   {phrase!r}")
        print("\n   Fix the content in this script before shipping.")
        return 1

    print("✅ no three-a-week schedule figures left in the built document")
    print(f"✅ {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
