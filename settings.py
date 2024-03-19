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


def display_game_over_screen():
    font_size = 30
    font = pygame.font.SysFont('arial', font_size)

    screen.fill(BLACK)  # Clear the screen or choose a background
    game_over_text = font.render("GAME OVER", True, WHITE)
    # try_again_text = font.render("Press R to Try Again", True, WHITE)
    # quit_text = font.render("Press Q to Quit", True, WHITE)

    # Calculate positions for the texts
    game_over_pos = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2 - 30))
    # try_again_pos = try_again_text.get_rect(center=(screen_width / 2, screen_height / 2))
    # quit_pos = quit_text.get_rect(center=(screen_width / 2, screen_height / 2 + 30))

    # Blit the texts to the screen
    screen.blit(game_over_text, game_over_pos)
    # screen.blit(try_again_text, try_again_pos)
    # screen.blit(quit_text, quit_pos)

    pygame.display.flip()  # Update the screen
