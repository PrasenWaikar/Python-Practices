def can_partition(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False

    half_sum = total_sum // 2
    dp = [False] * (half_sum + 1)
    dp[0] = True

    for num in arr:
        for j in range(half_sum, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[half_sum]

arr = [1, 5, 11, 5]
print("Can partition array into two with equal sums?", can_partition(arr))
