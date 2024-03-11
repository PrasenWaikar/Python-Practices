import random
import string

def guess_the_letter():
    # Generate a random letter
    letter = random.choice(string.ascii_lowercase)
    tries = 0
    max_tries = 5
    guessed_letters = []

    print("I'm thinking of a letter between a and z. Can you guess it? You have 5 tries.")

    while tries < max_tries:
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single letter between a and z.")
            continue

        if guess == letter:
            print(f"Congratulations! You guessed the letter '{letter}' in {tries + 1} tries.")
            break
        else:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            else:
                guessed_letters.append(guess)
                print(f"Sorry, '{guess}' is not the letter. Try again.")
                tries += 1

    if guess != letter:
        print(f"Sorry, you ran out of tries. The letter was '{letter}'.")

# Run the game
guess_the_letter()
