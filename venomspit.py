
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
from time import *

class Venomspit(Gameobject):
    "Venom spit"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 24
        self.h = 24 
	self.stimlib = Stateimagelibrary()
        image = pygame.image.load('./pics/venomspit-24x24.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)		

	self.direction = "down"

    def draw(self, screen, room):
        self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)
		    
	     
    def update(self,room):
        sleep(.01) # FIX venom spit sleep
        if (self.direction == "down"):
	        self.y +=5
	if self.y > self.SCREENH:
            room.removeobject(self)

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with Venom spit!"
	    if player.hit():
		return 1 
	    else:
	    	return 2 
	else:
	    return 0

		 
