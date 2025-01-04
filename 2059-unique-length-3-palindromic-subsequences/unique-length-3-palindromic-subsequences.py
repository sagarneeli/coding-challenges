class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        left = set()
        right = Counter(s)

        for m in s:
            right[m] -= 1
            for ch in left:
                if right[ch] > 0:
                    result.add((m, ch))
            left.add(m)

        return len(result)
        