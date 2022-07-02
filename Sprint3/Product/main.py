import pygame
import json
from menu_ini import MenuIni
from Game import Game
from menu_mode import MenuMode
from text import Text

with open('../Product/conf.json') as f:
    data = json.load(f)
    screen_options = data['screen']
    board_options = data['board']
    f.close()

WIDTH, HEIGHT = screen_options['width'], screen_options['height']
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nine Men's Morris Game")


def main():
    
    current_screen = 'menu_ini'
    menu_ini = MenuIni()
    menu_mode = MenuMode()
    winner = None
    
    run = True
    while run:
        WIN.fill((screen_options['color']))
        
        if current_screen == 'menu_ini' :
            menu_ini.draw(WIN)    
        
        elif current_screen == 'menu_mode':
            menu_mode.draw(WIN)

        elif current_screen == 'game':
            game.draw(WIN)
        
        elif current_screen == 'win_menu':
            Text('winner is ' + winner.name, 20, 'verdana', (75,43,140)).draw(100, 100, WIN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if current_screen == 'menu_ini':
                    button = menu_ini.check_click(mouse_pos)
                    if button == 'start':
                        current_screen = 'menu_mode'

                
                elif current_screen == 'menu_mode':
                    if menu_mode.check_click(mouse_pos):
                        current_screen = 'game'
                        game = Game(menu_mode.selected_mode, None, 'Player 1', 'Player 2', board_options['first_color'], board_options['second_color'] )

                else:
                    game.make_move(pygame.mouse.get_pos())
                    if game.check_winner():
                        current_screen = 'win_menu'
                        winner = game.get_winner()

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
