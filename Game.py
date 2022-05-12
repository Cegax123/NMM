import json
from Board import Board
from Player import Player

with open('conf.json') as f:
    options = json.load(f)

    board_options = options['board']


    f.close()

class Game:
    def __init__(self, WIN, TYPE_BOARD : str, COLOR1 : str, COLOR2 : str):
        with open('conf.json') as f:
            data = json.load(f)
            V = data['game'][TYPE_BOARD + '_cell']
            E = data['game'][TYPE_BOARD + '_edge']
            
        N = 7
        if TYPE_BOARD == 'six':
            N = 5

        self.board = Board(WIN, N, V, E)
        
        self.turn_number=0
        self.players = []
        self.players.append(Player(board_options[COLOR1],1,9))
        self.players.append(Player(board_options[COLOR2],2,9))
    def turn_player(self):
        return self.players[self.turn_number%2]
    def move_insert_piece(self,mouse_pos):
        if self.turn_player().remain_pieces>0:
            if self.board.insert_piece(self.turn_player(),mouse_pos):
                self.turn_player().remain_pieces-=1
                self.turn_number+=1

