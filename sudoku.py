import random
import copy

class Sudoku:
    
    def __init__(self):
        self.value = []
        self.valueCorrect = []
        for i in range(9):
            self.value.append([])
            self.valueCorrect.append([])
            for j in range(9):
                self.value[i].append(None)
                self.valueCorrect[i].append(None)

    def get_value(self, locationX, locationY):
        return(self.value[locationX][locationY])

    def get_correct_value(self, locationX, locationY):
        return(self.valueCorrect[locationX][locationY])

    def enter_value(self, value, locationX, locationY):
        assert type(value) == int, "Value has to be an integer!"
        assert value >= 0 and value <= 9, "Value has to be in range 0 - 9!"

        self.value[locationX][locationY] = value

    def check_value(self, locationX, locationY, sudoku):
        for i in range(9):
            if i != locationX:
                if sudoku[i][locationY] == sudoku[locationX][locationY]:
                    return(False)
        for j in range(9):
            if j != locationY:
                if sudoku[locationX][j] == sudoku[locationX][locationY]:
                    return(False)

        if locationX in [0, 1, 2]:
            locX = [0,1,2]
        elif locationX in [3, 4, 5]:
            locX = [3,4,5]
        elif locationX in [6, 7, 8]:
            locX = [6,7,8]
        if locationY in [0, 1, 2]:
            locY = [0,1,2]
        elif locationY in [3, 4, 5]:
            locY = [3,4,5]
        elif locationY in [6, 7, 8]:
            locY = [6,7,8]

        for i in locX:
            for j in locY:
                if i != locationX and j != locationY:
                        if sudoku[i][j] == sudoku[locationX][locationY]:
                            return(False)          
        return(True)
        
    def find_values_brute_force(self):
        valueWork = copy.deepcopy(self.value)
        nextNumber = []

        for i in range(9):
            nextNumber.append([])
            for j in range(9):
                nextNumber[i].append(1)

        i = 0
        j = 0
        forward = 1
        while j <= 8 and i <= 8:
            if self.value[i][j] == None:
                valueWork[i][j] = nextNumber[i][j]
                nextNumber[i][j] = nextNumber[i][j] + 1
                if self.check_value(i, j, valueWork) == False or valueWork[i][j] > 9:
                    if valueWork[i][j] >= 9:
                        valueWork[i][j] = None
                        nextNumber[i][j] = 1
                        if j > 0:
                            j = j - 1 
                        else:
                            j = 8
                            i = i - 1
                    forward = 0
                else:
                    if j < 8:
                        j = j + 1
                    else:
                        j = 0
                        i = i + 1
                    forward = 1
            else:
                if forward == 1:
                    if j < 8:
                        j = j + 1
                    else:
                        j = 0
                        i = i + 1
                elif forward == 0:
                    if j > 0:
                        j = j - 1
                    else:
                        j = 8
                        i = i - 1
                                              
        self.valueCorrect = copy.deepcopy(valueWork)

    def validate_solution(self):
        mistake = 0
        if None in self.valueCorrect:
            self.find_values_brute_force()

        for i in range(9):
            for j in range(9):
                if self.valueCorrect[i][j] != self.value[i][j] and self.value[i][j] != None:
                    mistake += 1
        return(mistake)

    def generate_new_problem(self):
        newProblem = []
        for i in range(9):
            newProblem.append([])
            for j in range(9):
                newProblem[i].append(None)

        for i in range(8):
            j = random.randrange(0, 8, 1)
            k = random.randrange(0, 8, 1)
            newProblem[j][k] = random.randrange(1, 9, 1)
            if self.check_value(j, k, newProblem) != True:
                newProblem[j][k] = random.randrange(1, 9, 1)
        self.value = copy.deepcopy(newProblem)

