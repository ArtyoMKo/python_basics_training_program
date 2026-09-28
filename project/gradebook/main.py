"""
Մատյան — ծրագիր ուսուցչի համար։

Գործարկի՛ր այսպես՝
    python main.py

Այս ֆայլը ինքը ոչինչ չի հաշվում և ֆայլ չի կարդում։ Նա հարցնում է ուսուցչին,
թե ինչ է ուզում, և խնդրում է մյուս ֆայլերին անել այդ գործը։
"""

import grades
import settings
import storage


def show_register(class_grades):
    """Տպում է ամբողջ մատյանը։"""
    if not class_grades:
        print("Դասարանը դատարկ է։")
        return

    print()
    print("=== ՄԱՏՅԱՆ ===")

    for student_name, grade in class_grades.items():
        if grades.has_passed(grade):
            result = "անցավ"
        else:
            result = "չանցավ"
        print(f"{student_name:<{settings.NAME_WIDTH}} {grade:>3}   {result}")

    print()
    print(f"Աշակերտների թիվը՝ {len(class_grades)}")
    print(f"Դասարանի միջինը՝ {grades.class_average(class_grades)}")


def show_failing(class_grades):
    """Տպում է չանցածներին։"""
    failing = grades.failing_students(class_grades)

    print()
    if not failing:
        print("Բոլորն անցել են։")
        return

    print(f"Չեն անցել ({len(failing)} աշակերտ)՝")
    for student_name in failing:
        print(f" - {student_name}: {class_grades[student_name]}")


def add_grade(class_grades):
    """Հարցնում է անուն և գնահատական, ավելացնում կամ ուղղում է։"""
    student_name = input("Աշակերտի անունը՝ ").strip()
    if not student_name:
        print("Անունը դատարկ է — ոչինչ չավելացվեց։")
        return

    answer = input("Գնահատականը (1-10)՝ ").strip()
    if not answer.isdigit():
        print("Դա թիվ չէ — ոչինչ չավելացվեց։")
        return

    grade = int(answer)
    if grade < 1 or grade > 10:
        print("Գնահատականը պետք է լինի 1-ից 10 — ոչինչ չավելացվեց։")
        return

    if student_name in class_grades:
        print(f"{student_name}-ի գնահատականը փոխվեց {class_grades[student_name]}-ից {grade}-ի։")
    else:
        print(f"{student_name} ավելացվեց։")

    class_grades[student_name] = grade


def show_menu():
    print()
    print("1 — ցույց տալ մատյանը")
    print("2 — ցույց տալ չանցածներին")
    print("3 — ավելացնել կամ ուղղել գնահատական")
    print("4 — պահպանել")
    print("5 — դուրս գալ")


def main():
    class_grades = storage.load_class()
    print(f"Բացվեց {settings.CLASS_FILE} — {len(class_grades)} աշակերտ")

    while True:
        show_menu()
        choice = input("Ընտրի՛ր՝ ").strip()

        if choice == "1":
            show_register(class_grades)
        elif choice == "2":
            show_failing(class_grades)
        elif choice == "3":
            add_grade(class_grades)
        elif choice == "4":
            storage.save_class(class_grades)
        elif choice == "5":
            print("Ցտեսություն։")
            break
        else:
            print("Այդպիսի հրաման չկա։ Գրի՛ր 1-ից 5։")


if __name__ == "__main__":
    # Մեկ try/except ամբողջ ծրագրում, ամենադրսում։
    # Եթե ինչ-որ անսպասելի բան պատահի, ուսուցիչը տեսնի հասկանալի նախադասություն,
    # ոչ թե տասը տող կարմիր տեքստ։
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Ընդհատվեց։ Ցտեսություն։")
    except Exception as error:
        print()
        print(f"Անսպասելի սխալ՝ {type(error).__name__}: {error}")
        print("Ցույց տո՛ւր այս տողը ուսուցչին։")
