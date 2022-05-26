import pygame.draw
import json

with open('conf.json') as f:
    options = json.load(f)
    board_options = options['board']

    BOARD_START_X = board_options['start_x']
    BOARD_START_Y = board_options['start_y']
    BOARD_END_X = board_options['end_x']
    BOARD_END_Y = board_options['end_y']

    f.close()


class Vertex:
    def __init__(self, pos_board, side):
        self.pos_board = pos_board
        self.pos_screen = (BOARD_START_X + side * pos_board[0], BOARD_START_Y + side * pos_board[1])
        self.status = 'empty'  # 'black', 'white'

        self.radius = board_options['radius_empty_vertex']

    def draw(self, surf):
        pygame.draw.circle(surf, board_options['vertex_color'], self.pos_screen, self.radius)

    def clicked(self, pos_mouse):
        pass

