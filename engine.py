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


# def go_through_door(location):
#     if player #obok zablokowaneych drzwi i naciska klawisz w stronę drzwi
#         if inventory[key] != None:
#             #otwórz drzwi i zapamiętaj - zmiana na planszy
#             #zmień planszę
#         else:
#             print('You need a key to open the door')


# def add_to_inventory(player, inventory, item):
#     player = main.create_player()
#     items = {
#         "k": 'keys',
#         "w" : 'weapon',
#         "a" : 'armor',
#         "m" : 'medicine'
#     }
#     if player[1]
       
import util

def delete_from_inventory(inventory):
    my_key = util.key_pressed()
    if my_key == 'm':
        inventory['medicine'] -= 1

