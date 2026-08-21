# #
# # Part A — palindrome

# def is_palindrome(text):
#     """Return True if text reads the same forwards and backwards."""
# Must ignore case and spaces, so these are all True:

# "racecar"
# "A man a plan a canal Panama"
# "Was it a car or a cat I saw"
# And "hello" → False.

# Hint: normalise first (lowercase, strip out spaces), then compare against the reverse.#


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards."""
    # Normalize the text: lowercase and remove spaces
    normalized_text = ''.join(text.lower().split())
    # Check if the normalized text is equal to its reverse
    return normalized_text == normalized_text[::-1]

text = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
