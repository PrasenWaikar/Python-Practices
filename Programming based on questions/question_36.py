"""  
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
"""

def print_first_five_squares():
    square_list = [i**2 for i in range(1, 21)]
    first_five = square_list[:5]
    print(first_five)

# Example usage
print_first_five_squares()
