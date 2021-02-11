def merge(arr, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)
        merge(arr, left, right)


def mergeInversion(arr, left, right):
    i = 0
    j = 0
    k = 0
    inversion_count = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            inversion_count += len(left) - i
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return inversion_count

def mergesortInversion(arr):
    inversion_count = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        inversion_count += mergesortInversion(left)
        inversion_count += mergesortInversion(right)
        inversion_count += mergeInversion(arr, left, right)
        return inversion_count
    return inversion_count
        
arr = [54,26,93,17,77,31,44,55,20]
mergesort(arr)
print(arr)

arr = [54,26,93,17,77,31,44,55,20]
arr = [1, 20, 6, 4, 5]
arr = [8, 4, 2, 1]
arr = [3, 1, 2]
print(mergesortInversion(arr))