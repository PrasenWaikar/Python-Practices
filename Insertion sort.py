def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
arr = [10, 5, 13, 8, 2]
print("Unsorted array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
