"""Unit Test for the Intelligence Module."""

import unittest
from unittest.mock import patch
from game.intelligence import BinaryBrain


class TestIntelligenceClass(unittest.TestCase):
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

    @patch('game.intelligence.BinaryBrain.easy')
    def test_difficulty_easy(self, mock_easy):
        """Test if the difficulty changes correctly."""
        mock_easy.return_value = False
        binarybrain = BinaryBrain()
        binarybrain.difficulty = 0
        binarybrain.evaluate_round()
        res = binarybrain.keep_going
        self.assertFalse(res)

    @patch('game.intelligence.BinaryBrain.medium')
    def test_difficulty_medium(self, mock_medium):
        """Test if the difficulty changes correctly."""
        mock_medium.return_value = False
        binarybrain = BinaryBrain()
        binarybrain.difficulty = 1
        binarybrain.evaluate_round()
        res = binarybrain.keep_going
        self.assertFalse(res)

    @patch('game.intelligence.BinaryBrain.hard')
    def test_difficulty_hard(self, mock_hard):
        """Test if the difficulty changes correctly."""
        mock_hard.return_value = False
        binarybrain = BinaryBrain()
        binarybrain.difficulty = 2
        binarybrain.evaluate_round()
        res = binarybrain.keep_going
        self.assertFalse(res)

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

    def test_easy_hold(self):
        """Test the easy difficulties hold abilty."""
        binarybrain = BinaryBrain()
        binarybrain.dice_holder.roundpoints = 20
        res = binarybrain.easy()
        self.assertFalse(res)

    @patch('game.intelligence.BinaryBrain.roll')
    def test_easy_roll(self, mock_roll):
        """Test the easy difficulties roll abilty."""
        mock_roll.return_value = True
        binarybrain = BinaryBrain()
        res = binarybrain.easy()
        self.assertTrue(res)

    def test_medium_hold(self):
        """Test the medium difficulties hold abilty."""
        binarybrain = BinaryBrain()
        binarybrain.dice_holder.roundpoints = 25
        res = binarybrain.medium()
        self.assertFalse(res)

    @patch('game.intelligence.BinaryBrain.roll')
    def test_medium_roll(self, mock_roll):
        """Test the easy difficulties roll abilty."""
        mock_roll.return_value = True
        binarybrain = BinaryBrain()
        res = binarybrain.medium()
        self.assertTrue(res)

    def test_hard_hold(self):
        """Test the hard difficulties hold abilty."""
        binarybrain = BinaryBrain()
        binarybrain.dice_holder.roundpoints = 30
        res = binarybrain.hard()
        self.assertFalse(res)

        binarybrain.dice_holder.totalpoints = 72
        binarybrain.dice_holder.roundpoints = 28
        res = binarybrain.hard()
        self.assertFalse(res)

    @patch('game.intelligence.BinaryBrain.roll')
    @patch('random.randint')
    def test_hard_roll(self, mock_roll, mock_random):
        """Test the hard difficulties roll abilty."""
        mock_roll.return_value = True
        mock_random.return_value = 1
        binarybrain = BinaryBrain()
        binarybrain.dice_holder.roundpoints = 24
        res = binarybrain.hard()
        self.assertTrue(res)

        binarybrain.dice_holder.roundpoints = 18
        res = binarybrain.hard()
        self.assertTrue(res)

        binarybrain.dice_holder.totalpoints = 72
        binarybrain.dice_holder.roundpoints = 18
        res = binarybrain.hard()
        self.assertTrue(res)
