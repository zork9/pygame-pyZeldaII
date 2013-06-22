
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

class BlackKnightStanding(Gameobject):
    "BlackKnight"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 36
        self.h = 36 
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/darknut1-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/darknut2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
	self.direction = "left"

    def draw(self, screen, room):
	if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,room):
	if (random.randint(0,100) == 0 and self.direction == "left"):
	   self.direction = "right"
	elif (random.randint(0,100) == 0 and self.direction == "right"):
	   self.direction = "left"
 
	if (self.direction == "left" and self.collide(room,self)):
	    self.x -= 1 
	elif (self.direction == "right" and self.collide(room,self)):
	    self.x += 1 

