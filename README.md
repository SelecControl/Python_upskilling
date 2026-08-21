# Python Upskilling — Guided Course

A structured, graded walk through core programming concepts in Python.
Modules 1–9 cover the full syllabus: flowcharts and pseudocode, data types,
operators, conditionals, loops, functions, strings, lists/dictionaries, recursion.

---

## How each round works

1. **Teaching** — a few tight points on one topic, with examples
2. **Theory** — questions answered in your own words, typed, no lookups
3. **Correction** — what's right, what's shaky, what's wrong
4. **Code** — a real problem to solve
5. **Rating** — score plus specific gaps, then move on

Rules: don't paste code you didn't write. If you don't know, write "not sure"
rather than guessing vaguely. Wrong answers are more useful than blank ones.

---

## Progress so far

| Round | Topic | Theory | Code | Notes |
|---|---|---|---|---|
| 1 | Flowcharts & Pseudocode | 6/10 | 8/10 | leap-year logic correct first try |
| 2 | Data Types & Variables | 9/10 | 8.5/10 | mutable/immutable solid |
| 3 | Operators & Expressions | 8/10 | 6.5 → 8/10 | BMI boundary-gap bug, then fixed |
| 4 | Conditionals | 7.5/10 | 6.5/10 | match-case correct |
| 5 | Loops & Loop Control | 7/10 | 3 → 9/10 | unreachable branch + inverted for/else |
| 6 | Functions | 7.5/10 | 6.5/10 | mutable default trap missed |
| 7 | Strings | 9/10 | **10/10** | best round — palindrome + sentence stats |
| 8 | Lists & Dictionaries | pending | pending | |
| 9 | Recursion | pending | pending | |

### Files written so far

| File | Round | What it does |
|---|---|---|
| `EVEN_ODD.py` | 1 | even/odd via modulus |
| `LEAP_YEAR.py` | 1 | leap year, nested decision tree |
| `celsiustofahrenheit.py` | 2 | C to F, 2 decimal places |
| `sectoHMS.py` | 2 | seconds to hours/minutes/seconds |
| `BMIcalc.py` | 3, 6 | BMI + category, later refactored into functions |
| `digitsurvey.py` | 3 | 3-digit sum and reverse, arithmetic only |
| `calculator.py` | 4 | match-case calculator, divide-by-zero guarded |
| `report.py` | 4 | student grade report, guard clause |
| `fizzbuzz.py` | 5 | classic FizzBuzz |
| `prime.py` | 5, 6 | primality via for/else, later `is_prime()` |
| `cart.py` | 6 | `*args`, default and keyword arguments |
| `palindrome.py` | 7 | case/space-insensitive palindrome |
| `sentance.py` | 7 | word count, longest word, reversed words |

---

# Module 1 — Flowcharts & Pseudocode

## Why this exists

Code is *how*; an algorithm is *what*. Decide the steps before typing Python.
Beginners get stuck because they try to solve the problem and write the syntax
at the same time — two hard things at once.

## The 5 flowchart symbols

| Symbol | Shape | Means |
|---|---|---|
| Terminal | Oval / rounded | Start, Stop |
| Input/Output | Parallelogram | Read a value, Print a value |
| Process | Rectangle | A calculation or assignment |
| Decision | Diamond | A yes/no question — **exactly 2 arrows out** |
| Flow line | Arrow | Order of execution |

A diamond is the **only** symbol with two exits. That single property is what
gives a program the ability to branch or loop at all.

**Test to remember:** does it *do*, or does it *ask*?
Do → rectangle. Ask → diamond.

## The three control structures

Every program ever written is made of only these three, combined:

- **Sequence** — do A, then B, then C
- **Selection** — if a condition holds do A, else do B (the diamond)
- **Iteration** — repeat A while a condition holds

The key difference: in **if-else**, both branches move *forward* and merge below,
so flow never revisits a symbol. In a **loop**, one branch travels *backward* to a
point above the diamond, so the same symbols execute again. Same diamond,
different arrow destination.

## Pseudocode

English-like steps, no syntax rules, indentation shows structure.

```
START
   READ a, b
   IF a > b THEN
      PRINT a
   ELSE
      PRINT b
   ENDIF
STOP
```

Conventions: `READ`/`PRINT` for I/O, `SET x = ...` for assignment,
`IF/ENDIF`, `WHILE/ENDWHILE` to mark where blocks end, `MOD` for remainder.

