def haunted_house_adventure():
    # Step 1: Print the introduction and set the initial game state
    print("Welcome to the Haunted House Adventure!")
    print("You find yourself at the entrance of a spooky old house. Can you make it through?")
    game_state = {"room": "entrance", "has_key": False}

    while True:
        # Step 2: Describe the current room and present the available actions
        if game_state["room"] == "entrance":
            print("\nYou are at the entrance of the house. There's a door in front of you.")
            actions = ["Enter the house", "Leave"]

        elif game_state["room"] == "living_room":
            print("\nYou are in the living room. There's a door to your right and a locked chest.")
            actions = ["Go back", "Open the chest", "Go through the door"]

        elif game_state["room"] == "bedroom":
            print("\nYou are in a bedroom. There's a key on the table.")
            actions = ["Go back", "Take the key"]

        # Step 3: Take input from the user to choose an action
        print("\nWhat would you like to do?")
        for idx, action in enumerate(actions, start=1):
            print(f"{idx}. {action}")
        choice = int(input("Enter the number of your choice: "))

        # Step 4: Update the game state based on the chosen action
        if game_state["room"] == "entrance":
            if choice == 1:
                game_state["room"] = "living_room"
            elif choice == 2:
                print("You decide to leave the haunted house.")
                break

        elif game_state["room"] == "living_room":
            if choice == 1:
                game_state["room"] = "entrance"
            elif choice == 2:
                if game_state["has_key"]:
                    # Step 5: Check for victory condition
                    print("You unlock the chest and find a treasure! Congratulations, you win!")
                    break
                else:
                    print("The chest is locked. You need a key to open it.")
            elif choice == 3:
                game_state["room"] = "bedroom"

        elif game_state["room"] == "bedroom":
            if choice == 1:
                game_state["room"] = "living_room"
            elif choice == 2:
                game_state["has_key"] = True
                print("You take the key from the table.")

# Call the function to start the game
haunted_house_adventure()
