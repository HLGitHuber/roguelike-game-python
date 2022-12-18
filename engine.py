import util
import ui
import entities
import maps.map_controll as mc


saved_tiles = ['1']
SPACES_ALLOWED_TO_MOVE = ['.', '0', '1', '2', '3', '4']
SPACES_WITH_ITEMS = ['k', 'm']
GATES = ['G']
SPACED_BANNED_FROM_MOVING = ['5','6','7']
ENEMIES = ['R', 'W', 'G', 'D', 'B', 'T']
PASSAGE = ['8', '9']
PLAYER_SYMBOL = '@'
INVENTORY = {
    "cheese": 10,
    'meat': 0,
    'pill': 0,
    'fang': 0,
    'shank': 0,
    'blood vial': 0,
    'magic hand': 10,
    'fur needle': 0
}
INVENTORY_DICT = {
    'c': "cheese",
    'm': 'meat',
    'p': 'pill',
    'f': 'fang',
    's': 'shank',
    'b': 'blood vial',
    'h': 'magic hand',
    'n': 'fur needle'
}
BOARD_NO = 0

def create_player():
    player = entities.Entity('player', 0)
    player.location = [5, 5]
    return player


PLAYER = create_player()


def put_player_on_board(board, player):
    cord_1 = 5
    cord_2 = 5
    board[cord_1][cord_2] = player.symbol
    return board

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
                minus_from_inventory(inventory, item)
                return 'used'


def minus_from_inventory(inventory, item):
    inventory[item] -= 1
    name = item.split(" ")
    name.pop(0)
    name = " ".join(name)
    INVENTORY[name] -= 1


def item_action(item,inventory,text_log):
    if item == 'cheese':
        temp_item = '1. '+item
        if inventory[temp_item] == 0:
            text_log.append_html_text(f'You don\'t have any {item}\n')
        else:
            PLAYER.health += 10
            minus_from_inventory(inventory,temp_item)
    elif item == 'meat':
        temp_item = '2. '+item
        if inventory[temp_item] == 0:
            text_log.append_html_text(f'You don\'t have any {item}\n')
        else:
            PLAYER.health += 25
            minus_from_inventory(inventory,temp_item)
    elif item == 'pill':
        temp_item = '3. '+item
        if inventory[temp_item] == 0:
            text_log.append_html_text(f'You don\'t have any {item}\n')
        else:
            PLAYER.str += 1
            minus_from_inventory(inventory,temp_item)
    elif item == 'fang':
        temp_item = '4. '+item
        if inventory[temp_item] == 0:
            text_log.append_html_text(f'You don\'t have any {item}\n')
        else:
            PLAYER.roll += 1
            minus_from_inventory(inventory,temp_item)
    elif item == 'shank':
        temp_item = '5. '+item
        if inventory[temp_item] == 0:
            text_log.append_html_text(f'You don\'t have any {item}\n')
        else:
            PLAYER.roll += 1
            minus_from_inventory(inventory,temp_item)
    elif item == 'blood vial':
        temp_item = '6. '+item
        if inventory[temp_item] == 0:
            text_log.append_html_text(f'You don\'t have any {item}\n')
        else:
            PLAYER.str += 1
            PLAYER.roll += 1
            minus_from_inventory(inventory,temp_item)
    elif item == 'fur needle':
        temp_item = '8. '+item
        if inventory[temp_item] == 0:
            text_log.append_html_text(f'You don\'t have any {item}\n')
        else:
            PLAYER.roll += 2
            minus_from_inventory(inventory,temp_item)
    elif item == 'magic hand':
        temp_item = '7. '+item
        if inventory[temp_item] == 0:
            text_log.append_html_text(f'You don\'t have any {item}\n')
        else:
            PLAYER.dice += 2
            minus_from_inventory(inventory,temp_item)
    if PLAYER.health > PLAYER.maxhealth:
        PLAYER.health = PLAYER.maxhealth


