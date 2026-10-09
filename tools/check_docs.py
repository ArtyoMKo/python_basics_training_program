"""
Cross-document fact check for the whole repository.

Each course's own `verify.py` proves its material runs. Nothing proved that the
DOCUMENTS agree with each other, or with the material — and that is where this
programme actually drifts: a schedule changes, twelve files get swept, two do not,
and a partner ends up holding two different answers to the same question.

    python tools/check_docs.py

Every check below is a fact restated in more than one place. If you change one,
this is what tells you where else it lives.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES = ["grade10", "grade11"]

SESSIONS = 18
MINUTES = 75
TOTAL = SESSIONS * MINUTES
HOURS, REMAINDER = divmod(TOTAL, 60)
DURATION = f"{HOURS} h {REMAINDER:02d}" if REMAINDER else f"{HOURS} h"
TOPICS = 24
DISCOVERY = {"grade10": 5, "grade11": 7}

problems = []


def read(*parts):
    path = ROOT.joinpath(*parts)
    return path.read_text(encoding="utf-8") if path.exists() else None


def fail(where, message):
    problems.append(f"{where}: {message}")


# ---------------------------------------------------------------- the session map
def check_session_map(course):
    text = read(course, "docs", "CURRICULUM.md")
    if text is None:
        return fail(course, "docs/CURRICULUM.md is missing")

    rows = re.findall(r"(?m)^\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|\s*(\d+)\s*\|$", text)
    numbers = [int(r[0]) for r in rows]
    if numbers != list(range(1, SESSIONS + 1)):
        fail(f"{course}/CURRICULUM", f"session map lists {numbers}, not 1..{SESSIONS}")
    if any(int(r[4]) != MINUTES for r in rows):
        fail(f"{course}/CURRICULUM", f"a session is not {MINUTES} minutes")

    found = sum(1 for r in rows if "Discovery" in r[3])
    if found != DISCOVERY[course]:
        fail(f"{course}/CURRICULUM",
             f"{found} discovery sessions in the map, not the {DISCOVERY[course]} claimed")

    # Every topic 1..24 must be claimed by exactly one session.
    claimed = []
    for r in rows:
        for part in r[2].split(","):
            part = part.strip()
            if re.fullmatch(r"\d+", part):
                claimed.append(int(part))
            elif re.fullmatch(r"\d+\s*[–-]\s*\d+", part):
                a, b = re.split(r"[–-]", part)
                claimed.extend(range(int(a), int(b) + 1))
    if sorted(claimed) != list(range(1, TOPICS + 1)):
        missing = sorted(set(range(1, TOPICS + 1)) - set(claimed))
        twice = sorted(t for t in set(claimed) if claimed.count(t) > 1)
        fail(f"{course}/CURRICULUM",
             f"topics not covered exactly once — missing {missing}, repeated {twice}")


# ------------------------------------------------------- figures restated in prose
def check_figures(course):
    """Figures from a schedule this programme no longer runs.

    Three schedules have been used: 24 x 75 three a week, 16 x 120 twice a week, and now
    18 x 75 twice a week. Every one left figures behind in prose, and the ones that
    survive longest are the ones a plain search misses -- abbreviated ("120 min", "32 h"),
    wrapped across a line, written in Armenian, or sitting in a .py source rather than a
    document. All four cases are covered here.
    """
    stale = [
        # English, in every spelling that has actually appeared
        (r"\b24 sessions\b", "24 sessions"),
        (r"\b16 sessions\b", "16 sessions"),
        (r"\b120 min(?:ute)?s?\b", "120 minutes"),
        (r"120-minute", "120-minute"),
        (r"\btwo-hour\b", "two-hour"),
        (r"\b30 hours?\b", "30 hours"),
        (r"\b32 hours?\b", "32 hours"),
        (r"\b32 h\b", "32 h"),
        (r"\b32 contact hours\b", "32 contact hours"),
        (r"\b20 hours?\b", "20 hours"),
        (r"\b64 teacher-hours\b", "64 teacher-hours"),
        (r"\bsixty teacher-hours\b", "sixty teacher-hours"),
        (r"1,800", "1,800 minutes"),
        (r"1,920", "1,920 minutes"),
        (r"\bof 120\b", "a figure out of 120"),
        (r"three a week", "three a week"),
        (r"three times a week", "three times a week"),
        (r"\beight weeks\b", "eight weeks"),
        (r"\b8 weeks\b", "8 weeks"),
        (r"fifty minutes", "fifty minutes"),
        (r"\b24-session\b", "24-session"),
        (r"\b16 × 120\b|\b16 x 120\b", "16 × 120"),
        (r"sums to (?:exactly )?120", "an agenda summing to 120"),
        (r"\btwo hours\b", "two hours"),
        (r"Three sessions a week", "three sessions a week"),
        (r"never below 68%", "a 68% hands-on floor"),
        (r"may never exceed \*\*15\*\* minutes|exceed 15 minutes", "a 15-minute teaching cap"),
        (r"90–75|90-75", "a broken exam duration (90–75)"),
        (r"Discovery \+", "the Discovery+ shape, which no longer exists"),
        # Armenian -- the participant-facing material is written in it
        (r"Ութ շաբաթ", "ութ շաբաթ (eight weeks)"),
        (r"ութ շաբաթ", "ութ շաբաթ (eight weeks)"),
        (r"մեկ նիստը՝ \*\*2 ժամ\*\*", "2 ժամ (two-hour sessions)"),
        (r"Դասընթացում 16-ն է", "16 sessions, in the glossary"),
        (r"քսանչորս օր", "քսանչորս օր (twenty-four days)"),
        (r"Ընդմիջումից հետո", "'after the break' — no agenda has a break block at 75 min"),
        (r"Այս նիստի առաջին կեսին", "'in the first half of this session' — from the 120-minute pairing"),
        (r"\bԵրեկ\b", "Երեկ (yesterday)"),
        (r"\bերեկ\b", "երեկ (yesterday)"),
        (r"\bվաղվանից\b", "վաղվանից (from tomorrow)"),
        (r"8 շաբաթ", "8 շաբաթ (eight weeks)"),
        (r"24 դաս", "24 դաս (twenty-four lessons)"),
        (r"24 օրը", "24 օրը (all twenty-four days)"),
        (r"Քսանչորս օր", "Քսանչորս օր (twenty-four days)"),
        (r"տասնինը օրը", "տասնինը օրը (nineteen days)"),
        (r"Ոչ պարտադիր", "homework described as optional"),
    ]

    # Exam durations are not session lengths and must survive untouched.
    durations = ["60–75 min", "60-75 min", "90–120 min", "90-120 min",
                 "90–120 minutes", "45–60 min", "45-60 min", "60–75 րոպե",
                 "90–120 րոպե", "45–60 րոպե"]

    skip = ("notebooks", "solutions", "participant", "__pycache__")
    targets = [p for p in (ROOT / course).rglob("*.md") if not any(s in p.parts for s in skip)]
    targets += [p for p in (ROOT / course).rglob("*.py") if not any(s in p.parts for s in skip)]
    targets += [p for p in (ROOT / "shared").glob("*.md")]
    targets += [p for p in (ROOT / "tools").glob("*.py")]

    for path in targets:
        text = path.read_text(encoding="utf-8")
        if path.name in ("check_docs.py", "build_partner_docx.py", "build_changelog_docx.py"):
            continue            # these name the stale figures on purpose, to detect them
        for duration in durations:
            text = text.replace(duration, "")
        # A line may cite an earlier schedule on purpose -- a comparison, or the record
        # of what changed. Those are marked <!--history--> and are not drift.
        text = "\n".join(line for line in text.split("\n") if "<!--history-->" not in line)
        # Collapse newlines so a phrase broken across two lines is still found.
        flat = re.sub(r"\s+", " ", text)
        for pattern, why in stale:
            if re.search(pattern, flat):
                fail(str(path.relative_to(ROOT)), f"still says {why}")


# --------------------------------------------------- the material matches the docs
def check_inventory(course):
    counts = {
        "notebooks": len(list((ROOT / course / "notebooks").glob("*.ipynb"))),
        "solutions": len(list((ROOT / course / "solutions").glob("*.ipynb"))),
        "tests": len(list((ROOT / course / "tests").glob("*.ipynb"))),
        "participant tests": len(list((ROOT / course / "tests" / "participant").glob("*.ipynb"))),
    }
    if counts["tests"] != 3 or counts["participant tests"] != 3:
        fail(course, f"expected 3 exams in each build, found {counts}")
    # Every notebook that sets exercises needs a solution set. Grade 10's setup notebook
    # sets none, so it has none; grade 11's does, so it has one.
    gap = counts["notebooks"] - counts["solutions"]
    if gap not in (0, 1):
        fail(course, f"{counts['notebooks']} notebooks but {counts['solutions']} solution sets")

    readme = read(course, "README.md") or ""
    claimed = re.search(r"all (\d+) — lessons, solutions", readme)
    if claimed:
        total = sum(counts.values())
        if int(claimed.group(1)) != total:
            fail(f"{course}/README", f"claims {claimed.group(1)} notebooks, there are {total}")


# ------------------------------------------------------------ assessment timing
def check_assessment(course):
    """The three sittings must name the same moment everywhere they appear."""
    curriculum = read(course, "docs", "CURRICULUM.md") or ""
    midpoint = re.search(r"Midpoint \| \*\*After session (\d+)\*\*", curriculum)
    if not midpoint:
        return fail(f"{course}/CURRICULUM", "the midpoint's session is not stated")
    session = midpoint.group(1)

    for rel in ["tests/README.md", "tests/mark2_guide.md", "docs/INSTRUCTOR_NOTES.md"]:
        text = read(course, *rel.split("/"))
        if text and "midpoint" in text.lower():
            if f"session {session}" not in text and f"After session {session}" not in text:
                fail(f"{course}/{rel}", f"does not place the midpoint after session {session}")

    final = f"session {SESSIONS}"
    for rel in ["tests/README.md", "tests/mark3_guide.md"]:
        text = read(course, *rel.split("/"))
        if text and final not in text.lower():
            fail(f"{course}/{rel}", f"does not place the final practical in {final}")

    # The exam sources are what a participant actually reads, so check them too.
    exams = {"test2_midpoint": f"{session}-րդ նիստից հետո",
             "test3_final_practical": f"{SESSIONS}-րդ նիստ"}
    for name, expected in exams.items():
        text = read(course, "src", "tests", f"{name}.py")
        if text and expected not in text:
            fail(f"{course}/src/tests/{name}.py",
                 f"its header does not say {expected!r} — this ships to participants")


# -------------------------------------------------------- links point at real files
def check_links(course):
    """Only agent-facing documents quote repository paths.

    Participant-facing material -- guides/, handouts/, the project README -- refers to
    the flat folder a participant actually receives (AGENTS.md, "Where things live"),
    so `data/my_class.csv` there is a file they create, not a file we ship.
    """
    pattern = re.compile(r"`((?:docs|tools|src|tests|guides|handouts|project|notebooks|partners)/[\w./-]+)`")
    participant_created = ("my_class.csv", "my_school.csv", "markN_guide.md")
    for path in sorted((ROOT / course).rglob("*.md")):
        if any(part in path.parts
               for part in ("notebooks", "solutions", "participant", "guides", "project")):
            continue
        for match in pattern.findall(path.read_text(encoding="utf-8")):
            target = ROOT / course / match
            if "*" in match or match.endswith("/"):
                continue
            if any(match.endswith(name) for name in participant_created):
                continue
            if not target.exists():
                fail(str(path.relative_to(ROOT)), f"points at {match}, which does not exist")


def check_homework_is_disclosed(course):
    """Homework is load-bearing on this schedule, so it must be said before enrolment.

    A paired session sets the Required tier of two notebooks. If the recruitment text or
    the enrolment guidance still calls practice optional, a teacher agrees to a course
    that is not the one they will be asked to do.
    """
    for rel in ["docs/ANNOUNCEMENT.md", "docs/ENROLMENT.md", "docs/INSTRUCTOR_NOTES.md"]:
        text = read(course, *rel.split("/"))
        if text is None:
            continue
        lowered = text.lower()
        if "տնային" not in text and "homework" not in lowered:
            fail(f"{course}/{rel}", "never mentions homework, which is now required")
        if "ոչ պարտադիր" in lowered or "optional and the next" in lowered:
            fail(f"{course}/{rel}", "still describes homework as optional")


def check_partner_documents():
    """The dossier goes outside the organisation, so it must cover both courses."""
    import xml.etree.ElementTree as ET
    import zipfile

    dossier = ROOT / "partners" / "Python_from_Zero_Programme_Dossier.docx"
    if not dossier.exists():
        return fail("partners", "the dossier has not been built")

    namespace = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    with zipfile.ZipFile(dossier) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    text = " ".join(node.text or "" for node in root.iter(f"{namespace}t"))

    # Both courses must be described, not just named.
    required = {
        "the grade-10 curriculum": "Curriculum — the grade-10 course",
        "the grade-11 curriculum": "The grade-11 curriculum",
        "the grade-11 schedule": "The grade-11 schedule",
        "the grade-11 assessment": "How the grade-11 course is assessed",
        "what a grade-11 participant finishes with": "What a grade-11 participant finishes with",
    }
    for what, phrase in required.items():
        if phrase not in text:
            fail("partners/dossier", f"does not cover {what}")

    # A deliverable from each course must appear, so neither is described in the abstract.
    for deliverable in ["python main.py"]:
        if deliverable not in text:
            fail("partners/dossier", f"never mentions {deliverable!r}")


def main():
    for course in COURSES:
        check_session_map(course)
        check_figures(course)
        check_inventory(course)
        check_assessment(course)
        check_links(course)
        check_homework_is_disclosed(course)

    # Shared documents
    shared = read("shared", "GOVERNMENT_ASSIGNMENT.md") or ""
    for needed in ["grade-10 course", "grade-11 course", "topic 23"]:
        if needed not in shared:
            fail("shared/GOVERNMENT_ASSIGNMENT.md", f"no longer mentions {needed!r}")

    check_partner_documents()

    if problems:
        print(f"❌ {len(problems)} documentation problem(s):\n")
        for problem in problems:
            print(f"   {problem}")
        return 1

    print(f"✅ both session maps: {SESSIONS} sessions × {MINUTES} min = {TOTAL} min = {DURATION}")
    print(f"✅ all {TOPICS} topics covered exactly once, in both courses")
    print("✅ no figures from an earlier schedule, in any document, source or exam")
    print("✅ assessment timing agrees across curriculum, guides and instructor notes")
    print("✅ every file path quoted in a document exists")
    print("✅ the partner dossier covers both courses — curriculum, schedule, assessment")
    print("✅ homework is disclosed as required in both courses' enrolment material")
    return 0


if __name__ == "__main__":
    sys.exit(main())
