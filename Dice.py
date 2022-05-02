import random


class Dice():


    def __init__(self):
        
        self.numbersorted = 0
        
        for i in range(5):
            self.numbersorted = random.randint(1, 6)
       
    