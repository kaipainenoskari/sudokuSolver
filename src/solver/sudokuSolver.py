from solver.sudokuSolver_io import sudokuSolver_io

# Description: This file contains the code for the sudoku solver. It uses a backtracking algorithm to solve the puzzle.
class SudokuSolver:

    def __init__(self, io=sudokuSolver_io):
        self.io = io
        self.board = self.create_board()

    def create_board(self):
        # Example board
        #return [[4,0,0,0,0,0,3,7,8], [0,6,0,0,0,0,4,0,0], [0,0,0,3,0,0,5,0,0], [0,9,0,0,1,0,0,0,0], [0,0,0,0,5,3,0,0,0], [1,0,7,0,0,0,0,3,0], [0,0,9,0,0,0,0,1,0], [0,0,0,6,4,0,0,0,7], [0,0,2,5,0,0,0,8,0]]
        self.io.write("Enter the sudoku puzzle, use 0 to represent an empty cell")
        board = []
        for i in range(9):
            row = list(map(int, self.io.read(f"Enter row {i + 1}: ")))
            board.append(row)
        return board

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False
    
    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                self.io.write("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    self.io.write("| ", end="")
                if j == 8:
                    self.io.write(self.board[i][j])
                else:
                    self.io.write(f"{self.board[i][j]} ", end="")

    def valid(self, num, pos):
        # Check row
        if num in self.get_vertical(pos[1]):
            return False
        # Check column
        if num in self.get_horizontal(pos[0]):
            return False
        # Check box
        box_row = pos[0] // 3
        box_col = pos[1] // 3
        if num in self.get_box(box_row * 3, box_col * 3):
            return False
        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j) 
        return None

    def get_vertical(self, col):
        vertical = [self.board[i][col] for i in range(9)]
        return vertical

    def get_horizontal(self, row):
        horizontal = self.board[row]
        return horizontal

    def get_box(self, row, col):
        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.board[i + row][j + col])
        return box
