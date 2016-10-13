import pygame
import player
import ball

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


def keyboard():
    global playing
    global player_one_directions
    global player_two_directions
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                playing = False
            elif e.key == pygame.K_RETURN:
                pass
            elif e.key == pygame.K_w:
                player_one_directions['up'] = True
            elif e.key == pygame.K_s:
                player_one_directions['down'] = True
            elif e.key == pygame.K_UP:
                player_two_directions['up'] = True
            elif e.key == pygame.K_DOWN:
                player_two_directions['down'] = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                player_one_directions['up'] = False
            elif e.key == pygame.K_s:
                player_one_directions['down'] = False
            elif e.key == pygame.K_UP:
                player_two_directions['up'] = False
            elif e.key == pygame.K_DOWN:
                player_two_directions['down'] = False


def controls():
    global player_one_directions
    global player_two_directions
    global player_one
    global player_two
    if player_one_directions['up']:
        player_one.y_direction = -1
    if player_one_directions['down']:
        player_one.y_direction = 1
    if not(player_one_directions['up'] or player_one_directions['down']):
        player_one.y_direction = 0
    if player_one_directions['up'] and player_one_directions['down']:
        player_one.y_direction = 0

    if player_two_directions['up']:
        player_two.y_direction = -1
    if player_two_directions['down']:
        player_two.y_direction = 1
    if not(player_two_directions['up'] or player_two_directions['down']):
        player_two.y_direction = 0
    if player_two_directions['up'] and player_two_directions['down']:
        player_two.y_direction = 0


def self_play():
    player_one.y = ball.y - player_one.rect.height / 2
    player_two.y = ball.y - player_two.rect.height / 2


while playing:
    keyboard()
    controls()
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
