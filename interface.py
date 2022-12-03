import tkinter as tk

class UI:

    def __init__(self, master):
        
        self.canvas = tk.Canvas(master)
        self.canvas.place(relwidth = 1, relheight = 1)
        self.frame1 = tk.Frame(self.canvas, bg = '#000000')
        self.frame2 = tk.Frame(self.canvas, bg = '#000000')
        self.frame3 = tk.Frame(self.canvas, bg = '#000000')
        self.frame4 = tk.Frame(self.canvas, bg = '#000000')
        self.frame1.place(width = 3, relheight = 0.9, relx = 0.335, rely = 0)
        self.frame2.place(width = 3, relheight = 0.9, relx = 0.635, rely = 0)
        self.frame3.place(relwidth = 0.9, height = 3, relx = 0.05, rely = 0.28)
        self.frame4.place(relwidth = 0.9, height = 3, relx = 0.05, rely = 0.58)
        self.button = []
        for i in range(9):
            self.button.append([])
            for j in range(9):
                self.button[i].append(None)

    def edit_box(self,value, locationX, locationY, sudoku):
        self.button[locationX][locationY].destroy()
        self.button[locationX][locationY] = tk.Button(self.canvas, text = value, font = ("Arial 26"),
                                                      command = lambda: print(sudoku.check_value(locationX, locationY, sudoku.value)))
        self.button[locationX][locationY].place(height = 50, width = 50,
                                                relx = 0.05 + 0.1 * locationX, rely = 0.1 * locationY)

    def make_box(self, locationX, locationY):
        self.button[locationX][locationY] = tk.Button(self.canvas,)
        self.button[locationX][locationY].place(height = 50, width = 50,
                                                relx = 0.05 + 0.1 * locationX, rely = 0.1 * locationY)

