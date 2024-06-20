# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
def print_tuple_halves():
    # Given tuple
    given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
    # Calculate the midpoint
    midpoint = len(given_tuple) // 2
    
    # Print the first half values
    print(given_tuple[:midpoint])
    
    # Print the last half values
    print(given_tuple[midpoint:])

# Call the function
print_tuple_halves()
