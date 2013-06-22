
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

class Bomb(Gameobject):
    ""
    def __init__(self, xx,yy):
        Gameobject.__init__(self,xx,yy)
        self.w = 16 
        self.h = 16 
        self.image = pygame.image.load('./pics/bomb1-16x16.bmp').convert()
        self.image.set_colorkey((0,0,0)) 
   	self.counter = 0 


    def update(self,room):
	self.counter += 1
	j = 0
	if (self.counter > 50):
	    for i in room.gameobjects:
		if (i == self):
		    l = 0
		    for k in room.gameobjects: 
			if i != k and k and k.collideobjectXY(room):
			    room.gameobjects[l] = None
			l += 1    	
		    room.gameobjects[j] = None 
		    return
	    	j += 1 
