from typing import List
from collections import defaultdict

"""
Complexity Analysis
Time Complexity: 
O(N*K), where N is the length of strs, and K is the maximum length of a string in strs. 
Counting each string is linear in the size of the string, and we count every string.

Space Complexity: O(N*K), the total information content stored in ans.
"""


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """Groups anagrams together from a list of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            List[List[str]]: A list of lists, where each inner list contains anagrams.
        """
        mapping = defaultdict(list)

        for string in strs:
            char_count = [0] * 26
            for ch in string:
                char_count[ord(ch) - ord("a")] += 1
            mapping[tuple(char_count)].append(string)

        return list(mapping.values())


input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Expected Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

solution = Solution()
print(solution.group_anagrams(input_strings))
