import re
from collections import Counter


def find_repeated_words(paragraph):
    """Find repeated words in a paragraph, ignoring extra spaces and special characters."""

    # Normalize text: Convert to lowercase and remove non-alphanumeric characters except spaces
    cleaned_text = re.sub(r"[^\w\s]", "", paragraph.lower())
    # words = re.findall(r"[a-z']+", paragraph.lower())

    # print(cleaned_text)

    # Tokenize words (split by spaces)
    words = cleaned_text.split()

    # Count occurrences of each word
    word_counts = Counter(words)

    # Filter words that appear more than once
    repeated_words = {word: count for word, count in word_counts.items() if count > 1}

    return repeated_words


# Example usage
paragraph = """
Python is great, and Python is powerful! 
However, one must be careful with Python's flexibility words3. 
The best way to learn python's flexibility is to practice   Python.
Can't and    can't are same words3.
"""

result = find_repeated_words(paragraph)
print(result)
