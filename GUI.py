import util
import engine
import ui
import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.windows.ui_console_window import UIConsoleWindow

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

def moveTiles(self):
    xmove = self.parent.dt * self.panning[0] * self.panning_speed
    ymove = self.parent.dt * self.panning[1] * self.panning_speed
    for tile in self.game_map:
        tile.x += xmove
        tile.y += ymove
        tile.rect.x = int(tile.x)
        tile.rect.y = int(tile.y)
        tile.pos = (tile.rect.x, tile.rect.y)


def main():
    pygame.init()
    
    pygame.display.set_caption('Fight The Troll')
    
    window_size = (800,600)
    window_surface = pygame.display.set_mode(window_size)
    background = pygame.Surface(window_size)
    
    manager = pygame_gui.UIManager(window_size)
    
    clock = pygame.time.Clock()
    
    uipanel = pygame_gui.elements.UIPanel(relative_rect= pygame.Rect(0,400,800,200),
                                          manager=manager)
    
    name_input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0, 0), (300, 30)),
                                                         placeholder_text='Enter your name',
                                                         manager=manager,
                                                         container=uipanel,
                                                         anchors={'centerx': 'centerx',
                                                                  'centery': 'centery'})    
    player = create_player()
    board = read_table_from_file('roguelike-game-python-AdamNowicki22/maps/map0.txt')
    # TODO: usunac pierwszy path
    
    BLOCK_WIDTH = 20
    BLOCK_HEIGHT = 40
    
    #test putting player on board
    player_coord = player['player_cord']
    
    
    
    # inventory = create_inventory()
    player_name = ''
    util.clear_screen()
    is_running = True
    while is_running:
        time_delta = clock.tick(60)/1000.0
        concatenation = player_coord[1]+1
        board[player_coord[0]] = board[player_coord[0]][:player_coord[1]] +'@'+ board[player_coord[0]][concatenation:]
    
        top = 0
        for row in board:
            left = 0
            for element in row:
                if element == '#':
                    pygame.draw.rect(background,(0,0,255),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
                elif element == 'G':
                    pygame.draw.rect(background,(0,255,100),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
                elif element == '@':
                    pygame.draw.rect(background,(0,0,0),(left,top,BLOCK_WIDTH,BLOCK_HEIGHT))
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
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    engine.move_right(board,player_coord)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    engine.move_up(board,player_coord)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    engine.move_down(board,player_coord)
                
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == name_input_box:
                    player_name = event.text
                    print(player_name)
                    
            manager.process_events(event)
        
        manager.update(time_delta)
        
        window_surface.blit(background, (0,0))
        manager.draw_ui(window_surface)
        
        pygame.display.update()

        # TODO ui.display_inventory(inventory)
        # TODO Panning for map (cuz map too big for screen) TODO maybe put it on another pannel?
        # TODO maybe logs on right?
        # TODO bottom panel as interface (like inventory) (need to show it somehow :| )
        
        
if __name__ == '__main__':
    main()