import util
import ui


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
    temp_board = [*board[cords[0]]]
    temp_board[cords[1]] = player['player_symbol']
    board[cords[0]] = ''.join([str(elem) for elem in temp_board])
    #fix 


SPACES_ALLOWED_TO_MOVE = ['.']
SPACES_WITH_ITEMS = ['k', 'm']
SPACED_BANNED_FROM_MOVING = ''
PLAYER_SYMBOL = '@'
INVENTORY = {
    "keys": 3,
    "medicine" : 0,
}
INVENTORY_DICT = {
    'k' : 'keys',
    'm' : 'medicine'
}

def add_to_inventory(inventory, item):
    print('You have found a ', item)
    inventory[item] += 1
    return inventory

#NEEDED FIXES FOR MOVING 
def slicing_for_movement(board, player_coord, letter):
    concatenation = player_coord[1]+1
    board[player_coord[0]] = board[player_coord[0]][:player_coord[1]] +letter+ board[player_coord[0]][concatenation:]

def move_left(board, player_coord):
    if board[player_coord[0]][player_coord[1]-1] in SPACES_ALLOWED_TO_MOVE:
        slicing_for_movement(board,player_coord,'.')
        player_coord[1] +=-1
        slicing_for_movement(board,player_coord,PLAYER_SYMBOL)
    elif board[player_coord[0]][player_coord[1]-1] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = '.'
        player_coord[1] +=-1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
        #print(INVENTORY)


def move_right(board, player_coord):
    if board[player_coord[0]][player_coord[1]+1] in SPACES_ALLOWED_TO_MOVE:
        slicing_for_movement(board,player_coord,'.')
        player_coord[1] += 1
        slicing_for_movement(board,player_coord,PLAYER_SYMBOL)
    elif board[player_coord[0]][player_coord[1]+1] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = '.'
        player_coord[1] +=1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
        #print(INVENTORY)

def move_up(board, player_coord):
    if board[player_coord[0]-1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE:
        slicing_for_movement(board,player_coord,'.')
        player_coord[0] +=-1
        slicing_for_movement(board,player_coord,PLAYER_SYMBOL)
    elif board[player_coord[0]-1][player_coord[1]] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = '.'
        player_coord[0] +=-1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
        #print(INVENTORY)

def move_down(board, player_coord):
    if board[player_coord[0]+1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE:
        slicing_for_movement(board,player_coord,'.')
        player_coord[0] +=1
        slicing_for_movement(board,player_coord,PLAYER_SYMBOL)
    elif board[player_coord[0]+1][player_coord[1]] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = '.'
        player_coord[0] +=1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
        #print(INVENTORY)



def display(board):
    for line in board:
        print(*line)

board = [['O' for _ in range(10)] for _ in range(10)]
for x in range(10):
    board[x][0] = '#'
    board[x][9] = '#'
    board[0][x] = '#'
    board[9][x] = '#'
board[3][5] = 'k'


player_starting_coord = [3,3]
board[player_starting_coord[0]][player_starting_coord[1]] = PLAYER_SYMBOL
player_coord = player_starting_coord

# display(board)
# my_key = util.key_pressed()
# while my_key != 'q':
#     if my_key == 'd':
#         util.clear_screen()
#         move_right(board, player_coord)
#         display(board)
#         my_key = util.key_pressed()
#     if my_key == 'a':
#         util.clear_screen()
#         move_left(board, player_coord)
#         display(board)
#         my_key = util.key_pressed()
#     if my_key == 's':
#         util.clear_screen()
#         move_down(board, player_coord)
#         display(board)
#         my_key = util.key_pressed()
#     if my_key == 'w':
#         util.clear_screen()
#         move_up(board, player_coord)
#         display(board)
#         my_key = util.key_pressed()
    

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



def delete_from_inventory(inventory, item):
    inventory = INVENTORY
    inventory[item] -= 1
    return inventory


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
