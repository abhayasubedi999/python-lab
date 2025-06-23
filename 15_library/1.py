# Create a guessing game in Python. Computer has to randomly select a number between 1 to 10 and then prompt user to guess it. If user guesses correctly display You Win. If user guess is not correct display, You Loose. Number was {num}

import random


def guessing_game():
    # Computer selects a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Prompt user to guess the number
    user_guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is correct
    if user_guess == secret_number:
        print("You Win!")
    else:
        print(f"You Lose. The number was {secret_number}")


# Run the game
guessing_game()
