from typing import List
from collections import defaultdict

"""
Problem: Find Substrings of Size K with K-1 Unique Characters

Given a string s and an integer k, find all substrings of size k that contain
exactly (k-1) unique characters (i.e., exactly one character appears twice).
Return the starting indices of all such substrings.

Time Complexity: O(n) required instead of O(n * k)

Example:
    Input:
        s = "iraceacar"
        k = 5

    Output:
        [1, 4]

    Explanation:
        Valid substrings are:
        - "racea" (starts at index 1)
        - "eacar" (starts at index 4)
        Each substring has length 5 and contains exactly 4 unique characters.
"""


class Solution:
    """Finds substrings of size k with k-1 unique characters."""

    def find_substring(self, s: str, k: int) -> List[int]:
        """Finds the starting indices of substrings of size k with k-1 unique characters.

        Args:
            s (str): The input string.
            k (int): The size of the substring.

        Returns:
            List[int]: A list of starting indices.
        """
        dictionary = defaultdict(int)
        left, right = 0, 0
        result = []

        while right < len(s):
            dictionary[s[right]] += 1

            if right - left == k:
                dictionary[s[left]] -= 1
                if dictionary[s[left]] == 0:
                    del dictionary[s[left]]
                left += 1

            if right - left == k - 1 and len(dictionary) == k - 1:
                result.append(left)

            right += 1

        return result


print(Solution().find_substring("iraceacar", 5))
