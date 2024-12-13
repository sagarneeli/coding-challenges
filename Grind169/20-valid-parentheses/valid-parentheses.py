class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        # stack - ["("]
        for ch in s:
            if ch in {"(", "{", "["}:
                stack.append(ch)
                continue
            if not stack or stack[-1] != char_map[ch]:
                return False
            
            stack.pop()

        return not stack
        