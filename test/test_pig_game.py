"""Unit Test for the remaining untested parts of the pig-game Module."""

import unittest
import io
import sys
from unittest.mock import patch
from game.pig_game import Game
from game.player import Player


class TestGameClass(unittest.TestCase):
    """Test the pig-game class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_no_saved_players(self, mock_open, mock_stdout):
        """Test starting the game without a old player save."""
        game = Game()
        res = mock_stdout.getvalue()
        exp = "No saved players found.\n"
        self.assertEqual(exp, res)

    def test_start_no_profile(self):
        """Test if the game will not start if a player doesnt have a profile."""
        sys.stdout = io.StringIO()
        game = Game()
        res = game.start("Test")
        self.assertFalse(res)
        sys.stdout = sys.__stdout__

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_create_player(self, mock_stdout):
        """Test the profile creation method."""
        game = Game()
        game.create_player(["Test"])
        res = mock_stdout.getvalue()
        exp = "Player Test has been created!\n"
        self.assertEqual(exp, res)

    def test_disable_ai(self):
        """Test if the AI can be disabled."""
        sys.stdout = io.StringIO()
        game = Game()
        game.set_ai("false", "-h")
        res = game.active_ai
        exp = 0
        self.assertEqual(exp, res)
        sys.stdout = sys.__stdout__

    def test_ai_win(self):
        """Test if the AI can win the game."""
        sys.stdout = io.StringIO()
        game = Game()
        game.ai.dice_holder.totalpoints = 102
        game.play_ai()
        res = game.game_state
        exp = -1
        self.assertEqual(exp, res)
        sys.stdout = sys.__stdout__

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_restart_no_save(self, mock_stdout):
        """Test if the game can be restarted without a saved game."""
        game = Game()
        game.restart()
        res = mock_stdout.getvalue()
        exp = "There is no paused game!\n"
        self.assertEqual(exp, res)

    def test_player_hold(self):
        """Test the hold method of the player."""
        game = Game()
        game.game_state = 0
        game.active_players.append(Player("Test"))
        game.active_players[0].dice_holder.totalpoints = 100
        res = game.hold()
        exp = "Test has won the game!"
        self.assertEqual(exp, res)

        game.amount_players = 1
        game.game_state = 0
        game.active_players.append(Player("Test"))
        game.active_players[0].dice_holder.totalpoints = 10
        res = game.hold()
        exp = "\nTest's total points are now: 10\n"

    @patch("game.player.Player.roll_dice")
    def test_player_roll(self, mock_roll_dice):
        """Test the roll method of the player."""
        mock_roll_dice.return_value = 1
        game = Game()
        game.game_state = 0
        game.amount_players = 2
        game.active_players.append(Player("Test"))
        game.active_players.append(Player("Test2"))
        game.roll()
        res = game.game_state
        exp = 1
        self.assertEqual(exp, res)

        mock_roll_dice.return_value = 6
        game.roll()
        res = game.game_state
        exp = 1
        self.assertEqual(exp, res)
