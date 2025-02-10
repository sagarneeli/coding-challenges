class Solution:
    def clearDigits(self, s: str) -> str:
        """
        Complexity Analysis
        Let n be the length of the string s.
        
        Time Complexity: O(n).
        Like in the previous approach, we iterate over all characters in s and perform constant-time operations, including checks and retrievals of characters in a string. Additionally, the "resize" operation on the string requires O(n) time and therefore the total time complexity of the algorithm is O(n).

        Space Complexity: O(1).
        As the input string does not count as auxiliary space, the C++ implementation requires only constant extra space for the variables answerLength and charIndex.

        However, the Java and Python implementations require additional structures (such as a list or a charArray), as they do not provide mutable strings. Since these structures are neither part of the input nor the output of the algorithm, they contribute to its auxiliary space complexity, which is O(n).
        """
        stack = []

        for ch in s:
            if ch.isdigit() and stack:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

        