class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        dict_t = Counter(t)
        missing = len(dict_t)
        left, right = 0, 0
        result_index, result_size = -1, len(s)

        while right < len(s):
            if missing > 0:
                ch = s[right]
                if ch in dict_t:
                    dict_t[ch] -= 1
                    if dict_t[ch] == 0:
                        missing -= 1
                right += 1
            while missing == 0:
                if right - left <= result_size:
                    result_index, result_size = left, right - left
                ch = s[left]
                if ch in dict_t:
                    dict_t[ch] += 1
                    if dict_t[ch] == 1:
                        missing += 1
                left += 1
        print(result_index, result_size)
        return s[result_index: result_size + result_index] if result_index != -1 else ""
        