def display_board(board, color_scheme):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for row in board:
        for element in row:
            try:
                print(color_scheme[element], end = '')
            except KeyError:
                print(element, end='')
        print()

def display_stats(statistics):
    # statistics - dict
    print()
    for key, value in statistics.items():
        print(f'{key}: {value}', end='\t', flush=True)

def display_zone(map_file):
    map_name = map_file.replace('.txt','').replace('maps/', '')
    print(map_name,'\n')