
import unittest

from .sokoban_model import MoveResponse, SokobanModel

SIMPLE_LEVEL = """######
#-$-.#
#-$-.#
#-@--#
######""".splitlines()


class TestSokobanModel(unittest.TestCase):
    def test_player_can_move_into_empty_space(self):
        model = SokobanModel(SIMPLE_LEVEL)
        self.assertEqual(model.move(1, 0), MoveResponse.VALID)

    def test_player_cannot_move_into_wall(self):
        model = SokobanModel(SIMPLE_LEVEL)
        self.assertEqual(model.move(0, 1), MoveResponse.INVALID_WALL)

    def test_player_can_move_box_into_empty_space(self):
        model = SokobanModel(SIMPLE_LEVEL)
        self.assertEqual(model.move(1, 0), MoveResponse.VALID)
        self.assertEqual(model.move(0, -1), MoveResponse.VALID)
        self.assertEqual(model.move(-1, 0), MoveResponse.VALID)

    def test_player_cannot_move_box_into_box(self):
        model = SokobanModel(SIMPLE_LEVEL)
        self.assertEqual(model.move(0, -1), MoveResponse.INVALID_BOX)

    def test_player_cannot_move_box_into_wall(self):
        model = SokobanModel(SIMPLE_LEVEL)
        self.assertEqual(model.move(1, 0), MoveResponse.VALID)
        self.assertEqual(model.move(0, -1), MoveResponse.VALID)
        self.assertEqual(model.move(-1, 0), MoveResponse.VALID)
        self.assertEqual(model.move(-1, 0), MoveResponse.INVALID_BOX)

if __name__ == "__main__":
    unittest.main()
