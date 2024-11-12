from collections import Counter
text = "hello world"
freq_dict = Counter(text)
print(freq_dict)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
