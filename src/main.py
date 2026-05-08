"""Main entry point for Gomoku game."""

from game import Game
from ui import UI, get_restart_choice


def main() -> None:
    """Run the Gomoku game loop."""
    game = Game()
    ui = UI()

    while True:
        game.reset()

        while not game.get_state()["game_over"]:
            ui.display_board(game._board)
            row, col = ui.get_player_input(game.current_player)
            result = game.make_move(row, col)

            if result["status"] == "invalid":
                ui.display_message("Invalid move. Try again.")
                continue

        ui.display_board(game._board)
        ui.display_game_result(game._winner)

        if not get_restart_choice():
            break


if __name__ == "__main__":
    main()
