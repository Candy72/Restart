# Exercise 1: Working with a while loop
# Printing the game rules

import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Importing random and writing a while loop
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
# Writing pseudocode

# For example:

    # If the user has not guessed the correct answer, enter the loop.

    # Ask the user for a guess.

    # Is the guess the correct number?

    # If the correct guess, tell the user it was the correct guess and exit the loop.

    # If the wrong guess, tell the user it was the wrong guess and continue the loop.
print("Count to 10!")

for x in range (0, 11):
    print(x)