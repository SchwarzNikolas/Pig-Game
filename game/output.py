"""Module with commands for the player."""

from cmd import Cmd
from game.pig_game import Game
from game.intelligence import BinaryBrain


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
            -c: create Players  [profile -c John, Jane]
            -r: rename Player   [profile -r John]
            -d: delete Player   [profile -d John]
        """
        args = args.split()
        args = [item.strip().strip(",") for item in args]
        if not args:
            print("No arguments given!")
            return

        if self.game.game_state > 0:
            print("Can't modify profiles during an active game!")
            return

        try:
            playernames = args[1::]
            playername = args[1]
        except IndexError:
            if args[0] in ["-d", "-r", "-c"]:
                print("No playername provided!")
            else:
                print('Garbage argument. Use "help profile".')
        else:
            match args[0]:
                case "-c":
                    self.game.create_player(playernames)
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
                    print('Garbage argument. Use "help profile".')

    def do_start(self, args):
        """
        Start a new game. Usage: "start John, Jane".

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
        """Roll the dice for the current player."""
        msg = self.game.roll()
        print(msg)

    def do_ai(self, args):
        """
        Enable/Disable AI. Usage: "ai true -medium / ai false.

        After the ai keyword provide true or false to enable / disable the ai.
        If the ai should be enabled,
        set the difficulty level with the following arguments:
        -e: easy AI     [ai true -e]
        -m: medium AI   [ai true -m]
        -h: hard AI     [ai true -h]
        """
        if not args:
            print("No arguments given!")
            return

        args = args.lower()
        args = args.split()
        try:
            state = args[0]
            difficulty = args[1]
        except IndexError:
            print('Garbage argument. Use "help ai".')
        else:
            match difficulty:
                case "-e":
                    self.game.set_ai(state, 0)
                case "-m":
                    self.game.set_ai(state, 1)
                case "-h":
                    self.game.set_ai(state, 2)
                case _:
                    print('Garbage argument. Use "help ai".')

    def do_hold(self, _):
        """Keep the round points."""
        msg = self.game.hold()
        print(msg)

    def do_quit(self, _):
        """Quit the current game."""
        self.game.quit()

    def do_restart(self, _):
        """Restart a quit game."""
        self.game.restart()

    def do_cheat(self, _):
        """Help the player to finish the game faster."""
        self.game.cheat()

    def do_rules(self, _):
        """Print out the rules of the game."""
        with open("game/rules.txt", "r", -1, "utf-8") as file:
            print(file.read())

    def postcmd(self, stop, line):
        """
        Set correct player after each action.

        If the exit command is called the game will be closed.
        Otherwise if a real player has entered a command it will display
        the name of the next player.
        If no game is active the default prompt will be displayed.
        """
        index = self.game.game_state
        if stop is True or "exit" in line:
            return True
        if index >= 0:
            if isinstance(self.game.active_players[index], BinaryBrain):
                self.game.play_ai()
                index = self.game.game_state
            players = self.game.active_players
            if players[self.game.game_state].player_name != "BinaryBrain":
                Cmd.prompt = f"({players[index].player_name}) "
        else:
            Cmd.prompt = "(pig-game) "
        return False

    def do_exit(self, _):
        """Exit the game."""
        msg = self.game.exit()
        print(msg)
        return True
