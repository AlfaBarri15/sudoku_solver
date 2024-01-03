from sudoku_builder import SudokuBuilder
from sudoku_solver import SudokuSolver


def main():
    sudoku_builder = SudokuBuilder()
    sudoku_solver = SudokuSolver(sudoku_builder.side, sudoku_builder.board)
    sudoku_solver.solve_brute_force()
    sudoku_solver.print_grid()


if __name__ == '__main__':
    main()