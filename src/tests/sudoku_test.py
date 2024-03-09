import os
import unittest
import time
from datetime import datetime
from src.solver.sudokuSolver import SudokuSolver

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.boards = [
            [[0,1,0,0,0,2,0,3,0],[0,4,0,0,0,5,0,0,6],[0,0,0,7,0,0,5,0,0],[8,0,0,0,9,0,0,0,0],[6,0,0,0,0,0,0,0,4],[0,0,0,0,3,0,0,0,7],[0,0,5,0,0,1,0,0,0],[9,0,0,6,0,0,0,8,0],[0,3,0,4,0,0,0,2,0]],
            [[0,0,1,0,2,0,0,0,0],[3,0,0,0,4,0,0,5,0],[0,5,0,0,0,6,0,7,0],[4,0,8,0,0,2,0,0,0],[0,0,9,0,0,0,1,0,0],[0,0,0,5,0,0,8,0,9],[0,6,0,1,0,0,0,2,0],[0,8,0,0,7,0,0,0,4],[0,0,0,0,3,0,9,0,0]],
            [[0,0,1,0,0,2,0,0,0],[0,3,0,0,0,4,0,0,5],[0,0,6,0,5,0,0,7,0],[0,8,0,0,0,5,0,0,0],[0,0,2,0,0,0,4,0,0],[0,0,0,3,0,0,0,9,0],[0,4,0,0,1,0,8,0,0],[9,0,0,4,0,0,0,3,0],[0,0,0,7,0,0,2,0,0]]
        ]

    def test_speed(self):
        execution_times = []
        for board in self.boards:
            solver = SudokuSolver(test=True, board=board)
            start_time = time.time()
            if solver.solve():
                end_time = time.time()
                execution_time = end_time - start_time

                # assert the solver finishes within 5 seconds
                self.assertTrue(execution_time < 5)

                execution_times.append(execution_time)
            else:
                self.fail('Solver failed to solve board')

        # write sum of execution times and individual execution times to a file
        with open('execution_times.txt', 'a') as f:
            f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: {sum(execution_times)}\n')
            for execution_time in execution_times:
                f.write(f'    {execution_time}\n')

if __name__ == '__main__':
    unittest.main()