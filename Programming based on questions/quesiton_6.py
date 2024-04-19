"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
import math

def calculate_Q(D):
    C = 50
    H = 30
    return int(math.sqrt((2 * C * D) / H))

def main():
    input_sequence = input("Enter a sequence of comma-separated values for D: ")
    values_D = input_sequence.split(',')
    result = [str(calculate_Q(int(D))) for D in values_D]
    print(",".join(result))

if __name__ == "__main__":
    main()
