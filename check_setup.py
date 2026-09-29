"""
Check that this computer is ready for the course.

Run it from VS Code with the play button, or from a terminal:
    python check_setup.py

Six checks, in order. It stops at the first problem and says exactly what to do.
"""

import sys
from pathlib import Path

# Each check is a separate function so a failure names exactly which one failed.
TOTAL = 6


def fail(number, title, *lines):
    print(f"❌ {number}/{TOTAL}  {title}")
    print()
    for line in lines:
        print(f"    {line}")
    print()
    sys.exit(1)


def ok(number, title):
    print(f"✅ {number}/{TOTAL}  {title}")


def check_python_version():
    version = sys.version_info
    if version < (3, 9):
        fail(1, f"Python {version.major}.{version.minor} is too old",
             "The course needs Python 3.9 or newer.",
             "Most likely the wrong kernel is selected.",
             "In the top right of VS Code, pick the one that says 'base'.")
    ok(1, f"Python {version.major}.{version.minor}.{version.micro}")


def check_anaconda():
    # Anaconda's Python has 'anaconda' or 'conda' somewhere in its path.
    where = sys.executable.lower()
    if "anaconda" in where or "conda" in where:
        ok(2, "Anaconda")
        return
    # A warning, not a failure: it may work, but the screen will not match the class.
    print(f"⚠️  2/{TOTAL}  This Python is not from Anaconda")
    print()
    print(f"    Running this Python: {sys.executable}")
    print("    Most likely a python.org Python is installed as well.")
    print("    The course will still work, but pick 'base' in VS Code if it is listed.")
    print()


def check_armenian_text():
    message = "Hello, world"
    try:
        print(f"✅ 3/{TOTAL}  Text and files work - {message}")
    except UnicodeEncodeError:
        fail(3, "Text could not be printed",
             "The terminal cannot display this text.",
             "On Windows, run it from the terminal inside VS Code, not from cmd.")


def check_folder():
    folder = Path.cwd()
    if folder.name != "python_course":
        fail(4, f"Folder is {folder.name}",
             "You are not in the python_course folder.",
             "VS Code → File → Open Folder… → Documents/python_course",
             f"You are here: {folder}")
    ok(4, "Folder: python_course")


def check_write_and_read():
    test_file = Path("_check.txt")
    try:
        test_file.write_text("Ani,9\n", encoding="utf-8")
        content = test_file.read_text(encoding="utf-8")
        test_file.unlink()
    except Exception as error:
        fail(5, "Could not write a file",
             f"Error type: {type(error).__name__}",
             "The folder is probably protected against writing.",
             "Move python_course into Documents.")
    if "Ani" not in content:
        fail(5, "The file came back wrong",
             "Always open files with encoding='utf-8'.")
    ok(5, "Writing and reading a file works")


def check_sample_class():
    sample = Path("sample_class.csv")
    if not sample.exists():
        fail(6, "sample_class.csv was not found",
             "Your instructor gave you this file. Put it in the python_course folder.",
             "Day 1 works without it, but you will need it from day 6 onwards.")
    lines = sample.read_text(encoding="utf-8").strip().splitlines()
    students = len(lines) - 1  # the first line is the header
    ok(6, f"sample_class.csv - {students} students")


if __name__ == "__main__":
    print()
    check_python_version()
    check_anaconda()
    check_armenian_text()
    check_folder()
    check_write_and_read()
    check_sample_class()
    print()
    print("Everything is ready.")
    print()
