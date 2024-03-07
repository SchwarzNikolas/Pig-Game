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

        res = highscore.lowest_roll
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.lowest_round
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.highest_points

    def test_updated_values(self):
        """Check if values have updated."""
        highscore = Highscore()
        highscore.update_highscore(1, 1, 1, 1)

        exp = 1
        res = highscore.lowest_roll
        self.assertEqual(exp, res)

        exp = 1
        res = highscore.lowest_round
        self.assertEqual(exp, res)

        exp = 1
        res = highscore.highest_points
        self.assertEqual(exp, res)

        exp = 1
        res = highscore.all_time_points
        self.assertEqual(exp, res)

        exp = 1
        res = highscore.all_time_wins
        self.assertEqual(exp, res)

    def test_reset_stats(self):
        """Confirm that the values reset to zero."""
        highscore = Highscore()

        highscore.all_time_points = 1
        highscore.all_time_wins = 1
        highscore.lowest_roll = 1
        highscore.lowest_round = 1
        highscore.highest_points = 1

        highscore.reset_highscore()

        res = highscore.all_time_points
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.all_time_wins
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.lowest_roll
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.lowest_round
        exp = 0
        self.assertEqual(res, exp)

        res = highscore.highest_points
        exp = 0
        self.assertEqual(res, exp)
