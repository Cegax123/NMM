import pygame
import json
from text import Text
from button import Button


with open('../Product/conf.json') as f:
    data = json.load(f)
    screen_options = data['screen']
    board_options = data['board']
    f.close()
WIDTH, HEIGHT = screen_options['width'], screen_options['height']

class MenuIni:
    #load button images
    def __init__(self):

        self.start_img = pygame.image.load('menu_star.png').convert_alpha()
        self.nmm_img = pygame.image.load("images/nmm.png").convert_alpha()

        self.start_img = pygame.transform.scale(self.start_img, (56, 56))
        self.nmm_img = pygame.transform.scale(self.nmm_img,(WIDTH,HEIGHT))
        #creat button instances
        self.start_button = Button(550,600,self.start_img,2)
        self.nmm_rect = self.nmm_img.get_rect(topleft=(0,0))
        
        self.selected_mode = None

    def draw(self,surface):
        surface.blit(self.nmm_img, self.nmm_rect)
        self.start_button.draw(surface)
        text1 = Text("NINE MEN'S MORRIS", 85, 'verdana', (75,43,140))
        text1.draw(200, 150, surface)

    def check_click(self, mouse_pos):
        if self.start_button.is_clicked(mouse_pos):
            return 'start'
        return None