"""  
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
# Accept input sentence
sentence = input("Enter a sentence: ")

# Initialize counts for uppercase and lowercase letters
upper_count = 0
lower_count = 0

# Iterate over each character in the sentence
for char in sentence:
    if char.isupper():  # Check if the character is uppercase
        upper_count += 1
    elif char.islower():  # Check if the character is lowercase
        lower_count += 1

# Print the counts of uppercase and lowercase letters
print("UPPER CASE", upper_count)
print("LOWER CASE", lower_count)
