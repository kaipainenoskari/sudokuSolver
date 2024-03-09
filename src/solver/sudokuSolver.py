from solver.sudokuSolver_io import sudokuSolver_io

# Description: This file contains the code for the sudoku solver. It uses a backtracking algorithm to solve the puzzle.
class SudokuSolver:

    def __init__(self, io=sudokuSolver_io, gui=False, tk=None, show=False, test=False):
        self.io = io
        self.show = show
        if gui and not test:
            self.tk = tk
            self.create_board_with_gui()
        elif not test:
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
    
    def create_board_with_gui(self):
        # Create the main window
        self.root = self.tk.Tk()

        # Create a 9x9 grid of Entry widgets for input
        self.entries = [[self.tk.Entry(self.root, width=2) for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j)
        
        # Button to solve the board
        solve_button = self.tk.Button(self.root, text="Solve", command=self.solve_board)
        solve_button.grid(row=9, column=0, columnspan=9)

    # Function to collect the current state of the board
    def get_board(self):
        return [[int(self.entries[i][j].get()) if self.entries[i][j].get() != "" else 0 for j in range(9)] for i in range(9)]
    
    # Function to solve the board
    def solve_board(self):
        self.board = self.get_board()
        if self.solve():
            self.display_board()

    # Function to display a solved board
    def display_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, self.tk.END)
                self.entries[i][j].insert(self.tk.END, str(self.board[i][j]))
        self.root.update_idletasks()

    def solve(self):
        if self.show:
            self.display_board()
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
        empty_cells = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]
        if not empty_cells:
            return None
        else:
            # Choose the cell with the fewest remaining possible numbers
            return min(empty_cells, key=lambda cell: len(self.possible_numbers(cell)))
        
    def possible_numbers(self, cell):
        row, col = cell
        used_numbers = {self.board[i][col] for i in range(9)} | {self.board[row][j] for j in range(9)} | {self.board[row//3*3 + i//3][col//3*3 + i%3] for i in range(9)}
        return {i for i in range(1, 10)} - used_numbers

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
