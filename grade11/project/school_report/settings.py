"""Every number and name the report depends on, in one place.

Change the school year, the pass mark or the subject list here and nowhere else.
Nothing in this file calculates anything: if you find yourself writing an `if` here,
it belongs in one of the other four files.
"""

from pathlib import Path

SCHOOL_NAME = "School N 5"
TERM = "Term 1"

# Grades run 1-10 and anything below PASS_MARK is a fail.
PASS_MARK = 4
LOWEST_GRADE = 1
HIGHEST_GRADE = 10

SUBJECTS = ["Mathematics", "Physics", "Armenian", "History", "Informatics"]

# Where the data comes from and where the report goes.
HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "data" / "school.csv"
OUTPUT_DIR = HERE / "output"

# Chart appearance, so the two chart functions do not each invent their own.
FIGURE_SIZE = (8, 4)
DPI = 150
BAR_COLOUR = "#44aa77"
HISTOGRAM_COLOUR = "#4477aa"
