from dataclasses import dataclass
from typing import List
from PieceColor import PieceColor
import MoveSet
import Player
import Board

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
    _rule_set: DefaultMoveSet

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        return board.get_positions_empty_vertexes()

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        board.assign_color_in_pos(pos, player.color)
        player.pieces_to_insert -= 1

        if board.check_mill_in_pos(pos):
            self._rule_set.current_state = self._rule_set.remove_state

        elif player.pieces_to_insert == 0:
            self._rule_set.current_state = self._rule_set.select_state
            player.take_turn()


@dataclass
class SelectState(MoveSet.State):
    _rule_set: DefaultMoveSet
    _start_pos: tuple = (-1, -1)

    @property
    def start_pos(self) -> tuple:
        return self._start_pos

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        return board.get_positions_with_color(player.color)

    def _valid_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> bool:
        if not pos in self.get_possible_moves(player, board):
            return False

        self._start_pos = pos

        if player.color == board.get_color_from_pos(self._start_pos):
            return False

        return True

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        self._rule_set.current_state = self._rule_set.move_state


@dataclass
class MoveState(MoveSet.State):
    _rule_set: DefaultMoveSet

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        start_pos = self._rule_set.select_state.start_pos
        return board.get_positions_empty_neighbors_of_pos(start_pos)

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        start_pos = self._rule_set.select_state.start_pos
        board.assign_color_in_pos(start_pos, PieceColor.EMPTY)
        board.assign_color_in_pos(pos, player.color)

        if board.check_mill_in_pos(pos):
            self._rule_set.current_state = self._rule_set.remove_state
        else:
            player.take_turn()


@dataclass
class RemoveState(MoveSet.State):
    _rule_set: DefaultMoveSet

    def get_possible_moves(self, player: Player.IPlayer, board: Board.IBoard) -> List[tuple]:
        return board.get_positions_with_color(player.enemy.color)

    def make_move(self, pos: tuple, player: Player.IPlayer, board: Board.IBoard) -> None:
        if not self._valid_move(pos, player, board):
            return

        player.enemy.pieces_in_board -= 1
        board.assign_color_in_pos(pos, PieceColor.EMPTY)

        if player.enemy.check_lost():
            player.won()
        else:
            if player.pieces_to_insert > 0:
                self._rule_set.current_state = self._rule_set.insert_state
            else:
                self._rule_set.current_state = self._rule_set.select_state

            player.take_turn()

