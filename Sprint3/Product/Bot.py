from abc import ABC,abstractmethod
from typing import List, Tuple
import Game
import State

class IBot(ABC):
    @abstractmethod
    def get_best_reachable_move(self, game_state: Game.GameState) -> List[tuple]:
        pass


class BotMinimax(IBot):

    def get_best_reachable_move(self, game_state: Game.GameState) -> List[tuple]:
        self.current_turn = game_state.turn
        return self._minimax(game_state, 3, True)[1]

    def _minimax(self, game_state: Game.GameState, depth: int, maxPlayer: bool) -> Tuple[int, List[tuple]]:
        move_handler = State.MoveHandler()
        if depth == 0 or not game_state.running:
            return game_state.evaluate(self.current_turn), []

        if maxPlayer:
            maxEval = float('-inf')
            best_moves = None
            for moves, new_game_state in move_handler.obtain_result_change_turn(game_state):
                evaluation = self._minimax(new_game_state, depth-1, not maxPlayer)[0]
                if evaluation > maxEval:
                    maxEval = evaluation
                    best_moves = moves
            return maxEval, best_moves
        else:
            minEval = float('inf')
            best_moves = None
            for moves, new_game_state in move_handler.obtain_result_change_turn(game_state):
                evaluation = self._minimax(new_game_state, depth-1, not maxPlayer)[0]
                if evaluation < minEval:
                    minEval = evaluation
                    best_moves = moves
            return minEval, best_moves
