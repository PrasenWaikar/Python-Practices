def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Array after rotation:", rotate_array(arr, k))
