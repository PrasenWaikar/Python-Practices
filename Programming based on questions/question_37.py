# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
def generate_and_print_squares():
    # Generate a list of squares of numbers from 1 to 20
    squares = [x**2 for x in range(1, 21)]
    
    # Print the last 5 elements in the list
    print(squares[-5:])

# Call the function
generate_and_print_squares()
