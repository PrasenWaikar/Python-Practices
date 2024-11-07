def min_difference(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i - 1])
    return min_diff

arr = [1, 5, 3, 19, 18, 25]
print("Minimum difference:", min_difference(arr))
