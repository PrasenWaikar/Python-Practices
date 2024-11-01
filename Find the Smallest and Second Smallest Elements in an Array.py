def smallest_and_second_smallest(arr):
    if len(arr) < 2:
        return None, None

    first = second = float('inf')
    
    for num in arr:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
            
    return first, second

arr = [12, 13, 1, 10, 34, 1]
print("Smallest and second smallest elements:", smallest_and_second_smallest(arr))
