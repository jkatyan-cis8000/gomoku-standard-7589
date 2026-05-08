# Game Module Design

## Overview

The `Game` class in `src/game.py` manages the state and flow of a Gomoku game. It coordinates player turns, processes moves, and determines game outcomes (win/loss/draw).

## Architecture

```
Game
├── board: Board          # 15x15 grid state
├── _current_player: str  # "black" or "white"
├── game_over: bool       # Game termination flag
└── winner: str | None    # Winning player or None
```

## Components

### Initialization

- Creates a `Board` instance for the 15x15 grid
- Sets starting player to "black" (per Gomoku rules)
- Initializes `game_over` and `winner` state

### current_player Property

Returns the player whose turn it is. Black always goes first.

### make_move(row, col) -> dict

Processes a player move and returns a result dictionary:

```python
{
    "status": "ongoing" | "win" | "draw",
    "winner": str | None,
    "board": Board
}
```

**Flow:**
1. Check if game is already over → return current state
2. Validate move using `Board.is_valid()` → return if invalid
3. Apply move via `Board.apply_move()`
4. Check for win via `Board.check_winner()`
   - If win: set `game_over=True`, record winner, return "win" status
5. Check for draw via `Board.is_full()`
   - If full: set `game_over=True`, return "draw" status
6. Switch current player
7. Return "ongoing" status

### reset()

Restores the game to initial state:
- Creates new `Board` instance
- Resets current player to "black"
- Clears `game_over` and `winner` state

### get_state() -> dict

Returns complete game state for UI:

```python
{
    "current_player": str,
    "game_over": bool,
    "winner": str | None,
    "board": Board
}
```

## Dependencies

- `Board` from `board.py`: Handles grid state, move validation, and win detection

## Design Decisions

1. **Separate winner tracking**: The Game class maintains its own `winner` field rather than querying the board directly, simplifying UI state management.

2. **Move validation at game level**: Invalid moves are handled by returning "ongoing" status without modifying game state, allowing UI to retry input.

3. **State immutability on game over**: Once `game_over=True`, subsequent moves don't modify the board or player state, preserving the final state for review.

4. **Return board in results**: Each move returns the current board state, enabling UI to refresh without separate state queries.
