class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS * COLS - 1

        while left <= right:
            pivot_index = (left + right) // 2
            pivot_element = matrix[pivot_index // COLS][pivot_index % COLS]
            if pivot_element == target:
                return True
            elif pivot_element < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1
        
        return False
        