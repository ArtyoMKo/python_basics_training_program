#%% md
# Օր 9 — Հարյուր պայման

### Python զրոյից · Օր 9-ը 24-ից

**Այսօր էլ նոր բան չենք սովորում։** Ուղիղ ինչպես 6-րդ օրը։

Բայց այսօր մի տարբերություն կա. այսօրվա խնդրի կեսը դու ինքդ ես լուծելու, և լուծելու
ես **այն գիտելիքով, որ արդեն ունես**։

## ԱՅՍՕՐ:

- **Ա մաս:** քսանհինգ պայման, արդեն գրված
- **Բ մաս:** անցողիկ միավորը փոխվում է
- **Գ մաս:** կես լուծում — և դու գիտես այն 5-րդ օրվանից
- **Դ մաս:** ինչը դեռ մնում է վատ

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
<code>if</code> / <code>elif</code> / <code>else</code>, չորս բացատ, և
<code>and</code> / <code>or</code> / <code>not</code>։<br/><br/>
Այսօր դրանցից պետք կգա միայն ամենապարզը՝ <code>if</code> և <code>else</code>։
</p>
</div>

#%% md
## Ա մաս: Քսանհինգ պայման

Ներքևի բջիջում քսանհինգ աշակերտ է։ Ամեն մեկի համար՝ նույն պայմանը։

Ես գրել եմ դրանք քեզ համար։ **Գործարկի՛ր և կարդա՛։**

#%% code
grade = 9
if grade >= 4:
    print("Անի: անցավ")
else:
    print("Անի: չանցավ")

grade = 6
if grade >= 4:
    print("Դավիթ: անցավ")
else:
    print("Դավիթ: չանցավ")

grade = 10
if grade >= 4:
    print("Նարե: անցավ")
else:
    print("Նարե: չանցավ")

grade = 3
if grade >= 4:
    print("Արամ: անցավ")
else:
    print("Արամ: չանցավ")

grade = 8
if grade >= 4:
    print("Մարիամ: անցավ")
else:
    print("Մարիամ: չանցավ")

grade = 5
if grade >= 4:
    print("Տիգրան: անցավ")
else:
    print("Տիգրան: չանցավ")

grade = 8
if grade >= 4:
    print("Լիլիթ: անցավ")
else:
    print("Լիլիթ: չանցավ")

grade = 4
if grade >= 4:
    print("Գոռ: անցավ")
else:
    print("Գոռ: չանցավ")

grade = 9
if grade >= 4:
    print("Անահիտ: անցավ")
else:
    print("Անահիտ: չանցավ")

grade = 2
if grade >= 4:
    print("Հայկ: անցավ")
else:
    print("Հայկ: չանցավ")

grade = 8
if grade >= 4:
    print("Սոնա: անցավ")
else:
    print("Սոնա: չանցավ")

grade = 6
if grade >= 4:
    print("Վահե: անցավ")
else:
    print("Վահե: չանցավ")

grade = 7
if grade >= 4:
    print("Մանե: անցավ")
else:
    print("Մանե: չանցավ")

grade = 5
if grade >= 4:
    print("Սամվել: անցավ")
else:
    print("Սամվել: չանցավ")

grade = 9
if grade >= 4:
    print("Էլեն: անցավ")
else:
    print("Էլեն: չանցավ")

grade = 4
if grade >= 4:
    print("Նարեկ: անցավ")
else:
    print("Նարեկ: չանցավ")

grade = 10
if grade >= 4:
    print("Ալիս: անցավ")
else:
    print("Ալիս: չանցավ")

grade = 6
if grade >= 4:
    print("Արթուր: անցավ")
else:
    print("Արթուր: չանցավ")

grade = 7
if grade >= 4:
    print("Սիրանուշ: անցավ")
else:
    print("Սիրանուշ: չանցավ")

grade = 3
if grade >= 4:
    print("Վարդան: անցավ")
else:
    print("Վարդան: չանցավ")

grade = 8
if grade >= 4:
    print("Միլենա: անցավ")
else:
    print("Միլենա: չանցավ")

grade = 9
if grade >= 4:
    print("Կարեն: անցավ")
else:
    print("Կարեն: չանցավ")

grade = 5
if grade >= 4:
    print("Անգին: անցավ")
else:
    print("Անգին: չանցավ")

grade = 6
if grade >= 4:
    print("Հրանտ: անցավ")
else:
    print("Հրանտ: չանցավ")

grade = 10
if grade >= 4:
    print("Լուսինե: անցավ")
