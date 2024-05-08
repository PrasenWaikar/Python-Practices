"""  
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

"""
def square_dictionary():
    square_dict = {key: key**2 for key in range(1, 4)}
    print(square_dict)

# Example usage
square_dictionary()
