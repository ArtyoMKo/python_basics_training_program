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

    curriculum = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
    index_rows = re.findall(r"^\|\s*(\d+)\s*\|[^|]+\|[^|]+\|[^|]+\|\s*(\d+)\s*\|\s*$",
                            curriculum, re.M)
    days = [int(n) for n, _ in index_rows]
    minutes = [int(m) for _, m in index_rows]

    if days != list(range(1, 25)):
        problems.append(f"CURRICULUM.md lists days {days[:3]}…, not 1..24")
    if sum(minutes) != 1200:
        problems.append(f"total is {sum(minutes)} minutes, not 1200")

    counts = {
        "notebooks": len(list((ROOT / "notebooks").glob("*.ipynb"))),
        "solutions": len(list((ROOT / "solutions").glob("*.ipynb"))),
        "tests": len(list((ROOT / "tests").glob("*.ipynb"))),
        "guides": len(list((ROOT / "guides").glob("*.md"))),
        "marking guides": len(list((ROOT / "tests").glob("mark*_guide.md"))),
        "project files": len(list((ROOT / "project" / "gradebook").glob("*.py"))),
    }
    expected = {"notebooks": 19, "solutions": 18, "tests": 4, "guides": 5,
                "marking guides": 4, "project files": 4}
    for name, want in expected.items():
        if counts[name] != want:
            problems.append(f"{name}: found {counts[name]}, dossier says {want}")

    # The sample class is quoted in the dossier and in the course prose.
    sample = (ROOT / "notebooks" / "sample_class.csv").read_text(encoding="utf-8")
    grades = [int(line.split(",")[1]) for line in sample.strip().splitlines()[1:]]
    if len(grades) != 12 or sum(grades) != 78 or sum(grades) / len(grades) != 6.5:
        problems.append(f"sample class: {len(grades)} students, sum {sum(grades)}, "
                        f"average {sum(grades) / len(grades)}")

    # Discovery days must still be the five the dossier names.
    for day in ("day06_class_register", "day10_for_loops", "day14_dictionaries",
                "day17_functions"):
        if not (ROOT / "notebooks" / f"{day}.ipynb").exists():
            problems.append(f"missing discovery notebook {day}")
    if not (ROOT / "guides" / "day22_your_own_class.md").exists():
        problems.append("missing discovery guide day22_your_own_class.md")

    return problems


# -------------------------------------------------------------------------- content

TODAY = "2 October 2026"
VERSION = "1.0"


