import sudoku as sl
import random

def sudokuCoordinates(coords):
    return [int(coords[0]), int(coords[2])]

def is_valid_move(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
        if sudoku[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False
    return True

def generate_sudoku():
    # Initialize an empty 9x9 matrix
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    # Solve the Sudoku puzzle
    solve_sudoku(sudoku)

    # Remove random cells from the solved Sudoku to create the puzzle
    sl.remove_cells(sudoku, 40)

    return sudoku
    
def solve_sudoku(sudoku):
    # Find an empty cell in the Sudoku
    empty_cell = sl.find_empty_cell(sudoku)
    row = empty_cell[0]
    col = empty_cell[1]

    # If all cells are filled, the Sudoku is solved
    if empty_cell == [-1, -1]:
        return sudoku

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    # Loop over these numbers and check it they are valid in the empty cell
    for i in range(9):
        current_guess = numbers[i]
        if is_valid_move(sudoku, row, col, current_guess):
            # Place the number in the empty cell
            sudoku[row][col] = current_guess

            # Recursively solve the Sudoku
            if (solve_sudoku(sudoku) != False):
                return sudoku

            # If the Sudoku cannot be solved, backtrack and try a different number
            sudoku[row][col] = 0
    
    return False

sudoku = generate_sudoku()

while (True):
    sl.display_sudoku(sudoku)

    num = int(input("What number would you like to place?: "))
    position = sudokuCoordinates(input("Where woudld you like to place it? [X,Y]: "))
    
    if is_valid_move(sudoku, position[0], position[1], num):
        sudoku[position[0]][position[1]] = num
    else:
        print("\nThat was not a valid move, make another!\n")
