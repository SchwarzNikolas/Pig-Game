"""Module for implementing game intelligence algorithms."""

import random
from game.dice import Dice
from game.dicehand import DiceHand


class BinaryBrain:
    """
    Class for the computer player.

    Can act as an additional player.
    Difficulty can be adjusted between:
    -easy
    -medium
    -hard
    """

    def __init__(self):
        """
        Beginning of the AI.

        Create AI's dicehand object, set its name and difficulty.
        Additionally set the random seed.
        """
        self.dice_holder = DiceHand()
        self.player_name = "BinaryBrain"
        self.difficulty = 0
        random.seed()

    def roll_dice(self):
        """
        AI rolls the dice.

        Call the roll method on the dice object.
        Update the dicehand with the rolled number.
        Method returns the rolled number.
        """
        dice = Dice()
        roll_number = dice.roll()
        self.dice_holder.update_hand(roll_number)
        return roll_number

    def update_difficulty(self, difficulty):
        """
        Set the difficulty of the AI.

        Change the difficulty level according to the parameter.
        Can can range from 0-2, where 0 is the easiest difficulty.
        """
        self.difficulty = difficulty

    def evaluate_round(self):
        """
        Let the AI play its turn.

        Loop which runs until the AI decides to hold its points or rolls a 1.
        Starts a different algorithm according to the difficulty varaible.
        """
        keep_going = True
        while keep_going:
            match self.difficulty:
                case 0:
                    keep_going = self.easy()
                case 1:
                    keep_going = self.medium()
                case 2:
                    keep_going = self.hard()

    def roll(self):
        """
        Roll the dice and evaluate result.

        Rolls the dice, evaluates and prints out result.
        """
        roll = self.roll_dice()
        round_points = self.dice_holder.get_round_points()
        total_points = self.dice_holder.get_total_points()
        if roll == 1:
            print("BinaryBrain has rolled a 1 and lost its round points.")
            print(f"\nTotal score: {total_points}\n")
            return False
        print(f"BinaryBrain has rolled a {roll}.")
        points = f"Round score: {round_points}"
        score = f"\nTotal score: {total_points}\n"
        print(points + score)
        return True

    def hold(self):
        """
        Hold the round points.

        AI decides to transver the round points to its total points.
        Print out the results afterwards.
        """
        self.dice_holder.hold()
        total_points = self.dice_holder.get_total_points()
        print("\nBinaryBrain has kept its points.")
        print(f"Its total score is now: {total_points}")

    def easy(self):
        """
        Easiest difficulty level of the AI.

        The AI will always roll until it has 15 round points.
        After it reaches 15 points it will hold.
        If the AI rolls a one or holds it will return False,
        so that the playing loop stops.
        """
        if self.dice_holder.get_round_points() < 15:
            return self.roll()
        self.hold()
        return False

    def medium(self):
        """
        Medium difficulty level of the AI.

        The AI will always roll until it has 20 round points.
        After it reaches 20 points it will hold.
        If the AI rolls a one or holds it will return False,
        so that the playing loop stops.
        """
        if self.dice_holder.get_round_points() < 15:
            return self.roll()
        self.hold()
        return False

    def hard(self):
        """
        Hard difficulty level of the AI.

        AI will always roll until it has 20 points,
        between 20 and 25 points it will randomly decide if it wants
        to hold or to continue playing.
        If the AI has 70 total points it will roll until it wins.
        If the AI rolls a one or holds it will return False, so that the
        playing loop stops.
        """
        if self.dice_holder.get_total_points() > 70:
            if self.dice_holder.get_round_points() >= 29:
                self.hold()
                return False
            return self.roll()
        if self.dice_holder.get_round_points() < 20:
            return self.roll()
        if self.dice_holder.get_round_points() < 26:
            decision = random.randint(0, 1)
            if decision == 1:
                return self.roll()
        self.hold()
        return False
