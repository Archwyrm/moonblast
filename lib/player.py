from entity import Character

import pygame

class Player(Character):
    def __init__(self, position):
        super(Player, self).__init__(position)
        self.color = pygame.Color(255,0,0)
