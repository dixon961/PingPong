import pygame
import utils
import player


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Ping Pong')

player_one = player.Player(0, WINDOW_HEIGHT / 2 - 32, 'player.png')
player_two = player.Player(WINDOW_WIDTH - 16, WINDOW_HEIGHT / 2 - 32, 'player.png')
ball = player.Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 'ball.png')
ball.x_direction = -1
ball.y_direction = -0.5
center_img = pygame.image.load('center.png')
center_img.set_colorkey((0, 0, 0))

screen = pygame.Surface((600, 400))
screen.fill((50, 50, 50))

playing = True

while playing:
    ev = pygame.event.get()
    if utils.check_keyboard(ev) == 'EXIT':
        playing = False
    elif utils.check_keyboard(ev) == 'PLAY':
        print('Enter')
    elif utils.check_keyboard(ev) == 'P1_UP':
        player_one.y_direction = -1
    elif utils.check_keyboard(ev) == 'P1_DOWN':
        player_one.y_direction = 1
    elif utils.check_keyboard(ev) == 'P2_UP':
        print('Player 2 goes UP')
    elif utils.check_keyboard(ev) == 'P2_DOWN':
        print('Player 2 goes DOWN')

    player_one.update()
    player_two.update()
    ball.update()

    if ball.rect.colliderect(player_two) and ball.x <= player_two.x:
        ball.x_direction *= -1
        #ball.y_direction *= -1
    elif ball.rect.colliderect(player_one) and ball.x >= player_one.x:
        ball.x_direction *= -1
        #ball.y_direction *= -1

    if ball.y <= 0:
        ball.y_direction *= -1
    elif ball.y >= WINDOW_HEIGHT - ball.rect.height:
        ball.y_direction *= -1

    player_one.y = ball.y - player_one.rect.height / 2
    player_two.y = ball.y - player_two.rect.height / 2

    if player_one.y <= 0:
        player_one.y = 0
    elif player_one.y >= WINDOW_HEIGHT - player_one.rect.height:
        player_one.y = WINDOW_HEIGHT - player_one.rect.height

    if player_two.y <= 0:
        player_two.y = 0
    elif player_two.y >= WINDOW_HEIGHT - player_two.rect.height:
        player_two.y = WINDOW_HEIGHT - player_two.rect.height

    window.blit(screen, (0, 0))
    window.blit(center_img, (WINDOW_WIDTH / 2, 5))
    window.blit(player_one.sprite, (player_one.x, player_one.y))
    window.blit(player_two.sprite, (player_two.x, player_two.y))
    window.blit(ball.sprite, (ball.x, ball.y))
    pygame.display.flip()
