from Dice import Dice


class ListDice:

    def __init__(self):
        
        self.listDice = []
        
        for i in range(5):
            number = Dice()
            self.listDice.append(number.numbersorted)
        
          
    