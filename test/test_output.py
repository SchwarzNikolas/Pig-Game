"""Unit Test for the Output Module."""

import unittest
from unittest.mock import patch
from game.output import Output


class TestOutputClass(unittest.TestCase):
    """Test the Output class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Output()
        exp = Output
        self.assertIsInstance(res, exp)
