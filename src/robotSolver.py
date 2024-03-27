from time import sleep
from robocorp import browser
from robocorp.tasks import task
from solver.sudokuSolver import SudokuSolver

URL = "https://www.nytimes.com/puzzles/sudoku/hard"

@task
def solve_challenge():
    """Solve the Sudoku challenge"""
    open_browser()
    board = create_board()
    solver = SudokuSolver(board=board, browser=browser)
    if solver.solve_with_robot():
        print("Sudoku solved!")
    sleep(5)

def open_browser():
    browser.configure(
        browser_engine="chromium",
        slowmo=0,
    )
    page = browser.goto(URL)
    page.wait_for_selector("//button[contains(text(),'Accept all')]").click()
    page.wait_for_selector("//button[contains(text(),'Normal')]").click()
    sleep(1)

def create_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            cell = browser.page().locator(f'//div[@data-cell="{(i * 9) + j}"]').element_handle()
            number = cell.get_attribute("aria-label")
            row.append(int(number) if number != "empty" else 0)
        board.append(row)
    return board

if __name__ == "__main__":
    solve_challenge()