# coin_flip_streaks.py

# A program that investigates how often a streak of N head or N tails 
#   comes up in a randomly generated list of heads and tails.

import random


def coin_flips(sample_size=100):
    """
    Creates a list of a 'sample_size' number of 'H' and 'T's for heads and tails.

    Parameters
    ----------
    sample_size : int, optional
        The number of 'coin flips' to execute, by default 100

    Returns
    -------
    results_list: list
        A list of 'H' and 'T's depicting the results fron the coin flips.
    """
    SAMPLE_SIZE = sample_size
    results_list = []
    
    for experiment_num in range(SAMPLE_SIZE):       # Generate list of heads and tails values.
        coin_flip = random.choice(['H', 'T'])       # Random 'H' or 'T'
        results_list.append(coin_flip)
    
    return results_list



def streak_tracker(flips_list=[], streak_of=3):
    """
    Determines the number of streaks of a specific length, 'streak_of'.

    Parameters
    ----------
    flips_list : list, optional
        The list to search for streaks, by default []
    streak_of : int, optional
        The length necessary to count as a streak, by default 3

    Returns
    -------
    dict
        A dictionary of the form: {'HEAD STREAKS': ###, 'TAIL STREAKS': ###}, 
        that displays how many of each type of streak occurred.
    """
    STREAKS = {'HEADS': 0, 'TAILS': 0}      # Keep a dictionary to track counts.
    HEAD_STREAKS, TAIL_STREAKS = (0, 0)       # Keep track of the type of streak and how many.
    
    if (flips_list != []):          # CASE: Nonempty list
        previous = None
        for i, current in enumerate(flips_list):
            # Catch streaks & Reset dictionary values
            if (STREAKS['HEADS'] == streak_of):
                HEAD_STREAKS += 1         
                STREAKS['HEADS'] = 0
            elif (STREAKS['TAILS'] == streak_of):
                TAIL_STREAKS += 1
                STREAKS['TAILS'] = 0
                
            # CASE: Same as previous value
            if (current==previous):         
                if (current=='H'):
                    STREAKS['HEADS'] += 1
                elif (current=='T'):
                    STREAKS['TAILS'] += 1
            # CASE: Different than previous value
            else:
                if (current=='H'):
                    STREAKS['HEADS'] = 1
                elif (current=='T'):
                    STREAKS['TAILS'] = 1
                    
            previous = flips_list[i-1]             # Store current as previous for next iteration
                
        return {'HEAD STREAKS': HEAD_STREAKS, 'TAIL STREAKS': TAIL_STREAKS}
    
    else:                           # CASE: Empty list
        return {'HEAD STREAKS': None, 'TAIL STREAKS': None}



# TESTS COMMENTED BELOW:
'''
coin_flip_results = coin_flips(10000)
print(' '.join(coin_flip_results))

sample = [ 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'H', 'T', 
            'H', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'H', 'H', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'T', 'H' ]
head_sample = ['H', 'H', 'H', 'H', 'H', 'H', 'H']
tail_sample = ['T', 'T', 'T', 'T', 'T', 'T', 'T']

report_back = streak_tracker(coin_flip_results, 7)
print(report_back)
'''