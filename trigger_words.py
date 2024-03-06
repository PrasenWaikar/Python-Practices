def check_trigger_word(input_text, trigger_word):
    return trigger_word.lower() in input_text.lower()

trigger_word = "hello"
user_input = input("Enter a sentence: ")

if check_trigger_word(user_input, trigger_word):
    print(f"Trigger word '{trigger_word}' found in input!")
else:
    print(f"Trigger word '{trigger_word}' not found in input.")