## Loops need three parts

**Initialise, test, update.** Miss the update and you get an infinite loop.

```
SET i = 1                 <- initialise
WHILE i <= 5              <- test
   PRINT i
   SET i = i + 1          <- update
ENDWHILE
```

---

# Module 2 — Data Types & Variables

## A variable is a label, not a box

Most tutorials say "a variable is a container that holds a value." In Python
that's **wrong** and it causes confusion later. A variable is a **name tag stuck
onto an object**.

```python
a = 5      # object 5 exists; name 'a' points at it
b = a      # 'b' points at the SAME object; nothing was copied
```

## The core types

| Type | Example | Notes |
|---|---|---|
| `int` | `5`, `-3` | whole numbers, unlimited size |
| `float` | `3.14`, `2.0` | the `.` makes it a float |
| `str` | `"hi"`, `'hi'` | quotes make it a string |
| `bool` | `True`, `False` | capital T and F, always |
| `NoneType` | `None` | "no value at all" — different from `0` or `""` |

`2` and `2.0` are *different types* with the same value. Check with `type(x)`.

## Typecasting

```python
int("5")      # 5      str -> int
int(5.9)      # 5      TRUNCATES toward zero — int(-7.9) is -7
round(5.9)    # 6      actual rounding
float("3.14") # 3.14
str(5)        # "5"
int("abc")    # ValueError
bool(0)       # False
bool("")      # False
bool("False") # True — any non-empty string is truthy
```

`input()` **always** returns a `str`. Forget to cast and `"5" + "3"` is `"53"`, not `8`.

## Mutable vs immutable — the big one

- **Immutable**: `int`, `float`, `str`, `bool`, `tuple`
- **Mutable**: `list`, `dict`, `set`

```python
s = "hello"
s[0] = "H"        # TypeError — strings are immutable
s = "Hello"       # fine — builds a NEW string, re-points the label
```

```python
a = [1, 2, 3]
b = a             # b points at the SAME list
b.append(4)
print(a)          # [1, 2, 3, 4]  <- a changed too
c = a.copy()      # a genuinely independent list
```

Immutability is a property of the **object**, not the variable. When you write
`s = "bye"`, the string `"hi"` never changed — the *name* moved to a different object.

## None vs 0 vs ""

Three different types, three different objects. All three are **falsy**, but
falsy is not the same as boolean:

```python
0 == False      # True  (equal in value)
0 is False      # False (different objects, different types)
```

Why it matters:

```python
score = 0          # student genuinely scored zero
if score:          # skips! 0 is falsy
    print(score)   # bug: a real answer silently ignored
```

Fix by saying what you mean: `if score is not None:`.
**`None` means "no answer yet." `0` means "the answer is zero."**

## Naming rules

Start with a letter or `_`, no spaces, case-sensitive, no keywords.
Convention: `snake_case` for variables, `UPPER_CASE` for constants.
`CapitalizedNames` are reserved for **classes**.

---

# Module 3 — Operators & Expressions

## Arithmetic

```python
7 / 2      # 3.5   TRUE division — ALWAYS returns a float
7 // 2     # 3     FLOOR division — rounds DOWN
7 % 2      # 1     modulus — the remainder
2 ** 10    # 1024  exponent (not ^)
```

Two traps:
- `6 / 2` gives `3.0`, a **float**, never an int
- `//` **floors**, it does not truncate: `-7 // 2` is `-4`, not `-3`

## Comparison operators return booleans

`==`  `!=`  `>`  `<`  `>=`  `<=` — each evaluates to `True` or `False`.

Python allows **chaining**, unlike most languages:

```python
if 0 < age < 18:      # reads like maths
```

## Logical operators

| | Result |
|---|---|
| `A and B` | True only if **both** are true |
| `A or B` | True if **at least one** is true |
| `not A` | flips it |

**Short-circuiting** — Python stops as soon as the answer is certain:

```python
if n != 0 and 100 / n > 5:     # if n is 0, the second half NEVER RUNS
```

Not an optimisation, a **safety technique**. Order matters: put the guard first.

## Precedence, high to low

```
**              exponent
-x              unary minus
* / // %        multiply/divide
+ -             add/subtract
< <= > >= == != comparisons
not
and
or
```

`2 + 3 * 4 ** 2` → `4**2=16` → `3*16=48` → `2+48` = **50**.

## Compound assignment

