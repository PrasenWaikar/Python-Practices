numbers = range(10)
even_squares = {x: x*x for x in numbers if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
