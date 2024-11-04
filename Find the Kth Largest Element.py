import heapq

def find_kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]

arr = [3, 2, 1, 5, 6, 4]
k = 2
print("Kth largest element:", find_kth_largest(arr, k))
