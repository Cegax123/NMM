from dataclasses import dataclass
from typing import List
import MoveSet
import Game


@dataclass
class DefaultMoveSet(MoveSet.IMoveSet):
    def __init__(self):
        self.insert_state = InsertState(self)
        self.select_state = SelectState(self)
        self.move_state = MoveState(self)
        self.remove_state = RemoveState(self)
        self._current_state = self.insert_state

    @property
    def current_state(self) -> MoveSet.IState:
        return self._current_state

    @current_state.setter
    def current_state(self, state: MoveSet.IState) -> None:
        self._current_state = state

    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        self._current_state.make_move(pos, game_state)

    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        return self._current_state.get_possible_moves(game_state)


@dataclass
class InsertState(MoveSet.State):
    _move_set: DefaultMoveSet

    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        return game_state.board.get_positions_empty_vertexes()

    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        if not self._valid_move(pos, game_state):
            return

        game_state.board.assign_color_in_pos(pos, game_state.current_player.color)

        game_state.current_player.pieces_to_insert -= 1
        game_state.current_player.pieces_in_board += 1

        if game_state.board.check_mill_in_pos(pos):
            self._move_set.current_state = self._move_set.remove_state
        else:
            if game_state.current_player.pieces_to_insert == 0:
                self._move_set.current_state = self._move_set.select_state

            game_state.change_turn()


@dataclass
class SelectState(MoveSet.State):
    _move_set: DefaultMoveSet

    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        return game_state.board.get_positions_with_color(game_state.current_player.color)

    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        if not self._valid_move(pos, game_state):
            return

        game_state.current_player.start_pos = pos
        self._move_set.current_state = self._move_set.move_state


@dataclass
class MoveState(MoveSet.State):
    _move_set: DefaultMoveSet

    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        start_pos = game_state.current_player.start_pos
        empty_adyacent = game_state.board.get_positions_empty_neighbors_of_pos(start_pos)
        #same_color = game_state.board.get_positions_with_color(game_state.current_player.color)
        return empty_adyacent #+ same_color

    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        if not self._valid_move(pos, game_state):
            return

        if game_state.board.get_color_from_pos(pos) == game_state.current_player.color:
            game_state.current_player.start_pos = pos
            return

        start_pos = game_state.current_player.start_pos
        game_state.current_player.start_pos = (-1, -1)

        game_state.board.remove_piece_in_pos(start_pos)
        game_state.board.assign_color_in_pos(pos, game_state.current_player.color)

        if game_state.board.check_mill_in_pos(pos):
            self._move_set.current_state = self._move_set.remove_state
        else:
            if game_state.current_player.pieces_to_insert > 0:
                self._move_set.current_state = self._move_set.insert_state
            else:
                self._move_set.current_state = self._move_set.select_state

            game_state.change_turn()


@dataclass
class RemoveState(MoveSet.State):
    _move_set: DefaultMoveSet

    def get_possible_moves(self, game_state: Game.GameState) -> List[tuple]:
        enemy_color_positions = game_state.board.get_positions_with_color(game_state.enemy_player.color)
        possible_moves = []

        for pos in enemy_color_positions:
            if not game_state.board.check_mill_in_pos(pos):
                possible_moves.append(pos)

        if len(possible_moves) == 0:
            possible_moves = enemy_color_positions

        return possible_moves

    def make_move(self, pos: tuple, game_state: Game.GameState) -> None:
        if not self._valid_move(pos, game_state):
            return

        game_state.enemy_player.pieces_in_board -= 1
        game_state.board.remove_piece_in_pos(pos)

        if game_state.enemy_player.check_lost():
            game_state.end_game()
        else:
            if game_state.current_player.pieces_to_insert > 0:
                self._move_set.current_state = self._move_set.insert_state
            else:
                self._move_set.current_state = self._move_set.select_state

            game_state.change_turn()

