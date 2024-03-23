# Create instances
import pygame as pygame

from game_functions.collisions import ball_walls_collision, ball_paddle_collision, ball_brick_collision
from game_manager import GameManager
from game_objects.ball import Ball
from game_objects.bricks import create_bricks
from game_objects.paddle import Paddle
from settings import screen, WHITE, background_img, screen_height, screen_width

font_size = 30
font = pygame.font.SysFont('arial', font_size)

paddle = Paddle()
ball = Ball()
bricks = create_bricks()
game_manager = GameManager(3, ball=ball, paddle=paddle, bricks=bricks)


def display_end_game_message(game_won=False):
    screen.fill((0, 0, 0))  # Clear the screen
    message = "You've won the game! Press R to Restart or Q to Quit" if game_won else "Game Over. " \
                                                                                      "Try again? " \
                                                                                      "Press R to " \
                                                                                      "Restart or Q " \
                                                                                      "to Quit "
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Wait for player input
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'restart'
                elif event.key == pygame.K_q:
                    return 'quit'


def reset_game():
    global paddle, ball, bricks, game_manager
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()
    game_manager = GameManager(3, ball=ball, paddle=paddle, bricks=bricks)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_manager.is_game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move("left")
        if keys[pygame.K_RIGHT]:
            paddle.move("right")

        ball.move()

        ball_walls_collision(ball, screen_width, screen_height, game_manager)
        ball_paddle_collision(ball, paddle)
        ball_brick_collision(ball, bricks, game_manager)

        screen.blit(background_img, (0, 0))
        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()

        lives_text = f'Lives: {game_manager.lives}'
        text_surface = font.render(lives_text, True, WHITE)
        screen.blit(text_surface, (10, 10))
    else:
        if game_manager.is_game_won:
            action = display_end_game_message(game_won=True)
        else:
            action = display_end_game_message(game_won=False)

        if action == 'quit':
            running = False
        elif action == 'restart':
            reset_game()
            game_manager.is_game_over = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
