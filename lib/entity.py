import copy
import math
import pygame

import world

class Entity(object):
    type = "Entity"

    def __init__(self, position):
        self.position = position
        self.bb = (20, 20) # Bounding box

    def update(self):
        pass

    def draw(self, surf):
        pass

class Character(Entity):
    type = "Character"

    def __init__(self, position):
        super(Character, self).__init__(position)
        self.bb = (20, 20) # Bounding box

        self.speed = 5 # Max speed
        self.velocity = [0, 0] # Current given frame velocity
        self.move_velocity = 0 # Movement velocity
        self.on_ground = False

        self.facing = 1 # Entity's facing direction, positive == right
        self.color = pygame.Color(255,255,255)

    def update(self):
        self.position[0] += self.velocity[0] + self.move_velocity
        self.position[1] += self.velocity[1] + world.GRAVITY
        self.move_velocity -= world.AIR_RESISTANCE * math.copysign(1, self.move_velocity)
        if self.on_ground:
            self.move_velocity = 0

    def draw(self, surf):
        color = copy.deepcopy(self.color)
        if self.on_ground:
            color[1] = 150
        pygame.draw.rect(surf, color, tuple(self.position) + self.bb, 2)

    def move_left(self):
        self.move(-1 * self.speed)
        self.facing = -1

    def move_right(self):
        self.move(self.speed)
        self.facing = 1

    def move(self, speed):
        if self.on_ground:
            self.move_velocity += speed

class Projectile(Entity):
    type = "Projectile"

    def __init__(self, position, velocity):
        super(Projectile, self).__init__(position)
        self.position = position
        self.velocity = velocity

    def draw(self, surf):
        pos = (int(self.position[0]), int(self.position[1]))
        pygame.draw.circle(surf, pygame.Color("white"), pos, 2)

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
