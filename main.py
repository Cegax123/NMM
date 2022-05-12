import pygame
import json
from Game import Game

with open('conf.json') as f:
    screen_options = json.load(f)['screen']
    f.close()

WIDTH, HEIGHT = screen_options['width'], screen_options['height']
SCREEN_COLOR = screen_options['color']

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    run = True


    game = Game(WIN, "six", "white", "black")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            

        WIN.fill(SCREEN_COLOR)
        game.board.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
