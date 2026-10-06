# The government assignment — reference extract

**Source:** «ԱԲ սերունդ» school programme curriculum, authored by the **FAST Foundation**,
approved by the Ministry of Education (ԿԳՄՍՆ), **order 1875 of 09.09.2026**. Subject:
**ՀԱՄԱԿԱՐԳՉԱՅԻՆ ԳԻՏՈՒԹՅՈՒՆ՝ PYTHON ԼԵԶՎՈՎ** (Computer Science in Python).

This file exists so the PDF never has to be parsed again. **It is a summary, not the
authority** — if a question turns on exact wording, the original is in git history
(`git show 8928479 -- docs/`).

> **The single most important thing about this document: it is a curriculum for *pupils*
> in grades 10–11, not for teachers.** 193 classroom hours over two years. Our teachers
> are the people who must deliver it. Our programme is not a compressed copy of it — it
> is the preparation that makes delivering it possible.

---

## 1. Where Python sits in the school programme

The «ԱԲ սերունդ» plan has three compulsory subjects: Advanced Algebra, **Computer Science
in Python**, and Artificial Intelligence (plus AI project learning). There are also
extracurricular project clubs, including «Python ծրագրավորումն իրական կյանքում».

Weekly hours for Python, by semester:

| | 10·S1 | 10·S2 | 11·S1 | 11·S2 | 12·S1 |
|---|---|---|---|---|---|
| Hours per week | **4** | 2 | 2 | 2 | 0 |

## 2. The four levels

| Level | Grade · semester | Topics | Hours |
|---|---|---|---|
| **Ծրագրավորման հիմունքներ** — fundamentals | 10 · S1 | 1–12 | 60 |
| **Միջին մակարդակ** — intermediate | 10 · S2 | 13–17 | 65 |
| **Խորը մակարդակ** — deep | 11 · S1 | 18–20 | 30 |
| **Տվյալների վերլուծություն և վիզուալիզացիա** — data analysis and visualisation | 11 · S2 | 21–24 | 38 |
| | | **24 topics** | **193** |

## 3. The 24 topics

Hours are given as **total (theory / practical)**. The document is heavily
practice-weighted — roughly 80% of its hours are practical, which is worth noting because
our own method makes the same choice.

### Grade 10, semester 1 — fundamentals (60 h)

| # | Topic | Hours | What it contains |
|---|---|---|---|
| 1 | Python ներածություն | 3 (2/1) | What programming is; why Python; fields of application; comparing Python to C++/Java for readability |
| 2 | Շարահյուսություն | 4 (1/3) | `.py` file structure, `print()`, **indentation**, comments `#` |
| 3 | Մուտքեր, ելքեր | 5 (1/4) | `input()` and **that it returns `str`**; string joining; **f-strings** |
| 4 | Փոփոխականներ | 4 (1/3) | Variables as named storage; naming rules; dynamic typing; `int()`, `float()`, `str()` |
| 5 | Տիպեր, տողեր | 5 (1/4) | **Strings in depth**: ASCII, mixing `int` and `str`, concatenation, **indexing, slicing, half-open ranges** |
| 6 | Թվային օպերատորներ | 6 (2/4) | `+ - * / // % **`, **operator precedence**, compound assignment, `abs` `pow` `divmod` `round` |
| 7 | Տրամաբանական օպերատորներ | 6 (2/4) | `== != > < >= <=`, `True`/`False`, `and` `or` `not`, **truth tables**, grouping with brackets |
| 8 | **Ցիկլեր** | 6 (2/4) | `while` first, then `for` and `range()`; infinite loops; `break`, `continue` |
| 9 | **Պայմաններ** | 6 (2/4) | `if`, `if-else`, `if-elif-else`; indentation's role |
| 10 | Զանգված list | 6 (2/4) | Creation, indexing, slicing; `append insert remove pop sort reverse`; **2-D lists**; mutability and references (`list2 = list1`) |
| 11 | Հավաքածուներ (Tuple, set) | 5 (2/3) | Tuples and sets; tuple methods and **unpacking**; set operations; reference vs copy; comparing list/tuple/set |
| 12 | Բառարաններ (dict) | 4 (1/3) | `{}` and `dict()`; lookup by key; **`get()` for safe access**; `keys() values() items()`; looping |

### Grade 10, semester 2 — intermediate (65 h)

| # | Topic | Hours | What it contains |
|---|---|---|---|
| 13 | Ֆունկցիաներ | 13 (2/11) | `def`, parameters, `return`; **the four shapes** of function (in/out combinations); **local and global** variables |
| 14 | Ֆայլեր | 7 (2/5) | RAM vs persistent storage; `open()` modes; **`with open()`**; `read readline readlines write writelines`; CSV |
| 15 | Մոդուլների ներածություն \| Colab | 15 (2/13) | ⚠️ **`pip` and `requirements.txt`; NumPy arrays; Matplotlib plotting; Google Colab and Jupyter.** Much more than "modules" |
| 16 | Խորացված ֆունկցիաներ | 15 (2/13) | ⚠️ Positional / keyword / default arguments; **`*args`, `**kwargs`**; multiple return with tuple unpacking; **list comprehensions**; one-line `if-else`; **`lambda`** |
| 17 | Ռեկուրսիա | 15 (3/12) | Recursion; base and recursive cases; factorial and Fibonacci; **the call stack** and Python's limits; recursion vs loops |

