"""
Հաշվարկները՝ միջին, ամենաբարձր, անցավ թե ոչ։

Այս ֆայլը ոչինչ չգիտի ֆայլերի մասին և ոչինչ չգիտի տպելու մասին։
Նա միայն հաշվում է։

Դա դիտավորյալ է. այսպես կարող ես ստուգել հաշվարկները՝ առանց ֆայլ ունենալու։
"""

import settings


def average_of(grades):
    """
    Վերադարձնում է գնահատականների միջինը՝ կլորացրած։

    Սպասում է ցուցակ՝ [9, 6, 10]։ Դատարկ ցուցակի դեպքում վերադարձնում է 0,
    որովհետև զրոյի վրա բաժանելը ծրագիրը կկանգնեցներ։
    """
    if not grades:
        return 0

    total = 0
    for grade in grades:
        total = total + grade

    return round(total / len(grades), settings.DECIMAL_PLACES)


def has_passed(grade, pass_mark=settings.PASS_MARK):
    """Վերադարձնում է True, եթե գնահատականը անցողիկ է։"""
    return grade >= pass_mark


def highest_of(class_grades):
    """
    Վերադարձնում է ամենաբարձր գնահատական ունեցող աշակերտի անունը։

    Սպասում է բառարան՝ {"Անի": 9}։ Դատարկ դասարանի դեպքում վերադարձնում է ""։
    Եթե մի քանիսը նույն բարձր գնահատականն ունեն, վերադարձնում է առաջինին։
    """
    best_name = ""
    best_grade = -1

    for student_name, grade in class_grades.items():
        if grade > best_grade:
            best_grade = grade
            best_name = student_name

    return best_name


def failing_students(class_grades, pass_mark=settings.PASS_MARK):
    """Վերադարձնում է չանցած աշակերտների անունների ցուցակը։"""
    failing = []

    for student_name, grade in class_grades.items():
        if grade < pass_mark:
            failing.append(student_name)

    return failing


def class_average(class_grades):
    """Վերադարձնում է ամբողջ դասարանի միջինը։"""
    return average_of(list(class_grades.values()))


if __name__ == "__main__":
    # Այս մասը աշխատում է միայն երբ գործարկում ես ուղիղ այս ֆայլը՝
    #     python grades.py
    # Երբ main.py-ն ներմուծում է այս ֆայլը, այս տողերը չեն աշխատում։
    test_class = {"Անի": 9, "Դավիթ": 6, "Նարե": 10, "Արամ": 3}

    print("Ստուգում՝ grades.py")
    print("Միջինը՝", class_average(test_class))
    print("Ամենաբարձրը՝", highest_of(test_class))
    print("Չեն անցել՝", failing_students(test_class))
