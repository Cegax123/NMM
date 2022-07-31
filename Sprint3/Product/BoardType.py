import pygame
from button import Button
from text import Text
from BoardVariant import BoardVariant

class MenuModeType:
    def __init__(self, surface):
        self.surface = surface
        #load button images
        self.three_img = pygame.image.load("images/three_img.png").convert_alpha()
        self.nine_img = pygame.image.load("images/nine_img.png").convert_alpha()
        self.five_img = pygame.image.load("images/five_img.png").convert_alpha()

        #creat button instances
        want_width = 266
        want_hight = 340
        self.three_img = pygame.transform.scale(self.three_img, (want_width, want_hight))
        self.nine_img = pygame.transform.scale(self.nine_img, (want_width, want_hight))
        self.five_img = pygame.transform.scale(self.five_img, (want_width, want_hight))

        want_dow = 250
        self.three_button = Button(100,want_dow,self.three_img,1)
        self.nine_button = Button(466,want_dow,self.nine_img,1)
        self.five_button = Button(832,want_dow,self.five_img,1)
        self.selected_mode = None
        self.text1 = Text("Three men",60,'arialblack',(10,110,168))
        self.text2 = Text("Nine men",60,'arialblack',(10,110,168))
        self.text3 = Text("Five men",60,'arialblack',(10,110,168))


    def draw(self):
        #Text
        self.text1.draw(90,100,self.surface)
        self.text2.draw(466,100,self.surface)
        self.text3.draw(832,100,self.surface)

        #Butoons
        self.three_button.draw(self.surface)
        self.nine_button.draw(self.surface)
        self.five_button.draw(self.surface)

    def check_click(self,mose_pos):
        if self.three_button.is_clicked(mose_pos):
            return BoardVariant.THREE_MEN_MORRIS
        elif self.nine_button.is_clicked(mose_pos):
            return BoardVariant.NINE_MEN_MORRIS
        elif self.five_button.is_clicked(mose_pos):
            return BoardVariant.FIVE_MEN_MORRIS
        return None
