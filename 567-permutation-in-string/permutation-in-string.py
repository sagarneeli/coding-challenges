class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = defaultdict(int)
        for ch in s1:
            s1_map[ch] += 1

        s2_map = defaultdict(int)
        L, k = 0, len(s1)
        
        for R, ch in enumerate(s2):
            s2_map[ch] += 1

            if R - L + 1 == k:
                if s1_map == s2_map:
                    return True
                else:
                    s2_map[s2[L]] -= 1
                    if s2_map[s2[L]] == 0:
                        del s2_map[s2[L]]
                    L += 1
        
        return False

        