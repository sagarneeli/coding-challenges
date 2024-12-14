class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = [0] * 26

        for ch in s:
            char_count[ord(ch) - ord("a")] += 1
        
        for ch in t:
            char_count[ord(ch) - ord("a")] -= 1
            if char_count[ord(ch) - ord("a")] < 0:
                return False
            
        return True
        