import tkinter as tk

class GUI:
    def __init__(self, parent):
        self.tk = tk
        self.parent = parent
        self.solving = False
        self.create_board_with_gui()

    def create_board_with_gui(self):
        # Create the main window
        self.root = self.tk.Tk()
        self.root.title("Sudoku Solver")

        # Create a 3x3 grid of Frame widgets, each containing a 3x3 grid of Entry widgets
        self.entries = [[None for j in range(9)] for i in range(9)]
        for box_row in range(3):
            for box_col in range(3):
                box = self.tk.Frame(self.root, borderwidth=1, relief="solid")
                box.grid(row=box_row, column=box_col)
                for cell_row in range(3):
                    for cell_col in range(3):
                        i, j = box_row * 3 + cell_row, box_col * 3 + cell_col
                        entry_var = self.tk.StringVar()
                        entry_var.trace("w", lambda name, index, mode, sv=entry_var, row=i, col=j: self.validate_entry(sv, row, col))
                        entry = self.tk.Entry(box, textvariable=entry_var, width=2, font=('Arial', 42), justify='center')
                        entry.grid(row=cell_row, column=cell_col, padx=1, pady=1)
                        entry.bind('<FocusIn>', lambda event, row=i, col=j: self.highlight_cells(row, col))
                        self.entries[i][j] = entry

        # Button to solve the board
        solve_button = self.tk.Button(self.root, text="Solve", command=self.solve_board, bg='lightblue', font=('Arial', 28), padx=14, pady=14)
        solve_button.grid(row=3, column=0, columnspan=3, pady=20)

    def highlight_cells(self, row, col):
        # Reset all cells to white
        for i in range(9):
            for j in range(9):
                if self.entries[i][j].cget('bg') != 'red':
                    self.entries[i][j].config(bg='white')

        # Highlight the row, column, and box of the selected cell
        box_start_row, box_start_col = row - row % 3, col - col % 3
        for i in range(9):
            if self.entries[row][i].cget('bg') != 'red':
                self.entries[row][i].config(bg='lightblue')  # Highlight row
            if self.entries[i][col].cget('bg') != 'red':
                self.entries[i][col].config(bg='lightblue')  # Highlight column
            if self.entries[box_start_row + i // 3][box_start_col + i % 3].cget('bg') != 'red':
                self.entries[box_start_row + i // 3][box_start_col + i % 3].config(bg='lightblue')  # Highlight box

    def validate_entry(self, entry_var, row, col):
        if self.solving:
            return
        value = entry_var.get()
        if not value.isdigit() or not 1 <= int(value) <= 9:
            entry_var.set("")
        elif self.update_board() and not self.parent.valid(int(value), (row, col)):
            self.entries[row][col].config(bg='red')  # Make the cell red if the move is not valid
        else:
            self.entries[row][col].config(bg='lightblue')  # Make the cell white if the move is valid

    def update_board(self):
        self.parent.board = self.get_board()
        return True

    # Function to collect the current state of the board
    def get_board(self):
        return [[int(self.entries[i][j].get()) if self.entries[i][j].get() != "" else 0 for j in range(9)] for i in range(9)]
    
    # Function to solve the board
    def solve_board(self):
        self.parent.board = self.get_board()
        self.parent.update_possible_values()
        self.solving = True
        if self.parent.solve():
            self.display_board()

    # Function to display a solved board
    def display_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, self.tk.END)
                self.entries[i][j].insert(self.tk.END, self.parent.board[i][j])
        self.root.update_idletasks()