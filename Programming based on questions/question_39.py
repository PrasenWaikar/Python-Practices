# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
def generate_and_print_squares_tuple():
    # Generate a tuple of squares of numbers from 1 to 20
    squares_tuple = tuple(x**2 for x in range(1, 21))
    
    # Print the tuple
    print(squares_tuple)

# Call the function
generate_and_print_squares_tuple()
