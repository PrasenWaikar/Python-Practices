def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        index = abs(arr[i]) - 1
        if arr[index] < 0:
            duplicates.append(index + 1)
        else:
            arr[index] = -arr[index]
    
    return duplicates

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print("Duplicates:", find_duplicates(arr))
