import math

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs_val = float("inf")
        num_negatives = 0
        total_abs_sum = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                num = matrix[r][c]
                if num < 0:
                    num_negatives += 1
                total_abs_sum += abs(num)
                min_abs_val = min(min_abs_val, abs(num))
        
        if num_negatives % 2 == 0:
            return total_abs_sum
        
        return total_abs_sum - (2 * min_abs_val)

        