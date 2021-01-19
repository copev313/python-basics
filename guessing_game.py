# guessing_game.py

# This is a simple guess the number game.

import random

start, end = (1, 100)
guesses_allowed = 15

# Generate a number between 'start' and 'end'.
secret_num = random.randint(start, end)
print("\n# Hello! I am thinking of a number between {} and {}.\n# You have {} guesses. GO!".format(start, end, guesses_allowed))

for num_guesses in range(1, guesses_allowed + 1):
    
    # Prompt the user:
    try:
        guess = int(input("\nTake a guess:  "))
    
    except ValueError:
        print("* Please submit a valid value...")
        continue
    
    # HINT CASES:    
    if (guess > secret_num):
        print("Your guess was too high.")
    elif (guess < secret_num):
        print ("Your guess was too low.")
    else:
        break   # WINNER! --> exit loop

if (guess == secret_num):
    print("\nWINNER!  You guessed my number in " + str(num_guesses) + " guesses!")
else:
    print("\nSorry, the number I was thinking of was " + str(secret_num) + ".")
    