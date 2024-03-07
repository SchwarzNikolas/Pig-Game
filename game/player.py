"""The Module with the Player blueprint."""

from game.dice import Dice
from game.dicehand import DiceHand
from game.highscore import Highscore


class Player:
    """Blueprint for a Player."""

    def __init__(self, player_name):
        """Beginning of a new Player."""
        self.player_name = player_name
        self.dice_holder = DiceHand()
        self.highscores = Highscore()

    def reset_player_stats(self):
        """Beginning for an existing Player."""
        confirmation = input("Proceed with Reset? [y/N] ")
        confirmation.lower()
        if confirmation == "y":
            self.highscores.reset_highscore()

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
        lowest_roll, lowest_round = self.highscores.return_low_stats()
        highest_points = self.highscores.return_high_stats()
        wins, all_time_points = self.highscores.return_all_time_stats()
        return lowest_roll, lowest_round, highest_points, wins, all_time_points

    def update_scores(self, win):
        """Update museum after finished game."""
        rolls = self.dice_holder.get_amount_of_rolls()
        rounds = self.dice_holder.get_total_points()
        points = self.dice_holder.get_rounds()

        self.highscores.update_highscore(rolls, rounds, points, win)
