"""Module with commands for the player."""

from cmd import Cmd
from pig_game import Game


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
    intro = f"{welcome_colour}Welcome to Pig Game.{end_colour}\nType help or ? to list commands.\n"
    Cmd.prompt = "(pig-game) "
    completekey = "tab"

    def __init__(self):
        """Initialize the Object."""
        super().__init__()
        self.game = Game()

    def do_create(self, arg):
        r"""Create players. Try: \"create John Amanda\"."""
        args = arg.split()
        msg = self.game.create_player(args)
        print(msg)

    def do_start(self, args):
        r"""
        Start a new game. Usage: \"start John Jane\".

        After the start keyword provide playernames.
        If AI is enabled it will automatically join the game.
        """
        msg = "Missing argument, provide player names"
        if not args:
            print(msg)
            return
        try:
            if self.game.start(args):
                print("Game started, player one starts!")
            else:
                print("Please identify yourself!")
        except (ValueError, TypeError) as err:
            print(err)

    def do_roll(self, _):
        """Roll the dice."""
        Cmd.prompt = "(Player 1) "
        msg = self.game.roll()
        print(msg)

    def do_exit(self, _):
        """Exit the game."""
        msg = self.game.exit()
        print(msg)
        return True
