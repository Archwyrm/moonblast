import math
import pygame

import world

class Character:
    def __init__(self, position):
        self.position = position
        self.bb = (20, 20) # Bounding box

        self.speed = 5 # Max speed
        self.velocity = [0, 0] # Current given frame velocity
        self.move_velocity = 0 # Movement velocity
        self.on_ground = False

        self.color = pygame.Color(255,0,0)

    def update(self):
        self.position[0] += self.velocity[0] + self.move_velocity
        self.position[1] += self.velocity[1] + world.GRAVITY
        self.move_velocity -= world.AIR_RESISTANCE * math.copysign(1, self.move_velocity)
        if self.on_ground:
            self.move_velocity = 0

    def draw(self, surf):
        if self.on_ground:
            self.color = pygame.Color(255,255,0)
        else:
            self.color = pygame.Color(255,0,0)
        pygame.draw.rect(surf, self.color, tuple(self.position) + self.bb, 2)

    def move_left(self):
        self.move(-1 * self.speed)

    def move_right(self):
        self.move(self.speed)

    def move(self, speed):
        if self.on_ground:
            self.move_velocity += speed
