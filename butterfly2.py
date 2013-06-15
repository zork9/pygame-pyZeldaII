
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

class Butterfly2(Gameobject):
    ""
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 16
        self.h = 16 
	self.stimlib = Stateimagelibrary()
        image = pygame.image.load('./pics/butterfly1-16x16.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/butterfly2-16x16.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/butterfly3-16x16.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/butterfly4-16x16.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)

	self.direction = "left"

    def draw(self, screen, room):
        self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)    
	     
    def update(self,room):
        sleep(.005)
##        self.x-=1

        r = random.randint(0,4)
	if (r == 0):
	   self.direction = "right"
        if (r == 1):
	   self.direction = "left"
        if (r == 2):
	   self.direction = "up"
	if (r == 3):
	   self.direction = "down"

	if (not self.collideobjectX(room)): 
	    if (self.direction == "left"):
	        self.x +=2
	        self.direction = "right" 
	    elif (self.direction == "right"):
	        self.x -=2
	        self.direction = "left"

	if (not self.collideobjectY(room)): 
	    if (self.direction == "up"):
	        self.x +=2
	        self.direction = "down" 
	    elif (self.direction == "down"):
	        self.x -=2
	        self.direction = "up"


	if (self.direction == "left"):
	        self.x -=1 
	elif (self.direction == "right"):
	        self.x +=1
	elif (self.direction == "down"):
	        self.y +=1
	elif (self.direction == "up"):
	        self.y -=1
	        

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with Butterfly!"
	return 0

		 
