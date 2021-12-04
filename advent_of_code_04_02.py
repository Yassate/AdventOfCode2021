class Bingo:
    def __init__(self):
        self.board = []

    def insert_row(self, row):
        self.board.append(row)

    def print_board(self):
        for row in self.board:
            print(row)

    def check_number(self, called_val):
        for row in self.board:
            for i, number in enumerate(row):
                if number == called_val:
                    row[i] = 0

    def check_bingo(self):
        for i in range(5):
            sum_col = 0
            sum_row = 0
            for j in range(5):
                sum_col = sum_col + self.board[j][i]
                sum_row = sum_row + self.board[i][j]
            if 0 in (sum_col, sum_row):
                return True
        return False

    def get_sum(self):
        board_sum = 0
        for row in self.board:
            board_sum = board_sum + sum(row)
        return board_sum


bingo_boards = []
with open('inputs/input_01_04.txt') as f:
    values = [int(x) for x in f.readline().split(',')]
    for i, line in enumerate(f):
        if i % 6 == 0:
            bingo_boards.append(Bingo())
        else:
            stripped = [int(x) for x in line.split()]
            bingo_boards[-1].insert_row(stripped)

for value in values:
    for board in bingo_boards:
        a = 2
        board.check_number(value)
        if board.check_bingo():
            print(board.get_sum()*value)
            exit()




