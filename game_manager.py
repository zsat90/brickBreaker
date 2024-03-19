from game_functions.sound import game_over_sound


class GameManager:
    def __init__(self, initial_lives, ball, paddle, bricks):
        self.lives = initial_lives
        self.ball = ball
        self.paddle = paddle
        self.bricks = bricks
        self.is_game_over = False
        self.is_game_won = False

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over()
        else:
            self.reset_ball()

    def game_over(self):
        self.is_game_over = True
        game_over_sound.play()

    def reset_ball(self):
        # Reset ball to its initial position
        self.ball.reset_position()

    def check_win(self):
        if not self.bricks:
            self.is_game_won = True
            self.is_game_over = True
