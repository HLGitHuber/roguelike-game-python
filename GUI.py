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
PANEL_HEIGHT = 200

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
    
    text = 'This is the text_box\n'
    text_box = pygame_gui.elements.UITextBox(text,
                                             relative_rect= pygame.Rect(-3,-3,window_size[0],PANEL_HEIGHT),
                                             container=uipanel,
                                             manager=manager)
    
    # name_input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0, 0), (300, 30)),
    #                                                      placeholder_text='Enter your name',
    #                                                      manager=manager,
    #                                                      container=uipanel,
    #                                                      anchors={'centerx': 'centerx',
    #                                                               'centery': 'centery'})    
    player = create_player()
    board = read_table_from_file('maps/map0.txt')
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
        #statistics = f'HP {entities.player.health} / {entities.player.maxhealth}'
        pygame.draw.rect(background,(0,0,50),(0,0,window_size[0],window_size[1]))
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
                else:
                    pygame.draw.rect(background,(125,40,90),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
                left += BLOCK_WIDTH
            top += BLOCK_HEIGHT
    
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            #character movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    engine.move_left(board,player_coord)
                    text = 'You moved left\n'
                    text_box.append_html_text(text)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    engine.move_right(board,player_coord)
                    text = 'You moved right\n'
                    text_box.append_html_text(text)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    engine.move_up(board,player_coord)
                    text = 'You moved up\n'
                    text_box.append_html_text(text)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    engine.move_down(board,player_coord)
                    text = 'You moved down\n'
                    text_box.append_html_text(text)
            
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
        
        
if __name__ == '__main__':
    main()