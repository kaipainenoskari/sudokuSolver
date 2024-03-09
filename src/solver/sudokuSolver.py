from solver.sudokuSolver_io import sudokuSolver_io
from solver.GUI import GUI

# Description: This file contains the code for the sudoku solver. It uses a backtracking algorithm to solve the puzzle.
class SudokuSolver:

    def __init__(self, io=sudokuSolver_io, gui=False, show=False, test=False, board=None):
        self.io = io
        self.show = show
        self.possible_values = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]
        if gui:
            parent = self
            self.GUI = GUI(parent)
        elif not test:
            self.board = self.create_board()
            self.update_possible_values()
        elif board:
            self.board = board
            self.update_possible_values()

    def create_board(self):
        # Example board
        #return [[4,0,0,0,0,0,3,7,8], [0,6,0,0,0,0,4,0,0], [0,0,0,3,0,0,5,0,0], [0,9,0,0,1,0,0,0,0], [0,0,0,0,5,3,0,0,0], [1,0,7,0,0,0,0,3,0], [0,0,9,0,0,0,0,1,0], [0,0,0,6,4,0,0,0,7], [0,0,2,5,0,0,0,8,0]]
        self.io.write("Enter the sudoku puzzle, use 0 to represent an empty cell")
        board = []
        for i in range(9):
            row = list(map(int, self.io.read(f"Enter row {i + 1}: ")))
            board.append(row)
        return board

    def update_possible_values(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.possible_values[i][j] = set()
                    continue
                for num in range(1, 10):
                    if not self.valid(num, (i, j)):
                        self.possible_values[i][j].discard(num)

    def solve(self):
        if self.show:
            self.GUI.display_board()
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for num in sorted(self.possible_values[row][col], key=lambda x: len(self.possible_values[row][col])):
            if self.valid(num, (row, col)):
                self.board[row][col] = num
                self.update_possible_values()
                if self.solve():
                    return True
                self.board[row][col] = 0
                self.update_possible_values()
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
        if num in self.get_vertical(pos[0], pos[1]):
            return False
        # Check column
        if num in self.get_horizontal(pos[0], pos[1]):
            return False
        # Check box
        if num in self.get_box(pos[0], pos[1]):
            return False
        return True

    def find_empty(self):
        empty_cells = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]
        if not empty_cells:
            return None
        else:
            # Choose the cell with the fewest remaining possible numbers
            return min(empty_cells, key=lambda cell: len(self.possible_values[cell[0]][cell[1]]))

    def get_vertical(self, row, col):
        vertical = [self.board[i][col] for i in range(9) if i != row]
        return vertical

    def get_horizontal(self, row, col):
        horizontal = self.board[row][:]
        horizontal.pop(col)
        return horizontal

    def get_box(self, row, col):
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        box = []
        for i in range(3):
            for j in range(3):
                if not (i + box_row == row and j + box_col == col):
                    box.append(self.board[i + box_row][j + box_col])
        return box
