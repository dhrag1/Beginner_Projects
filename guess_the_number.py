import random

min = int(input("Enter an integer value for the minimum potential guess number: "))
max  = int(input("Enter an integer value for the maximum potential guess number: "))
num_attempts = 1

guess = int()

while True:
    target = random.randint(min, max)

    if target != 0:
        break


print("The target number has been randomly selected.")
guess = int(input("Enter your guess: "))

while guess != target:
    if guess > target:
        print("Try Again! Your guess was too high!")
    elif guess < target:
        print("Try Again! Your guess was too low!")
    num_attempts += 1
    guess = int(input("Enter your guess: "))

print("You successfully guessed the number in", num_attempts, "guesses!")
        