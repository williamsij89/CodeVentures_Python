import random

def number_guessing_game(min_num, max_num, max_attempts):
    # Step 1: Generate a random number within the given range
    secret_number = random.randint(min_num, max_num)
    
    # Print the introduction message
    print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {min_num} and {max_num}. You have {max_attempts} attempts to guess my number. Good luck!")

    # Step 2: Set the maximum number of attempts
    attempts_left = max_attempts

    while attempts_left > 0:
        # Step 3: Take input from the user for their guess
        guess = int(input(f"\nYou have {attempts_left} attempts left. Please enter your guess: "))
        
        # Step 4: Compare the user's guess with the actual number
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly!")
            return
        elif guess < secret_number:
            # Step 5: Provide hints based on the comparison
            print("Oops! Your guess is too low.")
        else:
            print("Oops! Your guess is too high.")
        
        # Decrease the number of attempts left
        attempts_left -= 1

    # If the player runs out of attempts, reveal the secret number
    print(f"\nSorry, you're out of attempts! The secret number was {secret_number}. Better luck next time!")

# Call the function to start the game
number_guessing_game(1, 100, 7)
