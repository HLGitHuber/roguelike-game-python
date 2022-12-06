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
    pass

def read_table_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [ *(element.replace("\n", "") for element in lines)]
    except IOError:
        return []

def main():
    color_scheme = {        
        '.': ' '
    }
    statistics = {
        'HP': '100',
        'STR': '20'
    }
    
    map_file = 'maps/map2.txt'
    player = create_player()
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = read_table_from_file(map_file)
    
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_zone(map_file)
        ui.display_board(board, color_scheme)
        ui.display_stats(statistics)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
