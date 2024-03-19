import pygame
import random
from settings import screen, RED, screen_width, screen_height


def create_bricks():
    bricks = []
    # Standard brick size
    brick_width = 60
    brick_height = 25
    # Spacing between bricks to create visible gaps
    gap = 5
    # Calculate how many bricks can fit in a row, accounting for gaps
    bricks_per_row = screen_width // (brick_width + gap)

    # Maximum number of rows that will fit in the upper quarter of the screen
    max_rows = (screen_height // 4) // (brick_height + gap)
    # Chance of a position being left empty to create a "hole"
    hole_probability = 0.3

    for row in range(max_rows):
        for col in range(bricks_per_row):
            if random.random() < hole_probability:
                continue
            # Calculate the x and y position for the current brick
            x = col * (brick_width + gap)
            y = row * (brick_height + gap) + 50  # Starting 50 pixels down from the top
            # Add a new brick to the list
            bricks.append(Brick(x, y, brick_width, brick_height))

    return bricks


class Brick:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = RED

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

