class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        missing = len(t_count)
        result_index, result_size = -1, len(s)
        left, right = 0, 0

        while right < len(s):
            if missing > 0:
                ch = s[right]
                if ch in t_count:
                    t_count[ch] -= 1
                    if t_count[ch] == 0:
                        missing -= 1
                right += 1
            while missing == 0:
                if right - left <= result_size:
                    result_index, result_size = left, right - left
                ch = s[left]
                if ch in t_count:
                    t_count[ch] += 1
                    if t_count[ch] == 1:
                        missing += 1
                left += 1

        return s[result_index : result_index + result_size] if result_size != -1 else ""
        