```python
count += 1        # count = count + 1
total -= 5
price *= 1.18
n //= 2
```

## == vs is

- `==` asks **"same value?"**
- `is` asks **"same object in memory?"**

```python
10 == 10.0     # True  — int and float compare by NUMERIC VALUE
10 is 10.0     # False — two distinct objects
"5" == 5       # False — str and int, no conversion
[1,2] == [1,2] # True  — same contents
[1,2] is [1,2] # False — two separate list objects
```

**Type identity does not control value equality.** `10 == 10.0` is True because
both are *numbers* at the same point on the number line.

**Use `is` only for the three singletons: `None`, `True`, `False`.**
`if result is None:` is correct. `if name is "Sam":` is a bug that sometimes appears to work.

---

# Module 4 — Conditionals

## Truthiness — `if` doesn't need a comparison

`if` accepts **any** value and asks "is this truthy?"

**Falsy** (the complete list): `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`
**Truthy**: everything else

```python
name = input("Name: ")
if name:              # instead of: if name != ""
    print(f"Hi {name}")
```

`if my_list:` beats `if len(my_list) > 0:` because it is the idiom every Python
reader expects, it works unchanged for strings/dicts/sets/tuples, and it is
**safe against `None`** — `len(None)` raises `TypeError`.

But remember the Module 2 trap: `if score:` is wrong when `0` is a legitimate
value. Use `if score is not None:` there.

## The ternary — one-line if/else

```python
status = "Adult" if age >= 18 else "Minor"
```

Reads: *value-if-true* `if` *condition* `else` *value-if-false*.
Use it **only** when picking between two values. Never nest ternaries.

## and / or / not inside conditions

```python
if age >= 18 and has_id:
if day == "Sat" or day == "Sun":
if day in ("Sat", "Sun"):        # better — no repetition
if not is_logged_in:
```

`in` checks membership and beats a chain of `or`s every time.

## match-case (Python 3.10+)

```python
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause" | "hold":        # | means OR
        print("Paused")
    case _:                       # _ is the default, like else
        print("Unknown command")
```

**When to use which:** `match` for one variable against **discrete fixed values**.
`elif` for **ranges and complex conditions** — `match` cannot express `< 18.5`.
No fall-through, no `break` needed.

## Nesting — when it's justified

Genuine nesting is fine when conditions are **dependent**:

```python
if is_logged_in:
    if is_admin:          # only meaningful IF logged in
        show_admin_panel()
```

`elif` is better than an `else` containing an `if` because it keeps everything at
**one indentation level**, so the branches are visibly a single mutually-exclusive
chain read top to bottom. Four nested conditions become sixteen spaces of
indentation and you lose sight of the structure.

**Rule of thumb:** more than 2 levels of indentation means rethink the structure.

## Boundary gaps — a real bug from Round 3

```python
if 18.5 <= bmi <= 24.9:      # WRONG for floats
elif 25 <= bmi <= 29.9:
```

A BMI of `24.913` matches **neither** — it falls through to `else`. There is a
hole between 24.9 and 25.0. The fix is to never bound both ends:

```python
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
```

Each `elif` reads "not the previous one, and under X" — no gap is possible.
**For continuous ranges use one-sided tests and let `elif` supply the lower bound.**
Chained comparisons are great for *discrete* values, dangerous for floats.

---

# Module 5 — Loops & Loop Control

## while — repeat while a condition holds

```python
count = 1                # initialise
while count <= 5:        # test
    print(count)
    count += 1           # update  <- forget this = infinite loop
```

`while True:` is deliberate infinity — you `break` out manually.

## for — repeat over a sequence

```python
for char in "hello":
    print(char)

for item in [10, 20, 30]:
    print(item)
```

**Use `for` when you know the collection** (print every character in a name).
**Use `while` when you don't know how many rounds** (keep asking until the
password is correct).

## range()

```python
range(5)          # 0 1 2 3 4        stop only — starts at 0
range(1, 6)       # 1 2 3 4 5        start, stop
range(1, 10, 2)   # 1 3 5 7 9        start, stop, step
range(10, 0, -1)  # 10 9 8 ... 1     counting down
```

**The stop value is always excluded.** `range(1, n + 1)` is the idiom for
"1 through n inclusive" — the `+ 1` compensates. This off-by-one is the most
common loop bug there is.

## The accumulator pattern

