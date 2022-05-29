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

    def colinear(self, u, v, w): #verifica si 3 vertices son colineares
        diag1 = self.V[u].pos_board[0] - self.V[u].pos_board[1] == self.V[v].pos_board[0] - self.V[v].pos_board[1] == self.V[w].pos_board[0] - self.V[w].pos_board[1]
        diag2 = self.V[u].pos_board[0] + self.V[u].pos_board[1] == self.V[v].pos_board[0] + self.V[v].pos_board[1] == self.V[w].pos_board[0] + self.V[w].pos_board[1]
        row = self.V[u].pos_board[0] == self.V[v].pos_board[0] and self.V[v].pos_board[0] == self.V[w].pos_board[0]
        column = self.V[u].pos_board[1] == self.V[v].pos_board[1] and self.V[v].pos_board[1] == self.V[w].pos_board[1]
        return row or column or diag1 or diag2

    def verify_mill(self, id_vertex): #verifica si hay un mill 
        status = self.V[id_vertex].status
        for u in self.adj[id_vertex]:
            if self.V[u].status != status:
                continue
            for v in self.adj[id_vertex]:
                if(u==v or self.V[v].status!=status):
                    continue
                if self.colinear(u,id_vertex,v):
                    return True
        for u in self.adj[id_vertex]:
            if self.V[u].status != status:
                continue
            for v in self.adj[u]:
                if(v==id_vertex or self.V[v].status!=status):
                    continue
                if self.colinear(id_vertex,u,v):
                    return True
        return False

    def insert_piece(self, player, id_vertex):
        if id_vertex != -1 and self.V[id_vertex].status == 0 and player.pieces_to_insert > 0:
            self.V[id_vertex].update(player)
            player.insert_update()
            if self.verify_mill(id_vertex):
                turn_change = False
                player.status = 'remove'
            else:
                turn_change = True
        else:
            turn_change = False
        return turn_change

    def remove_piece(self, player, enemy, id_vertex):
        if id_vertex != -1 and self.V[id_vertex].status == enemy.turn:
            self.V[id_vertex].update()
            player.update()
            enemy.remove_update()
            turn_change = True
        else:
            turn_change = False

        return turn_change

    def select_piece(self, player, id_vertex):
        if id_vertex !=-1 and self.V[id_vertex].status == player.turn:
            player.select_update(id_vertex)
            #poner posibles movimientos
            

    def move_piece(self, player, id_vertex):
        if id_vertex != -1:
            if id_vertex == player.selected_id: #te mueves al mismo lugar
                player.update()
                turn_change = False
            elif self.V[id_vertex].status == player.turn: #te mueves a diferente lugar pero mismo color
                self.select_piece(player, id_vertex)
                turn_change = False
            elif id_vertex in self.adj[player.selected_id] and self.V[id_vertex].status == 0: #te mueves a una posicion vacia correcta
                self.V[player.selected_id].update()
                self.V[id_vertex].update(player)
                player.update()
                if self.verify_mill(id_vertex):
                    turn_change = False
                    player.status = 'remove'
                else:
                    turn_change = True
            else:
                turn_change = False
        else:
            turn_change = False
            
        return turn_change        

    def fly_piece(self, player, id_vertex):
        if id_vertex != -1:
            if id_vertex == player.selected_id:
                player.update()
                turn_change = False
            elif self.V[id_vertex].status == player.turn:
                self.select_piece(player, id_vertex)
                turn_change = False
            elif self.V[id_vertex].status == 0:
                self.V[player.selected_id].update()
                self.V[id_vertex].update(player)
                player.update()
                if self.verify_mill(id_vertex):
                    turn_change = False
                    player.status = 'remove'
                else:
                    turn_change = True
            else:
                turn_change = False
        else:
            turn_change = False
        return turn_change
