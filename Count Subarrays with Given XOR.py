def subarray_xor(arr, target_xor):
    xor_map = {}
    count = 0
    current_xor = 0
    
    for num in arr:
        current_xor ^= num
        if current_xor == target_xor:
            count += 1
        count += xor_map.get(current_xor ^ target_xor, 0)
        xor_map[current_xor] = xor_map.get(current_xor, 0) + 1
    
    return count

arr = [4, 2, 2, 6, 4]
target_xor = 6
print("Count of subarrays with XOR equal to target:", subarray_xor(arr, target_xor))
