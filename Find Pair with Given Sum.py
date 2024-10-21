def pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

arr = [2, 7, 11, 15]
target = 9
print("Pair with sum:", pair_with_sum(arr, target))
