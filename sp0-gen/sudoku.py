import sudoku_lib as sl

sudoku = []
for i in range(10):
    sudoku.append(sl.generate_sudoku((i*6)+20))
print(sudoku)

"""
sl.display_sudoku(sudoku[0])
sl.display_sudoku(sudoku[9])
"""