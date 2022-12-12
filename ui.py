import util

COLOR_SCHEME = {        
        '.': ' ',                                       # puste pola
        '#': '\033[0;34;40m'u'\u2551''\033[0;37;40m',   # sciany boczne
        '_': '\033[0;34;40m'u'\u2550''\033[0;37;40m',   # sciany gorne/dolne
        '[': '\033[0;34;40m'u'\u2554''\033[0;37;40m',   # lewy gorny rog
        ']': '\033[0;34;40m'u'\u2557''\033[0;37;40m',   # prawy gorny rog
        '\\': '\033[0;34;40m'u'\u255A''\033[0;37;40m',  # lewy dolny rog
        '/': '\033[0;34;40m'u'\u255D''\033[0;37;40m',   # prawy dolny rog
        'T': "\033[0;32;40m,\033[0;37;40m",             # drzewa
    }


def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for row in board:
        for element in row:
            try:
                print(COLOR_SCHEME[element], end = '')
            except:
                print(element, end='')
        print()

def display_inventory(inventory):
    for item in inventory :
        print(item, ": ", inventory[item])


def ask_for_using(item):
    print('Do you want to use one of your ', item, "? Confirm by c")
    my_key = util.key_pressed()
    if my_key == 'c':
        return True
    
