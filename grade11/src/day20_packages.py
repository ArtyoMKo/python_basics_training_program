#%% md
# Թեմա 20 — Որտեղի՞ց է գալիս կոդը

### Python 11-րդ դասարանի համար · Թեմա 20-ը 24-ից

Ներմուծեցինք երեք գրադարան՝ numpy, matplotlib, pandas։ Ոչ մեկը մենք չենք գրել,
և ոչ մեկը չենք տեղադրել։

Այսօր պարզում ենք, թե **որտեղից են դրանք եկել**, և ինչ անել, երբ պետք լինի չորրորդը։

> ⚠️ **Սա միակ դասն է, որին ինտերնետ է պետք։** Մնացած 23-ը աշխատում են անջատված
> ցանցով։

## ԱՅՍՕՐ:

- **Ա մաս:** երեք տեսակի `import`
- **Բ մաս:** `pip` և `requirements.txt`
- **Գ մաս:** միջավայրեր և Colab

#%% md
<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#06c; margin-top:0;">🔄 Որտեղ էինք մնացել</h3>
<p style="color:#06c; margin-bottom:0;">
Ռեկուրսիա · երեք գրադարան · կիսամյակի հաշվետվությունը<br/><br/>
<b>Այսօր նայում ենք ներմուծման տակ։</b>
</p>
</div>

#%% md
## Ա մաս: Երեք տեսակի `import`

Երբ գրում ես `import something`, Python-ը փնտրում է երեք տեղում։

#%% code
import sys
from pathlib import Path

# 1. Our own files -- the folder we are sitting in
print("our folder:", Path.cwd().name)

# 2. The standard library -- ships with Python itself
import json
import random
print("standard library:", json.__name__, random.__name__)

# 3. Installed packages
import numpy
print("installed:", numpy.__name__, numpy.__version__)

#%% md
Որտե՞ղ են դրանք ֆիզիկապես։

#%% code
print("pathlib (standard):")
print("   ", Path(json.__file__).parent)
print()
print("numpy (installed):")
print("   ", Path(numpy.__file__).parent)

#%% md
<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b>Նկատի՛ր տարբերությունը։</b><br/>
Ստանդարտ գրադարանը Python-ի կողքին է։<br/>
numpy-ը <code>site-packages</code> թղթապանակում է — <b>այնտեղ, ուր տեղադրվում են
ուրիշների գրած գրադարանները</b>։<br/><br/>
Anaconda-ն տեղադրելիս այնտեղ արդեն դրել է մոտ 300 փաթեթ։ Մենք օգտագործում ենք
երեքը։
</p>
</div>

#%% md
### `import` գրելու ձևերը

#%% code
# The whole module, under its own name
import numpy
print(numpy.array([1, 2, 3]).mean())

# The whole module, under a short name -- what everyone does
import numpy as np
print(np.array([1, 2, 3]).mean())

# One piece out of it
from pathlib import Path
print(Path("school.csv").exists())

# One piece, renamed
from numpy import array as make_array
print(make_array([1, 2, 3]).mean())

#%% md
<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Մի բան, որ երբեք չգրես՝ <code>from numpy import *</code></b><br/><br/>
Այն բերում է numpy-ի բոլոր անունները քո ֆայլ, և եթե դրանցից մեկը համընկնի քո
փոփոխականի անվան հետ — <b>լուռ կփոխարինի այն</b>։<br/>
Սխալի հաղորդագրություն չի լինի։
</p>
</div>

#%% md
## Բ մաս: `pip` և `requirements.txt`

`pip`-ը այն ծրագիրն է, որը փաթեթներ է բերում ինտերնետից և դնում `site-packages`-ում։

Այն **գրվում է տերմինալում, ոչ թե նոթատետրում**։

```bash
pip list                    # ինչ կա տեղադրված
pip show numpy              # մանրամասներ մեկի մասին
pip install requests        # բերել նորը
pip uninstall requests      # հեռացնել
```

**Բացի՛ր տերմինալը VS Code-ում և գործարկի՛ր առաջին երկուսը։**

#%% code
# From inside the notebook we can at least see what is installed:
import importlib.metadata as metadata

for name in ["numpy", "pandas", "matplotlib"]:
    print(f"{name:<12} {metadata.version(name)}")

#%% md
### `requirements.txt`

Երբ ծրագիրդ ուղարկում ես գործընկերոջը, նրա համակարգչում այդ գրադարանները
կարող են չլինել։

Լուծումը՝ **ցուցակ**, որը ասում է, թե ինչ է պետք։

#%% code
from pathlib import Path

requirements = "\n".join([
    f"numpy=={metadata.version('numpy')}",
    f"pandas=={metadata.version('pandas')}",
    f"matplotlib=={metadata.version('matplotlib')}",
]) + "\n"

Path("requirements.txt").write_text(requirements, encoding="utf-8")
print(requirements)

#%% md
Գործընկերը գրում է **մեկ հրաման**, և ամեն ինչ տեղադրվում է.

```bash
pip install -r requirements.txt
```

