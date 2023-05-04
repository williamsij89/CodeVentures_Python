def start():
    print("You're in a dark room. There are two doors.")
    print("Do you choose door 1 or door 2?")

    choice = input("> ")

    if choice == "1":
        door1()
    elif choice == "2":
        door2()
    else:
        print("Invalid choice. Please try again.")
        start()

def door1():
    print("You find a treasure chest!")
    print("Do you want to open it? (yes/no)")

    choice = input("> ").lower()

    if choice == "yes":
        print("You found a pile of gold! You win!")
    elif choice == "no":
        print("You leave the chest and walk away.")
    else:
        print("Invalid choice. Please try again.")
        door1()

def door2():
    print("You find a sleeping dragon!")
    print("Do you want to wake it up? (yes/no)")

    choice = input("> ").lower()

    if choice == "yes":
        print("The dragon wakes up and eats you! Game over!")
    elif choice == "no":
        print("You quietly leave the room and close the door.")
    else:
        print("Invalid choice. Please try again.")
        door2()
