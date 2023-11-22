import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}\n")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'paper' and computer_choice == 'rock') or
            (player_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nPlayer score: {player_score}")
        print(f"Computer score: {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nFinal score:")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")

play_game()
