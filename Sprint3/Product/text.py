import pygame
class Text():
    def __init__(self,text,size,letra,colour):
        pygame.init()
        self.text = text
        self.antialias = True
        self.colour = colour
        self.background = None
        self.font = pygame.font.SysFont(letra,size)
        self.img = self.font.render(self.text, self.antialias, self.colour,self.background)
    def draw(self,x,y,surface):
        surface.blit(self.img,(x,y))
