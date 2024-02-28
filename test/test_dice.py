import unittest

from game.dice import Dice


class Test_Dice_Roll(unittest.TestCase):
    
    
    def test_init_default_object(self):
        """Instantiate an object and check its properties"""
        res = Dice()
        exp = Dice
        self.assertIsInstance(res, exp)
        
    def test_roll_dice(self):
        """Test roll dice"""
        dice = Dice()
        res = dice.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)