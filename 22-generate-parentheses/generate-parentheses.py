class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open_n, close_n):
            if open_n == n and close_n == n:
                result.append("".join(stack))
                return
            
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, close_n)
                stack.pop()
            
            if close_n < open_n:
                stack.append(")")
                backtrack(open_n, close_n + 1)
                stack.pop()

        backtrack(0, 0)
        return result
        