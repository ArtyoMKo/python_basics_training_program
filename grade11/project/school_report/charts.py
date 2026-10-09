"""Two charts, saved as files.

Each function takes a School and a path, draws one picture and returns nothing.
Keeping them here means main.py never imports matplotlib, and a new chart is a
new function rather than another twenty lines in the entry point.
"""

import matplotlib.pyplot as plt

import settings


def save_subject_chart(school, path):
    """Average mark per subject, with the school average as a reference line."""
    averages = school.subject_averages()
    names = sorted(averages, key=averages.get)
    values = [averages[name] for name in names]

    plt.figure(figsize=settings.FIGURE_SIZE)
    plt.barh(names, values, color=settings.BAR_COLOUR)
    plt.xlim(0, settings.HIGHEST_GRADE)
    plt.axvline(x=school.average(), color="red", linestyle="--",
                label="school average")
    plt.xlabel("Average grade")
    plt.title(f"{school.name} — subject averages, {settings.TERM}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=settings.DPI)
    plt.close()


def save_distribution_chart(school, path):
    """How many marks of each value the school gave out."""
    marks = []
    for student in school.students():
        marks = marks + student.marks()

    plt.figure(figsize=settings.FIGURE_SIZE)
    plt.hist(marks, bins=range(settings.LOWEST_GRADE, settings.HIGHEST_GRADE + 2),
             edgecolor="white", color=settings.HISTOGRAM_COLOUR)
    plt.xlabel("Grade")
    plt.ylabel("How many")
    plt.title(f"{school.name} — grade distribution, {settings.TERM}")
    plt.tight_layout()
    plt.savefig(path, dpi=settings.DPI)
    plt.close()
