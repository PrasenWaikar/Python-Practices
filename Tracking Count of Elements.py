from collections import defaultdict
words = ['apple', 'banana', 'apple', 'orange']
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
