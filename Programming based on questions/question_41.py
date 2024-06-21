#Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
# Given tuple
input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Generate a new tuple with only even numbers
even_tuple = tuple(num for num in input_tuple if num % 2 == 0)

# Print the new tuple
print(even_tuple)
