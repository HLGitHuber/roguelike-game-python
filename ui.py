
def display_board(board, color_scheme):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    # row_count = 0
    # element_count = 0
    for row in board:
        for element in row:
            try:
                '''
                try:
                    if board[row_count+1][element_count] == '#' and row[element_count+1] == '#':
                        temp = color_scheme[element]
                        temp= '\033[0;34;40m'u'\u2554''\033[0;37;40m'
                        print(temp, end='')
                    if board[row_count+1][element_count] == '#' and row[element_count-1] == '#':
                        temp = color_scheme[element]
                        temp= '\033[0;34;40m'u'\u2557''\033[0;37;40m'
                        print(temp, end='')
                    if board[row_count-1][element_count] == '#' and row[element_count+1] == '#':
                        temp = color_scheme[element]
                        temp= '\033[0;34;40m'u'\u255A''\033[0;37;40m'
                        print(temp, end='')
                    if board[row_count-1][element_count] != '#' and board[row_count+1][element_count] != '#':
                        temp = color_scheme[element]
                        temp= '\033[0;34;40m'u'\u2550''\033[0;37;40m'
                        print(temp, end='')
                    if row[element_count-1] != '#' and row[element_count+1] != '#':
                        temp = color_scheme[element]
                        temp= '\033[0;34;40m'u'\u2551''\033[0;37;40m'
                        print(temp, end='')
                except:
                '''
                print(color_scheme[element], end = '')
                
            except KeyError:
                print(element, end='')
            # element_count += 1
        print()
        # row_count += 1

def display_stats(statistics):
    # statistics - dict
    print()
    for key, value in statistics.items():
        print(f'{key}: {value}', end='\t', flush=True)

def display_zone(map_file):
    #map_file - string, directory of the map
    map_name = map_file.replace('.txt','').replace('maps/', '')
    print(map_name,'\n')