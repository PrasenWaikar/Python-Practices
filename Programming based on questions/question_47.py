# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
# Given range
numbers = list(range(1, 21))

# Use map to get squares of numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Print the list of squared numbers
print(squared_numbers)
