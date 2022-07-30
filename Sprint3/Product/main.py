from typing import Deque
import pygame
import GameBuilder
import State
from PlayerType import PlayerType
from BoardVariant import BoardVariant
from pprint import pprint
import GUI

WIDTH, HEIGHT = 700, 700
MARGIN = 50
BG_COLOR = (226, 220, 200)

pygame.display.set_caption("Nine Men's Morris Game")
surf = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    turn = 1

    move_handler = State.MoveHandler()
    game_state = GameBuilder.GameDirector().build_game(BoardVariant.NINE_MEN_MORRIS, PlayerType.HUMAN, PlayerType.HUMAN)
    game_gui = GUI.GUI(surf, game_state, MARGIN, WIDTH - 2 * MARGIN)

    while game_state.running:
        if turn != game_state.turn:
            pprint(move_handler.get_possible_moves_to_change_turn(game_state))

            print('-------')
            print('-------')
            turn ^= 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.end_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                pos_board = game_gui.get_position_in_board(mouse_pos)

                if game_state.current_player.get_type() == PlayerType.HUMAN:
                    move_handler.apply_move(pos_board, game_state)

        surf.fill(BG_COLOR)
        game_gui.draw_board()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
