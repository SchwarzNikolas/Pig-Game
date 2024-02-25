"""Module with the game logic."""

from player import Player
from dice import Dice
import pickle


class Game:
    """Pig-Game Class."""

    def __init__(self):
        """Initialize Object."""
        self.players = []
        try:
            with open("players.dat", "rb") as file:
                self.player = pickle.load(file)
        except FileNotFoundError:
            print("No saved players found.")
        self.game_state = -1
        self.amount_players = 0
        self.dice = Dice()

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
        if self.game_state < 0:
            return "No active game!"
        dice_num = Dice.roll()
        if dice_num == 1:
            return f"{self.players[self.game_state].name}\
has rolled a 1 and lost all points this round."
        return f"{self.players[self.game_state].name} has rolled a {dice_num}."

    def exit(self):
        """Save players and exit"""
        with open("players.dat", "wb") as file:
            pickle.dump(self.players, file)
