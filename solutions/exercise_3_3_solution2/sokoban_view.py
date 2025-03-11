from enum import Enum

from sokoban_model import Symbol


class Ansi(Enum):
    """
    Define ANSI escape codes for colors and resetting screen
    """

    BOX = "\033[0;33;40m"   # Yellow
    BOX_ON_GOAL = "\033[1;36;40m"  # Cyan
    PLAYER = "\033[1;32;40m"  # Green
    PLAYER_ON_GOAL = "\033[0;31;40m"  # Red
    WALL = "\033[0;34;40m"  # Bold Blue
    GOAL = "\033[0;35;40m"  # Magenta
    FLOOR = "\033[0;30;40m"  # Invisible
    RESET = "\033[0m"  # Reset to default
    CLEAR_SCREEN = "\033c"


# Define the mapping of board symbols to colors
symbol_color_mapping = {
    Symbol.BOX: Ansi.BOX,
    Symbol.BOX_ON_GOAL: Ansi.BOX_ON_GOAL,
    Symbol.PLAYER: Ansi.PLAYER,
    Symbol.PLAYER_ON_GOAL: Ansi.PLAYER_ON_GOAL,
    Symbol.WALL: Ansi.WALL,
    Symbol.GOAL: Ansi.GOAL,
    Symbol.FLOOR: Ansi.FLOOR,
}


class SokobanView:
    def print(self, model):
        print(Ansi.CLEAR_SCREEN.value)
        for y in range(model.height()):
            for x in range(model.width()):
                s = model.symbol(x, y)
                print(symbol_color_mapping[s].value + s.value, end="")
            print("")
        print(Ansi.RESET.value)
