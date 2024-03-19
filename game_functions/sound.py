import pygame

pygame.mixer.init()

brick_collision_sound = pygame.mixer.Sound('assets/brick-broken.wav')
paddle_collision_sound = pygame.mixer.Sound('assets/paddle.wav')
game_over_sound = pygame.mixer.Sound('assets/game-over.wav')

brick_collision_sound.set_volume(0.8)
paddle_collision_sound.set_volume(0.8)
game_over_sound.set_volume(0.8)


