"""Unit Test for the Highscore Module."""

import unittest
from game.highscore import Highscore


class TestHighscoreClass(unittest.TestCase):
    """Test the Highscore class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Highscore()
        exp = Highscore
        self.assertIsInstance(res, exp)
