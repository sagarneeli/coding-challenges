class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s = list(s)
        while left <= right:
            if (s[left] in vowels) and (s[right] in vowels):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowels and s[right] in vowels:
                left += 1
            else:
                right -= 1
        return "".join(s)