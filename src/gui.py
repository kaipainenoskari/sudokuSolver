# Description: This file contains the code for the sudoku solver.
# It uses a backtracking algorithm to solve the puzzle.

def solve(board):
    # If you want to see the backtracking algorithm in action, uncomment the line below, will slow down the solving process
    #display_board(board)
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def valid(board, num, pos):
    # Check row
    if num in get_vertical(board, pos[1]):
        return False
    # Check column
    if num in get_horizontal(board, pos[0]):
        return False
    # Check box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    if num in get_box(board, box_row * 3, box_col * 3):
        return False
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) 
    return None

def get_vertical(board, col):
    vertical = [board[i][col] for i in range(9)]
    return vertical

def get_horizontal(board, row):
    horizontal = board[row]
    return horizontal

def get_box(board, row, col):
    box = []
    for i in range(3):
        for j in range(3):
            box.append(board[i + row][j + col])
    return box

import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a 9x9 grid of Entry widgets for input
entries = [[tk.Entry(root, width=2) for j in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i, column=j)

# Function to collect the current state of the board
def get_board():
    return [[int(entries[i][j].get()) if entries[i][j].get() != "" else 0 for j in range(9)] for i in range(9)]

# Function to display a solved board
def display_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(tk.END, str(board[i][j]))
    root.update_idletasks()

# Function to solve the board
def solve_board():
    board = get_board()
    if solve(board):
        display_board(board)

# Button to solve the board
solve_button = tk.Button(root, text="Solve", command=solve_board)
solve_button.grid(row=9, column=0, columnspan=9)

# Run the GUI
root.mainloop()
