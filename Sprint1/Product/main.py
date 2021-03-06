import pygame
import json
from Game import Game

with open('../Product/conf.json') as f:
    data = json.load(f)
    screen_options = data['screen']
    board_options = data['board']
    f.close()

WIDTH, HEIGHT = screen_options['width'], screen_options['height']
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nine Men's Morris Game")


def main():
    game = Game('nine', None, None, None, board_options['first_color'], board_options['second_color'] )

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.make_move(pygame.mouse.get_pos())
        WIN.fill((screen_options['color']))
        game.draw(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
