#number guessing game

import random
random_number = random.randint(1, 15)
print("Guess a number between 1 and 15")

while True:
    user_guess = input("Enter your guess: ")
    user_guess = int(user_guess)
    if user_guess == random_number:
        print("Congratulations! You guessed the number.")
        break
    elif user_guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")