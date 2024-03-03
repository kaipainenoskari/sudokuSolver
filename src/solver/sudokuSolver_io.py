class sudokuSolverIO:
    def read(self, text):
        input_expression = input(f"{text}")
        return input_expression
    
    def write(self, output, end="\n"):
        if output is not None:
            print(output, end=end)

sudokuSolver_io = sudokuSolverIO()