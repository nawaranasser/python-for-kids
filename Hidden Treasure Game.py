import random

def find_the_treasure():
    print("Welcome to the Find the Hidden Treasure Game! 🎁")
    print("There are 3 boxes: [1] [2] [3]")
    print("One of them has the treasure inside. Can you find it?")

    # Randomly hide the treasure in one of the boxes
    treasure_box = random.choice([1, 2, 3])

    # Player makes a guess
    guess = int(input("Pick a box (1, 2, or 3): "))

    # Check if the player found the treasure
    if guess == treasure_box:
        print("🎉 Congratulations! You found the treasure!")
    else:
        print("❌ Oops! No treasure here. The treasure was in box", treasure_box)

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes" or "y":
        print("\n" * 2)  # Space before restarting
        find_the_treasure()
    else:
        print("Thanks for playing! Goodbye! 👋")

# Start the game
find_the_treasure()
