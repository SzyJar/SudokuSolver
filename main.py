import tkinter as tk
from sudoku import Sudoku
from interface import UI

root = tk.Tk()
root.title("SudokuSolver")
root.minsize(700, 700)
root.iconbitmap('icon.ico')

sudoku = Sudoku()
interface = UI(root, sudoku)

sudoku.enter_value(4, 0, 0)
sudoku.enter_value(5, 8, 0)

sudoku.enter_value(4, 4, 1)
sudoku.enter_value(1, 5, 1)
sudoku.enter_value(6, 6, 1)

sudoku.enter_value(8, 1, 2)
sudoku.enter_value(1, 2, 2)
sudoku.enter_value(6, 3, 2)
sudoku.enter_value(3, 4, 2)

sudoku.enter_value(3, 3, 3)
sudoku.enter_value(1, 6, 3)

sudoku.enter_value(1, 0, 4)
sudoku.enter_value(9, 1, 4)
sudoku.enter_value(8, 6, 4)
sudoku.enter_value(7, 8, 4)

sudoku.enter_value(5, 1, 5)
sudoku.enter_value(4, 2, 5)
sudoku.enter_value(7, 5, 5)
sudoku.enter_value(6, 8, 5)

sudoku.enter_value(8, 0, 6)
sudoku.enter_value(2, 1, 6)
sudoku.enter_value(5, 2, 6)
sudoku.enter_value(1, 4, 6)
sudoku.enter_value(9, 5, 6)
sudoku.enter_value(7, 6, 6)
sudoku.enter_value(6, 7, 6)

sudoku.enter_value(8, 3, 7)
sudoku.enter_value(5, 6, 7)
sudoku.enter_value(9, 7, 7)

sudoku.enter_value(6, 0, 8)
sudoku.enter_value(1, 1, 8)
sudoku.enter_value(5, 3, 8)
sudoku.enter_value(7, 4, 8)
sudoku.enter_value(3, 5, 8)
sudoku.enter_value(2, 6, 8)
sudoku.enter_value(4, 7, 8)

for i in range(9):
    for j in range(9):
        interface.make_box(i, j)

interface.refresh_box(sudoku)

root.mainloop()
