"""
A just simple TicTacToe implementation with O(n) per move and O(n*n) space, where n is the size of a row or column
once that we're working with a square matrix

"""


class TicTacToe:

    def __init__(self, n: int):
        self.board = [[]] * n
        for i in range(n):
            self.board[i] = [0] * n
        self.size = n

    def check_column(self, col, player):
        score = 0
        for i in range(self.size):
            if self.board[i][col] == player:
                score += 1

        return score == self.size

    def check_row(self, row, player):
        score = 0
        for i in range(self.size):
            if self.board[row][i] == player:
                score += 1

        return score == self.size

    def check_diagonal(self, player):
        score = 0
        for i in range(self.size):
            if self.board[i][i] == player:
                score += 1

        return score == self.size

    def check_anti_diagonal(self, player):
        score = 0
        for i in range(self.size):
            if self.board[self.size - i - 1][i] == player:
                score += 1

        return score == self.size

    def has_winner(self, row, col, player) -> int:

        if self.check_column(col, player) or self.check_row(row, player) or self.check_diagonal(
                player) or self.check_anti_diagonal(player):
            return player

        return 0

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
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
