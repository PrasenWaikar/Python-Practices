def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Input list of numbers
arr = [64, 34, 25, 12, 22, 11, 90]

# Sort the list using bubble sort
sorted_arr = bubble_sort(arr)

# Print the sorted list
print("Sorted array is:", sorted_arr)
