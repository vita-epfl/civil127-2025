# Define ANSI escape codes for colors
COLOR_BOX = "\033[0;33;40m"   # Yellow
COLOR_BOX_ON_GOAL = "\033[1;36;40m"  # Cyan
COLOR_PLAYER = "\033[1;32;40m"  # Green
COLOR_PLAYER_ON_GOAL = "\033[0;31;40m"  # Red
COLOR_WALL = "\033[0;34;40m"  # Bold Blue
COLOR_GOAL = "\033[0;35;40m"  # Magenta
COLOR_FLOOR = "\033[0;30;40m"  # Invisible
COLOR_RESET = "\033[0m"  # Reset to default
COLOR_CLEAR_SCREEN = "\033c"

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

    print(COLOR_CLEAR_SCREEN)  # clear screen
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


def move(board, dx, dy):
    (x, y) = getPlayerPosition(board)
    (nx, ny) = (x + dx, y + dy)  # nx, ny are where the player is trying to go

    # Due to our board representation, we must take goal and regular tiles
    # into account. There are better ways around.
    if isEmpty(board, nx, ny):
        if board[ny][nx] == SYMBOL_GOAL:
            board[ny][nx] = SYMBOL_PLAYER_ON_GOAL
        else:
            board[ny][nx] = SYMBOL_PLAYER

        if board[y][x] == SYMBOL_PLAYER_ON_GOAL:
            board[y][x] = SYMBOL_GOAL
        else:
            board[y][x] = SYMBOL_FLOOR

    elif isBox(board, nx, ny):
        (nnx, nny) = (nx+dx, ny+dy)  # nnx, nny are where the box is trying to go
        if isEmpty(board, nnx, nny):
            if board[nny][nnx] == SYMBOL_GOAL:
                board[nny][nnx] = SYMBOL_BOX_ON_GOAL
            else:
                board[nny][nnx] = SYMBOL_BOX

            if board[ny][nx] == SYMBOL_BOX_ON_GOAL:
                board[ny][nx] = SYMBOL_PLAYER_ON_GOAL
            else:
                board[ny][nx] = SYMBOL_PLAYER

            if board[y][x] == SYMBOL_PLAYER_ON_GOAL:
                board[y][x] = SYMBOL_GOAL
            else:
                board[y][x] = SYMBOL_FLOOR
        else:
            return "can't push this box"
    else:
        return "can't push walls"


board = read_file("games/level1.xsb")
print_board_color(board)
while True:
    player_movement = input("enter move (w, a, s, d), restart (r), or quit (q):")
    match player_movement:
        case 'w':
            invalid = move(board, 0, -1)
        case 'a':
            invalid = move(board, -1, 0)
        case 's':
            invalid = move(board, 0, 1)
        case 'd':
            invalid = move(board, 1, 0)
        case 'r':
            board = read_file("games/level1.xsb")
            invalid = None
        case 'q':
            break
    if not invalid:
        print_board_color(board)
    else:
        print('invalid move: ', invalid)