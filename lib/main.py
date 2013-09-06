from world import World
from player import Player

import pygame
from pygame.locals import *
import sys

def init_gfx():
    global window, clock

    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Moon Blasters')

def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()
            elif event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == K_c:
                world.checked = False
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                player.position[0], player.position[1] = event.pos[0], event.pos[1]
                world.checked = False

def game_loop():
    global world, player
    world = World()
    player = Player()

    while True:
        handle_events()
        world.update(player)
        world.collide(player)

        # Draw
        window.fill(pygame.Color(0,0,0))
        world.draw(window)
        player.draw(window)
        pygame.display.update()
        clock.tick(30)

def main():
    init_gfx()
    game_loop()
