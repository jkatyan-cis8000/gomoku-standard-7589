class Board:
    def __init__(self):
        self.grid = [[None for _ in range(15)] for _ in range(15)]

    def is_valid(self, row, col):
        return 0 <= row < 15 and 0 <= col < 15 and self.grid[row][col] is None

    def apply_move(self, row, col, player):
        self.grid[row][col] = player

    def check_winner(self, row, col, player):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            r, c = row + dr, col + dc
            while 0 <= r < 15 and 0 <= c < 15 and self.grid[r][c] == player:
                count += 1
                r += dr
                c += dc
            r, c = row - dr, col - dc
            while 0 <= r < 15 and 0 <= c < 15 and self.grid[r][c] == player:
                count += 1
                r -= dr
                c -= dc
            if count >= 5:
                return player
        return None

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell is None:
                    return False
        return True

    def display(self):
        lines = []
        lines.append("   " + " ".join(f"{i:2d}" for i in range(15)))
        for i, row in enumerate(self.grid):
            line = f"{i:2d} "
            for cell in row:
                if cell is None:
                    line += " . "
                else:
                    line += f" {cell[0].upper()} "
            lines.append(line)
        return "\n".join(lines)
