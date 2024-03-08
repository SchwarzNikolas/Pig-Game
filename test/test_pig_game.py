"""Unit Test for the pig-game Module."""

import unittest
from unittest.mock import patch
from game.pig_game import Game


class TestGameClass(unittest.TestCase):
    """Test the pig-game class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)
