import tkinter as tk
from tkinter import filedialog
from PIL import Image


class UI:

    def __init__(self, master, sudoku):
        self.sudoku = sudoku
        self.menuIsOpen = 0
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

        self.statusInfo=tk.StringVar()
        labelStatus=tk.Label(self.canvas, textvariable = self.statusInfo, font=("Arial 14"), justify="center")
        labelStatus.place(height = 30, relwidth = 0.9, relx = 0.05, rely = 0.9)

        self.buttonSolve = tk.Button(self.canvas, text = "Show solution", font = ("Arial 14"),
                                command = lambda:[self.get_all_correct_values()])
        self.buttonSolve.place(height = 30, width = 150,
                                relx = 0.5, rely = 0.95)
      
        buttonValidate = tk.Button(self.canvas, text = "Validate", font = ("Arial 14"),
                                command = lambda: self.validate_solution())
        buttonValidate.place(height = 30, width = 100,
                             relx = 0.05, rely = 0.95)

        buttonGenerate = tk.Button(self.canvas, text = "Generate new", font = ("Arial 14"),
                                command = lambda: self.draw_generate())
        buttonGenerate.place(height = 30, width = 150,
                             relx = 0.75, rely = 0.95)

        buttonSave = tk.Button(self.canvas, text = "Save sudoku", font = ("Arial 14"),
                                command = lambda: self.draw_print())
        buttonSave.place(height = 30, width = 150,
                             relx = 0.75, rely = 0.9)
    
    def load_images(self):
        self.number = []
        for i in range(10):
            self.number.append(Image.open(f'images/{i}.png'))

    def print_sudoku(self, value):
        outputImage = Image.new('1', (2500,2500), color = 1)
        spaceX = 0
        spaceY = 0
        for i in range(9):
            if i%3 == 0 and i != 0:
                spaceX += 20
            spaceY = 0
            for j in range(9):
                if j%3 == 0 and j != 0:
                    spaceY += 20
                if value[i][j] == None:
                    value[i][j] = 0
                x = 65 + 250 * i + spaceX
                y = 65 + 250 * j + spaceY
                outputImage.paste(self.number[value[i][j]], (x, y))
        path = filedialog.asksaveasfile(defaultextension = '.png', filetypes = [("png image", ".png")])
        outputImage.save(path.name)

    def refresh_box(self):
        for i in range(9):
            for j in range(9):
                self.edit_box(self.sudoku.get_value(i, j), i, j)

    def draw_print(self):
        if self.menuIsOpen == 0:
            self.menu = tk.Toplevel()
            self.menu.minsize(200, 200)
            self.menu.attributes('-toolwindow', True)
            self.menu.attributes('-topmost', True)
            self.menu.title("Save to image")
            self.menu.protocol('WM_DELETE_WINDOW', lambda: self.closeWindow(self.menu))
            self.menuIsOpen = 1
            self.buttonSudoku = tk.Button(self.menu, text = "Print problem", font = ("Arial 14"),
                                command = lambda:[self.print_sudoku(self.sudoku.value)])
            self.buttonSudoku.place(relheight = 0.15, relwidth = 0.9,
                                  relx = 0.05, rely = 0.05)
            self.buttonSolution = tk.Button(self.menu, text = "Print solution", font = ("Arial 14"),
                                command = lambda:[self.print_sudoku(self.sudoku.valueCorrect)])
            self.buttonSolution.place(relheight = 0.15, relwidth = 0.9,
                                  relx = 0.05, rely = 0.25)

    def draw_generate(self):
        if self.menuIsOpen == 0:
            self.menu = tk.Toplevel()
            self.menu.minsize(200, 200)
            
            self.menu.attributes('-toolwindow', True)
            self.menu.attributes('-topmost', True)
            self.menu.title("Generate new")
            self.menu.protocol('WM_DELETE_WINDOW', lambda: self.closeWindow(self.menu))
            self.menuIsOpen = 1
            self.buttonClean = tk.Button(self.menu, text = "Clean sudoku", font = ("Arial 14"),
                                command = lambda:[self.generate_new_problem(81)])
            self.buttonClean.place(relheight = 0.15, relwidth = 0.9,
                                  relx = 0.05, rely = 0.05)
            self.buttonEasy = tk.Button(self.menu, text = "Easy sudoku", font = ("Arial 14"),
                                command = lambda:[self.generate_new_problem(30)])
            self.buttonEasy.place(relheight = 0.15, relwidth = 0.9,
                                  relx = 0.05, rely = 0.25)
            self.buttonHard = tk.Button(self.menu, text = "Hard sudoku", font = ("Arial 14"),
                                command = lambda:[self.generate_new_problem(50)])
            self.buttonHard.place(relheight = 0.15, relwidth = 0.9,
                                  relx = 0.05, rely = 0.45)

    def generate_new_problem(self, count):
        self.sudoku.generate_new_problem()
        self.get_all_correct_values()
        self.sudoku.clear_values(count)
        self.get_all_correct_values()
        self.clean_solution()
        if self.sudoku.check_for_extra_solution() == True:
            self.generate_new_problem(count)
        self.clean_solution()
        self.refresh_box()
        
    def clean_solution(self):
        self.refresh_box()
        self.buttonShow.destroy()
        self.buttonSolve = tk.Button(self.canvas, text = "Show solution", font = ("Arial 14"),
                                     command = lambda:[self.get_all_correct_values()])
        self.buttonSolve.place(height = 30, width = 150,
                               relx = 0.5, rely = 0.95)

    def validate_solution(self):
        mistakes = self.sudoku.validate_solution()
        if self.sudoku.validate_solution() == 0:
            self.statusInfo.set("No mistakes has been made")
        else:
            self.statusInfo.set(f"{mistakes} mistakes has been found")

    def get_all_correct_values(self):
        try:
            self.sudoku.find_values_brute_force()
            for i in range(9):
                for j in range(9):
                    self.edit_box(self.sudoku.get_correct_value(i, j), i, j)
            self.statusInfo.set("One solution has been found")
            self.buttonSolve.destroy()
            self.buttonShow = tk.Button(self.canvas, text = "Clean solution", font = ("Arial 14"),
                                        command = lambda: self.clean_solution())
            self.buttonShow.place(height = 30, width = 150,
                                    relx = 0.5, rely = 0.95)
            if self.sudoku.check_for_extra_solution() == True:
                self.statusInfo.set(f"Found more than one solution")
        except:
            self.statusInfo.set("Unable to solve sudoku")
        
    def draw_menu(self, locationX, locationY):
        if self.menuIsOpen == 0:
            self.menu = tk.Toplevel()
            self.menu.minsize(250, 250)
            self.menu.attributes('-toolwindow', True)
            self.menu.attributes('-topmost', True)
            self.menu.title(f"Edit number:  x[{locationX + 1}]  y[{locationY + 1}]  current = {self.sudoku.get_value(locationX, locationY)}")
            self.menu.protocol('WM_DELETE_WINDOW', lambda: self.closeWindow(self.menu))
            self.menuIsOpen = 1
            self.menuButton = []
            self.menuNumber = []
            for i in range(3):
                self.menuButton.append([])
                for j in range(3):
                    self.menuButton[i].append(tk.Button(self.menu, text= (j * 3 + i + 1), font = ("Arial 26"),
                                                 command = lambda i = i, j = j: [self.sudoku.enter_value((j * 3 + i + 1), locationX, locationY),
                                                 self.edit_box(self.sudoku.get_value(locationX, locationY), locationX, locationY),
                                                 self.closeWindow(self.menu)]))
                    self.menuButton[-1][-1].place(relheight = 0.2, relwidth = 0.2,
                                                  relx = 0.08 + 0.3 * i, rely = 0.3 * j)
            self.noneButton = tk.Button(self.menu, text = "Erase value", font = ("Arial 22"),
                                        command = lambda: [self.sudoku.enter_value(None, locationX, locationY),
                                                 self.edit_box(self.sudoku.get_value(locationX, locationY), locationX, locationY),
                                                 self.closeWindow(self.menu)])
            self.noneButton.place(relheight = 0.14, relwidth = 0.86,
                                  relx = 0.05, rely = 0.85)

    def closeWindow(self, window):
        self.menuIsOpen = 0
        window.destroy()

    def edit_box(self, value, locationX, locationY):
        self.button[locationX][locationY].destroy()
        self.button[locationX][locationY] = tk.Button(self.canvas, text = value, font = ("Arial 26"),
                                                      command = lambda: self.draw_menu(locationX, locationY))
        self.button[locationX][locationY].place(relheight = 0.071, relwidth = 0.071,
                                                relx = 0.05 + 0.1 * locationX, rely = 0.1 * locationY)

    def make_box(self, locationX, locationY):
        self.button[locationX][locationY] = tk.Button(self.canvas)
        self.button[locationX][locationY].place(height = 50, width = 50,
                                                relx = 0.05 + 0.1 * locationX, rely = 0.1 * locationY)

