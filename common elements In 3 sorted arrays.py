def find_common_elements(arr1, arr2, arr3):
    # Initialize pointers for arr1, arr2, and arr3
    i, j, k = 0, 0, 0
    
    # List to store common elements
    common_elements = []

    # Traverse through all three arrays until one of them is exhausted
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If the current elements of all arrays are equal, add it to the result
        if arr1[i] == arr2[j] == arr3[k]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # Move the pointer of the smallest element forward
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return common_elements

# Example usage
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = find_common_elements(arr1, arr2, arr3)
print("Common elements:", common)
