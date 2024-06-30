#Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
def extract_digit_words(input_string):
    words = input_string.split()
    digit_words = [word for word in words if word.isdigit()]
    return digit_words

# Example usage:
input_string = "hello 123 world 4567 python 89"
digit_words = extract_digit_words(input_string)
print("Words composed of digits only:", digit_words)
