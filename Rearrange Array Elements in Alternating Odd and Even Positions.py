def rearrange_odd_even(arr):
    odd = [x for x in arr if x % 2 != 0]
    even = [x for x in arr if x % 2 == 0]
    result = []

    i = j = 0
    while i < len(odd) or j < len(even):
        if i < len(odd):
            result.append(odd[i])
            i += 1
        if j < len(even):
            result.append(even[j])
            j += 1

    return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Rearranged array (odd/even):", rearrange_odd_even(arr))
