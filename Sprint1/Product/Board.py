class Board:
    def __init__(self, N, V, E):
        self.V = [] # Lista de objetos Vertex 
        self.E = [] # Lista de aristas: (v1, v2) -> se usaran las posiciones que se encuentran en self.V
        self.adj = None # Lista de adyecencia: {0 : [2, 3], 1 : [3, 4]} -> se usaran las posiciones que se encuentran en self.V
        

        self.message_in_screen = {
            'insert' : 'Inserte una pieza en alguna casilla vacia',
            'to_select' : 'Seleccione una pieza a mover',
            'selected' : 'Seleccione una casilla vacia como destino',
            'to_remove' : 'Escoja una pieza del oponente a eliminar'
        }

        self.selected_piece = None

    def draw(self):
        # Draw board

        

        # Draw all Vertex
        for v in self.V:
            v.draw()

    def get_vertex(self, pos_mouse):
        pass

    def verify_mill(self, id_vertex):
        pass

    def set_mode(self, new_mode):
        self.mode = new_mode

    def insert_piece(self, player, id_vertex):
        result = {'valid' : None, 'created_mill' : None}

        return result

    def remove_piece(self, player, id_vertex):
        result = {'valid' : None}

        return result

    def select_piece(self, id_vertex):
        result = {'valid' : None}

        return result

    def move_piece(self, player, id_vertex):
        result = {'valid' : None, 'created_mill' : None}


        return result
