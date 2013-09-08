# Copyright (c) 2013 Markus Martin <markus@archwyrm.net>. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

import pygame
from pygame.locals import *

class Controller(object):
    """Associates input events with a player entity."""

    def __init__(self, player):
        self.player = player
        self.keys_down = list()

        self.bindings = {
            K_LEFT : player.move_left,
            K_RIGHT : player.move_right,
            K_LALT : player.shoot,
        }

    def update(self):
        for key in self.keys_down:
            self.bindings[key]()

    def key_down(self, event):
        """Handles a key down event. Returns true if handled, false if not."""
        if event.key in self.bindings:
            self.keys_down.append(event.key)
            return True
        else:
            return False

    def key_up(self, event):
        """Handles a key up event. Returns true if handled, false if not."""
        if event.key in self.bindings:
            self.keys_down.remove(event.key)
            return True
        else:
            return False
