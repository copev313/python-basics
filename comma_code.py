# comma_code.py

def list_the_list(the_list=[]):
    """
    Takes a list value as an argument and returns a string with all the items 
    seperated by a comma and a space, with 'and' inserted before the last item.

    Parameters
    ----------
    the_list : list, optional
        A list of items, by default []

    Returns
    -------
    list_string: str
        A string listing the items found in 'the_list'.
    """
    if (the_list != []):        # CASE: List is nonempty
        list_string = ''
        list_length = len(the_list)
        for index, item in enumerate(the_list):
            item = str(item)                        # Force to string (just in case).
            if (index == 0):                        ## CASE: First item in the list.
                list_string += item
            elif (index == list_length - 1):        ## CASE: Last item in the list.
                list_string += ', and ' + item + '.'
            else:                                   ## CASE: Between first and last item in the list.
                list_string += ', ' + item
                
    else:                       # CASE: List is empty
        list_string = '(An empty list)'

    return list_string



# COMMENTED SOME TESTS BELOW:
'''
test_list = [11, 'eleven', 'twelve', 'cat', 'dog', 'cow', 'pig', False]
empty_list = []
list_in_a_list = [['cookie', 'cooky', 'cook-E'], ['burger', 'french fries', 'milkshake']]

print(list_the_list(test_list))
print()
print(list_the_list(empty_list))
print()
print(list_the_list(list_in_a_list))
'''