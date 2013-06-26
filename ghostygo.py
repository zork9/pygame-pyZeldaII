
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
from commongo import *
from stateimagelibrary import *

class GhostyGO(CommonGO):
    "Game object"
    def __init__(self, xx,yy):
	CommonGO.__init__(self,xx,yy)	

	self.x = xx 
        self.y = yy
	# default width and height 
        self.w = 24 
        self.h = 24
#####	self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/ghosty-left-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/ghosty-right-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        self.hitpoints = 1000000000
        # NOTE : decrease 1 hitpoint with default sword
        self.hitf = self.hit1

    def update(self,room,player):
	r = randint(0,30)
	if r >= 10 and self.x > player.x + room.relativex:
		self.direction = "west"	
	elif r >= 10 and self.x < player.x + room.relativex:
		self.direction = "east"	
	elif r >= 10 and self.y > player.y + room.relativey:
		self.direction = "north"	
	elif r >= 10 and self.y < player.y + room.relativey:
		self.direction = "south"	
	if self.direction == "west":
		self.x -= 5
	elif self.direction == "east":
		self.x += 5
	elif self.direction == "north":
		self.y -= 5
	elif self.direction == "south":
		self.y -= 5

    def draw(self, screen, room):
        self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)    
        
