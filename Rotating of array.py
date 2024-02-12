def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # To handle cases where k > n
    return arr[-k:] + arr[:-k]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array(arr, k)
print("Original array:", arr)
print("Rotated array:", rotated_arr)
