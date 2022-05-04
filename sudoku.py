class Sudoku:
    def __init__(self, board_file = None):
        if not board_file:
            self.board = []
            for i in range(9):
                row = []
                for j in range(9):
                    row.append('0')
                self.board.append(row)
        else:
            self.board = create_board(board_file)
    

    def __str__(self):
        spaced_board = ''
        for row in self.board:
            spaced_board += str(row) + '\n'
        return spaced_board


    def place_number(self, position, num):
        row, col = position
        self.board[row][col] = num


    def check_row(self, position):
        row, col = position
        possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for num in self.board[row]:
            if num != '0':
                if not num in possible:
                    return set()
                possible.remove(num)
        return set(possible)


    def check_col(self, position):
        row, col = position
        possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(len(self.board)):
            num = self.board[i][col]
            if num != '0':
                if not num in possible:
                    return set()
                possible.remove(num)
        return set(possible)
    

    def check_box(self, position):
        row, col = position
        box_row = row // 3 
        box_col = col // 3 
        possible = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(3):
            for j in range(3):
                num = self.board[box_row*3+i][box_col*3+j]
                if num != '0':
                    if not num in possible:
                        return set()
                    possible.remove(num)
        return set(possible)


    def solve(self, i = 0, j = 0):
        if i == 9:
            return True
        if self.board[i][j] == '0':
            possible = self.check_row([i,j]).intersection(self.check_col([i,j]).intersection(self.check_box([i,j])))
            if possible == set():
                return False
            temp_board = []
            store_list(self.board, temp_board)
            for num in possible:
                copy_list(temp_board, self.board)
                self.place_number([i,j], str(num))
                if self.solve(i+(j+1)//9, (j+1)%9):
                    return True
            return False
        else:
            return self.solve(i+(j+1)//9, (j+1)%9)


def create_board(f):
    f_open = open(f+'.txt', 'r')
    board = []
    for line in f_open:
        board.append(list(line.strip()))
    f_open.close()
    return board


def copy_list(l1, l2):
    for i in range(9):
        for j in range(9):
            l2[i][j] = l1[i][j]


def store_list(l1, l2):
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(l1[i][j])
        l2.append(temp)

    
if __name__ == '__main__':
    sudoku = Sudoku('sample_boards/very_hard_board')
    print(sudoku)
    sudoku.solve()
    print(sudoku)