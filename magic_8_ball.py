# magic_8_ball.py

# Give the all knowing ball a shake

import random, time

print("###  MAGIC 8 BALL  ###", end='\n\n')

def shake():
    # Generate random num btw 0 & 8.
    r = random.randint(0, 8)
    print("Shaking . . . ", end='\n\n')
    # List of possible fortunes.        
    fortune_list = ["- It is certain",
                    "- It is decidedly so",
                    "- Yes",
                    "- Reply hazy try again",
                    "- Ask again later",
                    "- Concentrate and try again",
                    "- My reply is no",
                    "- Outlook not so good",
                    "- Very doubtful"             ]
    
    time.sleep(5)               # Add some suspense
    return fortune_list[r]      # Return reply
    
    
print(shake())