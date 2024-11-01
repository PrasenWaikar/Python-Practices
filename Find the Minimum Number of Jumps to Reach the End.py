def min_jumps(arr):
    if len(arr) <= 1:
        return 0
    if arr[0] == 0:
        return float('inf')

    jumps = 1
    max_reach = arr[0]
    steps = arr[0]

    for i in range(1, len(arr)):
        if i == len(arr) - 1:
            return jumps
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return float('inf')
            steps = max_reach - i

    return jumps

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("Minimum jumps to reach the end:", min_jumps(arr))
