class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def backtrack(curr_sum, i):
            if curr_sum == n:
                return True

            if curr_sum > n or 3 ** i > n:
                return False
            
            include = backtrack(curr_sum + 3 ** i, i + 1)
            exclude = backtrack(curr_sum, i + 1)

            return include or exclude

        return backtrack(0, 0)
        