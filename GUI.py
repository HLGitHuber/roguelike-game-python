import util
import engine
import pygame
import pygame_gui
import entities

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20
BLOCK_WIDTH = 40
BLOCK_HEIGHT = 40
PANEL_HEIGHT = 240

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        'player_symbol' : '@',
        'player_cord' :[5, 5]
    }
    return player

def read_table_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [ *(element.replace("\n", "") for element in lines)]
    except IOError:
        return []

def create_inventory():
    inventory= { 
    "keys": 0,
    "weapon" : 0,
    "armor" : 0,
    "medicine" : 2
    }
    return inventory

'''
0 - podłoga
1 - ziemia
2 - trawa
3 - żwir
4 - most
5 - lawa
6 - woda
7 - ściana
8 - dziura
9 - brama

mobki TODO
R W G D B T

RGB:
6 = 155, 194, 230
8 = 38, 38, 38
5 = 128, 0, 0
4 = 128, 96, 0
3 = 197, 197, 197
2 = 169, 208, 142
1 = 191, 143, 0
0 = 128, 128, 128
7 = 70, 0, 0
9 = 112, 48, 160
'''

def paint_board(board,background,top_player,left_player,player_coord,window_size):
    color_of_outside = (0,0,0)
    if board[0][0] == '6':
        color_of_outside = (155, 194, 230)
    elif board[0][0] == '5':
        color_of_outside = (128, 0, 0)
    pygame.draw.rect(background,color_of_outside,(0,0,window_size[0],window_size[1]))
    top = top_player - (int(player_coord[0])*BLOCK_HEIGHT)
    for row in board:
        left = left_player - (int(player_coord[1])*BLOCK_WIDTH)
        for element in row:
            if element == '#':
                pygame.draw.rect(background,(0,0,255),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == 'G':
                pygame.draw.rect(background,(0,255,100),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '@':
                pygame.draw.rect(background,(255,0,0),(left_player,top_player,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '6':
                pygame.draw.rect(background,(155, 194, 230),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '8':
                pygame.draw.rect(background,(38, 38, 38),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '5':
                pygame.draw.rect(background,(128, 0, 0),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '4':
                pygame.draw.rect(background,(128, 96, 0),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '3':
                pygame.draw.rect(background,(197, 197, 197),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '2':
                pygame.draw.rect(background,(169, 208, 142),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '1':
                pygame.draw.rect(background,(191, 143, 0),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '0':
                pygame.draw.rect(background,(128, 128, 128),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '9':
                pygame.draw.rect(background,(112, 48, 160),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            elif element == '7':
                pygame.draw.rect(background,(70, 0, 0),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            else:
                pygame.draw.rect(background,(0,0,0),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
            left += BLOCK_WIDTH
        top += BLOCK_HEIGHT

def main():
    pygame.init()
    
    pygame.display.set_caption('Fight The Troll')
    
    window_size = (1024,768)
    window_surface = pygame.display.set_mode(window_size)
    background = pygame.Surface(window_size)
    
    manager = pygame_gui.UIManager(window_size)
    
    clock = pygame.time.Clock()
    
    uipanel = pygame_gui.elements.UIPanel(relative_rect= pygame.Rect(-3,-PANEL_HEIGHT-3,window_size[0]+6,PANEL_HEIGHT+6),
                                          manager=manager,
                                          anchors={'bottom': 'bottom'},)
    
    log_panel = pygame_gui.elements.UIPanel(relative_rect= pygame.Rect(0,40,(window_size[0]/4)*3,200),
                                          manager=manager,
                                          container=uipanel,)
                                          
    
    stats_panel = pygame_gui.elements.UIPanel(relative_rect= pygame.Rect(0,0,window_size[0],40),
                                              manager=manager,
                                              container=uipanel,)
    
    inv_panel = pygame_gui.elements.UIPanel(relative_rect= pygame.Rect(-window_size[0]/4,-200,window_size[0]/4,200),
                                              manager=manager,
                                              container=uipanel,
                                              anchors={'bottom':'bottom',
                                                       'right': 'right'})
                                              
                                              
    
    text="""
     ..    ..:::..^~?!        
     7?!!~~~~^^^^~77J~        
     .JY?~^::::::::^77.       
      7?~^~J^:::7J^^~7?.      
     .?7!~!?~^^^~~7~!!77      
     :?7?!!!~~~^~~~~!!?~      
      !J?7!!!!~~~~!!!77~:     
     !!~7!~~^::::::^^~!^!^    
    !7^7?~:.........:~J~:!^   
   ^?^:?7!::.......:^!Y!^^7:  
   77~~7J!~^^^^^^^^~!7Y?!!!.  
   .^~~J?!!!7?!~?7!!!!J^ .    
       :!!!!!!. !!!!!7!       
        """
    text_log = pygame_gui.elements.UITextBox(text,
                                             relative_rect= pygame.Rect(-3,-3,(window_size[0]/4*3),200),
                                             container=log_panel,
                                             manager=manager)
    
    text_inv = pygame_gui.elements.UITextBox(text,
                                             relative_rect= pygame.Rect(-3,-3,window_size[0]/4,200),
                                             container=inv_panel,
                                             manager=manager)
    
    # name_input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0, 0), (300, 30)),
    #                                                      placeholder_text='Enter your name',
    #                                                      manager=manager,
    #                                                      container=uipanel,
    #                                                      anchors={'centerx': 'centerx',
    #                                                               'centery': 'centery'})    
    player = create_player()
    board = read_table_from_file('maps/map2.txt')
    player_coord = player['player_cord']
    engine.put_player_on_board(board,player)
    
    top_player = (window_size[1]-PANEL_HEIGHT-BLOCK_HEIGHT)/2
    left_player = (window_size[0]-BLOCK_WIDTH)/2
    # inventory = create_inventory()
    player_name = ''
    util.clear_screen()
    is_running = True
    while is_running:
        time_delta = clock.tick(60)/1000.0
        
        #statistics = f'HP {entities.Entity} / {entities.player.maxhealth}'
        
        paint_board(board,background,top_player,left_player,player_coord,window_size)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            #character movement
            if board == board2 and player_coord == [0,2]:
                player_coord = [13,35]
                board = board1
            if board == board2 and player_coord == [0,3]:
                player_coord = [13,36]
                board = board1
            if board == board0 and player_coord == [10,32]:
                board = board1
                player_coord = [5,5]
            if board == board1 and player_coord == [15,35]:
                board = board2
                player_coord = [1,2]
            if board == board1 and player_coord == [15,36]:
                board = board2
                player_coord = [1,3]
            if board == board2 and player_coord == [0, 30]:
                board = board3
                player_coord = [3,1]
            if board == board3 and player_coord == [3,0]:
                board = board2
                player_coord = [1,30]
            if board == board3 and player_coord == [30, 3]:
                board = board4
                player_coord = [27,26]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    engine.move_left(board,player_coord)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    engine.move_right(board,player_coord)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    engine.move_up(board,player_coord)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    engine.move_down(board,player_coord)
            
            # if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            #     if event.ui_element == name_input_box:
            #         player_name = event.text
            #         print(player_name)
                    
            manager.process_events(event)
        
        manager.update(time_delta)
        
        window_surface.blit(background, (0,0))
        manager.draw_ui(window_surface)
        
        pygame.display.update()

        # TODO ui.display_inventory(inventory)
        # TODO bottom panel as interface (like inventory) (need to show it somehow :| )
        # TODO testowa walka z bossem (eventy, znikanie mapy i wiekszy log) (smaller font)
        
        
if __name__ == '__main__':
    main()
