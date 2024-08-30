import random

def high_low_game(rounds):
    player_score = 0

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")

        # Generate random numbers for player and computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Show the player's number
        print(f"Your number is: {player_number}")

        # Ask the player to guess if their number is higher or lower
        guess = input("Do you think your number is 'higher' or 'lower' than the computer's number? ").lower()

        # Determine if the player guessed correctly
        if (guess == 'higher' and player_number > computer_number) or (guess == 'lower' and player_number < computer_number):
            print("Correct! You earn a point.")
            player_score += 1
        else:
            print("Wrong guess! No points earned.")
        
        # Reveal the computer's number
        print(f"The computer's number was: {computer_number}")

    # Final score
    print("\nGame Over!")
    print(f"Your final score: {player_score}")

    if player_score == rounds:
        print("Perfect score! Well done!")
    else:
        print("Thanks for playing!")

# Start the game with a specified number of rounds
rounds_to_play = int(input("Enter the number of rounds you want to play: "))
high_low_game(rounds_to_play)
