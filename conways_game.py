# conways_game.py

# A demonstration of Conway's Game of Life:

#   An example of cellular automata (a set of rules governing 
#   the behavior of a field made up of discrete cells).
#   Although the the rules are simple, there are several 
#   surprising behaviors that emerge. Patterns can move,
#   self-repliate, and even mimic CPUs.

import time, random, copy, sys

WIDTH, HEIGHT = (50, 25)
ALIVE, DEAD = ('■', '□')

# Create a list of lists for the cells:
next_cells = []
for x in range(WIDTH):
    column = []                         # Create a new column.
    for y in range(HEIGHT):
        if (random.randint(0, 1) == 0):
            column.append(ALIVE)          # Add a 'living' cell
        else:
            column.append(DEAD)          # Add a 'dead' cell
    
    next_cells.append(column)           # next_cells is a list of column lists.
    
try:    
    while True:                             # Main program loop
        print('\n\n\n\n\n')                 # Add seperate between each step.
        current_cells = copy.deepcopy(next_cells)
        
        for y in range(HEIGHT):             # Print current_cells
            for x in range(WIDTH):
                print(current_cells[x][y], end='')          # Print # or space
                
            print()                         # Print newline at the end of the row.
            
        for x in range(WIDTH):              # Calculate the next step's cells based on current step's cells.
            for y in range(HEIGHT):         # Get neighboring coordinates: 
                left  = (x - 1) % WIDTH     # '% WIDTH' ensures that left (coordinate) is always btw 0 and WIDTH - 1.
                right = (x + 1) % WIDTH
                above = (y - 1) % HEIGHT
                below = (y + 1) % HEIGHT
                
                num_neighbors = 0           # Count number of living neighbors.
                
                if (current_cells[left][above] == ALIVE):     # CASE: Top-left neighbor is alive.
                    num_neighbors += 1
                if (current_cells[x][above] == ALIVE):        # CASE: Top neighbor is alive.
                    num_neighbors += 1
                if (current_cells[right][above] == ALIVE):    # CASE: Top-right neighbor is alive.
                    num_neighbors += 1
                if (current_cells[left][y] == ALIVE):         # CASE: Left neighbor is alive.
                    num_neighbors += 1
                if (current_cells[right][y] == ALIVE):        # CASE: Right neighbor is alive.
                    num_neighbors += 1
                if (current_cells[left][below] == ALIVE):     # CASE: Bottom-left neighbor is alive.
                    num_neighbors += 1
                if (current_cells[x][below] == ALIVE):        # CASE: Bottom neighbor is alive.
                    num_neighbors += 1
                if (current_cells[right][below] == ALIVE):    # CASE: Bottom-right neighbor is alive.
                    num_neighbors += 1
                
                # Set cell based on Conway's Game of Life rules:
                
                # CASE: Living cells wiht 2 or 3 neighbors stay alive.
                if (current_cells[x][y] == ALIVE and (num_neighbors == 2 or num_neighbors ==3)):
                    next_cells[x][y] = ALIVE
                
                # CASE: Dead cells with 3 neighbors become alive.
                elif (current_cells[x][y] == ' ' and num_neighbors == 3):
                    next_cells[x][y] = ALIVE
                    
                # CASE: Everything else dies or stays dead.
                else:
                    next_cells[x][y] = DEAD
        
        time.sleep(1.5)           # Add a pause to reduce flickering.
        
except KeyboardInterrupt:
    sys.exit()
