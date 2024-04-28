""" 
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
def count_upper_lower(sentence):
    upper_case = 0
    lower_case = 0
    for char in sentence:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
    return upper_case, lower_case

sentence = input("Enter a sentence: ")
upper_case, lower_case = count_upper_lower(sentence)
print("UPPER CASE", upper_case)
print("LOWER CASE", lower_case)
