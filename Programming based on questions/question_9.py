""" 
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

# Read input lines
lines = []
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if not line:
        break
    lines.append(line)

# Capitalize and print the lines
for line in lines:
    print(line.upper())
