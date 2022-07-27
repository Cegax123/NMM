class Player:
    def __init__(self, name, turn, color_piece, pieces_to_insert, threshold_fly):
        self.name = name
        self.turn = turn
        self.color_piece = color_piece
        self.pieces_in_board = 0
        self.pieces_to_insert = pieces_to_insert
        self.threshold_fly = threshold_fly
        self.selected_id = None

        self.status = 'insert'  # 'select', 'move', 'fly' , 'remove' 
        self.winner = False

    def get_message_in_screen(self):
        if self.status == 'insert':
            return 'Piezas restantes a insertar: ' + str(self.pieces_to_insert)
        elif self.status == 'move':
            return 'Mueve una pieza a una casilla vacia adyacente'
        else:
            return 'Mueve una pieza a cualquier casilla vacia'

    def insert_update(self):
        self.pieces_to_insert -= 1
        self.pieces_in_board += 1
        if self.pieces_to_insert == 0:
            self.status = 'select'

    def select_update(self, id_vertex):
        self.selected_id = id_vertex
        if self.pieces_in_board > self.threshold_fly:
            self.status = 'move'
        else:
            self.status = 'fly'

    def remove_update(self):
        self.pieces_in_board -= 1
        if self.pieces_to_insert== 0:
            self.status = 'select'
        else:
            self.status = 'insert'

    def update(self):
        if self.pieces_to_insert == 0:
            self.status = 'select'
        else :
            self.status = 'insert'

    def lost_game(self):
        return self.pieces_to_insert + self.pieces_in_board < 3
