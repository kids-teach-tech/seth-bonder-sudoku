import random

def display_sudoku(sudoku_board):
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

def repeatCharacter(character, amount): # Repeats a character a certain amount of times
    for i in range(amount):
        print(character, end="")

def generate_sudoku(difficulty=40):
    # Initialize an empty 9x9 matrix
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    # Solve the Sudoku puzzle
    solve_sudoku(sudoku)

    # Remove random cells from the solved Sudoku to create the puzzle
    remove_cells(sudoku, difficulty)

    return sudoku

def solve_sudoku(sudoku):
    # Find an empty cell in the Sudoku
    row, col = find_empty_cell(sudoku)

    # If all cells are filled, the Sudoku is solved
    if row == -1 and col == -1:
        return True

    # Generate random numbers from 1 to 9 -> UNIQUE
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    for num in numbers:
        if is_valid_move(sudoku, row, col, num):
            # Place the number in the empty cell
            sudoku[row][col] = num

            # Recursively solve the Sudoku
            if solve_sudoku(sudoku):
                return True

            # If the Sudoku cannot be solved, backtrack and try a different number
            sudoku[row][col] = 0

    return False

def find_empty_cell(sudoku):
    # Find and return the coordinates of the first empty cell (cell with 0 value)
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return -1, -1

def sudokuCoordinates(coords):
    return [int(coords[0]), int(coords[2])]

def is_valid_move(sudoku, row, col, num):
    # Check if 'num' is already present in the row
    for i in range(9):
        if sudoku[row][i] == num:
            return False

    # Check if 'num' is already present in the column
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # Check if 'num' is already present in the 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

def remove_cells(sudoku, cells_to_remove):
    # Remove random cells from the solved Sudoku
    # The number of cells to be removed can vary depending on the desired difficulty level

    for _ in range(cells_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        sudoku[row][col] = 0