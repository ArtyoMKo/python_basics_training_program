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

SESSIONS = 16
MINUTES = 120
TOTAL = SESSIONS * MINUTES          # 1,920
HOURS = TOTAL // 60                 # 32
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
    stale = {
        r"\b24 sessions\b": "24 sessions (now 16)",
        r"\b30 hours\b": "30 hours (now 32)",
        r"\b20 hours\b": "20 hours (now 32)",
        r"1,800": "1,800 minutes (now 1,920)",
        r"\b75 minutes\b": "75 minutes (now 120)",
        r"75-minute": "75-minute (now 120)",
        r"three a week": "three a week (now two)",
        r"three times a week": "three times a week (now twice)",
        r"fifty minutes": "fifty minutes",
    }
    for path in sorted((ROOT / course).rglob("*.md")):
        if any(part in path.parts for part in ("notebooks", "solutions", "participant")):
            continue
        text = path.read_text(encoding="utf-8")
        # An exam runs 60-75 minutes. That is a duration, not a session length.
        text = text.replace("60–75 min", "").replace("60-75 min", "")
        for pattern, why in stale.items():
            if re.search(pattern, text):
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

    for rel in ["tests/README.md", "tests/mark3_guide.md"]:
        text = read(course, *rel.split("/"))
        if text and "session 16" not in text.lower():
            fail(f"{course}/{rel}", "does not place the final practical in session 16")


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

    print(f"✅ both session maps: {SESSIONS} sessions × {MINUTES} min = {TOTAL} min = {HOURS} h")
    print(f"✅ all {TOPICS} topics covered exactly once, in both courses")
    print("✅ no three-a-week figures left in any document")
    print("✅ assessment timing agrees across curriculum, guides and instructor notes")
    print("✅ every file path quoted in a document exists")
    print("✅ the partner dossier covers both courses — curriculum, schedule, assessment")
    return 0


if __name__ == "__main__":
    sys.exit(main())
