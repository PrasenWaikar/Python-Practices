def longest_palindromic_subarray(arr):
    def is_palindrome(subarr):
        return subarr == subarr[::-1]

    n = len(arr)
    max_len = 1
    start = 0
    
    for i in range(n):
        for j in range(i, n):
            subarr = arr[i:j + 1]
            if is_palindrome(subarr) and len(subarr) > max_len:
                start = i
                max_len = len(subarr)
                
    return arr[start:start + max_len]

arr = [1, 2, 3, 4, 3, 2, 1, 5, 6]
print("Longest palindromic subarray:", longest_palindromic_subarray(arr))
