def count_word_frequency(text):
    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

input_text = "hello world hello python world"
frequency_dict = count_word_frequency(input_text)
print(frequency_dict)
