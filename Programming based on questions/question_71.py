#Please write a program which accepts a string from console and print the characters that have even indexes.
# Accept a string from the console
input_string = input("Enter a string: ")

# Print characters that have even indexes
even_index_characters = input_string[::2]
print("Characters with even indexes:", even_index_characters)
