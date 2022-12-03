import tkinter as tk

class UI:

    def __init__(self, master, sudoku):
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
                                command = lambda:[self.get_all_correct_values(sudoku)])
        self.buttonSolve.place(height = 30, width = 150,
                                relx = 0.5, rely = 0.95)
      
        buttonValidate = tk.Button(self.canvas, text = "Validate", font = ("Arial 14"),
                                command = lambda: self.validate_solution(sudoku))
        buttonValidate.place(height = 30, width = 100,
                             relx = 0.3, rely = 0.95)

        buttonGenerate = tk.Button(self.canvas, text = "Generate", font = ("Arial 14"),
                                command = lambda: self.generate_new_problem(sudoku))
        buttonGenerate.place(height = 30, width = 100,
                             relx = 0.8, rely = 0.95)
        
    def refresh_box(self, sudoku):
        for i in range(9):
            for j in range(9):
                self.edit_box(sudoku.get_value(i, j), i, j, sudoku)

    def generate_new_problem(self, sudoku):
        sudoku.generate_new_problem()
        self.refresh_box(sudoku)

    def get_values(self, sudoku):
        self.refresh_box(sudoku)
        self.buttonShow.destroy()
        self.buttonSolve = tk.Button(self.canvas, text = "Show solution", font = ("Arial 14"),
                                     command = lambda:[self.get_all_correct_values(sudoku)])
        self.buttonSolve.place(height = 30, width = 150,
                               relx = 0.5, rely = 0.95)

    def validate_solution(self, sudoku):
        mistakes = sudoku.validate_solution()
        if sudoku.validate_solution() == 0:
            self.statusInfo.set("No mistakes has been made")
        else:
            self.statusInfo.set(f"{mistakes} mistakes has been found")

    def get_all_correct_values(self, sudoku):
        try:
            sudoku.find_values_brute_force()
            for i in range(9):
                for j in range(9):
                    self.edit_box(sudoku.get_correct_value(i, j), i, j, sudoku)
            self.statusInfo.set("Solution has been found")
            self.buttonSolve.destroy()
            self.buttonShow = tk.Button(self.canvas, text = "Clean solution", font = ("Arial 14"),
                                        command = lambda: self.get_values(sudoku))
            self.buttonShow.place(height = 30, width = 150,
                                  relx = 0.5, rely = 0.95)
        except:
            self.statusInfo.set("Unable to solve sudoku")

    def draw_menu(self, locationX, locationY, sudoku):
        if self.menuIsOpen == 0:
            self.menu = tk.Toplevel()
            self.menu.attributes('-toolwindow', True)
            self.menu.protocol('WM_DELETE_WINDOW', lambda: self.closeWindow(self.menu))
            self.menuIsOpen = 1
            self.menuButton = []
            self.menuNumber = []
            for i in range(3):
                self.menuButton.append([])
                for j in range(3):
                    self.menuButton[i].append(tk.Button(self.menu, text= (j * 3 + i + 1), font = ("Arial 26"),
                                                 command = lambda i = i, j = j: [sudoku.enter_value((j * 3 + i + 1), locationX, locationY),
                                                 self.edit_box(sudoku.get_value(locationX, locationY), locationX, locationY, sudoku),
                                                 self.closeWindow(self.menu)]))
                    self.menuButton[-1][-1].place(height = 50, width = 50,
                                                  relx = 0.05 + 0.3 * i, rely = 0.3 * j)

    def closeWindow(self, window):
        self.menuIsOpen = 0
        window.destroy()

    def edit_box(self, value, locationX, locationY, sudoku):
        self.button[locationX][locationY].destroy()
        self.button[locationX][locationY] = tk.Button(self.canvas, text = value, font = ("Arial 26"),
                                                      command = lambda: self.draw_menu(locationX, locationY, sudoku))
        self.button[locationX][locationY].place(height = 50, width = 50,
                                                relx = 0.05 + 0.1 * locationX, rely = 0.1 * locationY)

    def make_box(self, locationX, locationY):
        self.button[locationX][locationY] = tk.Button(self.canvas,)
        self.button[locationX][locationY].place(height = 50, width = 50,
                                                relx = 0.05 + 0.1 * locationX, rely = 0.1 * locationY)

