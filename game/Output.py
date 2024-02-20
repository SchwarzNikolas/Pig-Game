import cmd
from Game import Game


class Output(cmd.Cmd):
    intro = "Welcome to the pig-game. Type help or ? to list commands.\n"
    prompt = "(pig-game) "
    completekey = "tab"

    def __init__(self):
        """Initialize the Object."""
        super().__init__()
        self.game = Game()

    def do_play(self, _):
        """Continue playing."""
        self.game.play()

    def do_exit(self, _):
        """Exit the game."""
        print("Thank you for playing!")
        return True
