from world import World
from player import Player
from input import Controller

import pygame
from pygame.locals import *
import sys

def init_gfx():
    global window, clock

    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Moon Blasters')

def handle_events(controller):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            else:
                controller.key_down(event)
        elif event.type == KEYUP:
            controller.key_up(event)
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                player.position[0], player.position[1] = event.pos[0], event.pos[1]

def game_loop():
    global player
    world = World()
    player = Player([340,300])
    world.add_player(player)
    controller = Controller(player)

    while True:
        handle_events(controller)
        controller.update()
        world.update(player)

        # Draw
        window.fill(pygame.Color(0,0,0))
        world.draw(window)
        player.draw(window)
        pygame.display.update()
        clock.tick(30)

def main():
    init_gfx()
    game_loop()