<div style="border-left: 6px solid #0a7; background: #f2fff8; padding: 12px 16px; margin: 12px 0;">
<p style="color:#0a7; margin:0;">
✅ <b><code>numpy==1.26.4</code></b> — երկու հավասարման նշանը նշանակում է
<b>ուղիղ այս տարբերակը</b>։<br/><br/>
Ինչո՞ւ է կարևոր։ Որովհետև գրադարանները փոխվում են։ Ծրագիր, որ աշխատում էր
2024-ին, կարող է չաշխատել 2027-ի տարբերակի հետ։ Տարբերակը գրելով՝ <b>սառեցնում
ես</b> այն։
</p>
</div>

#%% md
**Հիմա դու։** Բացի՛ր տերմինալը և տեղադրի՛ր մեկ փոքր փաթեթ.

```bash
pip install emoji
```

Ապա գործարկի՛ր ներքևի բջիջը։ Եթե սխալ է տալիս՝ փաթեթը չի տեղադրվել։

#%% code
# Run this only after `pip install emoji` in the terminal.
#
# import emoji
# print(emoji.emojize("School :school: is open"))
#
# Then remove it again:  pip uninstall emoji

#%% md
## Գ մաս: Միջավայրեր և Colab

### Ինչո՞ւ են միջավայրերը պետք

Պատկերացրու՝ երկու ծրագիր ունես։ Մեկին պետք է `pandas` 1.5, մյուսին՝ 2.2։

Մեկ համակարգչում երկու տարբերակ **չի կարող միաժամանակ լինել**։

**Միջավայրը** առանձին `site-packages` թղթապանակ է. ամեն ծրագիր իր սեփականն ունի։

```bash
python -m venv myproject        # սարքել միջավայր
source myproject/bin/activate   # միացնել (macOS / Linux)
myproject\Scripts\activate      # միացնել (Windows)
pip install pandas              # տեղադրվում է ՄԻԱՅՆ այստեղ
deactivate                      # անջատել
```

<div style="border-left: 6px solid #f71; background: #fff8f2; padding: 12px 16px; margin: 12px 0;">
<p style="color:#f71; margin:0;">
📌 <b>Այս դասընթացում միջավայր չենք սարքելու։</b> Anaconda-ի <code>base</code>-ը
բավական է, և պակաս շարժվող մասեր ունենալը ավելի կարևոր է։<br/><br/>
<b>Բայց պետք է իմանաս, որ դրանք կան</b> — աշակերտների ծրագրում կան, և երբ
ծրագրերդ շատանան, քեզ էլ պետք կգան։
</p>
</div>

#%% md
### Google Colab

Colab-ը Jupyter նոթատետր է, որը աշխատում է **Google-ի համակարգչի վրա**, ոչ թե քոնի։

| | VS Code + Jupyter | Google Colab |
|---|---|---|
| Որտեղ է աշխատում | քո համակարգչում | Google-ի սերվերում |
| Տեղադրում | պետք է | **պետք չէ** |
| Ինտերնետ | պետք չէ | **պարտադիր** |
| Ֆայլերը | քո թղթապանակում | պետք է վերբեռնել |
| numpy, pandas | Anaconda-ից | **արդեն կան** |
| Աշակերտների դասագրքում | — | **16 անգամ հիշատակված** |

**Բացի՛ր** `colab.research.google.com`, սարքի՛ր նոր նոթատետր, և գործարկի՛ր.

```python
import pandas as pd
print(pd.__version__)
```

Ֆայլ վերբեռնելու համար՝ ձախ կողմի թղթապանակի նշանը → «Upload»։

<div style="border-left: 6px solid #06c; background: #f2f7ff; padding: 12px 16px; margin: 12px 0;">
<p style="color:#06c; margin:0;">
<b>Ինչո՞ւ ենք սա ցույց տալիս։</b> Որովհետև աշակերտների ծրագիրը Colab-ով է գրված,
և դպրոցի համակարգիչների վրա Anaconda տեղադրելը միշտ հնարավոր չէ։<br/><br/>
<b>Կոդը նույնն է։</b> Այն, ինչ գրել ես այս դասընթացում, աշխատում է երկուսում էլ։
</p>
</div>

#%% md
## Պարտադիր (բոլորի համար)

#%% md
### 1. Ի՞նչ կա տեղադրված

Տերմինալում գործարկի՛ր `pip list` և գտի՛ր երեք գրադարանների տարբերակները։
Գրի՛ր դրանք markdown բջիջում։

#%% code
import importlib.metadata as metadata

# Print the three versions here as well.
# ...

#%% md
### 2. Որտե՞ղ է ապրում

Տպի՛ր `pandas`-ի և `matplotlib`-ի թղթապանակները, ինչպես Ա մասում։

#%% code
# ...

#%% md
### 3. Քո `requirements.txt`-ը

Սարքի՛ր `requirements.txt` ֆայլ երեք գրադարանով և բացի՛ր այն խմբագրիչում։

#%% code
# ...

