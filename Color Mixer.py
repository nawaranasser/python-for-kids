#function without parameters
def color_mixer():
    color1 = input("Enter the first color: ").lower()
    color2 = input("Enter the second color: ").lower()

    # try to remember the logical operators
    if ((color1 == "red" and color2 == "blue") or
            (color1 == "blue" and color2 == "red")):
        print("You get purple 💜!")
    elif ((color1 == "red" and color2 == "yellow") or
          (color1 == "yellow" and color2 == "red")):
        print("You get orange 🧡!")
    elif ((color1 == "red" and color2 == "green") or
        (color1 == "green" and color2 == "red")):
        print("You get yellow 💛!")
    elif ((color1 == "yellow" and color2 == "blue") or
        (color1 == "blue" and color2 == "yellow")):
        print("You get green 💚!")
    elif ((color1 == "white" and color2 == "black") or
        (color1 == "black" and color2 == "white")):
        print("You get grey 🩶!")
    else:
        print("I don't know that mix.")


# same function with parameters
def color_mixer_2(color1 , color2):


    # try to remember the logical operators
    if ((color1 == "red" and color2 == "blue") or
            (color1 == "blue" and color2 == "red")):
        print("You get purple 💜!")
    elif ((color1 == "red" and color2 == "yellow") or
          (color1 == "yellow" and color2 == "red")):
        print("You get orange 🧡!")
    elif ((color1 == "red" and color2 == "green") or
          (color1 == "green" and color2 == "red")):
        print("You get yellow 💛!")
    elif ((color1 == "yellow" and color2 == "blue") or
          (color1 == "blue" and color2 == "yellow")):
        print("You get green 💚!")
    elif ((color1 == "white" and color2 == "black") or
          (color1 == "black" and color2 == "white")):
        print("You get grey 🩶!")
    else:
        print("I don't know that mix.")




# first function call
print('Welcome to color mixer game 🎨')
color_mixer()
# second function call
print('Welcome to color mixer game 🎨')
color_mixer_2("yellow" , "blue")
