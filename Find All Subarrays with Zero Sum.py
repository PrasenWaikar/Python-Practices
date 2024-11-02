def find_zero_sum_subarrays(arr):
    subarrays = []
    sum_map = {}
    current_sum = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum == 0:
            subarrays.append((0, i))
        if current_sum in sum_map:
            subarrays.extend([(start + 1, i) for start in sum_map[current_sum]])
        sum_map.setdefault(current_sum, []).append(i)
        
    return subarrays

arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print("Subarrays with zero sum:", find_zero_sum_subarrays(arr))
