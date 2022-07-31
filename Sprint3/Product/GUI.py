from Board import IBoard
from PieceColor import PieceColor
import pygame
import Player


class GameRunning:
    def __init__(self, surf, game_state, margin, size):
        self._game_state = game_state
        self._surf = surf

        self._board = game_state.board
        self._rows = self._board.rows
        self._cols = self._board.cols

        self._margin = margin
        self._size = size
        self._side = size // (self._rows - 1)

        self._positions = [[pygame.Rect(0, 0, 0, 0) for _ in range(self._cols)] for _ in range(self._rows)]

        for i in range(self._rows):
            for j in range(self._cols):
                if self._board.valid_position((i, j)):
                    BLOCK = 60
                    self._positions[i][j].size = (BLOCK, BLOCK)
                    self._positions[i][j].center = (self._margin + j * self._side, self._margin + i * self._side)

    def draw(self):
        EDGES_COLOR = (15, 61, 62)

        for v1, v2 in self._board.edges:
            x1, y1 = self._board.positions[v1]
            x2, y2 = self._board.positions[v2]

            pygame.draw.line(self._surf, EDGES_COLOR, self._positions[x1][y1].center, self._positions[x2][y2].center)


        start_pos = self._game_state.current_player.start_pos
        if start_pos != (-1, -1):
            x, y = start_pos
            pygame.draw.circle(self._surf, (129, 202, 207), self._positions[x][y].center, 40)

        for x, y in self._board.positions:

            color = self._board.get_color_from_pos((x, y))

            COLOR_VERTEX = EDGES_COLOR
            RADIUS = 20

            if color == PieceColor.BLACK:
                COLOR_VERTEX = (0, 0, 0)
                RADIUS *= 1.5

            if color == PieceColor.WHITE:
                COLOR_VERTEX = (255, 255, 255)
                RADIUS *= 1.5

            pygame.draw.circle(self._surf, COLOR_VERTEX, self._positions[x][y].center, RADIUS)
            # pygame.draw.rect(self._surf, EDGES_COLOR, self._positions[x][y])

    def get_position_in_board(self, mouse_pos):
        for x, y in self._board.positions:
            if self._positions[x][y].collidepoint(mouse_pos):
                return (x, y)

        return (-1, -1)
