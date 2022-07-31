import pygame
from button import Button
from text import Text
from PlayerType import PlayerType

class MenuMode:
    def __init__(self, surface):
        self.surface = surface
        #load button images
        self.pvp = pygame.image.load("images/pvp.png").convert_alpha()
        self.pve = pygame.image.load("images/pve.png").convert_alpha()

        #creat button instances
        want_width = 266
        want_hight = 340
        self.pvp = pygame.transform.scale(self.pvp, (want_width, want_hight))
        self.pve = pygame.transform.scale(self.pve, (want_width, want_hight))

        want_dow = 250
        self.pvp_button = Button(290,want_dow,self.pvp,1)
        self.pve_button = Button(732,want_dow,self.pve,1)
        self.selected_mode = None
        self.text1 = Text("CHOOSE GAME MODE",75,'arialblack',(10,110,168))


    def draw(self):
        #Text
        self.text1.draw(280,100,self.surface)

        #Butoons
        self.pvp_button.draw(self.surface)
        self.pve_button.draw(self.surface)

    def check_click(self,mose_pos):
        if self.pvp_button.is_clicked(mose_pos):
            return PlayerType.HUMAN

        elif self.pve_button.is_clicked(mose_pos):
            return PlayerType.BOT

        return None

