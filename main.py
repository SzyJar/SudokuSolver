import tkinter as tk
from sudoku import Sudoku

root = tk.Tk()

root.title("Sudoku")

frame = tk.Frame(root)
frame.place(relwidth = 1, relheight = 1)
root.mainloop()