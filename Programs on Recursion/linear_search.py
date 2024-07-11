def linear_search(arr, index, target):
    # Base case: If the index exceeds the length of the array, return -1 (not found)
    if index >= len(arr):
        return -1
    
    # If the target is found at the current index, return the index
    if arr[index] == target:
        return index
    
    # Recursively call the function with the next index
    return linear_search(arr, index + 1, target)

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10

# Perform linear search starting from index 0
result = linear_search(arr, 0, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
