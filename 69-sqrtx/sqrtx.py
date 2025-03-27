class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return result
        