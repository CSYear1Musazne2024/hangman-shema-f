import random
import string


with open('words.txt', 'r') as file:
    word_list = file.read().split()

def choose_word(word_list):
    """Randomly selects a word from the word list."""
    return random.choice(word_list)

def is_word_guessed(secret_word, letters_guessed):
    """Checks if the secret word is fully guessed."""
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    """Displays the guessed letters and dashes for remaining letters."""
    return ''.join(letter if letter in letters_guessed else '-' for letter in secret_word)

def get_available_letters(letters_guessed):
    """Returns the letters that haven't been guessed yet."""
    return ''.join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)

def hangman():
    secret_word = choose_word(word_list)
    guesses_remaining = 10
    warnings_remaining = 3
    letters_guessed = []

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("You have 3 warnings and 10 guesses.")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 20)
        print(f"Guesses remaining: {guesses_remaining}")
        print(f"Warnings remaining: {warnings_remaining}")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Invalid input. You lose a warning. Warnings left: {warnings_remaining}")
            else:
                guesses_remaining -= 1
                print("Invalid input. You lose a guess.")
            continue

        if guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"You already guessed that letter. Warnings left: {warnings_remaining}")
            else:
                guesses_remaining -= 1
                print("You already guessed that letter. You lose a guess.")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            if guess in 'aeiou':
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

    print("-" * 20)
    if is_word_guessed(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        score = guesses_remaining * unique_letters
        print(f"Congratulations, you won! Your total score is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was: {secret_word}")


if __name__ == "__main__":
    hangman()
