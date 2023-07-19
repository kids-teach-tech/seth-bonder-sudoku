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

sudoku = sl.generate_sudoku()

while (True):
    sl.display_sudoku(sudoku)

    num = int(input("What number would you like to place?: "))
    position = sudokuCoordinates(input("Where woudld you like to place it? [X,Y]: "))
    
    if is_valid_move(sudoku, position[0], position[1], num):
        sudoku[position[0]][position[1]] = num
    else:
        print("\nThat was not a valid move, make another!\n")
