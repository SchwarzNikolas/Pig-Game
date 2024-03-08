"""Unit Test for the Output Module."""

import unittest
import io
import sys
from unittest.mock import patch
from unittest import mock
from game.output import Output
from game.player import Player


class TestOutputClass(unittest.TestCase):
    """Test the Output class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Output()
        exp = Output
        self.assertIsInstance(res, exp)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_profile(self, mock_stdout):
        """Test all possible profile commands."""
        output = Output()
        output.do_profile("")
        exp = "No arguments given!\n"
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        output.game.game_state = 1
        output.do_profile("test, -d")
        exp = "Can't modify profiles during an active game!\n"
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        output.game.game_state = -1
        output.do_profile("-d")
        exp = "No playername provided!\n"
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        output.do_profile("-a")
        exp = 'Garbage argument. Use "help profile".\n'
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        output.do_profile("-a, Test")
        exp = 'Garbage argument. Use "help profile".\n'
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        output.game.players.append(Player("Test"))
        output.do_profile("-c, Test")
        exp = "Playername Test is already taken!\n"
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "Test1"
        output.do_profile("-r, Test")
        mock.builtins.input = original_input
        exp = "Playername sucessfully changed!\n"
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        output.do_profile("-r, Thisisnotaplayer")
        exp = "Player Thisisnotaplayer doesn't exist.\n"
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "y"
        output.do_profile("-d, Test1")
        mock.builtins.input = original_input
        exp = "Player Test1 has been deleted.\n"
        self.assertEqual(exp, mock_stdout.getvalue())

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        output.do_profile("-d, Test1")
        exp = "Player Test1 doesn't exist.\n"
        self.assertEqual(exp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rules(self, mock_stdout):
        """Test the rules output."""
        output = Output()
        output.do_rules("rules")
        with open("game/rules.txt", "r") as file:
            exp = file.read() + "\n"
        self.assertEqual(exp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hold(self, mock_stdout):
        """Test the hold method."""
        output = Output()
        output.do_hold("hold")
        exp = "No active game!\n"
        self.assertEqual(exp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll(self, mock_stdout):
        """Test the roll method."""
        output = Output()
        output.do_roll("roll")
        exp = "No active game!\n"
        self.assertEqual(exp, mock_stdout.getvalue())

    def test_cheat(self):
        """Test the cheat method."""
        sys.stdout = io.StringIO()
        output = Output()
        output.game.active_players.append(Player(""))
        output.do_cheat("cheat")
        res = output.game.cheated_game
        exp = 1
        self.assertEqual(exp, res)
        sys.stdout = sys.__stdout__

    def test_quit(self):
        """Test the quit method."""
        output = Output()
        output.game.game_state = 1
        output.do_quit("quit")
        res = output.game.game_state
        exp = -1
        self.assertEqual(exp, res)

    def test_restart(self):
        """Test the restart method."""
        output = Output()
        output.game.game_state = 2
        output.do_quit("quit")
        output.do_restart("restart")
        res = output.game.game_state
        exp = 2
        self.assertEqual(exp, res)

    def test_exit(self):
        """Test the exit method."""
        sys.stdout = io.StringIO()
        output = Output()
        res = output.do_exit("exit")
        self.assertTrue(res)
        sys.stdout = sys.__stdout__
