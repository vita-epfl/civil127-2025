from sokoban_model import MoveResponse, SokobanModel
from sokoban_view import SokobanView


class SokobanController:
    def __init__(self, xsb_file):
        with open(xsb_file, "r") as f:
            self.model = SokobanModel(list(f))
        self.view = SokobanView()

    def game_loop(self):
        move_response = MoveResponse.VALID
        while True:
            if move_response == MoveResponse.VALID:
                self.view.print(self.model)
            elif move_response == MoveResponse.DONE:
                self.view.print(self.model)
                break
            else:
                print(move_response.value)
            player_movement = input("enter move (w, a, s, d):")
            match player_movement:
                case 'w':
                    move_response = self.model.move(0, -1)
                case 'a':
                    move_response = self.model.move(-1, 0)
                case 's':
                    move_response = self.model.move(0, 1)
                case 'd':
                    move_response = self.model.move(1, 0)