else:
    print("Լուսինե: չանցավ")

#%% md
Աշխատում է։ Քսանհինգ աշակերտ, քսանհինգ ճիշտ պատասխան։

Հիմա նայի՛ր այդ բջիջին ուշադիր և գտի՛ր, թե **քանի անգամ** է գրված `4` թիվը։

#%% md
## Բ մաս: Անցողիկ միավորը փոխվում է

Նոր որոշում.

> «Այս տարվանից անցողիկ միավորը 4-ի փոխարեն 5 է»։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 1 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Ներքևի բջիջում նույն քսանհինգ պայմանն է։ <b>Փոխի՛ր բոլոր 4-երը 5-ի։</b><br/><br/>
Բոլորը՝ քսանհինգ հատ։ Եթե մեկը բաց թողնես, այդ աշակերտը սխալ պատասխան կստանա, և
<b>ոչ մի սխալի հաղորդագրություն չես տեսնի</b>։<br/><br/>
Նայի՛ր ժամացույցին սկսելուց առաջ։
</p>
</div>

#%% code
grade = 9
if grade >= 4:
    print("Անի: անցավ")
else:
    print("Անի: չանցավ")

grade = 6
if grade >= 4:
    print("Դավիթ: անցավ")
else:
    print("Դավիթ: չանցավ")

grade = 10
if grade >= 4:
    print("Նարե: անցավ")
else:
    print("Նարե: չանցավ")

grade = 3
if grade >= 4:
    print("Արամ: անցավ")
else:
    print("Արամ: չանցավ")

grade = 8
if grade >= 4:
    print("Մարիամ: անցավ")
else:
    print("Մարիամ: չանցավ")

grade = 5
if grade >= 4:
    print("Տիգրան: անցավ")
else:
    print("Տիգրան: չանցավ")

grade = 8
if grade >= 4:
    print("Լիլիթ: անցավ")
else:
    print("Լիլիթ: չանցավ")

grade = 4
if grade >= 4:
    print("Գոռ: անցավ")
else:
    print("Գոռ: չանցավ")

grade = 9
if grade >= 4:
    print("Անահիտ: անցավ")
else:
    print("Անահիտ: չանցավ")

grade = 2
if grade >= 4:
    print("Հայկ: անցավ")
else:
    print("Հայկ: չանցավ")

grade = 8
if grade >= 4:
    print("Սոնա: անցավ")
else:
    print("Սոնա: չանցավ")

grade = 6
if grade >= 4:
    print("Վահե: անցավ")
else:
    print("Վահե: չանցավ")

grade = 7
if grade >= 4:
    print("Մանե: անցավ")
else:
    print("Մանե: չանցավ")

grade = 5
if grade >= 4:
    print("Սամվել: անցավ")
else:
    print("Սամվել: չանցավ")

grade = 9
if grade >= 4:
    print("Էլեն: անցավ")
else:
    print("Էլեն: չանցավ")

grade = 4
if grade >= 4:
    print("Նարեկ: անցավ")
else:
    print("Նարեկ: չանցավ")

grade = 10
if grade >= 4:
    print("Ալիս: անցավ")
else:
    print("Ալիս: չանցավ")

grade = 6
if grade >= 4:
    print("Արթուր: անցավ")
else:
    print("Արթուր: չանցավ")

grade = 7
if grade >= 4:
    print("Սիրանուշ: անցավ")
else:
    print("Սիրանուշ: չանցավ")

grade = 3
if grade >= 4:
    print("Վարդան: անցավ")
else:
    print("Վարդան: չանցավ")

grade = 8
if grade >= 4:
    print("Միլենա: անցավ")
else:
    print("Միլենա: չանցավ")

grade = 9
if grade >= 4:
    print("Կարեն: անցավ")
else:
    print("Կարեն: չանցավ")

grade = 5
if grade >= 4:
    print("Անգին: անցավ")
else:
    print("Անգին: չանցավ")

grade = 6
if grade >= 4:
    print("Հրանտ: անցավ")
else:
    print("Հրանտ: չանցավ")

grade = 10
if grade >= 4:
    print("Լուսինե: անցավ")
else:
    print("Լուսինե: չանցավ")

#%% md
Որքա՞ն տևեց։ Եվ ամենակարևոր հարցը՝ **վստա՞հ ես, որ ոչ մեկը բաց չթողեցիր։**

Դա է իրական խնդիրը։ Ոչ թե ժամանակը, այլ այն, որ **ստուգելու ձև չկա**։

