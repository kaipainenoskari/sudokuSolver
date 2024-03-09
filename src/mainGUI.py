from solver.sudokuSolver import SudokuSolver

def main():
    solver = SudokuSolver(gui=True, show=True)
    solver.GUI.root.mainloop()

if __name__ == "__main__":
    main()