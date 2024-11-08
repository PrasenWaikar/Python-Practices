def is_subsequence(arr1, arr2):
    it = iter(arr2)
    return all(elem in it for elem in arr1)

arr1 = [1, 3, 5]
arr2 = [1, 2, 3, 4, 5]
print("Is arr1 a subsequence of arr2?", is_subsequence(arr1, arr2))
