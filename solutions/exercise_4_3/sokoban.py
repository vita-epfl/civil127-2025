import os
from sokoban_controller import SokobanController

# use os.path.join for portable code (so it works on Mac/Windows/Linux)
path = os.path.join("levels", "level1.xsb")
sokoban = SokobanController(path)
sokoban.game_loop()
