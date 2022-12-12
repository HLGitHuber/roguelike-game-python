import util
import engine
import ui


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        'player_symbol' : '@',
        'player_cord_1' : 5,
        'player_cord_2' : 5
    }
    return player



def read_table_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [ *(element.replace("\n", "") for element in lines)]
    except IOError:
        return []


def main():
    player = create_player()
    board = engine.get_board('maps/map0.txt')
    inventory = engine.INVENTORY
    engine.put_player_on_board(board, player)
    util.clear_screen()
    player_starting_coord = [5,5] 
    player_coord = player_starting_coord
    is_running = True
    while is_running:
        
        ui.display_board(board)
        ui.display_inventory(inventory)
    

        my_key = util.key_pressed()
        if my_key == 'q':
            is_running = False
        if my_key == 'd':
            util.clear_screen()
            engine.move_right(board, player_coord)
            ui.display_board(board)
            my_key = util.key_pressed()
        if my_key == 'a':
            util.clear_screen()
            engine.move_left(board, player_coord)
            ui.display_board(board)
            my_key = util.key_pressed()
        if my_key == 's':
            util.clear_screen()
            engine.move_down(board, player_coord)
            ui.display_board(board)
            my_key = util.key_pressed()
        if my_key == 'w':
            util.clear_screen()
            engine.move_up(board, player_coord)
            ui.display_board(board)
            my_key = util.key_pressed()
        util.clear_screen()


if __name__ == '__main__':
    main()

