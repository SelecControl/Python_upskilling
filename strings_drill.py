# Bonus Round 7B — String Slicing & Methods
# Questions: PRACTICE_strings.md
#
# Rule: write your prediction in the comment BEFORE you run this file.


# ---------------------------------------------------------------- Part A
s = "Programming"

# 1  s[3:7]        ->
print(repr(s[3:7]))
# 2  s[:5]         ->
print(repr(s[:5]))
# 3  s[7:]         ->
print(repr(s[7:]))
# 4  s[-4:]        ->
print(repr(s[-4:]))
# 5  s[:-4]        ->
print(repr(s[:-4])) # -4 is not included, so it will return everything up to the 4th character from the end
# 6  s[::3]        ->
print(repr(s[::3]))
# 7  s[::-1]       ->
print(repr(s[::-1])) 
# 8  s[::-2]       ->
print(repr(s[::-2]))
# 9  s[7:3]        ->
print(repr(s[7:3]))
# 10 s[7:3:-1]     ->
print(repr(s[7:3:-1]))
# 11 s[-1:-5:-1]   ->
print(repr(s[-1:-5:-1]))
# 12 s[2:100]      ->
print(repr(s[2:100]))
# 13 s[100:]       ->
print(repr(s[100:]))
# 14 s[-100:3]     ->
print(repr(s[-100:3]))
# 15 s[len(s):]    ->
print(repr(s[len(s):]))
# 16 s[1:8:2]      ->
print(repr(s[1:8:2]))
# 17 s[-6:-2]      ->
print(repr(s[-6:-2]))
# 18 s[::-1][::-1] ->
print(repr(s[::-1][::-1]))

# Uncomment ONE AT A TIME, after you've written the prediction above.
print(repr(s[3:7]))



# ---------------------------------------------------------------- Part B
t = "  hello World  "

# 1  t.strip().title()                 ->
# 2  t.upper()                         ->
# ... continue for all 25

print(repr(t.strip().title()))
print(repr(t.upper()))
print(repr(t.lower()))
print(repr(t.strip()))
print(repr(t.strip().capitalize()))
print(repr(t.strip().swapcase()))
print(repr(t.strip().replace(" ", "")))
print(repr(t.strip().replace(" ", "-")))
print(repr(t.split(",")))
print(repr(t.startswith("  hello")))
print(repr(t.endswith("World  ")))
print(repr(t.find("o")))  
print(repr(t.count("l")))
print(repr(t.isdigit())) # this will return False because the string contains letters and spaces, not just digits
print(repr(t.isalpha())) # this will return False because the string contains spaces and letters, not just letters
print(repr(t.isalnum())) # this will return False because the string contains spaces, not just alphanumeric characters
print(repr(t.isspace())) # this will return False because the string contains letters and spaces, not just whitespace
# ---------------------------------------------------------------- Part C
# C1 what's wrong:
# C1 fix:

# C2 what's wrong:
# C2 fix:

# C3 what's wrong:
# C3 fix:

# C4 what's wrong:
# C4 fix:


# ---------------------------------------------------------------- Part D

def mask_card(number):
    """Mask all but the last 4 digits, preserving spacing."""
    pass


def initials(full_name):
    """'ada lovelace' -> 'A.L.'"""
    pass


def proper_title(text):
    """Title-case without .title()'s apostrophe bug."""
    pass


def chunk(s, n):
    """Cut s into a list of pieces of length n."""
    pass


def is_rotation(a, b):
    """True if b is a rotated by any amount."""
    pass


# ---------------------------------------------------------------- your tests
if __name__ == "__main__":
    print(mask_card("4539 1488 0343 6467"))
    print(mask_card("4539148803436467"))
    print(initials("  grace   brewster hopper  "))
    print(proper_title("it's a dog's life"))
    print(chunk("Programming", 3))
    print(chunk("", 3))
    print(is_rotation("python", "thonpy"))
    # add two of your own: one boundary, one weird
