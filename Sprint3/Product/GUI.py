from Board import IBoard
from PieceColor import PieceColor
import pygame
from text import Text
from State import MoveHandler
from PlayerState import PlayerState
import Player


class GameRunning:
    def __init__(self, surf, game_state, margin, size):
        self._game_state = game_state
        self._surf = surf

        self._board = game_state.board
        self._rows = self._board.rows
        self._cols = self._board.cols

        self._margin_x, self._margin_y = margin
        self._size = size
        self._side = size // (self._rows - 1)

        self._positions = [[pygame.Rect(0, 0, 0, 0) for _ in range(self._cols)] for _ in range(self._rows)]

        for i in range(self._rows):
            for j in range(self._cols):
                if self._board.valid_position((i, j)):
                    BLOCK = 60
                    self._positions[i][j].size = (BLOCK, BLOCK)
                    self._positions[i][j].center = (self._margin_x + j * self._side, self._margin_y + i * self._side)

    def draw(self):
        move_handler = MoveHandler()
        EDGES_COLOR = (15, 61, 62)

        for v1, v2 in self._board.edges:
            x1, y1 = self._board.positions[v1]
            x2, y2 = self._board.positions[v2]

            pygame.draw.line(self._surf, EDGES_COLOR, self._positions[x1][y1].center, self._positions[x2][y2].center)


        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(self._rows+1):
            Text(str(i+1), 40, 'verdana', [0, 0, 0]).draw(self._margin_x-60, self._margin_y + self._size - i * self._side-25, self._surf)
            Text(alpha[i], 40, 'verdana', [0, 0, 0]).draw(self._margin_x + self._side * i-12, self._margin_y+self._size+30, self._surf)



        possible_moves = move_handler.get_possible_moves(self._game_state)
        current_state = self._game_state.current_player.state
        start_pos = self._game_state.current_player.start_pos

        for x, y in self._board.positions:
            color = self._board.get_color_from_pos((x, y))

            COLOR_VERTEX = EDGES_COLOR
            REMOVE_COLOR = (223, 120, 97)
            MOVE_COLOR = (0, 150, 255)
            RADIUS = 20

            if color == PieceColor.BLACK:
                COLOR_VERTEX = (0, 0, 0)
                RADIUS *= 1.5

            if color == PieceColor.WHITE:
                COLOR_VERTEX = (255, 255, 255)
                RADIUS *= 1.5

            if self._game_state.current_player.start_selected() and (x,y) == start_pos:
                pygame.draw.circle(self._surf, (129, 202, 207), self._positions[x][y].center, RADIUS * 1.3)

            if self._game_state.current_player.state == PlayerState.REMOVE:
                if (x, y) in possible_moves:
                    pygame.draw.circle(self._surf, REMOVE_COLOR, self._positions[x][y].center, RADIUS * 1.2)

            if current_state == PlayerState.MOVE or current_state == PlayerState.FLY:
                if self._game_state.current_player.start_selected():
                    if (x, y) in possible_moves and color != self._game_state.current_player.color:
                        pygame.draw.circle(self._surf, MOVE_COLOR, self._positions[x][y].center, RADIUS * 1.2)
                else:
                    if (x, y) in possible_moves and color:
                        pygame.draw.circle(self._surf, MOVE_COLOR, self._positions[x][y].center, RADIUS * 1.1)

            pygame.draw.circle(self._surf, COLOR_VERTEX, self._positions[x][y].center, RADIUS)

            if self._game_state.winner:
                text = Text(self._game_state.name_winner + " won!!", 20, 'arialblack', (0, 0, 0))
                text.draw(200, 0, self._surf)



            # pygame.draw.rect(self._surf, EDGES_COLOR, self._positions[x][y])

    def get_position_in_board(self, mouse_pos):
        for x, y in self._board.positions:
            if self._positions[x][y].collidepoint(mouse_pos):
                return (x, y)

        return (-1, -1)