```python
total = 0                      # initialise BEFORE the loop
for n in range(1, 6):
    total += n                 # accumulate INSIDE
print(total)                   # 15 — use AFTER
```

Put `total = 0` **inside** the loop and it resets every round, so it holds only
the most recent value: you get `5` instead of `15`. Note the loop still
terminates normally — it just reports a **wrong answer**, which is far more
dangerous than an infinite loop, because an infinite loop announces itself.

## break and continue

- **`break`** — leave the loop entirely, right now
- **`continue`** — skip the rest of this round, jump to the next

```python
for n in range(1, 7):
    if n == 3:
        continue          # skip 3
    if n == 5:
        break             # stop before printing 5
    print(n)              # 1 2 4
```

Both affect **only the innermost loop** they're inside.

## for...else — read it as "no break"

A loop's `else` runs **only if the loop finished without hitting `break`**:

```python
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")        # only if we never broke out
```

`break` = found it. `else` = searched everything, found nothing.
An **empty** loop still triggers `else` — which is why `num = 2` works:
`range(2, 2)` never runs, no break, so `else` correctly reports prime.

## Nested loops

```python
for i in range(3):
    for j in range(4):
        print(i, j)       # runs 3 x 4 = 12 times
```

The inner loop runs completely for **each** step of the outer.

## Unreachable branches — a real bug from Round 5

```python
if i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
elif i % 3 == 0 and i % 5 == 0:   # DEAD CODE — never runs
    print("FizzBuzz")
```

Any number divisible by both already matched the **first** branch.
**In an if/elif chain the most specific condition must come first.**

---

# Module 6 — Functions

## Definition and call

```python
def greet(name):          # def, name, parameters, colon
    print(f"Hello {name}")

greet("Priya")            # the call — this is what runs it
```

Defining a function **runs nothing**. It stores the recipe. A common beginner
surprise: the file runs, prints nothing, and nothing is wrong — you defined and
never called.

## Parameters vs arguments

```python
def add(a, b):        # a, b are PARAMETERS (the placeholders)
    return a + b

add(3, 5)             # 3, 5 are ARGUMENTS (the actual values)
```

## return vs print — the distinction that matters most

```python
def double_print(n):
    print(n * 2)          # shows a human, gives back NOTHING

def double_return(n):
    return n * 2          # HANDS THE VALUE BACK to the caller

x = double_print(5)       # prints 10, but x is None
y = double_return(5)      # prints nothing, but y is 10
z = double_return(5) * 3  # 30 — you can keep computing
```

**`print` shows a human. `return` gives a value to the rest of your program.**
A function without `return` returns `None` automatically.

Functions should **compute and return**; let the caller decide whether to print.

## return exits immediately — guard clauses

```python
def grade(marks):
    if marks >= 80:
        return "A"        # leaves the function RIGHT HERE
    if marks >= 60:
        return "B"
    return "F"
```

No `elif` needed — the first `return` that fires ends everything. `return` gives
you mutual exclusivity for free, and flattens the nesting from Module 4:

```python
def report(name, marks):
    if not name:
        return "Error: name required"     # bail out early
    ...                                   # rest stays unindented
```

## Default and keyword arguments

```python
def power(base, exp=2):        # exp defaults to 2
    return base ** exp

power(5)                       # 25  — uses default
power(5, 3)                    # 125 — overrides positionally
power(exp=3, base=5)           # 125 — keyword args, order irrelevant
```

Parameters with defaults must come **after** ones without.

## The mutable default trap

```python
def add_item(item, cart=[]):      # THE BUG
    cart.append(item)
    return cart

add_item('apple')     # ['apple']
add_item('milk')      # ['apple', 'milk']   <- same list, still there
add_item('bread')     # ['apple', 'milk', 'bread']
```

A default is created **once, when the function is defined** — not fresh per call.
One list gets shared by every caller forever. The fix:

```python
def add_item(item, cart=None):
    if cart is None:
        cart = []       # a fresh list, every single call
    cart.append(item)
    return cart
```

`None` is safe as a default precisely because it is **immutable**.
**Never put a `list`, `dict`, or `set` in a default.**

## *args and **kwargs

```python
def total(*numbers):           # collects positional args into a TUPLE
    return sum(numbers)

total(1, 2, 3)                 # 6
total()                        # 0 — sum of an empty tuple

def show(**details):           # collects keyword args into a DICT
    print(details)

show(name="Sam", age=20)       # {'name': 'Sam', 'age': 20}
```

