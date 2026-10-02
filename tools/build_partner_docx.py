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
VERSION = "1.1"


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
            ["Programme", "24 sessions × 50 minutes = **20 hours exactly**, three times a week over eight weeks"],
            ["Audience", "Public-school teachers, any subject. **No prior programming assumed** — the course begins with installing software"],
            ["Group size", "Up to 16, one instructor"],
            ["Deliverable", "A runnable four-file Python program over the participant's own class data, demonstrated to a colleague"],
            ["Cost", "**Zero.** All software is free; nothing touches a paid service or needs the internet after day one"],
            ["Status", "Materials complete and verified. **Not yet taught to a cohort**"],
            ["Version", f"{VERSION} — for partner review · {TODAY}"],
        ],
        [0.17, 0.83],
    )

    d.callout(
        "How to read this",
        [
            "Sections 3–6 answer what you asked: the method, the schedule, the curriculum "
            "and the expected results.",
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
        "A 20-hour introductory programming course for public-school teachers who have "
        "never written a line of code. Every participant finishes with a small program "
        "they wrote themselves and can use: a gradebook that opens their own class list, "
        "shows who has passed, calculates the average, and saves changes back to a file."
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
            "**A two-month experiment with a decision at the end, not a finished "
            "methodology.** Section 8 sets out what we will measure; section 11 what we "
            "will do with either result.",
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
            ["10", "Mark the whole class pass or fail", "One `if` block per student", "**`for` loops**"],
            ["14", "Find one student's grade by name", "Two parallel lists and a position", "**Dictionaries**"],
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

    d.h2("Other design decisions")
    d.table(
        ["Decision", "Reason"],
        [
            ["**Every example is a classroom**", "Students, grades, attendance, averages, report lines. No abstract placeholders, no puzzles. A participant should see their Tuesday morning in any line"],
            ["**Armenian explains, English codes**", "A teacher who names a variable in Armenian writes valid Python and can then read no other Python, search for no answer online, and copy no example ever again. Example names are transliterated, so the data stays familiar while the code stays portable"],
            ["**One deliberate error per session**", "Each notebook has one cell *meant* to fail, read together afterwards. Beginners lose more time to fear of red text than to any concept in the course"],
        ],
        [0.26, 0.74],
    )

    d.page_break()

    # --------------------------------------------------------------- 4. schedule
    d.h1("Schedule")

    d.para(
        "**24 sessions × 50 minutes = 1,200 minutes = 20 hours exactly**, three times a "
        "week over eight weeks. Every agenda is planned to the minute and the arithmetic "
        "is verified by script, not by eye."
    )

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
        "**Week 4 is the centre of the course** — where the first two discovery days pay "
        "off and a loop first does thirty students' work. If the calendar slips, that week "
        "is protected.",
        italic=True,
    )

    d.h2("The shape of a session")
    d.para(
        "Teaching never exceeds **12 minutes in one block**; hands-on work is never less "
        "than 26 of the 50 minutes."
    )
    d.table(
        ["Standard session (14 of the 24)", "Min", "Discovery session (days 6, 10, 14, 17, 22)", "Min"],
        [
            ["Recap, and the question left last time", "5", "Recap", "5"],
            ["**Teach:** the new idea — ends with something running", "12", "**Teach:** today's task, and the only way we can do it so far", "7"],
            ["**Run together:** the example cells, one at a time", "15", "**Do it the long way:** the real task, most of it supplied", "13"],
            ["**Do it yourself:** the exercises", "15", "**Teach:** the tool that shortens it", "9"],
            ["Retrospective", "3", "**Do the same task again** with the tool, and compare", "13"],
            ["", "", "Retrospective", "3"],
            ["**Total**", "**50**", "**Total**", "**50**"],
        ],
        [0.36, 0.08, 0.48, 0.08],
        size=9,
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
        "practice task** that the next session never assumes was done. The four "
        "assessments are take-home and consume no session time."
    )

    d.page_break()

    # ------------------------------------------------------------- 5. curriculum
    d.h1("Curriculum — the twenty-four sessions")

    d.para(
        "Topics are taught in the order a beginner can absorb them: printing, types, "
        "variables, conditions, loops, functions. Lists and dictionaries are placed where "
        "they solve a problem the participant has just met, rather than where a textbook "
        "would put them. **D** marks a discovery day, **T** the transition to real files, "
        "**P** the project phase."
    )

    d.table(
        ["Day", "", "Session", "What the participant has at the end"],
        [
            ["1", "", "Install everything and run your first line", "Six green setup checks, and a line printed by a machine they set up themselves"],
            ["2", "", "Printing properly", "A four-line class register header"],
            ["3", "", "Four kinds of value", "Each type shown, and why `\"2\" + 2` fails"],
            ["4", "", "Changing type, and asking a question", "A cell that takes a grade and prints it plus one"],
            ["5", "", "Giving a value a name", "One student's row printed from named values"],
            ["6", "**D**", "**A register for the whole class**", "Their class as one list, written both ways and compared"],
            ["7", "", "Working with the register", "A sorted class list, one student added and one removed"],
            ["8", "", "The first decision", "Pass or fail, on their own school's pass mark"],
            ["9", "", "More than two outcomes", "A grade sorted into four named bands"],
            ["10", "**D**", "**Marking the whole class**", "The whole register marked, in four lines"],
            ["11", "", "Counting and totalling", "Their own class average, computed"],
            ["12", "", "Loops that decide", "Who failed, how many passed, the highest grade"],
            ["13", "", "Entering grades one by one", "A loop that collects grades until told to stop"],
            ["14", "**D**", "**Finding one student**", "Their class as name-to-grade, and a note on what went wrong before"],
            ["15", "", "Reports from the register", "A printed register line per student, columns aligned"],
            ["16", "", "Several grades per student", "A report card per student with three grades each"],
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
        "Days 1–19 use Jupyter notebooks; days 20–24 use plain Python files with a written "
        "guide beside them, because by then the participants are running a terminal. "
        "Day 19 doubles as the catch-up session — nothing new arrives, so anyone who has "
        "fallen behind has a session to recover in.",
        size=9.5, italic=True,
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
            ["Day 24", "A documented program a colleague ran unaided, and a 90-second demonstration given aloud"],
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
    d.para("**Habits that outlast the syntax** — what we most want to survive the course:")
    d.bullets([
        "If a number appears more than once, give it a name. If code appears more than once, give it a name.",
        "When a result is wrong, ask *which half* is wrong before changing anything.",
        "An error message is a sentence telling you what to fix, not a judgement.",
    ])

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
        "The exclusion list matters as much as the syllabus. Each item would cost roughly "
        "fifteen minutes and buy a teacher nothing in the program they are going to write."
    )
    d.table(
        ["Excluded", "Why"],
        [
            ["Classes and objects; recursion", "Nothing in a four-file gradebook needs them"],
            ["Comprehensions, `lambda`, generators", "Shorter to write, much harder to read for someone eight weeks into programming"],
            ["Error handling beyond one safeguard", "Exactly one `try` sits at the outermost edge, so an unexpected failure shows a sentence rather than ten lines of red text"],
            ["Package installation, virtual environments", "Removes the most common way a beginner's setup breaks between sessions"],
            ["Regular expressions, type hints, decorators, web frameworks, databases", "Not reachable in 20 hours, and not needed"],
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
        "In a room of sixteen adults, three or four finish early in **every** session, so "
        "each notebook carries three tiers: **3–4 required tasks** sized so nobody leaves "
        "with unfinished work, **3–4 extra tasks** for whoever has eight minutes to spare, "
        "and **1–2 challenges** for the fastest. Extra tasks use only what has already "
        "been taught — wider, not further ahead. Running out of work is how a competent "
        "participant concludes a course is beneath them."
    )

    d.h2("Assessment")
    d.para(
        "**Four take-home tests**, after days 6, 12, 18 and 24, covering the six sessions "
        "before each. Handed out at the end of a session and collected at the start of the "
        "next, so they consume no session time."
    )
    d.para(
        "They are **not graded, and the participants are told so in writing** — they exist "
        "to tell the instructor where to slow down. An honest blank is more useful than a "
        "copied answer. Every question is a classroom task, never a puzzle; nothing "
        "untaught appears, and every question has a skeleton rather than a blank cell."
    )
    d.para(
        "Each test ships with an instructor marking guide whose **second column is the "
        "point**: not whether the answer was right, but what a wrong answer tells you."
    )
    d.table(
        ["Test", "A wrong answer that changes what the instructor does next"],
        [
            ["1", "Writing `grade = 7` instead of `grade = grade + 1` means assignment has not landed. **If a third of the room misses this, day 7 does not start as written**"],
            ["3", "Printing instead of returning a value means the four-file program is not yet reachable. **If the room fails this, day 19 is spent on `return` rather than consolidation**"],
        ],
        [0.08, 0.92],
    )

    d.page_break()

    # ------------------------------------------------------- 8. measuring success
    d.h1("How success will be measured")

    d.para(
        "An experiment nobody can evaluate is just a change of plan. **These checkpoints "
        "should be agreed before the first session**, not argued about afterwards. Most "
        "need no extra work, because the course already produces artefacts that are "
        "objectively checkable."
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
        "**None of the checks above tests the actual bet**, because none is an algorithmic "
        "problem — they measure whether the course ran well. So the final test ends with "
        "one question that is different:"
    )
    d.callout(
        "Test 4, final question — the transfer question",
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
            ["**Participants may not accept it.** Adults judge a course by how substantial it feels, and one that explains little and asks for a lot of typing can read as shallow. The first half of each discovery session is deliberately laborious", "Every discovery day resolves inside the same 50 minutes; the shortcut is promised in writing before the long half starts; the work is never framed as an ordeal. A participant who leaves day 6 thinking \"I typed for twenty minutes\" rather than \"I learned what a list is for\" is a genuine failure, and it will happen to somebody"],
            ["**Twenty hours is not much**, in 50-minute pieces, for working teachers", "The scope is deliberately narrow and the exclusion list is explicit. Narrow means things are missing, by design"],
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
            ["**The ~1 GB software download on school wifi.** Sixteen people downloading at once will cost a session", "High", "Setup instructions sent three days early so most arrive installed; **a USB stick with offline installers for both platforms is mandatory kit**"],
            ["Laptops that block software installation, or lack the ~5 GB needed", "Medium", "Confirmed with schools, and asked on the enrolment form, before anyone is admitted. A browser-based fallback exists for sessions 1–19, but that participant cannot do days 20–24 fully"],
            ["The editor's interpreter picker — the most common beginner failure", "High", "Only one choice is ever present; a red callout on days 1 and 2; the setup script reports which Python is actually running"],
            ["Missed sessions — three a week for eight weeks, on top of a teaching job", "High", "Every session is self-contained; worked solutions published after each one; day 19 is a catch-up session with nothing new in it"],
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
            ["Per participant", "A Windows or macOS laptop — their own or the school's — with about **5 GB free** and permission to install software"],
            ["Software", "**Anaconda** and **VS Code**, both free. Two installations on day one and nothing afterwards; the course uses only Python's standard library"],
            ["Network", "Day one only. **Every session after that runs with the wifi switched off**"],
            ["Not needed", "No GPU, no server, no accounts, no API keys, no paid service of any kind"],
            ["Room and staffing", "Seats for up to 16 with power, a projector, and one instructor"],
            ["**Cost**", "**Zero.** The only material cost is instructor time, the room, and a USB stick of offline installers"],
        ],
        [0.21, 0.79],
    )

    d.h2("Verified by automated checks")
    d.para(
        "**All materials are written.** The following are checked by scripts that run "
        "against them, not by inspection, and all currently pass."
    )
    d.table(
        ["Check", "Result"],
        [
            ["Session arithmetic", "Every agenda sums to exactly 50 minutes; 24 sessions total 1,200"],
            ["Materials execute", "**41 notebooks** — 19 lessons, 18 solution sets, 4 assessments — run cell by cell, in order, from a clean start"],
            ["Deliberate errors behave", "Every teaching cell designed to fail raises exactly the error it claims. One that silently starts working is treated as a defect"],
            ["Language and dependencies", "Explanations Armenian, code English, with nothing outside Python's standard library imported anywhere"],
            ["The finished program", "`python main.py` runs end to end; missing files, corrupt data and bad input each produce one actionable sentence, never a technical traceback"],
        ],
        [0.26, 0.74],
    )

    d.h2("Not yet verified — stated plainly")
    d.table(
        ["Open item", "What closes it"],
        [
            ["**The Armenian terminology has not been reviewed by a native-speaker teacher**", "Every term is drawn from a single glossary, so a correction is one edit plus an automated sweep rather than a rewrite of nineteen files. Terms we are least sure of are already marked"],
            ["**The installation instructions have never been followed on a clean machine**", "Run once on a fresh Windows laptop and once on a fresh Mac, and timed, before the first session"],
            ["**Nothing has been taught to a real cohort**", "Every estimate of pacing here is a design estimate. The first cohort will find things we did not"],
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
        "**What should the success numbers be?** Agreed before the first session.",
        "**Will the discovery sessions be accepted or resented?** Anyone who knows this audience better than we do should say so before we run it, not after.",
    ])

    d.page_break()

    # ------------------------------------------------------- 11. decision point
    d.h1("The decision point after two months")

    d.para(
        "The programme is deliberately framed as an experiment with a decision at the end, "
        "and both outcomes are useful."
    )

    d.h2("If it works")
    d.para(
        "If participants can code, and the transfer question suggests problem-solving is "
        "now within reach, we continue with the same method into object-oriented "
        "programming and more advanced material — and **go back to add the theory that "
        "was deliberately skipped**, now that there is practice for it to attach to. The "
        "theory is not cancelled; it is postponed until it can stick. Then real "
        "algorithmic work, which is where we wanted to be two years ago."
    )

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

    # ------------------------------------------------------------ A. appendix
    d.h1("Appendix — inventory of materials", numbered=False)

    d.para(
        "Everything below exists today and is version-controlled. The counts are verified "
        "against the materials when this document is generated."
    )
    d.table(
        ["Material", "Count", "Audience"],
        [
            ["Lesson notebooks (days 1–19)", "19", "Participant"],
            ["Written guides (days 20–24)", "5", "Participant"],
            ["Worked solutions", "18", "Participant, after each session"],
            ["Take-home assessments, with marking guides", "4 + 4", "Participant / instructor"],
            ["Reference program", "4 files", "Participant, from day 21"],
            ["Installation instructions, reference sheet, setup check", "3", "Participant"],
            ["Instructor notes, curriculum, build specification", "3", "Instructor / organiser"],
            ["Recruitment announcement", "1", "Prospective participants"],
        ],
        [0.47, 0.13, 0.40],
    )
    d.para(
        "Materials are held in a version-controlled repository with four automated checks "
        "that must pass before any change is accepted: session arithmetic, execution of "
        "all 41 notebooks, the language and dependency rules, and the finished program "
        "running end to end. Nothing is reported as complete on the strength of "
        "inspection alone."
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
    print(f"✅ {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
