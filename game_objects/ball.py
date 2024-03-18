import pygame
from settings import screen, screen_width, screen_height, BLACK


class Ball:
    def __init__(self):
        self.radius = 10
        self.x = screen_width / 2
        self.y = screen_height - 40 - self.radius
        self.speed_x = 4
        self.speed_y = -4

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # Bounce off the left and right walls
        if self.x <= 0 or self.x >= screen_width:
            self.speed_x *= -1
        # Bounce off the top wall
        if self.y <= 0:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius)
