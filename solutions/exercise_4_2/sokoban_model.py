from enum import Enum


class Symbol(Enum):
    """
    Symbols that may appear in the level file
    """

    BOX = "$"
    BOX_ON_GOAL = "*"
    PLAYER = "@"
    PLAYER_ON_GOAL = "+"
    GOAL = "."
    WALL = "#"
    FLOOR = "-"


class MoveResponse(Enum):
    INVALID_WALL = "can't push walls"
    INVALID_BOX = "can't push this box"
    VALID = "valid"
    DONE = "success"


class SokobanModel:
    def __init__(self, level_data):
        """ level_data is a list of strings"""

        # Keeping the board the way we did in labs 1 and 2 makes implementing
        # movement painful (we have to keep track of goals and restore them).
        # We could just keep the goals in a different datastructure. Storing
        # each type of wall/box/goal in their own datastructure however makes
        # things easier.
        #
        # We'll use sets. A set is like a dictionnary with only keys. Sets
        # also have various operators (union, difference, etc.) but we
        # won't use any of those here.
        #
        # Since we are refactoring our code from lab 1 and 2, we are going
        # to drop code we no longer need.
        self.walls = set()
        self.boxes = set()
        self.goals = set()

        # We'll assume the level data is well formed (all lines are the
        # same length).
        self.size = [len(level_data[0].strip()), len(level_data)]

        for y, row in enumerate(level_data):
            for x, symbol in enumerate(row.strip()):
                pos = (x, y)
                match symbol:
                    case Symbol.BOX.value:
                        self.boxes.add(pos)
                    case Symbol.BOX_ON_GOAL.value:
                        self.boxes.add(pos)
                        self.goals.add(pos)
                    case Symbol.PLAYER.value:
                        self.player = pos
                    case Symbol.PLAYER_ON_GOAL.value:
                        self.player = pos
                        self.goals.add(pos)
                    case Symbol.GOAL.value:
                        self.goals.add(pos)
                    case Symbol.WALL.value:
                        self.walls.add(pos)
                    # Anything that's not a goal/player/box/wall is implied to
                    # be a floor. We don't keep track of floors.

    def is_empty(self, x, y):
        pos = (x, y)
        # return pos not in self.walls | self.boxes would be short to write
        # but somewhat harder to read
        if pos in self.walls | self.boxes:
            return False
        return True

    def move(self, dx, dy):
        (x, y) = self.player
        (nx, ny) = (x + dx, y + dy)  # nx, ny are where the player is trying to go
        if self.is_empty(nx, ny):
            self.player = (nx, ny)
            return MoveResponse.VALID
        elif (nx, ny) in self.boxes:
            # nnx, nny are where the box is trying to go
            (nnx, nny) = (nx+dx, ny+dy)
            if self.is_empty(nnx, nny):
                self.boxes.remove((nx, ny))
                self.boxes.add((nnx, nny))
                self.player = (nx, ny)

                # check if we are done using set.issubset. We only need to check
                # if we are done after we moved a box
                if self.goals <= self.boxes:
                    return MoveResponse.DONE
                return MoveResponse.VALID
            else:
                return MoveResponse.INVALID_BOX
        else:
            return MoveResponse.INVALID_WALL

    def width(self):
        return self.size[0]

    def height(self):
        return self.size[1]

    def symbol(self, x, y):
        pos = (x, y)
        if pos in self.goals:
            if pos in self.boxes:
                return Symbol.BOX_ON_GOAL
            if pos == self.player:
                return Symbol.PLAYER_ON_GOAL
            return Symbol.GOAL
        if pos in self.boxes:
            return Symbol.BOX
        if pos == self.player:
            return Symbol.PLAYER
        if pos in self.walls:
            return Symbol.WALL
        return Symbol.FLOOR
