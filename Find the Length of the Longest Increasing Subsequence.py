def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    lis = [1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                
    return max(lis)

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Length of longest increasing subsequence:", longest_increasing_subsequence(arr))
