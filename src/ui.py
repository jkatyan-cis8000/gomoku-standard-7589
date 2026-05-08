"""UI module for Gomoku game.

Provides the UI class which handles terminal rendering and user input.
"""

from typing import Tuple

from board import Board


class UI:
    """Handles terminal UI for the Gomoku game."""

    def display_board(self, board: Board) -> None:
        """Render the board to terminal.

        Args:
            board: The Board instance to display
        """
        print(board.display())
        print()

    def get_player_input(self, player: str) -> Tuple[int, int]:
        """Prompt for coordinates, return (row, col) tuple.

        Args:
            player: The player making the move

        Returns:
            Tuple of (row, col) coordinates
        """
        while True:
            user_input = input(f"{player.capitalize()}'s turn. Enter row and col (e.g., '7 7'): ")
            try:
                parts = user_input.strip().split()
                if len(parts) != 2:
                    raise ValueError("Enter exactly two numbers")
                row, col = int(parts[0]), int(parts[1])
                return row, col
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter two numbers separated by space.")

    def display_message(self, message: str) -> None:
        """Show message to players.

        Args:
            message: The message to display
        """
        print(message)
        print()

    def display_game_result(self, winner: str) -> None:
        """Show final result.

        Args:
            winner: The winning player name, or None for draw
        """
        if winner:
            self.display_message(f"{winner.capitalize()} wins!")
        else:
            self.display_message("It's a draw!")


def get_restart_choice() -> bool:
    """Ask player if they want to restart.

    Returns:
        True if yes, False if no
    """
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")
