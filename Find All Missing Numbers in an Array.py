def find_missing_numbers(arr, n):
    full_set = set(range(1, n+1))
    arr_set = set(arr)
    return list(full_set - arr_set)

arr = [4, 3, 2, 7, 8, 2, 3, 1]
n = 8
print("Missing numbers:", find_missing_numbers(arr, n))
