# Define ANSI escape codes for colors
import os


COLOR_BOX = "\033[0;33;40m"   # Yellow
COLOR_BOX_ON_GOAL = "\033[1;36;40m"  # Cyan
COLOR_PLAYER = "\033[1;32;40m"  # Green
COLOR_PLAYER_ON_GOAL = "\033[0;31;40m"  # Red
COLOR_WALL = "\033[0;34;40m"  # Bold Blue
COLOR_GOAL = "\033[0;35;40m"  # Magenta
COLOR_FLOOR = "\033[0;30;40m"  # Invisible
COLOR_RESET = "\033[0m"  # Reset to default

# Define the symbols that may appear in the board
SYMBOL_BOX = "$"
SYMBOL_BOX_ON_GOAL = "*"
SYMBOL_PLAYER = "@"
SYMBOL_PLAYER_ON_GOAL = "+"
SYMBOL_GOAL = "."
SYMBOL_WALL = "#"
SYMBOL_FLOOR = "-"

# Define the mapping of board symbols to colors
symbolColorMapping = {
    SYMBOL_BOX: COLOR_BOX,
    SYMBOL_BOX_ON_GOAL: COLOR_BOX_ON_GOAL,
    SYMBOL_PLAYER: COLOR_PLAYER,
    SYMBOL_PLAYER_ON_GOAL: COLOR_PLAYER_ON_GOAL,
    SYMBOL_WALL: COLOR_WALL,
    SYMBOL_GOAL: COLOR_GOAL,
    SYMBOL_FLOOR: COLOR_FLOOR,
}


def read_file(xsb_file):
    '''read `xsb_file` and return a two-dimensional array.

    The two-dimensional array can be accessed with [y][x], where
    x is the horizontal axis and y is the vertical axis. The origin is the
    top-left corner.
    '''
    with open(xsb_file, "r") as f:
        return [list(line.strip()) for line in f]


def print_board_color(board):
    '''print the board.'''
    for row in board:
        colored_row = "".join(symbolColorMapping[cell] + cell for cell in row)
        print(colored_row + COLOR_RESET)  # Reset color at the end of each line


def getPlayerPosition(board):
    '''scan board for the player's position. Returns a tuple.'''
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell in {SYMBOL_PLAYER, SYMBOL_PLAYER_ON_GOAL}:
                return (x, y)


def isEmpty(board, x, y):
    '''checks if the given x, y position is empty (valid for the player or a box to move into)'''
    return board[y][x] in {SYMBOL_FLOOR, SYMBOL_GOAL}


def isBox(board, x, y):
    '''checks if the given x, y position is a box.'''
    return board[y][x] in {SYMBOL_BOX, SYMBOL_BOX_ON_GOAL}


# Read the xsb file
# use os.path.join for portable code (so it works on Mac/Windows/Linux)
path = os.path.join("levels", "level1.xsb")
board = read_file(path)

print_board_color(board)
print("The player is now at position: ", getPlayerPosition(board))
print("Position (1, 7) is a floor or a goal: ", isEmpty(board, 1, 7))
print("Position (2, 5) is a box:", isBox(board, 2, 5))
