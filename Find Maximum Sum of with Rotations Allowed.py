def max_sum_with_rotations(arr):
    arr_sum = sum(arr)
    current_val = sum(i * arr[i] for i in range(len(arr)))
    max_val = current_val

    for i in range(1, len(arr)):
        current_val += arr_sum - len(arr) * arr[-i]
        max_val = max(max_val, current_val)
        
    return max_val

arr = [8, 3, 1, 2]
print("Maximum sum with rotations:", max_sum_with_rotations(arr))
