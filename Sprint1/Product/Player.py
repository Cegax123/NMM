class Player:
    def __init__(self, name, turn, color_piece, pieces_to_insert):
        self.name = name
        self.turn = turn
        self.color_piece = color_piece
        self.pieces_in_board = 0
        self.pieces_to_insert = pieces_to_insert

        self.status = 'insert'  # 'move', 'fly'
        self.winner = False

    def get_message_in_screen(self):
        if self.status == 'insert':
            return 'Piezas restantes a insertar: ' + str(self.pieces_to_insert)
        elif self.status == 'move':
            return 'Mueve una pieza a una casilla vacia adyacente'
        else:
            return 'Mueve una pieza a cualquier casilla vacia'

    def insert_piece(self):
        self.pieces_to_insert -= 1
        self.pieces_in_board += 1
        if(self.pieces_to_insert == 0):
            self.status = 'move'