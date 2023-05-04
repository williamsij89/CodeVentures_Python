import random

def rock_paper_scissors():
    # Step 1: Create a list of the three possible shapes
    shapes = ["Rock", "Paper", "Scissors"]

    # Print the game's introduction message
    print("Welcome to the Rock-Paper-Scissors Showdown!")

    while True:
        # Step 2: Make the computer choose one shape randomly from the list
        computer_shape = random.choice(shapes)

        # Step 3: Take input from the user to choose their shape
        user_shape = input("\nPlease choose your shape (Rock, Paper, or Scissors): ").capitalize()

        if user_shape not in shapes:
            print("Invalid input! Please choose from Rock, Paper, or Scissors.")
            continue

        print(f"Computer's shape: {computer_shape}")

        # Step 4: Compare the user's shape with the computer's shape to determine the winner
        if user_shape == computer_shape:
            # Step 5: Display the result based on the comparison
            print("It's a draw!")
        elif (user_shape == "Rock" and computer_shape == "Scissors") or \
             (user_shape == "Scissors" and computer_shape == "Paper") or \
             (user_shape == "Paper" and computer_shape == "Rock"):
            print("Congratulations! You win!")
        else:
            print("You lose! Better luck next time!")

        # Step 6: Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes or no): ").lower()
        if play_again != "yes":
            break

# Call the function to start the game
rock_paper_scissors()
