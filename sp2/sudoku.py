import sudoku_lib as sl

sudoku = sl.generate_sudoku()

while True:
    sl.display_sudoku(sudoku)

    num = int(input("What number would you like to place?: "))
    position = sl.sudokuCoordinates(input("Where woudld you like to place it? [X,Y]: "))
    
    if sl.is_valid_move(sudoku, position[0], position[1], num):
        sudoku[position[0]][position[1]] = num
    else:
        print("\nThat was not a valid move, make another!\n")