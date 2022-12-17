import util
import ui
from entities import Entity
import maps.map_controll as mc

saved_tiles = ['1']
SPACES_ALLOWED_TO_MOVE = ['.', '0', '1', '2', '3', '4']
SPACES_WITH_ITEMS = ['k', 'm']
GATES = ['G']
SPACED_BANNED_FROM_MOVING = ''
ENEMIES = ['R', 'W', 'G', 'D', 'B', 'T']
PASSAGE = ['8', '9']
PLAYER_SYMBOL = '@'
INVENTORY = {
    "keys": 0,
    "cheese": 2,
    'meat': 0,
    'pill': 0,
    'fang': 1,
    'shank': 0,
    'blood vial': 0,
    'magic hand': 0,
    'fur needle': 0
}
INVENTORY_DICT = {
    'k': 'keys',
    'c': "cheese",
    'm': 'meat',
    'p': 'pill',
    'f': 'fang',
    's': 'shank',
    'b': 'blood vial',
    'h': 'magic hand',
    'n': 'fur needle'
}


def create_player():
    player = Entity('player')
    player.location = [5, 5]
    return player


PLAYER = create_player()


def put_player_on_board(board, player):
    cord_1 = 5
    cord_2 = 5
    board[cord_1][cord_2] = player.symbol
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


def item_action(item):
    if item == 'cheese':
        PLAYER.health += 10
    elif item == 'meat':
        PLAYER.health += 25
    elif item == 'pill':
        PLAYER.str += 1
    elif item in ['fang', 'shank']:
        PLAYER.roll += 1
    elif item == 'blood vial':
        PLAYER.str += 1
        PLAYER.roll += 1
    elif item == 'fur needle':
        PLAYER.roll += 2
    elif item == 'magic hand':
        PLAYER.dice += 2
    if PLAYER.health > PLAYER.maxhealth:
        PLAYER.health = PLAYER.maxhealth


def move_left(board, player_coord, org_board):
    if board[player_coord[0]][player_coord[1]-1] in SPACES_ALLOWED_TO_MOVE:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[1] -= 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]-1] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] += -1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
    elif board[player_coord[0]][player_coord[1]-1] in PASSAGE:
        player_coord[1] += - 1


def move_right(board, player_coord, org_board):
    if board[player_coord[0]][player_coord[1]+1] in SPACES_ALLOWED_TO_MOVE:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[1] += 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]+1] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[1] += 1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
    elif board[player_coord[0]][player_coord[1]+1] in PASSAGE:
        player_coord[1] += 1


def move_up(board, player_coord, org_board):
    if board[player_coord[0]-1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[0] += -1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]-1][player_coord[1]] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[0] += -1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
    elif board[player_coord[0]-1][player_coord[1]] in PASSAGE:
        player_coord[0] += -1


def move_down(board, player_coord, org_board):
    if board[player_coord[0]+1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[0] += 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]+1][player_coord[1]] in SPACES_WITH_ITEMS:
        board[player_coord[0]][player_coord[1]] = 'O'
        player_coord[0] += 1
        item = board[player_coord[0]][player_coord[1]]
        item = INVENTORY_DICT[item]
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
        add_to_inventory(INVENTORY, item)
        # print(INVENTORY)
    elif board[player_coord[0]+1][player_coord[1]] in PASSAGE:
        player_coord[0] += 1


def display(board):
    for line in board:
        print(*line)


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
    elf = 'player;@;35;3;4;(0,0);blood;1'
    dwarf = 'player;@;65;1;9;(0,0);blood;1'
    data = open('enemy_template.txt').read().splitlines()

    table = data[1].split(';')
    character = Entity(table[0])
    return character


def attack_monster(coords: list[int], map_index: int):
    enemy = mc.enemies[map_index][mc.find_enemy(coords, map_index)]
    enemy.recieve_damage(mc.enemies[map_index], PLAYER.deal_damage())


def attack_player(coords: list[int], map_index: int):
    enemy = mc.enemies[map_index][mc.find_enemy(coords, map_index)]
    PLAYER.player_recieve_damage(enemy, enemy.deal_damage())


def item_from_enemy(enemy_loot, enemy_location, board):
    board[enemy_location] = enemy_loot
    return board[enemy_location]
    




    