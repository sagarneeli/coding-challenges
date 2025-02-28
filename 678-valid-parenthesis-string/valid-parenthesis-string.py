class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count, close_count = 0, 0
        N = len(s) - 1

        for i in range(N + 1):
            if s[i] in {"(", "*"}:
                open_count += 1
            else:
                open_count -= 1
            
            if s[N - i] in {")", "*"}:
                close_count += 1
            else:
                close_count -= 1
            
            if open_count < 0 or close_count < 0:
                return False

        return True


        