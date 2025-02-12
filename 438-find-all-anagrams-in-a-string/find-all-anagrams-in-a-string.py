class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_count_p = Counter(p)
        missing = len(char_count_p)
        result = []
        left, right = 0, 0
        k = len(p)

        while right < len(s):
            if right - left == k:
                ch = s[left]
                if ch in char_count_p:
                    char_count_p[ch] += 1
                    if char_count_p[ch] == 1:
                        missing += 1
                left += 1


            ch = s[right]
            if ch in char_count_p:
                char_count_p[ch] -= 1
                if char_count_p[ch] == 0:
                    missing -= 1
                    
            right += 1
    
            if missing == 0:
                result.append(left)

        return result
        