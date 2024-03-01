import unittest

from game.dicehand import DiceHand

class Test_DiceHand(unittest.TestCase):
    
    def test_init_default_object(self):
        """Instantiate an object and check its properties"""
        res = DiceHand()
        exp = DiceHand
        self.assertIsInstance(res, exp)
        diceHand = DiceHand()
        
        res = diceHand.roundpoints
        exp = 0
        self.assertEqual(res, exp)

    def test_change_round_points_using_update_hand(self):
        diceHand = DiceHand()
        
        diceHand.update_Hand(6)
        
        res = diceHand.roundpoints
        exp = 6
        self.assertEqual(res, exp)
        
        diceHand.update_Hand(1)
        res = diceHand.roundpoints
        exp = 0
        self.assertEqual(res, exp)

    def test_hold_and_totalpoints(self):
        diceHand = DiceHand()
        
        diceHand.update_Hand(4)
        diceHand.update_Hand(5)
        diceHand.hold()
        
        res = diceHand.get_totalPoints()
        exp = 9
        self.assertEqual(res, exp)

    def test_amount_of_rolls(self):
        dicehand = DiceHand()
        
        dicehand.update_Hand(4)
        dicehand.update_Hand(4)
        dicehand.update_Hand(4)
        dicehand.update_Hand(4)
        dicehand.update_Hand(4)
        
        res = dicehand.get_amountOfRolls()
        exp = 5
        self.assertEqual(res, exp)

    def test_rounds(self):
        dicehand = DiceHand()
        
        dicehand.update_Hand(1)
        dicehand.update_Hand(4)
        dicehand.update_Hand(1)
        
        res = dicehand.get_rounds()
        exp = 2
        self.assertEqual(res, exp)
