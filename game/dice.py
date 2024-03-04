"""Representing a dice object for rolling."""

import random


class Dice:
    """This here the dice."""

    def __init__(self):
        """Initialize object."""
        random.seed()

    def roll(self):
        """Roll the dice and return the result."""
        return random.randint(1, 6)
