from game_functions.sound import brick_collision_sound, paddle_collision_sound


def ball_paddle_collision(ball, paddle):
    """Handle collisions between the ball and the paddle."""
    if ball.rect.colliderect(paddle.rect):
        # plays paddle collision sound
        paddle_collision_sound.play()
        # Invert the vertical direction of the ball
        ball.speed_y *= -1


def ball_brick_collision(ball, bricks, game_manager):
    """Handle collisions between the ball and bricks."""
    for brick in bricks:
        if ball.rect.colliderect(brick.rect):
            # Remove the brick from the list
            bricks.remove(brick)
            # play collision sound
            brick_collision_sound.play()
            game_manager.check_win()
            # Change the ball's direction
            ball.speed_y *= -1
            break


def ball_walls_collision(ball, screen_width, screen_height, game_manager):
    """Handle collisions between the ball and the walls."""
    # Left and right walls
    if ball.rect.left <= 0 or ball.rect.right >= screen_width:
        ball.speed_x *= -1
    # Top wall
    if ball.rect.top <= 0:
        ball.speed_y *= -1
    # Bottom wall
    if ball.rect.bottom >= screen_height:
        ball.speed_y *= -1
        game_manager.lose_life()
