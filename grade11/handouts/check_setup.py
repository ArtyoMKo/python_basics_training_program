"""Six checks, run on day 1. Every line should be green.

    python check_setup.py

If a line is red, read what it says -- it names the one thing to fix. Nothing here
installs anything: Anaconda already ships all three libraries, and if one is missing
that is a broken install rather than something you forgot.
"""

import sys

OK = "\033[92m✅\033[0m"
BAD = "\033[91m❌\033[0m"


def check(label, test):
    try:
        detail = test()
    except Exception as problem:
        print(f"{BAD} {label:<28} {problem}")
        return False
    print(f"{OK} {label:<28} {detail}")
    return True


def python_version():
    major, minor = sys.version_info[0], sys.version_info[1]
    if major < 3 or (major == 3 and minor < 9):
        raise RuntimeError(f"Python {major}.{minor} is too old -- 3.9 or newer is needed")
    return f"{major}.{minor}"


def library(name):
    def test():
        module = __import__(name)
        return module.__version__
    return test


def can_write():
    from pathlib import Path
    probe = Path("check_setup_probe.txt")
    probe.write_text("ok", encoding="utf-8")
    probe.unlink()
    return "this folder is writable"


def can_draw():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from pathlib import Path
    plt.figure()
    plt.bar(["a", "b"], [1, 2])
    plt.savefig("check_setup_probe.png", dpi=50)
    plt.close()
    Path("check_setup_probe.png").unlink()
    return "a chart was drawn and saved"


def main():
    print()
    print("Checking your setup for the grade 11 course")
    print("-" * 52)

    results = [
        check("Python", python_version),
        check("numpy", library("numpy")),
        check("pandas", library("pandas")),
        check("matplotlib", library("matplotlib")),
        check("writing files", can_write),
        check("drawing a chart", can_draw),
    ]

    print("-" * 52)
    if all(results):
        print(f"{OK} All six are green. You are ready for session 1.")
        return 0

    print(f"{BAD} {results.count(False)} of 6 need attention -- see the lines above.")
    print("   Send a screenshot of this output to your instructor before session 1.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
