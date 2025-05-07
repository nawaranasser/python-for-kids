import time
import random

def memory_game():

    # remember the syntax of the list
    words = ["apple","lion" ,"banana", "carrot","bag"]
    print("Remember these words:")
    print(words)
    # stop code for 5 seconds
    time.sleep(5)
    # "\n" to create new line
    print("\n" * 50)
    for i in range(len(words)):
        random_num = random.choice([1,2,3,4,5])
        guess = input("What was the " +str(random_num)+" word?" )
        if guess == words[random_num - 1]:
            print("Correct 🥳!")
        else:
            print("Try again !")


#call the function
memory_game()