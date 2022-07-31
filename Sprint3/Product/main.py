import pygame
import GameBuilder
import State
from PlayerType import PlayerType
from Menus import Menus
from BoardType import MenuModeType
from BoardVariant import BoardVariant
from MenuGameMode import MenuMode
import GUI
import Bot

pygame.display.set_caption("Nine Men's Morris Game")

def main():
    WIDTH, HEIGHT = 1200, 800
    surf = pygame.display.set_mode((WIDTH, HEIGHT))
    BG_COLOR = (226, 220, 200)
    MARGIN = 50

    board_variant = None
    type_player1 = PlayerType.HUMAN
    type_player2 = None

    my_bot = Bot.BotMinimax()
    move_handler = State.MoveHandler()

    current_menu = Menus.MENU_BOARD_VARIANT
    gui = MenuModeType(surf)

    running = True

    while running:
        if current_menu == Menus.GAME_RUNNING:
            if game_state.current_player.get_type() == PlayerType.BOT and not game_state.winner:
                best_move = my_bot.get_best_reachable_move(game_state)
                move_handler.apply_list_moves(best_move, game_state)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos, current_menu)

                if current_menu == Menus.MENU_BOARD_VARIANT:
                    result = gui.check_click(mouse_pos)

                    if result:
                        board_variant = result

                        gui = MenuMode(surf)
                        current_menu = Menus.MENU_GAME_MODE

                elif current_menu == Menus.MENU_GAME_MODE:
                    result = gui.check_click(mouse_pos)

                    if result:
                        type_player2 = result

                        WIDTH, HEIGHT = 700, 700
                        surf = pygame.display.set_mode((WIDTH, HEIGHT))

                        game_state = GameBuilder.GameDirector().build_game(board_variant, type_player1, type_player2)
                        gui = GUI.GameRunning(surf, game_state, MARGIN, WIDTH - 2 * MARGIN)

                        current_menu = Menus.GAME_RUNNING


                elif current_menu == Menus.GAME_RUNNING:
                    if game_state.current_player.get_type() == PlayerType.HUMAN and not game_state.winner:
                        pos_board = gui.get_position_in_board(mouse_pos)
                        move_handler.apply_move(pos_board, game_state)


        surf.fill(BG_COLOR)
        gui.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
