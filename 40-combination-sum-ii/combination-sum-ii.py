class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(target, i, path):
            if target == 0:
                result.append(list(path))
                return
            if target < 0 or i == len(candidates):
                return

            path.append(candidates[i])
            backtrack(target - candidates[i], i + 1, path)
            path.pop()
            
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1

            backtrack(target, i, path)

        result = []
        candidates.sort()
        backtrack(target, 0, [])
        return result
        