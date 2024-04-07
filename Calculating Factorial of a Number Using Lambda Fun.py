import functools
factorial = lambda n: functools.reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(5))  # Output: 120
