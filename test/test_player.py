"""Unit Test for the Player Module."""

import unittest
from unittest import mock
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
        player = Player("Test")

        player.highscores.all_time_points = 1
        player.highscores.all_time_wins = 1
        player.highscores.lowest_roll = 1
        player.highscores.lowest_round = 1
        player.highscores.highest_points = 1

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "y"
        player.reset_player_stats()
        mock.builtins.input = original_input

        res = player.highscores.all_time_points
        exp = 0
        self.assertEqual(res, exp)

        res = player.highscores.all_time_wins
        exp = 0
        self.assertEqual(res, exp)

        res = player.highscores.lowest_roll
        exp = 0
        self.assertEqual(res, exp)

        res = player.highscores.lowest_round
        exp = 0
        self.assertEqual(res, exp)

        res = player.highscores.highest_points
        exp = 0
        self.assertEqual(res, exp)

    def test_change_name(self):
        """Test if the Player's name changed."""
        player = Player("Test")
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "Test1"
        player.change_name()
        res = player.player_name
        exp = "Test1"
        self.assertEqual(exp, res)
        mock.builtins.input = original_input

    def test_roll_dice(self):
        """Method to validate dice roll."""
        player = Player("Test")
        res = player.roll_dice()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_return_stats(self):
        """Test if statistics are shown."""
        player = Player("Test")

        player.highscores.all_time_points = 1
        player.highscores.all_time_wins = 1
        player.highscores.lowest_roll = 1
        player.highscores.lowest_round = 1
        player.highscores.highest_points = 1

        res1, res2, res3, res4, res5 = player.return_stats()
        exp = 1
        self.assertEqual(res1, exp)
        self.assertEqual(res2, exp)
        self.assertEqual(res3, exp)
        self.assertEqual(res4, exp)
        self.assertEqual(res5, exp)

    def test_update_stats(self):
        """Test if statistics are updated."""
        player = Player("Test")
        player.dice_holder.totalpoints = 1
        player.dice_holder.amountofrolls = 1
        player.dice_holder.rounds = 1

        player.update_scores(1)

        res = player.highscores.all_time_points
        exp = 1
        self.assertEqual(res, exp)

        res = player.highscores.all_time_wins
        exp = 1
        self.assertEqual(res, exp)

        res = player.highscores.lowest_roll
        exp = 1
        self.assertEqual(res, exp)

        res = player.highscores.lowest_round
        exp = 1
        self.assertEqual(res, exp)

        res = player.highscores.highest_points
        exp = 1
        self.assertEqual(res, exp)
