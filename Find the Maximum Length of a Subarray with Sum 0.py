def max_len_subarray_zero_sum(arr):
    sum_map = {}
    max_len = 0
    current_sum = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum == 0:
            max_len = i + 1
        if current_sum in sum_map:
            max_len = max(max_len, i - sum_map[current_sum])
        else:
            sum_map[current_sum] = i
            
    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print("Max length of subarray with sum 0:", max_len_subarray_zero_sum(arr))
