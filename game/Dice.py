import random

class Dice:
    def __init__(self):
        self.num = 0
        
    def roll(self):
        return random.randint(1, 6)
    
