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
    # CASE: '1' -- end recursion
    if (num == 1):
        print("Sequence Complete!")
    # CASE: not '1'
    else:
        # CASE) Even -- print and return (num // 2)
        if (num % 2 == 0):
            new_num = num // 2
        # CASE) Odd -- print and return (3 * number +1)
        else:
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
        print("Enter a positive or negative whole number.")
        netrunner()
    except RecursionError:
        print("Enter a positive or negative whole number. Zero is neither.")


# Run program
netrunner()
