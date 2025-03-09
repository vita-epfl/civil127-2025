from enum import Enum


class Symbol(Enum):
    """
    Symbols that may appear in the level file.
    """
    BOX = "$"
    BOX_ON_GOAL = "*"
    PLAYER = "@"
    PLAYER_ON_GOAL = "+"
    GOAL = "."
    WALL = "#"
    FLOOR = "-"


class MoveResponse(Enum):
    """
    Return values for SokobanModel.move().
    """
    INVALID_WALL = "can't push walls"
    INVALID_BOX = "can't push this box"
    VALID = "valid"


class SokobanModel:
    def __init__(self, level_data):
        """ level_data is a list of strings"""

        self.board = []
        for row in level_data:
            next_row = []
            for c in row.strip():
                next_row.append(Symbol(c))
            self.board.append(next_row)

    def get_player_position(self):
        '''Scan board for the player's position. Returns (x, y) tuple.'''

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell == Symbol.PLAYER:
                    return (x, y)
                if cell == Symbol.PLAYER_ON_GOAL:
                    return (x, y)

    def is_empty(self, x, y):
        '''Checks if the given x, y position is empty (valid for the player or a box to move into).'''

        if self.board[y][x] == Symbol.FLOOR:
            return True
        if self.board[y][x] == Symbol.GOAL:
            return True
        return False

    def is_box(self, x, y):
        '''Checks if the given x, y position is a box.'''

        if self.board[y][x] == Symbol.BOX:
            return True
        if self.board[y][x] == Symbol.BOX_ON_GOAL:
            return True
        return False

    def _set_player(self, x, y):
        '''
        Sets the given x, y position as the player or player on goal. This
        method allows replacing a box with a player, since we assume set_box
        will be called immediately before or after.
        '''

        if self.board[y][x] == Symbol.GOAL:
            self.board[y][x] = Symbol.PLAYER_ON_GOAL
        elif self.board[y][x] == Symbol.BOX_ON_GOAL:
            self.board[y][x] = Symbol.PLAYER_ON_GOAL
        else:
            self.board[y][x] = Symbol.PLAYER

    def _set_box(self, x, y):
        '''Sets the given x, y position as a box or box on goal.'''

        if self.board[y][x] == Symbol.GOAL:
            self.board[y][x] = Symbol.BOX_ON_GOAL
        else:
            self.board[y][x] = Symbol.BOX

    def _clear(self, x, y):
        '''
        Removes the box or player from the given x, y position.
        Restores floor or goal accordingly.
        '''
        if self.board[y][x] == Symbol.PLAYER_ON_GOAL:
            self.board[y][x] = Symbol.GOAL
        elif self.board[y][x] == Symbol.BOX_ON_GOAL:
            self.board[y][x] = Symbol.GOAL
        else:
            self.board[y][x] = Symbol.FLOOR

    def move(self, dx, dy):
        (x, y) = self.get_player_position()
        # nx, ny is where the player is trying to go
        (nx, ny) = (x + dx, y + dy)

        # Due to our board representation, we must take floor and goal cells
        # into account. We use _set_player, _set_box, and _clear helper
        # methods to keep the code more readable.
        if self.is_empty(nx, ny):
            self._set_player(nx, ny)
            self._clear(x, y)
            return MoveResponse.VALID
        elif self.is_box(nx, ny):
            # nnx, nny is where the box is trying to go
            (nnx, nny) = (nx+dx, ny+dy)
            if self.is_empty(nnx, nny):
                self._set_box(nnx, nny)
                self._set_player(nx, ny)
                self._clear(x, y)
                return MoveResponse.VALID
            else:
                return MoveResponse.INVALID_BOX
        else:
            return MoveResponse.INVALID_WALL

    def width(self):
        return len(self.board[0])

    def height(self):
        return len(self.board)

    def symbol(self, x, y):
        return self.board[y][x]
