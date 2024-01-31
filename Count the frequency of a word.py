# Program to count the frequency of words in a given text
# Input: "This is a sample text. This text is used for testing purposes."
# Output: {'This': 2, 'is': 2, 'a': 1, 'sample': 1, 'text.': 1, 'used': 1, 'for': 1, 'testing': 1, 'purposes.': 1}

input="This is a sample text. This text is used for testing purposes."
a=input.split()
print((a))
for i in a:
    print(i,a.count(i))
