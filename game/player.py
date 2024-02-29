"""The Module with the Player blueprint."""

from dice import Dice
from dicehand import DiceHand


class Player:
    """Blueprint for a Player."""

    def __init__(self, player_name):
        """Beginning of a New Player."""
        self.player_name = player_name
        self.dice_holder = DiceHand()
        self.highscore_least_rolls = 0
        self.highscore_least_rounds = 0

    def reset_player_stats(self):
        """Beginning for an Existing Player."""
        confirmation = input("Proceed with Reset? [y/N] ")
        confirmation.lower()
        if confirmation == "y":
            self.highscore_least_rolls = 0
            self.highscore_least_rounds = 0

    def change_name(self):
        """Alter the Identity of the Player."""
        self.player_name = input("Please enter your new player name: ")

    def roll_dice(self):
        """Decides Fate."""
        dice = Dice()
        # roll_number = dice.roll()

    def return_stats(self):
        """Museum of your previous games."""
