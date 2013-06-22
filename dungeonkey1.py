
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
from stateimagelibrary import *
import random

class Dungeonkey1(Gameobject):
    "Darknut"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 36
        self.h = 36
	self.stimlib = Stateimagelibrary()		
        image = pygame.image.load('./pics/dungeonkey1-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
	

    def draw(self, screen, room):
        self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)
	
	     
    def update(self,room):
	1

    def pickup(self, room):
        room.removeobject(self)
	return 3

    def collide(self, room, player):
	    return 0

        
