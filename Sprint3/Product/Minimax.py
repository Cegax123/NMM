from copy import deepcopy
import pygame
from DefaultMoveSet import DefaultMoveSet
from DefaultWithFlyMoveSet import DefaultRulesWithFly

class node:
    def __init__(self, game_state, move_set1, move_set2):
        self.game_state = deepcopy(game_state)
        self.move_sets = [deepcopy(move_set1), deepcopy(move_set2)]


def minimax(now , depth):
    #print(depth)
    #print(now.game_state.evaluate())
    if depth == 0 or not now.game_state.running:
        return now.game_state.evaluate(), (-1,-1)

    if now.game_state.turn == 0:
        maxEval = float('-inf')
        best_pos = None
        for pos, move in get_all_moves(now):
            evaluation = minimax(move, depth-1)[0]
            if evaluation > maxEval:
                maxEval = evaluation
                best_pos = pos
        return maxEval, best_pos
    else:
        minEval = float('inf')
        best_pos = None
        for pos, move in get_all_moves(now):
            evaluation = minimax(move, depth-1)[0]
            if evaluation < minEval:
                minEval = evaluation
                best_pos = pos
        return minEval, best_pos

def get_all_moves(now):
    moves = []
    for pos in now.move_sets[now.game_state.turn].get_possible_moves(now.game_state):
        next=deepcopy(now)
        next.move_sets[next.game_state.turn].make_move(pos, next.game_state)
        moves.append((pos,next))
    return moves