### Grade 11, semester 1 — deep (30 h)

| # | Topic | Hours | What it contains |
|---|---|---|---|
| 18 | Դասեր (Class) | 12 (2/10) | Class and object; `__init__`; attributes and methods; `self`; **programming paradigms** compared |
| 19 | Ժառանգականություն | 10 (2/8) | `class Child(Parent)`; multi-level inheritance; **method overriding and polymorphism** |
| 20 | Մոդուլներ և կրկնություն | 8 (2/6) | `import` and `from ... import`; NumPy, Matplotlib, functions from sklearn; revision |

### Grade 11, semester 2 — data analysis and visualisation (38 h)

| # | Topic | Hours | What it contains |
|---|---|---|---|
| 21 | Գրադարաններ և միջավայրեր | **23 (3/20)** | ⚠️ **The largest topic.** Cloud environments: Kaggle, Colab, Anaconda, Docker, Hugging Face. Package management: `pip`, `conda`, `venv`. Libraries: **numpy, matplotlib, pandas, sklearn, pytorch, tensorflow** |
| 22 | Սխալների հանգուցալուծում | 7 (1/6) | Debugging as its own topic |
| 23 | Տարբերակի և վահանակի կառավարում | 6 (1/5) | **Git and version control**; team projects; terminal |
| 24 | Ամփոփում, քննարկումներ | 2 (2/0) | Summary and discussion |

## 4. Tools the document names

Counted across all 24 topics:

| Tool | Mentions | Where it is used |
|---|---|---|
| **Thonny** | 23 | **Topics 2–14** — the default environment for everything our Part 1 teaches |
| **IDLE** | 22 | Alongside Thonny throughout |
| **Google Colab** | 16 | From topic 15 onward |
| **Profound Academy** | 13 | A platform, used throughout |
| Jupyter | 10 | From topic 16 onward |
| **VS Code** | 3 | **Topic 23 only** |
| Replit | 1 | Once |

Libraries and platforms named: NumPy, Matplotlib, pandas, sklearn, pytorch, tensorflow,
Kaggle, Anaconda, Docker, Hugging Face, git/GitHub.

> **This is the evidence behind the toolchain discussion.** The curriculum's default
> environment for the material our Part 1 covers is **Thonny**, not VS Code. Jupyter
> appears only in the advanced half; VS Code appears once, in the final topic.

## 5. How each topic is specified

Every topic in the document follows the same template, which is worth knowing because it
is the format any material we hand to the ministry would be expected to match:

- **Նպատակ** — the aim, one sentence
- **Վերջնարդյունք** — numbered learning outcomes, "by the end the pupil will be able to…"
- **Բովանդակություն** — content
- **Ուսուցման գործողություններ** — teaching activities, numbered
- **Գործիքներ/Հարթակներ** — tools and platforms
- **Հատվող թեմաներ** — cross-curricular links
- **Գնահատման չափորոշիչներ** — assessment criteria
- **Հայտորոշիչ գիտելիքներ** — prerequisite knowledge

## 6. What this means for our programme

**Our Part 1 covers the pupils' topics 1–15**, compressed from ~125 pupil-hours into
roughly 30 teacher-hours. A teacher finishing Part 1 can teach grade 10 semester 1
outright, and most of semester 2.

Deliberate divergences, agreed and recorded:

| | The document | Us | Why |
|---|---|---|---|
| Order | loops (8) **before** conditions (9) | conditions **before** loops | Our day-10 discovery needs conditions to already exist |
| Order | lists and dicts (10–12) **after** loops | all data types **before** conditions and loops | Our discovery sequence depends on it, and loops are far more useful once there is something to loop over |
| Order | recursion (17) before OOP (18) | **same** — recursion before OOP in Part 2 | Follows the document |
| OOP | grade 11 | Part 2 | Same relative position |
| Depth | full theory of each construct | the 20% that yields 80% | Teachers need to teach it, and they get the depth in Part 2 |

Known gaps against the document, with where they land:

| Topic | Gap | Plan |
|---|---|---|
| 11 — tuples and sets | Was excluded | **Added to Part 1**, lightly |
| 15, 21 — libraries and environments | NumPy, Matplotlib, pandas, pip, venv | **Part 2** |
| 16 — comprehensions, `lambda`, `*args` | On our exclusion list for Part 1 | **Part 2** |
| 23 — git | Excluded | **Out of scope for now.** Revisited for Part 2 depending on Part 1's result |
| 22 — debugging as a topic | We teach it continuously instead | Deliberate; no action |
