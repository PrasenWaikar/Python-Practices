def count_letters(word):
    word = word.lower().replace(" ", "")
    letter_count = {}
    for letter in word:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

# Test the function
print(count_letters("Hello, World!"))
