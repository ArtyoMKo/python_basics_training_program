#%% md
# Օր 9 — Լուծումներ

#%% code
# Առաջադրանք 2 — մեկ փոփոխական քսանհինգ թվի փոխարեն

PASS_MARK = 4

class_grades = {"Անի": 9, "Դավիթ": 6, "Նարե": 10, "Արամ": 3}

for student_name, grade in class_grades.items():
    if grade >= PASS_MARK:
        print(f"{student_name}: անցավ")
    else:
        print(f"{student_name}: չանցավ")

#%% md
> Այս լուծումը ցիկլ է օգտագործում, որը դեռ չենք սովորել 9-րդ օրը։ Այն այստեղ է,
> որպեսզի տեսնես, թե ուր ենք գնում։ **14-րդ օրը դա գրելու ես ինքդ։**
