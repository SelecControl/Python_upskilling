# Bonus Round 7B — String Slicing & Methods

Extra drilling before Modules 8 + 9. Same rules as every round:
**no lookups, no running the code until you've committed an answer in writing.**

Write your answers in `strings_drill.py` as comments, then run it to check
yourself. The point is the gap between what you predicted and what happened —
that gap is the only thing worth studying.

---

## Part A — Slicing: predict the output

```python
s = "Programming"
#    01234567890
#    P r o g r a m m i n g
```

Write the **exact** output, quotes included. `''` is a valid answer.

| #  | Expression        | Your answer |
|----|-------------------|-------------|
| 1  | `s[3:7]`          | |
| 2  | `s[:5]`           | |
| 3  | `s[7:]`           | |
| 4  | `s[-4:]`          | |
| 5  | `s[:-4]`          | |
| 6  | `s[::3]`          | |
| 7  | `s[::-1]`         | |
| 8  | `s[::-2]`         | |
| 9  | `s[7:3]`          | |
| 10 | `s[7:3:-1]`       | |
| 11 | `s[-1:-5:-1]`     | |
| 12 | `s[2:100]`        | |
| 13 | `s[100:]`         | |
| 14 | `s[-100:3]`       | |
| 15 | `s[len(s):]`      | |
| 16 | `s[1:8:2]`        | |
| 17 | `s[-6:-2]`        | |
| 18 | `s[::-1][::-1]`   | |

**After you've answered, explain in one sentence each:**

- A1. Why do 9 and 10 differ, when the numbers are identical?
- A2. Why does 12 not raise `IndexError` when `s[100]` would?
- A3. `s[len(s)]` raises. `s[len(s):]` does not. State the rule that covers both.

---

## Part B — Methods: predict the output

```python
t = "  hello World  "
```

| #  | Expression                          | Your answer |
|----|-------------------------------------|-------------|
| 1  | `t.strip().title()`                 | |
| 2  | `t.upper()`                         | |
| 3  | `"Hello World".swapcase()`          | |
| 4  | `"hello world".capitalize()`        | |
| 5  | `"hello hello".capitalize()`        | |
| 6  | `t.replace("l", "L", 2)`            | |
| 7  | `"a,b,,c".split(",")`               | |
| 8  | `"a b  c".split()`                  | |
| 9  | `"2024-08-23".split("-", 1)`        | |
| 10 | `"-".join("abc")`                   | |
| 11 | `"42".isdigit()`                    | |
| 12 | `"4.2".isdigit()`                   | |
| 13 | `"-42".isdigit()`                   | |
| 14 | `"Hello".find("l")`                 | |
| 15 | `"Hello".find("z")`                 | |
| 16 | `"Hello".rfind("l")`                | |
| 17 | `"Hello".count("l")`                | |
| 18 | `"aaaa".count("aa")`                | |
| 19 | `"Python".startswith(("Py", "Ja"))` | |
| 20 | `" ".isspace()`                     | |
| 21 | `"".isspace()`                      | |
| 22 | `"it's here".title()`               | |
| 23 | `"  x  ".lstrip()`                  | |
| 24 | `"xxhixx".strip("x")`               | |
| 25 | `"banana".strip("ba")`              | |

**Then explain:**

- B1. #4 vs #5 — `capitalize()` does two things, not one. What are they?
- B2. #7 vs #8 — why does one produce an empty string in the list and the other
  doesn't? State the rule for `split()` with an argument vs without.
- B3. #18 — you probably said 3. Say why the real answer is what it is.
- B4. #22 — `.title()` has a genuine bug for English text. Describe it.
- B5. #24 vs #25 — `strip("ba")` does **not** remove the substring `"ba"`.
  What does the argument actually mean? Why does `"banana"` end at `"nan"`?
- B6. `.find()` returns `-1` when absent. `-1` is also a valid index.
  Write the wrong way and the right way to test "is this substring present".

---

## Part C — Fix the bug

Each snippet is broken. Say what's wrong **and** write the fix.

```python
# C1
name = "  ada lovelace  "
name.strip()
name.title()
print(name)          # wanted: "Ada Lovelace"
```

```python
# C2
s = "hello"
s[0] = "H"
print(s)             # wanted: "Hello"
```

```python
# C3
text = "Python is fun"
if text.find("Java"):
    print("found Java")
else:
    print("no Java")
```

```python
# C4  — meant to reverse only the last 4 characters
s = "Programming"
print(s[-4:-1][::-1])   # wanted: "gnim"
```

---

## Part D — Coding problems

Put these in `strings_drill.py`. Every one **returns** a value — no `print()`
inside the functions. Add your own test calls at the bottom.

### D1. `mask_card(number)`

```
"4539 1488 0343 6467"  ->  "**** **** **** 6467"
"4539148803436467"     ->  "************6467"
```

Keep the last 4 digits visible, mask every digit before them, and keep the
original spacing. Must work for any length ≥ 4.

### D2. `initials(full_name)`

```
"ada lovelace"            ->  "A.L."
"  grace   brewster hopper  "  ->  "G.B.H."
```

Handle extra whitespace. Uppercase. Trailing dot included.

### D3. `proper_title(text)`

Fix the `.title()` bug from B4 — do it yourself, without `.title()`.

```
"it's a dog's life"  ->  "It's A Dog's Life"
"hello   world"      ->  "Hello World"
```

### D4. `chunk(s, n)`

Cut a string into pieces of length `n`, returning a **list**. Last piece may be
short. Use slicing, not character-by-character building.

```
chunk("Programming", 3)  ->  ['Pro', 'gra', 'mmi', 'ng']
chunk("abc", 5)          ->  ['abc']
chunk("", 3)             ->  []
```

### D5. `is_rotation(a, b)` — stretch

Return `True` if `b` is `a` rotated by any number of characters.

```
is_rotation("python", "thonpy")  ->  True
is_rotation("python", "typhon")  ->  False
is_rotation("abc", "abcd")       ->  False
```

Solvable in one line with slicing and `in`. Find the one-liner if you can, but a
loop over every rotation is a perfectly good answer.

---

## Before you submit

- [ ] Answers written **before** running anything
- [ ] Every D function `return`s, none of them `print`
- [ ] Tested the empty string `""` on all five
- [ ] Tested `n` larger than the string in D4
- [ ] Ran the file top to bottom with no errors
