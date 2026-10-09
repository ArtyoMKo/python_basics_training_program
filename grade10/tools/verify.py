"""
Run every check. Nothing is done until this passes.

    python tools/verify.py

Four checks, in the order that makes a failure easiest to read:

  1. check_times        every agenda sums to 120; 16 sessions = 1,920 minutes
  2. run_all_notebooks  every cell of every notebook, solution and test runs in order
  3. check_style        language rule, standard library only, excluded constructs
  4. the project        python main.py runs end to end over the sample class
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHECKS = [
    ("agenda arithmetic", [sys.executable, "tools/check_times.py"], ROOT),
    ("notebooks execute", [sys.executable, "tools/run_all_notebooks.py"], ROOT),
    ("style and language", [sys.executable, "tools/check_style.py"], ROOT),
]


def run_project():
    """Drive main.py through a short menu session and check what it prints."""
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=ROOT / "project" / "gradebook",
        input="1\n2\n5\n",
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout[-2000:])
        print(result.stderr[-2000:])
        return False

    # The sample class is engineered; these numbers are quoted in the course prose.
    expected = ["students:      12", "class average: 6.5", "Did not pass (2 students)"]
    missing = [line for line in expected if line not in result.stdout]
    if missing:
        print("   the program ran but did not print:")
        for line in missing:
            print(f"     {line!r}")
        return False

    return True


def main():
    failed = []

    for name, command, cwd in CHECKS:
        print(f"── {name} " + "─" * (56 - len(name)))
        sys.stdout.flush()      # otherwise the header lands after the child's output
        result = subprocess.run(command, cwd=cwd)
        if result.returncode != 0:
            failed.append(name)
        print()

    print("── project end to end " + "─" * 39)
    sys.stdout.flush()
    if run_project():
        print("✅ python main.py: 12 students, average 6.5, 2 failing")
    else:
        failed.append("project end to end")
    print()

    if failed:
        print(f"❌ FAILED: {', '.join(failed)}")
        return 1

    print("✅ everything passes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