The `*` and `**` are what matter; `args`/`kwargs` are conventional names.

## Scope — local vs global

```python
total = 100                # global

def spend():
    total = 50             # creates a NEW LOCAL variable
    print(total)           # 50

spend()
print(total)               # 100 — the global was never touched
```

There is no "priority" contest. `total = 50` inside creates a **brand-new,
separate variable that happens to share the name**. Two variables, two lifetimes;
the local dies when the function returns.

To *reassign* a global you need `global total` — but needing `global` almost
always means the design is wrong. **Pass values in as parameters, hand results
back with `return`.**

## Docstrings

```python
def bmi(weight, height):
    """Return BMI from weight in kg and height in metres."""
    return weight / height ** 2
```

Triple-quoted string as the **first** line of the body. `help(bmi)` shows it.

## Give values a name when you need them twice

```python
print(f"You are: {bmi_category(calculate_bmi(weight, height))}")   # BMI thrown away
```

Nesting calls is fine when the intermediate is genuinely disposable. Here it
wasn't — no variable holds the BMI, so printing the number became impossible:

```python
bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi:.1f} ({bmi_category(bmi)})")   # now usable twice
```

---

# Module 7 — Strings

## Indexing — forwards and backwards

```python
s = "Python"
#    012345
#   -654321

s[0]      # 'P'   first
s[-1]     # 'n'   last, the easy way
s[-2]     # 'o'   second from the end
s[10]     # IndexError
```

**Negative indices count from the end**, starting at `-1`. `s[-1]` needs no
length calculation, so there is no off-by-one to get wrong.

## Slicing — [start:stop:step]

```python
s = "Python"

s[0:3]     # 'Pyt'    start at 0, STOP BEFORE 3
s[2:]      # 'thon'   from 2 to the end
s[:4]      # 'Pyth'   from start to before 4
s[::2]     # 'Pto'    every 2nd character
s[::-1]    # 'nohtyP' REVERSED — negative step
s[-3:]     # 'hon'    last three
```

**The stop is always excluded** — same rule as `range()`. Unlike indexing,
slicing **never raises IndexError**: `s[0:100]` just gives what's there.

`s[::-1]` is the standard Python reverse.

## Strings are immutable

```python
s = "hello"
s.upper()            # returns 'HELLO'
print(s)             # still 'hello' — s never changed
s = s.upper()        # you must REASSIGN
```

Every "modifying" method returns a **new string**. Forgetting the reassignment
is the #1 string bug. `s[0] = "H"` tries to mutate the existing object and raises
`TypeError`; `s = "H" + s[1:]` builds a new object and moves the label.

## The methods worth knowing

```python
s.upper()  s.lower()  s.title()        # case
s.strip()                              # remove whitespace from both ends
s.replace("a", "b")                    # swap all occurrences
s.split(",")                           # string -> LIST
",".join(["a","b","c"])                # list -> string: 'a,b,c'
s.find("th")                           # index of first match, -1 if absent
s.count("o")                           # how many times
s.startswith("Py")  s.endswith("on")   # bool
s.isdigit()  s.isalpha()  s.isspace()  # bool — validation
len(s)                                 # length
```

`.find()` returns `-1` rather than raising — and `-1` is a valid index, so
`if s.find(x):` is a bug. Write `if s.find(x) != -1:`.

`split()` with **no argument** splits on any whitespace run and discards empties,
so `''.join(text.lower().split())` strips tabs and double spaces too —
better than `text.replace(" ", "")`.

## Iterating and membership

```python
for char in "hello":
    print(char)

if "th" in "Python":      # substring check — True
```

## f-strings

```python
name, score = "Sam", 87.6543

f"{score:.2f}"      # 87.65      2 decimals
f"{score:>10}"      # right-align in 10 columns
f"{name:<10}|"      # left-align
f"{name:^10}|"      # centre
f"{score:.1%}"      # percentage
f"{name.upper()}"   # method calls work inside
f"{{literal}}"      # escape a brace by doubling
```

## Escape sequences

```python
"\n"    newline        "\t"    tab
"\\"    backslash      "\""    quote
r"C:\Users\new"        raw string — backslashes stay literal
```

Matters on Windows: `"C:\Users\new"` contains a newline where `\n` is.
Use `r"..."` for paths.

---

# Module 8 — Lists & Dictionaries

