import random
import sys

# Title
print("\n!!!  LET'S PLAY ROCK, PAPER, SCISSORS  !!!")

# Track our stats
wins, losses, ties = 0, 0, 0

# Mapping of choices to their string representation
CHOICES = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
VALID_CHOICES = list(CHOICES.keys())

# Game Loop
while True:
    # Print current stats
    print(f"\n# You've had {wins} Wins, {losses} Losses, and {ties} Ties. #")

    # Player Input Loop
    while True:
        player_choice = input("Enter your move: (r)ock (p)aper (s)cissors [or (q)uit]: ").lower()

        if player_choice == 'q':
            sys.exit()  # Exit the program
        elif player_choice in VALID_CHOICES:
            break  # Leave player input loop
        else:
            print("Invalid input. Please enter 'r', 'p', 's', or 'q'.")

    # Display user's choice
    print(f"\n{CHOICES[player_choice]} versus...", end=' ')

    # Display computer's choice
    computer_choice = random.choice(VALID_CHOICES)
    print(CHOICES[computer_choice])

    # Determine the result
    if player_choice == computer_choice:
        print("\n\t* Hey, we tied! *")
        ties += 1
    elif (player_choice == 'r' and computer_choice == 's') or \
         (player_choice == 's' and computer_choice == 'p') or \
         (player_choice == 'p' and computer_choice == 'r'):
        print("\n\t* You WIN! *")
        wins += 1
    else:
        print("\n\t* You LOSE! *")
        losses += 1
