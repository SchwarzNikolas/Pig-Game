"""Module with the game logic."""

import pickle
from player import Player
from dice import Dice


class Game:
    """Pig-Game Class."""

    def __init__(self):
        """Initialize Object."""
        self.players = []
        try:
            with open("players.dat", "rb") as file:
                self.players = pickle.load(file)
        except FileNotFoundError:
            print("No saved players found.")
        self.active_players = []
        self.game_state = -1
        self.amount_players = 0
        self.dice = Dice()

    def start(self, args):
        """Start a new game."""
        player_names = args.split()
        if len(player_names) > 6 or len(player_names) < 1:
            raise ValueError("The amount of players must be between 1 and 6.")
        self.amount_players = len(player_names)

        for name in player_names:
            player_exists = False
            for player in self.players:
                if player.player_name == name:
                    player_exists = True
                    self.active_players.append(player)
                    break
            if not player_exists:
                print(f"Player {name} doesnt have a profile yet!")
                return False

        self.game_state = 0
        return self.active_players[0]

    def create_player(self, names):
        """Create players with a list of names."""
        for name in names:
            taken = 0
            if len(self.players) > 0:
                for existing_player in self.players:
                    if name == existing_player.player_name:
                        print(f"Playername {name} is already taken!")
                        taken = 1
                        break
            if not taken:
                self.players.append(Player(name))
                print(f"Player {name} has been created!")

    def roll(self):
        """Player decides to roll the dice."""
        if self.game_state < 0:
            return "No active game!"
        dice = Dice()
        dice_num = dice.roll()
        if dice_num == 1:
            return f"{self.players[self.game_state].name}\
has rolled a 1 and lost all points this round."
        return f"{self.players[self.game_state].name} has rolled a {dice_num}."

    def exit(self):
        """Save players and exit"""
        with open("players.dat", "wb") as file:
            pickle.dump(self.players, file)
        return "Thank you for playing!"
