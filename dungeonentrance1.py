
# Copyright (C) Johan Ceuppens 2010
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from gameobject import *

class Dungeonentrance1(Gameobject):
    "Dungeon entrance 1"
    def __init__(self, xx,yy):
	Gameobject.__init__(self,xx,yy)	
	self.w = 200 
        self.h = 100 
        self.image = pygame.image.load('./pics/dungeon-entrance1-200x100.bmp').convert()
        self.image.set_colorkey((0,0,0)) 


