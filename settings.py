import pygame

pygame.init()

# Game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Brick Breaker')

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (242, 10, 10)
GREEN = (6, 143, 15)

# background image
background_img_path = 'assets/background.jpg'
background_img = pygame.image.load(background_img_path).convert()
