# conways_game.py

# A demonstration of Conway's Game of Life:

#   An example of cellular automata (a set of rules governing
#       the behavior of a field made up of discrete cells).
#       Although the the rules are simple, there are several
#       surprising behaviors that emerge. Patterns can move,
#       self-repliate, and even mimic CPUs.

import copy
import random
import sys
import time

WIDTH, HEIGHT = (50, 25)
ALIVE, DEAD = ('■', '□')

# Create a list of lists for the cells:
next_cells = []
for x in range(WIDTH):
    # Create a new column.
    column = []
    for y in range(HEIGHT):
        # CASE) Add a 'living' cell.
        if (random.randint(0, 1) == 0):
            column.append(ALIVE)
        # CASE) Add a 'dead' cell.
        else:
            column.append(DEAD)
    # next_cells is a list of column lists.
    next_cells.append(column)

try:
    # Main Program Loop
    while True:
        # Add seperate between each step.
        print('\n\n\n\n\n')
        current_cells = copy.deepcopy(next_cells)

        # Print current_cells
        for y in range(HEIGHT):
            for x in range(WIDTH):
                # Print # or space
                print(current_cells[x][y], end='')
            # Print newline at the end of the row.
            print()

        # Calc the next step's cells based on current step's cells.
        for x in range(WIDTH):
            # Get neighboring coordinates:
            for y in range(HEIGHT):
                # '% WIDTH' ensures that left is always btw 0 and WIDTH - 1.
                left = (x - 1) % WIDTH
                right = (x + 1) % WIDTH
                above = (y - 1) % HEIGHT
                below = (y + 1) % HEIGHT

                # Count number of living neighbors.
                num_neighbors = 0

                # CASE: Top-left neighbor is alive.
                if (current_cells[left][above] == ALIVE):
                    num_neighbors += 1
                # CASE: Top neighbor is alive.
                if (current_cells[x][above] == ALIVE):
                    num_neighbors += 1
                # CASE: Top-right neighbor is alive.
                if (current_cells[right][above] == ALIVE):
                    num_neighbors += 1
                # CASE: Left neighbor is alive.
                if (current_cells[left][y] == ALIVE):
                    num_neighbors += 1
                # CASE: Right neighbor is alive.
                if (current_cells[right][y] == ALIVE):
                    num_neighbors += 1
                # CASE: Bottom-left neighbor is alive.
                if (current_cells[left][below] == ALIVE):
                    num_neighbors += 1
                # CASE: Bottom neighbor is alive.
                if (current_cells[x][below] == ALIVE):
                    num_neighbors += 1
                # CASE: Bottom-right neighbor is alive.
                if (current_cells[right][below] == ALIVE):
                    num_neighbors += 1

            # Set cell based on Conway's Game of Life rules:

                # CASE: Living cells with 2 or 3 neighbors stay alive.
                if (current_cells[x][y] == ALIVE and
                   (num_neighbors == 2 or num_neighbors == 3)):
                    next_cells[x][y] = ALIVE
                # CASE: Dead cells with 3 neighbors become alive.
                elif (current_cells[x][y] == ' ' and num_neighbors == 3):
                    next_cells[x][y] = ALIVE
                # CASE: Everything else dies or stays dead.
                else:
                    next_cells[x][y] = DEAD

        # Add a pause to reduce flickering.
        time.sleep(1.5)

except KeyboardInterrupt:
    sys.exit()
