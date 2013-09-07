"""The opposing forces"""

import pygame

import entity

class Alien(entity.Character):
    def __init__(self, position):
        super(Alien, self).__init__(position)
        self.color = pygame.Color(0,0,255)
