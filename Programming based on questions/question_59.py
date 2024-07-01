#Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
def convert_to_unicode(ascii_string):
    # Encode the ASCII string to bytes using UTF-8 encoding
    utf8_encoded_bytes = ascii_string.encode('utf-8')
    # Decode the bytes back to a Unicode string
    unicode_string = utf8_encoded_bytes.decode('utf-8')
    return unicode_string

# Example usage:
ascii_string = "hello world"
unicode_string = convert_to_unicode(ascii_string)
print("Unicode string:", unicode_string)
