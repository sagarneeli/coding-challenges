class Solution:
    def clearDigits(self, s: str) -> str:
        """
        cb34
           i

        stack = 
        """
        stack = []

        for ch in s:
            if ch.isdigit():
                if stack:
                    stack.pop()
                else:
                    return ""
            else:
                stack.append(ch)

        return "".join(stack)

        