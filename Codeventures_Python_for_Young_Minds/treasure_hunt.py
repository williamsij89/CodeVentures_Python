import random

def treasure_hunt(grid_size):
    # Step 1: Define the size of the grid
    grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

    # Step 2: Create a grid with a randomly placed treasure
    treasure_x = random.randint(0, grid_size - 1)
    treasure_y = random.randint(0, grid_size - 1)

    # Step 3: Initialize the player's position at the center of the grid
    player_x, player_y = grid_size // 2, grid_size // 2
    grid[player_y][player_x] = "P"

    def print_grid():
        for row in grid:
            print(" | ".join(row))
            print("-" * (grid_size * 2 - 1))

    # Step 4: Print the initial game board
    print("Welcome to the Treasure Hunt!")
    print_grid()

    while True:
        # Step 5: Take input from the user for their move
        move = input("Enter your move (up, down, left, or right): ").lower()

        # Step 6: Update the player's position based on their move
        grid[player_y][player_x] = " "
        if move == "up":
            player_y = max(0, player_y - 1)
        elif move == "down":
            player_y = min(grid_size - 1, player_y + 1)
        elif move == "left":
            player_x = max(0, player_x - 1)
        elif move == "right":
            player_x = min(grid_size - 1, player_x + 1)
        else:
            print("Invalid move! Please enter up, down, left, or right.")
            continue
        grid[player_y][player_x] = "P"

        # Step 7: Check if the player has found the treasure
        if player_x == treasure_x and player_y == treasure_y:
            # Step 9: Congratulate the player and end the game
            print_grid()
            print("Congratulations! You found the treasure!")
            break

        # Step 8: Provide a hint and repeat the process
        print_grid()
        if abs(player_x - treasure_x) > abs(player_y - treasure_y):
            print("Hint: Move in the horizontal direction.")
        else:
            print("Hint: Move in the vertical direction.")

# Call the function to start the game
treasure_hunt(5)
