import pygame.draw
import json

with open('../Product/conf.json') as f:
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
        self.status = 0  # 'empty'  # 'black', 'white'
        self.color = board_options['vertex_color']
        self.radius = board_options['radius_empty_vertex']

    def draw(self, surf):
        if self.status == 0:
            scale = 1
        else:
            scale = 2
        pygame.draw.circle(surf, self.color, self.pos_screen, self.radius*scale)

    def clicked(self, pos_mouse):
        mx,my = pos_mouse
        px,py = self.pos_screen
        return (py-my)*(py-my) + (px-mx)*(px-mx) < 4*self.radius*self.radius

    def update(self, player = None):
        if player:
            self.status = player.turn
            self.color = player.color_piece
        else:
            self.status = 0
            self.color = board_options['vertex_color']
        