Your syllabus says "arrays" — in Python that means **lists**.

## Lists: creation and access

```python
nums  = [10, 20, 30, 40]
mixed = [1, "two", 3.0, True]      # types can mix
empty = []

nums[0]       # 10
nums[-1]      # 40
nums[1:3]     # [20, 30]  — slicing works exactly like strings
len(nums)     # 4
```

## Lists are mutable — the difference from strings

```python
nums[0] = 99          # works; strings would raise TypeError
```

Which brings back the aliasing trap:

```python
a = [1, 2, 3]
b = a                 # SAME list
b.append(4)
print(a)              # [1, 2, 3, 4]

c = a.copy()          # or a[:] or list(a) — a NEW list
c.append(5)
print(a)              # unchanged
```

**`=` never copies a list. Use `.copy()` when you want independence.**

## List methods

```python
nums.append(50)          # add ONE item to the end
nums.extend([60, 70])    # add MANY items
nums.insert(0, 5)        # insert at index
nums.remove(30)          # remove first matching VALUE (ValueError if absent)
nums.pop()               # remove and RETURN last
nums.pop(0)              # remove and return by INDEX
nums.sort()              # sorts IN PLACE, returns None
nums.reverse()           # in place
nums.index(20)           # position of a value
nums.count(20)           # occurrences
nums.clear()             # empty it
```

Two traps:
- `nums.append([1,2])` adds a **list as one item**; `extend` adds the elements
- **`nums.sort()` returns `None`** — `x = nums.sort()` gives `None`.
  Use `sorted(nums)` when you want a new sorted list back

## Iteration and enumerate

```python
for n in nums:                          # values
    print(n)

for i, n in enumerate(nums):            # index AND value
    print(f"{i}: {n}")

for i, n in enumerate(nums, start=1):   # numbering from 1
```

`enumerate` is the right answer whenever you catch yourself writing
`for i in range(len(nums))`.

## List comprehension

```python
squares = [n ** 2 for n in range(1, 6)]              # [1, 4, 9, 16, 25]
evens   = [n for n in nums if n % 2 == 0]            # with a filter
upper   = [w.upper() for w in words]
```

Reads as: *"give me EXPRESSION for each ITEM in SEQUENCE, optionally if CONDITION."*
It replaces the three-line append loop. Keep them to one line and one condition —
beyond that, use a real loop.

## Nested lists

```python
grid = [[1, 2, 3],
        [4, 5, 6]]

grid[0]        # [1, 2, 3]
grid[1][2]     # 6      row 1, column 2

for row in grid:
    for value in row:
        print(value)
```

## Dictionaries: key-value pairs

```python
student = {"name": "Priya", "age": 20, "marks": 82}

student["name"]                # 'Priya'
student["grade"]               # KeyError — key doesn't exist
student.get("grade")           # None — safe, no crash
student.get("grade", "N/A")    # 'N/A' — with a fallback
```

**Use `.get()` whenever the key might be missing.** Lists are indexed by
*position*; dicts by *key* — a name you choose.

Keys must be **immutable** (`str`, `int`, `tuple` — never a list).
Values can be anything.

## Modifying

```python
student["age"] = 21            # update
student["city"] = "Pune"       # add — same syntax
del student["city"]            # delete
student.pop("age")             # delete and return
"name" in student              # True — checks KEYS, not values
```

## Iteration

```python
for key in student:                       # keys by default
for key in student.keys():
for value in student.values():
for key, value in student.items():        # BOTH — the one you'll use most
    print(f"{key}: {value}")
```

## Nesting — how real data looks

```python
students = {
    "priya": {"marks": 82, "grade": "A"},
    "sam":   {"marks": 55, "grade": "C"},
}

students["priya"]["marks"]         # 82

for name, info in students.items():
    print(f"{name}: {info['marks']}")
```

Note the **single quotes** inside the f-string's braces — you can't reuse double quotes there.

## When to use which

- **List** — ordered, accessed by position, order matters, duplicates fine
- **Dict** — looked up by a meaningful name, keys unique, lookup instant regardless of size

If you're searching a list to find "the student named Priya," you want a dict.

---

# Module 9 — Recursion

## What it is

A function that **calls itself**. That's the whole mechanic. The skill is knowing
how to make it stop.

```python
def countdown(n):
    if n == 0:            # BASE CASE — stops the recursion
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)      # RECURSIVE CASE — a SMALLER problem
```

