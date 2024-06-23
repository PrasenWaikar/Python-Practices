# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
# Given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Use map to get squares of even numbers
squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))

# Print the list of squared even numbers
print(squared_even_numbers)
