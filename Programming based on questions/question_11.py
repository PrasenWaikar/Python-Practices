"""  
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
"""
# Accept input sequence of comma separated 4-digit binary numbers
binary_numbers = input("Enter a sequence of comma separated 4-digit binary numbers: ").split(',')

# Initialize an empty list to store divisible numbers
divisible_by_5 = []

# Iterate through the binary numbers
for binary_number in binary_numbers:
    decimal_number = int(binary_number, 2)  # Convert binary to decimal
    if decimal_number % 5 == 0:  # Check if divisible by 5
        divisible_by_5.append(binary_number)

# Join the divisible numbers and print the result
result = ','.join(divisible_by_5)
print(result)
