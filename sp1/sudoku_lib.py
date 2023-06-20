def display_sudoku(sudoku_board): # PROVIDED
    def repeatCharacter(character, amount):
    for i in range(amount):
        print(character, end="")
    
    # Print the column numbers
    repeatCharacter(" ", 1+2)
    for i in range(9):
        print(f"{i:^3}", end=" ")
    print()

    # Top bar
    repeatCharacter(" ", 1+1)
    repeatCharacter("—", 9*4+1)
    print()
    
    for i in range(9): # Repeat each row
       
        # Print row numbers and cell wall
        print(f"{i:<{1+1}}", end="")
        print(f"|", end="")
        
        for j in range(9): # Repeat each cell
            #Print the number inside the cell and cell walls
            if sudoku_board[i][j] == 0:
                print(f"   ", end="|")
            else:
                print(f" {str(sudoku_board[i][j])} ", end="|")
        print()

        # Print bar between every row
        if i != 9-1:
            repeatCharacter(" ", 1+1)
            repeatCharacter("|———", 9)
            print("|")
        else:
            repeatCharacter(" ", 1+1)
            repeatCharacter("—", 9*4+1)
    print()

def sudokuCoordinates(coords): # STUDENT MADE
    return [int(coords[0]), int(coords[2])]

def is_valid_move(sudoku, row, col, num): # STUDENT MADE
    # Check if 'num' is already present in the row
    for i in range(9):
        if sudoku[row][i] == num:
            return False
        if sudoku[i][column] == num:
            return False

    # Check if 'num' is already present in the 3x3 grid
    """
    1.
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    2.
    if (row == 0 or row == 1 or row == 2):
        start_row = 0
    elif (row == 3 or row == 4 or row == 5):
        start_row = 3
    elif (row == 6 or row == 7 or row == 8):
        start_row = 6

    if (column == 0 or column == 1 or column == 2):
        start_column = 0
    elif (column == 3 or column == 4 or column == 5):
        start_column = 3
    elif (column == 6 or column == 7 or column == 8):
        start_column = 6

    3.
    indexToStart = {
        0: 0,
        1: 0,
        2: 0,
        3: 3,
        4: 3,
        5: 3,
        6: 6,
        7: 6,
        8: 6,
    }
    start_column = indexToStart[column]
    start_row = indexToStart[row]
    """

    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True