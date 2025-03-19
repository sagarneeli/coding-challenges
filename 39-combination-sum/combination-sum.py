class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(target, i, stack):
            if target < 0 or i >= len(candidates):
                return
            
            if target == 0:
                result.append(list(stack))
                return

            stack.append(candidates[i])
            backtrack(target - candidates[i], i, stack)
            stack.pop()

            backtrack(target, i + 1, stack)

        result = []
        backtrack(target, 0, [])
        return result