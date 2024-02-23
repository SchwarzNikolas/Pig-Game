"We rolling dice baby"
import random


class Dice:
    "This here the dice"
    def __init__(self):
        self.num = 0
        
    def roll(self):
        return random.randint(1, 6)
    
