"""Module with commands for the player."""

from cmd import Cmd
from game.pig_game import Game


class Output(Cmd):
    """Class with methods to interact with the player."""

    pink_pig_colour = "\33[95m"
    welcome_colour = "\33[43m"
    round_over_colour = "\33[91m"
    winning_colour = "\33[92m"
    keep_going_colour = "\33[94m"
    end_colour = "\033[0m"
    flashing_effect = "\33[5m"
    italics = "\33[3m"
    intro = f"{welcome_colour}Welcome to Pig Game.{end_colour}\
\nType help or ? to list commands.\n"
    Cmd.prompt = "(pig-game) "
    completekey = "tab"

    def __init__(self):
        """Initialize the Object."""
        super().__init__()
        self.game = Game()

    def do_profile(self, args):
        """
        Player profile settings.

        Arguments:
            -c: create Players  [profile -c John,Jane]
            -r: rename Player   [profile -r John]
            -d: delete Player   [profile -d John]
        """
        args = args.split()
        if not args:
            print("No arguments given!")
            return

        try:
            playername = args[1]
        except IndexError:
            if args[0] in ["-d", "-r", "-c"]:
                print("No playername provided!")
            else:
                print("Garbage argument. Use \"help profile\".")
        else:
            match args[0]:
                case "-c":
                    self.game.create_player(playername.split(","))
                case "-r":
                    if self.game.rename_player(playername):
                        print("Playername sucessfully changed!")
                    else:
                        print(f"Player {playername} doesn't exist.")
                case "-d":
                    if self.game.delete_player(playername):
                        print(f"Player {playername} has been deleted.")
                    else:
                        print(f"Player {playername} doesn't exist.")
                case _:
                    print("Garbage argument. Use \"help profile\".")

    def do_start(self, args):
        """
        Start a new game. Usage: "start John,Jane".

        After the start keyword provide playernames.
        If AI is enabled it will automatically join the game.
        """
        msg = "Missing argument, provide player names"
        if not args:
            print(msg)
            return
        try:
            first_player = self.game.start(args)
            if first_player is not False:
                print(f"Game started, {first_player.player_name} begins!")
                Cmd.prompt = f"({first_player.player_name}) "
        except (ValueError, TypeError) as err:
            print(err)

    def do_roll(self, _):
        """Roll the dice."""
        msg = self.game.roll()
        print(msg)

    def do_hold(self, _):
        """Keep the round points."""
        msg = self.game.hold()
        print(msg)

    def postcmd(self, stop, line):
        if stop is True or "exit" in line:
            return True
        if self.game.game_state >= 0:
            Cmd.prompt = f"({self.game.active_players[self.game.game_state].player_name}) "
        return False

    def do_exit(self, _):
        """Exit the game."""
        msg = self.game.exit()
        print(msg)
        return True
