class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, comb):
            if i > n:
                if len(comb) == k:
                    result.append(list(comb))
                return

            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()

            backtrack(i + 1, comb)

        result = []
        backtrack(1, [])
        return result

        