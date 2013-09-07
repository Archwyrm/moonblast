from world import World
from player import Player
from opfor import Alien
from input import Controller
import ctx

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
    global world, player
    world = ctx.world
    player = Player([340,300])
    alien = Alien([600,300])

    world.add_player(player)
    world.add_entity(alien)
    controller = Controller(player)

    while True:
        handle_events(controller)
        controller.update()
        world.update()

        # Draw
        window.fill(pygame.Color(0,0,0))
        world.draw(window)
        pygame.display.update()
        clock.tick(30)

def init_sound():
    # TODO: os.path.join('data', 'foo.ogg')
    ctx.sounds['shoot'] = pygame.mixer.Sound('data/hit.wav')
    pygame.mixer.music.load('data/DST-RailJet-LongSeamlessLoop.ogg')
    pygame.mixer.music.play(-1)

def main():
    init_gfx()
    init_sound()
    game_loop()
