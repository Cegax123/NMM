from turtle import pos
import pygame.draw
from Vertex import Vertex
import json
from text import Text

with open('../Product/conf.json') as f:
    options = json.load(f)
    board_options = options['board']

    f.close()


class Board:
    def __init__(self, n, vertices, edges):
        self.n = n
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

        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(self.n+1):
            Text(str(i+1), 40, 'verdana', [0, 0, 0]).draw(board_options['start_x']-100, board_options['end_y'] - i * self.side - 20, surf)
            Text(alpha[i], 40, 'verdana', [0, 0, 0]).draw(board_options['start_x'] + self.side * i-12, board_options['end_y']+30, surf)

    def get_vertex(self, pos_mouse):
        for i in range(len(self.V)):
            if self.V[i].clicked(pos_mouse):
                return i
        return -1

    def update_border_vertex(self, player):
        for v in self.V:
            v.border = None
        pos_remove=self.get_posible_takes(player)

        for id, v in enumerate(self.V):
            '''if player.status == 'select':
                if v.status == player.turn:
                    v.border = 'target_piece' '''

            if player.status == 'move':
                if id == player.selected_id:
                    v.border = 'selected_piece'
                elif id in self.adj[player.selected_id] and v.status == 0:
                    v.border = 'target_piece'

            elif player.status == 'fly':
                if id == player.selected_id:
                    v.border = 'selected_piece'
                elif v.status == 0:
                    v.border = 'target_piece'

            elif player.status == 'remove':
                if v.status != 0 and id in pos_remove:
                    v.border = 'remove_piece'

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

    def get_posible_takes(self, player):
        pos_moves = []
        for i in range(len(self.V)):
            if self.V[i].status==3-player.turn and not self.verify_mill(i):
                pos_moves.append(i)
        if len(pos_moves)==0:
            for i in range(len(self.V)):
                if self.V[i].status==3-player.turn:
                    pos_moves.append(i)
        return pos_moves

    def insert_piece(self, player, id_vertex):
        if id_vertex != -1 and self.V[id_vertex].status == 0 and player.pieces_to_insert > 0:
            self.V[id_vertex].update(player)
            player.insert_update()
            if self.verify_mill(id_vertex):
                change_turn = False
                player.status = 'remove'
            else:
                change_turn = True
        else:
            change_turn = False

        return change_turn

    def remove_piece(self, player, enemy, id_vertex):
        pos_remove=self.get_posible_takes(player)
        if id_vertex != -1 and id_vertex in pos_remove:
            self.V[id_vertex].update()
            player.update()
            enemy.remove_update()
            change_turn = True
        else:
            change_turn = False

        return change_turn

    def select_piece(self, player, id_vertex):
        if id_vertex !=-1 and self.V[id_vertex].status == player.turn:
            player.select_update(id_vertex)
            #poner posibles movimientos

    def move_piece(self, player, id_vertex):
        if id_vertex == player.selected_id: #te mueves al mismo lugar
            player.update()
            change_turn = False

        elif self.V[id_vertex].status == player.turn: #te mueves a diferente lugar pero mismo color
            
            self.select_piece(player, id_vertex)
            change_turn = False

        elif id_vertex in self.adj[player.selected_id] and self.V[id_vertex].status == 0: #te mueves a una posicion vacia correcta
            self.V[player.selected_id].update()
            self.V[id_vertex].update(player)
            player.update()
            if self.verify_mill(id_vertex):
                change_turn = False
                player.status = 'remove'
            else:
                change_turn = True
        else:
            change_turn = False
            
        return change_turn        

    def fly_piece(self, player, id_vertex):
        if id_vertex != -1:
            if id_vertex == player.selected_id:
                player.update()
                change_turn = False
            elif self.V[id_vertex].status == player.turn:
                self.select_piece(player, id_vertex)
                change_turn = False
            elif self.V[id_vertex].status == 0:
                self.V[player.selected_id].update()
                self.V[id_vertex].update(player)
                player.update()
                if self.verify_mill(id_vertex):
                    change_turn = False
                    player.status = 'remove'
                else:
                    change_turn = True
            else:
                change_turn = False
        else:
            change_turn = False
            
        return change_turn
