import pygame
from settings import screen, screen_width, screen_height, WHITE


class Ball:
    def __init__(self):
        self.radius = 10
        self.x = screen_width / 2
        self.y = screen_height - 40 - self.radius
        self.speed_x = 4
        self.speed_y = -4
        self.start_x = self.x
        self.start_y = self.y

    @property
    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)
