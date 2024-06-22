#Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
# Given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to square a number
def square(num):
    return num ** 2

# Use map function to get squares of numbers
squared_numbers = list(map(square, numbers))

# Print the list of squared numbers
print(squared_numbers)
