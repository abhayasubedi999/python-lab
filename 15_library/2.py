# Modify this guessing game so that user has three attempt to guess. On incorrect display Incorrect!! Guess higher/lower number depending upon if number guessed by user is lower or higher. If user can’t guess in 3 attempt display You Loose. Number was {num}.
import random


def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("Welcome to the Guessing Game!")
    print("You have 3 attempts to guess a number between 1 and 10.")

    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt}:")
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess == secret_number:
                print("Congratulations! You Win!")
                return
            elif user_guess < secret_number:
                print("Incorrect!! Guess a higher number.")
            else:
                print("Incorrect!! Guess a lower number.")

        except ValueError:
            print("Please enter a valid number between 1 and 10.")

    print(f"\nYou Lose. The number was {secret_number}")


guessing_game()
