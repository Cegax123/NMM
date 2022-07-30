from typing import Deque
import pygame
import GameBuilder
import State
from PlayerType import PlayerType
from BoardVariant import BoardVariant
from pprint import pprint
import GUI
import Bot

WIDTH, HEIGHT = 700, 700
MARGIN = 50
BG_COLOR = (226, 220, 200)

pygame.display.set_caption("Nine Men's Morris Game")
surf = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    turn = 1

    move_handler = State.MoveHandler()
    game_state = GameBuilder.GameDirector().build_game(BoardVariant.NINE_MEN_MORRIS, PlayerType.HUMAN, PlayerType.BOT)
    game_gui = GUI.GUI(surf, game_state, MARGIN, WIDTH - 2 * MARGIN)
    my_bot = Bot.BotMinimax()

    while game_state.running:
        if turn != game_state.turn:
            # print(my_bot.get_best_reachable_move(game_state))

#            pprint(move_handler.get_possible_moves_to_change_turn(game_state))

#            print('-------')
#            print('-------')
            turn ^= 1

        if game_state.current_player.get_type() == PlayerType.BOT and not game_state.winner:
            best_move = my_bot.get_best_reachable_move(game_state)
            move_handler.apply_list_moves(best_move, game_state)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.exit_program()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                pos_board = game_gui.get_position_in_board(mouse_pos)

                if game_state.current_player.get_type() == PlayerType.HUMAN and not game_state.winner:
                    move_handler.apply_move(pos_board, game_state)

        surf.fill(BG_COLOR)
        game_gui.draw_board()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
