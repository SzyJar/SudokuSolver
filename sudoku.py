import random

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
        pass

    def enter_value(self, value, locationX, locationY):
        assert type(value) == int, "Value has to be an integer!"
        assert value >= 0 and value <= 9, "Value has to be in range 0 - 9!"

        self.value[locationX][locationY] = value

    def find_values(self, locationX, locationY):
        for i in range(9):
            self.valueCorrect[locationX][locationY]

    def generate_values(self, locationX, locationY):
        self.value[locationX][locationY] = random.randrange(0, 9, 1)

