# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random as r

name = input("What is your name?: ")
randomGenerated = list()
tryAgain =  ["y", "yes", "no", "n"]

while 1:
    while 1:  # keeps asking if the input is not in the number range
        print("provide three numbers from 1-9: ")
        userInput = [int(input()), int(input()), int(input())]
        randomGenerated = [r.randint(1, 9), r.randint(1, 9), r.randint(1, 9)]
        
        # checks if the user input is between the range of the desired number
        if userInput[0] in range(1, 10) and userInput[1] in range(1, 10) and userInput[2] in range(1, 10):
            break

    # sorts the lists so order doesn't matter
    randomGenerated.sort()
    userInput.sort()

    if userInput == randomGenerated:
        print("Winner")
    else:
        print(f"You Loss, the numbers were {randomGenerated}")
        userAnswer = input(f"Would you like to try again " + (name) + "? ")

        # checks if the user entered yes or no
        while 1: 
            if userAnswer in tryAgain:
                break
            else:
                userAnswer = input("yes or no: ")
        
        if userAnswer in tryAgain[2:]:
            break