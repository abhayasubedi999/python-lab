# Create a Rock, Scissor, Paper game. Computer chooses & prompt user to choose his choice. Display You Win/Loose. [Should ask if he wants to replay]

import random


def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice in choices:
            break
        print("Invalid choice! Please try again.")

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
    else:
        print("You Lose!")


def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        play_game()

        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
