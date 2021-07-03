__foundby__ = "zabilsabri"

import random

print("GUESS THE NUMBER GAME!")
print("Good Luck!")
number = random.randint(1, 9)
guess = int()
guess_limit = 3
out_of_guesses = False

while guess != number and not out_of_guesses:

    if guess_limit != 0:
        print("\nYou Have", end=" ")
        print(guess_limit, end=" ")
        print("Guesses!")
        guess = int(input("ENTER THE NUMBER: "))
        guess_limit -= 1

        if guess == number - 1 or guess == number + 1:
            print("CLOSE")
        elif guess < number:
            print("LOW")
        elif guess > number:
            print("HIGH")

    else:
        out_of_guesses = True

if out_of_guesses:
    print("\nYOU LOSE!")
else:
    print("\nYOU WIN!!")
