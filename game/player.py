"""The Module with the Player blueprint."""

from game.dice import Dice
from game.dicehand import DiceHand


class Player:
    """Blueprint for a Player."""

    def __init__(self, player_name):
        """Beginning of a new Player."""
        self.player_name = player_name
        self.dice_holder = DiceHand()
        self.highscore_least_rolls = 0
        self.highscore_least_rounds = 0

    def reset_player_stats(self):
        """Beginning for an existing Player."""
        confirmation = input("Proceed with Reset? [y/N] ")
        confirmation.lower()
        if confirmation == "y":
            self.highscore_least_rolls = 0
            self.highscore_least_rounds = 0

    def change_name(self):
        """Alter the identity of the Player."""
        self.player_name = input("Please enter your new player name: ")

    def roll_dice(self):
        """Decides fate."""
        dice = Dice()
        roll_number = dice.roll()
        self.dice_holder.update_hand(roll_number)
        return roll_number

    def return_stats(self):
        """Museum of your previous games."""
