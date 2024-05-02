"""  
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""

def word_frequency(sentence):
    words = sentence.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[0])
    return sorted_word_freq

# Input
sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

# Calculate word frequency
result = word_frequency(sentence)

# Output
for word, freq in result:
    print(f"{word}:{freq}")
