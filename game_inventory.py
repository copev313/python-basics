# game_inventory.py

# We demonstrate some ways to display, add and remove
# items from a player's inventory in a fantasy game.


def display_inventory(inventory={}):
    print('\n- - - - - - - - - -')
    print('INVENTORY: \n')          # Print title
    count = 0                       # Initialize counter variable
    
    if (inventory != {}):           # CASE: Nonempty Inventory
        for key, val in inventory.items():
            count += val
            if (val > 1):   key += 's'          # Handle plurals
            
            as_string = '{num} {name}'.format(num=val, name=key)
            print(as_string)
    else:                           # CASE: Empty Inventory
        print('  (empty)  ')
    
    weight_msg = '  (Things are getting pretty heavy.)' if (count > 400) else ''   # Conditional weight comment.
    print("\nTotal number of items: " + str(count) + weight_msg)            # Always print the total.
    print('\n- - - - - - - - - -\n\n')



def add_items(inventory={}, add_list=[]):
    if (add_list != []):            # CASE: Nonempty list
        for item in add_list:       # Iterate through each item in the list
            if item not in inventory.keys():       ## CASE: New type of item
                inventory[item] = 1
            else:                                  ## CASE: Item of this type already exist.
                inventory[item] += 1
                
    else:   pass                    # CASE: Empty list



def remove_items(inventory={}, remove_list=[]):
    if (remove_list != []):                # CASE: Nonempty list
        for item in remove_list:        # Iterate through each item in the list
            if item not in inventory.keys():        ## CASE: No such item in the inventory.
                continue
            else:                                   ## CASE: Item of this type exists, and one was removed.
                inventory[item] -= 1
                if (inventory[item] == 0):          # Delete items with zero inventory.
                    del inventory[item]
                    
    else:   pass                        # CASE: Empty list



# SOME TESTS COMMENTED BELOW:
'''
empty = {}
basic = {   'rope': 1, 'arrow': 12, 'gold coin': 25, 'fire stick': 5, 'dagger': 1  }
advanced = {     'rope': 8, 'arrow': 42, 'gold coin': 312, 'fire stick': 18, 'dagger': 11, 'helmet': 5, 
            'glove': 7, 'shield potion': 11, 'health potion': 7, 'elixir': 2, 'orb of confusion': 1,
            'label maker': 1, 'label': 4, 'cookie': 5  }

display_inventory(empty)
add_items(empty, ['rope', 'gold coin', 'twig', 'dirt', 'pebble', 'gold coin', 'gold coin'])
display_inventory(empty)

display_inventory(advanced)
remove_items(advanced, ['rope', 'arrow', 'arrow', 'label', 'health potion', 'arrow', 'fire stick', 'cookie'])
display_inventory(advanced)
'''
