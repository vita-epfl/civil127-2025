from sokoban_model import MoveResponse, SokobanModel
from sokoban_view import SokobanView
import pygame


class SokobanController:
    def __init__(self, xsb_file):
        # Initialize model first, so we know how large to make the window
        with open(xsb_file, "r") as f:
            self.model = SokobanModel(list(f))

        # Initialize pygame, calculate optimal size
        pygame.init()
        self.clock = pygame.time.Clock()
        w, h = pygame.display.get_desktop_sizes()[0]
        s1 = w // self.model.width()
        s2 = h // self.model.height()
        size = max(min(s1, s2, 100), 1)
        canvas = pygame.display.set_mode(
            (self.model.width() * size, self.model.height() * size))
        pygame.display.set_caption("Sokoban")

        self.view = SokobanView(canvas, size)

    def game_loop(self):
        move_response = MoveResponse.VALID
        self.view.print(self.model)
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            move_response = self.model.move(-1, 0)
                        case pygame.K_RIGHT:
                            move_response = self.model.move(1, 0)
                        case pygame.K_UP:
                            move_response = self.model.move(0, -1)
                        case pygame.K_DOWN:
                            move_response = self.model.move(0, 1)

                    if move_response == MoveResponse.VALID:
                        self.view.print(self.model)
                    elif move_response == MoveResponse.DONE:
                        self.view.print(self.model)
                        self.view.display_message("You Won!", (255, 215, 0), wait_time=3000)
                        return
                    else:
                        self.view.display_message("Invalid Move", (139, 0, 0))
