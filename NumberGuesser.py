# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.
import random as r
random_number = r.randint(0, 100)
user_guess = None
while user_guess != random_number:
    print(random_number)
    while 1:
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