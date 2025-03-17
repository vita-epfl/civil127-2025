import pygame
from sokoban_model import Symbol

# Define the mapping of board symbols to svg files
symbolFileMapping = {
    Symbol.BOX: "./assets/box.png",
    Symbol.BOX_ON_GOAL: "./assets/box-on-goal.png",
    Symbol.PLAYER:  "./assets/player.png",
    Symbol.WALL: "./assets/wall.png",
    Symbol.GOAL: "./assets/goal.png",
}


class SokobanView:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size

        # load SVG graphics
        self.surface = {}
        for s in symbolFileMapping:
            svg = pygame.image.load(symbolFileMapping[s])
            self.surface[s] = pygame.transform.smoothscale(svg, (size, size))

    def print(self, model):
        self.screen.fill((255, 255, 255))  # clear screen with white background

        # Draw walls
        for (x, y) in model.walls:
            self.screen.blit(
                self.surface[Symbol.WALL], (x * self.size, y * self.size))

        # Draw boxes and goals
        for (x, y) in model.boxes.union(model.goals):
            if (x, y) in model.boxes and (x, y) in model.goals:
                self.screen.blit(
                    self.surface[Symbol.BOX_ON_GOAL], (x * self.size, y * self.size))
            elif (x, y) in model.boxes:
                self.screen.blit(
                    self.surface[Symbol.BOX], (x * self.size, y * self.size))
            else:
                self.screen.blit(
                    self.surface[Symbol.GOAL], (x * self.size, y * self.size))

        # Draw player
        (x, y) = model.player
        self.screen.blit(self.surface[Symbol.PLAYER],
                         (x * self.size, y * self.size))

        # Tell pygame we are done drawing
        pygame.display.flip()

    def winning_message(self):
        font = pygame.font.Font(None, 36)
        text = font.render("You Won!", True, (255, 215, 0))
        textRect = text.get_rect()
        textRect.center = self.screen.get_rect().center
        self.screen.blit(text, textRect)
        pygame.display.flip()
        pygame.time.wait(3000)