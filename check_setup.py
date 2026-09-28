"""
Ստուգում է, որ համակարգիչը պատրաստ է դասընթացին։

Գործարկիր VS Code-ից՝ ▷ կոճակով, կամ տերմինալից՝  python check_setup.py

Վեց ստուգում, հերթով։ Կանգ է առնում առաջին խնդրի վրա և ասում, թե ուղիղ ինչ անել։
"""

import sys
from pathlib import Path

# Ամեն ստուգում գրված է առանձին, որպեսզի սխալի դեպքում պարզ լինի, թե որն է ձախողվել։
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
        fail(1, f"Python {version.major}.{version.minor} — շատ հին է",
             "Դասընթացը պահանջում է Python 3.9 կամ ավելի նոր։",
             "Ամենայն հավանականությամբ սխալ kernel է ընտրված։",
             "VS Code-ի վերևի աջ անկյունում ընտրիր այն, որի մեջ գրված է 'base'։")
    ok(1, f"Python {version.major}.{version.minor}.{version.micro}")


def check_anaconda():
    # Anaconda-ի Python-ը իր ուղու մեջ պարունակում է 'anaconda' կամ 'conda'։
    where = sys.executable.lower()
    if "anaconda" in where or "conda" in where:
        ok(2, "Anaconda")
        return
    # Ոչ թե սխալ, այլ նախազգուշացում. կարող է աշխատել, բայց դասին այլ բան կտեսնես։
    print(f"⚠️  2/{TOTAL}  Python-ը Anaconda-ից չէ")
    print()
    print(f"    Աշխատում է այս Python-ը՝ {sys.executable}")
    print("    Ամենայն հավանականությամբ python.org-ի Python է տեղադրված։")
    print("    Դասընթացը կաշխատի, բայց VS Code-ում ընտրիր 'base'-ը, եթե այն ցուցակում կա։")
    print()


def check_armenian_text():
    message = "Բարև, աշխարհ"
    try:
        print(f"✅ 3/{TOTAL}  Հայերեն տեքստը աշխատում է — {message}")
    except UnicodeEncodeError:
        fail(3, "Հայերեն տառերը չեն տպվում",
             "Տերմինալը հայերեն չի ցուցադրում։",
             "Windows-ում՝ գործարկիր VS Code-ի ներսի տերմինալից, ոչ թե cmd-ից։")


def check_folder():
    folder = Path.cwd()
    if folder.name != "python_course":
        fail(4, f"Թղթապանակը՝ {folder.name}",
             "Դու python_course թղթապանակում չես։",
             "VS Code → File → Open Folder… → Documents/python_course",
             f"Հիմա այստեղ ես՝ {folder}")
    ok(4, "Թղթապանակը՝ python_course")


def check_write_and_read():
    test_file = Path("_ստուգում.txt")
    try:
        test_file.write_text("Անի,9\n", encoding="utf-8")
        content = test_file.read_text(encoding="utf-8")
        test_file.unlink()
    except Exception as error:
        fail(5, "Ֆայլ գրել չհաջողվեց",
             f"Սխալի տեսակը՝ {type(error).__name__}",
             "Թղթապանակը, հավանաբար, պաշտպանված է գրելուց։",
             "Տեղափոխիր python_course-ը Documents-ի մեջ։")
    if "Անի" not in content:
        fail(5, "Ֆայլում հայերենը կոտրվեց",
             "Ֆայլերը միշտ բացիր encoding='utf-8' պարամետրով։")
    ok(5, "Ֆայլ գրել և կարդալ — ստացվեց")


def check_sample_class():
    sample = Path("sample_class.csv")
    if not sample.exists():
        fail(6, "sample_class.csv ֆայլը չգտնվեց",
             "Ուսուցիչը տվել է այս ֆայլը։ Դիր այն python_course թղթապանակի մեջ։",
             "Առանց դրա առաջին դասը կաշխատի, բայց 10-րդ օրվանից պետք կգա։")
    lines = sample.read_text(encoding="utf-8").strip().splitlines()
    students = len(lines) - 1  # առաջին տողը վերնագիրն է
    ok(6, f"sample_class.csv — {students} աշակերտ")


if __name__ == "__main__":
    print()
    check_python_version()
    check_anaconda()
    check_armenian_text()
    check_folder()
    check_write_and_read()
    check_sample_class()
    print()
    print("Ամեն ինչ պատրաստ է։")
    print()
