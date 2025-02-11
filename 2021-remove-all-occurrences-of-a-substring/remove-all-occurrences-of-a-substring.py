class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Time Complexity: Each replace operation scans s for the substring part, which takes O(n) time in the worst case, where n is the length of s. If there are k occurrences of part in s, the overall time complexity is O(n * k).
        Space Complexity: The space complexity is O(1) for the in-place modification of the string, but since strings are immutable in Python, each replace operation creates a new string. Therefore, the space complexity is O(n) due to the storage of intermediate strings.
        """
        while part in s:
            s = s.replace(part, "", 1)

        return s
        