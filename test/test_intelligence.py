"""Unit Test for the Intelligence Module."""

import unittest
from unittest.mock import patch
from game.intelligence import BinaryBrain


class TestPlayerClass(unittest.TestCase):
    """Test the Intelligence class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = BinaryBrain()
        exp = BinaryBrain
        self.assertIsInstance(res, exp)

        binarybrain = BinaryBrain()
        res = binarybrain.difficulty
        exp = 0
        self.assertEqual(exp, res)

        res = binarybrain.player_name
        exp = "BinaryBrain"
        self.assertEqual(exp, res)

    def test_roll_dice(self):
        """Test if the roll_dice method returns a value between 1 and 6."""
        binarybrain = BinaryBrain()

        res = binarybrain.roll_dice()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    def test_update_difficulty(self):
        """Test if you are able to change the AIs difficulty."""
        binarybrain = BinaryBrain()
        binarybrain.update_difficulty(2)

        res = binarybrain.difficulty
        exp = 2
        self.assertEqual(exp, res)

    # def test_difficulty(self):
    #     """Test if the difficulty changes correctly."""
    #     binarybrain = BinaryBrain()
    #
    #     res = binarybrain.evaluate_round.keep_going
    #     exp = binarybrain.easy
    #     self.assertEqual(res, exp)

    @patch('game.intelligence.BinaryBrain.roll_dice')
    def test_roll(self, mock_roll_dice):
        """Test if the AIs roll method works."""
        mock_roll_dice.return_value = 2
        binarybrain = BinaryBrain()

        res = binarybrain.roll()
        self.assertTrue(res)

        mock_roll_dice.return_value = 1
        binarybrain = BinaryBrain()

        res = binarybrain.roll()
        self.assertFalse(res)

    def test_hold(self):
        """Test if the AI can hold its points."""
        binarybrain = BinaryBrain()
        binarybrain.dice_holder.roundpoints = 20
        binarybrain.hold()

        res = binarybrain.dice_holder.get_total_points()
        exp = 20
        self.assertEqual(exp, res)

    def test_easy(self):
        """Test the easy difficulty."""
        binarybrain = BinaryBrain()
        binarybrain.easy()

        res = binarybrain.dice_holder.get_total_points()
        exp = 0 <= res <= 20
        self.assertTrue(exp)
