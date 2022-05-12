import json

with open('conf.json') as f:
    options = json.load(f)
    board_options = options['board']
    f.close()

class Player:
    def __init__(self, piece_color, order, remain_pieces):
        self.piece_color = piece_color
        self.remain_pieces = remain_pieces
        self.order = order
