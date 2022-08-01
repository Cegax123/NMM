from abc import ABC,abstractmethod
from typing import List, Tuple
import random
import time
import Game
import State


class IBot(ABC):
    @abstractmethod
    def get_best_reachable_move(self, game_state: Game.GameState) -> List[tuple]:
        pass


class BotMinimax(IBot):

    def __init__(self) -> None:
        self.move_handler = State.MoveHandler()
        self.max_ms = 5000

    def get_best_reachable_move(self, game_state: Game.GameState, depth: int) -> List[tuple]:
        self.current_turn = game_state.turn
        self.start_time = time.time()
        ans = self._minimax(game_state, depth, True, float('-inf'), float('inf'))
        print(ans)
        return ans[1]
        #return self._iterative_deepening(game_state)

    def _check_time(self):
        time_diff_ms = (time.time() - self.start_time)*1000
        return time_diff_ms >= self.max_ms


    def _minimax(self, game_state: Game.GameState, depth: int, maxPlayer: bool, alpha: float, beta: float) -> Tuple[int, List[tuple]]:

        if depth == 0 or game_state.winner or self._check_time():
            return game_state.evaluate(self.current_turn), []

        pos_new_moves = self.move_handler.obtain_result_change_turn(game_state)
        #pos_new_moves.sort(key = len, reverse = True)
        random.shuffle(pos_new_moves)


        if maxPlayer:
            maxEval = float('-inf')
            best_moves = None
            for moves, new_game_state in pos_new_moves:
                evaluation = self._minimax(new_game_state, depth-1, not maxPlayer, alpha, beta)[0]
                if maxEval < evaluation:
                    maxEval = evaluation
                    best_moves = moves
                alpha = max(alpha, maxEval)
                if maxEval >= beta:
                    break
            return maxEval, best_moves
        else:
            minEval = float('inf')
            best_moves = None
            for moves, new_game_state in pos_new_moves:
                evaluation = self._minimax(new_game_state, depth-1, not maxPlayer, alpha, beta)[0]
                if evaluation < minEval:
                    minEval = evaluation
                    best_moves = moves
                beta = min(beta, minEval)
                if minEval <= alpha:
                    break
            return minEval, best_moves

    def _iterative_deepening(self, game_state: Game.GameState):
        curr_depth = 1
        while not self._check_time():
            ans = self._minimax(game_state, curr_depth, True, float('-inf'), float('inf'))[1]
            curr_depth += 1
        return ans
