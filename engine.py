from entities import Entity
import util
import ui
saved_tiles =['1']
SPACES_ALLOWED_TO_MOVE = ['.', '0', '1', '2', '3', '4']
SPACES_WITH_ITEMS = ['k', 'm']
GATES = ['G']
SPACED_BANNED_FROM_MOVING = ''
PASSAGE = ['8', '9']
PLAYER_SYMBOL = '@'
INVENTORY = {
    "keys": 0,
    "cheese" : 2,
    'meat': 0,
    'pill': 0,
    'fang': 1,
    'shank': 0,
    'blood vial': 0,
    'magic hand' : 0,
    'fur needle': 0
}
INVENTORY_DICT = {
    'k' : 'keys',
    'c': "cheese", 
    'm': 'meat',
    'p': 'pill',
    'f': 'fang',
    's': 'shank',
    'b': 'blood vial',
    'h': 'magic hand',
    'n': 'fur needle'
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
    cord_1 = 5
    cord_2 = 5
    board[cord_1][ cord_2] = player['player_symbol']
    return board


def add_to_inventory(inventory, item):
    print('You have found a ', item)
    inventory[item] += 1
    return inventory

def use_item(inventory):
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
                item_action(item)
                delete_from_inventory(inventory, item)
                return 'used'

def delete_from_inventory(inventory, item):
    inventory = INVENTORY
    inventory[item] -= 1
    return inventory


def item_action(item):
    data = open('enemy_template.txt').read().splitlines()
    table = data[1].split(';')
    
    if item == 'cheese':
        hp = int(table[3])
        hp+=10
        table[3] = str(hp)
    elif item == 'meat':
        hp = int(table[3])
        hp+=25
        table[3] = str(hp)
    elif item == 'pill':
        strength = int(table[5])
        strength+=1
        table[5] = str(strength)
    elif item == 'fang' or 'shank':
        rolls = int(table[7])
        rolls+=1
        table[7] = str(rolls)
    elif item == 'blood vial':
        strength = int(table[5])
        strength+=1
        table[5] = str(strength)
        rolls = int(table[7])
        rolls+=1
        table[7] = str(rolls)
    elif item == 'fur needle':
        rolls = int(table[7])
        rolls+=2
        table[7] = str(rolls)
    elif item == 'magic hand':
        dices = int(table[6])
        dices+=2
        table[6] = str(dices)

    data[1] = ';'.join(table)
    with open('enemy_template.txt', 'w') as file:
        for element in data:
            file.write(element + "\n")


def move_left(board, player_coord):
    if board[player_coord[0]][player_coord[1]-1] in SPACES_ALLOWED_TO_MOVE:
        global saved_tiles
        board[player_coord[0]][player_coord[1]] = saved_tiles
        player_coord[1] -=1
        saved_tiles = board[player_coord[0]][player_coord[1]]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]-1] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] +=-1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
    elif board[player_coord[0]][player_coord[1]-1] in PASSAGE:
        player_coord[1] +=- 1

def move_right(board, player_coord):
    if board[player_coord[0]][player_coord[1]+1] in SPACES_ALLOWED_TO_MOVE:
        global saved_tiles
        board[player_coord[0]][player_coord[1]] = saved_tiles
        player_coord[1] +=1
        saved_tiles = board[player_coord[0]][player_coord[1]]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]+1] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] +=1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
    elif board[player_coord[0]][player_coord[1]+1] in PASSAGE:
        player_coord[1] += 1

def move_up(board, player_coord):
    if board[player_coord[0]-1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE:
        global saved_tiles
        board[player_coord[0]][player_coord[1]] = saved_tiles
        player_coord[0] +=-1
        saved_tiles = board[player_coord[0]][player_coord[1]]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]-1][player_coord[1]] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[0] +=-1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
    elif board[player_coord[0]-1][player_coord[1]] in PASSAGE:
        player_coord[0] +=-1

def move_down(board, player_coord):
    if board[player_coord[0]+1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE:
        global saved_tiles
        board[player_coord[0]][player_coord[1]] = saved_tiles
        player_coord[0] +=1
        saved_tiles = board[player_coord[0]][player_coord[1]]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]+1][player_coord[1]] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[0] +=1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
        # print(INVENTORY)
    elif board[player_coord[0]+1][player_coord[1]] in PASSAGE:
        player_coord[0] +=1


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


player_starting_coord = [3, 3]
board[player_starting_coord[0]][player_starting_coord[1]] = PLAYER_SYMBOL
player_coord = player_starting_coord


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
    

def get_race():
    given_race = ui.ask_for_race()
    human = 'player;@;50;2;5;(0,0);blood;1'
    elph = 'player;@;35;3;4;(0,0);blood;1'
    dwarf = 'player;@;65;1;9;(0,0);blood;1'
    data = open('enemy_template.txt').read().splitlines()
    
    if given_race == 'human':
        data[1] = human
    elif given_race == 'elph':
        data[1] = elph
    elif given_race == 'dwarf':
        data[1] = dwarf
    print(data[1])
    with open('enemy_template.txt', 'w') as file:
        for element in data:
            file.write(element + "\n")

#get_race()




def get_race():
    given_race = ui.ask_for_race()
    human = 'player;@;50;2;5;(0,0);blood;1'
    elph = 'player;@;35;3;4;(0,0);blood;1'
    dwarf = 'player;@;65;1;9;(0,0);blood;1'
    data = open('enemy_template.txt').read().splitlines()
    
    table = data[1].split(';')
    

    character = Entity(table[0])
    print(character.name)
    print(character.health)
    return character


#get_race()




def item_from_enemy(enemy_loot, enemy_location, board):
    board[enemy_location] = enemy_loot
    return board[enemy_location]
    




    