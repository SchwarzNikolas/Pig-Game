"""The Module to display Highscore graphically."""


class Histogram:
    """Blueprint for a Histogram."""

    def __init__(self):
        """Colours."""
        self.colour1 = "\x1b[38;2;136;73;143m"
        self.colour2 = "\x1b[38;2;207;92;54m"
        self.colour3 = "\x1b[38;2;225;212;73m"
        self.colour4 = "\x1b[38;2;84;140;47m"
        self.colour5 = "\x1b[38;2;26;101;158m"
        self.end = "\x1b[0m"

    def barchart(self, name, num, colour, scale):
        """Print out the bar."""
        box = "*" * int(num / scale)
        print(f"{name:^10} | {num:^5} | {colour}{box[:35]}{self.end}")
        print(f"{'>< ' * 19 }")

    def key(self):
        """Key to assist reading Histograms."""
        print("------------ KEY ------------")
        print(f"{'=' * 29}")
        print(f"{self.colour1}*  | {'lowest rolls':^16} |  1:17{self.end}")
        print(f"{self.colour2}*  | {'lowest rounds':^16} |   1:2{self.end}")
        print(f"{self.colour3}*  | {'highest points':^16} |   1:6{self.end}")
        print(f"{self.colour4}*  | {'all time points':^16} | 1:100{self.end}")
        print(f"{self.colour5}*  | {'all time wins':^16} |   1:1{self.end}")
        print(f"{'=' * 29}")
        print("Note on scale -> block:score\n")

    def display(self, players):
        """Display the stats for each Player."""
        self.key()
        for player in players:
            name = player.player_name
            rolls, rounds, max_points, points, wins = player.return_stats()
            self.barchart(name, rolls, self.colour1, 17)
            self.barchart(name, rounds, self.colour2, 2)
            self.barchart(name, max_points, self.colour3, 6)
            self.barchart(name, points, self.colour4, 100)
            self.barchart(name, wins, self.colour5, 1)
            print()