#%% md
### 4. Ներմուծման չորս ձևը

Գրի՛ր չորս տարբեր `import`, որոնք բոլորն էլ թույլ են տալիս կանչել
`numpy`-ի `mean` ֆունկցիան։

#%% code
# ...

#%% md
## Լրացուցիչ (եթե ժամանակ մնաց)

#%% md
### 5. Ստանդա՞րդ, թե՞ տեղադրված

Ահա ցուցակ։ Ամեն մեկի համար պարզի՛ր՝ ստանդարտ գրադարանի՞ց է, թե տեղադրված։

**Հուշում:** ներմուծի՛ր և նայի՛ր `__file__`-ի ճանապարհը։

#%% code
names = ["json", "numpy", "math", "pandas", "csv", "matplotlib", "datetime"]

# ...

#%% md
### 6. Մեր սեփական մոդուլը

Սարքի՛ր `my_tools.py` ֆայլ նոթատետրի կողքին, մեկ ֆունկցիայով, և ներմուծի՛ր այն։

#%% code
from pathlib import Path

Path("my_tools.py").write_text(
    'def greet(name):\n    return f"Hello, {name}"\n', encoding="utf-8")

# import my_tools
# print(my_tools.greet("Ani"))

#%% md
### 7. Տարբերակները ֆայլում

Գրի՛ր ֆունկցիա, որը սարքում է `requirements.txt` **ցանկացած** փաթեթների
ցուցակի համար։

#%% code
# ...

#%% md
### 8. Colab-ում

Վերբեռնի՛ր `school.csv`-ը Colab և գործարկի՛ր 17-րդ թեմայի `groupby`-ը այնտեղ։
Ստուգի՛ր, որ պատասխանները նույնն են՝ 11A 6.98, 11B 6.33, 11C 7.68։

#%% code
# No code here -- this one is done in the browser.

#%% md
## Մարտահրավեր

#%% md
### 9. Ի՞նչ է բերում մեկ փաթեթը

Տերմինալում գործարկի՛ր `pip show pandas` և նայի՛ր `Requires:` տողին։

pandas-ը ինքը **ուրիշ փաթեթների կարիք ունի**։ Գրի՛ր դրանք, հետո ստուգի՛ր
ամեն մեկի համար՝ նա էլ ինչի՞ կարիք ունի։

Markdown-ում նկարի՛ր ծառը։ **Սա նախորդ թեմայի ռեկուրսիան է, իրական կյանքում։**

#%% code
# ...

#%% md
### 10. Անունների բախումը

Սարքի՛ր ֆայլ՝ `random.py` անունով, նոթատետրի կողքին, մեկ տողով՝
`print("this is not the real random")`։

Ապա նոր նոթատետրում գրի՛ր `import random` և տես, թե ինչ է լինում։

Markdown-ում բացատրի՛ր, և **ջնջի՛ր ֆայլը**, որ հետո չխանգարի։

#%% code
# ...

#%% md
<div style="border-left: 6px solid #747; background: #f8f6fb; padding: 12px 16px; margin: 12px 0;">
<h3 style="color:#747; margin-top:0;">🏠 Տնային</h3>
<p style="color:#747; margin-bottom:0;">
Այս նոթատետրի <b>Պարտադիր</b> առաջադրանքները — այս նիստում երկու նոթատետր ենք անցնում, և դրանք դասին չեն տեղավորվում։<br/><b>Լրացուցիչը տանը պետք չէ անել։</b><br/><br/>
<b>Նոր բան չկա</b> — ամեն առաջադրանք այս նոթատետրից է, նույն ձևի, ինչ դասին
արածները, և օգտագործում է միայն այն, ինչ այսօր սովորեցինք։<br/>
Հաջորդ նիստը սկսվում է դրանց ստուգումով։
</p>
</div>

#%% md
## Ինչի հասանք

- `import`-ը փնտրում է **երեք տեղում**՝ մեր թղթապանակ, ստանդարտ գրադարան, `site-packages`
- `pip install` · `pip list` · `pip show` — **տերմինալում**, ոչ թե նոթատետրում
- `requirements.txt` + `pip install -r` — գործընկերը մեկ հրամանով ստանում է ամեն ինչ
- `numpy==1.26.4` — **սառեցնում** է տարբերակը
- **Միջավայր** — առանձին `site-packages` ամեն ծրագրի համար։ Գիտենք, որ կան
- **Colab** — նույն կոդը, Google-ի համակարգչի վրա։ Աշակերտների դասագրքի գործիքը
- **Երբեք `from x import *`**

## Ի՞նչ է գալիս հետո

Ծրագիրը կարող է սխալ պատասխան տալ **առանց որևէ սխալի հաղորդագրության**։
Դա ամենավտանգավոր դեպքն է։

Այս նիստի երկրորդ կեսին՝ ինչպես կարդալ traceback-ը, ինչպես կանգնեցնել ծրագիրը մեջտեղում, և
ինչպես նայել փոփոխականի ներսը, երբ այն սխալ է։
