a, b, c = 5, 5, 5
result = "Equilateral" if a == b == c else "Isosceles" if a == b or b == c or a == c else "Scalene"
print(result)  # Output: Equilateral
