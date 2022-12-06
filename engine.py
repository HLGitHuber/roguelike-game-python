import util

def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    cords = player['player_cord']
    board[cords[0]][cords[1]] = player['player_symbol']


# def go_through_door(player, board, player_coord, inventory):
#     my_key = util.key_pressed()
#     if board[player_coord[1]] - 1 ==  #obok zablokowaneych drzwi i naciska klawisz w stronę drzwi
#         if inventory['key'] != None and my_key == 'k':
#             delete_from_inventory(inventory['key'])
#             #otwórz drzwi i zapamiętaj - zmiana na planszy
#             #zmień planszę
#         else:
#             print('You need a key to open the door')


def take_item(player, item):
    if player['player_cords'] == item['cords']:
        ask_for_adding(item)


def ask_for_adding(item):
    return True

def add_to_inventory(inventory, item):
    permission = ask_for_adding()
    if permission:
        inventory[item] += 1
    return inventory




def use_item(inventory):
    my_key = util.key_pressed()
    using_items = {
        "k": 'keys',
        "m" : 'medicine'
    }
    if str(my_key) in using_items:
        if input('Do you want to use one of your ', using_items[my_key], "? Confirm by c"):
            delete_from_inventory(inventory, using_items[str(my_key)])




def ask_for_using(item):
    return True



def delete_from_inventory(inventory, item):
    inventory[item] -=1
    return inventory
