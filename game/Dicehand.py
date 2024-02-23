"Using result of rolling dice"

class DiceHand:
    "Keeps track of integer variables and returns them with getters"

    def __init__(self):
        self.points = 0
        self.rounds = 0
        self.rollamount = 0

    def updateHand(self, diceroll):
        if diceroll != 1:
            self.points += diceroll
            self.rollamount += 1
        else:
            "placeholder for sending result to highscore/histogram"
            self.points = 0
            self.rounds += 1

    def getRoundPoints(self):
        return self.points

    def getRoundsplayed(self):
        return self.rounds

    def getRollAmount(self):
        return self.rollamount
