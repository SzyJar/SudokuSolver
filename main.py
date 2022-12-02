import tkinter as tk
from sudoku import Sudoku


root = tk.Tk()
root.title("Sudoku")
root.minsize(600, 700)

class UI:

    def __init__(self, master):
        
        self.canvas = tk.Canvas(master)
        self.canvas.place(relwidth = 1, relheight = 1)

        self.button = []
        for i in range(9):
            self.button.append([])
            for j in range(9):
                self.button[i].append(None)

    def edit_box():
        pass

    def make_box(self, locationX, locationY):
        self.button[locationX][locationY] = tk.Button(self.canvas)
        self.button[locationX][locationY].place(height = 50, width = 50,
                                                relx = 0.05 + 0.1 * locationX, rely = 0.1 * locationY)

interface = UI(root)
for i in range(9):
    for j in range(9):
        interface.make_box(i, j)


sudoku1 = Sudoku()
sudoku1.enter_value(5, 0, 0)
print(sudoku1.get_value(0, 0))
#sudoku1.find_value(1, 1)
print(sudoku1.get_value(1, 1))

root.mainloop()
