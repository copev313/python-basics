# rock_paper_scissors.py

# A nice game of rock, paper, scissor.

import random
import sys

# Title
print("\n!!!  LET'S PLAY ROCK, PAPER, SCISSORS  !!!")

# Track our stats
wins, losses, ties = (0, 0, 0)

# Game Loop
while True:
    # Print current stats
    stat_str = "\n# You've had {w} Wins, {l} Losses, and {t} Ties. #"
    stat_str = stat_str.format(w=wins, l=losses, t=ties)
    print(stat_str)

    # Player Input Loop
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors  [or (q)uit]")
        p_choice = input()

        if (p_choice == 'q'):
            sys.exit()              # Exit the program
        elif (p_choice in ['r', 'p', 's']):
            break                   # Leave player input loop
        else:
            print("Please enter r, p, s, or q.")

    # Display user's choice
    choices_dict = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
    players_move = choices_dict[p_choice]
    print("\n{} versus... ".format(players_move), end='')

    # Display computer's choice
    choices_list = ['r', 'p', 's']
    c_choice = random.choice(choices_list)
    print(choices_dict[c_choice])

    # RESULT CASES:
    tie_condition = (p_choice == c_choice)
    player_win_cond = ((p_choice == 'r' and c_choice == 's') or
                       (p_choice == 's' and c_choice == 'p') or
                       (p_choice == 'p' and c_choice == 'r'))
    player_lose_cond = ((p_choice == 'r' and c_choice == 'p') or
                        (p_choice == 's' and c_choice == 'r') or
                        (p_choice == 'p' and c_choice == 's'))

    # Display the result and update stats
    if (tie_condition):
        print("\n\t* Hey, we tied! *")
        ties += 1
    elif (player_win_cond):
        print("\n\t* You WIN! *")
        wins += 1
    elif (player_lose_cond):
        print("\n\t* You LOSE! *")
        losses += 1
