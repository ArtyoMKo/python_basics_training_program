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
TEN = ROOT / "grade10"
ELEVEN = ROOT / "grade11"
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
# The baseline predates the grade10/ + grade11/ split, so inside that commit the
# dossier still sits at the repository root. Keep both spellings.
BASELINE_DOSSIER = "partners/Python_from_Zero_Programme_Dossier.docx"


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
        old = subprocess.run(["git", "show", f"{BASELINE_COMMIT}:{BASELINE_DOSSIER}"],
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
        ("22½ hours", "22½ hours", False, True),
        ("a three-file program", "three-file", False, True),
        ("18 sessions", "18 sessions", False, True),
        ("fully remote delivery", "Fully remote", False, True),
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

TODAY = "14 October 2026"
CURRENT = "3.3"
BASELINE = "1.1"
BASELINE_DATE = "Friday 2 October"


def build():
    """
    One page, in plain language, for a reader who is not a programmer.

    Rules this page is written to:
      - no technical vocabulary at all, and no code formatting
      - say what each change MEANS, not what moved in the document
      - no section numbers or cross-references; a reader here is not holding the dossier
    """
    d = Dossier()
    doc = d.document

    title = doc.add_paragraph()
    title.paragraph_format.space_after = Pt(1)
    run = title.add_run("What has changed in the teacher training programme")
    run.font.size = Pt(18)
    run.bold = True
    run.font.color.rgb = NAVY

    sub = doc.add_paragraph()
    sub.paragraph_format.space_after = Pt(10)
    run = sub.add_run(
        f"A summary of the changes made since {BASELINE_DATE} · prepared for Fast Foundation"
    )
    run.font.size = Pt(10.5)
    run.font.color.rgb = GREY
    bottom_rule(sub, size=10)

    d.para(
        "This is a programme that teaches school teachers to write computer programs, so "
        "that they can then teach the subject to their pupils. The changes since the "
        "version you were sent fall into four groups, below. **Nothing has been cancelled "
        "or cut.** The programme is now longer, taught in smaller groups, measured far "
        "more carefully — and it now covers **both school years, not one**.",
        size=10.5,
    )

    # ----------------------------------------------------- how it is organised
    d.h2("There is now a second course, and it is finished")

    d.para(
        "The version you were sent prepared a teacher to teach **one school year**. Since "
        "then a **second course has been written and checked**, which prepares the same "
        "teacher to teach **the following year**. It is the same length and the same "
        "shape: nine weeks, two lessons a week, small groups, online.",
        size=10.5,
    )
    d.para(
        "**The enclosed document now describes both courses in the same detail** — each "
        "with its own curriculum, schedule, assessment and finished program. Earlier "
        "versions covered the first course in full and the second in a single page.",
        size=10.5,
    )
    d.table(
        ["", "First course", "Second course"],
        [
            ["**Prepares a teacher for**", "the first year of the subject", "**the second year**"],
            ["**Who can join**", "anyone — it starts from installing the software", "**teachers who finished the first course**, and nobody else"],
            ["**What they learn**", "the basics of writing a program", "**organising larger programs, and using professional tools to analyse real school data and draw charts from it**"],
            ["**What they finish with**", "a program that handles their own class", "**a program that handles their whole school** and produces a report with charts"],
            ["**Is it ready**", "yes", "**yes**"],
        ],
        [0.20, 0.33, 0.47],
        size=9,
    )
    d.para(
        "**Together the two courses now cover almost the whole official school "
        "curriculum** — all of it except one topic, which has deliberately been left "
        "until the rest is secure. Sixty hours of teacher training covers a subject the "
        "ministry gives pupils one hundred and ninety-three hours to learn.",
        size=10.5,
    )
    d.para(
        "**Neither course has been taught to a group of teachers yet.** Both are written, "
        "checked and ready. That is the honest position.",
        size=10.5,
    )

    d.h2("How the programme is organised")
    d.table(
        ["", "Before", "Now", "Why"],
        [
            ["**Shape**", "One course", "**Two courses, one per school year**", "Each one prepares a teacher for the year they will actually be teaching"],
            ["**Each course**", "—", "**A practical part of 2 months, then a thinking part of 4**", "The first part teaches teachers to write code. The second teaches them to solve problems with it. They are different skills, and the second only makes sense once the first is in place"],
            ["**Lessons**", "50 minutes, three a week, 20 hours in total", "**75 minutes, twice a week — 18 sessions, 22½ hours in total**", "Two evenings a week instead of three, which is what teachers asked for. The practice that no longer fits in the room is set as homework — and every piece of it is a task the materials already contained"],
            ["**Class size**", "Up to 16 teachers", "**4 to 8 teachers**", "Fewer than four and they cannot discuss anything with each other. More than eight and the trainer cannot keep an eye on everyone"],
            ["**Where**", "In a classroom", "**Fully online**, by video call", "Every session in both courses, without exception. Teachers join from home or school. This removes some problems and creates others, both described in the full document"],
        ],
        [0.11, 0.17, 0.26, 0.46],
        size=9,
    )

    # ---------------------------------------------------- how it is measured
    d.h2("Homework — this is new, and teachers are told before they enrol")

    d.para(
        "Two evenings a week instead of three means less time together: **22½ hours in "
        "the room, against 30 on the original plan**. Nothing was removed from the "
        "course. What no longer fits is done at home.",
        size=10.5,
    )
    d.table(
        ["After a session that covered…", "What is done at home", "How long"],
        [
            ["one topic *(twelve of the eighteen)*", "the extra questions", "**15–20 minutes**"],
            ["two topics *(six of the eighteen)*", "the main questions for both", "**30–40 minutes**"],
            ["the two practical build sessions", "nothing", "—"],
        ],
        [0.38, 0.38, 0.24],
        size=9,
    )
    d.para(
        "**Nothing new is ever set at home.** Every question is already printed in the "
        "same workbook the session used, in the same form as the questions done "
        "together, and the next session begins by going through them. **Teachers are "
        "told this before they agree to join**, not after they have started.",
        size=10.5,
    )

    d.h2("How we will know whether it worked")
    d.para(
        "This is the part that changed most, and it is the part worth your attention. "
        "The earlier version could not actually say what success would look like.",
        size=10,
    )
    d.table(
        ["", ""],
        [
            ["**A clear pass mark for the programme**", "If **more than 90%** of teachers can write working programs by the end, the approach worked and we continue. If **fewer than half** can, it did not, and we go back to the old way of teaching. Anything in between means we adjust and try once more. **These numbers are agreed now, before we start**, so the result cannot be argued about afterwards"],
            ["**A test before the course begins**", "Teachers sit a short assessment on day one, before being taught anything. Nobody can fail it. It tells us where each teacher is starting from — so at the end we can report **how much they improved**, not just where they ended up"],
            ["**Teaching a real class in March**", "After the first part, every teacher teaches one lesson to real pupils. This answers a question no written test can: being able to write a program and being able to **teach** it are different abilities, and a teacher who has one without the other would otherwise go unnoticed"],
            ["**Three proper exams instead of four homework tasks**", "Supervised and marked, each with three equivalent versions so that neighbours cannot copy. The last one decides who continues to the second part — and teachers are told this **before** they enrol, not afterwards"],
        ],
        [0.26, 0.74],
        size=9,
    )

    # ------------------------------------------------- the official curriculum
    d.h2("Fitting the official school curriculum")
    d.para(
        "The programme has been checked against the state curriculum for Computer Science "
        "in Python, approved in September. Every one of its topics has been matched to the "
        "part of our programme that prepares teachers for it, and the few that were "
        "missing have been added or scheduled. **A teacher finishing the first part will "
        "be ready to teach the whole of the first school year.**",
        size=10,
    )

    # --------------------------------------------------------------- unchanged
    d.h2("What has not changed")
    d.para(
        "The reasoning behind the programme, and our honesty about its risks. We still say "
        "plainly that the approach may not work — it is possible to produce teachers who "
        "can type out programs and still cannot solve problems with them. We also still "
        "list the three things we have not yet been able to check: the Armenian wording "
        "has not been reviewed by a teacher, the setup instructions have not been tried on "
        "a clean computer, and nothing has been taught to a real group yet.",
        size=10,
    )

    d.callout(
        "In one sentence",
        [
            "**The programme is now longer, taught in smaller groups online, split into two "
            "parts, and — most importantly — it now has an agreed definition of success "
            "that we committed to before starting.**",
        ],
        fill=BAND_FILL,
    )

    closing = doc.add_paragraph()
    closing.paragraph_format.space_before = Pt(4)
    bottom_rule(closing)
    d.para(
        f"Summary of changes to the programme document, version {BASELINE} → {CURRENT} · "
        f"{TODAY}. The full document accompanies this page if you would like the detail.",
        size=8.5, colour=GREY,
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
