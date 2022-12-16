import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        'player_symbol': '@',
        'player_cord': (5, 5)
    }
    return player


def read_table_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [*(element.replace("\n", "") for element in lines)]
    except IOError:
        return []


def create_inventory():
    inventory = {
        "keys": 0,
        "weapon": 0,
        "armor": 0,
        "medicine": 2
    }
    return inventory


def main():
    player = create_player()
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = read_table_from_file('maps/map0.txt')
    inventory = create_inventory()
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        ui.display_inventory(inventory)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
