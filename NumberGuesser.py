# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.
import random as r

def numberGuess(difficulty):
    random_number = r.randint(0, 100)
    user_guess = None
    
    if difficulty == "medium":
        tries = 15
    elif difficulty == "hard":
        tries = 10
    
    if difficulty == "easy":
        print("You have unlimited tries")
        while user_guess != random_number:
            while 1:  # checks if the user guessed between the number range
                user_guess = int(input("guess the number in range of 0 - 100: \n"))
                if user_guess in range(0, 101):
                    break
                else:
                    print("Enter a number in range of 0 - 100\n")

            if user_guess < random_number:
                print("Lesser Than\n")
            elif user_guess > random_number:
                print("Greater Than\n")
        print("You Win!")
    else:
        for x in range(tries):
            print(f"You amount of tries: {tries - x}")
            
            while 1:  # checks if the user guessed between the number range
                user_guess = int(input("guess the number in range of 0 - 100: \n"))
                if user_guess in range(0, 101):
                    break
                else:
                    print("Enter a number in range of 0 - 100: ")

            if user_guess < random_number:
                print("Lesser Than\n")
            elif user_guess > random_number:
                print("Greater Than\n")
            elif user_guess == random_number:
                print("You Win")
                break
        if user_guess != random_number:
            print("You ran out of tries and lost")
        



difficulty = ["easy", "medium", "hard"]
userDifficulty = int(input("Enter a difficulty (easy (1), medium (2), hard(3)): "))

numberGuess(difficulty[userDifficulty - 1])