import util
import ui

SPACES_ALLOWED_TO_MOVE = ['O']
SPACES_WITH_ITEMS = ['k', 'm']
GATES = ['G']
SPACED_BANNED_FROM_MOVING = ''
PLAYER_SYMBOL = '@'
INVENTORY = {
    "keys": 0,
    "medicine" : 3,
}
INVENTORY_DICT = {
    'k' : 'keys',
    'm' : 'medicine'
}


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
    cord_1 = player['player_cord_1']
    cord_2 = player['player_cord_2']
    board[cord_1][ cord_2] = player['player_symbol']
    return board


def add_to_inventory(inventory, item):
    print('You have found a ', item)
    inventory[item] += 1
    return inventory

def use_item(inventory):
    print(inventory)
    my_key = util.key_pressed()
    inventory = INVENTORY
    
    if my_key in INVENTORY_DICT:
        item = my_key
        item = INVENTORY_DICT[item]
        if inventory[item] == 0:
            print('You do not have', item, 'to use')
        
        elif inventory[item] > 0:
            permission = ui.ask_for_using(item)
            if permission:
                delete_from_inventory(inventory, item)
                return 'used'

def delete_from_inventory(inventory, item):
    inventory = INVENTORY
    inventory[item] -= 1
    return inventory


def move_left(board, player_coord):
    if board[player_coord[0]][player_coord[1]-1] in SPACES_ALLOWED_TO_MOVE:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] +=-1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]-1] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] +=-1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)



def move_right(board, player_coord):
    if board[player_coord[0]][player_coord[1]+1] in SPACES_ALLOWED_TO_MOVE:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] += 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]+1] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] +=1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
    elif board[player_coord[0]][player_coord[1]+1] in GATES:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] +=1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        if open_door() == 'open':
            pass #przenieś na inną planszę

        

def move_up(board, player_coord):
    if board[player_coord[0]-1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[0] +=-1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]-1][player_coord[1]] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[0] +=-1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)


def move_down(board, player_coord):
    if board[player_coord[0]+1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[0] +=1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]+1][player_coord[1]] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[0] +=1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)



def open_door():
    print('If you want to go through door, you need to use a key. Press k to do it.')
    if use_item(INVENTORY) == 'used':
        return 'open'

def display(board):
    for line in board:
        print(*line)



def get_board(filename):
    with open(filename, 'r') as file:
        return [list(line)[:-1] for line in file.readlines()]
    









## do sprawdzania działania inwentarza
# for _ in range(2):
#     use_item(INVENTORY)
#     #print(INVENTORY)



# def go_through_door(player, board, player_coord, inventory):
#     my_key = util.key_pressed()
#     if board[player_coord[1]] - 1 ==  #obok zablokowaneych drzwi i naciska klawisz w stronę drzwi
#         if inventory['key'] != None and my_key == 'k':
#             delete_from_inventory(inventory['key'])
#             #otwórz drzwi i zapamiętaj - zmiana na planszy
#             #zmień planszę
#         else:
#             print('You need a key to open the door')





# def add_to_inventory_file(inventory, file_name):
#     inventory = add_to_inventory()
#     added_things = []
#     for row in inventory:
#         added_things.append(row)

#     with open(file_name, 'r') as readFile:
#         reader = csv.reader(readFile)
#         for row in reader:
#             added_things.append(row)
#     with open(file_name, 'w') as writeFile:
#         for row in writeFile:
#             writeFile(row) = added_things[row]
#         writer = csv.writer(writeFile)
#         writer.writerows(added_things)
