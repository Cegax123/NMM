from abc import ABC, abstractmethod
from typing import List
from copy import deepcopy
from PlayerState import PlayerState
import Game


class IState(ABC):
    @abstractmethod
    def apply_move(self, pos: tuple, game_state: Game.GameState) -> None:
        pass

    @abstractmethod
    def apply_list_moves(self, list_pos: List[tuple], game_state: Game.GameState) -> None:
        pass

    @abstractmethod
    def get_result_move(self, pos: tuple, game_state: Game.GameState) -> Game.GameState:
        pass

    @abstractmethod
    def get_result_list_moves(self, list_pos: List[tuple], game_state: Game.GameState) -> Game.GameState:
        pass

    @abstractmethod
    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        pass

    @abstractmethod
    def get_possible_moves_to_change_turn(self, game_state: Game.GameState) -> List[List[tuple]]:
        pass

    @abstractmethod
    def obtain_result_change_turn(self, game_state: Game.GameState) -> List[tuple]:
        pass

class MoveHandler(IState):
    def apply_move(self, pos: tuple, game_state: Game.GameState) -> None:
        state = StateFactory.get_state(game_state.current_player.state)
        state.apply_move(pos, game_state)

    def apply_list_moves(self, list_pos: List[tuple], game_state: Game.GameState) -> None:
        state = StateFactory.get_state(game_state.current_player.state)
        state.apply_list_moves(list_pos, game_state)

    def get_result_move(self, pos: tuple, game_state: Game.GameState) -> Game.GameState:
        state = StateFactory.get_state(game_state.current_player.state)
        return state.get_result_move(pos, game_state)

    def get_result_list_moves(self, list_pos: List[tuple], game_state: Game.GameState) -> Game.GameState:
        state = StateFactory.get_state(game_state.current_player.state)
        return state.get_result_list_moves(list_pos, game_state)

    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        state = StateFactory.get_state(game_state.current_player.state)
        return state.get_possible_moves(game_state)

    def get_possible_moves_to_change_turn(self, game_state: Game.GameState) -> List[List[tuple]]:
        state = StateFactory.get_state(game_state.current_player.state)
        return state.get_possible_moves_to_change_turn(game_state)

    def obtain_result_change_turn(self, game_state: Game.GameState) -> List[tuple]:
        state = StateFactory.get_state(game_state.current_player.state)
        return state.obtain_result_change_turn(game_state)


class State(IState, ABC):
    @property
    @abstractmethod
    def deep(self) -> int:
        pass

    @abstractmethod
    def apply_move(self, pos: tuple, game_state: Game.GameState) -> None:
        pass

    def apply_list_moves(self, list_pos: List[tuple], game_state: Game.GameState) -> None:
        for pos in list_pos:
            self.apply_move(pos, game_state)

    def get_result_move(self, pos: tuple, game_state: Game.GameState) -> Game.GameState:
        game_state = deepcopy(game_state)
        self.apply_move(pos, game_state)
        return game_state

    def get_result_list_moves(self, list_pos: List[tuple], game_state: Game.GameState) -> Game.GameState:
        game_state = deepcopy(game_state)
        self.apply_list_moves(list_pos, game_state)
        return game_state

    @abstractmethod
    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        pass

    def get_possible_moves_to_change_turn(self, game_state: Game.GameState) -> List[List[tuple]]:
        list_moves = []
        nodes = [([], game_state)]

        current_turn = game_state.turn

        deep = 3

        for i in range(deep):
            new_nodes = []
            for list_pos, game_state in nodes:
                move_handler = MoveHandler()
                possible_moves = move_handler.get_possible_moves(game_state)

                for pos in possible_moves:
                    next_list_pos = list_pos.copy()
                    next_list_pos.append(pos)

                    next_game_state = move_handler.get_result_move(pos, game_state)

                    if current_turn != next_game_state.turn:
                        list_moves.append(next_list_pos)
                    else:
                        new_nodes.append((next_list_pos, next_game_state))

            nodes = new_nodes

        return list_moves

    def obtain_result_change_turn(self, game_state: Game.GameState) -> List[tuple]:
        list_moves = self.get_possible_moves_to_change_turn(game_state)
        result = []

        for moves in list_moves:
            next_game_state = self.get_result_list_moves(moves, game_state)
            result.append((moves, next_game_state))

        return result

    def _valid_move(self, pos: tuple, game_state: Game.GameState) -> bool:
        return pos in self.get_possible_moves(game_state)


