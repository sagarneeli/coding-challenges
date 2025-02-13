class Solution:
    def remove_occurrences(self, s: str, part: str) -> str:
        """Removes all occurrences of a substring from a string.

        Time Complexity:
        Each replace operation scans s for the substring part,
        which takes O(n) time in the worst case, where n is the length of s.
        If there are k occurrences of part in s, the overall time complexity is O(n * k).

        Space Complexity:
        The space complexity is O(1) for the in-place modification of the string,
        but since strings are immutable in Python, each replace operation creates a new string.
        Therefore, the space complexity is O(n) due to the storage of intermediate strings.

        ✔ Time Complexity: O(N) instead of O(NM) in naive approaches.
        ✔ No Unnecessary String Copying: Avoids excessive use of replace() or recursion.
        ✔ Memory Efficient: Uses only a stack of size O(N) in the worst case.

        Args:
            s (str): The original string.
            part (str): The substring to remove.

        Returns:
            str: The string with all occurrences of the substring removed.
        """
        stack = []

        for ch in s:
            stack.append(ch)

            if len(stack) >= len(part):
                if "".join(stack[-len(part) :]) == part:
                    for _ in range(len(part)):
                        stack.pop()

        return "".join(stack)


solution = Solution()

print(solution.remove_occurrences("daabcbaabcbc", "abc"))
