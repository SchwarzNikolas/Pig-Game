"""Unit Test for the Histogram Module."""

import unittest
from game.histogram import Histogram


class TestHistogramClass(unittest.TestCase):
    """Test the Histogram class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Histogram()
        exp = Histogram
        self.assertIsInstance(res, exp)
