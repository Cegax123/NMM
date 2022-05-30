from re import X
from Board import Board
import json
from Player import Player

with open('../Product/conf.json') as f:
    game_options = json.load(f)['game']
    f.close()


class Game:
    def __init__(self, type_board, type_game, name1, name2, color1, color2):
        vertices = game_options[type_board + '_vertices']
        edges = game_options[type_board + '_edges']

        self.n = 0

        if type_board == 'nine':
            p = 9
            self.n = 6
            threshold_fly = 3
        elif type_board == 'five':
            p = 5
            self.n = 4
            threshold_fly = 0
        else:
            p = 3
            self.n = 2
            threshold_fly = 0


        self.board = Board(self.n, vertices, edges)
        self.players = [Player(name1, 1, color1, p, threshold_fly), Player(name2, 2, color2, p, threshold_fly)]
        self.winner = None
        self.turn_number = 0

        self.mode = 'insert' # 'to_select', 'selected', 'to_remove'

    def current_player(self):
        return self.players[self.turn_number%2]

    def other_player(self):
        return self.players[(self.turn_number+1)%2]

    def make_move(self, pos_mouse):
        id_vertex = self.board.get_vertex(pos_mouse)
        if id_vertex == -1: return

        if self.current_player().status == 'insert':
            change_turn = self.board.insert_piece(self.current_player(), id_vertex)
            if change_turn:
                self.turn_number+=1
        elif self.current_player().status == 'select':
            self.board.select_piece(self.current_player(), id_vertex)
        elif self.current_player().status == 'move':
            change_turn = self.board.move_piece(self.current_player(), id_vertex)
            if change_turn:
                self.turn_number += 1
        elif self.current_player().status == 'fly':
            change_turn = self.board.fly_piece(self.current_player(), id_vertex)
            if change_turn:
                self.turn_number += 1
        elif self.current_player().status == 'remove':
            change_turn = self.board.remove_piece(self.current_player(), self.other_player(), id_vertex)
            if change_turn:
                self.turn_number += 1

        self.board.update_border_vertex(self.current_player())

    def check_winner(self):
        return self.players[0].lost_game() or self.players[1].lost_game()

    def get_winner(self):
        if self.players[0].lost_game():
            return self.players[1]
        else:
            return self.players[0]

    def draw(self, surf):
        # Dibujar otros aspectos del juego (como el nombre del jugador actual
        
        # Draw board
        self.board.draw(surf)
