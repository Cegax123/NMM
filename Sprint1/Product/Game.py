from Board import Board
from Player import Player

class Game:
    def __init__(self, type_board, type_game, name1, name2, color1, color2):
        V = None # Cargamos los valores de V de conf
        E = None # Cargamos los valores de E de conf

        N = None # Setteamos el valor de N segun type_board

        self.board = Board(N, V, E)
        self.players = []
        self.current = 0
        self.other = 1
        self.winner = None

        self.mode = 'insert' # 'to_select', 'selected', 'to_remove'

    def make_move(self, pos_mouse):

        if self.mode == 'insert':
            result = self.board.insert_piece(self.players[self.turn_number], pos_mouse)
            self.players[self.turn_number].insert_piece()

            if not result['valid']:
                return

            if result['created_mill']:
                self.board.mode = 'to_remove'
            else:
                self.turn_number = self.turn_number ^ 1
                if not self.players[self.turn_number].status == 'insert':
                    self.board.mode = 'to_move'

        elif self.mode == 'to_remove':
            result = self.board.remove_piece(self.players[self.turn_number], pos_mouse)


    def draw(self):
        # Dibujar otros aspectos del juego (como el nombre del jugador actual

        

        # Draw board
        self.board.draw()
