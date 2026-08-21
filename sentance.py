# Given a sentence, print:

# how many words
# the longest word
# the sentence with every word reversed in place (word order kept, letters flipped)

# "Python is really fun"
# → 4 words
# → longest: Python
# → reversed: nohtyP si yllaer nuf
# Use split(), join(), and [::-1]. No loops needed for the reverse if you don't want them — but a loop is fine.

# That's it. Two functions, make them work.

def analyze_sentence(sentence):
    """Analyze the given sentence and return word count, longest word, and reversed words."""
    words = sentence.split()
    word_count = len(words)
    longest_word = max(words, key=len) if words else ""
    reversed_words = ' '.join(word[::-1] for word in words)
    
    return word_count, longest_word, reversed_words

text = input("Enter a sentence: ")
word_count, longest_word, reversed_words = analyze_sentence(text)
print(f"Number of words: {word_count}")
print(f"Longest word: {longest_word}")
print(f"Reversed words: {reversed_words}")