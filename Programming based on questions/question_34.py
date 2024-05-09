"""  
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

"""
def print_keys():
    square_dict = {key: key**2 for key in range(1, 21)}
    keys = square_dict.keys()
    for key in keys:
        print(key)

# Example usage
print_keys()
