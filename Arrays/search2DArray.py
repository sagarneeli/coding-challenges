# Driver Code 

def search2D(matrix, target):
    result = []
    low = 0
    high = len(matrix[0]) - 1

    while low <= len(matrix) and high >= 0:
        if matrix[low][high] < target:
            low += 1
        elif matrix[low][high] > target:
            high -= 1
        else:
            result.append((low, high))
            low += 1
            high -= 1

    return result


mat = [ [10, 20, 29, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48]] 
print(search2D(mat, 29))