import pygame.draw
from Vertex import Vertex
import json

with open('../Product/conf.json') as f:
    options = json.load(f)
    board_options = options['board']

    f.close()


class Board:
    def __init__(self, n, vertices, edges):
        self.side = board_options['total'] / n
        self.V = [Vertex((x, y), self.side) for x, y in vertices]
        self.E = edges
        self.adj = {}

        for v in range(len(self.V)):
            self.adj[v] = []

        for e in self.E:
            self.adj[e[0]].append(e[1])
            self.adj[e[1]].append(e[0])

        self.message_in_screen = {
            'insert': 'Inserte una pieza en alguna casilla vacia',
            'to_select': 'Seleccione una pieza a mover',
            'selected': 'Seleccione una casilla vacia como destino',
            'to_remove': 'Escoja una pieza del oponente a eliminar'
        }

        self.selected_piece = None

    def draw(self, surf):
        for e in self.E:
            pygame.draw.line(surf, board_options['edge_color'], self.V[e[0]].pos_screen, self.V[e[1]].pos_screen)

        for v in self.V:
            v.draw(surf)

    def get_vertex(self, pos_mouse):
        for i in range(len(self.V)):
            if self.V[i].clicked(pos_mouse):
                return i
        return -1

    def verify_mill(self, id_vertex):

        pass

    def insert_piece(self, player, id_vertex):
        if id_vertex != -1 and self.V[id_vertex].status == 0 and player.pieces_to_insert > 0:
            self.V[id_vertex].update(player)
            player.insert_update()
            turn_change = not self.verify_mill(id_vertex)
        else:
            turn_change = False
        return turn_change

    def remove_piece(self, player, enemy, id_vertex):
        result = {'valid': False, 'winner': False}

        return result

    def select_piece(self, player, id_vertex):
        pass

    def move_piece(self, player, id_vertex):
        result = {'valid': None, 'created_mill': None}
        
        return result

    def fly_piece(self, player, id_vertex):
        pass
