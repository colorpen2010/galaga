import pygame

import model

pygame.key.set_repeat(100)

all_points = [[100, 200], [300, 150], [126, 421]]


def control():
    events = pygame.event.get()
    model.player.control(events)
    for o in model.enemies:
        o.toolgun(events)

    for o in events:
        if o.type == pygame.QUIT:
            exit(9)

        if o.type == pygame.KEYUP and o.key == pygame.K_TAB:
            model.debug = not model.debug
        if o.type == pygame.KEYUP and o.key == pygame.K_q:
            model.paint = not model.paint
        if o.type == pygame.KEYUP and o.key == pygame.K_d:
            model.enemies[0].plavniy_fly(45, True)
        if o.type == pygame.KEYUP and o.key == pygame.K_a:
            model.enemies[0].rovnyi()
        if o.type == pygame.KEYUP and o.key == pygame.K_f:
            model.enemies[0].plavniy_fly(111, False)
        if o.type == pygame.KEYUP and o.key == pygame.K_r:
            model.enemies[0].plavniy_fly(180, False)
        if o.type == pygame.KEYUP and o.key == pygame.K_b:
            model.enemies[0].plavniy_fly_tohcy()

        if o.type == pygame.MOUSEBUTTONUP:
            model.enemies[0].mouse_pointer(o.pos)
