# create a list of words
import random

fruits = ['apple', 'banana', 'strawberry']


# Main function for the guessing game
def guessing_game():
    # define the function guessing_game

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the fruit.")
    word = random.choice(fruits)
    attempts = 3
    while attempts > 0:
        print('attempts left:' + str(attempts))
        guess = input("Guess the word ")
        if guess == word:
            print("Congratulations! You guessed the word: " + word)
            return
        else:
            print("Sorry, that's not the word.")
            attempts -= 1

            if word == fruits[0]:
                print("Its a round fruit and can be red, green, or yellow in color")
            elif word == fruits[1]:
                print("Its color is yellow and it's easily peeled")
            elif word == fruits[2]:
                print("Its color is red and with tiny yellow seeds on the surface")

    print("Game over! The word was: " + word)


# Call the guessing_game function to start the game
gussing_game()
