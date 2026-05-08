"""Game module for Gomoku game.

Provides the Game class which manages game state, turns, and game flow.
"""

from typing import Optional

from board import Board


class Game:
    """Manages the Gomoku game state and flow.

    Handles turn management, move processing, and win condition checking.
    """

    def __init__(self) -> None:
        """Initialize a new game with an empty board and black starting."""
        self._board = Board()
        self._current_player = "black"
        self._game_over = False
        self._winner: Optional[str] = None

    @property
    def current_player(self) -> str:
        """Get the current player."""
        return self._current_player

    def make_move(self, row: int, col: int) -> dict:
        """Process a move at the given position.

        Args:
            row: Row index of the move
            col: Column index of the move

        Returns:
            Dictionary with status, winner, and board representation
        """
        if self._game_over:
            return {
                "status": "game_over",
                "winner": self._winner,
                "board": self._board,
            }

        if not self._board.is_valid(row, col):
            return {
                "status": "invalid",
                "winner": None,
                "board": self._board,
            }

        self._board.apply_move(row, col, self._current_player)

        winner = self._board.check_winner(row, col, self._current_player)

        if winner:
            self._game_over = True
            self._winner = winner
            return {
                "status": "win",
                "winner": winner,
                "board": self._board,
            }

        if self._board.is_full():
            self._game_over = True
            self._winner = None
            return {
                "status": "draw",
                "winner": None,
                "board": self._board,
            }

        self._switch_player()
        return {
            "status": "ongoing",
            "winner": None,
            "board": self._board,
        }

    def _switch_player(self) -> None:
        """Switch to the other player."""
        self._current_player = "white" if self._current_player == "black" else "black"

    def reset(self) -> None:
        """Reset the game to initial state."""
        self._board = Board()
        self._current_player = "black"
        self._game_over = False
        self._winner = None

    def get_state(self) -> dict:
        """Return current game state for UI.

        Returns:
            Dictionary with current player, game status, and winner if any
        """
        return {
            "current_player": self._current_player,
            "game_over": self._game_over,
            "winner": self._winner,
        }
