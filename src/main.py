from solver.sudokuSolver import SudokuSolver

def main():
    solver = SudokuSolver()
    solver.solve()
    solver.print_board()

if __name__ == "__main__":
    main()