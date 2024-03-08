"""Module with the game logic."""

import pickle
from game.player import Player
from game.intelligence import BinaryBrain
from game.histogram import Histogram


class Game:
    """
    Pig-Game Class.

    This class holds the game logic.
    It holds the playerdata aswell as the AI.
    """

    def __init__(self):
        """
        Initialize Object.

        self.players holds all the saved players with their stats.
        self.active_players holds all the players of an active game.
        self.gamestate indicates if a game is active and whoes turn it is.
        self.amount_players stores the amount of active players in a round.
        self.ai is the object of the pig-game AI.
        self.saved_game saves the state of an ongoing game if the user quits.
        self.cheated_game indicates if someone used the cheat command.
        """
        self.players = []
        try:
            with open("players.dat", "rb") as file:
                self.players = pickle.load(file)
        except FileNotFoundError:
            print("No saved players found.")
        self.active_players = []
        self.game_state = -1
        self.amount_players = 0
        self.ai = BinaryBrain()
        self.active_ai = 0
        self.save_game = 0
        self.cheated_game = 0

    def start(self, args):
        """
        Start a new game.

        Checks how many players will join the game,
        will enable AI if only 1 player joins.
        After the amount of players is checked all provided players
        will be moved into the active player list.
        If everything is sucessfull the gamestate will be set to 0.
        """
        player_names = args.split(",")
        if len(player_names) > 6 or len(player_names) < 1:
            raise ValueError("The amount of players must be between 1 and 6.")
        if len(player_names) == 1:
            self.active_ai = 1
            print("AI will join this game!")

        self.active_players = []
        self.ai.dice_holder.reset()
        for name in player_names:
            player_exists = False
            for player in self.players:
                if player.player_name == name.strip():
                    player_exists = True
                    player.dice_holder.reset()
                    self.active_players.append(player)
                    if self.active_ai == 1:
                        self.active_ai = 2
                        self.active_players.append(self.ai)
                    break
            if not player_exists:
                print(f"Player {name.strip()} doesnt have a profile yet!")
                return False

        self.game_state = 0
        self.amount_players = len(self.active_players)
        return self.active_players[0]

    def create_player(self, names):
        """
        Create a new player object.

        Loops through a list of player names.
        Create a new player is the given name isn't taken.
        """
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
        """
        Delete player from list.

        Delete the player object from the player list if the name matches.
        Needs confirmation before deleting.
        """
        for player in self.players:
            if player.player_name == name:
                confirm = input(f"Proceed with deleting Player {name}? [y/N] ")
                confirm.lower()
                if confirm == "y":
                    self.players.remove(player)
                    return True
        return False

    def roll(self):
        """
        Player decides to roll the dice.

        Select the active player and use the roll_dice method.
        The player returns the result of the roll.
        If a 1 is rolled, the active player will change and then
        the round score will be printed.
        If something else is rolled, the stats will be printed
        and the player may continue to roll.
        """
        msg = "No active game!"
        if self.game_state < 0:
            return msg
        roll = self.active_players[self.game_state].roll_dice()
        if roll == 1:
            self.game_state = (self.game_state + 1) % self.amount_players
            player = self.active_players[self.game_state - 1]
            name = f"\n{player.player_name}"
            string = " has rolled a 1 and lost all points this round.\n"
            score = f"\nTotal score: {player.dice_holder.get_total_points()}"
            points = f"\nRound score: {player.dice_holder.get_round_points()}"
            return name + string + points + score
        player = self.active_players[self.game_state]
        name = f"\n{player.player_name}"
        string = f" has rolled a {roll}"
        points = f"\nRound score: {player.dice_holder.get_round_points()}"
        score = f"\nTotal score: {player.dice_holder.get_total_points()}\n"
        return name + string + points + score

    def hold(self):
        """
        Player decides to hold the round points.

        If a player decides to hold the round points
        will be added to the total points. Afterwards the game evaluates
        if the totalscore is higher or equal to 100 points.
        If thats the case the game ends and the current player wins.
        """
        msg = "No active game!"
        if self.game_state < 0:
            return msg
        player = self.active_players[self.game_state]
        player.dice_holder.hold()
        if player.dice_holder.get_total_points() >= 100:
            self.game_state = -1
            self.active_ai = 0
            if self.cheated_game == 0:
                player.update_scores(1)
            return f"{player.player_name} has won the game!"
        self.game_state = (self.game_state + 1) % self.amount_players
        name = f"\n{player.player_name}'s total points are now: "
        score = f"{player.dice_holder.get_total_points()}\n"
        return name + score

    def set_ai(self, state, difficulty):
        """
        Enable the AI.

        If the state parameter quals to ture the ai will be enabled
        and the difficulty will be set.
        Otherwise the ai will be disabled.
        """
        if state == "true":
            self.active_ai = 1
            self.ai.update_difficulty(difficulty)
            print("AI will join the next game!")
        else:
            self.active_ai = 0
            print("AI is disabled for the next game!")

    def play_ai(self):
        """
        Let the AI do its moves.

        Calls the game loop of the AI.
        Afterwards a check runs if the AI has won the game.
        """
        self.ai.evaluate_round()
        player = self.ai
        if player.dice_holder.get_total_points() >= 100:
            self.game_state = -1
            print(f"{player.player_name} has won the game!")
            print("Type quit to leave the current game.")
            self.active_ai = 0
            return
        self.game_state = (self.game_state + 1) % self.amount_players

    def quit(self):
        """
        Pause/Quit current game.

        If a game is currently active it will be paused
        and the gamestate will be saved.
        """
        if self.game_state >= 0:
            self.save_game = self.game_state
            self.game_state = -1

    def cheat(self):
        """
        Help a player to win faster.

        Set the current players points to 99.
        """
        self.cheated_game = 1
        self.active_players[self.game_state].dice_holder.totalpoints = 99
        print("You cheated!\nYour total points are set to 99.")

    def restart(self):
        """
        Restart paused game.

        If a running game has been quit it will be restarted
        and the saved data will be loaded.
        """
        if self.save_game > 0:
            self.game_state = self.save_game
        else:
            print("There is no paused game!")

    def show_histogram(self):
        """
        Show all players stats.

        Prints out charts about each players stats.
        Returns true if histogram is displayed sucessfully.
        """
        histogram = Histogram()
        histogram.display(self.players)
        return True

    def exit(self):
        """
        Save players and exit.

        Method will be called when the user exits the program,
        The playerlist will be saved as a binary file.
        """
        with open("players.dat", "wb") as file:
            pickle.dump(self.players, file)
        return "Thank you for playing!"
