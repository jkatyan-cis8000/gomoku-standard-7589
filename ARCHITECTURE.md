# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/board.py: 15x15 grid state, move validation, win detection with 5-in-a-row logic
- src/game.py: turn management, player state, game loop, win condition checking
- src/ui.py: terminal rendering, user input parsing for coordinates
- src/main.py: entry point that ties everything together

## Interfaces

### board.py
- `Board` class:
  - `__init__()` - creates 15x15 empty grid
  - `is_valid(row, col) -> bool` - check if move is within bounds and cell is empty
  - `apply_move(row, col, player) -> None` - place stone at position
  - `check_winner(row, col, player) -> str | None` - check if this move creates a win
  - `is_full() -> bool` - check if board is full (draw)
  - `display() -> str` - return string representation of board

### game.py
- `Game` class:
  - `__init__()` - initializes Board and sets starting player
  - `current_player` property
  - `make_move(row, col) -> dict` - process a move, returns result with status, winner, etc.
  - `reset()` - reset game state
  - `get_state() -> dict` - return current game state for UI

### ui.py
- `UI` class:
  - `display_board(board)` - render the board to terminal
  - `get_player_input(player)` - prompt for coordinates, return (row, col) tuple
  - `display_message(message)` - show message to players
  - `display_game_result(winner)` - show final result

### main.py
- Entry point that:
  - Creates Game instance
  - Creates UI instance
  - Runs game loop: display board -> get input -> make move -> check result
  - Handles game termination and restart

## Shared Data Structures

- `Player`: `"black"` or `"white"`
- `Cell`: `None`, `"black"`, or `"white"`
- `Board`: 15x15 list of lists of Cells
- `Move result`: `{"status": "ongoing" | "win" | "draw", "winner": str | None, "board": Board}`
- `Coordinates`: `(row, col)` tuple where 0 <= row, col < 15

## External Dependencies

- None (standard library only)
