class Bingo:
    def __init__(self):
        self.board = []

    def insert_row(self, row):
        self.board.append(row)

    def mark_number(self, called_val):
        for row in self.board:
            if called_val in row:
                row[row.index(called_val)] = 0

    def check_bingo(self):
        for i in range(5):
            sum_col, sum_row = (0, 0)
            for j in range(5):
                sum_col += self.board[j][i]
                sum_row += self.board[i][j]
            if sum_col == 0 or sum_row == 0:
                return True
        return False

    def get_sum(self):
        board_sum = 0
        for row in self.board:
            board_sum += sum(row)
        return board_sum


bingo_boards = []
with open('inputs/input_01_04.txt') as f:
    values = [int(x) for x in f.readline().split(',')]
    for i, line in enumerate(f):
        if i % 6 == 0:
            bingo_boards.append(Bingo())
        else:
            split = [int(x) for x in line.split()]
            bingo_boards[-1].insert_row(split)

for value in values:
    for board in bingo_boards:
        board.mark_number(value)
        if board.check_bingo():
            print(board.get_sum()*value)
            # 12796
            exit()
