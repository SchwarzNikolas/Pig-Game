"""Representing a dice object for rolling."""


import random


class Dice:
    """This here the dice."""

    def __init__(self):
        """Initialize object."""
        self.num = 0

    def roll(self):
        """Roll the dice and return the result."""
        return random.randint(1, 6)
