"""Module with commands for the player."""

from cmd import Cmd
from Game import Game


class Output(Cmd):
    """Class with methods to interact with the player."""

    intro = "Welcome to the pig-game. Type help or ? to list commands.\n"
    Cmd.prompt = "(pig-game) "
    completekey = "tab"

    def __init__(self):
        """Initialize the Object."""
        super().__init__()
        self.game = Game()

    def do_player_amount(self, arg):
        """
        Set the amount of players.

        If set to 1 the player will play against the computer.
        If set to another value the players will play against each other
        Maxmimum amount of players is 6
        """
        msg = 'Missing argument, provide the amount of players. \
Try: "player_amount 1"'
        if not arg:
            print(msg)
            return

        try:
            msg = self.game.player_amount(int(arg))
        except (ValueError, TypeError) as err:
            print(err)

    def do_create(self, arg):
        r"""Create players. Try: \"create John Amanda\"."""
        args = arg.split()
        msg = self.game.create_player(args)
        print(msg)

    def do_start(self, _):
        """Start a new game."""
        if self.game.start():
            print("Game started, player one starts!")
        else:
            print("Please identify yourself!")

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
