class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        max_prod = nums[0]
        result = nums[0]

        for num in nums[1:]:
            if num < 0:
                min_prod, max_prod = max_prod, min_prod
            
            min_prod = min(num, num * min_prod)
            max_prod = max(num, num * max_prod)

            result = max(result, max_prod)
        
        return result