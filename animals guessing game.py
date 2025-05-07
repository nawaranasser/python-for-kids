import random

animals = ["cat", "dog", "elephant", "lion", "tiger"]
# use dictionary concept to link animal with its description
hints = {
    "cat": "I like to chase mice and say 'meow'",
    "dog": "I bark and wag my tail",
    "elephant": "I have a long trunk",
    "lion": "I am the king of the jungle",
    "tiger": "I have high speed and a loud roar"
}

chosen = random.choice(animals)
print("Guess the animal!")
print("Hint:", hints[chosen])

guess = input("Your guess: ").lower()

if guess == chosen:
    print("Correct! 🎉")
else:
    print("Oops! The answer was:", chosen)
