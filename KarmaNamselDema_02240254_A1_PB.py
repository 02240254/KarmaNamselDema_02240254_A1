import random

def main():
    while True:
        # Display the menu
        print("Select a function (1-3):")
        print("1. Guess Number game")
        print("2. Rock paper scissors game")
        print("3. Exit program")

        # Get user's choice
        choice = input("Enter your choice: ")

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def guess_number_game():
    print("Welcome to the Guess Number Game!")
    try:
        lower = int(input("Enter the lower range: "))
        upper = int(input("Enter the upper range: "))
        number_to_guess = random.randint(lower, upper)

        while True:
            try:
                guess = int(input("Guess a number: "))
                if guess < lower or guess > upper:
                    print(f"Please guess a number between {lower} and {upper}.")
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You guessed the correct number.")
                    break
            except ValueError:
                print("Please enter a valid number.")

    except ValueError:
        print("Invalid input. Please enter valid integers for the range.")

def rock_paper_scissors_game():
    print("Welcome to Rock Paper Scissors!")

    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
