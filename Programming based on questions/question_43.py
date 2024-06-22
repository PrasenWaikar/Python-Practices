#Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
# Given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Use filter function to get even numbers
even_numbers = list(filter(is_even, numbers))

# Print the list of even numbers
print(even_numbers)
