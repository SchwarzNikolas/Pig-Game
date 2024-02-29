"""Unit Test for the Player Module."""

import unittest
from game.player import Player

class TestPlayerClass(unittest.TestCase):
        """Test the Player class."""

        def test_init_default_object(self):
            """Instantiate an object and check its properties."""
            res = Player()
            exp = Player
            self.assertIsInstance(res, exp)
