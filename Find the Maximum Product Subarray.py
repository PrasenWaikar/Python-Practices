def max_product_subarray(arr):
    max_ending_here = min_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        candidates = (num, max_ending_here * num, min_ending_here * num)
        max_ending_here = max(candidates)
        min_ending_here = min(candidates)
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far

arr = [2, 3, -2, 4]
print("Maximum product subarray:", max_product_subarray(arr))
