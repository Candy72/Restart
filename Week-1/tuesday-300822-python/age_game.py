#puppo
name = input("Please enter your name ")
age = input("Please enter your age ")
game = input("Please enter the game name ")
rating = input("Please enter the game's rating ")
if age < 16 and rating == "R16":
    print("You are too young to play " + game + " " + name)
elif age >= rating:
    print("Your are old enough to play " + game + name)
else:
    print("Something has gone wrong, please ensure the age is a number and not text")


    #Brandon.p
    age = int(input("What is your age?"))
if age >= 18:
    print("you are old enough")
else:
    print("sorry, come back when you're older")
