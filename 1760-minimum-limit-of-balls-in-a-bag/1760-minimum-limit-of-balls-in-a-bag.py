class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_divide(max_balls_in_bag):
            ops = 0
            for n in nums:
                ops += ceil(n / max_balls_in_bag) - 1
                if ops > maxOperations:
                    return False
            return True
                
        left = 1
        right = max(nums)
        while left < right:
            middle = (left + right) // 2
            if can_divide(middle):
                right = middle
            else:
                left = middle + 1

        return left
        