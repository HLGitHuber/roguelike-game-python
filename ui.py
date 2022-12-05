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
