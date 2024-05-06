"""  
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

"""
def print_longest_string(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        print(str1)
    elif len2 > len1:
        print(str2)
    else:
        print(str1)
        print(str2)

# Example usage
string1 = "Python"
string2 = "Java"
print_longest_string(string1, string2)

string3 = "Hello"
string4 = "World"
print_longest_string(string3, string4)

string5 = "Python"
string6 = "Java"
print_longest_string(string5, string6)
