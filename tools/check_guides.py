"""
Check that the written guides build the reference project.

verify.py proves the finished `project/` folder runs. Nothing proved that a participant
following `guides/*.md` step by step arrives at it -- so a guide could instruct
`grades.class_average(...)` for a function no step ever creates, and every tool would
still report green. That happened, and it broke the course's hard gate.

    python tools/check_guides.py

Every `module.name` a guide writes must exist in the module the project actually ships.
"""

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = {"grade10": "gradebook", "grade11": "school_report"}

# Module names the projects have used at some point. A guide naming one that the project
# no longer ships is pointing at a file that was renamed or folded away.
RETIRED = {"settings", "storage", "grades", "people", "loading", "charts", "report"}

problems = []


def names_defined(path):
    """Top-level functions, classes and constants in one module."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            found.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    found.add(target.id)
    return found


def check(course):
    folder = ROOT / course / "project" / PROJECTS[course]
    if not folder.exists():
        return
    modules = {p.stem: names_defined(p) for p in folder.glob("*.py")}

    guides = sorted((ROOT / course / "guides").glob("*.md"))
    for guide in guides:
        text = guide.read_text(encoding="utf-8")
        blocks = re.findall(r"```python\n(.*?)```", text, re.DOTALL)
        for block in blocks:
            for module, attribute in re.findall(r"\b(\w+)\.(\w+)\s*[\(\),:\]]", block):
                if module not in modules:
                    # A name that looks like one of OUR modules but is not in the project
                    # is the more dangerous case: a guide referring to a file that was
                    # renamed or folded away. Everything else (pathlib, plt) is external.
                    if module in RETIRED:
                        problems.append(
                            f"{guide.relative_to(ROOT)}: writes `{module}.{attribute}`, "
                            f"but `{module}.py` is not part of project/"
                            f"{PROJECTS[course]}/ any more")
                    continue
                if attribute not in modules[module]:
                    problems.append(
                        f"{guide.relative_to(ROOT)}: writes `{module}.{attribute}`, "
                        f"which `project/{PROJECTS[course]}/{module}.py` does not define")

        # A guide must not import a module the project does not ship.
        for imported in re.findall(r"(?m)^import (\w+)$", "\n".join(blocks)):
            if imported.islower() and imported not in modules and imported in (
                    "settings", "storage", "grades", "people", "loading", "charts"):
                problems.append(
                    f"{guide.relative_to(ROOT)}: imports `{imported}`, which is not a "
                    f"module of project/{PROJECTS[course]}/")


def main():
    for course in PROJECTS:
        check(course)
    if problems:
        print(f"❌ {len(problems)} guide instruction(s) do not match the project:\n")
        for problem in sorted(set(problems)):
            print(f"   {problem}")
        return 1
    print("✅ every `module.name` the guides write exists in the project they build")
    return 0


if __name__ == "__main__":
    sys.exit(main())
