import pygame
import player
import ball
import utils

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Ping Pong')

player_one = player.Player(0, WINDOW_HEIGHT / 2 - 32, 'player.png')
player_two = player.Player(WINDOW_WIDTH - 16, WINDOW_HEIGHT / 2 - 32, 'player.png')
ball = ball.Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 'ball.png')
ball.x_direction = -1
ball.y_direction = -0.5
center_img = pygame.image.load('center.png')
center_img.set_colorkey((0, 0, 0))

p_one_count = 0
p_two_count = 0

screen = pygame.Surface((600, 400))
screen.fill((50, 50, 50))

playing = True

player_one_directions = {'up': False, 'down': False}
player_two_directions = {'up': False, 'down': False}

while playing:
    playing = utils.keyboard(player_one_directions, player_two_directions)
    utils.controls(player_one_directions, player_two_directions, player_one, player_two)
    player_one.update()
    player_two.update()
    ball.update()

    if ball.rect.colliderect(player_two) and ball.x <= player_two.x:
        ball.x_direction *= -1
    elif ball.rect.colliderect(player_one) and ball.x >= player_one.x:
        ball.x_direction *= -1

    window.blit(screen, (0, 0))
    window.blit(center_img, (WINDOW_WIDTH / 2, 5))
    window.blit(player_one.sprite, (player_one.x, player_one.y))
    window.blit(player_two.sprite, (player_two.x, player_two.y))
    window.blit(ball.sprite, (ball.x, ball.y))
    pygame.display.flip()
