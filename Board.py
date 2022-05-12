import json
import pygame

with open('conf.json') as f:
    options = json.load(f)

    screen_options = options['screen']
    board_options = options['board']

    screen_width = screen_options['width']
    screen_height = screen_options['height']

    f.close()


class Board:
    def __init__(self, WIN, N : int, V, E):
        self.WIN = WIN
        self.N = N
        self.E = E

        self.V = []

        for v in V:
            self.V.append(Cell(WIN, N, (v[0], v[1])))

    # Draw board
    def draw(self):
        for v in self.V:
            v.draw()
        
        for e in self.E:
            pygame.draw.line(self.WIN, board_options['edge_color'], self.V[e[0]].screen, self.V[e[1]].screen)

    # Insert a piece in the board
    def insert_piece(self, player, mouse_pos):
        pass

class Cell:
    def __init__(self, WIN, N : int, pos : tuple):
        self.pos = pos
        self.WIN = WIN

        self.MARGIN_X = board_options['margin_x']
        self.MARGIN_Y = board_options['margin_y']
        self.COLOR = board_options['cell_color']
        self.radius = board_options['radius_empty_cell']

        assert(screen_width - 2 * self.MARGIN_X == screen_height - 2 * self.MARGIN_Y)

        self.LEN_BOARD = screen_width - 2 * self.MARGIN_X
        self.LEN_EDGE = self.LEN_BOARD // (N-1)

        self.board_x, self.board_y = self.pos
        self.status = 0

        self.screen_x = self.MARGIN_X + self.LEN_EDGE * self.board_x
        self.screen_y = self.MARGIN_Y + self.LEN_EDGE * self.board_y

        self.screen = (self.screen_x, self.screen_y)

    def draw(self):
        pygame.draw.circle(self.WIN, self.COLOR, (self.screen_x, self.screen_y), self.radius)

    def clicked(self, mouse_pos):
        pass

    def set_status(self, new_status):
        self.status = new_status

