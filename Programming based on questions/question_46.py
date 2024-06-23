#Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
# Given range
numbers = list(range(1, 21))

# Use filter to get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the list of even numbers
print(even_numbers)
