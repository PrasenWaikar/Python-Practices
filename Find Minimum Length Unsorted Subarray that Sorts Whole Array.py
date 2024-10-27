def find_unsorted_subarray(arr):
    sorted_arr = sorted(arr)
    left, right = 0, len(arr) - 1

    while left < len(arr) and arr[left] == sorted_arr[left]:
        left += 1
    while right > left and arr[right] == sorted_arr[right]:
        right -= 1

    return (left, right) if right > left else (-1, -1)

arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
print("Unsorted subarray indices:", find_unsorted_subarray(arr))
