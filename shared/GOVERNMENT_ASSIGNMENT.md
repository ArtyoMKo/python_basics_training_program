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

**Our Part 1 covers the pupils' topics 1–14, plus the `import` half of topic 15**,
compressed from ~118 pupil-hours into roughly 30 teacher-hours. A teacher finishing Part 1
can teach **grade 10 semester 1 outright**, and the first two topics of semester 2
(functions and files).

Deliberate divergences, agreed and recorded:

| | The document | Us | Why |
|---|---|---|---|
| Order | loops (8) **before** conditions (9) | conditions **before** loops | Our day-10 discovery needs conditions to already exist |
| Order | lists and dicts (10–12) **after** loops | all data types **before** conditions and loops | Our discovery sequence depends on it, and loops are far more useful once there is something to loop over |
| Order | recursion (17) before OOP (18) | **same** — recursion before OOP in Part 2 | Follows the document |
| OOP | grade 11 | Part 2 | Same relative position |
| Depth | full theory of each construct | the 20% that yields 80% | Teachers need to teach it, and they get the depth in Part 2 |

## 7. Coverage audit — the grade-10 course, topic by topic

Checked against the built materials (`grade10/src/`, `guides/`, `project/`) on **2026-10-07**, by
searching for the specific constructs each topic names. ✅ taught · ◐ partly · ○ not yet.

| # | Topic | Part 1 | Named outcomes we do **not** yet teach |
|---|---|---|---|
| 1 | Ներածություն | ✅ | |
| 2 | Շարահյուսություն | ✅ | |
| 3 | Մուտքեր, ելքեր | ✅ | |
| 4 | Փոփոխականներ | ✅ | |
| 5 | Տիպեր, տողեր | ◐ | `ord()`/`chr()` and the ASCII idea; string **slicing** (we slice lists, never strings) |
| 6 | Թվային օպերատորներ | ◐ | `**`; compound assignment `+=`; `pow`, `divmod`; operator **precedence** as a stated rule |
| 7 | Տրամաբանական օպերատորներ | ✅ | truth tables are used but never drawn as tables |
| 8 | Ցիկլեր | ✅ | |
| 9 | Պայմաններ | ✅ | |
| 10 | Զանգված list | ◐ | `insert`, `reverse`, `.index()`; **2-D lists** (only via dict-of-lists); **mutability and references** (`list2 = list1`) |
| 11 | Tuple, set | ◐ | **tuple unpacking**; reference vs copy |
| 12 | Բառարաններ | ◐ | **`.get()` for safe access**; the `dict()` constructor |
| 13 | Ֆունկցիաներ | ◐ | **local and global** scope, and the `global` keyword |
| 14 | Ֆայլեր | ◐ | **`open()` and `with open()`**, the file modes, and `read / readline / readlines / write / writelines`. We teach `pathlib`'s `read_text` / `write_text` instead — simpler, but *not what the pupils' curriculum names* |
| 15 | Մոդուլներ \| Colab | ◐ | `pip`, `requirements.txt`, NumPy, Matplotlib, Colab. We teach `import` of our own modules (day 21) and work in Jupyter throughout |
| 16–24 | | ○ | **the grade-11 course** — see §8 |

### What to do about the gaps

Most are one cell each and could be added as **Extra tasks**, which cost no agenda time
because they are only reached by participants who finish early. Three are not:

1. **Topic 14 — `with open()`.** The widest gap, because a teacher must demonstrate the
   syntax the pupils' book uses. `pathlib` was chosen for simplicity (`PLAN.md` §0) and
   that choice still looks right for *learning*; but day 22 should show `with open()`
   once, side by side, so the teacher has seen it.
2. **Topic 13 — local and global scope.** Deferred to Part 2 stage 1 on purpose. Worth
   stating explicitly rather than leaving it to look like an oversight.
3. **Topic 10/11 — mutability and references.** Genuinely hard, and the curriculum puts
   it in grade 10. It is the one gap that is not cheap to close.

**None of these change Part 1's structure or its 30 hours.** They are additions to
existing days, and each one needs a decision before it is written.

---

## 8. Coverage audit — the grade-11 course, topic by topic

Checked against the built materials (`grade11/src/`, `guides/`, `project/`) on
**2026-10-09**, by searching for the specific constructs each topic names.
✅ taught · ◐ partly · ○ not taught.

| # | Topic | Pupil hrs | Grade 11 | Where, and what is left out |
|---|---|---|---|---|
| 15 | Մոդուլների ներածություն \| Colab | 15 | ✅ | days 1, 12, 14, 20 — `pip`, `requirements.txt`, NumPy, Matplotlib, Colab, environments |
| 16 | Խորացված ֆունկցիաներ | 15 | ✅ | days 2–5 — defaults, keyword arguments, `*args`, multiple return, comprehensions, one-line `if`/`else`, `lambda` |
| 17 | Ռեկուրսիա | 15 | ◐ | day 19 — **mechanics only.** Base case, self-call, `RecursionError`, depth-independence. **Factorial, Fibonacci, the call stack and complexity are Part 2 by decision**, and `check_style.py` fails a build that names either function |
| 18 | Դասեր (Class) | 12 | ✅ | days 6–8, 11 — `class`, `__init__`, `self`, methods, `__str__`, objects inside objects |
| 19 | Ժառանգականություն | 10 | ✅ | days 9–11 — `class X(Y)`, `super()`, overriding, polymorphism |
| 20 | Մոդուլներ և կրկնություն | 8 | ✅ | days 20, 22 — the three kinds of `import`, our own modules, the five-file split |
| 21 | Գրադարաններ և միջավայրեր | 23 | ◐ | days 12–18, 20 — **numpy, matplotlib and pandas properly.** `sklearn`, `pytorch`, `tensorflow`, Kaggle, Docker and Hugging Face are **named once on day 24 and never used** |
| 22 | Սխալների հանգուցալուծում | 7 | ✅ | day 21, and every day's error reading — tracebacks, `assert`, breakpoints, the silent wrong answer |
| 23 | Տարբերակի կառավարում (git) | 6 | ○ | **Not taught, by decision.** Taken up once the rest of the subject is secure |
| 24 | Ամփոփում | 2 | ✅ | day 24 |

### The three deliberate gaps

1. **Topic 17's algorithms.** Recursion's mechanics are taught; its algorithmic half is
   Part 2. A grade-11 teacher can demonstrate a recursive function and explain why it
   stops. They cannot yet reason about the call stack or complexity.
2. **Topic 21's long tail.** The document names six libraries and five environments. Three
   libraries are taught to the point of use; the rest are named on day 24 with what each
   one is and why a grade-11 teacher does not need it — because pupils will ask, and
   "that is difficult" is the wrong answer.
3. **Topic 23, git.** Out of scope for now. `grade11/docs/ROADMAP.md` says where it
   lands when it is taken up.

### Both courses together

| School semester | State topics | Prepared by |
|---|---|---|
| Grade 10 · S1 | 1–12 | **grade-10 course** |
| Grade 10 · S2 | 13–17 | grade-10 course (13–14) + **grade-11 course** (15–17) |
| Grade 11 · S1 | 18–20 | **grade-11 course** |
| Grade 11 · S2 | 21–24 | **grade-11 course**, except topic 23 |

**A teacher who completes both courses can deliver the whole subject except topic 23.**
That is 187 of the curriculum's 193 pupil-hours, in 60 teacher-hours.
