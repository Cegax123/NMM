import pygame
import GameBuilder
from PlayerType import PlayerType
from DefaultMoveSet import DefaultMoveSet
from DefaultWithFlyMoveSet import DefaultRulesWithFly
from Minimax import *
import GUI

WIDTH, HEIGHT = 700, 700
MARGIN = 50
BG_COLOR = (226, 220, 200)

pygame.display.set_caption("Nine Men's Morris Game")
surf = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    # game_state = GameBuilder.GameDirector().build_two_player_three_men_morris_game()
    game_state = GameBuilder.GameDirector().build_two_player_five_men_morris_game()
    # game_state = GameBuilder.GameDirector().build_two_player_nine_men_morris_game()

    move_set1 = DefaultRulesWithFly(3)
    move_set2 = DefaultRulesWithFly(3)

    game_gui = GUI.GUI(surf, game_state, MARGIN, WIDTH - 2 * MARGIN)

    while game_state.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.end_game()
            if game_state.turn % 2 == 1:
                eval,pos = minimax(node(game_state,move_set1,move_set2),3)
                move_set2.make_move(pos,game_state)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                pos_board = game_gui.get_position_in_board(mouse_pos)

                if game_state.current_player.get_type() == PlayerType.HUMAN:
                    if game_state.turn % 2 == 0:
                        move_set1.make_move(pos_board, game_state)
                    else:
                        
                        move_set2.make_move(pos_board, game_state)

        surf.fill(BG_COLOR)
        game_gui.draw_board()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
