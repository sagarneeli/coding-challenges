class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(nums) == len(path):
                result.append(path[:])
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack()
                    path.pop()
        
        path = []
        result = []
        backtrack()

        return result
        