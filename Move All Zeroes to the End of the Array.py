def move_zeroes(arr):
    non_zeroes = [num for num in arr if num != 0]
    zeroes = [0] * (len(arr) - len(non_zeroes))
    return non_zeroes + zeroes

arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
print("Array after moving zeroes:", move_zeroes(arr))
