import util

def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for row in board:
        for element in row:
            print(element, end = ' ')
        print()

def display_inventory(inventory):
    for item in inventory :
        print(item, ": ", inventory[item])


def ask_for_using(item):
    print('Do you want to use one of your ', item, "? Confirm by c")
    my_key = util.key_pressed()
    if my_key == 'c':
        return True
    