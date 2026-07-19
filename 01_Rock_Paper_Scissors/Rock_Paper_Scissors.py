import random

# Track the number of wins for the player and the computer
user_wins = 0
computer_wins = 0

# Available game choices
options = ["rock", "paper", "scissors"]

# Main game loop
while True:
    user_input = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()

    # Exit the game if the user chooses to quit
    if user_input == "q":
        break

    # Ignore invalid input and prompt the user again
    if user_input not in options:
        continue

    # Randomly select the computer's move
    random_number = random.randint(0, 2)  # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]

    print("Computer picked", computer_pick + ".")

    # Check for a draw first
    if user_input == computer_pick:
        print("It's a draw!")

    # Check all winning conditions for the player
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    # If none of the above conditions are met, the computer wins
    else:
        print("You lost!")
        computer_wins += 1

# Display the final score
print("\nFinal Score:")
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")