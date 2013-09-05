import pygame

class Player:
    def __init__(self):
        self.position = [340,300]
        self.bb = (20, 20) # Bounding box
        self.speed = 5

    def draw(self, surf):
        pygame.draw.rect(surf, pygame.Color(255,0,0), tuple(self.position) + self.bb)

    def move_left(self):
        self.position[0] -= self.speed

    def move_right(self):
        self.position[0] += self.speed