## Every recursive function needs exactly two things

1. **A base case** — a condition that returns *without* calling itself
2. **A recursive case** — calls itself with input that moves **closer to the base case**

Miss the base case, or fail to shrink the input, and you get
`RecursionError: maximum recursion depth exceeded`. That's recursion's version of
the infinite loop — the same bug as Module 5's missing update, wearing a different hat.

Python caps recursion at roughly 1000 frames deep. That's a safety net, not a feature.

## The call stack

```python
def factorial(n):
    if n <= 1:            # base case
        return 1
    return n * factorial(n - 1)
```

`factorial(4)` unwinds like this — **nothing multiplies until the base case is hit**:

```
factorial(4) -> 4 * factorial(3)          <- paused, waiting
  factorial(3) -> 3 * factorial(2)        <- paused, waiting
    factorial(2) -> 2 * factorial(1)      <- paused, waiting
      factorial(1) -> 1                   <- BASE CASE, returns
    factorial(2) -> 2 * 1 = 2             <- resumes
  factorial(3) -> 3 * 2 = 6               <- resumes
factorial(4) -> 4 * 6 = 24                <- resumes
```

Each call is **paused mid-expression**, stacked up, then unwound in reverse.
That stack is real memory, which is why deep recursion is expensive.

## The mental trick — trust the recursion

Don't trace all four levels in your head. Assume the recursive call **already
works**, then ask only: *"given that, what do I do with its answer?"*

For factorial: *"If `factorial(3)` correctly gives me 6, what do I do?"*
Multiply by `n`. Done.

That leap — trusting a function you haven't finished writing — is what makes
recursion click.

## Recursion vs loops

Anything recursive can be written as a loop, and loops are usually **faster and
safer** in Python (no stack limit, no frame overhead).

```python
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

**Use recursion when the problem is naturally self-similar** — a folder
containing folders, a tree, nested menus, divide-and-conquer sorting.
Use a loop for simple counting.

## Fibonacci — the classic warning

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Correct, elegant, and **catastrophically slow**. `fib(35)` makes about 30 million
calls, because `fib(30)` gets recomputed thousands of times. Two branches per
call means exponential growth — unlike `factorial`, which has one branch and is linear.

Fix with **memoisation** — cache what you've already computed:

```python
from functools import lru_cache

@lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Same function, one decorator, 30 million calls become 36.

## Recursion on lists and strings

```python
def total(items):
    if not items:                        # base case: empty list
        return 0
    return items[0] + total(items[1:])   # first + rest

def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]         # rest reversed, first at the end
```

The pattern is always **"handle the first element, recurse on the remainder."**

---

# PENDING WORK — do this at home

## Part 1 — Theory questions (Modules 8 + 9)

Answer in your own words, numbered, no lookups.

### Verification (from your Round 7 `sentance.py` — you used these before they were taught)

1. `max(words, key=len)` — what does `key=len` do? On `"cat bat hat"`, which word
   is returned and why?
2. `word[::-1] for word in words` inside `join()` — what is that construct called,
   and what does `join()` actually receive?
3. `return a, b, c` then `x, y, z = f()` — what type is actually returned, and
   what is that assignment called?

### Lists & Dictionaries

4. `append` vs `extend` — predict both:
   ```python
   a = [1, 2]; a.append([3, 4]); print(a)
   b = [1, 2]; b.extend([3, 4]); print(b)
   ```
5. Why is `x = nums.sort()` equal to `None`? What do you use instead?
6. Predict, and say how to make `b` independent:
   ```python
   a = [1, 2, 3]
   b = a
   b.append(4)
   print(a)
   ```
7. `student["grade"]` vs `student.get("grade")` when the key is missing?
8. Rewrite as a list comprehension:
   ```python
   result = []
   for n in range(1, 11):
       if n % 2 == 0:
           result.append(n * n)
   ```
9. What does `.items()` give you, and why is it better than looping keys and
   doing `d[key]`?
10. Why can a `tuple` be a dict key but a `list` cannot?

### Recursion

11. What are the two mandatory parts of any recursive function? What happens if
    the base case is missing?
12. Trace `factorial(4)` — show the unwinding, and say why nothing multiplies
    until the base case is reached.
13. Why is naive `fib(35)` so slow when `factorial(35)` is instant? Both are recursive.
14. When would you choose recursion over a loop? Give one concrete example where
    recursion is genuinely the better fit.
