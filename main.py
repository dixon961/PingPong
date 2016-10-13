import pygame

window = pygame.display.set_mode((300, 200))
pygame.display.set_caption('Hello Game!')

screen = pygame.Surface((300,200))

done = True

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((50,50,50))

    window.blit(screen, (0,0))
    pygame.display.flip()