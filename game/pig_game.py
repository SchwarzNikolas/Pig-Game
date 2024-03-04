"""Module with the game logic."""

import pickle
from game.player import Player


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

    def start(self, args):
        """Start a new game."""
        player_names = args.split(",")
        if len(player_names) > 6 or len(player_names) < 1:
            raise ValueError("The amount of players must be between 1 and 6.")
        self.amount_players = len(player_names)

        for name in player_names:
            player_exists = False
            for player in self.players:
                if player.player_name == name.strip():
                    player_exists = True
                    player.dice_holder.reset()
                    self.active_players.append(player)
                    break
            if not player_exists:
                print(f"Player {name.strip()} doesnt have a profile yet!")
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

    def rename_player(self, name):
        """Rename player's object."""
        for player in self.players:
            if player.player_name == name:
                player.change_name()
                return True
        return False

    def delete_player(self, name):
        """Delete player from list."""
        for player in self.players:
            if player.player_name == name:
                confirm = input(f"Proceed with deleting Player {name}? [y/N] ")
                confirm.lower()
                if confirm == "y":
                    self.players.remove(player)
                    return True
        return False

    def roll(self):
        """Player decides to roll the dice."""
        msg = "No active game!"
        if self.game_state < 0:
            return msg
        roll = self.active_players[self.game_state].roll_dice()
        if roll == 1:
            self.game_state = (self.game_state + 1) % len(self.active_players)
            player = self.active_players[self.game_state - 1]
            name = f"{player.player_name}"
            string = " has rolled a 1 and lost all points this round."
            score = f"\nTotal score: {player.dice_holder.get_totalPoints()}"
            points = f"\nRound score: {player.dice_holder.get_roundPoints()}"
            return name + string + points + score
        player = self.active_players[self.game_state]
        name = f"{player.player_name}"
        string = f" has rolled a {roll}"
        points = f"\nRound score: {player.dice_holder.get_roundPoints()}"
        score = f"\nTotal score: {player.dice_holder.get_totalPoints()}"
        return name + string + points + score

    def hold(self):
        """Player decides to roll the dice."""
        msg = "No active game!"
        if self.game_state < 0:
            return msg
        player = self.active_players[self.game_state]
        player.dice_holder.hold()
        if player.dice_holder.get_totalPoints() >= 100:
            self.game_state = -1
            return f"{player.player_name} has won the game!"
        self.game_state = (self.game_state + 1) % len(self.active_players)
        name = f"{player.player_name}'s total points are now: "
        score = f"{player.dice_holder.get_totalPoints()}"
        return name + score

    def exit(self):
        """Save players and exit."""
        with open("players.dat", "wb") as file:
            pickle.dump(self.players, file)
        return "Thank you for playing!"
