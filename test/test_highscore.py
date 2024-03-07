"""Unit Test for the Highscore Module."""

import unittest
from game.highscore import Highscore


class TestHighscoreClass(unittest.TestCase):
    """Test the Highscore class."""

    def test_init_default_object(self):
        """Instantiate an object and test the instantiation."""
        res = Highscore()
        exp = Highscore
        self.assertIsInstance(res, exp)

    def test_if_zero(self):
        """Confirm that the values start at zero."""
        highscore = Highscore()

        res = highscore.all_time_points
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.all_time_wins
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.lowest_roll_count
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.lowest_round_count
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.highest_points_in_one_round
        exp = 0
        self.assertEqual(res, exp)

    def test_updated_values(self):
        highscore = Highscore()
        highscore.update_highscore()