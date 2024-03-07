"""The Module to control Highscores."""


class Highscore:
    """The Blueprint for Highscores."""

    def __init__(self):
        """Beginning of a new Player's Highscores."""
        self.lowest_roll = 0  # Least amount of rolls to win.
        self.lowest_round = 0  # Least amount of rounds to win.
        self.highest_points = 0  # In one round.
        self.all_time_points = 0  # Overall point accumulator
        self.all_time_wins = 0  # Amount of total wins.

    def reset_highscore(self):
        """Restart a Player's Highscores."""
        self.lowest_roll = 0
        self.lowest_round = 0
        self.highest_points = 0
        self.all_time_points = 0
        self.all_time_wins = 0

    def update_highscore(self, total_rolls, total_rounds, points, win):
        """Alter highscore for a specific Player."""
        if self.lowest_roll > total_rolls or self.lowest_roll == 0:
            self.lowest_roll = total_rolls

        if self.lowest_round > total_rounds or self.lowest_round == 0:
            self.lowest_round = total_rounds

        if self.highest_points < points:
            self.highest_points = points

        self.all_time_wins += win
        self.all_time_points += points

    def return_low_stats(self):
        """Display lowest roll and lowest round count."""
        return self.lowest_roll, self.lowest_round

    def return_high_stats(self):
        """Display highest points in one round."""
        return self.highest_points

    def return_all_time_stats(self):
        """Display all time points and wins."""
        return self.all_time_points, self.all_time_wins
