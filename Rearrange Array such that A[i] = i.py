def rearrange_index(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != -1 and arr[i] != i:
            while arr[i] != -1 and arr[i] != i:
                temp = arr[arr[i]]
                arr[arr[i]] = arr[i]
                arr[i] = temp
    return arr

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print("Rearranged array:", rearrange_index(arr))
