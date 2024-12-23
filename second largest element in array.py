def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

arr = [12, 35, 1, 10, 34, 1]
print("Second largest element:", second_largest(arr))
