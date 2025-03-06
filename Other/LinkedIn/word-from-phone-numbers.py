"""
Part 1

Given the standard mapping from English letters to digits on a phone keypad
(1 → "", 2 → a,b,c, 3 → d,e,f, 4 → g,h,i, 5 → j,k,l, 6 → m,n,o, 7 → p,q,r,s, 8 → t,u,v, 9 → w,x,y,z),

Write a program that outputs all words that can be formed from any n-digit phone number
from the list of given KNOWN_WORDS considering the mapping mentioned above.

KNOWN_WORDS = ['careers', 'linkedin', 'hiring', 'interview', 'linkedgo']

phoneNumber: 2273377
Output: ['careers']

phoneNumber: 54653346
Output: ['linkedin', 'linkedgo']

Part 2
Adjust implementation for use case when new words can be added
and existing words can be removed from the dictionary at runtime.

"""

from collections import defaultdict
import threading
from typing import List, Dict, Set


class WordFinderFromPhoneNumber:
    """
    Finds words from a phone number based on keypad mappings.
    """

    # KEYBOARD = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    KEYBOARD = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    KNOWN_WORDS = [
        "careers",
        "linkedin",
        "hiring",
        "interview",
        "linkedgo",
    ]  # Given known words

    @staticmethod
    def words_from_phone_number(phone_number: str) -> List[str]:
        def generate_combinations(curr, index):
            """Recursive function to generate possible word combinations."""
            if index == len(curr):
                if curr in WordFinderFromPhoneNumber.KNOWN_WORDS:
                    valid_words.add(curr)
                return

            digit = phone_number[index]
            for char in WordFinderFromPhoneNumber.KEYBOARD.get(digit, ""):
                generate_combinations(curr + char, index + 1)

        valid_words = set()
        generate_combinations("", 0)
        return list(valid_words)


# print(WordFinderFromPhoneNumber.words_from_phone_number("2273377"))


class WordFinderFromPhoneNumber:
    """
    Finds words from a phone number based on keypad mappings.
    """

    DIGIT_TO_LETTERS: Dict[str, str] = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def __init__(self, words: List[str]) -> None:
        self.lock = threading.Lock()
        self.letter_to_digit_mapping: Dict[str, str] = {
            char: digit
            for digit, letters in self.DIGIT_TO_LETTERS.items()
            for char in letters
        }
        self.known_words: Set[str] = set(words)
        self.dictionary_to_phone_numbers: Dict[str, Set[str]] = (
            self.build_word_to_phone_number_mapping()
        )

    def word_to_number(self, word: str) -> str:
        """Converts a word into a phone number string."""
        return "".join(self.letter_to_digit_mapping.get(char, "") for char in word)

    def build_word_to_phone_number_mapping(self) -> Dict[str, Set[str]]:
        """Builds a dictionary mapping phone numbers to words."""
        mapping: Dict[str, Set[str]] = defaultdict(set)
        for word in self.known_words:
            phone_number = self.word_to_number(word)
            mapping[phone_number].add(word)
        return mapping

    def words_from_phone_number(self, phone_number: str) -> List[str]:
        """Returns words matching the phone number."""
        print(self.letter_to_digit_mapping)
        with self.lock:
            return list(self.dictionary_to_phone_numbers.get(phone_number, []))


# Example usage
KNOWN_WORDS: List[str] = ["careers", "linkedin", "hiring", "interview", "linkedgo"]
word_finder = WordFinderFromPhoneNumber(KNOWN_WORDS)

print(word_finder.words_from_phone_number("2273377"))  # Output: ['careers']
print(
    word_finder.words_from_phone_number("54653346")
)  # Output: ['linkedin', 'linkedgo']
