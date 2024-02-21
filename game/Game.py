"""Module with the game logic."""

from Player import Player


class Game:
    """Pig-Game Class."""

    def __init__(self):
        """Initialize Object."""
        self.players = []
        self.game_state = None
        self.amount_players = 0

    def start(self):
        """Start a new game."""
        if len(self.players) < 1:
            return False
        for player in self.players:
            if not isinstance(player, Player):
                return False
        self.game_state = 0
        return True

    def create_player(self, names):
        """Create players with a list of names."""
        if self.amount_players < 1:
            return "Please set the amount of players first!"
        for i in range(self.amount_players):
            self.players.append(Player(names[i]))
            print(f"Player {names[i]} has been created!")
        return "All players have been created!"

    def player_amount(self, num):
        """Set the player amount."""
        if num > 6 or num < 1:
            raise ValueError("The amount of players must be between 1 and 6.")

        self.amount_players = num

    def roll(self):
        """Player decides to roll the dice."""
        print("test")
