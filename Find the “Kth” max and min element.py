def kth_min_max(arr, k):
    arr.sort()  # Sort the array
    kth_min = arr[k-1]  # Kth minimum element
    kth_max = arr[-k]  # Kth maximum element
    return kth_min, kth_max

# Example usage:
arr = [12, 3, 5, 7, 19]
k = 2
kth_min, kth_max = kth_min_max(arr, k)
print(f"The {k}th minimum element is {kth_min}")
print(f"The {k}th maximum element is {kth_max}")
