import pygame
import json
from Game import Game

with open('conf.json') as f:
    data = json.load(f)
    screen_options = data['screen']
    board_options = data['board']
    f.close()

WIDTH, HEIGHT = screen_options['width'], screen_options['height']
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nine Men's Morris Game")


def main():

    game = Game('three', None, None, None, None, None)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill((screen_options['color']))

        game.draw(WIN)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
