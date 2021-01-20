# zigzag.py

# Print an infinite zigzag to the console.

import time, sys

indent= 0                   # Number of spaces to indent.
indent_increasing = True    # Whether indent is increasing or not.
max_indent = 25             # Set level of zag

try:
    while True:     # Main loop
        print(' ' * indent, end='')
        print('*****')
        time.sleep(0.1)         # Pause for 1/10 of a second.
        
        if indent_increasing:
            indent += 1         # Increase the number of spaces.
            if (indent == max_indent):  # Change direction:
                indent_increasing = False
        else:
            indent -= 1         # Decrease the number of spaces.
            if (indent == 0):   # Change direction:
                indent_increasing = True
                    
except KeyboardInterrupt:
    sys.exit()
                    