"""  
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

"""
def print_square_values():
    square_dict = {key: key**2 for key in range(1, 21)}
    values = square_dict.values()
    for value in values:
        print(value)

# Example usage
print_square_values()
