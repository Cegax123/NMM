import json
from Board import Board

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
