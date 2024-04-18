"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')  
"""
# Accept input from console
input_numbers = input("Enter a sequence of comma-separated numbers: ")

# Split the input into a list of strings
numbers_list = input_numbers.split(',')

# Convert the list of strings into a tuple
numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)