15. What's wrong here, and what does Python raise?
    ```python
    def countdown(n):
        print(n)
        countdown(n - 1)
    ```

---

## Part 2 — Coding problems

### Round 8 — Lists & Dictionaries

**A. `gradebook.py`**

Build a gradebook from this data:

```python
students = {
    "priya": [82, 91, 78],
    "sam":   [55, 62, 48],
    "ravi":  [95, 88, 100],
    "ali":   [30, 45, 38],
}
```

Write functions that **return** (never print):

- `average(marks)` — average of a list of marks
- `topper(students)` — name of the student with the highest average
- `passed(students)` — a **list** of names whose average is 40 or above

Then print a report:

```
priya: avg 83.7  PASS
sam:   avg 55.0  PASS
ravi:  avg 94.3  PASS
ali:   avg 37.7  FAIL

Topper: ravi
Passed: 3 of 4
```

Use `.items()` for the loop, and a **list comprehension** for `passed`.

**B. `wordcount.py`**

Given a sentence, count how many times each word appears — case-insensitive —
and print them from most frequent to least.

```
"the cat and the dog and the bird"
->
the: 3
and: 2
cat: 1
dog: 1
bird: 1
```

Hints: build a dict with `.get(word, 0) + 1`, then sort with
`sorted(counts.items(), key=lambda pair: pair[1], reverse=True)`.
(`lambda` is new — it's just an inline one-expression function. Look at what it
receives: each `pair` is a `(word, count)` tuple, and `pair[1]` is the count.)

### Round 9 — Recursion

**C. `recursion_basics.py`**

Write all four **recursively** — no loops anywhere:

- `factorial(n)` — 5 -> 120
- `sum_digits(n)` — 472 -> 13 (your Round 3 problem, now recursive and for any length)
- `reverse_string(s)` — "hello" -> "olleh"
- `count_down(n)` — prints n, n-1, ... 1, then "Liftoff!"

Each needs an explicit base case. Test `factorial(0)` — it should be `1`, not a crash.

**D. `fib_compare.py`**

Write `fib_slow(n)` (naive recursion) and `fib_fast(n)` (with `@lru_cache`).
Time both on `n = 32` and print the difference:

```python
import time
start = time.time()
fib_slow(32)
print(f"slow: {time.time() - start:.3f}s")
```

Then write `fib_loop(n)` using a `while` loop and time that too.
Tell me which is fastest and why.

---

## Recurring mistakes — check these before submitting

Logic bugs that have actually bitten in this course:

- [ ] **Off-by-one** — `range(1, n + 1)` for "1 through n inclusive"; stop is excluded
- [ ] **Boundary gaps** — for float ranges use one-sided `elif`, never `18.5 <= x <= 24.9`
- [ ] **Unreachable branches** — most specific condition FIRST in an if/elif chain
- [ ] **for/else inverted** — `break` = found it, `else` = searched and found nothing
- [ ] **Accumulator reset** — `total = 0` goes OUTSIDE the loop
- [ ] **Missing update** — every `while` needs initialise, test, update
- [ ] **`sort()` returns None** — use `sorted()` if you want a value back
- [ ] **Aliasing** — `b = a` shares the list; use `a.copy()`
- [ ] **Mutable defaults** — `def f(x=[])` is a bug; use `x=None`
- [ ] **String methods return new strings** — you must reassign
- [ ] **Falsy vs None** — `if score:` skips a legitimate 0
- [ ] **Type vs value** — `10 == 10.0` is True; `==` compares value, `is` compares object
- [ ] **Discarded intermediates** — name a value if you need it twice

And the one habit worth more than all of the above:

- [ ] **Run the file before submitting it.** Round 5's `prime.py` printed nothing
      at all for input 17 and was submitted anyway. Round 5 scored 3/10; the same
      code after one careful pass scored 9/10.
- [ ] **Invent two test cases of your own** — one on a boundary, one weird
      (zero, negative, empty, equal inputs). Every bug found in this course so far
      came from a case that wasn't in the original examples.

---

## Running your code

```powershell
cd "C:\Users\SM 031\AI_Automation_utility\Python_upskilling"
python fizzbuzz.py
```

Note: relative paths like `open("one.csv")` resolve against the **current working
directory**, not the script's folder. Either `cd` into the folder first, or use:

```python
from pathlib import Path
Path(__file__).parent / "one.csv"
```
