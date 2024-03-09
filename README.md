# Sudoku Solver

This is a Sudoku Solver project that aims to solve Sudoku puzzles programmatically.

## Introduction

In this project, we have implemented an algorithm to solve Sudoku puzzles. The solver takes an incomplete Sudoku puzzle as input and returns the solved puzzle as output.

## Features

- Solve Sudoku puzzles of varying difficulty levels
- Efficient algorithm for solving puzzles
- Command-line interface for easy interaction

## Installation

To use the Sudoku Solver, you need to have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

1. Clone the repository:

    ```bash
    git clone https://github.com/kaipainenoskari/sudokuSolver.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sudokuSolver/src
    ```

## Usage

To solve a Sudoku puzzle, run either of the following commands:

Text-based UI
```bash
python main.py
```
Graphical UI
```bash
python mainGUI.py
```

To test the speed of the algorithm and to save the results make sure you're in the project root and run:

```bash
python -m unittest discover -s src -p '*_test.py'
```