#%% md
## Գ մաս: Կես լուծում — և դու արդեն գիտես այն

Հարց՝ ինչո՞ւ է `4` թիվը գրված քսանհինգ անգամ։

Որովհետև այն **նույն թիվն է**։ Նույն գաղափարը՝ «անցողիկ միավոր»։ Եվ 5-րդ օրը սովորեցինք,
թե ինչ անել, երբ արժեքը անուն ունի.

> `PASS_MARK = 4`

Հետո բոլոր քսանհինգ տեղում գրում ենք `PASS_MARK`, ոչ թե թիվը։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 2 — պարտադիր</h3>
<p style="color:#900; margin-bottom:0;">
Ներքևի բջիջում դա արդեն արված է։ <b>Գործարկի՛ր և համոզվի՛ր, որ նույն արդյունքն է։</b><br/><br/>
Հետո՝ <b>ապացուցի՛ր, որ այն աշխատում է</b>.<br/><br/>
• Փոխի՛ր <code>PASS_MARK</code>-ը 5-ի։ Գործարկի՛ր։ <b>Մեկ խմբագրում։</b><br/>
• Փոխի՛ր 6-ի։ Գործարկի՛ր։ <b>Մեկ խմբագրում։</b><br/>
• Փոխի՛ր ետ 4-ի։<br/><br/>
Երեք փոփոխություն՝ երեք խմբագրում։ Առաջին անգամ դա յոթանասունհինգ խմբագրում կլիներ։
</p>
</div>

#%% code
PASS_MARK = 4

grade = 9
if grade >= PASS_MARK:
    print("Անի: անցավ")
else:
    print("Անի: չանցավ")

grade = 6
if grade >= PASS_MARK:
    print("Դավիթ: անցավ")
else:
    print("Դավիթ: չանցավ")

grade = 10
if grade >= PASS_MARK:
    print("Նարե: անցավ")
else:
    print("Նարե: չանցավ")

grade = 3
if grade >= PASS_MARK:
    print("Արամ: անցավ")
else:
    print("Արամ: չանցավ")

grade = 8
if grade >= PASS_MARK:
    print("Մարիամ: անցավ")
else:
    print("Մարիամ: չանցավ")

grade = 5
if grade >= PASS_MARK:
    print("Տիգրան: անցավ")
else:
    print("Տիգրան: չանցավ")

grade = 8
if grade >= PASS_MARK:
    print("Լիլիթ: անցավ")
else:
    print("Լիլիթ: չանցավ")

grade = 4
if grade >= PASS_MARK:
    print("Գոռ: անցավ")
else:
    print("Գոռ: չանցավ")

grade = 9
if grade >= PASS_MARK:
    print("Անահիտ: անցավ")
else:
    print("Անահիտ: չանցավ")

grade = 2
if grade >= PASS_MARK:
    print("Հայկ: անցավ")
else:
    print("Հայկ: չանցավ")

grade = 8
if grade >= PASS_MARK:
    print("Սոնա: անցավ")
else:
    print("Սոնա: չանցավ")

grade = 6
if grade >= PASS_MARK:
    print("Վահե: անցավ")
else:
    print("Վահե: չանցավ")

grade = 7
if grade >= PASS_MARK:
    print("Մանե: անցավ")
else:
    print("Մանե: չանցավ")

grade = 5
if grade >= PASS_MARK:
    print("Սամվել: անցավ")
else:
    print("Սամվել: չանցավ")

grade = 9
if grade >= PASS_MARK:
    print("Էլեն: անցավ")
else:
    print("Էլեն: չանցավ")

grade = 4
if grade >= PASS_MARK:
    print("Նարեկ: անցավ")
else:
    print("Նարեկ: չանցավ")

grade = 10
if grade >= PASS_MARK:
    print("Ալիս: անցավ")
else:
    print("Ալիս: չանցավ")

grade = 6
if grade >= PASS_MARK:
    print("Արթուր: անցավ")
else:
    print("Արթուր: չանցավ")

grade = 7
if grade >= PASS_MARK:
    print("Սիրանուշ: անցավ")
else:
    print("Սիրանուշ: չանցավ")

grade = 3
if grade >= PASS_MARK:
    print("Վարդան: անցավ")
else:
    print("Վարդան: չանցավ")

grade = 8
if grade >= PASS_MARK:
    print("Միլենա: անցավ")
else:
    print("Միլենա: չանցավ")

