class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = Counter(s1)
        L, R, k = 0, 0, len(s1)
        missing = len(s1_map)
        
        while R < len(s2):
            ch = s2[R]
            if ch in s1_map:
                s1_map[ch] -= 1
                if s1_map[ch] == 0:
                    missing -= 1

            if R - L == k:
                ch = s2[L]
                if ch in s1_map:
                    s1_map[ch] += 1
                    if s1_map[ch] == 1:
                        missing += 1
                L += 1
                          
            R += 1

            if missing == 0:
                return True


        return False

        
        return False

        