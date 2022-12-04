import tkinter as tk
from sudoku import Sudoku
from interface import UI

root = tk.Tk()
root.title("SudokuSolver")
root.minsize(700, 700)
root.iconbitmap('icon.ico')

sudoku = Sudoku()
interface = UI(root, sudoku)

for i in range(9):
    for j in range(9):
        interface.make_box(i, j)

interface.refresh_box()

root.mainloop()
