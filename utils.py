import pygame


def check_keyboard(event):
    for e in event:
        if e.type == pygame.QUIT:
            return 'EXIT'
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                return 'EXIT'
            elif e.key == pygame.K_RETURN:
                return 'PLAY'
            elif e.key == pygame.K_w:
                return 'P1_UP'
            elif e.key == pygame.K_s:
                return 'P1_DOWN'
            elif e.key == pygame.K_UP:
                return 'P2_UP'
            elif e.key == pygame.K_DOWN:
                return 'P2_DOWN'
