from entity import Character, Projectile
from ctx import world, sounds

import pygame

class Player(Character):
    type = "Player"

    def __init__(self, position):
        super(Player, self).__init__(position)
        self.color = pygame.Color(255,0,0)

    def shoot(self):
        pos = [self.position[0] + self.bb[0] / 2, self.position[1] + self.bb[1] / 2]
        world.add_entity(Projectile(pos, [10 * self.facing,0]))
        sounds['shoot'].play()
