"""Unit Test for the Histogram Module."""

import unittest
from unittest.mock import patch
import io
from game.histogram import Histogram
from game.player import Player


class TestHistogramClass(unittest.TestCase):
    """Test the Histogram class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Histogram()
        exp = Histogram
        self.assertIsInstance(res, exp)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_barchart(self, mock_stdout):
        """Test the bar chart."""
        histogram = Histogram()
        histogram.barchart("Test", 1, histogram.colour1, 1)
        exp1 = f"   Test    |   1   | {histogram.colour1}∎{histogram.end}\n"
        exp2 = ">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< \n"
        exp = exp1 + exp2
        self.assertEqual(exp, mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_key(self, mock_stdout):
        """Test key output."""
        his = Histogram()
        his.key()
        exp1 = "------------ KEY ------------\n"
        exp2 = f"{'=' * 29}\n"
        exp3 = f"{his.colour1}∎  | {'lowest rolls':^16} |  1:17{his.end}\n"
        exp4 = f"{his.colour2}∎  | {'lowest rounds':^16} |   1:2{his.end}\n"
        exp5 = f"{his.colour3}∎  | {'highest points':^16} |   1:6{his.end}\n"
        exp6 = f"{his.colour4}∎  | {'all time points':^16} | 1:100{his.end}\n"
        exp7 = f"{his.colour5}∎  | {'all time wins':^16} |   1:1{his.end}\n"
        exp8 = f"{'=' * 29}\n"
        exp9 = "Note on scale -> block:score\n\n"
        exp = exp1 + exp2 + exp3 + exp4 + exp5 + exp6 + exp7 + exp8 + exp9
        self.assertEqual(exp, mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        """Test display method."""
        his = Histogram()
        player = Player("Test")
        players = []
        players.append(player)
        his.display(players)
        exp1 = "------------ KEY ------------\n"
        exp2 = f"{'=' * 29}\n"
        exp3 = f"{his.colour1}∎  | {'lowest rolls':^16} |  1:17{his.end}\n"
        exp4 = f"{his.colour2}∎  | {'lowest rounds':^16} |   1:2{his.end}\n"
        exp5 = f"{his.colour3}∎  | {'highest points':^16} |   1:6{his.end}\n"
        exp6 = f"{his.colour4}∎  | {'all time points':^16} | 1:100{his.end}\n"
        exp7 = f"{his.colour5}∎  | {'all time wins':^16} |   1:1{his.end}\n"
        exp8 = f"{'=' * 29}\n"
        exp9 = "Note on scale -> block:score\n\n"
        exp1_1 = exp1 + exp2 + exp3 + exp4 + exp5 + exp6 + exp7 + exp8 + exp9
        exp10 = f"   Test    |   0   | {his.colour1}{his.end}\n"
        exp11 = f"{'>< ' * 19 }\n"
        exp12 = f"   Test    |   0   | {his.colour2}{his.end}\n"
        exp13 = f"   Test    |   0   | {his.colour3}{his.end}\n"
        exp15 = f"   Test    |   0   | {his.colour4}{his.end}\n"
        exp17 = f"   Test    |   0   | {his.colour5}{his.end}\n"
        exp1_2 = exp10 + exp11 + exp12 + exp11 + exp13
        exp1_3 = exp11 + exp15 + exp11 + exp17 + exp11 + "\n"
        exp = exp1_1 + exp1_2 + exp1_3
        self.assertEqual(exp, mock_stdout.getvalue())
