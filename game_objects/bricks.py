import pygame
from settings import screen, BLACK


class Brick:
    def __init__(self, x, y):
        self.width = 75
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect)
