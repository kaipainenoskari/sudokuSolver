from solver.sudokuSolver import SudokuSolver
import tkinter

def main():
    solver = SudokuSolver(gui=True, tk=tkinter, show=True)
    solver.root.mainloop()

if __name__ == "__main__":
    main()