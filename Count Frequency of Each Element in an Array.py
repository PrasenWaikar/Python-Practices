def count_frequency(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

arr = [10, 20, 20, 10, 10, 20, 5, 20]
print("Frequency of each element:", count_frequency(arr))
