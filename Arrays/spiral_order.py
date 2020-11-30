
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Game plan
1. Keep 4 pointers top, bottom, left, right
2. Start from the first row and iterate over the columns, top = 0, left += 1
3. Once you read the end, Keey the column constant and start incrementing the row. left = len(matrix) and top += 1
4. Once you reach the bottom, right -= 1, bottom = len(matrix)
5. Last step - top -= 1, left = 0
- 

"""

def spiralOrder(matrix):
    result = []
    if len(matrix) == 0:
        return []
    
    top = 0
    bottom = 0
    left = 0
    right = 0

    while left <= len(matrix) or right >= 0:
        for i in range(len(matrix)):
            result.append(matrix[top][left])
            left += 1
        top += 1
        isBottom = True
        if isBottom:
            for i in range(len(matrix)):
            result.append(matrix[top][left])
            left += 1


    


