def find_peak_element(arr):
    n = len(arr)
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]
    return max(arr[0], arr[-1])

arr = [1, 3, 20, 4, 1, 0]
print("Peak element:", find_peak_element(arr))
