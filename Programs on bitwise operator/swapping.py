def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

x, y = swap(12, 6)
print(x, y)  # Output: 6 12
