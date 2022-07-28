from dataclasses import dataclass
from typing import List
import MoveSet
import Player
import Board


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

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        self._current_state.make_move(pos, player, board)

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        return self._current_state.get_possible_moves(player, board)


@dataclass
class InsertState(MoveSet.State):
    _move_set: DefaultMoveSet

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        return board.get_positions_empty_vertexes()

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        board.assign_color_in_pos(pos, player.color)

        player.pieces_to_insert -= 1
        player.pieces_in_board += 1

        if board.check_mill_in_pos(pos):
            self._move_set.current_state = self._move_set.remove_state
        else:
            if player.pieces_to_insert == 0:
                self._move_set.current_state = self._move_set.select_state

            player.take_turn()


@dataclass
class SelectState(MoveSet.State):
    _move_set: DefaultMoveSet

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        return board.get_positions_with_color(player.color)

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        player.start_pos = pos
        self._move_set.current_state = self._move_set.move_state


@dataclass
class MoveState(MoveSet.State):
    _move_set: DefaultMoveSet

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        start_pos = player.start_pos
        empty_adyacent = board.get_positions_empty_neighbors_of_pos(start_pos)
        same_color = board.get_positions_with_color(player.color)
        return empty_adyacent + same_color

    def _valid_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard):
        if not pos in self.get_possible_moves(player, board):
            return False

        if board.get_color_from_pos(pos) == player.color:
            player.start_pos = pos
            return False

        return True

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        start_pos = player.start_pos
        player.start_pos = (-1, -1)

        board.remove_piece_in_pos(start_pos)
        board.assign_color_in_pos(pos, player.color)

        if board.check_mill_in_pos(pos):
            self._move_set.current_state = self._move_set.remove_state
        else:
            if player.pieces_to_insert > 0:
                self._move_set.current_state = self._move_set.insert_state
            else:
                self._move_set.current_state = self._move_set.select_state

            player.take_turn()


@dataclass
class RemoveState(MoveSet.State):
    _move_set: DefaultMoveSet

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        enemy_color_positions = board.get_positions_with_color(player.enemy.color)
        possible_moves = []

        for pos in enemy_color_positions:
            if not board.check_mill_in_pos(pos):
                possible_moves.append(pos)

        if len(possible_moves) == 0:
            possible_moves = enemy_color_positions

        return possible_moves

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        player.enemy.pieces_in_board -= 1
        board.remove_piece_in_pos(pos)

        if player.enemy.check_lost():
            player.won()
        else:
            if player.pieces_to_insert > 0:
                self._move_set.current_state = self._move_set.insert_state
            else:
                self._move_set.current_state = self._move_set.select_state

            player.take_turn()


