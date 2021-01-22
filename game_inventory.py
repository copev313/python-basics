# game_inventory.py

# We demonstrate some ways to display, add and remove items from a
# player's inventory in a fantasy game.


def display_inventory(inventory={}):
    print('\n- - - - - - - - - -')
    print('INVENTORY: \n')
    # Initialize counter variable
    count = 0

    # CASE: Nonempty Inventory
    if (inventory != {}):
        for key, val in inventory.items():
            count += val
            # Handle plurals
            if (val > 1):
                key += 's'
            as_string = '{num} {name}'.format(num=val, name=key)
            print(as_string)
    # CASE: Empty Inventory
    else:
        print('  (empty)  ')

    # Conditional weight comment.
    weight_msg = '  (Things are getting heavy...)' if (count > 400) else ''
    # Always print the total.
    print("\nTotal number of items: " + str(count) + weight_msg)
    print('\n- - - - - - - - - -\n\n')


def add_items(inventory={}, add_list=[]):
    # CASE: Nonempty list
    if (add_list != []):
        for item in add_list:
            # CASE) New type of item
            if item not in inventory.keys():
                inventory[item] = 1
            # CASE) Item of this type already exist.
            else:
                inventory[item] += 1
    return


def remove_items(inventory={}, remove_list=[]):
    # CASE: Nonempty list
    if (remove_list != []):
        for item in remove_list:
            # CASE) No such item in the inventory.
            if item not in inventory.keys():
                continue
            # CASE) Item of this type exists, and one was removed.
            else:
                inventory[item] -= 1
                # Delete items with zero inventory.
                if (inventory[item] == 0):
                    del inventory[item]
    return


# TESTS COMMENTED BELOW:
'''
empty = {}
basic = {'rope': 1, 'arrow': 12, 'gold coin': 25, 'fire stick': 5, 'dagger': 1}
advanced = {'rope': 8, 'arrow': 42, 'gold coin': 312, 'fire stick': 18,
            'dagger': 11, 'helmet': 5,'glove': 7, 'shield potion': 11,
            'health potion': 7, 'elixir': 2, 'orb of confusion': 1,
            'label maker': 1, 'label': 4, 'cookie': 5}

to_add = ['rope', 'gold coin', 'twig', 'dirt', 'pebble', 'gold coin',
            'gold coin']
display_inventory(empty)
add_items(empty, to_add)
display_inventory(empty)

to_remove = ['rope', 'arrow', 'arrow', 'label', 'health potion', 'arrow',
                'fire stick', 'cookie']
display_inventory(advanced)
remove_items(advanced, to_remove)
display_inventory(advanced)
'''
