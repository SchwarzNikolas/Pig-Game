import Dice

class DiceHand:
    def __init__(self):
        self.sum = 0
    
    def rollOneDie(self):
    
        die1 = Dice.Dice  
        roll1 = die1.roll()
        self.sum += roll1
        
        return roll1
        
    def rollTwoDice(self):
        
        die1 = Dice.Dice  
        die2 = Dice.Dice
        roll1 = die1.roll()    
        roll2 = die2.roll()
        
        self.sum += roll1 + roll2
        
        return roll1, roll2