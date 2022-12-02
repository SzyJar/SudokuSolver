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

    def check_value(self, locationX, locationY):
        for i in range(9):
            if i != locationX:
                if self.value[0][i] == self.value[locationX][locationY]:
                    return(False)
        for j in range(9):        
            if j != locationY:
                if self.value[j][0] == self.value[locationX][locationY]:
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
                        if self.value[i][j] == self.value[locationX][locationY]:
                            return(False)          
        return(True)
        

    def find_values_brute_force(self):
        valueWork = copy.deepcopy(self.value)
        passedAll = 0
        tries = 0
        while(passedAll == 0 and tries < 9999):
            tries = tries + 1
            print(tries)
            passedAll = 1
            for i in range(9):
                for j in range(9):
                    sequence =[1,2,3,4,5,6,7,8,9]
                    passed = 0
                    while(passed == 0 and len(sequence) > 0):
                        if self.value[i][j] == None:
                            valueWork[i][j] = random.choice(sequence)
                            sequence.remove(valueWork[i][j])
                            passed = 1
                            for k in range(9):
                                if k != i:
                                    if valueWork[i][j] == valueWork[k][j]:
                                        passed = 0
                                        passedAll = 0
                                if k != j:
                                    if valueWork[i][j] == valueWork[i][k]:
                                        passed = 0
                                        passedAll = 0                                
                        else:
                            passed = 1
                            
        self.valueCorrect = copy.deepcopy(valueWork)
        
    def generate_values(self, locationX, locationY):
        self.value[locationX][locationY] = random.randrange(0, 9, 1)

