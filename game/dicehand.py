"""Using result of rolling dice."""


class DiceHand:
    """Keeps track of integer variables and returns them with getters."""

    def __init__(self):
        """Initialize self."""
        self.roundpoints = 0
        self.rounds = 0
        self.amountofrolls = 0
        self.totalpoints = 0

    def update_hand(self, diceroll):
        """Update values of object."""
        if diceroll != 1:
            self.roundpoints += diceroll
            self.amountofrolls += 1
        else:
            self.amountofrolls += 1
            self.roundpoints = 0
            self.rounds += 1

    def hold(self):
        """End round."""
        self.totalpoints += self.roundpoints
        self.roundpoints = 0
        self.rounds += 1

    def reset(self):
        """Reset values."""
        self.roundpoints = 0
        self.rounds = 0
        self.amountofrolls = 0
        self.totalpoints = 0

    def get_amount_of_rolls(self):
        """Get amount of rolls."""
        return self.amountofrolls

    def get_rounds(self):
        """Get rounds."""
        return self.rounds

    def get_total_points(self):
        """Get total points."""
        return self.totalpoints

    def get_round_points(self):
        """Get points of current round."""
        return self.roundpoints
