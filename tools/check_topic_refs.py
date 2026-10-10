"""
Check every "topic N" claim against the topic that actually teaches it.

The courses have been renumbered twice. Prose that says "topic 13, `while` loops" is not
a stale *number* -- it is a stale *claim*, and no amount of checking figures will catch
it, because 13 is a perfectly good topic number. This parses the claim instead.

    python tools/check_topic_refs.py

The map below is built from the source filenames, which are the one place the topic
numbering cannot drift from the material: src/day16_while.py IS topic 16.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# A construct, and the topic that introduces it. Keys are matched case-insensitively
# against the words around a "topic N" reference.
SUBJECTS = {
    "grade10": {
        6: ["lists"],
        7: ["tuples", "`.append()`"],
        8: ["dictionaries", "`.items()`"],
        9: ["`if`/`else`", "pass_mark"],
        10: ["`elif`"],
        11: ["`for` loop", "`for` loops"],
        12: ["`range`", "6.5"],
        16: ["`while`", "`.isdigit()`"],
        17: ["`def`"],
        18: ["`return`"],
        21: ["four files"],
        22: ["`read_text`", "`write_text`"],
    },
    "grade11": {
        4: ["comprehension", "comprehensions"],
        5: ["`lambda`", "`.get()`"],
        6: ["`__init__`"],
        9: ["inheritance", "`super()`"],
        10: ["polymorphism"],
        12: ["numpy"],
        14: ["matplotlib"],
        16: ["pandas", "`read_csv`"],
        17: ["`groupby`", "`pivot_table`"],
        19: ["recursion", "recursive"],
        20: ["`pip`", "requirements.txt"],
        21: ["debugger", "traceback"],
        22: ["five files"],
    },
}

problems = []


def check(course):
    index = {}
    for topic, words in SUBJECTS[course].items():
        for word in words:
            index.setdefault(word.lower(), set()).add(topic)

    skip = ("notebooks", "solutions", "participant", "__pycache__")
    targets = [p for p in (ROOT / course).rglob("*.md") if not any(s in p.parts for s in skip)]
    targets += [p for p in (ROOT / course).rglob("*.py") if not any(s in p.parts for s in skip)]

    # "topics 6–13" is a range and covers everything inside it; "topic 13" is a claim
    # about one topic. Only the second is checkable.
    span = re.compile(r"[Tt]opics? \d+\s*[–-]\s*\d+")
    # "state topic N" is the ministry's numbering, not this course's.
    ministry = re.compile(r"[Ss]tate [Tt]opics?[\s\d,and]*")
    reference = re.compile(r"[Tt]opics? (\d+)")
    for path in targets:
        if path.name == "CURRICULUM.md":
            continue      # the topic table itself is the authority
        for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            if "<!--history-->" in line or "<!--ref-ok-->" in line:
                continue
            masked = ministry.sub(lambda m: "·" * len(m.group(0)), line)
            masked = span.sub(lambda m: "·" * len(m.group(0)), masked)
            for match in reference.finditer(masked):
                claimed = int(match.group(1))
                window = masked[max(0, match.start() - 90):match.end() + 90].lower()
                for word, topics in index.items():
                    if re.search(r"(?<![\w`\-])" + re.escape(word) + r"(?![\w\-])", window) \
                            and claimed not in topics:
                        owner = ", ".join(str(t) for t in sorted(topics))
                        problems.append(
                            f"{path.relative_to(ROOT)}:{number}: says topic {claimed} "
                            f"beside {word!r}, which is topic {owner}")
                        break


def main():
    for course in SUBJECTS:
        check(course)
    if problems:
        print(f"❌ {len(problems)} topic reference(s) name the wrong topic:\n")
        for problem in sorted(set(problems)):
            print(f"   {problem}")
        return 1
    print("✅ every 'topic N' claim names the topic that teaches it")
    return 0


if __name__ == "__main__":
    sys.exit(main())