class InsertState(State):
    def deep(self) -> int:
        return 1

    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        return game_state.board.get_positions_empty_vertexes()

    def apply_move(self, pos: tuple, game_state: Game.GameState) -> None:
        if not self._valid_move(pos, game_state):
            return

        game_state.board.assign_color_in_pos(pos, game_state.current_player.color)

        game_state.current_player.pieces_to_insert -= 1
        game_state.current_player.pieces_in_board += 1

        if game_state.board.check_mill_in_pos(pos):
            game_state.current_player.state = PlayerState.REMOVE
        else:
            if game_state.current_player.pieces_to_insert == 0:
                game_state.current_player.state = PlayerState.MOVE

            game_state.change_turn()


class MoveState(State, ABC):
    @property
    def deep(self) -> int:
        return 3

    def get_possible_moves_unselected(self, game_state: Game.GameState) -> List[tuple]:
        return game_state.board.get_positions_with_color(game_state.current_player.color)

    @abstractmethod
    def get_possible_moves_selected(self, game_state: Game.GameState) -> List[tuple]:
        pass

    def get_possible_moves(self, game_state: Game.GameState):
        if not game_state.current_player.start_selected():
            return self.get_possible_moves_unselected(game_state)

        return self.get_possible_moves_selected(game_state)

    def apply_move(self, pos: tuple, game_state: Game.GameState) -> None:
        if not self._valid_move(pos, game_state):
            return

        if not game_state.current_player.start_selected():
            game_state.current_player.start_pos = pos
            return

        if game_state.board.get_color_from_pos(pos) == game_state.current_player.color:
            game_state.current_player.start_pos = pos
            return

        start_pos = game_state.current_player.start_pos
        game_state.current_player.unselect_start()

        game_state.board.remove_piece_in_pos(start_pos)
        game_state.board.assign_color_in_pos(pos, game_state.current_player.color)

        if game_state.board.check_mill_in_pos(pos):
            game_state.current_player.state = PlayerState.REMOVE

        else:
            game_state.change_turn()


class MoveAdyacentState(MoveState):
    def get_possible_moves_selected(self, game_state: Game.GameState):
        start_pos = game_state.current_player.start_pos

        empty_adyacent = game_state.board.get_positions_empty_neighbors_of_pos(start_pos)
        same_color = game_state.board.get_positions_with_color(game_state.current_player.color)

        return empty_adyacent + same_color


class FlyState(MoveState):
    def get_possible_moves_selected(self, game_state: Game.GameState):
        empty_vertexes = game_state.board.get_positions_empty_vertexes()
        same_color = game_state.board.get_positions_with_color(game_state.current_player.color)

        return empty_vertexes + same_color


class RemoveState(State):
    @property
    def deep(self) -> int:
        return 1

    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        enemy_color_positions = game_state.board.get_positions_with_color(game_state.enemy_player.color)
        possible_moves = []

        for pos in enemy_color_positions:
            if not game_state.board.check_mill_in_pos(pos):
                possible_moves.append(pos)

        if len(possible_moves) == 0:
            possible_moves = enemy_color_positions

        return possible_moves

    def apply_move(self, pos: tuple, game_state: Game.GameState) -> None:
        if not self._valid_move(pos, game_state):
            return

        game_state.enemy_player.pieces_in_board -= 1
        game_state.board.remove_piece_in_pos(pos)

        pieces_to_insert = game_state.current_player.pieces_to_insert
        pieces_in_board = game_state.current_player.pieces_in_board

        if pieces_to_insert > 0:
            game_state.current_player.state = PlayerState.INSERT
        else:
            if pieces_in_board > game_state.threshold_fly:
                game_state.current_player.state = PlayerState.MOVE
            else:
                game_state.current_player.state = PlayerState.FLY

        if game_state.enemy_player.check_lost():
            game_state.end_game()

        game_state.change_turn()


class StateFactory:
    @staticmethod
    def get_state(state: PlayerState):
        if state == PlayerState.INSERT:
            return InsertState()
        if state == PlayerState.MOVE:
            return MoveAdyacentState()
        if state == PlayerState.FLY:
            return FlyState()
        if state == PlayerState.REMOVE:
            return RemoveState()

