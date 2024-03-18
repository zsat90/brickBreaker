import pygame
from settings import screen, screen_width, screen_height, WHITE


class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = (screen_width - self.width) / 2
        self.y = screen_height - self.height - 30
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        if direction == "right" and self.rect.right < screen_width:
            self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
