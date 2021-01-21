# collaz_sequence.py

# Demonstates the 'Collatz sequence'

def collatz(num):
    """
    Implements the procedure for generating the Collatz sequence.

    Parameters
    ----------
    num : int
        The integer that starts the sequence.
    """
    if (num == 1):                      # CASE: '1' -- end recursion
        print("Sequence Complete!")
        
    else:                               # CASE: not '1'
        if (num % 2 == 0):      ## CASE: EVEN -- print and return (num // 2)
            new_num = num // 2
        else:                   ## CASE: ODD -- print and return (3 * number +1)
            new_num = 3 * num + 1
        
        print(new_num)
        return collatz(new_num)



def netrunner():
    """
    Driver code of the program.
    """
    try:
        # Accept user input
        integer = int(input("\nEnter an integer:  "))
        collatz(integer)
        
    except ValueError:
        print("Value Error! -- Please enter a positive or negative whole number.")
        netrunner()
        
    except RecursionError:
        print("ZERO (booooo!)\nPlease enter a positive or negative whole number.")
        

# Run program        
netrunner()