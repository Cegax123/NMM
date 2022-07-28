import pygame
import GameBuilder
import GUI

WIDTH, HEIGHT = 700, 700
MARGIN = 50
BG_COLOR = (226, 220, 200)

pygame.display.set_caption("Nine Men's Morris Game")
surf = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    # game_state = GameBuilder.GameDirector().build_two_player_three_men_morris_game()
    # game_state = GameBuilder.GameDirector().build_two_player_five_men_morris_game()
    game_state = GameBuilder.GameDirector().build_two_player_nine_men_morris_game()
    game_gui = GUI.GUI(surf, game_state, MARGIN, WIDTH - 2 * MARGIN)

    while game_state.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.end_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                pos_board = game_gui.get_position_in_board(mouse_pos)
                game_state.make_move(pos_board)

        surf.fill(BG_COLOR)
        game_gui.draw_board()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
