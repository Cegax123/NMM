from re import X
from Board import Board
import json
from Player import Player

with open('conf.json') as f:
    game_options = json.load(f)['game']
    f.close()


class Game:
    def __init__(self, type_board, type_game, name1, name2, color1, color2):
        vertices = game_options[type_board + '_vertices']
        edges = game_options[type_board + '_edges']

        n = 0
        
        if type_board == 'nine':
            p = 9
            n = 6
        elif type_board == 'five':
            p = 5
            n = 4
        else:
            p = 3
            n = 2

        self.board = Board(n, vertices, edges)
        self.players = [Player(name1, 1, color1, p), Player(name2, 2, color2, p)]
        self.current = 0
        self.other = 1
        self.winner = None
        self.turn_number = 0

        self.mode = 'insert' # 'to_select', 'selected', 'to_remove'

        

    def make_move(self, pos_mouse):
        if self.mode == 'insert':
            result = self.board.insert_piece(self.players[self.turn_number%2], self.board.get_vertex(pos_mouse))
            if result['valid']:
                self.turn_number += 1
                
        

    def draw(self, surf):
        # Dibujar otros aspectos del juego (como el nombre del jugador actual

        # Draw board
        self.board.draw(surf)
