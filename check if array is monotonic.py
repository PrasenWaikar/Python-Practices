def is_monotonic(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

arr = [6, 5, 4, 4]
print("Is array monotonic?", is_monotonic(arr))
