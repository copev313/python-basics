# zigzag.py

# Prints a continuous zigzag to the console.

import sys
import time

indent = 0                  # Number of spaces to indent.
indent_increasing = True    # Whether indent is increasing or not.
max_indent = 25             # Set level of zag

try:
    # Main Loop
    while True:
        print(' ' * indent, end='')
        print('*****')
        time.sleep(0.1)         # Pause for 1/10 of a second.

        if indent_increasing:
            indent += 1
            if (indent == max_indent):
                indent_increasing = False       # Change direction
        else:
            indent -= 1         # Decrease the number of spaces.
            if (indent == 0):   # Change direction
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()
