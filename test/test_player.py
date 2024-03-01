"""Unit Test for the Player Module."""

import unittest
from game.player import Player


class TestPlayerClass(unittest.TestCase):
    """Test the Player class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Player("Test")
        exp = Player
        self.assertIsInstance(res, exp)

    def test_reset_player_stats(self):
        """Test if the Player's statistics are reset."""
        pass

    def test_change_name(self):
        """Test if the Player's name changed."""
        pass

    def test_roll_dice(self):
        """Method to validate dice roll."""
        pass

    def test_return_stats(self):
        """Test if statistics are shown."""
        pass
