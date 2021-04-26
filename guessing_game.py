__foundby__ = "zabilsabri"

import random

print("GUESS THE NUMBER!")
number = random.randint(1, 9)
guess = int()
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != number and not out_of_guesses:

    if guess_count < guess_limit:
        guess = int(input("\nENTER THE NUMBER: "))

        if guess == number - 1 or guess == number + 1:
            print("CLOSE")
        elif guess < number:
            print("LOW")
        elif guess > number:
            print("HIGH")
        guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("YOU LOSE!")
else:
    print("YOU WIN!!")
