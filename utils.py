import pygame


def keyboard(dir_one, dir_two):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            return False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                return False
            elif e.key == pygame.K_RETURN:
                pass
            elif e.key == pygame.K_w:
                dir_one['up'] = True
            elif e.key == pygame.K_s:
                dir_one['down'] = True
            elif e.key == pygame.K_UP:
                dir_two['up'] = True
            elif e.key == pygame.K_DOWN:
                dir_two['down'] = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                dir_one['up'] = False
            elif e.key == pygame.K_s:
                dir_one['down'] = False
            elif e.key == pygame.K_UP:
                dir_two['up'] = False
            elif e.key == pygame.K_DOWN:
                dir_two['down'] = False
    return True


def controls(o_dir, t_dir, o, t):
    if o_dir['up']:
        o.y_direction = -1
    if o_dir['down']:
        o.y_direction = 1
    if not(o_dir['up'] or o_dir['down']):
        o.y_direction = 0
    if o_dir['up'] and o_dir['down']:
        o.y_direction = 0

    if t_dir['up']:
        t.y_direction = -1
    if t_dir['down']:
        t.y_direction = 1
    if not(t_dir['up'] or t_dir['down']):
        t.y_direction = 0
    if t_dir['up'] and t_dir['down']:
        t.y_direction = 0
