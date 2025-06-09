import random

def guess_the_secret_word():
    print("Welcome to 'Guess the Secret Word!' 🎯")
    print("Try to guess the secret word, one letter at a time!")
    print("You have 6 chances. Let's go!\n")

    # Word list
    word_list = ["apple", "bag", "carrot", "lion", "tiger", "piano"]
    secret_word = random.choice(word_list)

    guessed_letters = []
    attempts = 6

    # Game loop

    while attempts > 0:
        # first draw "---" as length as the secret word
        display_word = ""
        for letter in secret_word:
            # if user suggest a correct letter , program puts this letter in the correct position
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                # draw a rest of word letters using " - "
                display_word += "_ "

        print("Word: ", display_word.strip())
        # "".strip()"" It removed the extra spaces at the start and end.


        # in case you have not any "- " , you are winner
        if "_" not in display_word:
            print("🎉 You guessed the secret word! Well done! 🎉")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try a new one!\n")
            continue  # skip this iteration of loop and repeat the loop from line 17

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Good job! Keep going!\n")
        else:
            attempts -= 1
            print("❌ Wrong guess! You have" , attempts , "attempts left.\n")

    if attempts == 0:
        print("Game Over! The secret word was '",secret_word,"'. Better luck next time!")

    # Ask to play again -----------------------------
    # play_again = input("Do you want to play again? (yes/no): ").lower()
    # if play_again == "yes":
    #     print("\n" * 2)
    #     guess_the_secret_word()
    # else:
    #     print("Thanks for playing! See you soon! 👋")

# Start the game
guess_the_secret_word()
