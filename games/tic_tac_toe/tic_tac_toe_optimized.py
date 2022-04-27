"""
An optimized  TicTacToe implementation with O(1) per move and O(n) space, where n is the size of a row or column
once that we're working with a square matrix

"""


class TicTacToe:

    def __init__(self, n: int):
        self.linear_row_score = [0] * n
        self.linear_col_score = [0] * n
        self.diagonal_score = 0
        self.anti_diagonal_score = 0
        self.size = n

    def check_column(self, col):
        return abs(self.linear_col_score[col]) == self.size

    def check_row(self, row):
        return abs(self.linear_row_score[row]) == self.size

    def check_diagonal(self):
        return abs(self.diagonal_score) == self.size

    def check_anti_diagonal(self):
        return abs(self.anti_diagonal_score) == self.size

    def has_winner(self, row, col, player) -> int:

        if self.check_column(col) or self.check_row(row) or self.check_diagonal() or self.check_anti_diagonal():
            return player

        return 0

    def move(self, row: int, col: int, player: int) -> int:

        value = 1 if player == 1 else -1

        self.linear_row_score[row] += value
        self.linear_col_score[col] += value

        if row == col:
            self.diagonal_score += value

        if col == self.size - row - 1:
            self.anti_diagonal_score += value

        return self.has_winner(row, col, player)


def main():
    game = TicTacToe(3)
    movements = [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]

    idx = 0
    result = game.move(*movements[idx])
    while result == 0 or idx > len(movements) - 1:
        idx += 1
        result = game.move(*movements[idx])

    print(f'Player: {result} win')


if __name__ == '__main__':
    main()