def build():
    d = Dossier()
    doc = d.document

    # ---------------------------------------------------------------- cover
    for _ in range(4):
        doc.add_paragraph()

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
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
    run = lead.add_run("Programme dossier")
    run.font.size = Pt(13)
    run.bold = True
    run.font.color.rgb = INK
    lead.paragraph_format.space_after = Pt(2)

    recipient = doc.add_paragraph()
    run = recipient.add_run("Prepared for Fast Foundation")
    run.font.size = Pt(12)
    run.font.color.rgb = GREY

    for _ in range(2):
        doc.add_paragraph()

    meta = doc.add_table(rows=0, cols=2)
    meta.autofit = False
    no_borders(meta)
    for label, value in (
        ("Document", "Programme dossier — schedule, methodology, plan, expected results"),
        ("Version", f"{VERSION} — for partner review"),
        ("Date", TODAY),
        ("Programme length", "24 sessions × 50 minutes = 20 hours, over 8 weeks"),
        ("Audience", "Public-school teachers, any subject, no programming background"),
        ("Status", "Materials complete and verified; not yet taught to a cohort"),
    ):
        cells = meta.add_row().cells
        cells[0].width = Cm(4.0)
        cells[1].width = Cm(12.6)
        cells[0].text = ""
        cells[1].text = ""
        p0 = cells[0].paragraphs[0]
        p0.paragraph_format.space_after = Pt(3)
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.size = Pt(10)
        r0.font.color.rgb = NAVY
        p1 = cells[1].paragraphs[0]
        p1.paragraph_format.space_after = Pt(3)
        rich(p1, value, size=10)

    doc.add_paragraph()
    d.callout(
        "How to read this document",
        [
            "Sections 3–6 answer the four questions you asked: the method, the schedule, "
            "the curriculum and the expected results.",
            "Section 9 sets out how the programme will be judged, including the one "
            "measurement that tests its central assumption.",
            "Section 10 states the risks plainly, including the ways this programme "
            "could fail. We would rather you read them here than discover them later.",
        ],
    )

    d.page_break()

    # ------------------------------------------------------------- contents
    d.h1("Contents", numbered=False)
    contents = [
        ("1", "Executive summary"),
        ("2", "The problem this programme addresses"),
        ("3", "Methodology — how the course teaches"),
        ("4", "Schedule"),
        ("5", "Curriculum — the twenty-four sessions"),
        ("6", "Expected results"),
        ("7", "Scope — what is taught, and what is deliberately excluded"),
        ("8", "Assessment"),
        ("9", "How success will be measured"),
        ("10", "Risks"),
        ("11", "Requirements and cost"),
        ("12", "Current status and what remains"),
        ("13", "The decision point after two months"),
        ("A", "Appendix — inventory of materials"),
    ]
    for number, label in contents:
        paragraph = doc.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(3)
        paragraph.paragraph_format.left_indent = Cm(0.4)
        run = paragraph.add_run(f"{number}.")
        run.bold = True
        run.font.color.rgb = NAVY
        run.font.size = Pt(10.5)
        paragraph.add_run(" " + label).font.size = Pt(10.5)

    d.page_break()

    # ------------------------------------------------------ 1. executive summary
    d.h1("Executive summary")

    d.para(
        "This is a 20-hour introductory programming course for public-school teachers "
        "who have never written a line of code. It runs as **24 sessions of 50 minutes, "
        "three times a week, over eight weeks**. Every participant finishes with a small "
        "program they wrote themselves and can actually use: a gradebook that opens their "
        "own class list, shows who has passed, calculates the class average, and saves "
        "changes back to a file."
    )
    d.para(
        "The programme is deliberately unusual, and the reason is stated in section 2. "
        "Two years of conventional teaching has not produced teachers who can write a "
        "program. Our diagnosis is that the bottleneck is not missing theory but missing "
        "**coding fluency** — and that teaching through algorithmic problems asks "
        "beginners to work out *what* a program should do and *how* to write it at the "
        "same time, so they fail at both. This course separates the two loads: it teaches "
        "the mechanics to fluency first, with almost no theory and no algorithmic "
        "difficulty at all, and leaves problem-solving to a later course."
    )
    d.para(
        "**We are presenting this as a two-month experiment with a decision at the end, "
        "not as a finished methodology.** Section 9 sets out what we will measure and "
        "section 13 what we will do with either result."
    )

    d.h2("Key facts")
    d.table(
        ["", ""],
        [
            ["Participants", "Public-school teachers, any subject. **No prior programming assumed** — the course begins with installing software."],
            ["Group size", "Up to 16, one instructor."],
            ["Format", "24 sessions × 50 minutes = **20 hours exactly**, three sessions per week over eight weeks."],
            ["Language", "All explanations, exercises and guides in **Armenian**. All code — keywords, variable names, comments and output — in **English**, so that what participants write matches Python everywhere else in the world."],
            ["Software", "Anaconda and VS Code. Two installations on day one and nothing afterwards; the course uses only Python's standard library."],
            ["Cost", "**Zero.** All software is free and nothing in the course touches a paid service or needs an internet connection after day one."],
            ["Final deliverable", "A runnable four-file Python program over the participant's own class data, demonstrated to a colleague."],
            ["Assessment", "Four take-home tests, one per fortnight, with instructor marking guides."],
            ["Current status", "All materials written and verified by automated checks. **Not yet taught to a cohort.**"],
        ],
        [0.22, 0.78],
        zebra=True,
    )

    d.page_break()

    # ------------------------------------------------------------- 2. the problem
    d.h1("The problem this programme addresses")

    d.para(
        "We have been teaching these teachers for **two years without the results we "
        "wanted**. This programme changes the method, not the effort. Setting out why is "
        "the most important part of this document, because everything else follows from it."
    )

    d.h2("Our diagnosis")
    d.para(
        "**The fundamental problem is that the teachers cannot code.** Not that they do "
        "not understand recursion, and not that they have not practised enough algorithms. "
        "They cannot comfortably produce working code at all — the typing, the syntax, the "
        "loop that runs, the error message that gets read and fixed."
    )
    d.para("When a course then teaches through algorithmic tasks, two things must happen at once:")
    d.numbered([
        "Work out **what** the program should do — the logic, the approach.",
        "Work out **how** to write it — the syntax, the structure, the mechanics.",
    ])
    d.para(
        "**They are overloaded, they confuse the two, and they fail at both.** A teacher "
        "stuck on an algorithm cannot tell whether they are stuck on the idea or on a "
        "missing colon. The theory never connects to the practice, because there is no "
        "practice for it to connect to."
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
    d.para("Concretely, for two months:")
    d.bullets([
        "**Almost no theory.** Around 12 minutes of explanation per session, then roughly 30 minutes of typing.",
        "**No algorithmic difficulty whatsoever.** Nothing in the course requires working anything out — not a single clever solution, not one problem that needs an insight.",
        "**A great deal of very simple code**, all of it about the participant's own classroom: students, grades, attendance, averages, report lines.",
        "**Concepts arrive as relief, never as definitions** — the mechanism is set out in section 3.",
    ])
    d.para("The intended sequence is:")
    d.table(
        ["Stage", "What happens"],
        [
            ["1", "Write code mechanically, with no hard thinking required"],
            ["2", "Concepts such as lists, loops and functions become obvious, because each one removes a specific difficulty the participant has just met"],
            ["3", "The participant can now code without thinking about coding"],
            ["4", "**Algorithmic problems become learnable**, because their whole attention is free for them"],
        ],
        [0.1, 0.9],
    )
    d.para(
        "**Stage 4 is not part of this course.** It is the next one, if this works.",
        italic=True,
    )

    d.page_break()

    # ------------------------------------------------------------ 3. methodology
    d.h1("Methodology — how the course teaches")

    d.para(
        "Teachers are given a real classroom task, solve it with what they already know, "
        "and then — **in the same session** — meet the tool that collapses it. We call "
        "these **discovery days**, and there are five of them."
    )

    d.h2("The five discovery days")
    d.table(
        ["Day", "The real task", "The long way they do it first", "The tool, same session"],
        [
            ["6", "A register for the whole class", "One variable per student", "**Lists**"],
            ["10", "Mark the whole class pass or fail", "One `if` block per student", "**`for` loops**"],
            ["14", "Find one student's grade by name", "Two parallel lists and a position counter", "**Dictionaries**"],
            ["17", "An average on every report card", "The same six lines written four times", "**Functions**"],
            ["22", "Keep the register after closing the program", "Retyping it every time", "**Files**"],
        ],
        [0.07, 0.29, 0.34, 0.30],
    )

    d.h3("A worked example — day 6")
    d.para(
        "Participants are told: *a teacher needs somewhere to keep the whole class — "
        "every name, every score — so the program can work with all of them.* That is a "
        "real task and it is given as one. With what they know on day 6, it means one "
        "variable per student. The notebook ships twenty already written; they add a few "
        "of their own and update the scores. It works, and it takes a while."
    )
    d.para(
        "**Thirty minutes later, in the same session**, the list arrives and the whole "
        "register becomes two lines. The notebook puts the two versions side by side and "
        "counts them: 40 lines against 2."
    )
    d.para(
        "Nobody has to explain why lists are useful. The participants spent twenty minutes "
        "finding out — and got the answer before they went home."
    )

    d.h2("Three rules that make it work")
    d.para(
        "These are the rules most easily broken by accident, so they are written into the "
        "course specification and enforced during material review."
    )

    d.h3("1. The relief comes in the same session. Always.")
    d.para(
        "An earlier draft of this course planted a difficulty on day 6 and resolved it on "
        "day 10. That is good structure on paper and bad teaching in practice: adults who "
        "spend an evening on tedious work and go home with no resolution do not come back. "
        "The long way and its replacement are now always **fifty minutes apart, never four "
        "sessions**. Splitting a discovery day across two sessions is forbidden; if a "
        "session runs long, the optional extension tasks are cut, never the second half."
    )

    d.h3("2. The task is real, and the tedium is never named.")
    d.para(
        "A participant is **never** told they are doing something in order to struggle, or "
        "that the long way was there to make a point. They are building a class register "
        "because a teacher needs a class register — which is true."
    )
    d.table(
        ["Never written in the materials", "Written instead"],
        [
            ['"Today is a difficult day on purpose."', '"Today we build a register for the whole class."'],
            ['"Write 30 variables so you feel how bad it is."', '"We need somewhere to keep each student\'s name and score."'],
            ['"Notice how slow that was."', "*(a table comparing line counts, and nothing else)*"],
        ],
        [0.5, 0.5],
    )
    d.para(
        "The distinction matters more than it sounds. Work you chose to do, and were then "
        "shown a better way to do, is a lesson. The identical work, revealed afterwards to "
        "have been a deliberate ordeal, is a trick — and this audience has been let down "
        "enough already."
    )

    d.h3("3. The shortcut is promised in advance, in writing.")
    d.para(
        "Before any stretch of repetitive work, the notebook says plainly that a shorter "
        "way is coming and when. A participant who knows a shortcut is twenty minutes away "
        "types the long version willingly; one who does not starts wondering whether the "
        "course knows what it is doing."
    )

    d.h2("Other design decisions")
    d.table(
        ["Decision", "Reason"],
        [
            ["**Every example is a classroom**", "Students, grades, attendance, averages, report lines. No abstract placeholders, no shopping baskets, no puzzles. A participant should see their Tuesday morning in any line of the course."],
            ["**Armenian explains, English codes**", "A teacher who names a variable in Armenian writes valid Python and can then read no other Python, search for no answer online, and copy no example ever again. Example names are transliterated (`Ani`, `Davit`) so the data stays familiar while the code stays portable."],
            ["**Standard library only**", "No package installation after day one. A library such as `pandas` would make day 11 a single line and teach a teacher nothing about loops."],
            ["**One deliberate error per session**", "Each notebook contains one cell that is *meant* to fail, with the error read together afterwards. Beginners lose more time to fear of red text than to any concept in the course."],
            ["**Every participant's output differs**", "From day 5 the exercises use the participant's own subject, class and pass mark; on day 23 they design a feature of their own. Sixteen identical programs would be a failed course."],
        ],
        [0.26, 0.74],
    )

    d.page_break()

    # --------------------------------------------------------------- 4. schedule
    d.h1("Schedule")

    d.para(
        "**24 sessions × 50 minutes = 1,200 minutes = 20 hours exactly.** Three sessions "
        "per week over eight weeks. Every session's agenda is planned to the minute and "
        "the arithmetic is verified by script, not by eye."
    )

    d.h2("The eight weeks")
    d.table(
        ["Week", "Sessions", "What the participant can do by the end of it", "Ends with"],
        [
            ["1", "1–3", "It runs on my laptop, and I know what a value is", ""],
            ["2", "4–6", "I can name things, and keep a whole class in one list", "**Test 1**"],
            ["3", "7–9", "The computer can make decisions", ""],
            ["4", "10–12", "One loop marks thirty students", "**Test 2**"],
            ["5", "13–15", "I can find any student by name", ""],
            ["6", "16–18", "I write a calculation once and use it everywhere", "**Test 3**"],
            ["7", "19–21", "It is a program now, not a notebook", ""],
            ["8", "22–24", "It has my class in it, it saves, and I showed it to someone", "**Test 4**"],
        ],
        [0.09, 0.13, 0.58, 0.20],
    )
    d.para(
        "**Week 4 is the centre of the course.** It is where the first two discovery days "
        "pay off and where participants first see a loop do thirty students' work. If the "
        "calendar slips, that week is protected.",
        italic=True,
    )

    d.h2("The shape of a session")
    d.para(
        "Two agenda shapes are used. Teaching never exceeds **12 minutes in one block**, "
        "and hands-on work is never less than 26 of the 50 minutes."
    )

    d.h3("Standard session — 14 of the 24")
    d.table(
        ["#", "Activity", "Minutes"],
        [
            ["1", "Recap, and the question left at the end of last session", "5"],
            ["2", "**Teach:** the new idea — ends with something running", "12"],
            ["3", "**Run together:** the notebook's example cells, one at a time", "15"],
            ["4", "**Do it yourself:** the exercises", "15"],
            ["5", "Retrospective: where we got to, what comes next", "3"],
            ["", "**Total**", "**50**"],
        ],
        [0.07, 0.78, 0.15],
    )

    d.h3("Discovery session — days 6, 10, 14, 17 and 22")
    d.table(
        ["#", "Activity", "Minutes"],
        [
            ["1", "Recap", "5"],
            ["2", "**Teach:** today's task, and the only way we can do it so far", "7"],
            ["3", "**Do it the long way:** the real task, with most of it supplied", "13"],
            ["4", "**Teach:** the tool that shortens it", "9"],
            ["5", "**Do the same task again** with the tool, and compare the two", "13"],
            ["6", "Retrospective", "3"],
            ["", "**Total**", "**50**"],
        ],
        [0.07, 0.78, 0.15],
    )
    d.para(
        "Teaching totals 16 minutes on a discovery day, but **split into blocks of 7 and "
        "9** — neither approaches the ceiling, and the second lands on a participant who "
        "now wants it.",
        italic=True,
    )

    d.h2("Between sessions")
    d.para(
        "Sessions are two days apart and the participants are working teachers, so nothing "
        "is required between them. Each notebook ends with an **optional ten-minute "
        "practice task**, and the next session never assumes it was done. The four "
        "assessments (section 8) are take-home and do not consume session time."
    )

    d.page_break()

    # ------------------------------------------------------------- 5. curriculum
    d.h1("Curriculum — the twenty-four sessions")

    d.para(
        "Topics are taught in the order a beginner can absorb them: printing, then types, "
        "then variables, then conditions, then loops, then functions. Collections — lists "
        "and dictionaries — are placed where they solve a problem the participant has just "
        "met rather than where a textbook would put them. **D** marks a discovery day."
    )

    d.table(
        ["Day", "Session", "", "New idea", "What the participant has at the end"],
        [
            ["1", "Install everything and run your first line", "", "Anaconda, VS Code, a notebook cell", "Six green setup checks and a line printed by their own notebook"],
            ["2", "Printing properly", "", "`print`, quotes, comments", "A four-line class register header"],
            ["3", "Four kinds of value", "", "Text, whole number, decimal, true/false", "Each type shown, and why `\"2\" + 2` fails"],
            ["4", "Changing type, and asking a question", "", "`int()`, `str()`, `input()`", "A cell that takes a grade and prints it plus one"],
            ["5", "Giving a value a name", "", "Variables, formatted strings", "One student's row printed from named values"],
            ["6", "**A register for the whole class**", "**D**", "Many variables → **lists**", "Their class as one list, written both ways and compared"],
            ["7", "Working with the register", "", "Add, remove, sort, slice", "A sorted class list, one student added and one removed"],
            ["8", "The first decision", "", "`if` / `else`, comparison, indentation", "Pass or fail for a grade, on their own school's pass mark"],
            ["9", "More than two outcomes", "", "`elif`, `and` / `or` / `not`", "A grade sorted into four named bands"],
            ["10", "**Marking the whole class**", "**D**", "Repeated `if` blocks → **`for` loops**", "The whole register marked, in four lines"],
            ["11", "Counting and totalling", "", "`range`, accumulating, averages", "Their own class average, computed"],
            ["12", "Loops that decide", "", "Loop with a condition inside it", "Who failed, how many passed, the highest grade"],
            ["13", "Entering grades one by one", "", "`while`, validating what was typed", "A loop that collects grades until told to stop"],
            ["14", "**Finding one student**", "**D**", "Two parallel lists → **dictionaries**", "Their class as name-to-grade, and a note on what went wrong before"],
            ["15", "Reports from the register", "", "Looping over a dictionary", "A printed register line per student, columns aligned"],
            ["16", "Several grades per student", "", "A value that is itself a list", "A report card per student with three grades each"],
            ["17", "**An average on every card**", "**D**", "Repeated calculation → **functions**", "The calculation written once, called four times"],
            ["18", "Sending an answer back", "", "`return`, default values", "Four working grade functions that return values"],
            ["19", "The register, assembled", "", "*No new syntax — consolidation*", "The complete register program in one notebook"],
            ["20", "Leaving the notebook", "T", "A `.py` file, the terminal", "`python grades.py` running in a terminal"],
            ["21", "Four files that each do one thing", "T", "Modules and imports", "**A working `python main.py`**, confirmed individually"],
            ["22", "**Keeping it after you close it**", "**D**", "Retyping → **files**", "Their own class in a file, loaded and saved back"],
            ["23", "Make it yours", "P", "Designing a small feature", "One feature of their own design, working"],
            ["24", "Finish and show", "P", "Documentation, demonstration", "A colleague runs their program from their notes alone"],
        ],
        [0.05, 0.27, 0.04, 0.25, 0.39],
        size=8.5,
    )
    d.para(
        "**T** = transition to real files · **P** = project phase. Days 1–19 use Jupyter "
        "notebooks; days 20–24 use plain Python files with a written guide open beside "
        "them, because by then the participants are running a terminal.",
        size=9.5, italic=True,
    )
    d.para(
        "Day 19 doubles as the catch-up session: nothing new arrives, so anyone who has "
        "fallen behind has a session to recover in.",
        size=9.5, italic=True,
    )

    d.page_break()

    # -------------------------------------------------------- 6. expected results
    d.h1("Expected results")

    d.h2("What every participant leaves with")
    d.para(
        "A **runnable Python program**, in their own folder, made of four files they "
        "typed themselves:"
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
        "One command — `python main.py` — opens their class, shows the register with who "
        "passed, lists who did not, adds or corrects a grade, and saves the file."
    )
    d.para(
        "The separation is itself a teaching outcome: because `grades.py` does not import "
        "`storage.py`, a participant can test the calculations without having a data file. "
        "When an answer looks wrong, they can ask *which half is wrong* — the calculation "
        "or the display — and halve the search. That habit is the most transferable thing "
        "in the course."
    )

    d.h2("Milestones to expect, session by session")
    d.table(
        ["By the end of", "Every participant has"],
        [
            ["Day 1", "Software installed and working, and a line printed by a machine they set up themselves"],
            ["Day 6", "Their class as a single list, with the two ways of writing it compared"],
            ["Day 10", "The whole register marked in four lines, proved by adding students without touching the loop"],
            ["Day 14", "Their class as a dictionary, and a written note of what went wrong with the earlier approach"],
            ["Day 17", "A calculation written once and used in four places, with a change proved in a single edit"],
            ["Day 19", "The complete register program working in one notebook"],
            ["**Day 21**", "**A working `python main.py` — confirmed individually, per person, before they leave the room.** Everything after this day assumes it"],
            ["Day 22", "Their own class, in a file, loaded and saved back"],
            ["Day 24", "A documented program a colleague ran unaided, and a 90-second demonstration given aloud"],
        ],
        [0.17, 0.83],
    )

    d.h2("Skills and habits")
    d.para("**Programming.** " +
        "`print` · the four value types · `input` · variables and formatted strings · "
        "`if` / `elif` / `else` · lists · `for` and `range` · `while` · dictionaries · "
        "functions and `return` · reading and writing files · modules and running a "
        "program from a terminal.")
    d.para("**Habits that outlast the syntax.** These are what we most want to survive the course:")
    d.bullets([
        "If a number appears more than once, give it a name.",
        "If code appears more than once, give it a name.",
        "When a result is wrong, ask *which half* is wrong before changing anything.",
        "An error message is a sentence telling you what to fix, not a judgement.",
    ])

    d.h2("What this course does not produce")
    d.para(
        "**It does not produce programmers, and it does not produce people who can solve "
        "algorithmic problems.** That is the next course, and only if this one works. "
        "A participant finishing this programme can write simple, working, useful code and "
        "read an error message. Stating this clearly now is what makes the measurement in "
        "section 9 honest."
    )

    d.page_break()

    # ------------------------------------------------------------------ 7. scope
    d.h1("Scope — what is taught, and what is deliberately excluded")

    d.para(
        "The exclusion list matters as much as the syllabus. Each item below would cost "
        "roughly fifteen minutes and buy a teacher nothing in the program they are going "
        "to write."
    )
    d.table(
        ["Excluded", "Why"],
        [
            ["Classes and objects", "Nothing in a four-file gradebook needs them"],
            ["Error handling beyond one safeguard", "Exactly one `try` sits at the outermost edge of the finished program, so an unexpected failure shows a sentence rather than ten lines of red text"],
            ["List comprehensions, `lambda`, generators", "Shorter to write, much harder to read for someone eight weeks into programming"],
            ["Recursion", "No classroom task in this course needs it"],
            ["Package installation, virtual environments", "Removes the most common way a beginner's setup breaks between sessions"],
            ["Regular expressions, type hints, decorators", "Not reachable in 20 hours, and not needed"],
            ["Web frameworks, databases, version control", "Different subjects entirely"],
        ],
        [0.33, 0.67],
    )
    d.para(
        "Before anything is added back, one question has to be answered: **which line of "
        "the finished gradebook needs it?**",
        italic=True,
    )

    d.h2("Differentiation within a session")
    d.para(
        "In a room of sixteen adults, three or four finish the required work early in "
        "**every** session. Every notebook therefore carries three tiers:"
    )
    d.table(
        ["Tier", "How many", "Sized for"],
        [
            ["Required", "3–4", "Everyone, inside the allotted minutes. Nobody should leave with required work unfinished"],
            ["Extra", "3–4", "The participant who finishes required work with eight minutes to spare"],
            ["Challenge", "1–2", "The fastest one or two in the room"],
        ],
        [0.15, 0.13, 0.72],
    )
    d.para(
        "Extra and challenge tasks use only what has already been taught — wider, not "
        "further ahead. Running out of work is how a competent participant concludes a "
        "course is beneath them.",
        italic=True,
    )

    # ------------------------------------------------------------- 8. assessment
    d.h1("Assessment")

    d.para(
        "**Four take-home tests, one per fortnight**, after days 6, 12, 18 and 24. They "
        "are handed out at the end of a session and collected at the start of the next, "
        "so they consume no session time."
    )
    d.table(
        ["Test", "After day", "Covers", "Sessions"],
        [
            ["1", "6", "Printing, value types, `input`, variables, lists", "1–6"],
            ["2", "12", "Conditions, `and` / `or`, loops, `range`, totals, filtering", "7–12"],
            ["3", "18", "`while`, dictionaries, reports, functions", "13–18"],
            ["4", "24", "`return`, real files, modules, the finished program", "19–24"],
        ],
        [0.09, 0.12, 0.62, 0.17],
    )

    d.h2("How they are designed")
    d.bullets([
        "**Not graded, and the participants are told so in writing.** They exist to tell the instructor where to slow down. An honest blank is more useful than a copied answer.",
        "**Every question is a classroom task**, never a puzzle. \"Print a register for these five students\", not \"reverse a string\".",
        "**Nothing untaught**, and nothing from the extra tier — a test measures the floor, not the ceiling.",
        "**A skeleton for every question.** Never a blank cell.",
        "Around 30 minutes of work, six to ten questions.",
    ])

    d.h2("The marking guides")
    d.para(
        "Each test ships with an instructor marking guide, and **the second column is the "
        "point**: not whether the answer was right, but *what a wrong answer tells you*. "
        "Three examples:"
    )
    d.table(
        ["Test", "Question", "What a wrong answer means, and what to do"],
        [
            ["1", "Add one to a grade without writing the answer", "They wrote `grade = 7` instead of `grade = grade + 1`. They have not understood that `=` means *assign*. **If a third of the room misses this, do not start day 7 as written.**"],
            ["2", "Print the whole register", "Still indexing by hand instead of writing a loop. This is the earliest real evidence for or against the whole approach"],
            ["3", "Write a function that returns a value", "Printed instead of returning. **If the room fails this, day 19 is spent on `return` rather than on consolidation** — the four-file program is not reachable without it"],
        ],
        [0.07, 0.25, 0.68],
    )

    d.page_break()

    # ------------------------------------------------------- 9. measuring success
    d.h1("How success will be measured")

    d.para(
        "An experiment nobody can evaluate is just a change of plan. **These checkpoints "
        "should be agreed before the first session**, not argued about afterwards."
    )
    d.para(
        "Most of them need no extra work, because the course already produces artefacts "
        "that are objectively checkable."
    )

    d.table(
        ["When", "The check", "Why it is the right one"],
        [
            ["Test 1", "Do they write `grade = grade + 1` rather than the answer?", "The earliest signal that assignment has landed; everything later depends on it"],
            ["Test 2", "Do they write a loop, or still index by hand?", "The first real evidence for or against the method"],
            ["Test 3", "Do they understand `return`?", "If not, the four-file program is out of reach"],
            ["**Day 21**", "**Does `python main.py` run?** Confirmed individually, per person", "Binary, unarguable, and the hard gate of the course"],
            ["Day 24", "Does a colleague run their program **from their notes alone**?", "Tests that the thing is real, not that it works on one desk"],
            ["Throughout", "Attendance across all 24 sessions", "Below a certain point, nothing else is interpretable"],
        ],
        [0.11, 0.37, 0.52],
    )

    d.h2("The one measurement that tests the theory")
    d.para(
        "**None of the checks above tests the actual bet**, because none of them is an "
        "algorithmic problem. They measure whether the course ran well. So the final test "
        "ends with one question that is different:"
    )
    d.callout(
        "Test 4, final question — the transfer question",
        [
            "*Given a class register, find the student whose grade is closest to the class average.*",
            "",
            "It uses **no syntax the course did not teach**, and **the course never "
            "demonstrates it**. The question asks the participant to write their approach "
            "in plain words first, then attempt the code, and to say where they stopped if "
            "they could not finish.",
        ],
    )
    d.para("Four things are recorded, not one:")
    d.numbered([
        "Did they write the plain-words plan at all?",
        "Was the plan a **correct approach**, even if the code failed?",
        "Did the code work?",
        "**Where did they stop, in their own words?**",
    ])

    d.h3("How to read the result")
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
            "though most of the code will not run.",
            "**We will not report this question as a pass rate**, and we would ask that it "
            "not be read as one.",
        ],
        fill=BAND_FILL,
    )

    d.h2("What we will report to you")
    d.bullets([
        "Per test: correct, wrong and blank counts per question, plus completion rate. Blank answers are recorded separately — a blank means something different from a wrong answer.",
        "The day 21 figure: how many participants left with a working program.",
        "The day 24 figure: how many programs a colleague ran unaided.",
        "Attendance.",
        "The transfer question, in the four columns above, with the participants' own words about where they stopped.",
    ])
    d.para(
        "**Target numbers should be set jointly before the first session.** A target "
        "chosen afterwards is not a target.",
        italic=True,
    )

    d.page_break()

    # ------------------------------------------------------------------ 10. risks
    d.h1("Risks")

    d.para(
        "Stated plainly, because the programme has to be judged fairly in two months and "
        "because we would rather you read these here than discover them later."
    )

    d.h2("The approach itself")
    d.table(
        ["Risk", "Assessment", "What we do about it"],
        [
            ["**The core assumption may simply be wrong.** We are betting that coding fluency transfers — that someone who can code mechanically will find algorithmic problems learnable later. That is plausible and unproven. It is possible to produce teachers who type Python fluently and still cannot solve a problem with it", "Real, and not mitigable within this course", "We measure it directly (section 9) rather than assuming it. If it happens, the programme failed, and no amount of the course being pleasant changes that"],
            ["**Participants may not accept it.** Adults judge a course by how substantial it feels. One that explains little and asks for a lot of typing can read as shallow. The first half of each discovery session is deliberately laborious", "Likely to affect some participants", "Every discovery day resolves inside the same 50 minutes; the shortcut is promised in writing before the long half starts; the work is never framed as an ordeal. A participant who leaves day 6 thinking \"I typed for twenty minutes\" rather than \"I learned what a list is for\" is a genuine failure, and it will happen to somebody"],
            ["**Twenty hours is not much**, in 50-minute pieces, for working teachers", "Certain", "The scope is deliberately narrow and the exclusion list is explicit. Narrow means things are missing, by design"],
        ],
        [0.40, 0.19, 0.41],
        size=9,
    )

    d.h2("Delivery")
    d.table(
        ["Risk", "Likelihood", "Mitigation"],
        [
            ["**The ~1 GB software download on school wifi.** Sixteen people downloading at once will cost a session", "High", "Setup instructions sent three days early so most arrive installed; **a USB stick with offline installers for both platforms is mandatory kit**"],
            ["Laptops that block software installation", "Medium", "Confirmed with schools before enrolment. A browser-based fallback exists for sessions 1–19, but that participant cannot do days 20–24 fully — so it is a last resort"],
            ["Not enough disk space (about 5 GB needed)", "Medium", "Asked on the enrolment form, before anyone is admitted"],
            ["The editor's interpreter picker — the most common beginner failure", "High", "Only one choice is ever present; a red callout on days 1 and 2; the setup script reports which Python is actually running"],
            ["Missed sessions — three a week for eight weeks, on top of a teaching job", "High", "Every session is self-contained; worked solutions are published after each one; day 19 is a catch-up session with nothing new in it"],
            ["Mixed pace within the room", "Certain", "Three tiers of exercise in every notebook; fast finishers paired with slower ones from day 3"],
        ],
        [0.40, 0.13, 0.47],
        size=9,
    )
    d.para(
        "The delivery risks can sink the experiment **without telling us anything about "
        "whether the approach works** — which is exactly why they are managed hard.",
        italic=True,
    )

    d.h2("The comparison we would ask you to make")
    d.callout(
        "This is not a risky option against a safe one",
        [
            "The conventional approach has **two years of evidence of not producing the "
            "result we wanted**. That is not a safe option; it is a known-unsuccessful one.",
            "This is a risky option with an argument behind it, a defined measurement, and "
            "a decision point. **We think there is a real chance it succeeds.** We are not "
            "claiming it will.",
        ],
        fill=BAND_FILL,
    )

    # ------------------------------------------------- 11. requirements and cost
    d.h1("Requirements and cost")

    d.table(
        ["", ""],
        [
            ["Per participant", "A Windows or macOS laptop — their own or the school's — with about **5 GB free** and permission to install software"],
            ["Software", "**Anaconda** and **VS Code**, both free. Two installations on day one and nothing afterwards"],
            ["Network", "Needed on day one only. **Every session after that runs with the wifi switched off**"],
            ["Not needed", "No GPU, no server, no accounts, no API keys, no paid service of any kind"],
            ["Room", "Seats for up to 16 with power, and a projector"],
            ["Staffing", "One instructor per cohort of 16"],
            ["**Software cost**", "**Zero**"],
            ["**Per-participant cost**", "**Zero** — nothing in the course touches a paid service"],
        ],
        [0.24, 0.76],
    )
    d.para(
        "The only material cost is instructor time, the room, and a USB stick holding the "
        "offline installers."
    )

    d.h2("Provided by the programme")
    d.bullets([
        "19 lesson notebooks and 5 written guides, in Armenian",
        "18 worked-solution notebooks, published after each session so a missed day can be recovered",
        "4 take-home assessments with instructor marking guides",
        "Installation instructions covering Windows and macOS separately, step by step",
        "A printable reference sheet with a bilingual glossary",
        "An automated setup check that stops at the first problem and says what to do about it",
        "A fictional sample class, so nobody is blocked on not having data",
        "The finished reference program, for anyone who falls badly behind at the transition",
        "Instructor notes: pre-flight checklist, pacing, what to cut if time runs short",
    ])

    d.page_break()

    # ---------------------------------------------------------------- 12. status
    d.h1("Current status and what remains")

    d.para(
        "**All materials are written.** The programme has not yet been taught to a cohort, "
        "and we do not want that stated any more softly than it is."
    )

    d.h2("Verified by automated checks")
    d.para(
        "The following are checked by scripts that run against the materials, not by "
        "inspection. All currently pass."
    )
    d.table(
        ["Check", "Result"],
        [
            ["Session arithmetic", "Every agenda sums to exactly 50 minutes; 24 sessions total 1,200 minutes"],
            ["Materials execute", "**41 notebooks** — 19 lessons, 18 solution sets and 4 assessments — run cell by cell, in order, from a clean start"],
            ["Deliberate errors behave", "Every teaching cell designed to fail raises exactly the error it claims. One that silently starts working is treated as a defect"],
            ["Language rule", "No Armenian anywhere inside a code cell; explanations Armenian, code English"],
            ["Dependencies", "Nothing outside Python's standard library is imported anywhere"],
            ["The finished program", "`python main.py` runs end to end and reports 12 students, average 6.5, 2 not passing"],
            ["Failure paths", "Missing file, corrupt data, bad input and out-of-range grade each produce one actionable sentence — never a technical traceback"],
        ],
        [0.26, 0.74],
    )

    d.h2("Not yet verified — stated plainly")
    d.table(
        ["Open item", "What it means and what closes it"],
        [
            ["**The Armenian terminology has not been reviewed by a native-speaker teacher**", "The materials are written in Armenian, but the technical vocabulary — the agreed word for *variable*, *list*, *loop* — needs a teacher's eye. Every term is drawn from a single glossary, so a correction is one edit plus an automated sweep rather than a rewrite of nineteen files. Terms we are least sure of are already marked"],
            ["**The installation instructions have never been followed on a clean machine**", "They must be run once on a fresh Windows laptop and once on a fresh Mac, and timed, before the first session. The specific risk is whether the editor's built-in terminal works on Windows without manual configuration"],
            ["**Nothing has been taught to a real cohort**", "Every estimate of pacing in this document is a design estimate. The first cohort will find things we did not"],
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
        "**Is 20 hours enough** to produce the fluency the approach depends on?",
        "**What should the success numbers be?** Agreed before the first session, per section 9.",
        "**Will the discovery sessions be accepted or resented?** Anyone who knows this audience better than we do should say so before we run it, not after.",
    ])

    # ------------------------------------------------------- 13. decision point
    d.h1("The decision point after two months")

    d.para(
        "The programme is deliberately framed as an experiment with a decision at the "
        "end, and both outcomes are useful."
    )

    d.h2("If it works")
    d.para(
        "If participants can code, and the transfer question suggests problem-solving is "
        "now within reach:"
    )
    d.bullets([
        "Continue with the same method into object-oriented programming and more advanced material.",
        "**Go back and add the theory that was deliberately skipped**, now that there is practice for it to attach to. The theory is not cancelled — it is postponed until it can stick.",
        "Begin real algorithmic work, which is where we wanted to be two years ago.",
    ])

    d.h2("If it does not work")
    d.para(
        "We return to the conventional approach, having learned something specific rather "
        "than having failed again in the same way. And we will know **where** it broke:"
    )
    d.table(
        ["Where it broke", "What that tells us"],
        [
            ["At the mechanics — they still cannot code after 20 hours", "The time budget is wrong, not the theory. A longer course on the same method"],
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

    d.page_break()

    # ------------------------------------------------------------ A. appendix
    d.h1("Appendix — inventory of materials", numbered=False)
    d.para(
        "Everything below exists today and is version-controlled. The counts are verified "
        "against the repository when this document is generated."
    )
    d.table(
        ["Material", "Count", "Audience", "Language"],
        [
            ["Lesson notebooks (days 1–19)", "19", "Participant", "Armenian / English code"],
            ["Written guides (days 20–24)", "5", "Participant", "Armenian / English code"],
            ["Worked solutions", "18", "Participant, after each session", "Armenian / English code"],
            ["Take-home assessments", "4", "Participant", "Armenian / English code"],
            ["Assessment marking guides", "4", "Instructor only", "English"],
            ["Reference program", "4 files", "Participant, from day 21", "English"],
            ["Installation instructions", "1", "Participant, before day 1", "Armenian"],
            ["Printable reference sheet and glossary", "1", "Participant", "Armenian / English code"],
            ["Automated setup check", "1", "Participant, day 1", "English output"],
            ["Instructor notes", "1", "Instructor", "English"],
            ["Curriculum with full session agendas", "1", "Instructor / organiser", "English"],
            ["Build specification", "1", "Material authors", "English"],
            ["Recruitment announcement", "1", "Prospective participants", "Armenian"],
        ],
        [0.40, 0.11, 0.30, 0.19],
    )

    d.h2("Quality control")
    d.para(
        "The materials are held in a version-controlled repository with four automated "
        "checks that must pass before any change is accepted: session arithmetic, "
        "execution of all 41 notebooks, the language and dependency rules, and the "
        "finished program running end to end. Nothing is reported as complete on the "
        "strength of inspection alone."
    )

    d.para("")
    closing = doc.add_paragraph()
    bottom_rule(closing)
    d.para(
        f"Programme dossier v{VERSION} · {TODAY} · Prepared for Fast Foundation. "
        "Figures in this document are generated from the programme materials and "
        "verified against them at the time of writing.",
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
    size = OUT.stat().st_size
    print(f"✅ facts verified against the repository")
    print(f"✅ {OUT.relative_to(ROOT)} ({size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
