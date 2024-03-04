"""Module for implementing game intelligence algorithms."""

from game.dice import Dice
from game.dicehand import DiceHand
import random


class BinaryBrain:
    """Class for the computer player."""

    def __init__(self):
        """Beginning of a new Player."""
        self.dice_holder = DiceHand()
        self.player_name = "BinaryBrain"
        self.difficulty = 0
        random.seed()

    def roll_dice(self):
        dice = Dice()
        roll_number = dice.roll()
        self.dice_holder.update_Hand(roll_number)
        return roll_number

    def update_difficulty(self, difficulty):
        self.difficulty = difficulty

    def evaluate_round(self):
        while True:
            if self.difficulty == 0:
                if self.dice_holder.get_roundPoints() < 15:
                    roll = self.roll_dice()
                    if roll == 1:
                        print("\nBinaryBrain has rolled a one and has lost all its round points.")
                        return
                    else:
                        print(f"BinaryBrain has rolled a {roll}.")
                        points = f"Round score: {self.dice_holder.get_roundPoints()}"
                        score = f"\nTotal score: {self.dice_holder.get_totalPoints()}\n"
                        print(points + score)
                else:
                    self.dice_holder.hold()
                    print("\nBinaryBrain has kept its points.")
                    print(f"Its total score is now: {self.dice_holder.get_totalPoints()}")
                    return
