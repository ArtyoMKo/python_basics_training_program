"""
Դասարանը կարդալ ֆայլից և գրել ետ։

Այս ֆայլը ոչինչ չգիտի գնահատականների մասին։ Նրա համար դրանք պարզապես թվեր են։

Ֆայլի ձևաչափը՝
    name,grade
    Անի,9
    Դավիթ,6
"""

from pathlib import Path

import settings


def load_class(file_name=settings.CLASS_FILE):
    """
    Կարդում է ֆայլը և վերադարձնում բառարան՝ {"Անի": 9}։

    Եթե ֆայլը չկա, վերադարձնում է դատարկ բառարան և ասում այդ մասին —
    ծրագիրը չի կանգնում։
    """
    path = Path(file_name)

    if not path.exists():
        print(f"❌ {file_name} ֆայլը չգտնվեց։")
        print(f"   Ստուգի՛ր, որ այն կա, և որ settings.py-ում անունը ճիշտ է գրված։")
        return {}

    # encoding="utf-8"-ը պարտադիր է, այլապես հայերեն անունները կկոտրվեն։
    lines = path.read_text(encoding="utf-8").strip().splitlines()

    class_grades = {}

    # Առաջին տողը վերնագիրն է (name,grade), ուստի սկսում ենք երկրորդից։
    for line in lines[1:]:
        if not line.strip():
            continue

        parts = line.split(",")
        if len(parts) != 2:
            print(f"⚠️  Այս տողը բաց թողնվեց, որովհետև ստորակետը մեկը չէ՝ {line}")
            continue

        student_name = parts[0].strip()
        grade_text = parts[1].strip()

        if not grade_text.isdigit():
            print(f"⚠️  {student_name} — «{grade_text}»-ը թիվ չէ, տողը բաց թողնվեց։")
            continue

        class_grades[student_name] = int(grade_text)

    return class_grades


def save_class(class_grades, file_name=settings.CLASS_FILE):
    """Գրում է բառարանը ետ ֆայլ՝ նույն ձևաչափով։"""
    path = Path(file_name)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = ["name,grade"]
    for student_name, grade in class_grades.items():
        lines.append(f"{student_name},{grade}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"✅ Պահպանվեց՝ {file_name} ({len(class_grades)} աշակերտ)")


if __name__ == "__main__":
    print("Ստուգում՝ storage.py")
    loaded = load_class()
    print(f"Կարդացվեց {len(loaded)} աշակերտ")
    print(loaded)