grade = 9
if grade >= PASS_MARK:
    print("Կարեն: անցավ")
else:
    print("Կարեն: չանցավ")

grade = 5
if grade >= PASS_MARK:
    print("Անգին: անցավ")
else:
    print("Անգին: չանցավ")

grade = 6
if grade >= PASS_MARK:
    print("Հրանտ: անցավ")
else:
    print("Հրանտ: չանցավ")

grade = 10
if grade >= PASS_MARK:
    print("Լուսինե: անցավ")
else:
    print("Լուսինե: չանցավ")

#%% md
**Ուշադրություն, թե ինչ արեցինք։** Ոչ մի նոր բան չսովորեցինք։ Օգտագործեցինք
փոփոխականը — 5-րդ օրվա գաղափարը — բայց ոչ թե տվյալ պահելու, այլ **որոշում պահելու**
համար։

Այս գաղափարը 21-րդ օրը կդառնա առանձին ֆայլ՝ `settings.py`, որտեղ կլինեն ծրագրի բոլոր
այն թվերը, որոնք կարող են փոխվել։

> **Կանոն, որը գործում է մինչև դասընթացի վերջը.**
> եթե թիվը գրված է մեկից ավելի անգամ — տո՛ւր նրան անուն։

#%% md
## Դ մաս: Ինչը դեռ մնում է վատ

Անցողիկ միավորի խնդիրը լուծված է։ Բայց նայի՛ր վերջին բջիջին նորից։

Այնտեղ դեռ **քսանհինգ գրեթե նույնական բլոկ** է։

#%% code
grade = 9
if grade >= 4:
    print("Անի: անցավ")
else:
    print("Անի: չանցավ")

grade = 6
if grade >= 4:
    print("Դավիթ: անցավ")
else:
    print("Դավիթ: չանցավ")

#%% md
Այս երկու բլոկը տարբերվում են ընդամենը երկու բանով՝ **անունով և թվով**։
Տրամաբանությունը ուղիղ նույնն է։

Եվ դա նշանակում է.

- Եթե ուզենաս «անցավ»-ի փոխարեն «բավարար» գրել — քսանհինգ խմբագրում։
- Եթե ուզենաս ավելացնել «գերազանց» մակարդակը — քսանհինգ խմբագրում։
- Եթե նոր աշակերտ գա — ևս հինգ տող՝ ձեռքով։
- Եթե մի բլոկում սխալվես — ոչ ոք չի նկատի։

#%% md
<div style="border-left: 6px solid #900; background: #fff4f4; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#900; margin-top:0;">🎯 Առաջադրանք 3 — պարտադիր. գրի՛ր, ոչ թե կոդ</h3>
<p style="color:#900; margin-bottom:0;">
Մեկնաբանության մեջ գրի՛ր <b>մեկ նախադասություն</b>. հիմա, երբ անցողիկ միավորի
խնդիրը լուծված է, <b>ի՞նչն է դեռ վատ</b> այս կոդում։<br/><br/>
Քո բառերով։ Ուսուցիչը կկարդա մի քանիսը բարձրաձայն։
</p>
</div>

#%% code
# Առաջադրանք 3 — քո նախադասությունը այստեղ։
#
# Դեռ վատն այն է, որ ...
#

#%% md
## Ինչի հասանք

- Քսանհինգ պայման՝ խմբագրված ձեռքով։ Հետո՝ մեկ փոփոխականով ուղղված։
- **Եթե թիվը գրված է մեկից ավելի անգամ — տո՛ւր նրան անուն։**
- Այդ գաղափարը 21-րդ օրը կդառնա `settings.py` ֆայլը։

## Ինչն է դեռ մեզ նյարդայնացնում

Քսանհինգ գրեթե նույնական բլոկ։ Նույն տրամաբանությունը՝ քսանհինգ անգամ պատճենված։
Ամեն փոփոխություն՝ քսանհինգ խմբագրում։

**Սա լուծվում է 14-րդ օրը։** Այդ քսանհինգ բլոկը դառնալու է **չորս տող**։
Այդ օրը նորից բացելու ենք այս տետրը և կդնենք դրանք կողք կողքի։

## Հաջորդ անգամ

Հաջորդ դասին վերադառնում ենք 6-րդ օրվա խնդրին՝ քառասուն փոփոխականին։

**Այն լուծվում է մեկ տողով։**

## Երկու րոպե ինքնուրույն (ըստ ցանկության)

Ոչինչ։ Այսօր էլ բավական գրեցիր։
