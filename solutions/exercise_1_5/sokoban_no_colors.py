import os

# Define the symbols that may appear in the board
SYMBOL_BOX = "$"
SYMBOL_BOX_ON_GOAL = "*"
SYMBOL_PLAYER = "@"
SYMBOL_PLAYER_ON_GOAL = "+"
SYMBOL_GOAL = "."
SYMBOL_FLOOR = "-"


def read_file(xsb_file):
    '''read `xsb_file` and return a two-dimensional array.

    The two-dimensional array can be accessed with [y][x], where
    x is the horizontal axis and y is the vertical axis. The origin is the
    top-left corner.
    '''
    with open(xsb_file, "r") as f:
        return [list(line.rstrip("\r\n")) for line in f]


def print_board(board):
    '''print the board.'''
    for row in board:
        print(row, sep="")


def get_player_position(board):
    '''scan board for the player's position. Returns a tuple.'''
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == SYMBOL_PLAYER or cell == SYMBOL_PLAYER_ON_GOAL:
                return (x, y)


def is_empty(board, x, y):
    '''checks if the given x, y position is empty (valid for the player or a box to move into)'''
    return board[y][x] == SYMBOL_FLOOR or board[y][x] == SYMBOL_GOAL


def is_box(board, x, y):
    '''checks if the given x, y position is a box.'''
    return board[y][x] == SYMBOL_BOX or board[y][x] == SYMBOL_BOX_ON_GOAL


# Read the xsb file
# use os.path.join for portable code (so it works on Mac/Windows/Linux)
path = os.path.join("levels", "level1.xsb")
board = read_file(path)

print_board(board)
print("The player is now at position: ", get_player_position(board))
print("Position (1, 7) is a floor or a goal: ", is_empty(board, 1, 7))
print("Position (2, 5) is a box:", is_box(board, 2, 5))
