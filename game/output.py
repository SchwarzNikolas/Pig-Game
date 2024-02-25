"""Module with commands for the player."""

import cmd
from game import Game


class Output(cmd.Cmd):
    """Class with methods to interact with the player."""

    intro = "Welcome to the pig-game. Type help or ? to list commands.\n"
    prompt = "(pig-game) "
    completekey = "tab"

    def __init__(self):
        """Initialize the Object."""
        super().__init__()
        self.game = Game()

    def do_start(self, _):
        """Start a new game."""
        if self.game.start():
            print("Game started, player one starts!")
        else:
            print("Please identify yourself!")

    def do_create(self, arg):
        r"""Create players. Try: \"create John Amanda\"."""
        args = arg.split()
        msg = self.game.create_player(args)
        print(msg)

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

    def do_exit(self, _):
        """Exit the game."""
        print("Thank you for playing!")
        return True
