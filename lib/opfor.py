# Copyright (c) 2013 Markus Martin <markus@archwyrm.net>. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

"""The opposing forces"""

import pygame

import entity

class Alien(entity.Character):
    type = "Alien"

    def __init__(self, position):
        super(Alien, self).__init__(position)
        self.color = pygame.Color(0,0,255)
