"""Using result of rolling dice."""


class DiceHand:
    """Keeps track of integer variables and returns them with getters."""

    def __init__(self):
        """Initialize self."""
        self.roundpoints = 0
        self.rounds = 0
        self.amountOfRolls = 0
        self.totalpoints = 0

    def update_Hand(self, diceroll):
        """Update values of object."""
        if diceroll != 1:
            self.roundpoints += diceroll
            self.amountOfRolls += 1
        else:
            self.amountOfRolls += 1
            self.roundpoints = 0
            self.rounds += 1

    def hold(self):
        """End round."""
        self.totalpoints += self.roundpoints
        self.roundpoints = 0
        self.rounds += 1

    def get_stats(self):
        """Get stats."""
        return self.amountOfRolls, self.rounds, self.totalpoints
