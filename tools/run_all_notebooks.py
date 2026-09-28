"""
Execute every notebook cell, in order, and report what failed.

    python tools/run_all_notebooks.py            # all notebooks
    python tools/run_all_notebooks.py day07      # one

Three course-specific rules, from PLAN.md section 11.2:

1. Each notebook runs in a FRESH namespace, cells in order. A cell that depends on a
   cell above it must work when the participant runs top to bottom.
2. Cells tagged `interactive` have input() replaced by a scripted answer. A notebook
   must never block waiting for a human.
3. Cells tagged `expected_error` MUST raise exactly that error. These are the
   "break it on purpose" cells; one that stops raising is a bug in the notebook.
"""

import builtins
import io
import json
import sys
import traceback
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS = ROOT / "notebooks"


def run_notebook(path):
    """Return (failures, executed, expected_errors_seen)."""
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    failures = []
    executed = 0
    deliberate = 0

    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] != "code":
            continue

        source = "".join(cell["source"])
        if not source.strip():
            continue

        metadata = cell.get("metadata", {})
        expected = metadata.get("expected_error")
        answers = list(metadata.get("interactive_input", []))

        # input() must never block. Feed the scripted answers, then fail loudly.
        def fake_input(prompt=""):
            if not answers:
                raise AssertionError(
                    "cell called input() more times than it has scripted answers"
                )
            return answers.pop(0)

        real_input = builtins.input
        builtins.input = fake_input
        executed += 1

        try:
            with redirect_stdout(io.StringIO()):
                exec(compile(source, f"{path.name}:cell{index}", "exec"), namespace)
        except BaseException as error:
            name = type(error).__name__
            if expected and name == expected:
                deliberate += 1
            elif expected:
                failures.append(
                    f"cell {index}: expected {expected}, got {name}: {error}"
                )
            else:
                line = traceback.format_exc().strip().splitlines()[-1]
                failures.append(f"cell {index}: {line}")
        else:
            if expected:
                failures.append(
                    f"cell {index}: expected {expected} but the cell ran fine "
                    f"-- the break-it-on-purpose demo is broken"
                )
        finally:
            builtins.input = real_input

        if answers:
            failures.append(
                f"cell {index}: {len(answers)} scripted answer(s) left unused"
            )

    return failures, executed, deliberate


def main(argv):
    wanted = argv[1] if len(argv) > 1 else None
    paths = sorted(NOTEBOOKS.glob("*.ipynb"))
    if wanted:
        paths = [p for p in paths if p.stem.startswith(wanted)]
    if not paths:
        print(f"❌ No notebooks found" + (f" matching '{wanted}'" if wanted else ""))
        return 1

    # Notebooks read sample_class.csv by a bare filename, exactly as a participant
    # does with the folder open in VS Code.
    import os
    os.chdir(NOTEBOOKS)

    total_failures = 0
    for path in paths:
        failures, executed, deliberate = run_notebook(path)
        total_failures += len(failures)
        mark = "✅" if not failures else "❌"
        extra = f", {deliberate} deliberate error(s) raised as designed" if deliberate else ""
        print(f"{mark} {path.stem:<32} {executed:>3} code cells{extra}")
        for failure in failures:
            print(f"      {failure}")

    print()
    if total_failures:
        print(f"❌ {total_failures} problem(s) across {len(paths)} notebook(s)")
        return 1
    print(f"✅ {len(paths)} notebook(s), every cell executed in order")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