def move_left(board, player_coord, org_board, text_log, noclip):
    if board[player_coord[0]][player_coord[1]-1] in SPACES_ALLOWED_TO_MOVE and noclip is False:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[1] -= 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]-1] in SPACES_ALLOWED_TO_MOVE+SPACED_BANNED_FROM_MOVING and noclip is True:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[1] -= 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]-1] in PASSAGE:
        player_coord[1] += - 1
    elif board[player_coord[0]][player_coord[1]-1] in ENEMIES:
        message = attack_monster([player_coord[0],player_coord[1]-1], BOARD_NO)
        try:
            if message.split(" ")[-1] == 'killed\n':
                board[player_coord[0]][player_coord[1]-1] = org_board[player_coord[0]][player_coord[1]-1]
                text_log.append_html_text(message)
            else:
                message2 = attack_player([player_coord[0],player_coord[1]-1], BOARD_NO)
                text_log.append_html_text(message2)
        except AttributeError:
            pass



def move_right(board, player_coord, org_board, text_log, noclip):
    if board[player_coord[0]][player_coord[1]+1] in SPACES_ALLOWED_TO_MOVE and noclip is False:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[1] += 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]+1] in SPACES_ALLOWED_TO_MOVE+SPACED_BANNED_FROM_MOVING and noclip is True:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[1] += 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]][player_coord[1]+1] in PASSAGE:
        player_coord[1] += 1
    elif board[player_coord[0]][player_coord[1]+1] in ENEMIES:
        message = attack_monster([player_coord[0],player_coord[1]+1], BOARD_NO)
        try:
            if message.split(" ")[-1] == 'killed\n':
                board[player_coord[0]][player_coord[1]+1] = org_board[player_coord[0]][player_coord[1]+1]
                text_log.append_html_text(message)
            else:
                message2 = attack_player([player_coord[0],player_coord[1]+1], BOARD_NO)
                text_log.append_html_text(message2)
        except AttributeError:
            pass



def move_up(board, player_coord, org_board, text_log, noclip):
    if board[player_coord[0]-1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE and noclip is False:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[0] += -1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]-1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE+SPACED_BANNED_FROM_MOVING and noclip is True:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[0] += -1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]-1][player_coord[1]] in PASSAGE:
        player_coord[0] += -1
    elif board[player_coord[0]-1][player_coord[1]] in ENEMIES:
        message = attack_monster([player_coord[0]-1,player_coord[1]], BOARD_NO)
        try:
            if message.split(" ")[-1] == 'killed\n':
                board[player_coord[0]-1][player_coord[1]] = org_board[player_coord[0]-1][player_coord[1]]
                text_log.append_html_text(message)
            else:
                message2 = attack_player([player_coord[0]-1,player_coord[1]], BOARD_NO)
                text_log.append_html_text(message2)
        except AttributeError:
            pass



def move_down(board, player_coord, org_board, text_log, noclip):
    if board[player_coord[0]+1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE and noclip is False:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[0] += 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]+1][player_coord[1]] in SPACES_ALLOWED_TO_MOVE+SPACED_BANNED_FROM_MOVING and noclip is True:
        board[player_coord[0]][player_coord[1]] = org_board[player_coord[0]][player_coord[1]]
        player_coord[0] += 1
        board[player_coord[0]][player_coord[1]] = PLAYER_SYMBOL
    elif board[player_coord[0]+1][player_coord[1]] in PASSAGE:
        player_coord[0] += 1
    elif board[player_coord[0]+1][player_coord[1]] in ENEMIES:
        message = attack_monster([player_coord[0]+1,player_coord[1]], BOARD_NO)
        try:
            if message.split(" ")[-1] == 'killed\n':
                board[player_coord[0]+1][player_coord[1]] = org_board[player_coord[0]+1][player_coord[1]]
                text_log.append_html_text(message)
            else:
                message2 = attack_player([player_coord[0]+1,player_coord[1]], BOARD_NO)
                text_log.append_html_text(message2)
        except AttributeError:
            pass

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
    character = entities.Entity(table[0])
    return character


def attack_monster(coords: list[int], map_index: int):
    enemy = mc.enemies[map_index][mc.find_enemy(coords, map_index)]
    message = enemy.recieve_damage(mc.enemies[map_index], PLAYER.deal_damage(), map_index)
    return message


def attack_player(coords: list[int], map_index: int):
    enemy = mc.enemies[map_index][mc.find_enemy(coords, map_index)]
    message = PLAYER.player_recieve_damage(enemy.deal_damage())
    return message

def item_from_enemy(enemy_loot, enemy_location, board):
    board[enemy_location] = enemy_loot
    return board[enemy_location]
    




    